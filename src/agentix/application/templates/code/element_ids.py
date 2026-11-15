"""Thread-safe readable widget IDs; structural Gradio Groups deliberately get no ID."""

import re
import threading


class ElementIds:
    """Own one application's allocated widget scopes and stable control selectors."""

    def __init__(self) -> None:
        """Create an empty registry; reuse this instance across the application's widgets."""
        self._lock = threading.RLock()
        self._scopes: set[str] = set()
        self._used: set[str] = set()
        self._controls: dict[tuple[str, str], str] = {}
        self._roles: dict[str, set[str]] = {}

    def new_widget(self, tool: str, parameters: list[str] | None = None) -> str:
        """Allocate a semantic instance scope; reject ambiguous or unsafe names."""
        if not isinstance(tool, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", tool):
            raise ValueError("Invalid widget tool identity")
        roles = {"input", "output", "execute", "group"} | set(parameters or [])
        if any(
            not isinstance(role, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", role)
            for role in roles
        ):
            raise ValueError("Invalid widget parameter identity")
        with self._lock:
            number = 1
            while True:
                scope = "application_" + tool + ("" if number == 1 else "_" + str(number))
                names = {scope + "_" + role for role in ("input", "output", "execute")}
                if scope not in self._scopes and not names.intersection(self._used):
                    self._scopes.add(scope)
                    self._roles[scope] = roles
                    self._used.update(names)
                    for role in ("input", "output", "execute"):
                        self._controls[(scope, role)] = scope + "_" + role
                    return scope
                number += 1

    def control(self, scope: str, role: str) -> str | None:
        """Return a stable allocated selector; Group duplication cannot be fixed by naming."""
        with self._lock:
            if scope not in self._scopes or role not in self._roles[scope]:
                raise ValueError("Unknown widget scope or control role")
            if role == "group":
                return None
            key = (scope, role)
            if key not in self._controls:
                candidate, suffix = scope + "_" + role, 2
                while candidate in self._used:
                    candidate = scope + "_" + role + "_" + str(suffix)
                    suffix += 1
                self._used.add(candidate)
                self._controls[key] = candidate
            return self._controls[key]

    def api_name(self, scope: str) -> str:
        """Return the unique readable event namespace paired with an allocated scope."""
        with self._lock:
            if scope not in self._scopes:
                raise ValueError("Unknown widget scope")
            return "count_" + scope.removeprefix("application_")
