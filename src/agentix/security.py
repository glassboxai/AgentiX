"""Compatibility security facade composing independent policy and storage services."""

from .approvals import ApprovalCoordinator
from .paths import SecurityViolationError, resolve_artifact_path
from .settings import Settings
from .storage import ArtifactStore

__all__ = ["SecurityManager", "SecurityViolationError"]


class SecurityManager(ApprovalCoordinator):
    """Preserve the class API used by callbacks and tool operations.

    Runtime-specific subclasses receive explicit storage roots. The default class
    retains the legacy process-wide coordinator for compatibility imports.
    """

    TOOLS_ROOT_DIR: str = str(Settings.from_environment().tools_root)

    @classmethod
    def validate_and_resolve_path(cls, tool_name: str, filename: str) -> str:
        """Delegate to the root-specific resolved containment policy."""
        return resolve_artifact_path(cls.TOOLS_ROOT_DIR, tool_name, filename)

    @classmethod
    def safe_write_file(cls, tool_name: str, filename: str, content: str, mode: str = "w") -> str:
        """Delegate persistence using this exact coordinator for approval state."""
        return ArtifactStore(cls).write(tool_name, filename, content, mode)
