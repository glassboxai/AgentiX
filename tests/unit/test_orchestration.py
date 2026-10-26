"""Characterize catalog inspection and manager routing without LLM calls."""

from types import SimpleNamespace
from unittest.mock import Mock

import pytest


def install(system, name, code):
    """Create a catalog input fixture without executing it."""
    folder = system.root / name
    folder.mkdir(parents=True)
    (folder / f"{name}_code.py").write_text(code, encoding="utf-8")


def test_catalog_missing_root(system):
    """Verify catalog missing root."""
    assert system.main.get_installed_tools_catalog() == "No tools installed yet."


def test_catalog_empty_root(system):
    """Verify catalog empty root."""
    system.root.mkdir()
    assert system.main.get_installed_tools_catalog() == "No tools installed yet."


def test_catalog_extracts_public_function_and_first_docstring_line(system):
    """Verify catalog extracts public function and first docstring line."""
    install(
        system,
        "adder",
        'def add(a, b=1):\n    """Add numbers.\n    Details."""\n    return a+b\ndef _hidden(): pass',
    )
    catalog = system.main.get_installed_tools_catalog()
    assert "add(a, b)" in catalog and "Add numbers." in catalog
    assert "_hidden" not in catalog and "Details." not in catalog
    assert "adder_code.py" in catalog and "adder_specifications.md" in catalog


def test_catalog_never_executes_module(system):
    """Verify catalog never executes module."""
    install(system, "safe", "raise RuntimeError('do not execute')\ndef calculate(): return 1")
    assert "calculate()" in system.main.get_installed_tools_catalog()


def test_catalog_order_is_stable(system):
    """Verify catalog order is stable."""
    install(system, "zebra", "def z(): pass")
    install(system, "alpha", "def a(): pass")
    result = system.main.get_installed_tools_catalog()
    assert result.index("alpha") < result.index("zebra")


def test_catalog_reports_syntax_error_and_continues(system):
    """Verify catalog reports syntax error and continues."""
    install(system, "bad", "def broken(:")
    install(system, "good", "def fine(): pass")
    result = system.main.get_installed_tools_catalog()
    assert "Error parsing code file" in result and "fine()" in result


def test_catalog_ignores_missing_code_and_plain_files(system):
    """Verify catalog ignores missing code and plain files."""
    (system.root / "empty").mkdir(parents=True)
    (system.root / "not_a_tool").write_text("text")
    assert system.main.get_installed_tools_catalog() == "No tools installed yet."


def test_catalog_reports_no_functions(system):
    """Verify catalog reports no functions."""
    install(system, "constants", "VALUE = 1")
    assert "No standalone functions detected" in system.main.get_installed_tools_catalog()


def test_catalog_default_description(system):
    """Verify catalog default description."""
    install(system, "plain", "def calculate(): pass")
    assert "No description provided." in system.main.get_installed_tools_catalog()


def test_existing_tool_answer_does_not_create_pipeline(system, monkeypatch):
    """Verify existing tool answer does not create pipeline."""
    monkeypatch.setattr(
        system.main, "Crew", Mock(return_value=SimpleNamespace(kickoff=lambda: "<tool_call> 42 "))
    )
    pipeline = Mock()
    monkeypatch.setattr(system.main, "build_tool_pipeline", pipeline)
    assert system.main.run_system("calculate") == "42"
    pipeline.assert_not_called()


@pytest.mark.parametrize(
    "response",
    [
        '{"action":"CREATE_TOOL","tool_name":"my_adder","purpose":"addition"}',
        '```json\n{"action":"CREATE_TOOL","tool_name":"my_adder","purpose":"addition"}\n```',
        '```\n{"action":"CREATE_TOOL","tool_name":"my_adder","purpose":"addition"}\n```',
    ],
)
def test_create_tool_routing(system, monkeypatch, response):
    """Verify create tool routing."""

    def execute():
        """Provide execute for the enclosing trusted test fixture."""
        assert system.custom_tools.execute_generated_tool_tool("my_adder", "add").endswith("3")
        return "<tool_call> final "

    crew = Mock(
        side_effect=[
            SimpleNamespace(kickoff=lambda: response),
            SimpleNamespace(kickoff=execute),
        ]
    )
    monkeypatch.setattr(system.main, "Crew", crew)

    def completed(**kwargs):
        """Provide completed for the enclosing trusted test fixture."""
        name = kwargs["tool_name"]
        install(system, name, "def add(): return 3")
        (system.root / name / f"{name}_tests.py").write_text("import unittest")
        ledger = system.custom_tools.verification
        code, tests = ledger.snapshot(name)
        assert ledger.record(
            name,
            code,
            tests,
            dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
            isolated=True,
            exit_code=0,
        )
        assert ledger.authorize(name, code, tests, "fixture-contract", frozenset({"add"}))

    pipeline = Mock(side_effect=completed)
    monkeypatch.setattr(system.main, "build_tool_pipeline", pipeline)
    assert system.main.run_system("add numbers") == (
        "Host-observed execution: my_adder.add\nArguments: {}\nResult: 3"
    )
    pipeline.assert_called_once_with(
        tool_name="my_adder",
        user_requirement="add numbers\n\nManager purpose (additional context only): addition",
    )
    assert crew.call_count == 2


def test_malformed_decision_is_rejected_without_fallback(system, monkeypatch):
    """Approved FLOW-02 replaces the formerly characterized arbitrary fallback."""
    monkeypatch.setattr(
        system.main,
        "Crew",
        Mock(return_value=SimpleNamespace(kickoff=lambda: "CREATE_TOOL bad json")),
    )
    pipeline = Mock()
    monkeypatch.setattr(system.main, "build_tool_pipeline", pipeline)
    with pytest.raises(ValueError, match="Manager"):
        system.main.run_system("query")
    pipeline.assert_not_called()


def test_pipeline_preserves_task_order_and_context(system, monkeypatch):
    """Approved staged design stops at an unsaved specification instead of advancing."""
    crew = Mock(return_value=SimpleNamespace(kickoff=lambda: "done"))
    monkeypatch.setattr(system.main, "Crew", crew)
    assert "PIPELINE_STAGE_FAILED: specification" in system.main.build_tool_pipeline(
        "adder", "addition"
    )
    assert crew.call_count == 1
    assert crew.call_args.kwargs["agents"] == [system.main.architect_agent]


def test_manager_failure_propagates(system, monkeypatch):
    """Verify manager failure propagates."""
    monkeypatch.setattr(
        system.main,
        "Crew",
        Mock(return_value=SimpleNamespace(kickoff=Mock(side_effect=RuntimeError("offline")))),
    )
    with pytest.raises(RuntimeError, match="offline"):
        system.main.run_system("query")
