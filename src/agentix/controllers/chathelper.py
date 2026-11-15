"""Owner-checked context chat controller; no Gradio dependency or file editing."""

import hashlib
import json

from agentix.application.app_review import ApplicationReview
from agentix.application.code_assistance import explain_code
from agentix.controllers.session_access import SessionOwnerAccess
from agentix.models.model_profiles import create_profile_llm

HISTORY_MESSAGE_LIMIT = 12  # Retained chat turns (user plus assistant) per editor scope.
SPECIFICATION_READ_LIMIT = 32769  # One character beyond 32 KiB so truncation is detectable.


class ChatHelperBackend(SessionOwnerAccess):
    """Resolve selected pending-review context and retain history on its session owner."""

    def __init__(self, registry, applications, *, client_factory=create_profile_llm):
        """Inject owner registry, application controller and provider composition boundary."""
        super().__init__(registry)
        self.applications, self.client_factory = applications, client_factory

    def ask(self, pane: str, selected: str, source: str, question: str, token: str | None, request):
        """Explain current editor text using only its verified tool's specification/contract.

        Browser file names are resolved through the application's finite review list.
        Source is treated as data, never opened as a path or executed. Histories
        remain session-local and reset when the file or editor buffer changes.
        """
        session, state = self.applications._resolve(token, request)
        controller = session.controller
        with controller._lock:
            if (
                controller.state.is_running
                or controller.state.application_busy
                or state.candidate is None
            ):
                raise ValueError("Open an idle application review before asking about code")
            if pane not in {"code", "widget", "tool_tests", "widget_tests"}:
                raise ValueError("Select a code column")
            related = ApplicationReview().panes(state.candidate, selected)
            contract = ApplicationReview()._contracts(state.candidate)[related["role"]]
            tool_name = contract["module"].removesuffix("_code")
            spec_path = controller.security.validate_and_resolve_path(
                tool_name, tool_name + "_specifications.md"
            )
            with open(spec_path, encoding="utf-8") as stream:
                specification = stream.read(SPECIFICATION_READ_LIMIT)
            suffix = {
                "code": "_code.py",
                "widget": "_widget.py",
                "tool_tests": "_tests.py",
                "widget_tests": "_widget_tests.py",
            }[pane]
            context = {
                "filename": tool_name + suffix,
                "source": source,
                "specification": specification,
                "contract": dict(contract),
            }
            if pane in {"widget", "widget_tests"}:
                context["contract"]["widget_context"] = (
                    "create_widget(context); context.elem_id(control); returned group/input/output/execute references"
                )
            scope = hashlib.sha256(json.dumps(context, sort_keys=True).encode()).hexdigest()
            owned = getattr(controller, "_code_help", {"scope": scope, "history": []})
            history = owned["history"] if owned["scope"] == scope else []
            configuration = controller.model_configuration
            client = self.client_factory(
                configuration.profile, configuration.vault, configuration.llm_factory
            )
            answer = explain_code(context, question, client, history[-HISTORY_MESSAGE_LIMIT:])
            history = [
                *history,
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer},
            ][-HISTORY_MESSAGE_LIMIT:]
            controller._code_help = {"scope": scope, "history": history}
        transcript = "\n\n".join(
            ("You: " if entry["role"] == "user" else "AgentiX: ") + entry["content"]
            for entry in history
        )
        return transcript, "", session.token
