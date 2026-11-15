"""Owner-checked Applications controller; no Gradio imports or generated execution."""

import atexit
import functools
import json
import logging
import os
import threading
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from agentix.storage.locations import data_directory
from typing import Any

from agentix.application.app_invocation import check_dependencies
from agentix.storage.application_catalog import ApprovedToolRegistry, CatalogDependencyError
from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor, Candidate
from agentix.application.app_review import ApplicationReview
from agentix.storage.installed_apps import InstalledApps
from agentix.lab.application_artifacts import approve_application
from agentix.storage.widget_store import WidgetStore
from agentix.ui.application_presentation import generated_application_frame
from agentix.controllers.sessions import SessionRegistry

logger = logging.getLogger(__name__)


class _StreamRejected(Exception):
    """Carry a precondition result out of a lock before yielding to Gradio."""

    def __init__(self, row: tuple) -> None:
        """Retain only the maintained response tuple, without private source data."""
        super().__init__("Application operation rejected")
        self.row = row


def _safe_stream(method):
    """Release lexical locks before suspending a rejected streaming callback."""

    @functools.wraps(method)
    def stream(*args, **kwargs):
        """Preserve callback metadata and return a safe precondition result."""
        try:
            yield from method(*args, **kwargs)
        except _StreamRejected as error:
            yield error.row

    return stream


@dataclass
class ApplicationState:
    """One browser's proposal and preview, bound to a verified Tools session."""

    token: str
    controller: Any
    candidate: Candidate | None = None
    cancelled: bool = False
    held_slot: bool = False
    repairs: int = 0
    repair_allowed: bool = False
    unsaved_file: str | None = None


