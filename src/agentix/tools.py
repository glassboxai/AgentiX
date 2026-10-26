"""Framework-free artifact operations composed with execution/test services.

CrewAI registration lives in adapters; imports never initialize frameworks/models.
Generated unittest results are provisional; human-reviewed host comparisons alone
authorize function execution for exact artifact snapshots. Successful calls may
establish session grants and optional protected durable approvals; each result remains operation-bound.
"""

import json
import logging
import os
from datetime import datetime

from .acceptance import AcceptanceEvaluator
from .approval_store import ApprovalStore
from .contracts import ExecutionBackend, SecurityBoundary
from .diagnostics import log_event
from .execution import ToolExecutor
from .sandbox import WindowsSandbox
from .testing import TestRunner
from .verification import VerificationLedger

logger = logging.getLogger(__name__)


class ArtifactTools:
    """Application operations for specifications, code, incidents and reads."""

    def __init__(
        self,
        security: SecurityBoundary,
        *,
        sandbox: ExecutionBackend | None = None,
        approval_store: ApprovalStore | None = None,
    ) -> None:
        """Compose owner-bound services, native execution and a shared evidence ledger."""
        self.security = security
        self.verification = VerificationLedger(security, store=approval_store)
        backend = sandbox if sandbox is not None else WindowsSandbox()
        self.executor = ToolExecutor(security, backend, self.verification)
        self.runner = TestRunner(
            security, self.append_structured_incidence, backend, self.verification
        )
        self.acceptance = AcceptanceEvaluator(security, backend, self.verification)

    def run_and_save_tests_tool(self, tool_name: str, test_code: str) -> str:
        """Save/run generated unittest as provisional evidence, never final authorization."""
        result = self.runner.run_and_save_tests_tool(tool_name, test_code)
        self.acceptance.note_provisional(tool_name, result)
        return result

    def verify_existing_tool_tool(self, tool_name: str) -> str:
        """Prepare an unchanged successful tool, or use first-use tests and review."""
        if self.verification.prepare_reuse(tool_name):
            log_event(logger, "tool_reuse_prepared")
            return "REUSE_READY: " + json.dumps(
                self.verification.acceptance_context(tool_name), ensure_ascii=True
            )
        result = self.runner.verify_existing_tool(tool_name)
        self.acceptance.note_provisional(tool_name, result)
        return result

    def submit_acceptance_cases_tool(self, tool_name: str, cases_json: str) -> str:
        """Request mandatory human review and host-evaluate declarative acceptance cases."""
        return self.acceptance.submit(tool_name, cases_json)

    def execute_generated_tool_tool(
        self, tool_name: str, function_name: str, kwargs_json: str = "{}"
    ) -> str:
        """Execute verified current bytes only inside the native OS boundary."""
        return self.executor.execute_generated_tool_tool(tool_name, function_name, kwargs_json)

    def append_structured_incidence(
        self, tool_name: str, suffix: str, title: str, details: str
    ) -> str:
        """
        Standardizes timestamped incidence logging across all agents.
        Writes formatted markdown to: <toolName>/<toolName>_<suffix>.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"{tool_name}_{suffix}"

        # Clean text to ensure proper markdown presentation
        clean_details = str(details).strip()

        entry = (
            f"\n## [{timestamp}] - {title}\n"
            f"- **Tool Name:** `{tool_name}`\n\n"
            f"### Incidence Details:\n"
            f"```text\n{clean_details}\n```\n"
            f"\n---\n"
        )

        log_event(logger, "artifact_incidence_requested")
        return self.security.safe_write_file(tool_name, filename, entry, mode="a")

    def save_specifications_tool(self, tool_name: str, content: str) -> str:
        """Saves software specifications to <toolName>/<toolName>_specifications.md."""
        filename = f"{tool_name}_specifications.md"
        return self.security.safe_write_file(tool_name, filename, content, mode="w")

    def log_specifications_incidence_tool(self, tool_name: str, incidence: str) -> str:
        """Appends a timestamped incidence to <toolName>/<toolName>_specifications_incidences.md."""
        return self.append_structured_incidence(
            tool_name=tool_name,
            suffix="specifications_incidences.md",
            title="Architectural Design Issue",
            details=incidence,
        )

    def compile_and_save_code_tool(self, tool_name: str, code: str) -> str:
        """
        Validates Python syntax by compiling it in memory before saving.
        If valid, saves to <toolName>/<toolName>_code.py.
        If invalid, AUTOMATICALLY records a timestamped entry in <toolName>_code_incidences.md.
        """
        filename = f"{tool_name}_code.py"

        # Strip markdown code blocks if the LLM wrapped the output
        clean_code = code.strip()
        if clean_code.startswith("```python"):
            clean_code = clean_code[len("```python") :].strip()
        elif clean_code.startswith("```"):
            clean_code = clean_code[len("```") :].strip()
        if clean_code.endswith("```"):
            clean_code = clean_code[:-3].strip()

        # Step 1: In-memory syntax validation
        try:
            compile(clean_code, f"{tool_name}_code.py", "exec")
        except SyntaxError as e:
            error_msg = f"SyntaxError on line {e.lineno}: {e.msg}\nCode snippet: {e.text}"
            log_event(
                logger, "python_compilation_rejected", error=e, level=logging.WARNING, line=e.lineno
            )

            # Log incidence with exact date and time
            self.append_structured_incidence(
                tool_name=tool_name,
                suffix="code_incidences.md",
                title="Compilation / Syntax Error",
                details=error_msg,
            )
            return (
                f"COMPILATION_ERROR: {error_msg}\n"
                f"The incident was automatically recorded with date and time in {tool_name}_code_incidences.md.\n"
                f"Please fix the code and submit again."
            )

        # Storage recompiles the final approved content, closing the editor gap.
        return self.security.safe_write_file(tool_name, filename, clean_code, mode="w")

    def log_coder_incidence_tool(self, tool_name: str, incidence: str) -> str:
        """Appends a timestamped manual incidence to <toolName>/<toolName>_code_incidences.md."""
        return self.append_structured_incidence(
            tool_name=tool_name,
            suffix="code_incidences.md",
            title="Implementation Hurdle",
            details=incidence,
        )

    def log_tester_incidence_tool(self, tool_name: str, incidence: str) -> str:
        """Appends a timestamped manual incidence to <toolName>/<toolName>_tests_incidences.md."""
        return self.append_structured_incidence(
            tool_name=tool_name,
            suffix="tests_incidences.md",
            title="QA Verification Issue",
            details=incidence,
        )

    def read_artifact_tool(self, tool_name: str, filename: str) -> str:
        """Safely reads an existing specification, code, or test file from the tool directory."""
        try:
            target_path = self.security.validate_and_resolve_path(tool_name, filename)
            if not os.path.exists(target_path):
                return f"Error: File '{filename}' does not exist in '{tool_name}' directory."

            with open(target_path, encoding="utf-8") as f:
                content = f.read()
            log_event(logger, "artifact_read")
            return content
        except Exception as e:
            log_event(logger, "artifact_read_failed", error=e, level=logging.ERROR)
            return f"Error reading file: {str(e)}"
