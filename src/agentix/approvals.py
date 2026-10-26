"""Owner-bound approval requests with explicit, single-use decision identifiers."""

import logging
import threading
import time
from copy import deepcopy
from typing import Any
from uuid import uuid4

from .diagnostics import log_event

logger = logging.getLogger(__name__)


class ApprovalCoordinator:
    """Coordinate one pending request per owner without overwriting live work.

    Runtime owners use for_owner() or an independently configured subclass.
    Resolution requires both identifiers; missing/late/cross-owner decisions deny.
    This is workflow ownership, not authentication of a human account.
    """

    owner_id = "legacy"
    operation_id = ""
    activity_capture: Any = None
    approval_timeout = 300.0
    auto_approve = False
    _approval_event = threading.Event()
    _approval_decision = False
    _edited_content: str | None = None
    _pending_request: dict[str, Any] | None = None
    _resolved = False
    _closed = False
    _lock = threading.Lock()
    _saved_artifacts: dict[str, tuple[str, str, str, str]] = {}
    _clock = staticmethod(time.monotonic)

    @classmethod
    def for_owner(cls, owner_id: str, timeout: float = 300) -> type:
        """Create isolated synchronization/configuration for a server-owned identity."""
        if not owner_id or timeout <= 0:
            raise ValueError("An owner and positive approval timeout are required")
        return type(
            "OwnedApproval",
            (cls,),
            {
                "owner_id": owner_id,
                "approval_timeout": timeout,
                "auto_approve": False,
                "_approval_event": threading.Event(),
                "_lock": threading.Lock(),
                "_approval_decision": False,
                "_edited_content": None,
                "_pending_request": None,
                "_resolved": False,
                "_closed": False,
                "operation_id": "",
                "activity_capture": None,
                "_saved_artifacts": {},
            },
        )

    @classmethod
    def record_saved_artifact(
        cls, path: str, digest: str, *, owner_id: str, operation_id: str
    ) -> None:
        """Record a host-observed approved write, bounded to this owner/operation.

        The random receipt distinguishes a fresh approved save of identical bytes
        from a stale file. Only maintained storage code calls this after writing.
        This is workflow evidence, not a replacement for isolated test execution.
        """
        with cls._lock:
            if cls._closed or (owner_id, operation_id) != (cls.owner_id, cls.operation_id):
                return
            cls._saved_artifacts = {
                key: value
                for key, value in cls._saved_artifacts.items()
                if value[:2] == (owner_id, operation_id)
            }
            cls._saved_artifacts[path] = (owner_id, operation_id, uuid4().hex, digest)
            while len(cls._saved_artifacts) > 64:
                cls._saved_artifacts.pop(next(iter(cls._saved_artifacts)))

    @classmethod
    def get_artifact_receipt(cls, path: str) -> tuple[str, str] | None:
        """Return immutable write identity/digest only for the current live operation."""
        with cls._lock:
            receipt = cls._saved_artifacts.get(path)
            if cls._closed or receipt is None or receipt[:2] != (cls.owner_id, cls.operation_id):
                return None
            return receipt[2:]

    @classmethod
    def request_user_permission(
        cls,
        filepath: str,
        action: str = "write",
        content: str = "",
        *,
        require_manual: bool = False,
        review_context: dict[str, Any] | None = None,
    ) -> tuple[bool, str]:
        """Publish a uniquely identified request; deny on timeout or an occupied slot.

        Only the owning waiter cleans its slot. The event is never reused while
        another request is pending, preventing cross-request decisions/cleanup.
        """
        with cls._lock:
            if cls._closed:
                log_event(logger, "approval_session_closed", level=logging.WARNING)
                return False, content
            if cls.auto_approve and not require_manual:
                log_event(logger, "approval_automatic")
                return True, content
            if cls._pending_request is not None:
                log_event(logger, "approval_busy", level=logging.WARNING)
                return False, content
            cls._approval_event.clear()
            cls._approval_decision = False
            cls._edited_content = None
            cls._resolved = False
            request = {
                "request_id": uuid4().hex,
                "owner_id": cls.owner_id,
                "filepath": filepath,
                "action": action,
                "content": content,
                "expires_at": cls._clock() + cls.approval_timeout,
            }
            if require_manual:
                request["review_context"] = deepcopy(review_context or {})
            cls._pending_request = request
            log_event(logger, "approval_requested", request_id=request["request_id"])
        received = cls._approval_event.wait(timeout=cls.approval_timeout)
        with cls._lock:
            approved = bool(received and cls._resolved and cls._approval_decision)
            final = cls._edited_content if cls._edited_content is not None else content
            if cls._pending_request is request:
                cls._pending_request = None
                cls._edited_content = None
            log_event(
                logger,
                "approval_granted" if approved else "approval_denied",
                request_id=request["request_id"],
            )
        return approved, final

    @classmethod
    def is_closed(cls) -> bool:
        """Report owner shutdown without exposing mutable synchronization state."""
        with cls._lock:
            return cls._closed

    @classmethod
    def get_pending_request(cls) -> dict[str, Any] | None:
        """Return a deep-copy snapshot so readers cannot alter the pending slot."""
        with cls._lock:
            return deepcopy(cls._pending_request)

    @classmethod
    def resolve_pending_request(
        cls,
        decision: bool,
        edited_content: str | None = None,
        *,
        request_id: str | None = None,
        owner_id: str | None = None,
    ) -> bool:
        """Resolve exactly once if owner/request match and the deadline is valid.

        False means no authorization was accepted. Expiration wakes the owning
        waiter with denial; duplicate responses cannot overwrite its first result.
        """
        with cls._lock:
            pending = cls._pending_request
            if (
                pending is None
                or cls._resolved
                or type(decision) is not bool
                or (edited_content is not None and not isinstance(edited_content, str))
                or not request_id
                or not owner_id
                or owner_id != cls.owner_id
                or pending.get("owner_id") != owner_id
                or pending.get("request_id") != request_id
            ):
                log_event(logger, "approval_response_rejected", level=logging.WARNING)
                return False
            if cls._clock() >= pending["expires_at"]:
                cls._resolved = True
                cls._approval_decision = False
                cls._approval_event.set()
                log_event(logger, "approval_expired", request_id=request_id, level=logging.WARNING)
                return False
            cls._resolved = True
            cls._approval_decision = bool(decision)
            cls._edited_content = edited_content
            cls._approval_event.set()
            log_event(logger, "approval_response_accepted", request_id=request_id)
            return True

    @classmethod
    def cancel_pending(cls) -> None:
        """Deny outstanding work when its session closes, waking the waiter."""
        with cls._lock:
            cls._closed = True
            if cls._pending_request is not None and not cls._resolved:
                cls._resolved = True
                cls._approval_decision = False
                cls._approval_event.set()
                log_event(
                    logger, "approval_cancelled", request_id=cls._pending_request["request_id"]
                )
