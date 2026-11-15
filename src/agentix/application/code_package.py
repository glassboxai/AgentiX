"""Version-3 package contracts for native generated connection code, without graphs."""

import hashlib
import re
from pathlib import Path

from agentix.application.templates.code.application_values import validate_value
from agentix.domain.application_code import ApplicationCode
from agentix.lab.application_artifacts import LOCK_PATH

SHARED = {
    "app.py",
    "operation.py",
    "application_context.py",
    "element_ids.py",
    "application_values.py",
}


def runtime_template(name: str) -> Path:
    """Select exact maintained native runtime bytes; no generated imports occur here.

    Every version-3 member resolves inside this package so the connection-code
    runtime no longer depends on legacy template paths or the lab package.
    """
    if name not in SHARED:
        raise ValueError("Unknown connection-code runtime member")
    return Path(__file__).with_name("templates") / "code" / name


def validate_manifest(manifest: dict) -> set[str]:
    """Validate presentation/input contracts and exact dependency closure without edges."""
    if (
        set(manifest)
        != {
            "schema_version",
            "name",
            "gui_entry",
            "data_entry",
            "permissions",
            "runtime_lock_sha256",
            "files",
            "tools",
            "inputs",
            "widgets",
        }
        or type(manifest["schema_version"]) is not int
        or manifest["schema_version"] != 3
        or manifest["name"] != "catalog_application"
        or manifest["gui_entry"] != "app:create_application"
        or manifest["data_entry"] != "operation:analyze_text"
        or manifest["permissions"] != []
    ):
        raise ValueError("Invalid connection-code application manifest")
    if manifest["runtime_lock_sha256"] != hashlib.sha256(LOCK_PATH.read_bytes()).hexdigest():
        raise ValueError("Application runtime lock changed")
    tools = manifest["tools"]
    if (
        type(tools) is not dict
        or not 1 <= len(tools) <= 16
        or any(not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", name) for name in tools)
    ):
        raise ValueError("Invalid application catalog closure")
    ApplicationCode.model_validate(
        {
            "inputs": manifest["inputs"],
            "widgets": manifest["widgets"],
            "connection_code": 'def run(payload, call):\n    """Validate metadata only."""\n    pass\n',
            "notes": "",
        }
    ).validate_catalog(tools)
    if {widget["tool"] for widget in manifest["widgets"]} != set(tools):
        raise ValueError("Unused application tool dependency")
    expected = (
        SHARED
        | {"application_logic.py"}
        | {
            name + suffix
            for name in tools
            for suffix in ("_code.py", "_widget.py", "_widget.css", "_widget_tests.py")
        }
    )
    if set(manifest["files"]) != expected:
        raise ValueError("Unexpected connection-code file closure")
    return expected


def validate_payload(payload: dict, manifest: dict) -> dict:
    """Require every public application input, without numeric or string coercion."""
    if type(payload) is not dict or set(payload) != set(manifest["inputs"]):
        raise ValueError("Missing or unknown application input")
    for name, shape in manifest["inputs"].items():
        validate_value(payload[name], shape)
    return payload


def validate_results(results: dict, manifest: dict) -> dict:
    """Validate every observed tool output against its exact approved return type."""
    if type(results) is not dict or set(results) != {
        widget["id"] for widget in manifest["widgets"]
    }:
        raise ValueError("Missing or unknown application result")
    for widget in manifest["widgets"]:
        validate_value(results[widget["id"]], manifest["tools"][widget["tool"]]["returns"])
    return results


def validate_acceptance(value: dict, manifest: dict) -> dict:
    """Require host-held reviewed cases; never infer expected values from child code."""
    if type(value) is not dict or set(value) != {"payload", "expected"}:
        raise ValueError("Independent application acceptance requires payload and expected")
    try:
        validate_payload(value["payload"], manifest)
        validate_results(value["expected"], manifest)
    except (ValueError, KeyError, TypeError) as error:
        raise ValueError(
            "Complete independent application acceptance inputs and expected results before approval"
        ) from error
    return value
