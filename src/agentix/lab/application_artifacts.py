"""Host-only complete package validation; never import application code.

Digests detect changes, not human approval. The reviewed digest comes from the
operator, outside the child-controlled package. The initial surface is fixed.
"""

import hashlib
import json
import stat
from dataclasses import dataclass
from pathlib import Path

from agentix.lab.ipc_protocol import decode_frame

LOCK_PATH = Path(__file__).resolve().parents[3] / "infra/runtime.lock.txt"


@dataclass(frozen=True)
class ApprovedApplication:
    """Immutable reviewed complete source/manifest snapshot."""

    files: tuple[tuple[str, bytes], ...]
    digest: str


def validate_result(value: object, manifest: dict) -> dict:
    """Reject coercion, negative counts and unknown fields in structured child results."""
    from agentix.application.general_package import validate_results

    return validate_results(value, manifest)


def _capture(folder: Path) -> tuple[tuple[str, bytes], ...]:
    """Validate the schema-3 package closure, lock, permissions and manifest."""
    if (
        not folder.is_absolute()
        or any(part.lower() == "generated_tools" for part in folder.parts)
        or (folder.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)
        or folder.resolve() != folder.absolute()
        or folder.drive.startswith("\\\\")
    ):
        raise ValueError("Invalid application package root")
    manifest_path = folder / "application.json"
    if (
        not manifest_path.is_file()
        or manifest_path.is_symlink()
        or manifest_path.stat().st_size > 65536
    ):
        raise ValueError("Application manifest is missing or invalid")
    if decode_frame(manifest_path.read_bytes()).get("schema_version") != 3:
        raise ValueError("Unsupported application schema version")
    from agentix.application.general_package import capture

    return capture(folder)


def application_digest(folder: Path) -> str:
    """Compute validated identity without granting authorization."""
    return _identity(_capture(folder))


def _identity(files: tuple[tuple[str, bytes], ...]) -> str:
    """Bind executable member names and bytes with unambiguous canonical JSON.

    Scoped widget stylesheets are deliberately excluded: their closed grammar in
    ``agentix.widgets.styles`` is the gate, so a colour, radius or font edit must
    not revoke an approval that covers the application's code. The declared style
    hashes inside ``application.json`` are dropped for the same reason, while every
    executable member hash in that manifest stays bound. The member hash on disk
    still ties those bytes to the package, so capture keeps rejecting a stylesheet
    edited outside the maintained writer.
    """
    from agentix.widgets.styles import STYLE_SUFFIX

    bound = {}
    for name, body in files:
        if name.endswith(STYLE_SUFFIX):
            continue
        if name == "application.json":
            body = _manifest_identity_bytes(body, STYLE_SUFFIX)
        bound[name] = hashlib.sha256(body).hexdigest()
    return hashlib.sha256(json.dumps(bound, sort_keys=True).encode()).hexdigest()


def _manifest_identity_bytes(body: bytes, suffix: str) -> bytes:
    """Drop declared style hashes so a style edit cannot move the identity."""
    try:
        manifest = json.loads(body)
    except ValueError:
        return body
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
        return body
    manifest["files"] = {
        name: value for name, value in manifest["files"].items() if not name.endswith(suffix)
    }
    return json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()


def approve_application(
    folder: Path, reviewed_digest: str, *, allow_runtime_drift: bool = False
) -> ApprovedApplication:
    """Capture exact reviewed bytes and reject changes before native startup.

    ``allow_runtime_drift`` is reserved for an explicit owner re-approval of an
    installed package whose only drift is a maintained runtime member; the
    captured snapshot then carries the current runtime bytes and its own digest.
    """
    from agentix.application.general_package import capture, capture_with_current_runtime

    files = capture_with_current_runtime(folder) if allow_runtime_drift else capture(folder)
    digest = _identity(files)
    if digest != reviewed_digest and not allow_runtime_drift:
        raise ValueError("Application changed after review")
    return ApprovedApplication(files, digest)
