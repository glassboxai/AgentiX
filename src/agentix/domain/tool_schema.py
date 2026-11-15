"""Static canonical tool contracts; source and annotation expressions never execute."""

import ast
import re
from typing import Any

# Tool identity, source and annotation bounds enforced by the static contract.
TOOL_NAME_PATTERN = r"[a-z][a-z0-9_]{0,63}"
MAX_TOOL_SOURCE_BYTES = 65536
MAX_PARAMETER_DESCRIPTION_LENGTH = 500
MAX_TOOL_PARAMETERS = 12
MAX_TOOL_MEANING_LENGTH = 2000
MAX_TEXT_VALUE_LENGTH = 16000


def _shape(node: ast.expr) -> dict:
    """Translate the bounded JSON annotation vocabulary, rejecting unknown Python."""
    if isinstance(node, ast.Name) and node.id in {"str", "int", "float", "bool"}:
        return {
            "type": {"str": "string", "int": "integer", "float": "number", "bool": "boolean"}[
                node.id
            ]
        }
    if (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id in {"list", "List"}
    ):
        return {"type": "array", "items": _shape(node.slice)}
    if (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "Literal"
    ):
        values = node.slice.elts if isinstance(node.slice, ast.Tuple) else [node.slice]
        literals = [ast.literal_eval(value) for value in values]
        if not literals or any(type(value) not in {str, int, bool} for value in literals):
            raise ValueError("Unsupported Literal annotation")
        if any(type(value) is not type(literals[0]) for value in literals):
            raise ValueError("Literal alternatives must have one strict JSON type")
        return {
            "type": {str: "string", int: "integer", bool: "boolean"}[type(literals[0])],
            "enum": literals,
        }
    raise ValueError("Use a supported JSON type in Annotated")


def _annotated(node: ast.expr | None) -> dict:
    """Require Annotated with a nonempty English description string or Field metadata."""
    if not isinstance(node, ast.Subscript) or not isinstance(node.value, (ast.Name, ast.Attribute)):
        raise ValueError("Public parameters and return require typing.Annotated")
    name = node.value.id if isinstance(node.value, ast.Name) else node.value.attr
    if name != "Annotated" or not isinstance(node.slice, ast.Tuple) or len(node.slice.elts) < 2:
        raise ValueError("Public parameters and return require typing.Annotated")
    description = None
    for meta in node.slice.elts[1:]:
        if isinstance(meta, ast.Constant) and isinstance(meta.value, str):
            description = meta.value
        elif (
            isinstance(meta, ast.Call)
            and isinstance(meta.func, ast.Name)
            and meta.func.id == "Field"
        ):
            for kw in meta.keywords:
                if kw.arg == "description" and isinstance(kw.value, ast.Constant):
                    description = kw.value.value
    if (
        not isinstance(description, str)
        or not description.strip()
        or len(description) > MAX_PARAMETER_DESCRIPTION_LENGTH
    ):
        raise ValueError("Annotated requires a meaningful description")
    return dict(_shape(node.slice.elts[0]), description=description.strip())


def extract_tool_schema(name: str, source: str) -> dict:
    """Return a canonical JSON contract; raise ValueError for unsupported/ambiguous APIs.

    Exactly one public top-level function is allowed, named after its package.
    Private helpers are permitted. Defaults must be JSON literals; varargs,
    positional-only parameters and async entrypoints are deliberately unsupported.
    """
    if not isinstance(name, str) or not re.fullmatch(TOOL_NAME_PATTERN, name):
        raise ValueError("Tool name must be a lowercase Python identifier")
    if not isinstance(source, str) or len(source.encode()) > MAX_TOOL_SOURCE_BYTES:
        raise ValueError("Tool source exceeds limit")
    tree = ast.parse(source)
    if not ast.get_docstring(tree):
        raise ValueError(
            "Tool module requires an English docstring as the very first statement, "
            "before any import"
        )
    public = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]
    if len(public) != 1 or public[0].name != name or isinstance(public[0], ast.AsyncFunctionDef):
        raise ValueError("The single public function must have exactly the tool name")
    fn = public[0]
    if fn.args.posonlyargs or fn.args.vararg or fn.args.kwarg or fn.decorator_list:
        raise ValueError("Unsupported public tool calling convention")
    params = {arg.arg: _annotated(arg.annotation) for arg in fn.args.args + fn.args.kwonlyargs}
    if not 1 <= len(params) <= MAX_TOOL_PARAMETERS:
        raise ValueError("Tool requires one to twelve named parameters")
    defaults = {}
    pairs = (
        list(zip(fn.args.args[len(fn.args.args) - len(fn.args.defaults) :], fn.args.defaults))
        if fn.args.defaults
        else []
    )
    pairs += [
        (arg, value)
        for arg, value in zip(fn.args.kwonlyargs, fn.args.kw_defaults)
        if value is not None
    ]
    for arg, value in pairs:
        literal = ast.literal_eval(value)
        validate_value(literal, params[arg.arg])
        defaults[arg.arg] = literal
    description = ast.get_docstring(fn) or ""
    if not description.strip():
        raise ValueError("Tool function requires an English docstring as its first statement")
    return {
        "module": name + "_code",
        "function": name,
        "meaning": description[:MAX_TOOL_MEANING_LENGTH],
        "parameters": params,
        "defaults": defaults,
        "returns": _annotated(fn.returns),
    }


def validate_value(value: Any, shape: dict) -> Any:
    """Check bounded JSON values without coercing booleans to numeric values."""
    from agentix.security.acceptance import validate_json

    if type(value) is str:
        if len(value) > MAX_TEXT_VALUE_LENGTH:
            raise ValueError("Text exceeds the tool input limit")
    else:
        validate_json(value)
    kind = shape["type"]
    valid = {
        "string": type(value) is str,
        "integer": type(value) is int,
        "number": type(value) in {int, float},
        "boolean": type(value) is bool,
        "array": type(value) is list,
    }.get(kind, False)
    if not valid or ("enum" in shape and value not in shape["enum"]):
        raise ValueError("Value does not match the reviewed tool contract")
    if kind == "array":
        for item in value:
            validate_value(item, shape["items"])
    return value
