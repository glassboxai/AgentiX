"""Stable explicit per-user v7 paths; resolving a path never creates directories."""

import os
import stat
from collections.abc import Mapping
from pathlib import Path

_LEGACY_NAMESPACES = (("agentix", "v5"), ("agentix-data", "v5"))


def require_v7_namespace(path: Path, label: str) -> Path:
    """Reject a resolved path inside the retired AgentiX v5 persistent namespace.

    Comparison uses whole path segments of the resolved path, so an unrelated
    directory whose name merely contains ``v5`` is accepted. Nothing is created.
    """
    resolved = Path(path).resolve()
    parts = tuple(part.casefold() for part in resolved.parts)
    for index in range(len(parts) - 1):
        if (parts[index], parts[index + 1]) in _LEGACY_NAMESPACES:
            raise ValueError(
                f"{label} resolves to the retired AgentiX v5 storage namespace: {resolved}. "
                "Point it at the AgentiX v7 data root instead; v5 data is not reused."
            )
    return resolved


def user_home(environment: Mapping[str, str] | None = None) -> Path:
    """Return the explicitly configured deployment home; no legacy default applies.

    AGENTIX_HOME is mandatory because the retired v5 profile must never receive
    v7 state. Relative roots, traversal and existing aliases are rejected, and no
    files are read recursively.
    """
    values = os.environ if environment is None else environment
    configured = values.get("AGENTIX_HOME")
    if not configured:
        raise ValueError(
            "AGENTIX_HOME must name the AgentiX v7 data root; the IaC launcher sets it "
            "and no v5 fallback is applied"
        )
    root = Path(configured)
    if not root.is_absolute() or ".." in root.parts:
        raise ValueError("AGENTIX_HOME must be an absolute directory")
    for part in (root, *root.parents):
        if part.is_symlink() or (
            part.exists()
            and part.stat(follow_symlinks=False).st_file_attributes
            & stat.FILE_ATTRIBUTE_REPARSE_POINT
        ):
            raise ValueError("Data aliases are forbidden")
    return require_v7_namespace(root, "AGENTIX_HOME")


def data_directory(environment: Mapping[str, str] | None = None) -> Path:
    """Return the common data root for tools, apps, grants and model metadata."""
    return user_home(environment) / "data"
