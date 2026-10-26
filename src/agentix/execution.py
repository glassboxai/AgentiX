"""Validate calls before importing code exclusively inside an OS-isolated child."""

import json
import logging
import re

from .contracts import ExecutionBackend, SecurityBoundary
from .diagnostics import log_event
from .reuse_policy import computation_only
from .verification import VerificationLedger

logger = logging.getLogger(__name__)


class ToolExecutor:
    """Enforce evidence and JSON boundaries independently of agent instructions."""

    def __init__(
        self,
        security: SecurityBoundary,
        sandbox: ExecutionBackend,
        verification: VerificationLedger,
    ) -> None:
        """Bind a per-runtime ledger and injectable isolated process backend."""
        self.security, self.sandbox, self.verification = security, sandbox, verification

    def execute_generated_tool_tool(
        self, tool_name: str, function_name: str, kwargs_json: str = "{}"
    ) -> str:
        """Validate input and evidence, then pass exact verified bytes to a child."""
        self.verification.begin_execution()
        try:
            clean = kwargs_json.strip()
            if len(clean) > 65536:
                raise ValueError("Arguments exceed 64 KiB")
            kwargs = json.loads(clean) if clean and clean not in ("''", '""') else {}
            if not isinstance(kwargs, dict):
                raise ValueError("Arguments must be a JSON object")
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,127}", function_name):
                raise ValueError("A public Python function name is required")
        except (ValueError, RecursionError) as exc:
            return f"Error parsing kwargs_json: {exc}"
        try:
            self.verification.prepare_reuse(tool_name)
            if not self.verification.is_verified(tool_name, function_name):
                log_event(logger, "tool_execution_not_verified", level=logging.WARNING)
                return "TOOL_NOT_VERIFIED: Run the current tool's tests in this operation first."
            code, tests = self.verification.snapshot(tool_name)
            if not self.verification.matches_authorized(tool_name, code, tests, function_name):
                return "TOOL_NOT_VERIFIED: Artifact content changed."
            identity = (self.security.owner_id, self.security.operation_id)
            if not computation_only(code):
                approved, _ = self.security.request_user_permission(
                    f"Execute {tool_name}.{function_name}",
                    "execute_sensitive_tool",
                    json.dumps(
                        {"tool": tool_name, "function": function_name, "arguments": kwargs},
                        ensure_ascii=True,
                    ),
                    require_manual=True,
                    review_context={
                        "summary": "This tool may perform sensitive or unclassified operations. Approve this exact call only. Native isolation permissions remain unchanged."
                    },
                )
                if not approved:
                    log_event(logger, "sensitive_execution_denied", level=logging.WARNING)
                    return "EXECUTION_DENIED: This call requires explicit approval."
            if identity != (
                self.security.owner_id,
                self.security.operation_id,
            ) or not self.verification.matches_authorized(tool_name, code, tests, function_name):
                return (
                    "TOOL_NOT_VERIFIED: Authorization or content changed while awaiting execution."
                )
            result = self.sandbox.execute(code, None, tool_name, function_name, kwargs)
            if result.failure or result.exit_code != 0 or not result.isolated or not result.report:
                return (
                    f"Execution Error: isolated child failed ({result.failure or 'child_error'})."
                )
            if result.report.get("kind") != "call":
                return "Execution Error: invalid child result."
            if not self.verification.record_execution(
                tool_name, code, tests, function_name, kwargs, result.report.get("result")
            ):
                return "Execution Error: acceptance or artifact changed during execution."
            log_event(logger, "tool_execution_finished")
            return f"Tool Execution Result: {result.report['result']}"
        except Exception as exc:
            log_event(logger, "tool_execution_failed", error=exc, level=logging.ERROR)
            return "Execution Error: isolation unavailable or artifact access failed."
