"""Owner-checked Applications controller; no Gradio imports or generated execution."""

import atexit
import functools
import json
import logging
import os
import threading
import time
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from agentix.application.app_invocation import check_dependencies, rebind_dependencies
from agentix.application.app_review import ApplicationReview
from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor, Candidate
from agentix.controllers.application_candidates import (
    AcceptedCandidates,
    CandidateSelection,
    CandidateState,
    SelectedToolRegistry,
    present_candidates,
)
from agentix.controllers.sessions import SessionRegistry
from agentix.diagnostics import log_event, operation_scope
from agentix.domain.application_code import ApplicationContractError
from agentix.lab.application_artifacts import approve_application
from agentix.retrieval import policy as retrieval_policy
from agentix.retrieval.gui import GuiToolRetrieval
from agentix.storage.application_catalog import ApprovedToolRegistry, CatalogDependencyError
from agentix.storage.catalog import ToolCatalog
from agentix.storage.installed_apps import InstalledApps
from agentix.storage.locations import data_directory
from agentix.storage.widget_store import WidgetStore
from agentix.ui.application_presentation import describe_data_inputs, generated_application_frame

logger = logging.getLogger(__name__)

MAX_CONCURRENT_PREVIEWS = 2  # Owner previews open at once across the backend.
MAX_REPAIR_ATTEMPTS = 2  # Structured repair proposals allowed per application operation.
TOOL_REVIEW_POLL_SECONDS = 0.5  # Streaming wait between modified-tool review updates.
GROUP_SELECTION_PREFIX = "group:"  # Marks a four-pane tool group as the dirty selection.
# Closed profile codes whose own message already names the required owner action.
IDENTITY_REJECTION_CODES = frozenset({"profile_not_selected", "generation_identity_changed"})
IDENTITY_UNAVAILABLE = (
    "The saved local model identity is unavailable or changed. Inspect it and use Reset "
    "trusted generation identity only if you accept the change."
)


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
    pending_host_requirement: str | None = None
    retrieval_state: CandidateState = field(default_factory=CandidateState)
    accepted_dependencies: AcceptedCandidates | None = None


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
        retrieval: Any = None,
        host_requirements: Any = None,
    ) -> None:
        """Inject storage/execution factories; construction starts no model or server."""
        self.sessions, self.pipeline_factory = sessions, pipeline_factory
        self.registry_factory = registry_factory
        self.library_factory = library_factory
        self.retrieval = retrieval if retrieval is not None else GuiToolRetrieval()
        # Bootstrap injects the production registry. Test-only controllers that do
        # not compose the host process deliberately leave recovery unavailable.
        self.host_requirements = host_requirements
        self.supervisor = supervisor or ApplicationSupervisor()
        self.origin = "http://127.0.0.1:" + str(
            parent_port or int(os.environ.get("AGENTIX_SERVER_PORT", "7877"))
        )
        self.states: dict[str, ApplicationState] = {}
        self.lock = threading.RLock()
        self.preview_slots = threading.BoundedSemaphore(MAX_CONCURRENT_PREVIEWS)
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
        state.retrieval_state.invalidate()
        state.unsaved_file = None
        if state.candidate is not None:
            state.candidate.close()
        if state.held_slot:
            self.preview_slots.release()
            state.held_slot = False
        state.controller.state.application_review_pending = False

    @staticmethod
    def _candidate_idle(controller: Any) -> None:
        """Reject candidate actions during Tools work, generation or pending review."""
        if (
            controller.state.is_running
            or controller.state.application_busy
            or controller.state.application_review_pending
        ):
            raise ValueError("Finish the current operation or reject its pending review first.")

    def owned_candidate(self, token: str | None, request: Any) -> tuple[Any, ApplicationState, Any]:
        """Resolve the caller's own proposal for a presentation-only service.

        Reuses the single ownership check instead of duplicating token/owner logic;
        the caller still decides whether the proposal is idle enough to mutate.
        """
        session, state = self._resolve(token, request)
        if state.candidate is None:
            raise ValueError("No application proposal is available")
        return session, state, state.candidate

    def invalidate_candidates(self, token: str | None, request: Any) -> str:
        """Invalidate edited description/limit revisions without cancelling model work."""
        session, state = self._resolve(token, request)
        invalidated = False
        with session.controller._lock:
            if (
                not session.controller.state.application_busy
                and not session.controller.state.application_review_pending
            ):
                state.retrieval_state.invalidate()
                invalidated = True
                state.accepted_dependencies = None
            elif getattr(session.controller.state, "application_phase", "") == "retrieving":
                state.retrieval_state.invalidate()
                invalidated = True
        logger.info(
            "session=%s event=%s",
            session.session_id,
            "candidate_invalidated" if invalidated else "candidate_invalidation_ignored",
        )
        return session.token

    def candidate_controls(
        self, token: str | None, request: Any, *, selected_ids: list[str] | None = None
    ) -> tuple[bool, bool, str, str]:
        """Read owner-local control availability plus a short reason for a blocked button."""
        session, state = self._resolve(token, request)
        idle = not (
            session.controller.state.is_running
            or session.controller.state.application_busy
            or session.controller.state.application_review_pending
        )
        selection = state.retrieval_state.selection
        ready, reason = False, "search for candidates first"
        if selection is not None:
            try:
                ready = bool(selection.selected_expected(selected_ids))
                reason = ""
            except ValueError:
                chosen = list(selection.expected) if selected_ids is None else selected_ids
                ineligible = bool(chosen) and not set(chosen).issubset(selection.eligible_ids)
                reason = (
                    "approve the selected tools in Tools first"
                    if ineligible
                    else "select at least one current candidate"
                )
        if not idle:
            ready, reason = False, "wait for the current operation to finish"
        return idle, bool(idle and ready), session.token, reason

    def request_candidates(
        self, query: str, limit: int, token: str | None, request: Any, *, name: str | None = None
    ) -> tuple[CandidateSelection | None, str]:
        """Search before generation; publish only the latest owner-bound description/limit.

        When the frontend supplies the application name, it is validated here so a
        missing or invalid name is reported before any retrieval inference starts.
        """
        session, state = self._resolve(token, request)
        controller = session.controller
        if name is not None:
            from agentix.domain.application_names import application_folder

            application_folder(name)
        if (
            not isinstance(query, str)
            or not query.strip()
            or len(query.encode("utf-8")) > retrieval_policy.MAX_QUERY_BYTES
        ):
            logger.info(
                "session=%s event=candidate_search_rejected reason=invalid_query",
                session.session_id,
            )
            raise ValueError("Enter a nonempty application description within the query limit.")
        if isinstance(limit, float) and limit.is_integer():
            limit = int(limit)
        if (
            isinstance(limit, bool)
            or not isinstance(limit, int)
            or not retrieval_policy.MIN_SEARCH_LIMIT <= limit <= retrieval_policy.MAX_SEARCH_LIMIT
        ):
            logger.info(
                "session=%s event=candidate_search_rejected reason=invalid_limit",
                session.session_id,
            )
            raise ValueError("Candidate limit must be an integer within the displayed bounds.")
        with controller._lock:
            try:
                self._candidate_idle(controller)
            except ValueError:
                logger.info(
                    "session=%s event=candidate_search_rejected reason=busy", session.session_id
                )
                raise
            revision = state.retrieval_state.invalidate()
            state.accepted_dependencies = None
            controller.state.application_busy = True
            controller.state.application_phase = "retrieving"
        started = time.perf_counter()
        try:
            with operation_scope(
                session.session_id,
                revision,
                capture=getattr(controller, "captured_stdout", None),
            ):
                log_event(logger, "candidate_search_started")
                catalog = getattr(controller.get_installed_tools_catalog, "__self__", None)
                if not isinstance(catalog, ToolCatalog):
                    raise ValueError("Installed tool catalog is unavailable.")
                log_event(logger, "candidate_search_retrieval_dispatching", level=logging.DEBUG)
                results = self.retrieval.search(catalog, state.retrieval_state.handle, query, limit)
                log_event(logger, "candidate_search_retrieval_ready", level=logging.DEBUG)
            view = present_candidates(
                revision, query, limit, results, self.registry_factory(controller)
            )
            with controller._lock:
                if state.retrieval_state.revision != revision:
                    logger.info(
                        "session=%s operation=%s event=candidate_search_superseded",
                        session.session_id,
                        revision,
                    )
                    return None, session.token
                state.retrieval_state.selection = view
            logger.info(
                "session=%s operation=%s event=candidate_search_finished limit=%s count=%s ready=%s duration_ms=%.3f",
                session.session_id,
                revision,
                limit,
                len(results),
                view.ready,
                (time.perf_counter() - started) * retrieval_policy.MILLISECONDS_PER_SECOND,
            )
            for item in results:
                logger.info(
                    "session=%s operation=%s event=candidate_ranked tool=%s rank=%s score=%s",
                    session.session_id,
                    revision,
                    item.descriptor.tool_id,
                    item.rank,
                    item.score,
                )
            return view, session.token
        except Exception as error:
            with controller._lock:
                if state.retrieval_state.revision != revision:
                    logger.info(
                        "session=%s operation=%s event=candidate_search_superseded outcome=failed",
                        session.session_id,
                        revision,
                    )
                    return None, session.token
            logger.warning(
                "session=%s operation=%s event=candidate_search_failed error_type=%s duration_ms=%.3f",
                session.session_id,
                revision,
                type(error).__name__,
                (time.perf_counter() - started) * retrieval_policy.MILLISECONDS_PER_SECOND,
            )
            raise ValueError(
                "Candidate search unavailable. Check local Ollama/catalog and retry Generate application."
            ) from None
        finally:
            with controller._lock:
                controller.state.application_busy = False
                controller.state.application_phase = ""

    def accept_candidates(
        self,
        name: str,
        query: str,
        limit: int,
        identity: str,
        token: str | None,
        request: Any,
        *,
        selected_ids: list[str] | None = None,
    ) -> Iterator[tuple[Any, ...]]:
        """Consume exactly the displayed server snapshot before starting application agents."""
        session, state = self._resolve(token, request)
        if isinstance(limit, float) and limit.is_integer():
            limit = int(limit)
        with operation_scope(
            session.session_id,
            identity,
            capture=getattr(session.controller, "captured_stdout", None),
        ):
            log_event(logger, "candidate_accept_requested")
        with session.controller._lock:
            self._candidate_idle(session.controller)
            selection = state.retrieval_state.selection
            if (
                selection is None
                or selection.identity != identity
                or selection.query != query
                or selection.limit != limit
            ):
                state.retrieval_state.invalidate()
                logger.info(
                    "session=%s event=candidate_accept_rejected reason=stale_or_unavailable",
                    session.session_id,
                )
                raise ValueError(
                    "Candidates are stale or unavailable. Search again and accept the displayed list."
                )
            try:
                expected = selection.selected_expected(selected_ids)
            except ValueError:
                logger.info(
                    "session=%s operation=%s event=candidate_accept_rejected reason=invalid_subset",
                    session.session_id,
                    identity,
                )
                raise
            selected = AcceptedCandidates(query, expected, identity=identity)
            state.retrieval_state.invalidate()
        try:
            SelectedToolRegistry(
                self.registry_factory(session.controller), selected.expected
            ).resolve()
        except Exception as error:
            logger.warning(
                "session=%s operation=%s event=candidate_accept_rejected reason=dependency_check error_type=%s",
                session.session_id,
                identity,
                type(error).__name__,
            )
            message = (
                "Candidates changed or lack current approval. Search again after reviewing them in Tools."
                if isinstance(error, ValueError)
                else "Candidate acceptance unavailable. Check the catalog and search again."
            )
            raise ValueError(message) from None
        logger.info(
            "session=%s operation=%s event=candidate_accepted count=%s limit=%s",
            session.session_id,
            identity,
            len(selected.expected),
            limit,
        )
        for tool_id in selected.expected:
            logger.info(
                "session=%s operation=%s event=candidate_selected tool=%s",
                session.session_id,
                identity,
                tool_id,
            )
        yield from self.generate_named(name, query, session.token, request, selected=selected)

    def generate_named(
        self,
        name: str,
        query: str,
        token: str | None,
        request: Any,
        *,
        selected: AcceptedCandidates | None = None,
    ) -> Iterator[tuple[Any, ...]]:
        """Require a user name before generation and bind it to the pending review."""
        from agentix.domain.application_names import application_folder

        application_folder(name)
        if not self.library_factory().name_available(name):
            raise ValueError(
                "An installed application already uses this name; delete it first or choose a different name"
            )
        for row in self.generate(query, token, request, selected=selected):
            session, state = self._resolve(token, request)
            if state.candidate is not None:
                state.candidate.display_name = name
                review = json.loads(state.candidate.review_text)
                review["application_name"] = name
                state.candidate.review_text = json.dumps(review, indent=2)
            yield row

    def generate(
        self,
        query: str,
        token: str | None,
        request: Any,
        *,
        selected: AcceptedCandidates | None = None,
    ) -> Iterator[tuple[Any, ...]]:
        """Start a fresh user operation, never an automatic repair after rejection."""
        session, state = self._resolve(token, request)
        if (
            not session.controller.state.application_busy
            and not session.controller.state.application_review_pending
        ):
            state.repairs = 0
            state.repair_allowed = False
        yield from self._generate(query, token, request, selected=selected)

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
        if state.repairs >= MAX_REPAIR_ATTEMPTS:
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
        display_name = state.candidate.display_name
        for row in self._generate(
            query, token, request, feedback=report, selected=state.accepted_dependencies
        ):
            if state.candidate is not None:
                state.candidate.display_name = display_name
            yield row

    @_safe_stream
    def _generate(
        self,
        query: str,
        token: str | None,
        request: Any,
        *,
        feedback: dict | None = None,
        selected: AcceptedCandidates | None = None,
    ) -> Iterator[tuple[Any, ...]]:
        """Stream stage visibility; never approve or execute generated artifacts."""
        session, state = self._resolve(token, request)
        controller = session.controller
        logger.info("session=%s event=application_generate_started", session.session_id)
        with controller._lock:
            if (
                controller.state.is_running
                or controller.state.application_busy
                or controller.state.application_review_pending
            ):
                logger.info(
                    "session=%s event=application_generate_rejected reason=busy",
                    session.session_id,
                )
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
            if profile is None or profile.provider != "Ollama":
                raise _StreamRejected(
                    (
                        "Applications requires a locally configured Ollama generation profile.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
                return
            from agentix.models.profile_errors import ProfileError

            try:
                had_trusted_digest = bool(
                    getattr(controller.model_configuration, "generation_digest", "")
                )
                controller.model_configuration.ensure_generation_identity()
                captured_tofu_baseline = not had_trusted_digest and bool(
                    getattr(controller.model_configuration, "generation_digest", "")
                )
            except ProfileError as error:
                # A closed code names the owner action; never reuse the changed-digest text.
                logger.info(
                    "session=%s event=application_generate_rejected reason=%s",
                    session.session_id,
                    error.code,
                )
                raise _StreamRejected(
                    (
                        str(error)
                        if error.code in IDENTITY_REJECTION_CODES
                        else IDENTITY_UNAVAILABLE,
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                ) from None
            except ValueError:
                logger.info(
                    "session=%s event=application_generate_rejected reason=identity_unavailable",
                    session.session_id,
                )
                raise _StreamRejected(
                    (IDENTITY_UNAVAILABLE, "", "", "", False, session.token)
                ) from None
            if controller.security.get_pending_request():
                raise _StreamRejected(
                    ("Finish the pending Tools review first.", "", "", "", False, session.token)
                )
                return
            self._close(state)
            state.accepted_dependencies = selected
            state.cancelled = False
            controller.state.application_busy = True
            controller.state.application_phase = "generating"
        try:
            yield (
                (
                    "Local model digest baseline recorded by TOFU; it detects local changes but does not prove authenticity. "
                    if captured_tofu_baseline
                    else ""
                )
                + "Checking approved tools and reusable widgets; preparing an unapproved application. No application code is executing.",
                "",
                "",
                "",
                False,
                session.token,
            )
            root = data_directory() / "drafts" / session.session_id
            registry = self.registry_factory(controller)
            if selected is not None:
                if selected.query != query:
                    raise CatalogDependencyError(
                        "Accepted candidates no longer match the application description."
                    )
                registry = SelectedToolRegistry(registry, selected.expected)
            tools = registry.resolve()
            logger.info(
                "session=%s event=application_tools_resolved selection=%s tools=%s",
                session.session_id,
                selected.identity if selected is not None else "legacy",
                sorted(tools),
            )
            pipeline = self.pipeline_factory(root)
            configured = getattr(controller, "model_configuration", None)
            set_model_client = getattr(pipeline, "set_model_client", None)
            if configured is not None and callable(set_model_client):
                set_model_client(configured.client)
            if isinstance(pipeline, ApplicationPipeline):
                pipeline.widget_store = WidgetStore.for_controller(controller)
            with operation_scope(
                session.session_id,
                uuid4().hex,
                capture=getattr(controller, "captured_stdout", None),
            ):
                logger.info("session=%s event=application_model_started", session.session_id)
                candidate = (
                    pipeline.generate(query, tools=tools)
                    if feedback is None
                    else pipeline.generate(query, feedback=feedback, tools=tools)
                )
                logger.info(
                    "session=%s event=application_model_finished identity=%s",
                    session.session_id,
                    candidate.identity,
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
            log_event(logger, "application_generation_failed", error=error, level=logging.WARNING)
            if isinstance(error, CatalogDependencyError):
                detail = str(error)
            elif isinstance(error, ApplicationContractError):
                # Closed host diagnostic: input identity and key names only, never payload.
                detail = str(error)
            else:
                detail = type(error).__name__
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
        logger.info("session=%s event=application_approve_started", session.session_id)
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
                from agentix.application.code_cases import acceptance_status

                valid, guidance = acceptance_status(json.loads(candidate.review_text))
                try:
                    if not valid:
                        failure = guidance
                    elif (
                        self.host_requirements is not None
                        and (requirement := self.host_requirements.missing("playwright-chromium"))
                        is not None
                    ):
                        state.pending_host_requirement = requirement.identifier
                        failure = (
                            "Independent browser verification requires a host dependency. "
                            + requirement.user_message
                            + " Review it, then click Install required host dependency."
                        )
                    else:
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
            logger.info(
                "session=%s event=application_approve_blocked reason=%.300s",
                session.session_id,
                failure,
            )
            yield (failure, "", session.token)
            return
        try:
            yield (
                "Supervisor: checking native data execution and actual GUI results with Playwright.",
                "",
                session.token,
            )
            logger.info("session=%s event=application_verify_started", session.session_id)
            preview = self.supervisor.verify(candidate, self.origin)
            installed = self.library_factory().publish(candidate)
            logger.info(
                "session=%s event=application_verified_published catalog_id=%s",
                session.session_id,
                installed.id,
            )
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
                generated_application_frame(preview.url, candidate.display_name),
                session.token,
            )
        except Exception as error:
            self._close(state)
            state.repair_allowed = (candidate.folder / "validation.json").is_file()
            logger.warning(
                "session=%s event=application_verification_failed error_type=%s error_message=%.200s",
                session.session_id,
                type(error).__name__,
                str(error),
                exc_info=True,
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

    def install_host_requirement(self, token: str | None, request: Any) -> tuple[str, str]:
        """Install a previously disclosed host dependency after an explicit UI action.

        Only the owner of an unchanged pending application review can reach the
        injected registry. No browser value, generated source or model response
        selects the requirement or its command.
        """
        session, state = self._resolve(token, request)
        controller = session.controller
        with controller._lock:
            identifier = state.pending_host_requirement
            candidate = state.candidate
            if (
                self.host_requirements is None
                or not identifier
                or candidate is None
                or not controller.state.application_review_pending
                or controller.state.application_busy
            ):
                raise ValueError("No confirmed host dependency installation is available.")
            candidate_identity = candidate.identity
            controller.state.application_busy = True
            controller.state.application_phase = "installing-host-dependency"
        try:
            self.host_requirements.install(identifier)
        except Exception as error:
            logger.warning(
                "session=%s event=host_dependency_install_failed requirement=%s error_type=%s",
                session.session_id,
                identifier,
                type(error).__name__,
            )
            return (
                "Host dependency installation failed. The reviewed proposal remains pending; retry only after resolving the host requirement.",
                session.token,
            )
        finally:
            with controller._lock:
                controller.state.application_busy = False
                controller.state.application_phase = ""
        with controller._lock:
            if (
                state.candidate is None
                or state.candidate.identity != candidate_identity
                or not controller.state.application_review_pending
                or state.pending_host_requirement != identifier
            ):
                return (
                    "Host dependency installed, but the reviewed proposal changed. Review the current proposal before approval.",
                    session.token,
                )
            state.pending_host_requirement = None
        logger.info(
            "session=%s event=host_dependency_install_verified requirement=%s",
            session.session_id,
            identifier,
        )
        return (
            "Host dependency installed and verified. Review is still required; click Approve and verify again.",
            session.token,
        )

    def stop(self, token: str | None, request: Any) -> tuple[str, str, str]:
        """Stop/reject this owner's application without touching other sessions."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            self._close(state)
            state.repair_allowed = False
            state.accepted_dependencies = None
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
        except ValueError as error:
            # Host-originated contract/JSON diagnostics are bounded and never echo the payload.
            detail = " ".join(str(error).split())[:200].rstrip(".")
            logger.warning(
                "session=%s event=data_operation_rejected error_type=%s",
                session.session_id,
                type(error).__name__,
            )
            message = "Data operation failed (" + type(error).__name__ + ")"
            return (
                None,
                message + (": " + detail + "." if detail else "."),
                session.token,
            )
        except Exception as error:
            logger.warning(
                "session=%s event=data_operation_failed error_type=%s",
                session.session_id,
                type(error).__name__,
            )
            return None, "Data operation failed (" + type(error).__name__ + ").", session.token
        finally:
            session.controller.state.application_busy = False
            session.controller.state.application_phase = ""

    def data_contract(self, token: str | None, request: Any) -> tuple[str, str]:
        """Describe the loaded application's declared data inputs without executing it.

        The manifest comes from the verified snapshot, so the owner sees the exact
        closed keys and types before typing a payload. No child module is imported
        and no model or native execution occurs.
        """
        session, state = self._resolve(token, request)
        candidate = state.candidate
        if candidate is None or candidate.snapshot is None:
            return (
                "Load and verify an application to see its data-operation input schema.",
                session.token,
            )
        manifest = json.loads(dict(candidate.snapshot.files)["application.json"])
        return describe_data_inputs(manifest), session.token

    def poll(self, token: str | None, request: Any) -> tuple[Any, Any, str]:
        """Serialize stop/failure observation with this owner's open/close transitions."""
        session, state = self._resolve(token, request)
        with session.controller._lock:
            return self._poll_owned(session, state)

    def _poll_owned(self, session: Any, state: ApplicationState) -> tuple[Any, Any, str]:
        """Observe and optionally close one preview while holding its owner lock.

        The busy-state check and teardown must be one lifecycle transition. A
        stale observation must never close a newly started worker or its lease.
        Model/native execution remains outside this polling path; teardown affects
        only the owning session and retains the existing public status contract.
        """
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
        """List protected installed apps; stale records stay visible for re-approval."""
        session, _ = self._resolve(token, request)
        choices = [
            (
                entry.name if entry.status == "valid" else entry.name + " (re-approval required)",
                entry.id,
            )
            for entry in self.library_factory().entries()
            if entry.id
        ]
        return choices, session.token

    def describe_app(self, identity: str, token: str | None, request: Any) -> str:
        """Display bounded escaped metadata; the browser never supplies a package path."""
        import html

        session, _ = self._resolve(token, request)
        library = self.library_factory()
        try:
            app = library.get(identity)
        except ValueError:
            entry = library.entry(identity)
            return (
                "**"
                + html.escape(entry.name)
                + "**\n\nRe-approval required: "
                + html.escape(entry.reason)
                + "\n\nUse Load selected app to review it again, or Re-verify selected app "
                "to repeat the independent gates on the installed bytes."
            )
        try:
            check_dependencies(app, self.registry_factory(session.controller))
        except ValueError as error:
            return (
                "**"
                + html.escape(app.name)
                + "**\n\nApproval required: "
                + html.escape(str(error))
                + "\n\nUse Load selected app to review it again."
            )
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
            try:
                app = library.get(identity)
                stale = False
            except ValueError:
                # A changed maintained runtime or a changed host policy still loads
                # for explicit re-approval; only a changed source stays refused.
                try:
                    app = library.load_for_runtime_refresh(identity)
                except ValueError:
                    app = library.load_stale(identity)
                stale = True
            registry = self.registry_factory(controller)
            rebound = None
            try:
                check_dependencies(app, registry)
            except ValueError:
                rebound = rebind_dependencies(app, registry)
                stale = True
            snapshot = approve_application(app.package, app.digest, allow_runtime_drift=True)
            nonce = uuid4().hex
            folder = library.root.parent / "drafts" / session.session_id / nonce
            package = folder / "application"
            package.mkdir(parents=True, exist_ok=False)
            for name, content in snapshot.files:
                (package / name).write_bytes(content)
            (package / "config.json").write_text(
                json.dumps(library.read_layout(identity, allow_runtime_drift=stale), indent=2),
                encoding="utf-8",
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
                snapshot.digest if stale else app.digest,
                json.dumps(review, indent=2),
                approved=not stale,
                verified=not stale,
                snapshot=snapshot,
                catalog_id=identity,
                display_name=app.name,
                runtime_refresh=stale,
            )

            def recheck() -> None:
                """Observe protected library and current installed-tool approval drift."""
                if stale:
                    try:
                        current = library.load_for_runtime_refresh(identity)
                    except ValueError:
                        current = library.load_stale(identity)
                else:
                    current = library.get(identity)
                if current.digest != app.digest:
                    raise ValueError("Installed application changed")
                if rebound is None:
                    check_dependencies(current, registry)
                    return
                binding = rebind_dependencies(current, registry)
                if binding != rebound:
                    raise ValueError("Installed catalog tools or their approvals changed")
                candidate.review_text = json.dumps(
                    {
                        **json.loads(candidate.review_text),
                        "approved_catalog_dependencies": binding,
                    },
                    indent=2,
                )

            candidate.dependency_check = recheck
            state.candidate = candidate
            state.cancelled = False
            state.repair_allowed = False
            if stale:
                controller.state.application_review_pending = True
                reason = (
                    "the host execution policy changed since it was installed"
                    if rebound is None
                    else "the approved tool contracts changed since it was installed"
                )
                yield (
                    "Loaded "
                    + app.name
                    + " for re-approval: "
                    + reason
                    + ". Review the restored code, then approve to repeat the "
                    "independent native and browser gates.",
                    candidate.review_text,
                    candidate.identity,
                    "",
                    False,
                    session.token,
                )
                return
            yield (
                "Loaded "
                + app.name
                + ". Review the restored code here; press Play selected app to start it in the "
                "sandbox, or Run data operation to call it without opening its interface. "
                "Previous tests are not repeated.",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
        except CatalogDependencyError as error:
            yield (
                "Application load failed: " + str(error),
                "",
                "",
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
        if not candidate.verified:
            raise _StreamRejected(
                (
                    "This application needs re-approval: review the restored code and approve "
                    "to repeat the independent native and browser gates.",
                    candidate.review_text,
                    candidate.identity,
                    "",
                    False,
                    session.token,
                )
            )
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
            candidate.library_lease = self.library_factory().open_lease(identity)
            yield (
                "Starting the approved application sandbox…",
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
                generated_application_frame(preview.url, candidate.display_name),
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

    @_safe_stream
    def reverify_app(self, identity: str, token: str | None, request: Any) -> Iterator[tuple]:
        """Repeat independent gates on installed bytes and reseal only after they pass."""
        from uuid import uuid4

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
                        "Finish the current operation first.",
                        "",
                        "",
                        "",
                        False,
                        session.token,
                    )
                )
            controller.state.application_busy = True
            controller.state.application_phase = "verifying"
        try:
            library = self.library_factory()
            try:
                library.get(identity)
                yield (
                    "This application is already current; no re-verification was needed.",
                    "",
                    "",
                    "",
                    False,
                    session.token,
                )
                return
            except ValueError:
                app = library.load_stale(identity)
            registry = self.registry_factory(controller)
            try:
                check_dependencies(app, registry)
            except ValueError:
                rebind_dependencies(app, registry)
                yield (
                    "Re-verification requires re-approval: the approved tool contracts "
                    "changed since this application was installed. Use Load selected app, "
                    "review the restored code and approve to repeat the independent gates.",
                    "",
                    "",
                    "",
                    False,
                    session.token,
                )
                return
            snapshot = approve_application(app.package, app.digest)
            folder = library.root.parent / "drafts" / session.session_id / uuid4().hex
            package = folder / "application"
            package.mkdir(parents=True, exist_ok=False)
            for name, content in snapshot.files:
                (package / name).write_bytes(content)
            review = dict(app.review)
            review["source_files"] = {
                name: content.decode("utf-8")
                for name, content in snapshot.files
                if name.endswith(".py")
            }
            candidate = Candidate(
                uuid4().hex,
                folder,
                package,
                app.digest,
                json.dumps(review, indent=2),
                approved=True,
                verified=False,
                snapshot=snapshot,
                catalog_id=identity,
                display_name=app.name,
            )

            def recheck() -> None:
                """Observe installed bytes and current tool approvals during the gates."""
                check_dependencies(library.load_stale(identity), registry)

            candidate.dependency_check = recheck
            yield (
                "Re-running independent native and browser gates on the installed bytes...",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
            preview = self.supervisor.verify(candidate, self.origin)
            resealed = library.reseal(identity)
            if preview is not None and hasattr(preview, "close"):
                preview.close()
            logger.info(
                "session=%s event=application_reverified catalog_id=%s",
                session.session_id,
                identity,
            )
            yield (
                "Re-verified " + resealed.name + " and rebound it to the current host policy.",
                candidate.review_text,
                candidate.identity,
                "",
                False,
                session.token,
            )
        except CatalogDependencyError as error:
            logger.warning(
                "session=%s event=application_reverify_failed app_id=%s error_type=%s "
                "error_message=%.200s",
                session.session_id,
                identity,
                type(error).__name__,
                str(error),
            )
            yield (
                "Re-verification failed: "
                + str(error)
                + " The stored application remains unapproved.",
                "",
                "",
                "",
                False,
                session.token,
            )
        except Exception as error:
            logger.warning(
                "session=%s event=application_reverify_failed app_id=%s error_type=%s "
                "error_message=%.200s",
                session.session_id,
                identity,
                type(error).__name__,
                str(error),
            )
            yield (
                "Re-verification failed ("
                + type(error).__name__
                + "). The stored application remains unapproved.",
                "",
                "",
                "",
                False,
                session.token,
            )
        finally:
            controller.state.application_busy = False
            controller.state.application_phase = ""

    def review_files(self, token: str | None, request: Any) -> tuple:
        """Read the current owner-only file inventory and concise review sections."""
        session, state = self._resolve(token, request)
        if state.candidate is None:
            return [], None, "", False, "No proposal available.", "", [], session.token
        service = ApplicationReview()
        entries = service.entries(state.candidate)
        snapshot = json.loads(state.candidate.review_text)
        first = (
            "application_acceptance.json"
            if snapshot.get("manifest", {}).get("schema_version") == 3
            else "app.py"
        )
        text, editable, hint = service.read(state.candidate, first)
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
        expected = GROUP_SELECTION_PREFIX + panes["role"]
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
            state.unsaved_file = GROUP_SELECTION_PREFIX + panes["role"]
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
            if state.unsaved_file and state.unsaved_file != GROUP_SELECTION_PREFIX + role:
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
            logger.info(
                "session=%s event=application_review_group_saved role=%s changed=%s",
                session.session_id,
                role,
                changed,
            )
            state.unsaved_file = ""
            if not changed:
                frame = (
                    generated_application_frame(
                        state.candidate.preview.url, state.candidate.display_name
                    )
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
            if name.endswith("_widget.css") and state.candidate.catalog_id:
                # The loaded candidate is a disposable draft copy, so the installed
                # package must receive the style too or the saved file never changes.
                self.library_factory().write_style_member(state.candidate.catalog_id, name, text)
            preview = getattr(state.candidate, "preview", None)
            if name.endswith("_widget.css") and preview is not None:
                # A running preview serves a stylesheet staged at startup; rewrite it
                # so a reload and the separate "View as web" tab see the new style.
                restage = getattr(getattr(preview, "session", None), "restage_styles", None)
                if restage is not None:
                    restage(name, text)
            revoked = ApplicationReview().save(state.candidate, name, text, identity)
            if revoked:
                self._close(state)
                state.repair_allowed = False
                session.controller.state.application_review_pending = True
                message = (
                    "Changes saved. Review the updated files and approve again before execution."
                )
            else:
                state.unsaved_file = ""
                message = (
                    "Widget style saved to the installed application. The approved "
                    "application stays valid; reopen the preview to see the new style."
                )
        return (
            message,
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

        from agentix.lab.application_artifacts import application_digest
        from agentix.security.acceptance import parse_contract

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
            contracts = snapshot.get("manifest", {}).get("tools", {})
            files = set(snapshot.get("manifest", {}).get("files", {}))
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
            while not completed.wait(TOOL_REVIEW_POLL_SECONDS):
                yield (
                    "Review modified tool code/tests and acceptance in Tools → Authorization & Test Review. Application approval stays blocked until completion.",
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
            if state.accepted_dependencies is not None:
                with controller._lock:
                    self._close(state)
                    state.candidate = None
                    state.accepted_dependencies = None
                    state.repair_allowed = False
                logger.info(
                    "session=%s event=candidate_invalidated reason=tool_revision",
                    session.session_id,
                )
                yield (
                    "Tool revisions approved. Candidate selection invalidated; use Generate application to search and accept the current tools again.",
                    "",
                    "",
                    "",
                    False,
                    session.token,
                )
                return
            registry = self.registry_factory(controller)
            tools = registry.resolve()
            for role, tool in tools.items():
                filename = contracts[role]["module"] + ".py"
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
                for name in files
            }
            (item.package / "application.json").write_text(
                json.dumps(manifest, indent=2), encoding="utf-8"
            )
            item.digest = application_digest(item.package)
            item.identity = uuid4().hex
            snapshot["manifest"] = manifest
            snapshot["source_files"] = {
                name: (item.package / name).read_text(encoding="utf-8") for name in files
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
        requirement = state.pending_host_requirement
        requirement_message = ""
        if requirement and self.host_requirements is not None:
            try:
                requirement_message = self.host_requirements.requirement(requirement).user_message
            except (AttributeError, ValueError):
                requirement_message = "A reviewed host dependency is required before independent browser verification."
        return {
            "repair_available": bool(
                state.repair_allowed
                and state.candidate is not None
                and state.repairs < MAX_REPAIR_ATTEMPTS
                and not busy
            ),
            "tool_revision_pending": bool(
                state.candidate is not None
                and json.loads(state.candidate.review_text).get("pending_tool_revisions")
            ),
            "busy": busy,
            "pending_review": session.controller.state.application_review_pending,
            "host_dependency_pending": bool(requirement),
            "host_dependency_message": requirement_message,
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
