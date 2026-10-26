"""Payload-free correlated events and context-local activity routing.

No per-worker stdout replacement is performed. The optional host router only
copies output associated with the current context to its own session capture.
Unrelated/background threads without context never enter another session buffer.
"""

import logging
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, TextIO
from uuid import uuid4

_session: ContextVar[str] = ContextVar("agentix_session", default="legacy")
_operation: ContextVar[str] = ContextVar("agentix_operation", default="")
_capture: ContextVar[Any] = ContextVar("agentix_capture", default=None)


@contextmanager
def operation_scope(
    session_id: str | None = None, operation_id: str | None = None, capture: Any = None
) -> Iterator[str]:
    """Bind diagnostic identity/activity and restore the caller's context afterward."""
    operation = operation_id or _operation.get() or uuid4().hex
    tokens = (
        _session.set(session_id or _session.get()),
        _operation.set(operation),
        _capture.set(capture if capture is not None else _capture.get()),
    )
    try:
        yield operation
    finally:
        _capture.reset(tokens[2])
        _operation.reset(tokens[1])
        _session.reset(tokens[0])


def log_event(
    logger: logging.Logger,
    event: str,
    *,
    request_id: str = "-",
    error: BaseException | None = None,
    level: int = logging.INFO,
    line: int | None = None,
) -> None:
    """Log fixed event/identity/type fields, never exception text or user payloads."""
    logger.log(
        level,
        "event=%s session_id=%s operation_id=%s request_id=%s error_type=%s line=%s",
        event,
        _session.get(),
        _operation.get() or "-",
        request_id,
        type(error).__name__ if error is not None else "-",
        line if line is not None else "-",
    )
    capture = _capture.get()
    if capture is not None:
        capture.write(f"{event} | operation={_operation.get()}\n")


class ActivityRouter:
    """One host stdout proxy that routes only explicitly scoped activity."""

    def __init__(self, original_stdout: TextIO) -> None:
        """Retain the actual host stream; never install the proxy implicitly."""
        self.original_stdout = original_stdout

    def write(self, text: str) -> int:
        """Mirror output through its own capture, or directly to the host."""
        from .credentials import redact

        text = redact(text)
        capture = _capture.get()
        if capture is not None:
            capture.write(text)
        else:
            self.original_stdout.write(text)
        return len(text)

    def flush(self) -> None:
        """Flush the actual host stream."""
        self.original_stdout.flush()

    def __getattr__(self, name: str) -> Any:
        """Preserve encoding, terminal and file-descriptor access."""
        return getattr(self.original_stdout, name)


@contextmanager
def activity_output() -> Iterator[None]:
    """Route verbose stdout for the lifetime of a server, restoring it on exit.

    Install once at startup, never per worker. Context-local captures associate
    both SDK messages and technical events with the owning GUI session. Nested
    startup contexts reuse the existing router instead of duplicating messages.
    """
    original = sys.stdout
    if isinstance(original, ActivityRouter):
        yield
        return
    sys.stdout = ActivityRouter(original)
    try:
        yield
    finally:
        sys.stdout = original
