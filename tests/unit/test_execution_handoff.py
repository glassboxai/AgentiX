"""Host execution receipts prevent manager completion prose from becoming evidence."""

import json
from types import SimpleNamespace

import pytest


def authorize_fixture(system):
    """Install independently authored trusted code; bypass only the human fixture UI."""
    folder = system.root / "adder"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "adder_code.py").write_text("def add(a: int, b: int = 2) -> int: return a + b")
    (folder / "adder_tests.py").write_text("import unittest")
    ledger = system.custom_tools.verification
    code, tests = ledger.snapshot("adder")
    assert ledger.record(
        "adder",
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    contract = {
        "version": 1,
        "cases": [
            {
                "id": "sum_case",
                "purpose": "Add two numbers",
                "function": "add",
                "kwargs": {"a": 1},
                "expect": {"kind": "value", "value": 3},
            }
        ],
    }
    assert ledger.authorize(
        "adder", code, tests, "reviewed-contract", frozenset({"add"}), reviewed_contract=contract
    )
    return ledger


@pytest.mark.parametrize("execute", [False, True])
def test_creation_final_answer_requires_actual_current_execution(system, monkeypatch, execute):
    """Verify creation final answer requires actual current execution."""
    stages = []

    def crew(**kwargs):
        """Provide crew for the enclosing trusted test fixture."""
        stages.append(kwargs["tasks"][0].description)

        def kickoff():
            """Provide kickoff for the enclosing trusted test fixture."""
            if len(stages) == 1:
                return '{"action":"CREATE_TOOL","tool_name":"adder","purpose":"Add"}'
            if execute:
                assert (
                    system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}')
                    == "Tool Execution Result: 42"
                )
            return "Fabricated answer: 999"

        return SimpleNamespace(kickoff=kickoff)

    monkeypatch.setattr(system.main, "Crew", crew)
    monkeypatch.setattr(system.main, "build_tool_pipeline", lambda **kw: authorize_fixture(system))
    result = system.main.run_system("Add two to 40")
    if execute:
        assert "42" in result and '"a": 40' in result and "999" not in result
    else:
        assert result.startswith("EXECUTION_NOT_VERIFIED:") and "999" not in result
    assert "add(a: int, b: int=2) -> int" in stages[1]
    assert "reviewed-contract" in stages[1] and '"value": 3' in stages[1]


def test_execution_context_is_defensive_and_receipt_is_call_bound(system):
    """Verify execution context is defensive and receipt is call bound."""
    ledger = authorize_fixture(system)
    context = ledger.acceptance_context("adder")
    context["reviewed_contract"]["cases"].clear()
    assert ledger.acceptance_context("adder")["reviewed_contract"]["cases"]
    args = {"a": 40}
    assert system.custom_tools.execute_generated_tool_tool(
        "adder", "add", json.dumps(args)
    ).endswith("42")
    receipt = ledger.execution_result()
    assert receipt["tool_name"] == "adder" and receipt["function_name"] == "add"
    assert receipt["kwargs"] == {"a": 40} and receipt["result"] == "42"
    receipt["kwargs"]["a"] = 999
    assert ledger.execution_result()["kwargs"] == {"a": 40}


@pytest.mark.parametrize(
    "invalidate", ["operation", "code", "tests", "acceptance", "closed", "failed_call"]
)
def test_stale_or_failed_call_cannot_supply_final_evidence(system, invalidate):
    """Verify stale or failed call cannot supply final evidence."""
    ledger = authorize_fixture(system)
    system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}')
    assert ledger.execution_result() is not None
    if invalidate == "operation":
        system.security.operation_id = "another-operation"
    elif invalidate in ("code", "tests"):
        with (system.root / "adder" / f"adder_{invalidate}.py").open("a") as stream:
            stream.write("\n# changed")
    elif invalidate == "acceptance":
        ledger.revoke_acceptance("adder")
    elif invalidate == "closed":
        system.security.cancel_pending()
    else:
        system.custom_tools.execute_generated_tool_tool("adder", "add", "[]")
    assert ledger.execution_result() is None


def test_reuse_cannot_replace_observed_result_with_model_prose(system, monkeypatch):
    """Verify reuse cannot replace observed result with model prose."""

    def kickoff():
        """Provide kickoff for the enclosing trusted test fixture."""
        authorize_fixture(system)
        system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}')
        return "Invented 999"

    monkeypatch.setattr(system.main, "Crew", lambda **kw: SimpleNamespace(kickoff=kickoff))
    result = system.main.run_system("Add two to 40")
    assert "42" in result and "999" not in result


def test_edit_during_child_execution_revokes_result(system, monkeypatch):
    """Verify edit during child execution revokes result."""
    ledger = authorize_fixture(system)
    backend = system.custom_tools.executor.sandbox
    original = backend.execute

    def replace(*args, **kwargs):
        """Provide replace for the enclosing trusted test fixture."""
        observed = original(*args, **kwargs)
        (system.root / "adder" / "adder_code.py").write_text("def add(a,b=2): return 999")
        return observed

    monkeypatch.setattr(backend, "execute", replace)
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":40}').startswith(
        "Execution Error:"
    )
    assert ledger.execution_result() is None
