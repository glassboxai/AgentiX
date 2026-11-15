"""Bounded generated connection-code contracts; host validation never executes source."""

import ast
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from agentix.agents.application_agents import validate_source
from agentix.domain.tool_schema import validate_value

IDENTIFIER = r"^[a-z][a-z0-9_]{0,63}$"
# Bounded inventory and source limits enforced by the pydantic contract.
MAX_APPLICATION_INPUTS = 16
MAX_APPLICATION_WIDGETS = 16
MAX_CONNECTION_CODE_LENGTH = 65536
MAX_NOTES_LENGTH = 8192
# Input-shape limits applied by validate_input_shape.
MAX_INPUT_DESCRIPTION_LENGTH = 1024
MAX_ENUM_VALUES = 32
# Fixed connection-module entry contract checked by validate_connection_source.
ENTRY_FUNCTION_NAME = "run"
ENTRY_ARGUMENTS = ("payload", "call")
# Closed public input keys; numeric bounds belong to the approved tool contract.
INPUT_SHAPE_KEYS = ("type", "description", "enum", "items")


class ApplicationContractError(ValueError):
    """Name a rejected public-input key without carrying model or user payload.

    The message is built only from the input identity and the closed key list, so
    it is safe for the owner-facing status line and the payload-free event log.
    """


def unsupported_input_keys(shape: object) -> list[str]:
    """Return the sorted keys a public input schema may not declare."""
    if type(shape) is not dict:
        return []
    return sorted(str(key) for key in set(shape) - set(INPUT_SHAPE_KEYS))


class WidgetInstance(BaseModel):
    """Describe a presentation instance and its approved tool, without connectivity."""

    model_config = ConfigDict(extra="forbid")
    id: str = Field(pattern=IDENTIFIER)
    tool: str = Field(pattern=IDENTIFIER)


class ApplicationCode(BaseModel):
    """Hold generated Python, public input schemas and the finite widget inventory."""

    model_config = ConfigDict(extra="forbid")
    inputs: dict[str, dict[str, Any]] = Field(min_length=1, max_length=MAX_APPLICATION_INPUTS)
    widgets: list[WidgetInstance] = Field(min_length=1, max_length=MAX_APPLICATION_WIDGETS)
    connection_code: str = Field(min_length=1, max_length=MAX_CONNECTION_CODE_LENGTH)
    notes: str = Field(max_length=MAX_NOTES_LENGTH)

    def validate_catalog(self, schemas: dict) -> dict:
        """Reject unknown dependencies, invalid input shapes and unsafe source structure.

        This is a syntax/contract filter, not isolation or a semantic proof. The
        returned source stays inert until exact-byte review and native execution.
        """
        import re

        if len({widget.id for widget in self.widgets}) != len(self.widgets) or any(
            widget.tool not in schemas or widget.id == "input" for widget in self.widgets
        ):
            raise ValueError("Unknown tool or duplicate/reserved widget identity")
        for name, shape in self.inputs.items():
            if not re.fullmatch(IDENTIFIER, name):
                raise ValueError("Invalid application input identity")
            try:
                validate_input_shape(shape)
            except ApplicationContractError as error:
                raise ApplicationContractError(f"Application input '{name}': {error}") from None
        validate_connection_source(self.connection_code)
        return self.model_dump(mode="json")


def validate_input_shape(shape: dict) -> None:
    """Accept only scalar/array JSON shapes supported by strict tool validation."""
    if type(shape) is not dict:
        raise ApplicationContractError("Unsupported application input schema")
    rejected = unsupported_input_keys(shape)
    if rejected:
        raise ApplicationContractError(
            "unsupported keys "
            + ", ".join(rejected)
            + ". Allowed: "
            + ", ".join(INPUT_SHAPE_KEYS)
            + "."
        )
    if shape.get("type") not in {"string", "integer", "number", "boolean", "array"}:
        raise ValueError("Unsupported application input type")
    if "description" in shape and (
        type(shape["description"]) is not str
        or len(shape["description"]) > MAX_INPUT_DESCRIPTION_LENGTH
    ):
        raise ValueError("Invalid input description")
    if shape["type"] == "array":
        if set(shape.get("items", {})) - {"type", "description", "enum"}:
            raise ValueError("Nested application arrays are unsupported")
        validate_input_shape(shape.get("items", {}))
    elif "items" in shape:
        raise ValueError("Only arrays accept item schemas")
    if "enum" in shape:
        if type(shape["enum"]) is not list or not 1 <= len(shape["enum"]) <= MAX_ENUM_VALUES:
            raise ValueError("Invalid input enum")
        for value in shape["enum"]:
            validate_value(value, {key: item for key, item in shape.items() if key != "enum"})


def validate_connection_source(source: str) -> None:
    """Compile but never import bounded source; reject module-level work and entry drift."""
    validate_source(source, {"typing"}, ENTRY_FUNCTION_NAME)
    tree = ast.parse(source)
    for statement in tree.body:
        if isinstance(statement, (ast.Import, ast.ImportFrom)):
            continue
        if (
            isinstance(statement, ast.Expr)
            and isinstance(statement.value, ast.Constant)
            and isinstance(statement.value.value, str)
        ):
            continue
        if (
            not isinstance(statement, ast.FunctionDef)
            or statement.decorator_list
            or statement.args.defaults
            or statement.args.kw_defaults
        ):
            raise ValueError(
                "Connection modules may contain only documented functions and typing imports"
            )
    entry = next(
        statement
        for statement in tree.body
        if isinstance(statement, ast.FunctionDef) and statement.name == ENTRY_FUNCTION_NAME
    )
    if (
        [argument.arg for argument in entry.args.args] != list(ENTRY_ARGUMENTS)
        or entry.args.vararg
        or entry.args.kwarg
        or entry.args.kwonlyargs
        or entry.args.posonlyargs
    ):
        raise ValueError("Connection entry must be run(payload, call)")
