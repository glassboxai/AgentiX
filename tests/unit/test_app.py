"""Exercise UI controllers and stream capture independently of browser widgets."""

import io
from unittest.mock import Mock

import pytest


def test_capture_mirrors_output_and_removes_ansi(system):
    """Verify capture mirrors output and removes ansi."""
    stream = io.StringIO()
    capture = system.capture_type(stream)
    capture.write("\x1b[31merror\x1b[0m\n")
    capture.write("   ")
    assert "\x1b[31m" in stream.getvalue()
    assert capture.get_logs() == "error"


def test_capture_tail_and_clear(system):
    """Verify capture tail and clear."""
    capture = system.capture_type(io.StringIO())
    for value in ["a", "b", "c"]:
        capture.write(value + "\n")
    assert capture.get_logs(2) == "b\nc"
    capture.clear()
    assert capture.get_logs() == ""


def test_capture_delegates_stream_operations(system):
    """Verify capture delegates stream operations."""
    stream = Mock()
    stream.isatty.return_value = True
    capture = system.capture_type(stream)
    capture.flush()
    stream.flush.assert_called_once()
    assert capture.isatty() is True
    assert capture.encoding == stream.encoding


@pytest.mark.parametrize("is_open", [False, True])
def test_thoughts_display(system, is_open):
    """Verify thoughts display."""
    result = system.format_thoughts_markdown("activity", is_open)
    assert ("<details open>" if is_open else "<details>") in result
    assert "```text\nactivity\n```" in result


def test_empty_thoughts_display(system):
    """Verify empty thoughts display."""
    assert "Initializing" in system.format_thoughts_markdown("")


def test_empty_query_does_not_start_worker(system, monkeypatch):
    """Verify empty query does not start worker."""
    worker = Mock()
    monkeypatch.setattr(system.threading, "Thread", worker)
    assert system.app.process_user_query("  ") == ("", [])
    worker.assert_not_called()


def test_busy_query_does_not_start_another_worker(system, monkeypatch):
    """Verify busy query does not start another worker."""
    system.app.state.is_running = True
    worker = Mock()
    monkeypatch.setattr(system.threading, "Thread", worker)
    _, history = system.app.process_user_query(" second ")
    assert history[0]["content"] == "second"
    assert "already in progress" in history[-1]["content"]
    worker.assert_not_called()


@pytest.mark.parametrize(
    "result,expected",
    [
        ("answer", "answer"),
        ("", "Execution finished without text output."),
        (None, "Execution finished without text output."),
    ],
)
def test_worker_success(system, monkeypatch, result, expected):
    """Verify worker success."""
    monkeypatch.setattr(system.app, "run_system", Mock(return_value=result))
    # Run the real worker closure synchronously for deterministic state assertions.
    monkeypatch.setattr(
        system.threading,
        "Thread",
        lambda target, daemon: type("Worker", (), {"start": staticmethod(target)})(),
    )
    system.app.process_user_query(" query ")
    assert system.app.state.last_response == expected
    assert system.app.state.is_running is False
    system.app.run_system.assert_called_once_with("query")


def test_worker_error_clears_running_flag(system, monkeypatch):
    """Verify worker error clears running flag."""
    monkeypatch.setattr(system.app, "run_system", Mock(side_effect=RuntimeError("offline")))
    monkeypatch.setattr(
        system.threading,
        "Thread",
        lambda target, daemon: type("Worker", (), {"start": staticmethod(target)})(),
    )
    system.app.process_user_query("query")
    assert system.app.state.error_message == "offline"
    assert system.app.state.is_running is False


def test_poll_loads_pending_content_once(system):
    """Verify poll loads pending content once."""
    system.security._pending_request = {
        "filepath": "file.py",
        "action": "write",
        "content": "original",
        "request_id": "request-1",
    }
    first = system.app.poll_system_status()
    second = system.app.poll_system_status()
    assert first[1] == {"visible": True}
    assert first[3]["value"] == "original"
    assert second[3] == {}, "Timer must preserve text being edited by the user"


def test_poll_resets_after_request_finishes(system):
    """Verify poll resets after request finishes."""
    system.app.state.last_displayed_filepath = "previous"
    result = system.app.poll_system_status()
    assert result[1] == {"visible": False}
    assert result[3]["value"] == ""
    assert system.app.state.last_displayed_filepath is None


@pytest.mark.parametrize(
    "error,response,expected", [("", "answer", "answer"), ("offline", "", "offline")]
)
def test_poll_renders_final_result(system, error, response, expected):
    """Verify poll renders final result."""
    state = system.app.state
    state.chat_history = [
        {"role": "assistant", "content": "⏳ **Agents are actively solving your request...**"}
    ]
    state.error_message, state.last_response = error, response
    history = system.app.poll_system_status()[0]
    assert expected in history[-1]["content"]
    assert "<details>" in history[-1]["content"]


def test_poll_running_displays_activity(system):
    """Verify poll running displays activity."""
    system.app.state.is_running = True
    system.app.state.chat_history = [{"role": "assistant", "content": ""}]
    assert "<details open>" in system.app.poll_system_status()[0][-1]["content"]


def test_approval_and_rejection_callbacks(system, monkeypatch):
    """Verify approval and rejection callbacks."""
    resolve = Mock()
    monkeypatch.setattr(system.security, "resolve_pending_request", resolve)
    system.app.on_approve("edited", "request-1")
    resolve.assert_called_with(
        True, "edited", request_id="request-1", owner_id=system.security.owner_id
    )
    system.app.on_reject("request-1")
    resolve.assert_called_with(False, request_id="request-1", owner_id=system.security.owner_id)


@pytest.mark.parametrize("enabled", [True, False])
def test_auto_approval_toggle(system, enabled):
    """Verify auto approval toggle."""
    system.app.on_toggle_auto_approve(enabled)
    assert system.security.auto_approve is enabled


def test_execution_states_have_independent_histories(system):
    """Verify execution states have independent histories."""
    first, second = system.state_type(), system.state_type()
    assert first.chat_history is not second.chat_history


def test_new_execution_state_does_not_inherit_other_state_values(system):
    """Verify new execution state does not inherit other state values."""
    first = system.state_type()
    first.chat_history.append({"role": "user", "content": "private"})
    first.is_running = True
    second = system.state_type()
    assert second.chat_history == []
    assert second.is_running is False
