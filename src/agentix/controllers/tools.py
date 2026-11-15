"""Tools tab backend and shared session/model callbacks, independent of Gradio."""

from __future__ import annotations

from typing import Any

from agentix.controllers.session_access import SessionOwnerAccess


class ToolsBackend(SessionOwnerAccess):
    """Framework-independent browser callbacks; every operation rechecks ownership."""

    def submit(self, message: str, token: str | None, request: Any) -> tuple[Any, ...]:
        """Submit to this browser's controller and update its server State token."""
        session = self._session(token, request)
        if getattr(session.controller.state, "application_busy", False) or getattr(
            session.controller.state, "application_review_pending", False
        ):
            raise ValueError(
                "Finish or reject the Applications operation before submitting a Tools query"
            )
        return (*session.controller.process_user_query(message), session.token)

    def poll(self, token: str | None, request: Any) -> tuple[Any, ...]:
        """Return a coherent editor/request-ID snapshot for this browser only."""
        session = self._session(token, request)
        return (*session.controller.poll_with_request(), session.token)

    def approve(self, text: str, request_id: str, token: str | None, request: Any) -> bool:
        """Approve only the displayed request through the verified owner controller."""
        session = self._session(token, request)
        return session.controller.on_approve(text, request_id)

    def reject(self, request_id: str, token: str | None, request: Any) -> bool:
        """Reject only the displayed request through the verified owner controller."""
        session = self._session(token, request)
        return session.controller.on_reject(request_id)

    def toggle(self, enabled: bool, token: str | None, request: Any) -> str:
        """Update this owner's setting and return its server State token."""
        session = self._session(token, request)
        session.controller.on_toggle_auto_approve(enabled)
        return session.token

    def validation_status(self, token: str | None, request: Any) -> str:
        """Read this owner's trusted validation state, never another session's."""
        return self._session(token, request).controller.validation_status()

    def approval_readiness(
        self, text: str, request_id: str, token: str | None, request: Any
    ) -> tuple[Any, str]:
        """Return the current proposal's UI-only approval readiness for its owner."""
        return self._session(token, request).controller.approval_readiness(text, request_id)

    def unload(self, request: Any) -> None:
        """Cancel this framework owner's pending work when its browser unloads."""
        self.registry.close_owner(getattr(request, "session_hash", None))
