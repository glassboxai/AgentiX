"""Per-runtime, content-bound observations; model output never creates evidence.

Provisional unittest reports alone never authorize execution. Additional host
acceptance records bind a human-reviewed contract, covered functions and evaluator
version to exact artifact bytes. Successful calls establish bounded session grants
and, when configured, Windows-protected durable approvals. Result receipts remain query-bound. Finite cases do not prove
all-input correctness.
"""

import ast
import copy
import hashlib
import logging
import threading
from pathlib import Path
from typing import Any

from .approval_store import ApprovalStore
from .contracts import SecurityBoundary
from .diagnostics import log_event

logger = logging.getLogger(__name__)


class VerificationLedger:
    """Own query receipts, bounded session grants and injected durable approval storage."""

    def __init__(self, security: SecurityBoundary, *, store: ApprovalStore | None = None) -> None:
        """Bind evidence to one approval owner and its current operation."""
        self.security = security
        self.store = store
        self._owner = security.owner_id
        self._lock = threading.RLock()
        self._records: dict[str, tuple[str, str, bytes]] = {}
        self._acceptance: dict[str, tuple[tuple[str, str, bytes], str, frozenset[str], str]] = {}
        self._contracts: dict[str, dict[str, Any]] = {}
        self._execution: tuple[tuple[str, str, bytes], str, dict[str, Any]] | None = None
        self._attempt: tuple[str, str] | None = None
        # Session cache; optional durable records live outside tool artifact storage.
        self._reuse: dict[str, tuple[str, bytes, bytes, str, frozenset[str], dict[str, Any]]] = {}

    def snapshot(self, tool_name: str) -> tuple[bytes, bytes]:
        """Read only the two explicitly validated runtime artifacts, never import."""
        paths = [
            self.security.validate_and_resolve_path(tool_name, f"{tool_name}_{part}.py")
            for part in ("code", "tests")
        ]
        # Bound memory and prevent unrelated directory traversal/enumeration.
        result = []
        for path in paths:
            with Path(path).open("rb") as stream:
                data = stream.read(1_048_577)
            if len(data) > 1_048_576:
                raise ValueError("Artifact exceeds the 1 MiB execution input limit")
            result.append(data)
        return result[0], result[1]

    def _identity(self, code: bytes, tests: bytes) -> tuple[str, str, bytes]:
        """Separate owner/run identity from an unambiguous length-framed digest."""
        digest = hashlib.sha256(len(code).to_bytes(8, "big") + code + tests).digest()
        return self.security.owner_id, self.security.operation_id, digest

    def invalidate(self, tool_name: str) -> None:
        """Revoke previous evidence before any new pipeline or test attempt."""
        with self._lock:
            self._revoke_stored(tool_name)
            self._reuse.pop(tool_name, None)
            self._records.pop(tool_name, None)
            self._acceptance.pop(tool_name, None)
            self._contracts.pop(tool_name, None)
            if self._execution and self._execution[2]["tool_name"] == tool_name:
                self._execution = None

    def record(
        self,
        tool_name: str,
        code: bytes,
        tests: bytes,
        report: Any,
        *,
        isolated: bool,
        exit_code: int,
    ) -> bool:
        """Accept only nonempty, unskipped successful observations of current bytes."""
        self.invalidate(tool_name)
        counts = ("run", "failures", "errors", "skipped")
        valid = (
            isolated is True
            and type(exit_code) is int
            and exit_code == 0
            and isinstance(report, dict)
            and report.get("kind") == "tests"
            and all(type(report.get(key)) is int and report[key] >= 0 for key in counts)
            and report["run"] > 0
            and report.get("successful") is True
            and all(report[key] == 0 for key in counts[1:])
        )
        if not valid:
            return False
        # A suite that never imports the implementation cannot establish even
        # syntax validity. Compile both exact snapshots without executing them.
        try:
            compile(code, f"{tool_name}_code.py", "exec")
            compile(tests, f"{tool_name}_tests.py", "exec")
        except (SyntaxError, ValueError, RecursionError):
            return False
        with self._lock:
            try:
                current = self.snapshot(tool_name)
            except (OSError, ValueError):
                return False
            if current != (code, tests):
                return False
            # Retain at most one tool observation: one creation pipeline per run.
            self._records.clear()
            self._records[tool_name] = self._identity(code, tests)
        return True

    def is_provisional(self, tool_name: str) -> bool:
        """Check current unittest observations; these never authorize execution."""
        with self._lock:
            try:
                code, tests = self.snapshot(tool_name)
            except (OSError, ValueError):
                self.invalidate(tool_name)
                return False
            if self._records.get(tool_name) != self._identity(code, tests):
                grant = self._reuse.get(tool_name)
                # A new query expires receipts, not an unchanged session grant.
                # UI status polling must not revoke reuse before preparation.
                if (
                    grant is None
                    or grant[0] != self.security.owner_id
                    or grant[1:3] != (code, tests)
                ):
                    self.invalidate(tool_name)
                return False
            return True

    def authorize(
        self,
        tool_name: str,
        code: bytes,
        tests: bytes,
        contract_digest: str,
        functions: frozenset[str],
        *,
        reviewed_contract: dict[str, Any] | None = None,
    ) -> bool:
        """Publish host acceptance after human review; never call from child reports.

        This is an internal trusted service boundary, not a model-facing tool.
        Its caller must compare every approved case in the host evaluator first.
        """
        with self._lock:
            if (
                self.security.is_closed()
                or not functions
                or not contract_digest
                or not self.is_provisional(tool_name)
                or not self.matches(tool_name, code, tests)
            ):
                return False
            self._acceptance.clear()
            self._contracts.clear()
            self._execution = None
            self._acceptance[tool_name] = (
                self._identity(code, tests),
                contract_digest,
                functions,
                "acceptance-v1",
            )
            self._contracts[tool_name] = copy.deepcopy(reviewed_contract or {})
            return True

    def _revoke_stored(self, tool_name: str) -> None:
        """Best-effort disk revocation; never expose native/filesystem exception bodies."""
        if self.store is not None:
            try:
                self.store.revoke(tool_name)
            except (OSError, ValueError) as exc:
                log_event(
                    logger, "durable_approval_revoke_failed", error=exc, level=logging.WARNING
                )

    def revoke_acceptance(self, tool_name: str) -> None:
        """Revoke human acceptance while retaining a current provisional observation."""
        with self._lock:
            self._revoke_stored(tool_name)
            self._reuse.pop(tool_name, None)
            self._acceptance.pop(tool_name, None)
            self._contracts.pop(tool_name, None)
            self._execution = None

    def acceptance_context(self, tool_name: str) -> dict[str, Any] | None:
        """Return defensive reviewed data and AST signatures for the final manager.

        Only currently accepted bytes are parsed; no generated module is imported.
        The evaluator owns contract validation and host comparison before publication.
        """
        with self._lock:
            if not self.is_verified(tool_name):
                return None
            code, tests = self.snapshot(tool_name)
            approved = self._acceptance[tool_name]
            if not self.matches(tool_name, code, tests):
                return None
            functions = []
            for node in ast.parse(code).body:
                if isinstance(node, ast.FunctionDef) and node.name in approved[2]:
                    signature = f"{node.name}({ast.unparse(node.args)})"
                    if node.returns is not None:
                        signature += " -> " + ast.unparse(node.returns)
                    functions.append(signature)
            return {
                "tool_name": tool_name,
                "contract_digest": approved[1],
                "approved_functions": functions,
                "reviewed_contract": copy.deepcopy(self._contracts.get(tool_name, {})),
            }

    def begin_execution(self) -> None:
        """Clear earlier results even when a new call fails input validation."""
        with self._lock:
            self._execution = None
            self._attempt = (self.security.owner_id, self.security.operation_id)

    def has_execution_activity(self) -> bool:
        """Identify current-operation tool workflows without parsing model prose."""
        with self._lock:
            identity = (self.security.owner_id, self.security.operation_id)
            return self._attempt == identity or any(
                value[0][:2] == identity for value in self._acceptance.values()
            )

    def record_execution(
        self,
        tool_name: str,
        code: bytes,
        tests: bytes,
        function_name: str,
        kwargs: dict[str, Any],
        result: str,
    ) -> bool:
        """Record an isolated call observation after dispatch, never model prose.

        The trusted executor must validate process success first. Recheck exact
        source/acceptance after the child returns; revoke on edits during execution.
        Retain one bounded child result and a defensive copy of JSON arguments.
        """
        with self._lock:
            if (
                not isinstance(result, str)
                or len(result) > 262144
                or not self.matches_authorized(tool_name, code, tests, function_name)
            ):
                self._execution = None
                return False
            self._execution = (
                self._identity(code, tests),
                self._acceptance[tool_name][1],
                {
                    "tool_name": tool_name,
                    "function_name": function_name,
                    "kwargs": copy.deepcopy(kwargs),
                    "result": result,
                },
            )
            approved = self._acceptance[tool_name]
            self._reuse[tool_name] = (
                self.security.owner_id,
                code,
                tests,
                approved[1],
                approved[2],
                copy.deepcopy(self._contracts.get(tool_name, {})),
            )
            if self.store is not None:
                try:
                    self.store.save(
                        tool_name,
                        code,
                        tests,
                        approved[1],
                        approved[2],
                        self._contracts.get(tool_name, {}),
                    )
                    log_event(logger, "durable_approval_saved")
                except (OSError, ValueError, TypeError) as exc:
                    log_event(
                        logger, "durable_approval_save_failed", error=exc, level=logging.WARNING
                    )
            while len(self._reuse) > 64:
                self._reuse.pop(next(iter(self._reuse)))
            return True

    def prepare_reuse(self, tool_name: str) -> bool:
        """Rebind a successful reviewed tool to this query without running tests.

        Grants come from successful host-accepted calls in this session or the
        injected protected store. Cross-session reuse never transfers a result
        receipt. Exact bytes, policy and covered functions are checked; observed
        drift or explicit revocation removes trust. Closing one session does not
        revoke a durable approval owned by the Windows user.
        """
        with self._lock:
            if self.security.is_closed() or self.security.owner_id != self._owner:
                return False
            if self.store is not None:
                try:
                    code, tests = self.snapshot(tool_name)
                    stored = self.store.load(tool_name, code, tests)
                except (OSError, ValueError) as exc:
                    log_event(
                        logger, "durable_approval_load_failed", error=exc, level=logging.WARNING
                    )
                    self.invalidate(tool_name)
                    return False
                if stored is None:
                    if tool_name in self._reuse:
                        self.invalidate(tool_name)
                    return False
                self._reuse[tool_name] = (
                    self.security.owner_id,
                    code,
                    tests,
                    stored["digest"],
                    frozenset(stored["functions"]),
                    copy.deepcopy(stored["contract"]),
                )
            grant = self._reuse.get(tool_name)
            if grant is None:
                return False
            try:
                current = self.snapshot(tool_name)
                if (
                    self.security.is_closed()
                    or grant[0] != self.security.owner_id
                    or current != grant[1:3]
                ):
                    self.invalidate(tool_name)
                    return False
            except (OSError, ValueError):
                self.invalidate(tool_name)
                return False
            identity = self._identity(*current)
            self._records[tool_name] = identity
            self._acceptance[tool_name] = (identity, grant[3], grant[4], "acceptance-v1")
            self._contracts[tool_name] = copy.deepcopy(grant[5])
            return True

    def execution_result(self) -> dict[str, Any] | None:
        """Return a current host-observed call or nothing; stale evidence is revoked."""
        with self._lock:
            if not self._execution:
                return None
            identity, digest, observation = self._execution
            name, function = observation["tool_name"], observation["function_name"]
            if (
                identity[:2] != (self.security.owner_id, self.security.operation_id)
                or not self.is_verified(name, function)
                or self._records.get(name) != identity
                or self._acceptance[name][1] != digest
            ):
                self._execution = None
                return None
            return copy.deepcopy(observation)

    def is_verified(self, tool_name: str, function_name: str | None = None) -> bool:
        """Require host acceptance for the current bytes, owner, run and function."""
        with self._lock:
            approved = self._acceptance.get(tool_name)
            return bool(
                approved
                and not self.security.is_closed()
                and self.is_provisional(tool_name)
                and approved[0] == self._records.get(tool_name)
                and (function_name is None or function_name in approved[2])
            )

    def matches(self, tool_name: str, code: bytes, tests: bytes) -> bool:
        """Check the exact snapshot about to execute, avoiding a path-based race."""
        with self._lock:
            return self._records.get(tool_name) == self._identity(code, tests)

    def matches_authorized(
        self, tool_name: str, code: bytes, tests: bytes, function_name: str
    ) -> bool:
        """Atomically recheck both acceptance and the exact snapshot before dispatch."""
        with self._lock:
            return self.is_verified(tool_name, function_name) and self.matches(
                tool_name, code, tests
            )
