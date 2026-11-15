"""Shared central activity status for long-running owner-scoped UI operations."""

from typing import Any

from agentix.controllers.sessions import SessionRegistry


class ActivityBackend:
    """Report background work without obscuring a pending human decision."""

    def __init__(self, sessions: SessionRegistry) -> None:
        """Inject the owning registry; construction starts no polling or worker."""
        self.sessions = sessions

    def activity_status(self, token: str | None, request: Any) -> str:
        """Return fixed accessible status HTML; never include prompts or exceptions."""
        session = self.sessions.resolve(token, getattr(request, "session_hash", None))
        controller = session.controller
        state = getattr(controller, "state", None)
        application = getattr(state, "application_busy", False)
        pending = getattr(
            getattr(controller, "security", None), "get_pending_request", lambda: None
        )()
        if pending:
            return ""
        running = getattr(state, "is_running", False)
        if not application and not running:
            return ""
        labels = {
            "generating": "Generating application…",
            "verifying": "Verifying application…",
            "running": "Running application…",
            "loading": "Loading application…",
            "saving": "Saving application…",
            "reviewing_tools": "Reviewing modified tools…",
        }
        label = (
            labels.get(getattr(state, "application_phase", ""), "Processing application…")
            if application
            else "Processing your query…"
        )
        return (
            '<div class="agentix-busy-panel" role="status" aria-live="polite" aria-atomic="true"><span class="agentix-spinner" aria-hidden="true"></span><span>'
            + label
            + "</span></div>"
        )
