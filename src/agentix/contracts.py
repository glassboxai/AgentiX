"""Structural contracts shared by storage, execution and interface adapters."""

from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from .sandbox import SandboxResult


class SecurityBoundary(Protocol):
    """Required authorization/path API; it does not promise OS isolation."""

    auto_approve: bool
    owner_id: str
    operation_id: str
    activity_capture: Any

    def record_saved_artifact(
        self, path: str, digest: str, *, owner_id: str, operation_id: str
    ) -> None:
        """Bind a host-observed approved save to its original operation identity."""
        ...

    def get_artifact_receipt(self, path: str) -> tuple[str, str] | None:
        """Read the current operation's immutable save receipt and byte digest."""
        ...

    def validate_and_resolve_path(self, tool_name: str, filename: str) -> str:
        """Return a confined path or raise SecurityViolationError."""
        ...

    def request_user_permission(
        self,
        filepath: str,
        action: str = "write",
        content: str = "",
        *,
        require_manual: bool = False,
        review_context: dict[str, Any] | None = None,
    ) -> tuple[bool, str]:
        """Return approval and final edited text, denying on timeout."""
        ...

    def is_closed(self) -> bool:
        """Return whether the owner has been cancelled or unloaded."""
        ...

    def safe_write_file(self, tool_name: str, filename: str, content: str, mode: str = "w") -> str:
        """Persist approved content or return the existing textual error result."""
        ...

    def get_pending_request(self) -> dict[str, Any] | None:
        """Return an independent snapshot of the pending request."""
        ...

    def resolve_pending_request(
        self,
        decision: bool,
        edited_content: str | None = None,
        *,
        request_id: str | None = None,
        owner_id: str | None = None,
    ) -> bool:
        """Accept a matching, unexpired, single-use owner/request decision."""
        ...

    def cancel_pending(self) -> None:
        """Close the owner and deny pending/future writes."""
        ...


class ExecutionBackend(Protocol):
    """Injected process boundary shared by execution, tests and acceptance.

    Structural compatibility is not proof of isolation. Callers must still
    check isolation flags, process outcomes and current operation evidence.
    """

    def execute(
        self,
        code: bytes,
        tests: bytes | None,
        tool_name: str,
        function_name: str,
        kwargs: dict[str, Any],
    ) -> "SandboxResult":
        """Run approved bytes inside a bounded child and return an observation.

        Code and optional tests are exact staged source bytes; tool_name names
        their module, function_name selects the public callable (empty in test
        mode), and kwargs contains bounded JSON data. The returned process
        outcome includes an untrusted child report, not a semantic guarantee.
        Implementations may raise RuntimeError if provisioning is unavailable;
        callers must deny execution rather than introduce a host fallback.
        """
        ...
