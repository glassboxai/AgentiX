"""Read and rewrite the six owner-editable declarations of one widget stylesheet.

The window edits a closed set of declarations inside the single scoped block that
``agentix.widgets.styles`` already accepts. Every other declaration and every
``:hover`` block is preserved byte-for-byte in meaning, and the merged result is
validated again before it can reach disk.
"""

import re
from dataclasses import dataclass

from agentix.widgets.styles import validate_widget_css

FONTS = (
    "system-ui",
    "Segoe UI",
    "Arial",
    "Verdana",
    "Tahoma",
    "Georgia",
    "Times New Roman",
    "Courier New",
)

MANAGED = (
    "border-radius",
    "border-width",
    "border-style",
    "border-color",
    "background-color",
    "font-family",
    "font-size",
)

# The field box and the caption own their own declarations; they are rewritten in
# their own blocks so the container values stay independent.
FIELD_MANAGED = ("background-color",)
LABEL_MANAGED = ("font-family", "font-size")

DEFAULT_BORDER = "#5bd9ef"
DEFAULT_BACKGROUND = "#10141c"
DEFAULT_SIZE = 16
MAX_RADIUS = 64
MAX_WIDTH = 8

HEX = re.compile(r"#[0-9a-fA-F]{6}")
PIXELS = re.compile(r"([0-9]{1,3}(?:\.[0-9]{1,2})?)px")
BLOCK = re.compile(
    r':where\(\[id\^="application_(?P<role>[a-z][a-z0-9_]{0,63})_"\]\)'
    r"(?P<suffix> input| textarea| label| \.label-wrap| \.output)?"
    r"(?P<hover>\s*:hover)?\s*\{(?P<body>[^{}]*)\}"
)

FIELD_SUFFIXES = (" input", " textarea")
LABEL_SUFFIXES = (" label", " .label-wrap")


@dataclass(frozen=True)
class StyleValues:
    """The nine values the window owns, already normalised to their stored form."""

    radius: int
    width: int
    border_color: str
    background: str
    font_family: str
    font_size: int
    field_background: str = DEFAULT_BACKGROUND
    label_font_family: str = FONTS[0]
    label_font_size: int = DEFAULT_SIZE


def _pixels(value: str, default: int) -> int:
    """Read one bounded pixel length, falling back to the palette default."""
    match = PIXELS.fullmatch(value.strip())
    return int(round(float(match[1]))) if match else default


def _color(value: str, default: str) -> str:
    """Accept only a full hexadecimal colour so the grammar stays satisfied."""
    return value.strip().lower() if HEX.fullmatch(value.strip()) else default


def read_style(css: str, role: str) -> StyleValues:
    """Return the managed values of the base, field and caption blocks.

    A missing declaration, an unparsable length or an unsupported family yields the
    documented default instead of an error: the window must open on any valid file.
    """
    declarations: dict[str, str] = {}
    field: dict[str, str] = {}
    label: dict[str, str] = {}
    for match in BLOCK.finditer(css):
        if match["role"] != role or match["hover"]:
            continue
        suffix = match["suffix"] or ""
        target = declarations
        if suffix in FIELD_SUFFIXES:
            target = field
        elif suffix in LABEL_SUFFIXES:
            target = label
        for declaration in match["body"].split(";"):
            name, separator, value = declaration.partition(":")
            if separator:
                target[name.strip()] = value.strip()
    family = declarations.get("font-family", FONTS[0]).strip("'\" ")
    label_family = label.get("font-family", family).strip("'\" ")
    return StyleValues(
        radius=_pixels(declarations.get("border-radius", "0px"), 0),
        width=_pixels(declarations.get("border-width", "0px"), 0),
        border_color=_color(declarations.get("border-color", DEFAULT_BORDER), DEFAULT_BORDER),
        background=_color(
            declarations.get("background-color", DEFAULT_BACKGROUND), DEFAULT_BACKGROUND
        ),
        font_family=family if family in FONTS else FONTS[0],
        font_size=_pixels(declarations.get("font-size", f"{DEFAULT_SIZE}px"), DEFAULT_SIZE),
        field_background=_color(
            field.get("background-color", DEFAULT_BACKGROUND), DEFAULT_BACKGROUND
        ),
        label_font_family=label_family if label_family in FONTS else FONTS[0],
        label_font_size=_pixels(label.get("font-size", f"{DEFAULT_SIZE}px"), DEFAULT_SIZE),
    )


