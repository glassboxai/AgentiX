"""Maintained presentation for generated applications; no executable child HTML."""

import html
import json

from agentix.lab.widget_panel import iframe_html

MAX_DESCRIPTION_LENGTH = 120  # Characters kept from one model-authored input description.
MAX_RESULT_ROWS = 32  # Named results shown for one bounded application execution.
MAX_RESULT_CELL_LENGTH = 200  # Characters kept from one rendered result value.
SAFE_DESCRIPTION = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,;:!?-'\"()/"
)
JSON_TYPE_NAMES = {
    "string": "string",
    "integer": "integer",
    "number": "number",
    "boolean": "boolean",
    "array": "array",
}
RESULT_TYPE_NAMES = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}


def _safe_description(shape: dict) -> str:
    """Keep a bounded single-line description; drop markup characters from model text."""
    text = shape.get("description")
    if not isinstance(text, str):
        return ""
    kept = "".join(
        character for character in " ".join(text.split()) if character in SAFE_DESCRIPTION
    )
    return kept[:MAX_DESCRIPTION_LENGTH]


def _example_value(shape: dict) -> object:
    """Derive one JSON example from the declared closed shape, never from child code."""
    enum = shape.get("enum")
    if isinstance(enum, list) and enum:
        return enum[0]
    kind = shape.get("type")
    if kind == "string":
        return "Hello World!"
    if kind == "integer":
        return 1
    if kind == "number":
        return 1.5
    if kind == "boolean":
        return True
    if kind == "array":
        items = shape.get("items")
        return [_example_value(items)] if isinstance(items, dict) else []
    return None


def describe_data_inputs(manifest: dict) -> str:
    """Render the reviewed input contract and one example payload as Markdown.

    Only the closed ``inputs`` mapping is read; no child module is imported and no
    value is executed. Keys are validated identifiers and descriptions are bounded
    to inert text, so the result is safe for a Gradio Markdown output.
    """
    inputs = manifest.get("inputs")
    if type(inputs) is not dict or not inputs:
        return "This application declares no data-operation inputs."
    lines = [
        "**Data operation inputs** — send one JSON object with exactly these keys:",
        "",
        "| Key | Type | Description |",
        "| --- | --- | --- |",
    ]
    for name, shape in inputs.items():
        kind = JSON_TYPE_NAMES.get(shape.get("type"), "unsupported")
        lines.append(f"| `{name}` | {kind} | {_safe_description(shape)} |")
    example = json.dumps(
        {name: _example_value(shape) for name, shape in inputs.items()}, ensure_ascii=False
    )
    lines.extend(["", f"Example payload: `{example}`"])
    return "\n".join(lines)


def named_result_rows(value: dict) -> dict:
    """Render observed named results as bounded table cells for one execution.

    The mapping is host-observed output from the isolated worker; every cell is
    converted to bounded text so no object, NaN or oversized body reaches the UI.
    """
    rows = []
    for name, item in list(value.items())[:MAX_RESULT_ROWS]:
        rendered = json.dumps(item, ensure_ascii=False, default=str)
        rows.append(
            [
                str(name),
                RESULT_TYPE_NAMES.get(type(item), "object"),
                rendered[:MAX_RESULT_CELL_LENGTH],
            ]
        )
    return {"headers": ["Result", "Type", "Value"], "data": rows}


def generated_application_frame(url: str, name: str = "") -> str:
    """Frame only the validated supervisor URL, without a reactive Gradio Group ID.

    The heading keeps the maintained cyan label and offers the same already
    validated loopback origin as a separate browser tab. The optional application
    name only labels that section and link; the isolated page titles itself from
    its own staged snapshot, never from a query parameter.
    """
    label = html.escape(name, quote=True) if name else "Generated Application"
    return (
        f'<section id="generated-application" aria-label="{label}">'
        '<div id="generated-application-heading-row">'
        '<h3 id="generated-application-heading">Generated Application</h3>'
        f'<a id="generated-application-web" href="{html.escape(url, quote=True)}"'
        f' title="Open {label} in a new tab"'
        ' target="_blank" rel="noopener noreferrer">View as web</a>'
        "</div>" + iframe_html(url) + "</section>"
    )