class ApplicationsBackend:
    """Coordinate owner, model, review and preview lifecycle independently of UI."""

    def __init__(
        self,
        sessions: SessionRegistry,
        *,
        pipeline_factory: Any = ApplicationPipeline,
        supervisor: Any = None,
        parent_port: int | None = None,
        registry_factory: Any = ApprovedToolRegistry.for_controller,
        library_factory: Any = InstalledApps.for_user,
    ) -> None:
        """Inject storage/execution factories; construction starts no model or server."""
        self.sessions, self.pipeline_factory = sessions, pipeline_factory
        self.registry_factory = registry_factory
        self.library_factory = library_factory
        self.supervisor = supervisor or ApplicationSupervisor()
        self.origin = "http://127.0.0.1:" + str(
            parent_port or int(os.environ.get("AGENTIX_SERVER_PORT", "7877"))
        )
        self.states: dict[str, ApplicationState] = {}
        self.lock = threading.RLock()
        self.preview_slots = threading.BoundedSemaphore(2)
        atexit.register(self.close_all)

    def _resolve(self, token: str | None, request: Any) -> tuple[Any, ApplicationState]:
        """Verify token/owner before touching a candidate or model boundary."""
        owner = getattr(request, "session_hash", None)
        session = self.sessions.resolve(token, owner)
        with self.lock:
            state = self.states.get(owner)
            if state is not None and state.token != session.token:
                self._close(state)
                state = None
            if state is None:
                state = ApplicationState(session.token, session.controller)
                self.states[owner] = state
                session.controller.application_cleanup = lambda: self.close_owner(owner)
            return session, state

    def _close(self, state: ApplicationState) -> None:
        """Cancel publication and close only this browser's owned preview."""
        state.cancelled = True
        state.unsaved_file = None
        if state.candidate is not None:
            state.candidate.close()
        if state.held_slot:
            self.preview_slots.release()
            state.held_slot = False
        state.controller.state.application_review_pending = False

    def generate_named(self, name: str, query: str, token: str | None, request: Any):
        """Require a user name before generation and bind it to the pending review."""
        from agentix.domain.application_names import application_folder

        application_folder(name)
        for row in self.generate(query, token, request):
            session, state = self._resolve(token, request)
            if state.candidate is not None:
                state.candidate.display_name = name
                review = json.loads(state.candidate.review_text)
                review["application_name"] = name
                state.candidate.review_text = json.dumps(review, indent=2)
            yield row

    def generate(self, query: str, token: str | None, request: Any) -> Iterator[tuple[Any, ...]]:
        """Start a fresh user operation, never an automatic repair after rejection."""
        session, state = self._resolve(token, request)
        if (
            not session.controller.state.application_busy
            and not session.controller.state.application_review_pending
        ):
            state.repairs = 0
            state.repair_allowed = False
        yield from self._generate(query, token, request)

    def repair(self, token: str | None, request: Any) -> Iterator[tuple[Any, ...]]:
        """Request at most two new proposals from structured independent failure data."""
        session, state = self._resolve(token, request)
        if state.candidate is None or not state.repair_allowed:
            yield (
                "A failed verification is required before requesting a repair.",
                "",
                "",
                "",
                False,
                session.token,
            )
            return
        if state.repairs >= 2:
            yield (
                "Two repair attempts are exhausted. Review the incident before starting a new operation.",
                "",
                "",
                "",
                False,
                session.token,
            )
            return
        report = json.loads((state.candidate.folder / "validation.json").read_bytes())
        query = (state.candidate.folder / "requirements.txt").read_text(encoding="utf-8")
        state.repairs += 1
        state.repair_allowed = False
        yield from self._generate(query, token, request, feedback=report)

    @_safe_stream
    def _generate(
        self, query: str, token: str | None, request: Any, *, feedback: dict | None = None
    ):
        """Stream stage visibility; never approve or execute generated artifacts."""
        session, state = self._resolve(token, request)
        controller = session.controller
        with controller._lock:
            if (
                controller.state.is_running
                or controller.state.application_busy
                or controller.state.application_review_pending
            ):
                raise _StreamRejected(
                    (
                        "Finish the current operation or reject its pending review first.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
                return
            profile = getattr(controller.model_configuration, "profile", None)
            if profile is not None and (
                profile.provider != "Ollama"
                or profile.model != "qwen3-coder:30b"
                or profile.endpoint.rstrip("/")
                not in ("http://127.0.0.1:11434", "http://localhost:11434")
            ):
                raise _StreamRejected(
                    (
                        "Applications requires local Ollama / qwen3-coder:30b at port 11434. Apply that profile in the shared sidebar.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
                return
            if controller.security.get_pending_request():
                raise _StreamRejected(
                    ("Finish the pending Tools review first.", "", "", "", False, session.token)
                )
                return
            self._close(state)
            state.cancelled = False
            controller.state.application_busy = True
            controller.state.application_phase = "generating"
        try:
            yield (
                "Checking approved tools and reusable widgets; preparing an unapproved application. No application code is executing.",
                "",
                "",
                "",
                False,
                session.token,
            )
            root = data_directory() / "drafts" / session.session_id
            registry = self.registry_factory(controller)
            tools = registry.resolve()
            pipeline = self.pipeline_factory(root)
            if isinstance(pipeline, ApplicationPipeline):
                pipeline.widget_store = WidgetStore.for_controller(controller)
            candidate = (
                pipeline.generate(query, tools=tools)
                if feedback is None
                else pipeline.generate(query, feedback=feedback, tools=tools)
            )
            widget_check = candidate.dependency_check

            def recheck_dependencies() -> None:
                """Recheck both installed tool grants and reused widget identities."""
                registry.recheck(tools)
                if widget_check is not None:
                    widget_check()

            candidate.dependency_check = recheck_dependencies
            with controller._lock:
                if state.cancelled or getattr(controller, "_closed", False):
                    raise _StreamRejected(
                        (
                            "Generation cancelled. Evidence retained; nothing approved.",
                            "",
                            "",
                            "",
                            False,
                            session.token,
                        )
                    )
                    return
                state.candidate = candidate
                controller.state.application_review_pending = True
            logger.info("session=%s event=application_review_ready", session.session_id)
            yield (
                "Human review required. Inspect the complete source, proposed tests and independent acceptance cases below.",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
        except Exception as error:
            logger.warning(
                "session=%s event=application_generation_failed error_type=%s",
                session.session_id,
                type(error).__name__,
            )
            detail = (
                str(error) if isinstance(error, CatalogDependencyError) else type(error).__name__
            )
            yield (
                "Application generation failed ("
                + detail
                + "). Evidence retained; no retry or approval occurred.",
                "",
                "",
                "",
                False,
                session.token,
            )
        finally:
            controller.state.application_busy = False
            controller.state.application_phase = ""

    def approve(
        self, reviewed: bool, identity: str, token: str | None, request: Any
    ) -> Iterator[tuple[Any, ...]]:
        """Run independent gates only after owner-bound explicit human approval."""
        session, state = self._resolve(token, request)
        controller = session.controller
        failure = None
        with controller._lock:
            candidate = state.candidate
            if candidate is not None and json.loads(candidate.review_text).get(
                "pending_tool_revisions"
            ):
                failure = (
                    "Review and approve modified tool revisions before verifying this application."
                )
            elif state.unsaved_file:
                failure = "Save the edited file before approving the updated review."
            elif (
                controller.state.is_running
                or controller.state.application_busy
                or not controller.state.application_review_pending
                or candidate is None
            ):
                failure = "No idle pending application review is available."
            else:
                try:
                    self.supervisor.approve(candidate, identity, reviewed)
                except ValueError:
                    failure = "Review and explicitly approve the displayed candidate. Changed or stale artifacts require a new review."
                if failure is None:
                    if not self.preview_slots.acquire(blocking=False):
                        failure = "Two applications are already open; stop one first."
                    else:
                        state.held_slot = True
                        controller.state.application_busy = True
                        controller.state.application_phase = "verifying"
                        state.cancelled = False
        # Gradio may resume generators on another worker thread. Never suspend
        # while an owning-thread RLock is held.
        if failure is not None:
            yield (failure, "", session.token)
            return
        try:
            yield (
                "Supervisor: checking native data execution and actual GUI results with Playwright.",
                "",
                session.token,
            )
            preview = self.supervisor.verify(candidate, self.origin)
            installed = self.library_factory().publish(candidate)
            candidate.catalog_id = installed.id
            if hasattr(preview, "configure_layout"):
                preview.configure_layout(
                    self.library_factory(), installed.id, candidate.dependency_check
                )
            if state.cancelled or getattr(controller, "_closed", False):
                self._close(state)
                yield ("Application stopped.", "", session.token)
                return
            controller.state.application_review_pending = False
            yield (
                "Verified. The application stays open until Close application or supervisor shutdown.",
                generated_application_frame(preview.url),
                session.token,
            )
        except Exception as error:
            self._close(state)
            state.repair_allowed = (candidate.folder / "validation.json").is_file()
            logger.warning(
                "session=%s event=application_verification_failed error_type=%s",
                session.session_id,
                type(error).__name__,
            )
            yield (
                "Independent verification failed ("
                + type(error).__name__
                + "). Application closed; evidence retained. Start a new reviewed proposal to repair it.",
                "",
                session.token,
            )
        finally:
            controller.state.application_busy = False
            controller.state.application_phase = ""

    def stop(self, token: str | None, request: Any) -> tuple[str, str, str]:
        """Stop/reject this owner's application without touching other sessions."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            self._close(state)
            state.repair_allowed = False
            if state.candidate is not None:
                # Explicit rejection revokes execution, unlike merely closing the GUI.
                state.candidate.approved = False
                state.candidate.verified = False
                state.candidate.snapshot = None
        return (
            "Application stopped. Pending proposal rejected; evidence retained.",
            "",
            session.token,
        )

    def data(self, text: str, token: str | None, request: Any) -> tuple[Any, str, str]:
        """Reuse the independently verified data operation without launching its GUI."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            if (
                session.controller.state.is_running
                or session.controller.state.application_busy
                or state.candidate is None
            ):
                return (
                    None,
                    "Finish the current operation and verify an application first.",
                    session.token,
                )
            session.controller.state.application_busy = True
            session.controller.state.application_phase = "running"
        try:
            return (
                self.supervisor.run_data(state.candidate, text),
                "Composite data operation completed in native isolation.",
                session.token,
            )
        except Exception as error:
            return None, "Data operation failed (" + type(error).__name__ + ").", session.token
        finally:
            session.controller.state.application_busy = False
            session.controller.state.application_phase = ""

    def poll(self, token: str | None, request: Any) -> tuple[Any, Any, str]:
        """Report owned worker failure/stop without overwriting active review fields."""
        session, state = self._resolve(token, request)
        candidate = state.candidate
        if (
            not session.controller.state.application_busy
            and candidate is not None
            and candidate.preview is not None
            and candidate.dependency_check is not None
        ):
            try:
                candidate.dependency_check()
            except (ValueError, OSError):
                self._close(state)
                candidate.approved = candidate.verified = False
                candidate.snapshot = None
                return (
                    "Application closed: an installed tool or its approval changed.",
                    "",
                    session.token,
                )
        if (
            not session.controller.state.application_busy
            and candidate is not None
            and candidate.preview is not None
            and not candidate.preview.alive
        ):
            diagnostics = candidate.preview.session.diagnostics
            timed_out = diagnostics.get("failure") == "callback_timeout"
            self._close(state)
            message = (
                "Application stopped: an operation exceeded its time limit."
                if timed_out
                else "Application stopped."
            )
            return message, "", session.token
        return None, None, session.token

    def catalog_entries(self, token: str | None, request: Any) -> tuple[list, str]:
        """List only protected compatible apps, without model or child execution."""
        session, _ = self._resolve(token, request)
        registry = self.registry_factory(session.controller)
        choices = []
        for app in self.library_factory().list():
            try:
                check_dependencies(app, registry)
                choices.append((app.name, app.id))
            except (OSError, ValueError):
                continue
        return choices, session.token

    def describe_app(self, identity: str, token: str | None, request: Any) -> str:
        """Display bounded escaped metadata; the browser never supplies a package path."""
        import html

        session, _ = self._resolve(token, request)
        app = self.library_factory().get(identity)
        check_dependencies(app, self.registry_factory(session.controller))
        return (
            "**"
            + html.escape(app.name)
            + "**\n\n"
            + html.escape(app.description)
            + "\n\nStored package: `"
            + str(app.package)
            + "`"
        )

    @_safe_stream
    def load_app(self, identity: str, token: str | None, request: Any) -> Iterator[tuple]:
        """Restore a verified app to an owner-local working copy; loading executes nothing."""
        from uuid import uuid4

        session, state = self._resolve(token, request)
        controller = session.controller
        with controller._lock:
            if (
                state.unsaved_file
                or controller.state.is_running
                or controller.state.application_busy
                or controller.state.application_review_pending
            ):
                raise _StreamRejected(
                    (
                        "Finish or reject the pending operation first.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
                return
            self._close(state)
            controller.state.application_busy = True
            controller.state.application_phase = "loading"
        try:
            yield (
                "Loading verified application; no model generation or test rerun.",
                "",
                "",
                "",
                False,
                session.token,
            )
            library = self.library_factory()
            app = library.get(identity)
            registry = self.registry_factory(controller)
            check_dependencies(app, registry)
            snapshot = approve_application(app.package, app.digest)
            nonce = uuid4().hex
            folder = library.root.parent / "drafts" / session.session_id / nonce
            package = folder / "application"
            package.mkdir(parents=True, exist_ok=False)
            for name, content in snapshot.files:
                (package / name).write_bytes(content)
            (package / "config.json").write_text(
                json.dumps(library.read_layout(identity), indent=2), encoding="utf-8"
            )
            review = dict(app.review)
            review["source_files"] = {
                name: content.decode("utf-8")
                for name, content in snapshot.files
                if name.endswith(".py")
            }
            (folder / "requirements.txt").write_text(
                review.get("original_request", app.description), encoding="utf-8"
            )
            candidate = Candidate(
                nonce,
                folder,
                package,
                app.digest,
                json.dumps(review, indent=2),
                approved=True,
                verified=True,
                snapshot=snapshot,
                catalog_id=identity,
            )

            def recheck() -> None:
                """Observe protected library and current installed-tool approval drift."""
                current = library.get(identity)
                if current.digest != app.digest:
                    raise ValueError("Installed application changed")
                check_dependencies(current, registry)

            candidate.dependency_check = recheck
            state.candidate = candidate
            state.cancelled = False
            state.repair_allowed = False
            yield (
                "Loaded "
                + app.name
                + ". Use Play or Run data operation; previous tests are not repeated.",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
        except Exception as error:
            yield (
                "Application load failed (" + type(error).__name__ + ").",
                "",
                "",
                "",
                False,
                session.token,
            )
        finally:
            controller.state.application_busy = False
            controller.state.application_phase = ""

    @_safe_stream
    def open_app(self, identity: str, token: str | None, request: Any) -> Iterator[tuple]:
        """Open an unchanged installed app without another model or acceptance suite."""
        session, state = self._resolve(token, request)
        if state.candidate is None or state.candidate.catalog_id != identity:
            yield from self.load_app(identity, token, request)
        candidate = state.candidate
        if candidate is None or candidate.catalog_id != identity:
            return
        with session.controller._lock:
            if (
                state.unsaved_file
                or session.controller.state.application_busy
                or session.controller.state.application_review_pending
                or session.controller.state.is_running
            ):
                raise _StreamRejected(
                    (
                        "Finish the current operation first.",
                        candidate.review_text,
                        candidate.identity,
                        "",
                        False,
                        session.token,
                    )
                )
                return
            if candidate.preview is not None:
                candidate.close()
            if not state.held_slot:
                if not self.preview_slots.acquire(blocking=False):
                    raise _StreamRejected(
                        (
                            "Two application previews are already open.",
                            candidate.review_text,
                            candidate.identity,
                            "",
                            False,
                            session.token,
                        )
                    )
                    return
                state.held_slot = True
            session.controller.state.application_busy = True
            session.controller.state.application_phase = "loading"
        try:
            yield (
                "Starting the approved application sandboxÃ¢â‚¬Â¦",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
            preview = self.supervisor.open_verified(candidate, self.origin)
            if hasattr(preview, "configure_layout"):
                preview.configure_layout(
                    self.library_factory(), identity, candidate.dependency_check
                )
            yield (
                "Application ready.",
                candidate.review_text,
                candidate.identity,
                generated_application_frame(preview.url),
                False,
                session.token,
            )
        except Exception as error:
            self._close(state)
            yield (
                "Application start failed (" + type(error).__name__ + ").",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
        finally:
            session.controller.state.application_busy = False
            session.controller.state.application_phase = ""

    def review_files(self, token: str | None, request: Any) -> tuple:
        """Read the current owner-only file inventory and concise review sections."""
        session, state = self._resolve(token, request)
        if state.candidate is None:
            return [], None, "", False, "No proposal available.", "", [], session.token
        service = ApplicationReview()
        entries = service.entries(state.candidate)
        first = "app.py"
        text, editable, hint = service.read(state.candidate, first)
        import json

        snapshot = json.loads(state.candidate.review_text)
        return (
            entries,
            first,
            text,
            editable,
            hint,
            snapshot.get("original_request", ""),
            snapshot.get("independent_acceptance", []),
            session.token,
        )

    def review_panes(self, name: str, token: str | None, request: Any) -> dict:
        """Resolve a tool group without discarding dirty buffers on a same-tool selection."""
        session, state = self._resolve(token, request)
        if state.candidate is None:
            raise ValueError("No proposal is available")
        panes = ApplicationReview().panes(state.candidate, name)
        expected = "group:" + panes["role"]
        if state.unsaved_file and state.unsaved_file != expected:
            raise ValueError("Save the current edited file/group before changing selection")
        panes["retain_buffers"] = state.unsaved_file == expected
        return panes

    def mark_group_edited(self, name: str, token: str | None, request: Any) -> str:
        """Mark any pane dirty; no old application approval may authorize unsaved code."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            if state.candidate is None or session.controller.state.application_busy:
                raise ValueError("No idle proposal is available")
            panes = ApplicationReview().panes(state.candidate, name)
            state.unsaved_file = "group:" + panes["role"]
        return "Unsaved changes. Save all panes before approval; tool code/test changes require a fresh tool review."

    def save_review(
        self,
        name: str,
        text: str,
        code: str,
        widget: str,
        tool_tests: str,
        widget_tests: str,
        identity: str,
        token: str | None,
        request: Any,
    ) -> tuple:
        """Validate and save the selected single file or all four grouped buffers."""
        session, state = self._resolve(token, request)
        if state.candidate is None:
            raise ValueError("No proposal is available")
        try:
            role = ApplicationReview().panes(state.candidate, name)["role"]
        except ValueError:
            return self.save_file(name, text, identity, token, request)
        with session.controller._lock:
            if session.controller.state.is_running or session.controller.state.application_busy:
                raise ValueError("Finish the active operation before saving")
            if state.unsaved_file and state.unsaved_file != "group:" + role:
                raise ValueError("Save the current group rather than a different selection")
            changed = ApplicationReview().save_group(
                state.candidate,
                {
                    "role": role,
                    "code": code,
                    "widget": widget,
                    "tool_tests": tool_tests,
                    "widget_tests": widget_tests,
                },
                identity,
            )
            state.unsaved_file = ""
            if not changed:
                frame = (
                    generated_application_frame(state.candidate.preview.url)
                    if state.candidate.preview
                    else ""
                )
                return (
                    "No changes to save.",
                    state.candidate.review_text,
                    state.candidate.identity,
                    frame,
                    False,
                    session.token,
                )
            self._close(state)
            state.repair_allowed = False
            session.controller.state.application_review_pending = True
        return (
            "Changes saved. Review updated files; modified tool code/tests need their own approval first.",
            state.candidate.review_text,
            state.candidate.identity,
            "",
            False,
            session.token,
        )

    def mark_edited(self, name: str, token: str | None, request: Any) -> str:
        """Invalidate the checkbox path as soon as an editable file changes on screen."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            if state.candidate is None or session.controller.state.application_busy:
                raise ValueError("No idle proposal is available for editing")
            _, editable, _ = ApplicationReview().read(state.candidate, name)
            if not editable:
                raise ValueError("This dependency is read-only")
            state.unsaved_file = name
        return "Unsaved changes. Save this file before selecting another or approving."

    def read_file(self, name: str, token: str | None, request: Any) -> tuple:
        """Resolve selected filenames on the server; reject arbitrary filesystem paths."""
        session, state = self._resolve(token, request)
        if state.candidate is None:
            raise ValueError("No application proposal is available")
        with session.controller._lock:
            if state.unsaved_file and state.unsaved_file != name:
                raise ValueError("Save the edited file before selecting another file")
            text, editable, hint = ApplicationReview().read(state.candidate, name)
        return text, editable, hint, session.token

    def save_file(
        self, name: str, text: str, identity: str, token: str | None, request: Any
    ) -> tuple:
        """Save only idle owner edits and require an entirely fresh application review."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            if (
                session.controller.state.is_running
                or session.controller.state.application_busy
                or state.candidate is None
            ):
                raise ValueError("Finish the active operation before editing a proposal")
            if state.unsaved_file and state.unsaved_file != name:
                raise ValueError("Save the file that was edited, not a different selection")
            ApplicationReview().save(state.candidate, name, text, identity)
            logger.info(
                "session=%s event=application_review_file_saved file=%s", session.session_id, name
            )
            self._close(state)
            state.repair_allowed = False
            session.controller.state.application_review_pending = True
        return (
            "Changes saved. Review the updated files and approve again before execution.",
            state.candidate.review_text,
            state.candidate.identity,
            "",
            False,
            session.token,
        )

    @_safe_stream
    def review_tools(self, token: str | None, request: Any) -> Iterator[tuple]:
        """Use normal manual file/test/acceptance services for modified shared tools."""
        import hashlib
        from uuid import uuid4

        from agentix.security.acceptance import parse_contract
        from agentix.agents.application_agents import TOOL_CONTRACTS
        from agentix.lab.application_artifacts import FILES, application_digest

        session, state = self._resolve(token, request)
        controller = session.controller
        with controller._lock:
            item = state.candidate
            operations = getattr(controller, "tool_operations", None)
            if (
                item is None
                or operations is None
                or controller.state.is_running
                or controller.state.application_busy
                or state.unsaved_file
            ):
                raise _StreamRejected(
                    (
                        "Save changes and finish active work before reviewing tool revisions.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
                return
            snapshot = json.loads(item.review_text)
            pending = snapshot.get("pending_tool_revisions", {})
            if not pending:
                raise _StreamRejected(
                    (
                        "No modified tool revision requires approval.",
                        item.review_text,
                        item.identity,
                        "",
                        False,
                        session.token,
                    )
                )
                return
            controller.state.application_busy = True
            controller.state.application_phase = "reviewing_tools"
            controller.security.operation_id = uuid4().hex
        completed = threading.Event()
        failures = []

        def review_worker() -> None:
            """The existing tool services own publication; no direct approval/ledger mutation."""
            try:
                for revision in pending.values():
                    name = revision["tool_name"]
                    contract = snapshot.get("tool_acceptance_contracts", {}).get(name)
                    if not contract:
                        raise ValueError("Reviewed tool contract is unavailable")
                    contract = parse_contract(json.dumps(contract))
                    result = operations.compile_and_save_code_tool(name, revision["code"])
                    if not result.startswith("Success:"):
                        raise ValueError("Tool code review was not approved")
                    result = operations.run_and_save_tests_tool(name, revision["tests"])
                    if not result.startswith("TESTS_PROVISIONAL_PASSED:"):
                        raise ValueError("Modified tool tests did not pass")
                    result = operations.submit_acceptance_cases_tool(name, json.dumps(contract))
                    if not result.startswith("ACCEPTANCE_VERIFIED:"):
                        raise ValueError("Modified tool acceptance was not approved")
                    case = next(
                        (case for case in contract["cases"] if case["expect"]["kind"] == "value"),
                        None,
                    )
                    if case is None:
                        raise ValueError(
                            "A successful reviewed case is required to publish reusable execution"
                        )
                    result = operations.execute_generated_tool_tool(
                        name, case["function"], json.dumps(case["kwargs"])
                    )
                    if not result.startswith("Tool Execution Result:"):
                        raise ValueError("Modified tool execution did not succeed")
            except Exception as error:
                failures.append(type(error).__name__)
            finally:
                completed.set()

        threading.Thread(target=review_worker, daemon=True).start()
        try:
            while not completed.wait(0.5):
                yield (
                    "Review modified tool code/tests and acceptance in Tools Ã¢â€ â€™ Authorization & Test Review. Application approval stays blocked until completion.",
                    item.review_text,
                    item.identity,
                    "",
                    False,
                    session.token,
                )
            if failures:
                yield (
                    "Tool revision review stopped ("
                    + failures[0]
                    + "). No application approval was granted.",
                    item.review_text,
                    item.identity,
                    "",
                    False,
                    session.token,
                )
                return
            registry = self.registry_factory(controller)
            tools = registry.resolve()
            for role, tool in tools.items():
                filename = TOOL_CONTRACTS[role]["module"] + ".py"
                (item.package / filename).write_bytes(tool.code)
                snapshot.setdefault("approved_tool_tests", {})[tool.tool_name] = tool.tests.decode(
                    "utf-8"
                )
                snapshot.setdefault("tool_test_drafts", {})[tool.tool_name] = tool.tests.decode(
                    "utf-8"
                )
                snapshot.setdefault("tool_revision_bases", {})[role] = {
                    "code": tool.code.decode("utf-8"),
                    "tests": tool.tests.decode("utf-8"),
                }
                snapshot.setdefault("tool_acceptance_contracts", {})[tool.tool_name] = (
                    tool.reviewed_contract
                )
                snapshot.setdefault("approved_catalog_dependencies", {})[role] = {
                    "tool_name": tool.tool_name,
                    "function": tool.function,
                    "contract_digest": tool.contract_digest,
                    "code_sha256": hashlib.sha256(tool.code).hexdigest(),
                    "tests_sha256": hashlib.sha256(tool.tests).hexdigest(),
                    "unit_tests": "Current revised tool approved",
                }
            snapshot["pending_tool_revisions"] = {}
            manifest = json.loads((item.package / "application.json").read_bytes())
            manifest["files"] = {
                name: hashlib.sha256((item.package / name).read_bytes()).hexdigest()
                for name in FILES
            }
            (item.package / "application.json").write_text(
                json.dumps(manifest, indent=2), encoding="utf-8"
            )
            item.digest = application_digest(item.package)
            item.identity = uuid4().hex
            snapshot["manifest"] = manifest
            snapshot["source_files"] = {
                name: (item.package / name).read_text(encoding="utf-8") for name in FILES
            }
            item.review_text = json.dumps(snapshot, indent=2)
            ApplicationPipeline(item.folder.parent).bind_widget_publication(
                item, tools, WidgetStore.for_controller(controller)
            )
            widget_check = item.dependency_check

            def recheck() -> None:
                """Bind the new app review to the newly published installed tools."""
                registry.recheck(tools)
                if widget_check is not None:
                    widget_check()

            item.dependency_check = recheck
            yield (
                "Tool revisions approved. Review the updated application and approve its widget/integration checks.",
                item.review_text,
                item.identity,
                "",
                False,
                session.token,
            )
        finally:
            controller.state.application_busy = False
            controller.state.application_phase = ""

    def review_state(self, token: str | None, request: Any) -> dict[str, Any]:
        """Expose only this owner's current review/repair eligibility to the frontend."""
        session, state = self._resolve(token, request)
        busy = session.controller.state.application_busy
        return {
            "repair_available": bool(
                state.repair_allowed
                and state.candidate is not None
                and state.repairs < 2
                and not busy
            ),
            "tool_revision_pending": bool(
                state.candidate is not None
                and json.loads(state.candidate.review_text).get("pending_tool_revisions")
            ),
            "busy": busy,
            "pending_review": session.controller.state.application_review_pending,
        }

    def close_owner(self, owner: str) -> None:
        """Close resources when either shared session expiry or browser unload occurs."""
        with self.lock:
            state = self.states.pop(owner, None)
        if state is not None:
            self._close(state)

    def unload(self, request: Any) -> None:
        """Close the framework owner's resources without resolving an expired token."""
        self.close_owner(getattr(request, "session_hash", None))

    def close_all(self) -> None:
        """Stop only registered application resources when the supervisor exits."""
        with self.lock:
            states = list(self.states.values())
            self.states.clear()
        for state in states:
            try:
                self._close(state)
            except Exception as error:
                logger.warning(
                    "event=application_cleanup_failed error_type=%s", type(error).__name__
                )
