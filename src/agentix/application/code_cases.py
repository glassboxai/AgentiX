"""Suggest bounded schema-3 cases using reviewed JSON values and inert AST matching.

No generated Python is imported, compiled or executed. Only direct assignments,
JSON references and canonical call statements can propagate reviewed expectations.
Unsupported syntax leaves explicit pending fields for human completion.
"""

import ast
import itertools
import json
from copy import deepcopy
from typing import Any

from agentix.domain.tool_schema import validate_value
from agentix.storage.application_catalog import ApprovedTool

MAX_PROPOSALS = 4096  # Maximum candidate payloads inspected per proposal.
MAX_VALUES = 32  # Maximum reviewed values considered per public input.


def _same(left: Any, right: Any) -> bool:
    """Compare JSON values without conflating booleans and integer values."""
    return json.dumps(left, sort_keys=True) == json.dumps(right, sort_keys=True)


def _reference(node: ast.expr, payload: dict, bindings: dict) -> Any:
    """Resolve only JSON constants/names/indexing; reject arbitrary Python work."""
    if isinstance(node, ast.Constant) and type(node.value) in {str, int, float, bool, type(None)}:
        return node.value
    if isinstance(node, ast.Name) and node.id in bindings:
        return bindings[node.id]
    if isinstance(node, ast.Subscript):
        if isinstance(node.value, ast.Name) and node.value.id == "payload":
            return payload[_reference(node.slice, payload, bindings)]
        value = _reference(node.value, payload, bindings)
        index = _reference(node.slice, payload, bindings)
        if type(value) is list and type(index) is int:
            return value[index]
    raise ValueError("Unsupported declarative reference")


def _match(
    statements: list[ast.stmt], payload: dict, widgets: dict, cases: dict, tools: dict
) -> dict:
    """Match direct calls to reviewed kwargs and copy only their approved results."""
    bindings, expected = {}, {}
    for statement in statements:
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Constant):
            continue
        target = None
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
        ):
            target = statement.targets[0].id
            expression = statement.value
        elif isinstance(statement, ast.Expr):
            expression = statement.value
        else:
            break
        try:
            if isinstance(expression, ast.Call):
                if (
                    not isinstance(expression.func, ast.Name)
                    or expression.func.id != "call"
                    or len(expression.args) != 1
                ):
                    break
                identity = _reference(expression.args[0], payload, bindings)
                if (
                    identity not in widgets
                    or identity in expected
                    or any(k.arg is None for k in expression.keywords)
                ):
                    break
                schema = tools[widgets[identity]].schema
                kwargs = dict(schema.get("defaults", {}))
                kwargs.update(
                    {k.arg: _reference(k.value, payload, bindings) for k in expression.keywords}
                )
                found = next(
                    (
                        case
                        for case in cases[identity]
                        if _same(dict(schema.get("defaults", {})) | case["kwargs"], kwargs)
                    ),
                    None,
                )
                if found is None:
                    break
                value = deepcopy(found["expect"]["value"])
                validate_value(value, schema["returns"])
                expected[identity] = value
            else:
                value = _reference(expression, payload, bindings)
            if target is not None:
                if target in {"payload", "call"}:
                    break
                bindings[target] = value
        except (ValueError, KeyError, TypeError, IndexError):
            break
    return expected


def propose_cases(assembly: dict, tools: dict[str, ApprovedTool]) -> dict:
    """Return editable reviewed-data suggestions, provenance and unresolved fields.

    Search is bounded and may be incomplete; proposals never authorize execution.
    Callers must still validate exact schemas and require explicit human review.
    Missing/incompatible cases and unsupported Python remain pending, not predicted.
    """
    widgets = {item["id"]: item["tool"] for item in assembly["widgets"]}
    cases = {
        identity: [
            case
            for case in (tools[name].reviewed_contract or {}).get("cases", [])
            if case["function"] == tools[name].function and case["expect"]["kind"] == "value"
        ]
        for identity, name in widgets.items()
    }
    domains = {}
    values = [
        value for choices in cases.values() for case in choices for value in case["kwargs"].values()
    ]
    for name, shape in assembly["inputs"].items():
        domains[name] = []
        for value in values:
            try:
                validate_value(value, shape)
            except ValueError:
                continue
            if not any(_same(value, prior) for prior in domains[name]):
                domains[name].append(deepcopy(value))
            if len(domains[name]) >= MAX_VALUES:
                break
    tree = ast.parse(assembly["connection_code"])
    entry = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "run"),
        None,
    )
    names = [name for name, choices in domains.items() if choices]
    best_payload, best_expected = {}, {}
    for values in itertools.islice(
        itertools.product(*(domains[name] for name in names)), MAX_PROPOSALS
    ):
        payload = dict(zip(names, values, strict=True))
        expected = _match(entry.body, payload, widgets, cases, tools) if entry else {}
        if len(expected) > len(best_expected):
            best_payload, best_expected = payload, expected
        if len(expected) == len(widgets):
            break
    pending = [f"payload.{name}" for name in assembly["inputs"] if name not in best_payload]
    pending += [f"expected.{name}" for name in widgets if name not in best_expected]
    return {
        "widgets": cases,
        "payload": best_payload,
        "expected": best_expected,
        "pending": pending,
        "provenance": {name: "Reviewed catalog value case" for name in best_expected},
    }


def acceptance_status(snapshot: dict) -> tuple[bool, str]:
    """Return safe persistent review guidance and validity; never expose case values.

    Missing fields are computed from current data, not historical proposal metadata.
    A valid shape still requires the existing owner-bound human approval gate.
    """
    from agentix.application.code_package import validate_acceptance

    manifest = snapshot.get("manifest", {})
    if manifest.get("schema_version") != 3:
        return True, "Review the independent catalog acceptance cases before approval."
    acceptance = snapshot.get("independent_acceptance", {})
    payload, expected = acceptance.get("payload", {}), acceptance.get("expected", {})
    missing = [
        f"payload.{name}"
        for name in manifest["inputs"]
        if type(payload) is not dict or name not in payload
    ]
    missing += [
        f"expected.{widget['id']}"
        for widget in manifest["widgets"]
        if type(expected) is not dict or widget["id"] not in expected
    ]
    instruction = "Edit application_acceptance.json in the file editor, save reviewed changes, then review and check the approval checkbox again."
    try:
        validate_acceptance({"payload": payload, "expected": expected}, manifest)
    except (ValueError, KeyError, TypeError):
        details = ", ".join(missing) if missing else "input/result types or unknown fields"
        return (
            False,
            "Verification blocked: complete or correct independent cases: "
            + details
            + ". "
            + instruction,
        )
    return (
        True,
        "Independent cases are structurally valid. Proposed values originate in reviewed catalog cases; manually edited values require your independent review. "
        + instruction,
    )
