"""Approval-aware UTF-8 artifact persistence and final Python validation.

The repository receives its path/approval boundary explicitly. It preserves the
legacy result strings and non-atomic write semantics; compile never executes.
"""

import hashlib
import logging
import os
from pathlib import Path

from .contracts import SecurityBoundary
from .diagnostics import log_event
from .paths import SecurityViolationError

logger = logging.getLogger(__name__)


class ArtifactStore:
    """Persist artifacts using an injected path and approval coordinator."""

    def __init__(self, security: SecurityBoundary) -> None:
        """Store the boundary without creating directories or requesting approval."""
        self.security = security

    def write(self, tool_name: str, filename: str, content: str, mode: str = "w") -> str:
        """
        Write/append UTF-8 content after path and human authorization checks.

        For Python artifacts, compile the final approved text without executing
        it before opening the destination. Appends validate the combined file.
        Rejected/invalid edits leave existing file contents intact. Errors retain
        the legacy string-result contract; invalid paths raise SecurityViolationError.
        Syntax validation is not a safety guarantee for executable Python.
        """
        target_path = self.security.validate_and_resolve_path(tool_name, filename)
        write_identity = (self.security.owner_id, self.security.operation_id)
        target_dir = os.path.dirname(target_path)

        # 1. Authorize directory creation if needed
        if not os.path.exists(target_dir):
            approved, _ = self.security.request_user_permission(
                target_dir, action="create directory", content=f"Directory: {target_dir}"
            )
            if not approved:
                return f"Operation aborted: Directory creation rejected for '{target_dir}'."
            os.makedirs(target_dir, exist_ok=True)

        # 2. Authorize file creation / write (captures user edits if any)
        action_name = "append to file" if mode == "a" else "write/overwrite file"
        approved, final_content = self.security.request_user_permission(
            target_path, action=action_name, content=content
        )
        if not approved:
            return f"Operation aborted: Write authorization denied for '{target_path}'."

        try:
            # Approval can take minutes. Reject a destination that changed while
            # waiting rather than writing to a newly resolved link destination.
            if self.security.validate_and_resolve_path(tool_name, filename) != target_path:
                raise SecurityViolationError("Artifact destination changed during approval")
            # A confined link may change the resolved suffix. Validate Python
            # when either the approved name or its actual destination is Python.
            if ".py" in (Path(filename).suffix.lower(), Path(target_path).suffix.lower()):
                candidate = final_content
                if mode == "a" and os.path.exists(target_path):
                    with open(target_path, encoding="utf-8") as existing:
                        candidate = existing.read() + final_content
                try:
                    compile(candidate, target_path, "exec")
                except (SyntaxError, ValueError, TypeError) as exc:
                    # Report location/type only: source lines may contain secrets.
                    log_event(
                        logger,
                        "approved_python_rejected",
                        error=exc,
                        level=logging.WARNING,
                        line=getattr(exc, "lineno", None),
                    )
                    return "Error validating Python: approved content has invalid syntax"
                log_event(logger, "approved_python_validated", level=logging.DEBUG)
            with open(target_path, mode, encoding="utf-8") as f:
                f.write(final_content)
            if mode == "w" and filename in {
                f"{tool_name}_specifications.md",
                f"{tool_name}_code.py",
                f"{tool_name}_tests.py",
            }:
                # Hash actual persisted bytes (including platform newline conversion),
                # never the model proposal. Oversized artifacts cannot advance a stage.
                with open(target_path, "rb") as stream:
                    observed = stream.read(1_048_577)
                expected = final_content.replace("\n", os.linesep).encode("utf-8")
                if observed != expected:
                    log_event(logger, "artifact_receipt_mismatch", level=logging.WARNING)
                    return "Error writing file: persisted content changed; approval receipt denied."
                if len(observed) <= 1_048_576:
                    self.security.record_saved_artifact(
                        target_path,
                        hashlib.sha256(observed).hexdigest(),
                        owner_id=write_identity[0],
                        operation_id=write_identity[1],
                    )
            log_event(logger, "artifact_saved")
            return f"Success: Content written to {target_path}"
        except Exception as e:
            log_event(logger, "artifact_write_failed", error=e, level=logging.ERROR)
            return f"Error writing file: {str(e)}"
