"""REUSE-001: exact reviewed tools may serve later queries in the same session."""

from types import SimpleNamespace

import pytest
from test_execution_handoff import authorize_fixture


def successful_tool(system):
    """Establish review and actual execution using independently authored code."""
    ledger = authorize_fixture(system)
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":10}').endswith(
        "12"
    )
    return ledger


def test_second_query_reuses_without_tests_review_or_reading_code(system, monkeypatch):
    """A real service call with new inputs must yield a fresh observed result."""
    successful_tool(system)

    def forbidden(*args, **kwargs):
        """Fail on any repeated review, artifact read or unittest execution."""
        pytest.fail("Normal reuse must not test, display code or request approval")

    monkeypatch.setattr(system.security, "request_user_permission", forbidden)
    monkeypatch.setattr(system.custom_tools.runner, "verify_existing_tool", forbidden)
    monkeypatch.setattr(system.custom_tools, "read_artifact_tool", forbidden)

    def kickoff():
        """Replace only LLM choice; exercise real preparation and execution."""
        prepared = system.custom_tools.verify_existing_tool_tool("adder")
        assert prepared.startswith("REUSE_READY:")
        assert "add(a: int, b: int=2) -> int" in prepared
        assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}').endswith(
            "42"
        )
        return "Invented 999"

    monkeypatch.setattr(system.main, "Crew", lambda **kw: SimpleNamespace(kickoff=kickoff))
    result = system.main.run_system("Please add two to forty.")
    assert "42" in result and '"a": 40' in result and "999" not in result


def test_review_without_successful_call_does_not_grant_reuse(system):
    """A review alone must not establish later-operation authorization."""
    ledger = authorize_fixture(system)
    system.security.operation_id = "next"
    assert not ledger.prepare_reuse("adder")


@pytest.mark.parametrize("change", ["code", "tests", "owner", "closed", "revoked"])
def test_reuse_rejects_drift_owner_and_revocation(system, change):
    """Observed edits and owner/lifecycle changes cannot revive earlier trust."""
    ledger = successful_tool(system)
    system.security.operation_id = "next"
    if change in ("code", "tests"):
        path = system.root / "adder" / f"adder_{change}.py"
        original = path.read_bytes()
        path.write_bytes(original + b"\n# changed")
        assert not ledger.prepare_reuse("adder")
        path.write_bytes(original)
    elif change == "owner":
        system.security.owner_id = "someone-else"
    elif change == "closed":
        system.security.cancel_pending()
    else:
        ledger.revoke_acceptance("adder")
    assert not ledger.prepare_reuse("adder")


def test_successful_tool_does_not_authorize_unreviewed_function(system):
    """Reusable grants retain the approved public-function boundary."""
    ledger = successful_tool(system)
    system.security.operation_id = "next"
    assert ledger.prepare_reuse("adder")
    assert "TOOL_NOT_VERIFIED" in system.custom_tools.execute_generated_tool_tool(
        "adder", "other", "{}"
    )


def test_sensitive_call_needs_manual_permission_even_after_review(system, monkeypatch):
    """File-capable code cannot inherit silent execution from acceptance."""
    folder = system.root / "adder"
    ledger = authorize_fixture(system)
    (folder / "adder_code.py").write_text(
        "def add(a, b=2):\n    if a < 0: open('output.txt', 'w')\n    return a+b"
    )
    code, tests = ledger.snapshot("adder")
    assert ledger.record(
        "adder",
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    assert ledger.authorize("adder", code, tests, "reviewed", frozenset({"add"}))
    requests = []

    def deny(*args, **kwargs):
        """Capture server-owned exact-call details and deny the sensitive action."""
        requests.append((args, kwargs))
        return False, ""

    monkeypatch.setattr(system.security, "request_user_permission", deny)
    outcome = system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}')
    assert outcome.startswith("EXECUTION_DENIED:")
    assert len(requests) == 1 and requests[0][1]["require_manual"] is True
    assert requests[0][0][1] == "execute_sensitive_tool"
    assert ledger.execution_result() is None


@pytest.mark.parametrize(
    "source,expected",
    [
        ("def add(a,b): return a+b", True),
        ("import math\ndef root(x): return math.sqrt(x)", True),
        ("def count(text): return len(text.split())", True),
        (
            "def check(x):\n    if not isinstance(x, (int,float)): raise TypeError('number')\n    return round(x,2)",
            True,
        ),
        ("def write(x): return open(x,'w')", False),
        ("import requests\ndef send(x): return requests.post(x)", False),
        ("def dynamic(x): return getattr(x,'write')('data')", False),
        ("def dynamic(x): return x()", False),
        ("def hidden(x): return x.__class__", False),
        ("class C: pass", False),
        ("def f(x): return eval(x)", False),
        ("import typing\ndef f(x): return typing.get_type_hints(x)", False),
        ("def f(x): return x.format(secret='value')", False),
    ],
)
def test_computation_classifier_is_conservative(source, expected):
    """Only explicit computation constructs avoid the per-call permission gate."""
    from agentix.reuse_policy import computation_only

    assert computation_only(source.encode()) is expected


@pytest.mark.parametrize("mutation", ["none", "code", "operation"])
def test_sensitive_approval_is_per_call_and_rechecks_waiting_state(system, monkeypatch, mutation):
    """An approved dialog neither changes arguments nor overrides concurrent drift."""
    ledger = authorize_fixture(system)
    path = system.root / "adder" / "adder_code.py"
    path.write_text("def add(a,b=2):\n    if a < 0: open('output.txt','w')\n    return a+b")
    code, tests = ledger.snapshot("adder")
    assert ledger.record(
        "adder",
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    assert ledger.authorize("adder", code, tests, "reviewed", frozenset({"add"}))
    seen = []

    def approve(*args, **kwargs):
        """Approve only the captured call, simulating a mutation during the wait."""
        seen.append(args)
        if mutation == "code":
            path.write_text("def add(a,b=2): return 999")
        elif mutation == "operation":
            system.security.operation_id = "concurrent-query"
        return True, "ignored edited arguments"

    monkeypatch.setattr(system.security, "request_user_permission", approve)
    first = system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}')
    if mutation != "none":
        assert first.startswith("TOOL_NOT_VERIFIED:")
        assert ledger.execution_result() is None
    else:
        assert first.endswith("42")
        system.security.operation_id = "next-query"
        assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":10}').endswith(
            "12"
        )
        assert len(seen) == 2


def test_new_ledger_cannot_import_session_grant_from_same_artifacts(system):
    """Disk artifacts and another session's success never establish reuse trust."""
    from agentix.verification import VerificationLedger

    successful_tool(system)
    other = VerificationLedger(system.security)
    assert not other.prepare_reuse("adder")
    assert not other.is_verified("adder", "add")


def test_status_polling_does_not_destroy_unchanged_later_query_grant(system):
    """Read-only UI status may expire a receipt without losing session approval."""
    ledger = successful_tool(system)
    system.security.operation_id = "later-query"
    assert ledger.execution_result() is None
    assert not ledger.is_verified("adder")
    assert ledger.prepare_reuse("adder")
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":5}').endswith("7")
