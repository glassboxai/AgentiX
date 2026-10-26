"""Session tokens and activity must not cross workflow owners."""

import io
import threading
from types import SimpleNamespace

import pytest


def test_session_registry_binds_token_to_owner():
    """Verify session registry binds token to owner."""
    from agentix.ui.sessions import SessionAccessError, SessionRegistry

    registry = SessionRegistry(
        lambda session_id: SimpleNamespace(
            state=SimpleNamespace(is_running=False),
            security=SimpleNamespace(cancel_pending=lambda: None),
        )
    )
    alice = registry.resolve(None, "alice-browser")
    assert registry.resolve(alice.token, "alice-browser") is alice
    bob = registry.resolve(None, "bob-browser")
    assert bob.token != alice.token
    with pytest.raises(SessionAccessError):
        registry.resolve(alice.token, "bob-browser")


def test_activity_routing_is_context_local_across_threads():
    """Verify activity routing is context local across threads."""
    from agentix.diagnostics import ActivityRouter, operation_scope
    from agentix.ui.state import ConsoleThoughtsCapture

    host = io.StringIO()
    router = ActivityRouter(host)
    first, second = ConsoleThoughtsCapture(host), ConsoleThoughtsCapture(host)
    barrier = threading.Barrier(2)

    def worker(capture, owner):
        """Provide worker for the enclosing trusted test fixture."""
        with operation_scope(owner, capture=capture):
            barrier.wait(2)
            router.write(owner)

    workers = [
        threading.Thread(target=worker, args=(first, "alice")),
        threading.Thread(target=worker, args=(second, "bob")),
    ]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join(2)
    assert first.get_logs() == "alice"
    assert second.get_logs() == "bob"


def test_session_expiry_capacity_and_owner_checked_close():
    """Verify session expiry capacity and owner checked close."""
    from agentix.ui.sessions import SessionAccessError, SessionRegistry

    cancelled = []
    now = [0.0]
    registry = SessionRegistry(
        lambda token: SimpleNamespace(
            state=SimpleNamespace(is_running=False),
            security=SimpleNamespace(cancel_pending=lambda: cancelled.append(token)),
        ),
        max_sessions=1,
        idle_timeout=10,
        clock=lambda: now[0],
    )
    alice = registry.resolve(None, "alice")
    registry.close(alice.token, "bob")
    assert registry.resolve(alice.token, "alice") is alice
    with pytest.raises(SessionAccessError, match="capacity"):
        registry.resolve(None, "bob")
    now[0] = 11
    bob = registry.resolve(None, "bob")
    assert cancelled == [alice.session_id]
    with pytest.raises(SessionAccessError):
        registry.resolve(alice.token, "alice")
    registry.close_state(bob.token)
    assert cancelled == [alice.session_id, bob.session_id]


def test_activity_buffer_is_bounded():
    """Verify activity buffer is bounded."""
    from agentix.ui.state import ConsoleThoughtsCapture

    capture = ConsoleThoughtsCapture(io.StringIO())
    for index in range(300):
        capture.write(f"{index}:" + "x" * 5000 + "\n")
    assert len(capture.logs_buffer) <= 256
    assert len(capture.get_logs(300)) <= 256 * 4097


def test_diagnostic_session_id_is_not_the_browser_capability_token():
    """Verify diagnostic session id is not the browser capability token."""
    from agentix.ui.sessions import SessionRegistry

    identities = []

    def create(identity):
        """Provide create for the enclosing trusted test fixture."""
        identities.append(identity)
        return SimpleNamespace(state=SimpleNamespace(is_running=False))

    session = SessionRegistry(create).resolve(None, "browser")
    assert identities[0] != session.token
