"""Session-owned rejected-tool editor and explicit validation restart controller."""

import json
import secrets

from agentix.agents.repair_acceptance import propose_repair_cases
from agentix.application.tool_repair import ToolRepair
from agentix.controllers.session_access import SessionOwnerAccess


class ToolRepairBackend(SessionOwnerAccess):
    """Bind editable buffers to the exact rejected proposal loaded by this browser."""

    def __init__(self, registry, applications, *, proposer=propose_repair_cases):
        """Inject the application dependency library and acceptance proposal service."""
        super().__init__(registry)
        self.applications, self.proposer = applications, proposer

    @staticmethod
    def _idle(controller) -> None:
        """Require the rejected workflow to finish before a new explicit repair."""
        if getattr(controller, "_closed", False) or any(
            getattr(controller.state, name, False)
            for name in ("is_running", "application_busy", "application_review_pending")
        ):
            raise ValueError("Wait for the current workflow to stop before repairing")

    def load(self, token: str | None, request):
        """Return only this owner's retained rejected buffers and a fresh editor nonce."""
        session = self._session(token, request)
        with session.controller._lock:
            self._idle(session.controller)
            draft = getattr(session.controller, "_rejected_tool", None)
            if draft is None:
                raise ValueError("No rejected tool proposal is available in this session")
            revision = secrets.token_urlsafe(32)
            session.controller._repair_loaded = (revision, draft)
        hint = (
            "Edit both files, then save and restart validation. No execution is authorized by Save."
        )
        if not draft.code or not draft.tests:
            hint += " One or both files were not proposed yet; complete them before validation."
        return draft.tool_name, draft.code, draft.tests, revision, hint, session.token

    def resume(self, revision: str, code: str, tests: str, token: str | None, request):
        """Start a new bounded owner operation, never a continuation of denied approval."""
        session = self._session(token, request)
        controller = session.controller
        with controller._lock:
            self._idle(controller)
            loaded = getattr(controller, "_repair_loaded", None)
            if (
                not loaded
                or not isinstance(revision, str)
                or not secrets.compare_digest(loaded[0], revision)
                or getattr(controller, "_rejected_tool", None) is not loaded[1]
            ):
                raise ValueError("Reload the current rejected tool before saving")
            controller._repair_loaded = None
            draft = loaded[1]

            def saved(current):
                """Keep corrected buffers available after a failure or another rejection."""
                with controller._lock:
                    controller._rejected_tool = current

            service = ToolRepair(
                controller.security,
                controller.tool_operations,
                self.applications.library_factory(),
                propose_cases=lambda context: self.proposer(
                    context, controller.model_configuration
                ),
                on_saved=saved,
            )

            def operation(query):
                """Reuse the controller's synchronized worker, activity capture and status."""
                result = service.save_and_validate(draft, code, tests)
                if result.startswith("ACCEPTANCE_VERIFIED"):
                    with controller._lock:
                        controller._rejected_tool = None
                    observed = controller.tool_operations.verification.execution_result()
                    if observed is not None:
                        return (
                            "Host-observed execution: tool."
                            + observed["tool_name"]
                            + "."
                            + observed["function_name"]
                            + "\nArguments: "
                            + json.dumps(observed["kwargs"], ensure_ascii=True)
                            + "\nResult: "
                            + observed["result"]
                        )
                    return "Tool repair passed the reviewed acceptance cases. No sample execution was recorded; check permissions or runtime diagnostics."
                return result

            controller.process_user_query(
                "Validate explicitly repaired tool " + draft.tool_name, operation=operation
            )
        return (
            "Repair validation started. Review new acceptance requests in Authorization & Test Review.",
            session.token,
        )
