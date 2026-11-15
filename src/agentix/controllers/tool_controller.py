"""UI-independent workflow callbacks with injected application dependencies."""

import html
import logging
import sys
import threading
from collections.abc import Callable
from copy import deepcopy
from typing import Any
from uuid import uuid4

from agentix.controllers.state import ConsoleThoughtsCapture, ExecutionState
from agentix.diagnostics import log_event, operation_scope
from agentix.domain.contracts import SecurityBoundary
from agentix.models.profile_errors import ProfileError
from agentix.security.credentials import redact
from agentix.security.paths import SecurityViolationError
from agentix.ui.presentation import format_catalog, format_result, render_validation

logger = logging.getLogger(__name__)

MAX_QUERY_CHARACTERS = 16000  # Longest accepted user query before redaction.
LIVE_LOG_TAIL_LINES = 30  # Activity lines shown while a workflow is running.
FINAL_LOG_TAIL_LINES = 50  # Activity lines retained in the collapsed final accordion.


def format_thoughts_markdown(thoughts_text: str, is_open: bool = False) -> str:
    """Render the existing activity accordion, preserving open/closed markup."""
    # Remove only Rich frame edges; preserve Python indentation and internal pipes.
    lines = []
    for line in thoughts_text.splitlines():
        trimmed = line.lstrip()
        if trimmed.startswith(("|", "│")):
            line = trimmed[1:].removeprefix(" ")
        if line.rstrip().endswith(("|", "│")):
            line = line.rstrip()[:-1].rstrip()
        lines.append(line)
    thoughts_text = "\n".join(lines)
    open_attr = " open" if is_open else ""
    status_label = "(In Progress...)" if is_open else "(Click to expand)"
    content = (
        f"<pre>{html.escape(thoughts_text)}</pre>"
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
        tool_operations: Any = None,
    ) -> None:
        """Connect services; stdout interception is installed only by startup."""
        self.run_system = run_system
        self.get_installed_tools_catalog = catalog
        self.security = security
        self._lock = threading.RLock()
        self._closed = False
        self.application_cleanup = None
        self.update = update
        self.state = state if state is not None else ExecutionState()
        self.captured_stdout = (
            capture
            if capture is not None
            else ConsoleThoughtsCapture(getattr(sys.stdout, "original_stdout", sys.stdout))
        )
        self.security.activity_capture = self.captured_stdout
        self.validation = validation
        self.tool_operations = tool_operations
        self.model_configuration = None
        self._last_profile_save_error = ""

    def validation_status(self) -> str:
        """Render owned host verdicts as escaped text, independently of model replies."""
        status = (
            self.validation.status() if self.validation is not None else {"stage": "not_started"}
        )
        return render_validation(status)

    def approval_readiness(self, text: str, request_id: str | None) -> tuple[Any, str]:
        """Return the review control state using the maintained acceptance parser.

        This only guides the browser. ``on_approve`` and the acceptance evaluator
        still validate the exact text and request identity at the security boundary.
        """
        pending = self.security.get_pending_request()
        if pending is None or request_id != pending.get("request_id"):
            return self.update(interactive=False), "Wait for the current review proposal to load."
        if pending.get("action") != "review_acceptance":
            return self.update(interactive=True), ""
        if self.validation is None or self.validation.status().get("stage") != "pending_review":
            return self.update(interactive=False), "Acceptance validation is pending."
        from agentix.security.acceptance import parse_contract

        try:
            parse_contract(text)
        except ValueError:
            return self.update(interactive=False), "Correct the acceptance JSON before approving."
        return self.update(interactive=True), "Acceptance cases are valid and ready for review."

    def process_user_query(
        self, message: str, *, operation: Callable[[str], str] | None = None
    ) -> tuple[str, list[dict[str, str]]]:
        """Atomically accept one workflow for this session."""
        with self._lock:
            if self._closed:
                raise ValueError("Session is closed")
            return self._process_user_query(message, operation=operation)

    def _process_user_query(
        self, message: str, *, operation: Callable[[str], str] | None = None
    ) -> tuple[str, list[dict[str, str]]]:
        """Submit a nonblank query to one daemon worker and return chat updates.

        Busy submissions retain the existing wait-message behavior. Worker errors
        are captured into state and rendered by polling, rather than propagated
        across the thread boundary. The registry gives each owner a separate controller.
        """
        if not isinstance(message, str) or len(message) > MAX_QUERY_CHARACTERS:
            raise ValueError(f"Query exceeds the {MAX_QUERY_CHARACTERS} character limit")
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
            "Starting reviewed tool validation..."
            if operation is not None
            else "Starting multi-agent workflow...",
            is_open=True,
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
                    result = (operation if operation is not None else self.run_system)(clean_msg)
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
                live_logs = self.captured_stdout.get_logs(max_lines=LIVE_LOG_TAIL_LINES)
                thoughts_box = format_thoughts_markdown(live_logs, is_open=True)
                last_item["content"] = (
                    f"{thoughts_box}\n\n"
                    f"**Agents are actively solving your request...**\n\n"
                    f"*(Check the Security Panel if authorization is required)*"
                )
            elif self.state.last_response or self.state.error_message:
                if "**Agents are actively solving" in last_item.get("content", ""):
                    final_logs = self.captured_stdout.get_logs(max_lines=FINAL_LOG_TAIL_LINES)
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
        """Deny the exact request and retain its proposal as an unapproved repair draft."""
        with self._lock, operation_scope(self.state.session_id, self.state.operation_id):
            pending = self.security.get_pending_request()
            resolved = self.security.resolve_pending_request(
                False, request_id=request_id, owner_id=self.security.owner_id
            )
            if resolved and pending is not None:
                from agentix.application.tool_repair import capture_rejection

                try:
                    draft = capture_rejection(self, pending)
                    if draft is not None:
                        self._rejected_tool = draft
                except (OSError, ValueError, SecurityViolationError):
                    log_event(logger, "rejected_tool_capture_failed", level=logging.WARNING)
            return resolved

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
                elif action in ("refresh", "load"):
                    status = "Saved profiles refreshed."
                    if self._last_profile_save_error:
                        status += " Last save failed: " + self._last_profile_save_error
                    if action == "load" and not configuration.saved_id:
                        # One saved profile needs no manual selection; several stay explicit.
                        saved = [choice for choice in configuration.saved_choices() if choice[1]]
                        if len(saved) == 1:
                            record = configuration.select_saved(saved[0][1])
                            if record:
                                name, provider, model, endpoint = (
                                    record[field]
                                    for field in ("name", "provider", "model", "endpoint")
                                )
                                status = (
                                    "Saved profile selected automatically for this session; "
                                    "it has not been activated."
                                )
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
        if self.application_cleanup is not None:
            self.application_cleanup()
        if self.model_configuration is not None:
            try:
                self.model_configuration.close()
            except Exception as error:
                log_event(logger, "credential_cleanup_failed", error=error, level=logging.ERROR)
