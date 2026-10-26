"""CLI-001: terminal decisions must reach the real owner-bound coordinator."""

import json
import threading

import pytest

from agentix.approvals import ApprovalCoordinator
from agentix.cli import run_cli


@pytest.mark.parametrize(
    ("answers", "expected"),
    [
        (["approve"], (True, "original")),
        (["reject"], (False, "original")),
        (
            [
                "",
            ],
            (False, "original"),
        ),
        (["edit", "replacement", ".end", "approve"], (True, "replacement")),
        (["unknown", "reject"], (False, "original")),
    ],
)
def test_terminal_resolves_manual_review(monkeypatch, capsys, answers, expected):
    """Verify terminal resolves manual review."""
    security = ApprovalCoordinator.for_owner("terminal", timeout=2)
    security.auto_approve = True
    results = []
    inputs = iter(["query", *answers, "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    def workflow(query):
        """Provide workflow for the enclosing trusted test fixture."""
        assert threading.current_thread() is not threading.main_thread()
        results.append(
            security.request_user_permission(
                "fixture",
                "review_acceptance",
                "original",
                require_manual=True,
                review_context={
                    "python_tests": "trusted tests",
                    "provisional_result": "provisional",
                },
            )
        )
        return "finished"

    with pytest.raises(SystemExit) as stopped:
        run_cli(workflow, security=security)
    assert stopped.value.code == 0
    assert results == [expected]
    output = capsys.readouterr().out
    assert "trusted tests" in output and "provisional" in output
    assert "finished" in output


@pytest.mark.parametrize("interruption", [EOFError, KeyboardInterrupt])
@pytest.mark.parametrize("during_edit", [False, True])
def test_interrupted_review_denies_and_closes_owner(monkeypatch, interruption, during_edit):
    """Verify interrupted review denies and closes owner."""
    security = ApprovalCoordinator.for_owner("interrupted", timeout=2)
    results = []
    finished = threading.Event()
    decisions = iter(["edit"] if during_edit else [])

    def read(prompt):
        """Provide read for the enclosing trusted test fixture."""
        if "query" in prompt.lower():
            return "query"
        if answer := next(decisions, None):
            return answer
        raise interruption()

    monkeypatch.setattr("builtins.input", read)

    def workflow(query):
        """Provide workflow for the enclosing trusted test fixture."""
        results.append(security.request_user_permission("fixture", content="original"))
        finished.set()
        return "denied"

    with pytest.raises(SystemExit):
        run_cli(workflow, security=security)
    assert finished.wait(2)
    assert results == [(False, "original")]
    assert security.is_closed()


def test_eof_at_query_exits_cleanly(monkeypatch):
    """Verify eof at query exits cleanly."""
    monkeypatch.setattr("builtins.input", lambda prompt: (_ for _ in ()).throw(EOFError()))
    with pytest.raises(SystemExit) as stopped:
        run_cli(lambda query: "unused")
    assert stopped.value.code == 0


def test_cli_shows_independent_host_verdicts(system, monkeypatch, capsys):
    """Verify cli shows independent host verdicts."""
    service = system.custom_tools
    system.security.auto_approve = True
    edited = json.dumps(
        {
            "version": 1,
            "cases": [
                {
                    "id": "sum",
                    "purpose": "Check sum",
                    "function": "add",
                    "kwargs": {},
                    "expect": {"kind": "value", "value": 3},
                }
            ],
        }
    )
    inputs = iter(["query", "edit", edited, ".end", "approve", "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    def workflow(query):
        """Provide workflow for the enclosing trusted test fixture."""
        service.compile_and_save_code_tool("adder", "def add(): return 3")
        result = service.run_and_save_tests_tool(
            "adder",
            "import unittest\nclass Checks(unittest.TestCase):\n def test_one(self): self.assertEqual(1,1)\n",
        )
        assert result.startswith("TESTS_PROVISIONAL_PASSED:")
        original = edited.replace('"value": 3', '"value": 99')
        return service.submit_acceptance_cases_tool("adder", original)

    with pytest.raises(SystemExit):
        run_cli(workflow, security=system.security, validation=service.acceptance)
    output = capsys.readouterr().out
    assert '"stage": "verified"' in output
    assert '"observed"' in output and '"passed": true' in output


def test_review_control_characters_cannot_hide_terminal_content(monkeypatch, capsys):
    """Verify review control characters cannot hide terminal content."""
    security = ApprovalCoordinator.for_owner("terminal-controls", timeout=2)
    content = "visible\x1b[2J\rhidden\u202econtent"
    inputs = iter(["query", "approve", "q"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    decisions = []

    def workflow(query):
        """Provide workflow for the enclosing trusted test fixture."""
        decisions.append(security.request_user_permission("fixture", content=content))
        return "done"

    with pytest.raises(SystemExit):
        run_cli(workflow, security=security)
    output = capsys.readouterr().out
    assert "\x1b" not in output and "\r" not in output and "\u202e" not in output
    assert decisions == [(True, content)]
