"""Bounded server-owned workflow sessions with owner-bound opaque tokens.

Gradio session hashes provide routing, not account authentication. Tokens remain
in server-side State, and every callback must verify both token and request owner.
"""

import secrets
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from uuid import uuid4

from ..diagnostics import operation_scope


class SessionAccessError(ValueError):
    """A stale, unknown or cross-owner session cannot be accessed."""


@dataclass
class Session:
    """Registry-owned session identity, controller and last activity timestamp."""

    token: str
    owner: str
    controller: Any
    last_seen: float
    session_id: str


class SessionRegistry:
    """Create isolated controllers and reject foreign/stale browser tokens."""

    def __init__(
        self,
        factory: Callable[[str], Any],
        *,
        max_sessions: int = 128,
        idle_timeout: float = 1800,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        """Configure bounded sessions; construction creates no runtime or model."""
        if max_sessions < 1 or idle_timeout <= 0:
            raise ValueError("Session capacity and idle timeout must be positive")
        self.factory, self.max_sessions = factory, max_sessions
        self.idle_timeout, self.clock = idle_timeout, clock
        self._sessions: dict[str, Session] = {}
        self._owners: dict[str, str] = {}
        self._lock = threading.RLock()

    def _remove(self, session: Session) -> None:
        """Cancel pending writes before dropping a closed/expired owner's state."""
        close = getattr(session.controller, "close", None)
        if callable(close):
            close()
        else:
            session.controller.security.cancel_pending()
        self._sessions.pop(session.token, None)
        self._owners.pop(session.owner, None)

    def resolve(self, token: str | None, owner: str) -> Session:
        """Return/create this owner's session, rejecting untrusted token changes.

        Initial callbacks can race with no token; the owner index makes creation
        idempotent. Active workers are not silently evicted by idle expiry.
        """
        if not isinstance(owner, str) or not owner or not owner.isascii() or len(owner) > 256:
            raise SessionAccessError("A framework session owner is required")
        with self._lock:
            now = self.clock()
            for session in list(self._sessions.values()):
                if (
                    now - session.last_seen >= self.idle_timeout
                    and not session.controller.state.is_running
                ):
                    self._remove(session)
            if token:
                session = self._sessions.get(token)
                if session is None or not secrets.compare_digest(session.owner, owner):
                    raise SessionAccessError("Session expired or owner does not match")
            elif owner in self._owners:
                session = self._sessions[self._owners[owner]]
            else:
                if len(self._sessions) >= self.max_sessions:
                    raise SessionAccessError("Session capacity reached; try again later")
                token = secrets.token_urlsafe(32)
                # A diagnostic ID must not expose the opaque browser capability.
                session_id = uuid4().hex
                with operation_scope(session_id):
                    controller = self.factory(session_id)
                session = Session(token, owner, controller, now, session_id)
                self._sessions[token], self._owners[owner] = session, token
            session.last_seen = now
            return session

    def close(self, token: str | None, owner: str) -> None:
        """Close only a matching owner; stale/unrelated unloads cannot cancel work."""
        with self._lock:
            session = self._sessions.get(token or "")
            if session is not None and secrets.compare_digest(session.owner, owner):
                self._remove(session)

    def close_state(self, token: str | None) -> None:
        """Trusted Gradio State cleanup hook; never register as a public callback."""
        with self._lock:
            session = self._sessions.get(token or "")
            if session is not None:
                self._remove(session)

    def close_owner(self, owner: str | None) -> None:
        """Handle a trusted framework unload request without requiring UI inputs."""
        with self._lock:
            token = self._owners.get(owner or "")
            if token is not None:
                self._remove(self._sessions[token])


class SessionCallbacks:
    """Framework-independent browser callbacks; every operation rechecks ownership."""

    def __init__(self, registry: SessionRegistry) -> None:
        """Retain only the server registry, never a global active controller."""
        self.registry = registry

    def _session(self, token: str | None, request: Any) -> Session:
        """Resolve trusted framework routing metadata and opaque server State."""
        return self.registry.resolve(token, getattr(request, "session_hash", None))

    def submit(self, message: str, token: str | None, request: Any) -> tuple[Any, ...]:
        """Submit to this browser's controller and update its server State token."""
        session = self._session(token, request)
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

    def configure_model(
        self,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
        consent: bool,
        token: str | None,
        request: Any,
    ) -> tuple[str, str, str]:
        """Verify browser ownership; clear the key input on both success and failure."""
        session = self._session(token, request)
        try:
            status = session.controller.configure_model(provider, model, endpoint, key, consent)
        except Exception:
            status = "Model configuration was not applied. Check the provider, key, consent and pending operation/review."
        return "", status, session.token

    def model_menu(
        self,
        action: str,
        identity: str,
        name: str,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
        token: str | None,
        request: Any,
    ) -> tuple[Any, ...]:
        """Dispatch fixed profile actions after owner checks; never return secrets."""
        session = self._session(token, request)
        return (
            *session.controller.profile_action(
                action, identity, name, provider, model, endpoint, key
            ),
            session.token,
        )

    def refresh_models(
        self, endpoint: str, token: str | None, request: Any
    ) -> tuple[list[str], str, str]:
        """Read only the local Ollama catalog after checking the browser owner."""
        from ..model_profiles import installed_models

        session = self._session(token, request)
        try:
            configuration = session.controller.model_configuration
            reader = configuration.catalog_reader if configuration is not None else None
            names = installed_models(endpoint, reader)
            status = "Installed Ollama models refreshed."
            if "qwen3-coder:30b" not in names:
                status += " Default qwen3-coder:30b is not installed; no download was started."
        except Exception:
            names = []
            status = "Could not read installed models. Check the local Ollama endpoint and service."
        return names, status, session.token

    def validation_status(self, token: str | None, request: Any) -> str:
        """Read this owner's trusted validation state, never another session's."""
        return self._session(token, request).controller.validation_status()

    def unload(self, request: Any) -> None:
        """Cancel this framework owner's pending work when its browser unloads."""
        self.registry.close_owner(getattr(request, "session_hash", None))
