"""Human-reviewed declarative cases and host-owned deterministic verdicts.

Generated unittest counts are only provisional. Only this maintained evaluator
compares approved expectations with isolated observations and requests execution
authorization. Expected values and the acceptance contract never enter a child.
"""

import hashlib
import json
import logging
import math
import re
import threading
from copy import deepcopy
from typing import Any

from .contracts import ExecutionBackend, SecurityBoundary
from .diagnostics import log_event
from .verification import VerificationLedger

logger = logging.getLogger(__name__)
_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,127}")


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject ambiguous duplicate JSON keys at every nesting level."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def validate_json(value: Any, depth: int = 0) -> None:
    """Bound JSON nesting/values and reject nonfinite or non-data objects."""
    if depth > 16:
        raise ValueError("JSON nesting exceeds 16")
    if value is None or type(value) in (bool, int):
        return
    if type(value) is float and math.isfinite(value):
        return
    if type(value) is str and len(value) <= 8192:
        return
    if type(value) in (list, dict) and len(value) <= 256:
        if isinstance(value, dict):
            if not all(type(key) is str and len(key) <= 128 for key in value):
                raise ValueError("Invalid object key")
            value = list(value.values())
        for item in value:
            validate_json(item, depth + 1)
        return
    raise ValueError("Unsupported, oversized or nonfinite JSON value")


def parse_contract(text: str) -> dict[str, Any]:
    """Parse bounded version-1 data only; executable assertions are unsupported."""
    if not isinstance(text, str) or len(text.encode("utf-8")) > 65536:
        raise ValueError("Acceptance JSON exceeds 64 KiB")
    try:
        contract = json.loads(text, object_pairs_hook=_unique)
        validate_json(contract)
    except (RecursionError, UnicodeError) as exc:
        raise ValueError("Invalid acceptance JSON") from exc
    if (
        not isinstance(contract, dict)
        or set(contract) != {"version", "cases"}
        or type(contract["version"]) is not int
        or contract["version"] != 1
        or not isinstance(contract["cases"], list)
        or not 1 <= len(contract["cases"]) <= 16
    ):
        raise ValueError("Require version 1 and one to sixteen cases")
    seen = set()
    for case in contract["cases"]:
        if not isinstance(case, dict) or set(case) != {
            "id",
            "purpose",
            "function",
            "kwargs",
            "expect",
        }:
            raise ValueError("Invalid acceptance case fields")
        if (
            not isinstance(case["id"], str)
            or not _NAME.fullmatch(case["id"])
            or case["id"] in seen
            or not isinstance(case["purpose"], str)
            or not case["purpose"].strip()
            or len(case["purpose"]) > 500
            or not isinstance(case["function"], str)
            or not _NAME.fullmatch(case["function"])
            or not isinstance(case["kwargs"], dict)
            or not all(key.isidentifier() and not key.startswith("_") for key in case["kwargs"])
        ):
            raise ValueError("Invalid case identity, purpose, function or inputs")
        seen.add(case["id"])
        expected = case["expect"]
        if not isinstance(expected, dict):
            raise ValueError("Expectation must be an object")
        kind = expected.get("kind")
        if kind == "value" and set(expected) == {"kind", "value"}:
            continue
        if (
            kind == "raises"
            and set(expected) == {"kind", "type"}
            and isinstance(expected["type"], str)
            and _NAME.fullmatch(expected["type"])
        ):
            continue
        if (
            kind == "approx"
            and set(expected) == {"kind", "value", "abs_tol", "rel_tol"}
            and all(type(expected[key]) in (int, float) for key in ("value", "abs_tol", "rel_tol"))
            and expected["abs_tol"] >= 0
            and expected["rel_tol"] >= 0
        ):
            continue
        raise ValueError("Invalid expectation or comparison rule")
    return contract