def checked(values: StyleValues) -> StyleValues:
    """Reject out-of-range input before it can reach the stylesheet grammar."""
    if type(values.radius) is not int or not 0 <= values.radius <= MAX_RADIUS:
        raise ValueError("Border radius must be a whole number between 0 and 64")
    if type(values.width) is not int or not 0 <= values.width <= MAX_WIDTH:
        raise ValueError("Border width must be a whole number between 0 and 8")
    if not HEX.fullmatch(values.border_color or ""):
        raise ValueError("Border color must be a hexadecimal colour")
    if not HEX.fullmatch(values.background or ""):
        raise ValueError("Background color must be a hexadecimal colour")
    if values.font_family not in FONTS:
        raise ValueError("Select one of the available fonts")
    if type(values.font_size) is not int or not 8 <= values.font_size <= 72:
        raise ValueError("Font size must be a whole number between 8 and 72")
    if not HEX.fullmatch(values.field_background or ""):
        raise ValueError("Field color must be a hexadecimal colour")
    if values.label_font_family not in FONTS:
        raise ValueError("Select one of the available caption fonts")
    if type(values.label_font_size) is not int or not 8 <= values.label_font_size <= 72:
        raise ValueError("Caption font size must be a whole number between 8 and 72")
    return StyleValues(
        values.radius,
        values.width,
        values.border_color.lower(),
        values.background.lower(),
        values.font_family,
        values.font_size,
        values.field_background.lower(),
        values.label_font_family,
        values.label_font_size,
    )


def merge_style(css: str, role: str, values: StyleValues) -> str:
    """Rewrite only the managed declarations, preserving every other block.

    The base block keeps its unmanaged declarations in their original order and the
    managed ones are appended in a fixed order. ``border-style`` is derived so a
    non-zero width is always visible and a zero width never draws a border. The field
    and caption blocks are rewritten the same way, so a padding or a colour that the
    window does not own survives.
    """
    validate_widget_css(css, role)
    values = checked(values)
    selector = f':where([id^="application_{role}_"])'
    managed = {
        "border-radius": f"{values.radius}px",
        "border-width": f"{values.width}px",
        "border-style": "solid" if values.width else "none",
        "border-color": values.border_color,
        "background-color": values.background,
        "font-family": values.font_family,
        "font-size": f"{values.font_size}px",
    }
    field = {"background-color": values.field_background}
    label = {
        "font-family": values.label_font_family,
        "font-size": f"{values.label_font_size}px",
    }
    blocks = list(BLOCK.finditer(css))

    def first(suffixes: tuple[str, ...]) -> re.Match | None:
        """Return the first non-hover block of this role for the given suffixes."""
        return next(
            (
                match
                for match in blocks
                if match["role"] == role
                and not match["hover"]
                and (match["suffix"] or "") in suffixes
            ),
            None,
        )

    def rewrite(match: re.Match | None, owned: dict[str, str]) -> str:
        """Keep unmanaged declarations of one block, then append the owned ones."""
        kept: list[str] = []
        if match is not None:
            for declaration in match["body"].split(";"):
                name, separator, _ = declaration.partition(":")
                if separator and name.strip() not in owned:
                    kept.append(declaration.strip())
        return "; ".join([*kept, *(f"{name}: {value}" for name, value in owned.items())])

    base_match = first(("",))
    rendered = rewrite(base_match, managed)
    field_input = first((" input",))
    field_textarea = first((" textarea",))
    label_match = first(LABEL_SUFFIXES)
    # Every block this writer owns is replaced, so repeated saves never accumulate
    # duplicate declarations that would later win by source order.
    owned_blocks = {
        id(match)
        for match in blocks
        if match["role"] == role
        and not match["hover"]
        and (match["suffix"] or "") in ("", *FIELD_SUFFIXES, *LABEL_SUFFIXES)
    }
    tail = [css[match.start() : match.end()] for match in blocks if id(match) not in owned_blocks]
    merged = (
        "\n".join(
            [
                f"{selector} {{ {rendered} }}",
                f"{selector} input {{ {rewrite(field_input, field)} }}",
                f"{selector} textarea {{ {rewrite(field_textarea, field)} }}",
                f"{selector} label {{ {rewrite(label_match, label)} }}",
                *tail,
            ]
        )
        + "\n"
    )
    return validate_widget_css(merged, role)
