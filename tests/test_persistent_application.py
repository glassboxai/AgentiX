"""Regression coverage for persistent previews with finite operations."""

import pytest

from agentix.lab.application_artifacts import application_digest, approve_application
from agentix.lab.application_session import ApplicationSession


def capability(tmp_path):
    """Explicitly review a generated schema-3 fixture, never existing artifacts."""
    from schema3_package import package

    folder = package(tmp_path)
    return approve_application(folder, application_digest(folder))


def test_persistent_gui_does_not_expire_when_idle(tmp_path):
    """Catch applying the headless duration cap to an idle interactive application."""
    session = ApplicationSession(capability(tmp_path), lifetime=None)
    try:
        assert session.lifetime is None
        session._check_runtime()
        assert not session.cancel.is_set()
    finally:
        session.close()


def test_callback_timeout_cancels_owned_application(tmp_path):
    """Catch infinite callbacks surviving a persistent GUI's operation budget."""
    session = ApplicationSession(capability(tmp_path))
    try:
        session.clock = lambda: 10.0
        assert session._control_message({"type": "callback_start", "id": "a" * 32})
        session.clock = lambda: 56.0
        session._check_runtime()
        assert session.cancel.is_set()
        assert session.diagnostics["failure"] == "callback_timeout"
    finally:
        session.close()


def test_finished_callback_releases_lease(tmp_path):
    """Catch expired completed work stopping an otherwise idle application."""
    session = ApplicationSession(capability(tmp_path))
    try:
        session.clock = lambda: 10.0
        session._control_message({"type": "callback_start", "id": "b" * 32})
        session._control_message({"type": "callback_end", "id": "b" * 32})
        session.clock = lambda: 99.0
        session._check_runtime()
        assert not session.cancel.is_set()
    finally:
        session.close()


def test_headless_cannot_select_unlimited_lifetime(tmp_path):
    """Catch removing execution deadlines from reusable data operations."""
    with pytest.raises(ValueError):
        ApplicationSession(capability(tmp_path), payload={"text": "Hello"}, lifetime=None)


def test_concurrent_close_waits_for_owned_cleanup(tmp_path):
    """Catch returning from a second close before the first has released resources."""
    import threading

    entered, release, second_started, second_done = (threading.Event() for _ in range(4))

    class Temporary:
        """Hold the external filesystem cleanup boundary deterministically."""

        def cleanup(self):
            """Block cleanup until both callers have reached the close protocol."""
            entered.set()
            assert release.wait(3)

    session = ApplicationSession(capability(tmp_path))
    session.temporary = Temporary()
    first = threading.Thread(target=session.close)

    def close_again():
        """Observe completion of the concurrent caller, not just its invocation."""
        second_started.set()
        session.close()
        second_done.set()

    second = threading.Thread(target=close_again)
    first.start()
    assert entered.wait(3)
    second.start()
    assert second_started.wait(3)
    try:
        assert not second_done.wait(0.15)
    finally:
        release.set()
        first.join(3)
        second.join(3)
    assert second_done.is_set()
