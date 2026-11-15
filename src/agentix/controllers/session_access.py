"""Shared owner resolution for tab/sidebar callbacks without framework dependencies."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from agentix.controllers.sessions import Session, SessionRegistry


class SessionOwnerAccess:
    """Require verified browser routing and token ownership before service access."""

    def __init__(self, registry: SessionRegistry) -> None:
        """Retain only the server registry, never a global active controller."""
        self.registry = registry

    def _session(self, token: str | None, request: Any) -> Session:
        """Resolve trusted framework routing metadata and opaque server State."""
        return self.registry.resolve(token, getattr(request, "session_hash", None))
