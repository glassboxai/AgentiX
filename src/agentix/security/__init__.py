"""Compatibility security facade composing approval, draft and public tool storage."""

import re
from pathlib import Path

from agentix.security.approvals import ApprovalCoordinator
from agentix.security.paths import SecurityViolationError, resolve_artifact_path
from agentix.settings import Settings
from agentix.storage.artifacts import ArtifactStore

__all__ = ["SecurityManager", "SecurityViolationError"]


class SecurityManager(ApprovalCoordinator):
    """Preserve the class API used by callbacks and tool operations.

    Runtime-specific subclasses receive explicit storage roots. The default class
    retains the legacy process-wide coordinator for compatibility imports.
    """

    TOOLS_ROOT_DIR: str = ""
    PUBLISHED_TOOLS_ROOT_DIR: str | None = None
    DRAFTS_ROOT_DIR: str | None = None
    _active_draft_root: str | None = None

    @classmethod
    def _own_root(cls, name: str) -> str | None:
        """Return a storage root only when this exact class configured it.

        Roots are mutable class state. Reading them through normal attribute
        lookup would let a subclass inherit a base-class runtime configuration
        and route its drafts or publication into another owner's catalog, so
        only the defining class's own namespace counts here.
        """
        return cls.__dict__.get(name)

    @classmethod
    def _tools_root(cls) -> str:
        """Resolve the effective tool root, failing closed when unconfigured.

        The default class resolves AGENTIX_TOOLS_ROOT lazily so importing this
        module never requires deployment configuration or creates storage.
        """
        configured = cls.TOOLS_ROOT_DIR
        if configured:
            return configured
        return str(Settings.from_environment().tools_root)

    @classmethod
    def published_tools_root(cls) -> str:
        """Return the installed catalog root, never an active draft directory.

        ``TOOLS_ROOT_DIR`` points at the isolated proposal while a tool is being
        created, so an explorer action must resolve the published root instead.
        Nothing is created and no directory is enumerated here.
        """
        return cls._own_root("PUBLISHED_TOOLS_ROOT_DIR") or cls._tools_root()

    @classmethod
    def configure_tool_storage(cls, public_root: Path, drafts_root: Path) -> None:
        """Bind public catalog and proposal roots without creating either directory."""
        cls.PUBLISHED_TOOLS_ROOT_DIR = str(Path(public_root).resolve())
        cls.DRAFTS_ROOT_DIR = str(Path(drafts_root).resolve())
        cls.TOOLS_ROOT_DIR = cls.PUBLISHED_TOOLS_ROOT_DIR
        cls._active_draft_root = None

    @classmethod
    def begin_tool_draft(cls, tool_name: str) -> None:
        """Route one creation operation to its isolated proposal root."""
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,127}", tool_name):
            raise ValueError("Invalid tool name")
        owner, operation = cls.owner_id, cls.operation_id or "legacy"
        if not all(
            re.fullmatch(r"[A-Za-z0-9_-]{1,128}", value or "") for value in (owner, operation)
        ):
            raise ValueError("Invalid draft ownership identity")
        public = Path(cls._own_root("PUBLISHED_TOOLS_ROOT_DIR") or cls._tools_root()).resolve()
        drafts = Path(cls._own_root("DRAFTS_ROOT_DIR") or (public.parent / "drafts")).resolve()
        active = drafts / owner / operation
        if active.is_relative_to(public):
            raise ValueError("Draft storage must be outside the public catalog")
        cls.PUBLISHED_TOOLS_ROOT_DIR = str(public)
        cls.DRAFTS_ROOT_DIR = str(drafts)
        cls._active_draft_root = str(active)
        cls.TOOLS_ROOT_DIR = str(active)

    @classmethod
    def publish_current_draft(cls, tool_name: str) -> None:
        """Publish current staged bytes to the public catalog after host acceptance."""
        from agentix.storage.tool_publication import publish_tool_draft

        active_draft = cls._own_root("_active_draft_root")
        published = cls._own_root("PUBLISHED_TOOLS_ROOT_DIR")
        if active_draft is None or published is None:
            raise ValueError("No active draft is available for publication")
        publish_tool_draft(Path(active_draft), Path(published), tool_name)
        cls.TOOLS_ROOT_DIR = published
        cls._active_draft_root = None

    @classmethod
    def restore_public_tool_storage(cls) -> None:
        """Leave a failed or completed proposal and restore public-catalog access."""
        published = cls._own_root("PUBLISHED_TOOLS_ROOT_DIR")
        if published is not None:
            cls.TOOLS_ROOT_DIR = published
        cls._active_draft_root = None

    @classmethod
    def validate_and_resolve_path(cls, tool_name: str, filename: str) -> str:
        """Delegate to the root-specific resolved containment policy."""
        return resolve_artifact_path(cls._tools_root(), tool_name, filename)

    @classmethod
    def safe_write_file(cls, tool_name: str, filename: str, content: str, mode: str = "w") -> str:
        """Delegate persistence using this exact coordinator for approval state."""
        return ArtifactStore(cls).write(tool_name, filename, content, mode)
