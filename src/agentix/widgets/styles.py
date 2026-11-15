"""Conservative tool-scoped CSS grammar with no external resource or global rules."""

import re

STYLE_SUFFIX = "_widget.css"

PROPERTIES = frozenset(
    {
        "color",
        "background-color",
        "font-size",
        "font-weight",
        "font-family",
        "padding",
        "margin",
        "border-color",
        "border-width",
        "border-style",
        "border-radius",
    }
)

# The field box and the caption are inner elements, so a container-only selector
# cannot reach them. Only these documented descendants may follow the scope.
DESCENDANTS = (" input", " textarea", " label", " .label-wrap", " .output")
_DESCENDANT = "(?:" + "|".join(re.escape(suffix) for suffix in DESCENDANTS) + ")?"


def default_widget_css(role: str) -> str:
    """Provide an independently editable file with the parent's default palette."""
    if not isinstance(role, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", role):
        raise ValueError("Unknown widget style scope")
    return f':where([id^="application_{role}_"]) {{ color: #f1f3f5; }}\n'


def validate_widget_css(css: str, role: str) -> str:
    """Accept bounded static declarations for only one approved widget ID prefix.

    No imports, URLs, escaped tokens, custom properties, nested rules, arbitrary
    selectors or properties affecting visibility, positioning or interaction.
    This intentionally supports a small customization surface, not arbitrary CSS.
    """
    if (
        not isinstance(role, str)
        or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", role)
        or not isinstance(css, str)
        or len(css.encode("utf-8")) > 16384
    ):
        raise ValueError("Invalid widget CSS")
    rest = css.strip()
    selector = f':where([id^="application_{role}_"])'
    while rest:
        match = re.match(re.escape(selector) + _DESCENDANT + r"(?:\s*:hover)?\s*\{([^{}]*)\}", rest)
        if not match:
            raise ValueError("Widget CSS must remain within its own scope")
        for declaration in match[1].split(";"):
            if not declaration.strip():
                continue
            name, separator, value = declaration.partition(":")
            if (
                not separator
                or name.strip() not in PROPERTIES
                or not re.fullmatch(r"[A-Za-z0-9#., %_-]{1,200}", value.strip())
            ):
                raise ValueError("Unsupported widget CSS declaration")
            property_name, property_value = name.strip(), value.strip()
            bounds = {
                "font-size": (8, 72, 1),
                "padding": (0, 64, 4),
                "margin": (0, 64, 4),
                "border-width": (0, 8, 4),
                "border-radius": (0, 64, 4),
            }
            if property_name in bounds:
                minimum, maximum, count = bounds[property_name]
                pieces = property_value.split()
                if not 1 <= len(pieces) <= count:
                    raise ValueError("Invalid widget style dimensions")
                for piece in pieces:
                    if (
                        not re.fullmatch(r"(?:0|[0-9]{1,3}(?:\.[0-9]{1,2})?px)", piece)
                        or not minimum <= float(piece.removesuffix("px")) <= maximum
                    ):
                        raise ValueError("Widget style dimensions exceed limits")

        rest = rest[match.end() :].strip()
    return css
