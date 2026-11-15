"""Validate version-3 catalog-driven package closures without importing their code."""

import hashlib
import json
from pathlib import Path

from agentix.domain.tool_schema import extract_tool_schema
from agentix.storage.catalog_lock import reject_alias
from agentix.widgets.styles import validate_widget_css


class RuntimeSourceChanged(ValueError):
    """A maintained runtime member differs from the exact installed package copy.

    Callers distinguish this drift from tampered application bytes; it stays a
    ``ValueError`` so existing bounded rejection paths keep working unchanged.
    """


def runtime_template(name: str) -> Path:
    """Return one maintained version-3 runtime member from the connection-code set.

    The version-3 package has a single maintained runtime generation, so every
    allowlisted member resolves inside ``templates/code`` through the
    connection-code contract; no legacy template path remains resolvable.
    """
    from agentix.application.code_package import runtime_template as code_template

    return code_template(name)


def validate_manifest(manifest: dict) -> set[str]:
    """Require the bounded exact unprivileged manifest and its typed catalog closure."""
    if manifest.get("schema_version") != 3:
        raise ValueError("Unsupported application schema version")
    from agentix.application.code_package import validate_manifest as validate_code_manifest

    return validate_code_manifest(manifest)


def capture(folder: Path) -> tuple[tuple[str, bytes], ...]:
    """Capture bounded exact files; reject aliases, changed hashes and tool schemas."""
    return _capture(folder, allow_runtime_drift=False)


def capture_with_current_runtime(folder: Path) -> tuple[tuple[str, bytes], ...]:
    """Capture an installed package, replacing only drifted maintained runtime members.

    The caller must already hold an explicit human decision for this exact
    application and must re-run the independent gates on the returned bytes.
    Application-owned members keep their exact installed bytes and are still
    checked against the manifest, so this never authorizes changed application
    source. The returned snapshot therefore has a different identity than the
    installed digest, and no record may be resealed from it.
    """
    return _capture(folder, allow_runtime_drift=True)


def _capture(folder: Path, *, allow_runtime_drift: bool) -> tuple[tuple[str, bytes], ...]:
    """Validate one package closure; runtime drift is either rejected or refreshed."""
    from agentix.application.code_package import SHARED as CODE_SHARED

    reject_alias(folder)
    manifest_path = folder / "application.json"
    reject_alias(manifest_path)
    if manifest_path.stat().st_size > 65536:
        raise ValueError("Application manifest exceeds limit")
    manifest = json.loads(manifest_path.read_bytes())
    expected = validate_manifest(manifest)
    if {member.name for member in folder.iterdir()} - {"__pycache__", "config.json"} != expected | {
        "application.json"
    }:
        raise ValueError("Unexpected application members")
    layout = folder / "config.json"
    if layout.exists():
        reject_alias(layout)
        if not layout.is_file() or layout.stat().st_size > 65536:
            raise ValueError("Invalid presentation config")
    data = {"application.json": manifest_path.read_bytes()}
    replaced: list[str] = []
    for name in sorted(expected):
        member = folder / name
        reject_alias(member)
        if not member.is_file() or member.stat().st_size > 65536:
            raise ValueError("Invalid application member")
        body = member.read_bytes()
        if hashlib.sha256(body).hexdigest() != manifest["files"][name]:
            raise ValueError("Application content differs from manifest")
        if name.endswith(".py"):
            compile(body, name, "exec")
        if name == "application_logic.py":
            from agentix.domain.application_code import validate_connection_source

            validate_connection_source(body.decode("utf-8"))
        if name in CODE_SHARED:
            current = runtime_template(name).read_bytes()
            if body != current:
                if not allow_runtime_drift:
                    raise RuntimeSourceChanged("Maintained compositor source was modified")
                body = current
                compile(body, name, "exec")
                replaced.append(name)
        data[name] = body
    if replaced:
        for name in replaced:
            manifest["files"][name] = hashlib.sha256(data[name]).hexdigest()
        data["application.json"] = json.dumps(manifest, indent=2).encode()
    for name, schema in manifest["tools"].items():
        if extract_tool_schema(name, data[name + "_code.py"].decode()) != schema:
            raise ValueError("Application tool schema differs from its exact source")
        validate_widget_css(data[name + "_widget.css"].decode(), name)
    return tuple(sorted(data.items()))


def validate_payload(payload: dict, manifest: dict) -> dict:
    """Validate external values against the exact schema-3 inputs without coercion."""
    from agentix.application.code_package import validate_payload as validate_code_payload

    return validate_code_payload(payload, manifest)


def validate_results(value: dict, manifest: dict) -> dict:
    """Reject missing, extra, oversized or incorrectly typed structured results."""
    from agentix.application.code_package import validate_results as validate_code_results

    return validate_code_results(value, manifest)
