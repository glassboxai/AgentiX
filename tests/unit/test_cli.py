"""Preserve CLI exit, blank-input and failure recovery behavior."""

from unittest.mock import Mock

import pytest

from agentix.cli import run_cli


@pytest.mark.parametrize("alias", ["quit", "exit", "q", " Q "])
def test_exit_aliases_do_not_run_workflow(monkeypatch, alias):
    """Verify exit aliases do not run workflow."""
    monkeypatch.setattr("builtins.input", lambda prompt: alias)
    workflow = Mock()
    with pytest.raises(SystemExit) as stopped:
        run_cli(workflow)
    assert stopped.value.code == 0
    workflow.assert_not_called()


def test_blank_input_is_ignored_and_valid_query_is_trimmed(monkeypatch, capsys):
    """Verify blank input is ignored and valid query is trimmed."""
    inputs = iter(["  ", " calculate ", "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    workflow = Mock(return_value="answer")
    with pytest.raises(SystemExit):
        run_cli(workflow)
    workflow.assert_called_once_with("calculate")
    assert "answer" in capsys.readouterr().out


def test_cli_reports_workflow_failure_and_accepts_next_query(monkeypatch, capsys):
    """Verify cli reports workflow failure and accepts next query."""
    inputs = iter(["first", "second", "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    workflow = Mock(side_effect=[RuntimeError("offline"), "recovered"])
    with pytest.raises(SystemExit):
        run_cli(workflow)
    output = capsys.readouterr().out
    assert "offline" in output and "recovered" in output
    assert workflow.call_count == 2


def test_cli_diagnostics_do_not_log_exception_payload(monkeypatch, caplog):
    """Verify cli diagnostics do not log exception payload."""
    inputs = iter(["query", "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    with pytest.raises(SystemExit):
        run_cli(Mock(side_effect=RuntimeError("private-query-token")))
    assert "private-query-token" not in caplog.text


def test_default_cli_uses_owner_runtime_instead_of_shared_legacy_facade(monkeypatch):
    """CLI generation must use the same canonical per-owner policy as the GUI."""
    from types import SimpleNamespace

    from agentix import bootstrap
    from agentix.cli import run_cli

    create = Mock(
        return_value=SimpleNamespace(
            orchestrator=SimpleNamespace(run_system=Mock()),
            security=SimpleNamespace(cancel_pending=Mock()),
            operations=SimpleNamespace(acceptance=Mock()),
        )
    )
    monkeypatch.setattr(bootstrap, "create_runtime", create)
    monkeypatch.setattr("builtins.input", lambda prompt: "exit")
    with pytest.raises(SystemExit):
        run_cli()
    create.assert_called_once()
    assert "security" not in create.call_args.kwargs