def _same(left: Any, right: Any) -> bool:
    """Compare recursively without Python's boolean/numeric equality coercion."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(_same(left[key], right[key]) for key in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(
            _same(a, b) for a, b in zip(left, right, strict=True)
        )
    return left == right


def matches_expectation(observation: Any, expected: dict[str, Any]) -> bool:
    """Compare data outside the child; a child success/count assertion is irrelevant."""
    try:
        validate_json(observation)
        if not isinstance(observation, dict) or observation.get("kind") != "observation":
            return False
        if expected["kind"] == "raises":
            return (
                set(observation) == {"kind", "status", "exception_type"}
                and observation["status"] == "raised"
                and observation["exception_type"] == expected["type"]
            )
        if set(observation) != {"kind", "status", "value"} or observation["status"] != "returned":
            return False
        actual = observation["value"]
        if expected["kind"] == "value":
            return _same(actual, expected["value"])
        return (
            expected["kind"] == "approx"
            and type(actual) in (int, float)
            and math.isclose(
                actual, expected["value"], abs_tol=expected["abs_tol"], rel_tol=expected["rel_tol"]
            )
        )
    except (ValueError, KeyError, OverflowError, TypeError):
        return False


class AcceptanceEvaluator:
    """Coordinate mandatory human review and compare fresh isolated observations."""

    def __init__(
        self, security: SecurityBoundary, sandbox: ExecutionBackend, ledger: VerificationLedger
    ) -> None:
        """Bind one session's review, backend and authorization ledger."""
        self.security, self.sandbox, self.ledger = security, sandbox, ledger
        self._lock = threading.RLock()
        self._busy = threading.Lock()
        self._status: dict[str, Any] = {"stage": "not_started", "cases": []}
        self._rejected_operation: tuple[str, str] | None = None

    def status(self) -> dict[str, Any]:
        """Return an independent display snapshot; never reveal a capability token."""
        with self._lock:
            result = deepcopy(self._status)
        if result["stage"] == "verified" and not self.ledger.is_verified(result["tool"]):
            result["stage"] = "invalidated"
        return result

    def note_provisional(self, tool_name: str, result: str) -> None:
        """Display automatic checks separately from human/final acceptance."""
        self._set(
            "provisional_passed"
            if result.startswith("TESTS_PROVISIONAL_PASSED:")
            else "provisional_failed",
            tool=tool_name,
            cases=[],
            contract_digest="",
            provisional_result=result[:8192],
            approved_contract=None,
        )

    def _set(self, stage: str, **details: Any) -> None:
        """Publish a coherent stage and log only the fixed stage event."""
        with self._lock:
            self._status.update(stage=stage, **details)
        log_event(logger, "acceptance_" + stage)

    def submit(self, tool_name: str, cases_json: str) -> str:
        """Review generated cases and authorize only host-compared human-approved data."""
        if not self._busy.acquire(blocking=False):
            return "ACCEPTANCE_FAILED: Another review is active."
        try:
            if self._rejected_operation == (self.security.owner_id, self.security.operation_id):
                self._set("rejected")
                return "ACCEPTANCE_REJECTED: Start a new user query to request another review."
            return self._submit(tool_name, cases_json)
        except Exception as exc:
            self.ledger.invalidate(tool_name)
            self._set("failed")
            log_event(logger, "acceptance_error", error=exc, level=logging.WARNING)
            return "ACCEPTANCE_FAILED: Invalid cases, changed artifacts or isolated evaluation failure."
        finally:
            self._busy.release()

    def _submit(self, tool_name: str, cases_json: str) -> str:
        """Keep expected values exclusively in the trusted parent process."""
        # A malformed model proposal is still reviewable data, not executable
        # input. Bound it before display, then require a valid edited contract
        # after explicit human approval. Never repair/execute it automatically.
        if not isinstance(cases_json, str) or len(cases_json.encode("utf-8")) > 65536:
            raise ValueError("Acceptance proposal exceeds 64 KiB")
        summary = "Provisional tests passed. Review each purpose, input and expected result. Approval is mandatory and authorizes only these cases, not all-input correctness."
        try:
            proposed = parse_contract(cases_json)
            review_text = json.dumps(proposed, indent=2, ensure_ascii=True)
        except ValueError:
            review_text = cases_json
            summary += " The generated proposal is invalid JSON or violates the case schema. Correct it before approval."
            log_event(logger, "acceptance_proposal_needs_correction", level=logging.WARNING)
        if not self.ledger.is_provisional(tool_name):
            raise ValueError("Current provisional tests are required")
        code, tests = self.ledger.snapshot(tool_name)
        identity = (self.security.owner_id, self.security.operation_id)
        self.ledger.revoke_acceptance(tool_name)
        self._set("pending_review", tool=tool_name, cases=[], contract_digest="")
        accepted, edited = self.security.request_user_permission(
            f"Acceptance cases for {tool_name}",
            "review_acceptance",
            review_text,
            require_manual=True,
            review_context={
                "python_tests": tests.decode("utf-8", errors="replace"),
                "provisional_result": self.status().get("provisional_result", ""),
                "summary": summary,
            },
        )
        if not accepted:
            self._rejected_operation = identity
            self.ledger.invalidate(tool_name)
            self._set("rejected")
            return "ACCEPTANCE_REJECTED: Human approval was denied, cancelled or expired."
        approved = parse_contract(edited)
        digest = hashlib.sha256(
            json.dumps(approved, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
        ).hexdigest()
        self._set("evaluating", contract_digest=digest, approved_contract=deepcopy(approved))
        verdicts = []
        for case in approved["cases"]:
            if (
                identity != (self.security.owner_id, self.security.operation_id)
                or self.security.is_closed()
                or not self.ledger.is_provisional(tool_name)
                or not self.ledger.matches(tool_name, code, tests)
            ):
                raise ValueError("Reviewed work changed")
            observed = self.sandbox.evaluate(code, tool_name, case["function"], case["kwargs"])
            passed = (
                observed.isolated is True
                and observed.exit_code == 0
                and not observed.failure
                and matches_expectation(observed.report, case["expect"])
            )
            verdicts.append(
                {
                    "id": case["id"],
                    "passed": passed,
                    "expected": deepcopy(case["expect"]),
                    "observed": deepcopy(observed.report),
                    "process_failure": observed.failure
                    or ("child_exit" if observed.exit_code else ""),
                }
            )
            self._set("evaluating", cases=deepcopy(verdicts))
            if not passed:
                raise ValueError("Approved case failed")
        if identity != (
            self.security.owner_id,
            self.security.operation_id,
        ) or not self.ledger.authorize(
            tool_name,
            code,
            tests,
            digest,
            frozenset(case["function"] for case in approved["cases"]),
            reviewed_contract=approved,
        ):
            raise ValueError("Acceptance publication rejected")
        self._set("verified")
        return f"ACCEPTANCE_VERIFIED: {len(verdicts)} approved cases passed. Contract SHA-256: {digest}"
