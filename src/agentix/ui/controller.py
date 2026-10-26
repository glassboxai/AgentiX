"""UI-independent workflow callbacks with injected application dependencies."""

import html
import logging
import sys
import threading
from collections.abc import Callable
from copy import deepcopy
from typing import Any
from uuid import uuid4

from ..contracts import SecurityBoundary
from ..credentials import redact
from ..diagnostics import log_event, operation_scope
from ..profile_errors import ProfileError
from .presentation import format_catalog, format_result, render_validation
from .state import ConsoleThoughtsCapture, ExecutionState

logger = logging.getLogger(__name__)


def format_thoughts_markdown(thoughts_text: str, is_open: bool = False) -> str:
    """Render the existing activity accordion, preserving open/closed markup."""
    open_attr = " open" if is_open else ""
    status_label = "(In Progress...)" if is_open else "(Click to expand)"
    content = (
        f"```text\n{thoughts_text}\n```"
        if thoughts_text
        else "*Initializing agents and inspecting catalog...*"
    )

    return (
        f"<details{open_attr}>\n"
        f"<summary><b>Agent Thoughts & Activity</b> <i>{status_label}</i></summary>\n\n"
        f"{content}\n"
        f"</details>"
    )


class UiController:
    """Own one session's state, activity and callbacks without browser widgets."""

    def __init__(
        self,
        run_system: Callable[[str], str],
        catalog: Callable[[], str],
        security: SecurityBoundary,
        update: Callable[..., Any],
        state: ExecutionState | None = None,
        capture: ConsoleThoughtsCapture | None = None,
        validation: Any = None,
    ) -> None:
        """Connect services; stdout interception is installed only by startup."""
        self.run_system = run_system
        self.get_installed_tools_catalog = catalog
        self.security = security
        self._lock = threading.RLock()
        self._closed = False
        self.update = update
        self.state = state if state is not None else ExecutionState()
        self.captured_stdout = (
            capture
            if capture is not None
            else ConsoleThoughtsCapture(getattr(sys.stdout, "original_stdout", sys.stdout))
        )
        self.security.activity_capture = self.captured_stdout
        self.validation = validation
        self.model_configuration = None
        self._last_profile_save_error = ""

    def validation_status(self) -> str:
        """Render owned host verdicts as escaped text, independently of model replies."""
        status = (
            self.validation.status() if self.validation is not None else {"stage": "not_started"}
        )
        return render_validation(status)

    def process_user_query(self, message: str) -> tuple[str, list[dict[str, str]]]:
        """Atomically accept one workflow for this session."""
        with self._lock:
            if self._closed:
                raise ValueError("Session is closed")
            return self._process_user_query(message)

    def _process_user_query(self, message: str) -> tuple[str, list[dict[str, str]]]:
        """Submit a nonblank query to one daemon worker and return chat updates.

        Busy submissions retain the existing wait-message behavior. Worker errors
        are captured into state and rendered by polling, rather than propagated
        across the thread boundary. The registry gives each owner a separate controller.
        """
        if not isinstance(message, str) or len(message) > 16000:
            raise ValueError("Query exceeds the 16000 character limit")
        clean_msg = redact(message.strip())
        if not clean_msg:
            return "", deepcopy(self.state.chat_history)

        if self.state.is_running:
            self.state.chat_history.append({"role": "user", "content": clean_msg})
            self.state.chat_history.append(
                {
                    "role": "assistant",
                    "content": "Another query is already in progress. Please wait for it to finish.",
                }
            )
            return "", deepcopy(self.state.chat_history)

        self.captured_stdout.clear()
        self.state.is_running = True
        self.state.operation_id = uuid4().hex
        self.security.operation_id = self.state.operation_id
        self.state.last_response = ""
        self.state.error_message = ""
        self.state.last_displayed_filepath = None
        self.state.last_displayed_request_id = None

        initial_thoughts = format_thoughts_markdown(
            "Starting multi-agent workflow...", is_open=True
        )
        self.state.chat_history.append({"role": "user", "content": clean_msg})
        self.state.chat_history.append(
            {
                "role": "assistant",
                "content": f"{initial_thoughts}\n\n**Agents are actively solving your request...**\n\n*(Check the Security Panel if authorization is required)*",
            }
        )

        self.state.active_message_index = len(self.state.chat_history) - 1

        def worker() -> None:
            """Run with explicit owner/activity context and synchronized state updates."""
            with operation_scope(
                self.state.session_id, self.state.operation_id, capture=self.captured_stdout
            ):
                log_event(logger, "workflow_started")
                try:
                    result = self.run_system(clean_msg)
                    with self._lock:
                        self.state.last_response = (
                            redact(str(result))
                            if result
                            else "Execution finished without text output."
                        )
                except Exception as exc:
                    log_event(logger, "workflow_failed", error=exc, level=logging.ERROR)
                    with self._lock:
                        self.state.error_message = redact(str(exc))
                finally:
                    with self._lock:
                        self.state.is_running = False
                    log_event(logger, "workflow_finished")

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

        return "", deepcopy(self.state.chat_history)

    def poll_system_status(self) -> tuple[list[dict[str, str]], Any, str, Any, str]:
        """Read one coherent session snapshot without overwriting in-progress edits."""
        with self._lock:
            return self._poll_system_status()

    def poll_with_request(self) -> tuple[Any, ...]:
        """Return the UI snapshot and exact request ID displayed in that snapshot."""
        with self._lock:
            return (*self._poll_system_status(), self.state.last_displayed_request_id or "")

    def _poll_system_status(self) -> tuple[list[dict[str, str]], Any, str, Any, str]:
        """
        Polled every second by gr.Timer:
        1. Updates live thoughts and final answer.
        2. Shows approval card and loads text ONCE (so user edits are never overwritten by timer).
        3. Refreshes tools catalog.
        """
        # 1. Update Chat
        index = self.state.active_message_index
        if index is None and self.state.chat_history:
            index = len(self.state.chat_history) - 1
        if (
            index is not None
            and index < len(self.state.chat_history)
            and self.state.chat_history[index].get("role") == "assistant"
        ):
            last_item = self.state.chat_history[index]

            if self.state.is_running:
                live_logs = self.captured_stdout.get_logs(max_lines=30)
                thoughts_box = format_thoughts_markdown(live_logs, is_open=True)
                last_item["content"] = (
                    f"{thoughts_box}\n\n"
                    f"**Agents are actively solving your request...**\n\n"
                    f"*(Check the Security Panel if authorization is required)*"
                )
            elif self.state.last_response or self.state.error_message:
                if "**Agents are actively solving" in last_item.get("content", ""):
                    final_logs = self.captured_stdout.get_logs(max_lines=50)
                    collapsed_thoughts = format_thoughts_markdown(final_logs, is_open=False)

                    if self.state.error_message:
                        last_item["content"] = (
                            f"{collapsed_thoughts}\n\n**Error during execution:**\n\n```text\n{self.state.error_message}\n```"
                        )
                    else:
                        query = next(
                            (
                                item["content"]
                                for item in reversed(self.state.chat_history[:index])
                                if item["role"] == "user"
                            ),
                            "",
                        )
                        answer = format_result(self.state.last_response, query)
                        last_item["content"] = f"{collapsed_thoughts}\n\n{answer}"
                    logger.info("Rendered final answer with collapsed thoughts accordion.")

        # 2. Check Pending Security Approval
        pending = self.security.get_pending_request()
        if pending:
            approval_visibility = self.update(visible=True)
            pending_file_text = (
                f"**File:** `{pending['filepath']}`\n\n**Action:** `{pending['action'].upper()}`"
            )
            if pending["action"] == "review_acceptance":
                context = pending.get("review_context", {})
                pending_file_text = (
                    "### Human acceptance review\n\n"
                    + html.escape(context.get("summary", "Review each case before approving."))
                    + "\n\nEdit the acceptance JSON below. File auto-approval does not apply."
                    + "\n\n<details><summary>Provisional automatic result (not independent proof)</summary><pre>"
                    + html.escape(context.get("provisional_result", ""))
                    + "</pre></details>"
                    + "\n\n<details><summary>Generated Python tests (read-only; reject to request changes)</summary><pre>"
                    + html.escape(context.get("python_tests", ""))
                    + "</pre></details>"
                )

                if getattr(getattr(self.validation, "ledger", None), "store", None) is not None:
                    pending_file_text += (
                        "\n\n**Approval will be remembered for future sessions** on this PC after a successful run, "
                        "while this tool and its security policy remain unchanged. "
                        "Sensitive or unclassified calls still require permission."
                    )

            # Populate text box only once when a new pending file arrives
            if self.state.last_displayed_request_id != pending["request_id"]:
                self.state.last_displayed_filepath = pending["filepath"]
                self.state.last_displayed_request_id = pending["request_id"]
                preview_update = self.update(value=pending["content"], interactive=True)
            else:
                # Keep existing user edits in the textarea without resetting
                preview_update = self.update()
        else:
            self.state.last_displayed_filepath = None
            self.state.last_displayed_request_id = None
            approval_visibility = self.update(visible=False)
            pending_file_text = "No pending approval requests."
            preview_update = self.update(value="", interactive=True)

        # 3. Refresh Catalog
        catalog_text = format_catalog(self.get_installed_tools_catalog())

        return (
            deepcopy(self.state.chat_history),
            approval_visibility,
            pending_file_text,
            preview_update,
            catalog_text,
        )

    def on_approve(self, edited_text: str, request_id: str | None = None) -> bool:
        """Approve only the ID sent with the displayed editor snapshot."""
        with operation_scope(self.state.session_id, self.state.operation_id):
            return self.security.resolve_pending_request(
                True, edited_text, request_id=request_id, owner_id=self.security.owner_id
            )

    def on_reject(self, request_id: str | None = None) -> bool:
        """Reject only the displayed request; missing/stale IDs have no effect."""
        with operation_scope(self.state.session_id, self.state.operation_id):
            return self.security.resolve_pending_request(
                False, request_id=request_id, owner_id=self.security.owner_id
            )

    def on_toggle_auto_approve(self, is_checked: bool) -> None:
        """Change only this owner's setting; do not resolve pending requests."""
        with self._lock:
            if self._closed:
                raise ValueError("Session is closed")
            self.security.auto_approve = bool(is_checked)
        with operation_scope(self.state.session_id, self.state.operation_id):
            log_event(logger, "approval_mode_changed")

    def profile_action(
        self,
        action: str,
        identity: str,
        name: str,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
    ) -> tuple[Any, ...]:
        """Serialize profile actions with this owner's execution and review state."""
        try:
            with self._lock:
                configuration = self.model_configuration
                if configuration is None or self._closed:
                    raise ValueError("Model settings unavailable")
                consent = False
                if action in ("save", "delete") and identity != configuration.saved_id:
                    raise ValueError("Displayed profile selection changed; reload before saving")
                if action == "select":
                    record = configuration.select_saved(identity)
                    if record:
                        name, provider, model, endpoint = (
                            record[field] for field in ("name", "provider", "model", "endpoint")
                        )
                    else:
                        name, provider, model, endpoint = (
                            "",
                            "Ollama",
                            "qwen3-coder:30b",
                            "http://127.0.0.1:11434",
                        )
                    status = "Profile loaded for editing. It has not been activated."
                elif action == "save":
                    status = configuration.save_profile(name, provider, model, endpoint, key)
                    self._last_profile_save_error = ""
                elif action == "delete":
                    status = configuration.delete_profile()
                    name = ""
                elif action == "refresh":
                    status = "Saved profiles refreshed."
                    if self._last_profile_save_error:
                        status += " Last save failed: " + self._last_profile_save_error
                else:
                    raise ValueError("Invalid profile action")
                choices = configuration.saved_choices()
                selected = configuration.saved_id
        except Exception as error:
            trace = error.__traceback__
            while trace and trace.tb_next:
                trace = trace.tb_next
            log_event(
                logger,
                "model_profile_action_failed",
                error=error,
                line=trace.tb_lineno if trace else None,
                level=logging.ERROR,
            )
            # Never let vendor/storage exception bodies cross the browser boundary.
            choices, selected, consent = [("New profile", "")], "", False
            try:
                if self.model_configuration is not None:
                    choices = self.model_configuration.saved_choices()
                    selected = self.model_configuration.saved_id
            except Exception:
                # Corrupt/unavailable metadata must never be silently replaced.
                pass
            status = "Profile action was not completed. Check saved selection, name, key and pending work; reload after concurrent edits. Switch to Ollama before deleting an active profile."
            if isinstance(error, ProfileError):
                status = "Profile action was not completed. " + str(error)
            if action == "save":
                self._last_profile_save_error = status
        return choices, selected, name, provider, model, endpoint, "", consent, status

    def configure_model(
        self, provider: str, model: str, endpoint: str, key: str, consent: bool
    ) -> str:
        """Change only this idle owner; preserve the runtime if configuration fails."""
        with self._lock:
            if self._closed or self.model_configuration is None:
                raise ValueError("Model configuration is unavailable for this session")
            result = self.model_configuration.configure(provider, model, endpoint, key, consent)
            log_event(logger, "model_configuration_applied")
            return result

    def close(self) -> None:
        """Stop accepting callbacks and cancel pending/future owner writes."""
        with self._lock:
            self._closed = True
        self.security.cancel_pending()
        if self.model_configuration is not None:
            try:
                self.model_configuration.close()
            except Exception as error:
                log_event(logger, "credential_cleanup_failed", error=error, level=logging.ERROR)
