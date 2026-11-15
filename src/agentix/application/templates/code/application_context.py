"""Native widget context with readable application-wide unique control identities."""

import re

from element_ids import ElementIds


class Context:
    """Allocate semantic controls once; repeated requests for a role are stable."""

    def __init__(self, instance: str, ids: ElementIds, parameters: list[str]) -> None:
        """Bind a validated widget instance and its exact named parameter vocabulary."""
        self.ids = ids
        self.scope = ids.new_widget(instance, parameters)
        self.api_name = ids.api_name(self.scope)
        self.allowed = set(parameters) | {"input", "output", "execute", "group"}
        self.controls = {}

    def elem_id(self, role: str) -> str | None:
        """Return unique semantic IDs; Group IDs are omitted for Gradio compatibility."""
        if role not in self.allowed or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", role):
            raise ValueError("Unknown widget control")
        if role == "group":
            return None
        self.controls.setdefault(role, self.ids.control(self.scope, role))
        return self.controls[role]
