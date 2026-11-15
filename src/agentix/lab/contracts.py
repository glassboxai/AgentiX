"""Strict immutable port, widget and workflow contracts for reviewed applications.

Only scalar text/count and bounded summary objects cross tool boundaries. Contract
validation runs before execution; arbitrary callables and filesystem paths are absent.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

PortType = Literal["text", "count", "summary"]
Identifier = Annotated[str, Field(pattern=r"^[a-z][a-z0-9_]{0,63}$")]
Text = Annotated[str, Field(strict=True, max_length=16000)]
Count = Annotated[int, Field(strict=True, ge=0)]


class Contract(BaseModel):
    """Forbid unknown fields and coercion; retain immutable contract identities."""

    model_config = ConfigDict(strict=True, frozen=True, extra="forbid")


class ToolDefinition(Contract):
    """Reviewed maintained function and its required/optional typed input ports."""

    id: Identifier
    function: Identifier
    inputs: dict[str, PortType]
    optional: tuple[str, ...] = ()
    output: PortType


class WidgetDefinition(Contract):
    """One widget instance; its ID namespaces controls independently of the tool."""

    id: Identifier
    tool: Identifier
    label: str

    def elem_id(self, control: str) -> str:
        """Return a stable instance/control selector without arbitrary DOM syntax."""
        if control not in ("result", "status"):
            raise ValueError("Unknown widget control")
        return f"lab_{self.id}_{control}"
