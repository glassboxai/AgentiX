"""LIVE-UX-001: preserve verbose agent messages alongside technical events."""

import io
import logging
import sys
import threading
from types import SimpleNamespace

import pytest

from agentix.diagnostics import log_event, operation_scope
from agentix.ui.state import ConsoleThoughtsCapture


@pytest.mark.parametrize("role", ["manager", "architect", "coder", "tester"])
def test_every_application_agent_keeps_verbose_enabled(system, role):
    """Verify every application agent keeps verbose enabled."""
    agent = getattr(system.main, role + "_agent")
    assert agent.verbose is True


def test_gated_creation_crews_keep_verbose_enabled(system, monkeypatch):
    """Verify gated creation crews keep verbose enabled."""
    observed = []
    system.security.auto_approve = True

    def crew(**kwargs):
        """Provide crew for the enclosing trusted test fixture."""
        observed.append(kwargs["verbose"])
        stage = len(observed)

        def kickoff():
            """Provide kickoff for the enclosing trusted test fixture."""
            if stage == 1:
                system.security.safe_write_file("adder", "adder_specifications.md", "Approved spec")
            elif stage == 2:
                system.custom_tools.compile_and_save_code_tool("adder", "def adder(): return 3")
            return "Completed"

        return SimpleNamespace(kickoff=kickoff)

    monkeypatch.setattr(system.main, "Crew", crew)
    assert "PIPELINE_STAGE_FAILED: acceptance" in system.main.build_tool_pipeline("adder", "Add")
    assert observed == [True, True, True]


def test_manager_and_final_execution_crews_keep_verbose_enabled(system, monkeypatch):
    """Check constructor policy only; this fixture does not validate execution."""
    observed = []

    def crew(**kwargs):
        """Provide crew for the enclosing trusted test fixture."""
        observed.append(kwargs["verbose"])
        response = (
            '{"action":"CREATE_TOOL","tool_name":"adder","purpose":"Add"}'
            if len(observed) == 1
            else "Final answer"
        )
        return SimpleNamespace(kickoff=lambda: response)

    monkeypatch.setattr(system.main, "Crew", crew)
    monkeypatch.setattr(system.main, "build_tool_pipeline", lambda **kwargs: None)
    monkeypatch.setattr(system.custom_tools.verification, "is_verified", lambda name: True)
    monkeypatch.setattr(system.custom_tools.verification, "acceptance_context", lambda name: {})
    assert system.main.run_system("Add").startswith("EXECUTION_NOT_VERIFIED:")
    assert observed == [True, True]


def test_verbose_output_and_technical_events_remain_owner_bound(monkeypatch):
    """Verify verbose output and technical events remain owner bound."""
    from agentix.diagnostics import activity_output

    host = io.StringIO()
    monkeypatch.setattr(sys, "stdout", host)
    captures = {owner: ConsoleThoughtsCapture(host) for owner in ("Alice", "Bob")}
    barrier = threading.Barrier(2)
    errors = []

    def worker(owner):
        """Provide worker for the enclosing trusted test fixture."""
        try:
            with operation_scope(owner, "operation-" + owner, capture=captures[owner]):
                barrier.wait(3)
                print("Agent: " + owner + " — Task and tool result")
                log_event(logging.getLogger(__name__), "workflow_started")
        except BaseException as exc:
            errors.append(exc)

    with activity_output():
        threads = [threading.Thread(target=worker, args=(owner,)) for owner in captures]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(5)
        assert not any(thread.is_alive() for thread in threads)
    assert not errors
    assert sys.stdout is host
    for owner, capture in captures.items():
        text = capture.get_logs()
        assert "Agent: " + owner in text and "workflow_started" in text
        assert ("Bob" if owner == "Alice" else "Alice") not in text


def test_activity_output_restores_original_stream_after_failure():
    """Verify activity output restores original stream after failure."""
    from agentix.diagnostics import activity_output

    original = sys.stdout
    with pytest.raises(RuntimeError, match="launch failed"):
        with activity_output():
            raise RuntimeError("launch failed")
    assert sys.stdout is original


def test_unicode_verbose_message_survives_legacy_windows_console():
    """A narrow host encoding must not prevent the GUI from seeing SDK messages."""

    class LegacyConsole(io.StringIO):
        """Provide LegacyConsole for the enclosing trusted test fixture."""

        def write(self, text):
            """Provide write for the enclosing trusted test fixture."""
            text.encode("cp1252")
            return super().write(text)

    host = LegacyConsole()
    capture = ConsoleThoughtsCapture(host)
    capture.write("🤖 Agent: Architect — approved result\n")
    assert capture.get_logs() == "🤖 Agent: Architect — approved result"
    assert "Agent: Architect" in host.getvalue()


def test_fragmented_verbose_output_preserves_logical_lines_and_ansi():
    """Verify fragmented verbose output preserves logical lines and ansi."""
    capture = ConsoleThoughtsCapture(io.StringIO())
    for fragment in ["\x1b[3", "1mAgent: ", "Architect", "\x1b[0m\n", "Task: ", "Create tool\n"]:
        capture.write(fragment)
    assert capture.get_logs() == "Agent: Architect\nTask: Create tool"
    capture.write("Pending verbose message")
    assert capture.get_logs(1) == "Pending verbose message"
    capture.clear()
    assert capture.get_logs() == ""
