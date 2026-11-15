"""Explicit repair of rejected tool source/tests; native validation and manual acceptance."""

import ast
import hashlib
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path

from agentix.storage.catalog_lock import CatalogLock, reject_alias

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class RejectedTool:
    """Owner-retained proposed buffers; these values never authorize execution."""

    tool_name: str
    code: str
    tests: str
    specification: str = ""


def _member(security, name: str, suffix: str) -> Path:
    """Resolve only a conventional member; reject file aliases before reads/writes."""
    expected = Path(security.TOOLS_ROOT_DIR).resolve() / name / (name + suffix)
    resolved = Path(security.validate_and_resolve_path(name, name + suffix))
    reject_alias(expected)
    if resolved != expected or (
        expected.exists() and (not expected.is_file() or expected.stat().st_nlink != 1)
    ):
        raise ValueError("Tool repair member aliases are forbidden")
    return expected


def capture_rejection(controller, pending: dict) -> RejectedTool | None:
    """Retain only an actually denied code/test/specification/acceptance proposal."""
    security = controller.security
    value = str(pending.get("filepath", ""))
    if pending.get("action") == "review_acceptance":
        match = re.fullmatch(r"Acceptance cases for ([A-Za-z][A-Za-z0-9_]{0,127})", value)
        name = match[1] if match else ""
    else:
        candidate = Path(value)
        name = candidate.parent.name
        if not name or candidate.name not in {
            name + "_code.py",
            name + "_tests.py",
            name + "_specifications.md",
        }:
            return None
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,127}", name):
        return None
    buffers = {}
    for key, suffix in (
        ("code", "_code.py"),
        ("tests", "_tests.py"),
        ("specification", "_specifications.md"),
    ):
        path = _member(security, name, suffix)
        if pending.get("action") != "review_acceptance" and Path(value) == path:
            text = pending.get("content", "")
        elif path.exists():
            with path.open(encoding="utf-8") as stream:
                text = stream.read(65537)
        else:
            text = ""
        if not isinstance(text, str) or len(text.encode("utf-8")) > 65536:
            raise ValueError("Rejected proposal exceeds its repair limit")
        buffers[key] = text
    return RejectedTool(name, **buffers)


class ToolRepair:
    """Save user-reviewed buffers and explicitly restart the existing validation gates."""

    def __init__(self, security, operations, apps, *, propose_cases, on_saved=None, capacity=None):
        """Inject metadata, native tool operations and a data-only proposal boundary."""
        from agentix.application.tool_workflow import _WORK_CAPACITY

        self.security, self.operations, self.apps = security, operations, apps
        self.propose_cases, self.on_saved = propose_cases, on_saved
        self.capacity = _WORK_CAPACITY if capacity is None else capacity

    def save_and_validate(self, draft: RejectedTool, code: str, tests: str) -> str:
        """Validate both buffers, revoke old grants, save and perform fresh validation.

        Save is an explicit owner action, not an authorization to execute. Native
        unittest success remains provisional. The generated cases require manual
        review and host comparison. A successful value case is executed through
        the normal permission-aware tool executor to establish durable reuse.
        """
        if not isinstance(draft, RejectedTool) or not re.fullmatch(
            r"[a-z][a-z0-9_]{0,63}", draft.tool_name
        ):
            raise ValueError("Select a rejected tool compatible with the native runner")
        for value in (code, tests):
            if (
                not isinstance(value, str)
                or not value.strip()
                or len(value.encode("utf-8")) > 65536
            ):
                raise ValueError("Both code and tests must contain at most 64 KiB")
        try:
            compile(code, draft.tool_name + "_code.py", "exec")
            compile(tests, draft.tool_name + "_tests.py", "exec")
        except (SyntaxError, ValueError, RecursionError):
            raise ValueError("Code or tests do not compile; no files were saved") from None
        if getattr(self.security, "strict_tool_contract", False):
            from agentix.domain.tool_schema import extract_tool_schema

            extract_tool_schema(draft.tool_name, code)
        if not self.capacity.acquire(blocking=False):
            raise ValueError("Four workflows are already running; retry later")
        try:
            self.security.begin_tool_draft(draft.tool_name)
            with CatalogLock(self.apps.root.parent):
                if self.apps.dependency_references(draft.tool_name):
                    raise ValueError(
                        "Installed application dependencies block editing this shared tool"
                    )
                code_path = _member(self.security, draft.tool_name, "_code.py")
                tests_path = _member(self.security, draft.tool_name, "_tests.py")
                specification_path = _member(self.security, draft.tool_name, "_specifications.md")
                self.operations.verification.invalidate(draft.tool_name)
                code_path.parent.mkdir(parents=True, exist_ok=True)
                code_path.write_bytes(code.encode("utf-8"))
                tests_path.write_bytes(tests.encode("utf-8"))
                specification_path.write_bytes(draft.specification.encode("utf-8"))
                identity = (self.security.owner_id, self.security.operation_id)
                for path in (code_path, tests_path, specification_path):
                    self.security.record_saved_artifact(
                        str(path),
                        hashlib.sha256(path.read_bytes()).hexdigest(),
                        owner_id=identity[0],
                        operation_id=identity[1],
                    )
                if self.on_saved is not None:
                    self.on_saved(RejectedTool(draft.tool_name, code, tests, draft.specification))
            provisional = self.operations.verify_existing_tool_tool(draft.tool_name)
            if not provisional.startswith("TESTS_PROVISIONAL_PASSED"):
                return provisional
            logger.info("event=repaired_tool_provisional_passed")
            proposal = self.propose_cases(
                {
                    "tool_name": draft.tool_name,
                    "specification": draft.specification,
                    "code": code,
                    "tests": tests,
                    "functions": [
                        node.name
                        for node in ast.parse(code).body
                        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
                    ],
                }
            )
            if not isinstance(proposal, str) or len(proposal.encode("utf-8")) > 65536:
                raise ValueError("Acceptance proposal exceeds its limit")
            result = self.operations.submit_acceptance_cases_tool(draft.tool_name, proposal)
            if not result.startswith("ACCEPTANCE_VERIFIED"):
                return result
            self.security.publish_current_draft(draft.tool_name)
            context = self.operations.verification.acceptance_context(draft.tool_name)
            for case in context["reviewed_contract"]["cases"]:
                if case["expect"]["kind"] == "value":
                    sample = self.operations.execute_generated_tool_tool(
                        draft.tool_name, case["function"], json.dumps(case["kwargs"])
                    )
                    return result + "\nReviewed sample execution: " + sample
            return (
                result
                + "\nNo normal value case was supplied; durable reuse awaits an approved execution."
            )
        finally:
            self.security.restore_public_tool_storage()
            self.capacity.release()
