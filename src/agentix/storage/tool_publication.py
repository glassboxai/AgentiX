"""Publish exact reviewed draft members into the public tool catalog."""

import os
import shutil
import uuid
from pathlib import Path

from agentix.security.paths import resolve_artifact_path

_MEMBERS = ("specifications.md", "code.py", "tests.py")


def publish_tool_draft(staging_root: Path, public_root: Path, tool_name: str) -> None:
    """Copy exact reviewed draft bytes to a new public directory without overwrite.

    The caller must have completed human acceptance for the current bytes. This
    helper performs no approval decision and retains the source draft as evidence.
    """
    source = Path(
        resolve_artifact_path(str(staging_root), tool_name, tool_name + "_code.py")
    ).parent
    destination = Path(
        resolve_artifact_path(str(public_root), tool_name, tool_name + "_code.py")
    ).parent
    files = {name: source / (tool_name + "_" + name) for name in _MEMBERS}
    if destination.exists():
        raise ValueError("Public tool directory already exists")
    payloads = {}
    for name, path in files.items():
        if not path.is_file() or path.is_symlink():
            raise ValueError("Reviewed draft member is missing")
        content = path.read_bytes()
        if not content or len(content) > 1_048_576:
            raise ValueError("Reviewed draft member is empty or oversized")
        payloads[name] = content
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.parent / ("." + tool_name + ".publishing-" + uuid.uuid4().hex)
    try:
        temporary.mkdir()
        for name, content in payloads.items():
            (temporary / (tool_name + "_" + name)).write_bytes(content)
        os.replace(temporary, destination)
        if any(
            (destination / (tool_name + "_" + name)).read_bytes() != content
            for name, content in payloads.items()
        ):
            raise ValueError("Published tool bytes changed during publication")
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
