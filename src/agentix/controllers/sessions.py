"""Bounded server-owned workflow sessions with owner-bound opaque tokens.

Gradio session hashes provide routing, not account authentication. Tokens remain
in server-side State, and every callback must verify both token and request owner.
"""

import logging
import secrets
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from uuid import uuid4

from agentix.diagnostics import log_event, operation_scope

logger = logging.getLogger(__name__)

DEFAULT_MAX_SESSIONS = 128  # Concurrent owner sessions retained by one registry.
DEFAULT_IDLE_TIMEOUT_SECONDS = 1800  # Idle expiry for an owner without running work.
MAX_OWNER_IDENTIFIER_LENGTH = 256  # Longest accepted framework owner identifier.


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
        max_sessions: int = DEFAULT_MAX_SESSIONS,
        idle_timeout: float = DEFAULT_IDLE_TIMEOUT_SECONDS,
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
        with operation_scope(session.session_id):
            log_event(logger, "session_closing", level=logging.DEBUG)
            close = getattr(session.controller, "close", None)
            if callable(close):
                close()
            else:
                session.controller.security.cancel_pending()
            self._sessions.pop(session.token, None)
            self._owners.pop(session.owner, None)
            log_event(logger, "session_closed", level=logging.DEBUG)

    def resolve(self, token: str | None, owner: str) -> Session:
        """Return/create this owner's session, rejecting untrusted token changes.

        Initial callbacks can race with no token; the owner index makes creation
        idempotent. Active workers are not silently evicted by idle expiry.
        """
        if (
            not isinstance(owner, str)
            or not owner
            or not owner.isascii()
            or len(owner) > MAX_OWNER_IDENTIFIER_LENGTH
        ):
            log_event(logger, "session_owner_rejected", level=logging.WARNING)
            raise SessionAccessError("A framework session owner is required")
        with self._lock:
            now = self.clock()
            for session in list(self._sessions.values()):
                if (
                    now - session.last_seen >= self.idle_timeout
                    and not session.controller.state.is_running
                ):
                    with operation_scope(session.session_id):
                        log_event(logger, "session_expired", level=logging.DEBUG)
                    self._remove(session)
            if token:
                session = self._sessions.get(token)
                if session is None or not secrets.compare_digest(session.owner, owner):
                    log_event(logger, "session_access_rejected", level=logging.WARNING)
                    raise SessionAccessError("Session expired or owner does not match")
            elif owner in self._owners:
                session = self._sessions[self._owners[owner]]
            else:
                if len(self._sessions) >= self.max_sessions:
                    log_event(logger, "session_capacity_rejected", level=logging.WARNING)
                    raise SessionAccessError("Session capacity reached; try again later")
                token = secrets.token_urlsafe(32)
                # A diagnostic ID must not expose the opaque browser capability.
                session_id = uuid4().hex
                with operation_scope(session_id):
                    log_event(logger, "session_creating", level=logging.DEBUG)
                    try:
                        controller = self.factory(session_id)
                    except Exception as error:
                        log_event(
                            logger, "session_creation_failed", error=error, level=logging.ERROR
                        )
                        raise
                    log_event(logger, "session_created", level=logging.DEBUG)
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


# Preserve the public callback import used by prior adapters.
from agentix.ui.callback_compat import SessionCallbacks  # noqa: E402,F401
