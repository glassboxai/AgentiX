"""Serialize application polling with opening/closing the same browser-owned preview."""

import threading
from types import SimpleNamespace

from agentix.controllers.applications import ApplicationsBackend


def test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock():
    """A stale dead-preview observation must not race a new preview/usage lease."""
    controller = SimpleNamespace(
        _lock=threading.RLock(), state=SimpleNamespace(application_busy=False)
    )
    candidate = SimpleNamespace(
        preview=SimpleNamespace(alive=False, session=SimpleNamespace(diagnostics={})),
        dependency_check=None,
    )
    state = SimpleNamespace(candidate=candidate)
    session = SimpleNamespace(controller=controller, token="owned")
    resolved = threading.Event()
    closed = threading.Event()
    backend = object.__new__(ApplicationsBackend)

    def resolve(token, request):
        """Expose controlled owner state without a browser or filesystem."""
        resolved.set()
        return session, state

    backend._resolve = resolve
    backend._close = lambda value: closed.set()
    thread = threading.Thread(target=lambda: backend.poll(None, None))
    with controller._lock:
        thread.start()
        assert resolved.wait(1)
        premature = closed.wait(0.2)
        controller.state.application_busy = True
    thread.join(2)
    assert not thread.is_alive()
    assert not premature
    assert not closed.is_set()
