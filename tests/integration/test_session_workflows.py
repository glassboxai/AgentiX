"""Exercise actual owner controllers/callbacks with deterministic parallel workers."""

import threading
from types import SimpleNamespace

import pytest

from agentix.security import SecurityManager
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionAccessError, SessionCallbacks, SessionRegistry


def test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity(
    tmp_path, monkeypatch
):
    """Verify parallel browser callbacks do not share history approvals or activity."""
    release = threading.Event()
    active = threading.Barrier(3)
    workers = []
    original_thread = threading.Thread

    def tracked_thread(*args, **kwargs):
        """Provide tracked thread for the enclosing trusted test fixture."""
        thread = original_thread(*args, **kwargs)
        workers.append(thread)
        return thread

    monkeypatch.setattr("agentix.ui.controller.threading.Thread", tracked_thread)

    def create(token):
        """Provide create for the enclosing trusted test fixture."""
        security = SecurityManager.for_owner(token)
        security.TOOLS_ROOT_DIR = str(tmp_path / "artifacts")

        def workflow(query):
            """Provide workflow for the enclosing trusted test fixture."""
            active.wait(2)
            release.wait(2)
            return "answer-" + query

        controller = UiController(workflow, lambda: "catalog", security, lambda **kw: kw)
        controller.state.session_id = token
        return controller

    registry = SessionRegistry(create)
    callbacks = SessionCallbacks(registry)
    owner_a, owner_b = (
        SimpleNamespace(session_hash="browser-a"),
        SimpleNamespace(session_hash="browser-b"),
    )
    _, _, token_a = callbacks.submit("alice-private", None, owner_a)
    _, _, token_b = callbacks.submit("bob-private", None, owner_b)
    try:
        active.wait(2)
        callbacks.toggle(True, token_a, owner_a)
        alice, bob = registry.resolve(token_a, "browser-a"), registry.resolve(token_b, "browser-b")
        assert alice.controller.security.auto_approve is True
        assert bob.controller.security.auto_approve is False
        assert "bob-private" not in str(callbacks.poll(token_a, owner_a))
        assert "alice-private" not in str(callbacks.poll(token_b, owner_b))
        with pytest.raises(SessionAccessError):
            callbacks.approve("foreign", "request", token_a, owner_b)
    finally:
        release.set()
        for worker in workers:
            worker.join(2)
            assert not worker.is_alive()
    assert "answer-alice-private" in str(callbacks.poll(token_a, owner_a))
    assert "answer-bob-private" in str(callbacks.poll(token_b, owner_b))
    assert token_b not in alice.controller.captured_stdout.get_logs()


def test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval(system):
    """Verify same filepath new request refreshes editor and rejects old approval."""
    boundary = system.security
    boundary.owner_id = "owner"
    boundary._pending_request = {
        "request_id": "first",
        "owner_id": "owner",
        "filepath": "same.py",
        "action": "write",
        "content": "old",
        "expires_at": float("inf"),
    }
    assert system.app.poll_with_request()[3]["value"] == "old"
    boundary._pending_request = dict(boundary._pending_request, request_id="second", content="new")
    boundary._resolved = False
    snapshot = system.app.poll_with_request()
    assert snapshot[3]["value"] == "new"
    assert snapshot[5] == "second"
    assert not system.app.on_approve("stale edit", "first")
    assert not boundary._approval_event.is_set()
    assert system.app.on_approve("valid edit", "second")


def test_busy_submission_cannot_steal_active_answer(system, monkeypatch):
    """Verify busy submission cannot steal active answer."""
    targets = []
    monkeypatch.setattr(
        system.threading,
        "Thread",
        lambda target, daemon: SimpleNamespace(start=lambda: targets.append(target)),
    )
    monkeypatch.setattr(system.app, "run_system", lambda query: "first-answer")
    system.app.process_user_query("first")
    system.app.process_user_query("second")
    targets[0]()
    history = system.app.poll_system_status()[0]
    assert "first-answer" in history[1]["content"]
    assert "already in progress" in history[3]["content"]


def test_tool_adapter_restores_owner_context_in_provider_threads(system, caplog):
    """Verify tool adapter restores owner context in provider threads."""
    from agentix.adapters.crewai import register_tools

    system.security.owner_id = "owner-id"
    system.security.operation_id = "run-id"
    system.security.auto_approve = True
    tools = register_tools(system.custom_tools, decorator=lambda name: lambda fn: fn)
    results = []
    with caplog.at_level("INFO", logger="agentix"):
        worker = threading.Thread(
            target=lambda: results.append(
                tools.save_specifications_tool("safe", "private-specification")
            )
        )
        worker.start()
        worker.join(2)
    assert not worker.is_alive()
    assert results[0].startswith("Success:")
    assert "session_id=owner-id operation_id=run-id" in caplog.text
    assert "private-specification" not in caplog.text
