"""Strict data-only tool routing and acceptance proposal contracts."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

# Readable tool-name identifiers and the bounded routing purpose text.
IDENTIFIER_PATTERN = r"^[a-z][a-z0-9_]{0,63}$"
MAX_PURPOSE_LENGTH = 2000
# Mirrors agentix.domain.tool_schema.MAX_TOOL_PARAMETERS without importing that module.
MAX_ARGUMENTS = 12

# Concrete argument grammar for provider-enforced structured output. Strict providers
# reject an empty schema, recursive $ref cycles and open key maps, so the JSON value
# vocabulary of tool contracts is bounded to scalars and two nested list levels.
JsonScalar = str | int | float | bool
JsonArgument = JsonScalar | list[JsonScalar] | list[list[JsonScalar]]


class ArgumentPair(BaseModel):
    """One named tool argument as a closed object instead of an open key map."""

    model_config = ConfigDict(extra="forbid", strict=True)
    name: str = Field(pattern=IDENTIFIER_PATTERN)
    value: JsonArgument


class ToolRoute(BaseModel):
    """A selection is data, never authority to call or approve the selected tool."""

    model_config = ConfigDict(extra="forbid", strict=True)
    action: Literal["CREATE_TOOL", "REUSE_TOOL"]
    tool_name: str = Field(pattern=IDENTIFIER_PATTERN)
    purpose: str = Field(min_length=1, max_length=MAX_PURPOSE_LENGTH)
    arguments: list[ArgumentPair] = Field(default_factory=list, max_length=MAX_ARGUMENTS)


class CreateRoute(BaseModel):
    """Creation proposes a capability, never arguments or executable API metadata."""

    model_config = ConfigDict(extra="forbid", strict=True)
    action: Literal["CREATE_TOOL"]
    tool_name: str = Field(pattern=IDENTIFIER_PATTERN)
    purpose: str = Field(min_length=1, max_length=MAX_PURPOSE_LENGTH)


class ReuseRoute(ToolRoute):
    """Reuse arguments are checked against the exact selected tool schema."""

    action: Literal["REUSE_TOOL"]
