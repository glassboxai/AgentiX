"""Owner-scoped rewrite of one scoped widget stylesheet without revoking approval.

The application identity excludes ``<tool>_widget.css`` members, so the closed
grammar in :mod:`agentix.widgets.styles` is the only gate a style edit passes.
This writer keeps the package self-consistent: it rewrites the member hash in
``application.json`` so capture still proves the bytes on disk are declared.
"""

import hashlib
import json
import re
from pathlib import Path

from agentix.storage.catalog_lock import reject_alias
from agentix.widgets.styles import STYLE_SUFFIX, validate_widget_css

MAX_STYLE_BYTES = 16384


def style_member_name(tool: str) -> str:
    """Resolve a canonical tool identifier to its scoped stylesheet member."""
    if not isinstance(tool, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", tool):
        raise ValueError("Select a widget from the generated application")
    return tool + STYLE_SUFFIX


def write_style_member(folder: Path, name: str, css: str) -> str:
    """Validate and persist one scoped stylesheet, rebinding only its manifest hash.

    Parameters: an absolute package folder, a ``<role>_widget.css`` member name and
    the complete replacement text. Returns the new SHA-256 of the written bytes.
    Raises ``ValueError`` for an unknown member, an unsafe declaration, an aliased
    path or a hard-linked file. No crash transaction is claimed across the two
    writes; a failure leaves capture rejecting the package rather than approving it.
    """
    if not isinstance(name, str) or not name.endswith(STYLE_SUFFIX):
        raise ValueError("Unknown widget style member")
    role = name.removesuffix(STYLE_SUFFIX)
    if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", role):
        raise ValueError("Unknown widget style member")
    validate_widget_css(css, role)
    body = css.encode("utf-8")
    if len(body) > MAX_STYLE_BYTES:
        raise ValueError("Widget style exceeds limit")
    if not isinstance(folder, Path) or not folder.is_absolute():
        raise ValueError("Invalid application package root")
    member = folder / name
    reject_alias(member)
    if not member.is_file() or member.stat().st_nlink != 1:
        raise ValueError("Invalid widget style member")
    manifest_path = folder / "application.json"
    reject_alias(manifest_path)
    manifest = json.loads(manifest_path.read_bytes())
    if name not in manifest.get("files", {}):
        raise ValueError("Widget style member is not declared by this package")
    manifest["files"][name] = hashlib.sha256(body).hexdigest()
    member.write_bytes(body)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest["files"][name]
