"""Central activity state is owner-scoped and yields to human review."""

from types import SimpleNamespace

import pytest
from test_applications_backend import registry


def test_background_execution_is_visible_and_pending_review_is_not_blocked():
    """Fast query-submit callbacks must not hide the actual background workload."""
    from agentix.controllers.activity import ActivityBackend

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)
    request = SimpleNamespace(session_hash="alice")
    service = ActivityBackend(sessions)
    owner.controller.state.is_running = True
    assert "agentix-busy-panel" in service.activity_status(owner.token, request)
    owner.controller.security.get_pending_request = lambda: {"action": "review_acceptance"}
    assert "agentix-busy-panel" not in service.activity_status(owner.token, request)
    owner.controller.state.is_running = False
    owner.controller.security.get_pending_request = lambda: None
    owner.controller.state.application_busy = True
    owner.controller.state.application_phase = "generating"
    assert "Generating application" in service.activity_status(owner.token, request)
    owner.controller.state.application_busy = False
    assert "agentix-busy-panel" not in service.activity_status(owner.token, request)


def test_foreign_owner_cannot_poll_another_sessions_processing_state():
    """Activity information must use the same ownership checks as business state."""
    from agentix.controllers.activity import ActivityBackend
    from agentix.controllers.sessions import SessionAccessError

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    with pytest.raises(SessionAccessError):
        ActivityBackend(sessions).activity_status(owner.token, SimpleNamespace(session_hash="bob"))


@pytest.mark.parametrize(
    "phase,label",
    [
        ("generating", "Generating application"),
        ("verifying", "Verifying application"),
        ("running", "Running application"),
        ("loading", "Loading application"),
        ("saving", "Saving application"),
    ],
)
def test_application_activity_describes_the_actual_phase(phase, label):
    """A data run must never be presented as model generation or verification."""
    from agentix.controllers.activity import ActivityBackend

    sessions = registry()
    owner = sessions.resolve(None, "phase-owner")
    owner.controller.state.application_busy = True
    owner.controller.state.application_phase = phase
    owner.controller.security = SimpleNamespace(get_pending_request=lambda: None)
    assert label in ActivityBackend(sessions).activity_status(
        owner.token, SimpleNamespace(session_hash="phase-owner")
    )
