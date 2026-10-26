"""Resolved artifact containment and Windows component validation.

No storage is inspected during import. Callers pass a trusted storage root.
Existing links are resolved at call time; this is not race-proof OS isolation.
"""

import logging
import ntpath
import re
from pathlib import Path

from .diagnostics import log_event

logger = logging.getLogger(__name__)


class SecurityViolationError(Exception):
    """An artifact path violates the configured storage boundary."""


def resolve_artifact_path(root_directory: str, tool_name: str, filename: str) -> str:
    """Return an absolute artifact path confined to one named tool directory.

    Args:
        tool_name: One portable directory component, without drive syntax.
        filename: Relative artifact path; nested directories are supported.

    Raises:
        SecurityViolationError: Invalid Windows names, traversal, aliases or
            resolved paths outside the configured root/tool boundary.

    Existing links are resolved before checking components. A tool directory
    may not alias another directory. This does not eliminate races against a
    hostile process changing filesystem links after validation.
    """
    try:
        if not isinstance(tool_name, str) or not isinstance(filename, str):
            raise ValueError("Path names must be strings")
        # Check Windows drive/UNC syntax even when tests run on another OS.
        if (
            not tool_name
            or "/" in tool_name
            or "\\" in tool_name
            or ntpath.splitdrive(tool_name)[0]
            or ntpath.splitdrive(filename)[0]
            or filename.startswith(("/", "\\"))
        ):
            raise ValueError("Only relative artifact paths are permitted")
        parts = re.split(r"[/\\]", filename)
        for part in [tool_name, *parts]:
            # Windows aliases (NUL, trailing dots, ADS) must never resolve
            # differently from the name that was displayed for approval.
            if (
                not part
                or part in (".", "..")
                or part.endswith((" ", "."))
                or re.search(r'[<>:"|?*\x00-\x1f]', part)
                or re.fullmatch(
                    r"(CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])(?:\..*)?", part, re.IGNORECASE
                )
            ):
                raise ValueError("Invalid or ambiguous path component")
        root = Path(root_directory).resolve()
        expected_tool = root / tool_name
        tool_dir = expected_tool.resolve()
        tool_dir.relative_to(root)
        if tool_dir != expected_tool:
            raise ValueError("Tool directory aliases are not permitted")
        target = tool_dir.joinpath(*parts).resolve()
        target.relative_to(tool_dir)
        if target == tool_dir:
            raise ValueError("An artifact must name a file")
    except (ValueError, OSError, RuntimeError) as exc:
        log_event(logger, "artifact_path_rejected", error=exc, level=logging.WARNING)
        raise SecurityViolationError("Access denied: invalid or escaping artifact path") from exc
    log_event(logger, "artifact_path_validated", level=logging.DEBUG)
    return str(target)
