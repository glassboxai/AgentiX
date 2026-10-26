"""Approved test persistence and OS-observed, content-bound unittest outcomes."""

import logging
from collections.abc import Callable

from .contracts import ExecutionBackend, SecurityBoundary
from .diagnostics import log_event
from .verification import VerificationLedger

logger = logging.getLogger(__name__)


class TestRunner:
    """Publish evidence only from an isolated process and current approved bytes."""

    def __init__(
        self,
        security: SecurityBoundary,
        record_incidence: Callable[..., str],
        sandbox: ExecutionBackend,
        verification: VerificationLedger,
    ) -> None:
        """Connect storage, an isolated backend and a per-runtime evidence ledger."""
        self.security, self.record_incidence = security, record_incidence
        self.sandbox, self.verification = sandbox, verification

    def run_and_save_tests_tool(self, tool_name: str, test_code: str) -> str:
        """Persist final approved edits, isolate execution and reject empty/skipped suites."""
        self.verification.invalidate(tool_name)
        clean = test_code.strip()
        if clean.startswith("```python"):
            clean = clean[len("```python") :].strip()
        elif clean.startswith("```"):
            clean = clean[3:].strip()
        if clean.endswith("```"):
            clean = clean[:-3].strip()
        saved = self.security.safe_write_file(tool_name, f"{tool_name}_tests.py", clean, mode="w")
        if not saved.startswith("Success:"):
            return saved
        return self.verify_existing_tool(tool_name)

    def verify_existing_tool(self, tool_name: str) -> str:
        """Re-run existing approved bytes without changing files or trusting old reports."""
        self.verification.invalidate(tool_name)
        try:
            identity = (self.security.owner_id, self.security.operation_id)
            code, tests = self.verification.snapshot(tool_name)
            result = self.sandbox.execute(code, tests, tool_name, "", {})
            if (
                identity == (self.security.owner_id, self.security.operation_id)
                and not result.failure
                and self.verification.record(
                    tool_name,
                    code,
                    tests,
                    result.report,
                    isolated=result.isolated,
                    exit_code=result.exit_code,
                )
            ):
                log_event(logger, "generated_tests_provisional_passed")
                return f"TESTS_PROVISIONAL_PASSED:\n{result.output}\nHuman acceptance review is still required."
            details = f"Isolated tests not verified ({result.failure or 'unsuccessful_or_empty'}).\n{result.output}"
        except Exception as exc:
            log_event(logger, "generated_test_runner_failed", error=exc, level=logging.ERROR)
            details = "Isolation unavailable or test input access failed; execution denied."
        self.verification.invalidate(tool_name)
        log_event(logger, "generated_tests_not_verified", level=logging.WARNING)
        self.record_incidence(
            tool_name=tool_name,
            suffix="tests_incidences.md",
            title="Isolated Test Verification Failure",
            details=details,
        )
        return f"TESTS_FAILED: {details}"
