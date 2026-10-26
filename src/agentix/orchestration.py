"""Workflow orchestration with explicit factories, agents and catalog dependencies.

Creation decisions use a strict fail-closed contract. Task/context ordering is
preserved; only current test-service evidence permits the final execution stage.
"""

import json
import logging
import threading
from collections.abc import Callable
from typing import Any

from .adapters.crewai import AgentSet
from .decisions import CreateToolDecision, parse_manager_response
from .diagnostics import log_event, operation_scope
from .verification import VerificationLedger

logger = logging.getLogger(__name__)
# Bound active pipelines across all browser and terminal owners in this process.
_WORK_CAPACITY = threading.BoundedSemaphore(4)


class Orchestrator:
    """Route queries and build tools without owning framework initialization."""

    def __init__(
        self,
        agents: AgentSet,
        backend: Any,
        catalog: Callable[[], str],
        verification: VerificationLedger | None = None,
    ) -> None:
        """Inject role objects, CrewAI factories and the read-only catalog callback."""
        self.manager_agent = agents.manager
        self.creation_manager_agent = agents.creation_manager
        self.architect_agent = agents.architect
        self.coder_agent = agents.coder
        self.tester_agent = agents.tester
        self.Task, self.Crew, self.Process = backend.Task, backend.Crew, backend.Process
        self.get_installed_tools_catalog = catalog
        self.verification = verification

    def _saved_stage_text(self, tool_name: str, suffix: str, before: Any) -> str:
        """Load fresh approved persisted bytes, never import or trust a model claim.

        Receipts bind writes to the current owner/operation. Reads are bounded,
        confined and hash checked; unchanged old receipts cannot advance a stage.
        """
        import hashlib
        from pathlib import Path

        security = self.verification.security
        path = security.validate_and_resolve_path(tool_name, f"{tool_name}_{suffix}")
        receipt = security.get_artifact_receipt(path)
        if receipt is None or receipt == before:
            raise ValueError("No fresh approved artifact receipt")
        with Path(path).open("rb") as stream:
            data = stream.read(1_048_577)
        if (
            not data.strip()
            or len(data) > 1_048_576
            or hashlib.sha256(data).hexdigest() != receipt[1]
        ):
            raise ValueError("Approved artifact is empty, oversized or changed")
        text = data.decode("utf-8")
        if suffix.endswith(".py"):
            compile(text, path, "exec")
        return text

    def _creation_stage(
        self, tool_name: str, stage: str, suffix: str, agent: Any, description: str
    ) -> str | None:
        """Run one model stage, then enforce its host-observed save postcondition.

        No automatic model retry follows missing evidence or human denial. Model
        errors propagate; artifact failures stop creation with payload-free logs.
        """
        security = self.verification.security
        path = security.validate_and_resolve_path(tool_name, f"{tool_name}_{suffix}")
        before = security.get_artifact_receipt(path)
        task = self.Task(
            description=description,
            expected_output=f"Save the reviewed {stage} artifact using the required tool, or report denial.",
            agent=agent,
        )
        log_event(logger, f"pipeline_{stage}_started")
        self.Crew(
            agents=[agent], tasks=[task], process=self.Process.sequential, verbose=True
        ).kickoff()
        try:
            saved = self._saved_stage_text(tool_name, suffix, before)
        except Exception as exc:
            log_event(logger, f"pipeline_{stage}_failed", error=exc, level=logging.WARNING)
            return None
        log_event(logger, f"pipeline_{stage}_saved")
        return saved

    def build_tool_pipeline(self, tool_name: str, user_requirement: str) -> str:
        """Create in gated stages using the original request and approved artifacts.

        Each model task runs separately so a completion claim cannot launch the
        next role before the host verifies a fresh approved save. Only maintained
        ledger evidence and human acceptance can complete the final stage.
        """
        log_event(logger, "tool_pipeline_started")
        if self.verification is None:
            return "PIPELINE_STAGE_FAILED: specification: verification service unavailable."
        self.verification.invalidate(tool_name)
        requirement = (
            f"Original user requirement (preserve every constraint):\n{user_requirement}\n"
        )
        denial = "If a permission is denied, stop and report it. Never retry a rejected write.\n"
        specification = self._creation_stage(
            tool_name,
            "specification",
            "specifications.md",
            self.architect_agent,
            requirement
            + denial
            + f"Design tool '{tool_name}' as pure standalone top-level Python functions. "
            "Specify exact function/argument names, types, invalid-input behavior and return format. "
            "Do not weaken validation constraints or replace exact arithmetic with approximate rules. "
            f"MANDATORY: call 'Save Architectural Specifications' with tool_name='{tool_name}'.",
        )
        if specification is None:
            return "PIPELINE_STAGE_FAILED: specification: no fresh approved artifact."
        code = self._creation_stage(
            tool_name,
            "code",
            "code.py",
            self.coder_agent,
            requirement + denial + f"Tool name: {tool_name}.\n"
            f"Actual approved specification, read from persisted bytes:\n{specification}\n"
            "Implement only pure standalone top-level functions, not classes. "
            "Use explicit validation and English documentation. "
            f"MANDATORY: call 'Compile and Save Python Code' with tool_name='{tool_name}'. "
            "Returning Python text without invoking the save tool does not complete this stage.",
        )
        if code is None:
            return "PIPELINE_STAGE_FAILED: code: no fresh approved artifact."
        security = self.verification.security
        tests_path = security.validate_and_resolve_path(tool_name, f"{tool_name}_tests.py")
        before = security.get_artifact_receipt(tests_path)
        task = self.Task(
            description=requirement
            + denial
            + f"Tool name: {tool_name}.\nActual approved specification:\n{specification}\n"
            f"Actual approved implementation:\n{code}\n"
            f"Write meaningful unittest tests importing from {tool_name}_code. "
            "Cover normal inputs, boundaries, invalid types and exact return types. "
            "MANDATORY: call 'Run and Save Unit Tests'. Never weaken an assertion to hide a defect. "
            "After TESTS_PROVISIONAL_PASSED call 'Submit Acceptance Cases for Human Review' "
            "with version-1 declarative cases. Only ACCEPTANCE_VERIFIED completes this task. "
            "If checks fail, report the failure; if review is rejected, stop without reprompting.",
            expected_output="Actual provisional tests and human-approved acceptance evidence, or failure.",
            agent=self.tester_agent,
        )
        log_event(logger, "pipeline_acceptance_started")
        self.Crew(
            agents=[self.tester_agent], tasks=[task], process=self.Process.sequential, verbose=True
        ).kickoff()
        try:
            self._saved_stage_text(tool_name, "tests.py", before)
            # Testing/acceptance may take minutes. Revoke if the implementation
            # or requirement changed since its approved stage, even if the new
            # bytes happened to pass the selected acceptance cases.
            if (
                self._saved_stage_text(tool_name, "code.py", None) != code
                or self._saved_stage_text(tool_name, "specifications.md", None) != specification
            ):
                raise ValueError("An approved stage changed during testing")
        except Exception as exc:
            self.verification.invalidate(tool_name)
            log_event(logger, "pipeline_acceptance_failed", error=exc, level=logging.WARNING)
            return "PIPELINE_STAGE_FAILED: acceptance: no fresh approved tests."
        if not self.verification.is_verified(tool_name):
            log_event(logger, "pipeline_acceptance_failed", level=logging.WARNING)
            return "PIPELINE_STAGE_FAILED: acceptance: no current human-approved evidence."
        log_event(logger, "pipeline_acceptance_verified")
        return "ACCEPTANCE_VERIFIED: creation stages completed with host evidence."

    def run_system(self, user_query: str) -> str:
        """Run one bounded manager decision under correlated diagnostic context."""
        if not isinstance(user_query, str) or len(user_query) > 16000:
            raise ValueError("Query exceeds the 16000 character limit")
        if not _WORK_CAPACITY.acquire(blocking=False):
            raise ValueError(
                "Active workflow capacity reached; retry after another operation finishes"
            )
        try:
            with operation_scope() as operation_id:
                if self.verification is not None:
                    self.verification.security.operation_id = operation_id
                log_event(logger, "manager_started")
                try:
                    result = self._run_system(user_query)
                except Exception as exc:
                    log_event(logger, "manager_failed", error=exc, level=logging.ERROR)
                    raise
                log_event(logger, "manager_finished")
                return result
        finally:
            _WORK_CAPACITY.release()

    def _run_system(self, user_query: str) -> str:
        """
        Main manager orchestrator: checks existing tools or builds a new one.
        """
        # Payloads are passed to the model, never copied into routine diagnostics.
        existing_tools = self.get_installed_tools_catalog()  # get_installed_tools()
        decision_agent = (
            self.creation_manager_agent
            if existing_tools == "No tools installed yet."
            else self.manager_agent
        )

        manager_task = self.Task(
            description=(
                f"User Query: '{user_query}'\n"
                f"Already installed tools on disk: {existing_tools}\n\n"
                "Decision Rules:\n"
                "Only verify a tool actually listed in the catalog. If the catalog is empty, "
                "do not call Verify Existing Tool or guess a tool name: return CREATE_TOOL JSON.\n"
                "1. If an installed tool can answer this query, first call 'Verify Existing Tool'. "
                "If it returns REUSE_READY, use its approved function signatures and the ORIGINAL query "
                "to call Execute Generated Tool immediately with appropriate new arguments. Do not read or "
                "display code, run tests or submit acceptance for REUSE_READY. Sensitive calls are gated by the host. "
                "Only if it returns TESTS_PROVISIONAL_PASSED, read the requirements/code and call "
                "'Read Artifact Tool' using the exact artifact filenames listed in the catalog. Then call "
                "'Submit Acceptance Cases for Human Review' with version-1 declarative cases "
                "(id, purpose, function, kwargs, expect), including expected values or exceptions. "
                "Only after ACCEPTANCE_VERIFIED call 'Execute Generated Tool' and provide the final answer. "
                "If verification fails, report the failure; never invent a successful result.\n"
                "2. If NO installed tool is suitable, output STRICTLY a JSON block in this exact format and nothing else:\n"
                "```json\n"
                "{\n"
                '  "action": "CREATE_TOOL",\n'
                '  "tool_name": "<snake_case_tool_name>",\n'
                '  "purpose": "<clear explanation of what calculation/function is needed>"\n'
                "}\n"
                "```"
            ),
            expected_output="Direct answer using existing tool OR JSON to trigger new tool creation.",
            agent=decision_agent,
        )

        manager_crew = self.Crew(
            agents=[decision_agent],
            tasks=[manager_task],
            process=self.Process.sequential,
            verbose=True,
        )

        manager_decision = str(manager_crew.kickoff())

        decision = parse_manager_response(manager_decision)
        if isinstance(decision, CreateToolDecision):
            tool_name, purpose = decision.tool_name, decision.purpose
            log_event(logger, "tool_creation_requested")

            # Execute creation pipeline: Architect -> Coder -> Tester
            if self.verification is not None:
                self.verification.invalidate(tool_name)
            pipeline = self.build_tool_pipeline(
                tool_name=tool_name,
                user_requirement=f"{user_query}\n\nManager purpose (additional context only): {purpose}",
            )
            if isinstance(pipeline, str) and pipeline.startswith("PIPELINE_STAGE_FAILED:"):
                return pipeline

            if self.verification is None or not self.verification.is_verified(tool_name):
                log_event(logger, "tool_pipeline_not_verified", level=logging.WARNING)
                return "PIPELINE_NOT_VERIFIED: No current successful isolated test evidence."

            # Run final task where Manager executes the verified tool
            context = self.verification.acceptance_context(tool_name)
            if context is None:
                return "PIPELINE_NOT_VERIFIED: Accepted execution context is unavailable."
            # Require a fresh call after the handoff, not a call made earlier in
            # testing or acceptance. This never grants execution authorization.
            self.verification.begin_execution()
            final_execution_task = self.Task(
                description=(
                    f"The tool '{tool_name}' passed the human-approved acceptance cases for this operation. "
                    f"This is not proof of correctness for every possible input. Do not re-run provisional "
                    f"verification here, because that revokes acceptance.\n"
                    f"Host-validated handoff (finite reviewed cases, not universal proof):\n"
                    f"{json.dumps(context, ensure_ascii=True)}\n"
                    f"Select an approved function and derive kwargs from the ORIGINAL query, not from a sample case. "
                    f"Use 'Execute Generated Tool' with tool_name='{tool_name}' to solve the user query: '{user_query}'."
                ),
                expected_output="Final result answering the user query.",
                agent=self.manager_agent,
            )

            final_crew = self.Crew(
                agents=[self.manager_agent], tasks=[final_execution_task], verbose=True
            )
            final_crew.kickoff()
            return self._execution_answer()

        if self.verification is not None and self.verification.has_execution_activity():
            return self._execution_answer()
        return decision

    def _execution_answer(self) -> str:
        """Render observed arguments/result, never certify unsupported model prose."""
        result = self.verification.execution_result()
        if result is None:
            log_event(logger, "final_execution_missing", level=logging.WARNING)
            return "EXECUTION_NOT_VERIFIED: No current successful isolated tool execution."
        log_event(logger, "final_execution_observed")
        return (
            f"Host-observed execution: {result['tool_name']}.{result['function_name']}\n"
            f"Arguments: {json.dumps(result['kwargs'], ensure_ascii=True)}\n"
            f"Result: {result['result']}"
        )
