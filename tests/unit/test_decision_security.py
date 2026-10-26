"""Fail-closed creation decisions must never trigger arbitrary tool creation."""

from types import SimpleNamespace
from unittest.mock import Mock

import pytest


@pytest.mark.parametrize(
    "response",
    [
        "CREATE_TOOL bad json",
        '{"action":"CREATE_TOOL"}',
        '{"action":"DELETE_TOOL","tool_name":"adder","purpose":"add"}',
        '{"action":"CREATE_TOOL","tool_name":"../outside","purpose":"add"}',
        '{"action":"CREATE_TOOL","tool_name":"My Adder","purpose":"add"}',
        '{"action":"CREATE_TOOL","tool_name":"con","purpose":"add"}',
        '{"action":"CREATE_TOOL","tool_name":"adder","purpose":""}',
        '{"action":"CREATE_TOOL","tool_name":"adder","purpose":42}',
        '{"action":"CREATE_TOOL","tool_name":"adder","purpose":"add","extra":true}',
        '{"action":"CREATE_TOOL","action":"CREATE_TOOL","tool_name":"adder","purpose":"add"}',
        'prefix {"action":"CREATE_TOOL","tool_name":"adder","purpose":"add"} suffix',
        '[{"action":"CREATE_TOOL","tool_name":"adder","purpose":"add"}]',
    ],
)
def test_invalid_manager_decision_never_starts_creation(system, monkeypatch, response):
    """Verify invalid manager decision never starts creation."""
    factory = Mock(return_value=SimpleNamespace(kickoff=lambda: response))
    monkeypatch.setattr(system.main, "Crew", factory)
    pipeline = Mock()
    monkeypatch.setattr(system.main, "build_tool_pipeline", pipeline)
    with pytest.raises(ValueError, match="Manager"):
        system.main.run_system("query")
    pipeline.assert_not_called()
    assert factory.call_count == 1


def test_manager_query_and_decision_payload_are_not_logged(system, monkeypatch, caplog):
    """Verify manager query and decision payload are not logged."""
    secret = "private-query-token-1234"
    monkeypatch.setattr(
        system.main, "Crew", Mock(return_value=SimpleNamespace(kickoff=lambda: "answer"))
    )
    with caplog.at_level("DEBUG", logger="agentix"):
        assert system.main.run_system(secret) == "answer"
    assert secret not in caplog.text
    assert "operation_id=" in caplog.text


def test_execution_exception_payload_is_not_logged(system, caplog):
    """Verify execution exception payload is not logged."""
    directory = system.root / "safe"
    directory.mkdir(parents=True)
    (directory / "safe_code.py").write_text('def run(): raise ValueError("private-source-token")')
    (directory / "safe_tests.py").write_text("import unittest")
    ledger = system.custom_tools.verification
    code, tests = ledger.snapshot("safe")
    assert ledger.record(
        "safe",
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    assert ledger.authorize("safe", code, tests, "fixture-contract", frozenset({"run"}))
    with caplog.at_level("DEBUG", logger="agentix"):
        assert "Execution Error:" in system.custom_tools.execute_generated_tool_tool("safe", "run")
    assert "private-source-token" not in caplog.text


def test_storage_exception_payload_is_not_logged(system, monkeypatch, caplog):
    """Verify storage exception payload is not logged."""
    (system.root / "safe").mkdir(parents=True)
    system.security.auto_approve = True
    monkeypatch.setattr("builtins.open", Mock(side_effect=OSError("private-source-token")))
    with caplog.at_level("DEBUG", logger="agentix"):
        system.security.safe_write_file("safe", "notes.txt", "content")
    assert "private-source-token" not in caplog.text


@pytest.mark.parametrize(
    "response",
    ["<tool_call>", '{"action":"CREATE_TOOL","tool_name":"adder","purpose":' + "9" * 5000 + "}"],
    ids=["empty-answer", "oversized-json-integer"],
)
def test_degenerate_manager_output_is_rejected_as_a_contract_error(system, monkeypatch, response):
    """Verify degenerate manager output is rejected as a contract error."""
    monkeypatch.setattr(
        system.main, "Crew", Mock(return_value=SimpleNamespace(kickoff=lambda: response))
    )
    with pytest.raises(ValueError, match="Manager"):
        system.main.run_system("query")
