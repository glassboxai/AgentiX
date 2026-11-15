"""Strict presentation-only geometry; no executable strings, selectors or host paths."""

import re

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator

_LEGACY_CONTROLS = {
    "application_input",
    "application_result",
    "application_words_result",
    "application_vowels_result",
    "application_status",
}
_LEGACY_WIDGET_CONTROL = re.compile(
    r"application_(?:words|vowels)(?:_(?:[2-9]|[1-9][0-9]+))?_(?:input|output|execute)"
)


def _legacy_control(name: str) -> bool:
    """Return whether a legacy schema-2 identifier is a movable canvas control."""
    return name in _LEGACY_CONTROLS or bool(_LEGACY_WIDGET_CONTROL.fullmatch(name))


class Rectangle(BaseModel):
    """Pixel geometry bounded to the generated application's editable canvas."""

    model_config = ConfigDict(strict=True, extra="forbid")
    x: int = Field(ge=0, le=10000)
    y: int = Field(ge=0, le=10000)
    width: int = Field(ge=48, le=4096)
    height: int = Field(ge=32, le=4096)


class Layout(BaseModel):
    """Versioned data-only layout with immutable toolbar/authorization boundaries."""

    model_config = ConfigDict(strict=True, extra="forbid")
    version: int = Field(default=1, ge=1, le=1)
    positions: dict[str, Rectangle] = Field(default_factory=dict, max_length=64)
    hidden: list[str] | None = Field(default=None, max_length=64)

    @field_validator("positions")
    @classmethod
    def known_controls(
        cls, positions: dict[str, Rectangle], info: ValidationInfo
    ) -> dict[str, Rectangle]:
        """Never let layout records target the toolbar, parent UI or arbitrary selectors."""
        allowed = info.context.get("allowed") if info.context else None
        if allowed is not None:
            if not set(positions) <= allowed:
                raise ValueError("Unknown movable application control")
            return positions
        for name in positions:
            if not _legacy_control(name):
                raise ValueError("Unknown movable application control")
        return positions

    @field_validator("hidden")
    @classmethod
    def known_hidden_controls(
        cls, hidden: list[str] | None, info: ValidationInfo
    ) -> list[str] | None:
        """Keep persisted visibility on the same reviewed controls as geometry."""
        if hidden is None:
            return None
        if len(set(hidden)) != len(hidden):
            raise ValueError("Duplicate hidden application control")
        allowed = info.context.get("allowed") if info.context else None
        if allowed is not None:
            if not set(hidden) <= allowed:
                raise ValueError("Unknown hidden application control")
            return hidden
        for name in hidden:
            if not _legacy_control(name):
                raise ValueError("Unknown hidden application control")
        return hidden


def validate_layout(value: object, *, allowed: set[str] | None = None) -> dict:
    """Return normalized safe JSON data; raise ValueError without applying invalid edits."""
    return Layout.model_validate(value, context={"allowed": allowed}).model_dump(
        mode="json", exclude_none=True
    )


def application_layout_groups(manifest: dict) -> dict[str, str]:
    """Map every movable control to the tool whose widgets it belongs to.

    Public inputs and Status are their own groups so unrelated controls never
    share a color. Legacy schema-2 manifests return an empty mapping because
    their widget-to-tool relation is not recorded. The result is presentation
    data only and never widens the movable allowlist.
    """
    if manifest.get("schema_version") != 3:
        return {}
    from agentix.application.templates.code.element_ids import ElementIds

    registry = ElementIds()
    groups = {"application_status": "application_status"}
    groups.update(
        ("application_input_" + name, "application_input_" + name)
        for name in manifest.get("inputs", {})
    )
    for node in manifest["widgets"]:
        parameters = list(manifest["tools"][node["tool"]]["parameters"])
        scope = registry.new_widget(node["id"], parameters)
        for role in parameters + ["input", "output", "execute"]:
            groups[registry.control(scope, role)] = node["tool"]
    return groups


def application_layout_ids(manifest: dict) -> set[str] | None:
    """Derive reviewed canvas IDs for connection-code widgets and public inputs.

    Return None for legacy formats using the fixed compatibility allowlist.
    Schema-3 public inputs use their stable application_input_<name> IDs.
    Toolbar IDs are never included; callers share this set for editing and storage.
    """
    if manifest.get("schema_version") != 3:
        return None
    from agentix.application.templates.code.element_ids import ElementIds

    registry = ElementIds()
    allowed = {"application_status"}
    allowed.update("application_input_" + name for name in manifest.get("inputs", {}))
    for node in manifest["widgets"]:
        parameters = list(manifest["tools"][node["tool"]]["parameters"])
        scope = registry.new_widget(node["id"], parameters)
        roles = parameters + ["input", "output", "execute"]
        allowed.update(registry.control(scope, role) for role in roles)
    return allowed
