"""Declarative typed read-only Gradio outputs, independent of model code or HTML."""

import math
import re
from dataclasses import dataclass
from typing import Any, Literal

MAX_SAFE_INTEGER = 2**53  # Largest integer a JSON consumer represents exactly.
MAX_TEXT_LENGTH = 16384  # Characters accepted in one text cell or value.
MAX_TABLE_ROWS = 1000  # Rows accepted in one table value.
MAX_TABLE_COLUMNS = 32  # Columns accepted in one table value.
MAX_HEADER_LENGTH = 100  # Characters accepted in one table header.
MAX_LABEL_LENGTH = 100  # Characters accepted in one field label.


@dataclass(frozen=True)
class ResultField:
    """A known output key, readable label and presentation type."""

    key: str
    label: str
    kind: Literal["text", "number", "boolean", "table"]

    def __post_init__(self) -> None:
        """Reject arbitrary selectors, unbounded labels and unsupported presentation types."""
        if (
            not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", self.key)
            or not 1 <= len(self.label) <= MAX_LABEL_LENGTH
            or self.kind not in ("text", "number", "boolean", "table")
        ):
            raise ValueError("Invalid result field contract")


def build_results(gr: Any, fields: list[ResultField], prefix: str) -> list[Any]:
    """Build explicit read-only controls, never a generic JSON output block."""
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", prefix):
        raise ValueError("Invalid result namespace")
    factories = {
        "text": gr.Textbox,
        "number": gr.Number,
        "boolean": gr.Checkbox,
        "table": gr.Dataframe,
    }
    return [
        factories[field.kind](
            label=field.label, interactive=False, elem_id=prefix + "-" + field.key
        )
        for field in fields
    ]


def _table_cell(value: Any) -> bool:
    """Bound table text/numbers and reject objects or nonfinite float values."""
    if value is None or type(value) is bool:
        return True
    if type(value) is str:
        return len(value) <= MAX_TEXT_LENGTH
    return type(value) in (int, float) and math.isfinite(value) and abs(value) <= MAX_SAFE_INTEGER


def result_values(value: dict | None, fields: list[ResultField]) -> list[Any]:
    """Validate data against presentation contracts; None clears stale results."""
    if value is None:
        return [False if field.kind == "boolean" else None for field in fields]
    if not isinstance(value, dict) or set(value) != {field.key for field in fields}:
        raise ValueError("Result does not match its output fields")
    output = []
    for field in fields:
        item = value[field.key]
        if field.kind == "text":
            valid = isinstance(item, str) and len(item) <= MAX_TEXT_LENGTH
        elif field.kind == "number":
            valid = (
                type(item) in (int, float) and math.isfinite(item) and abs(item) <= MAX_SAFE_INTEGER
            )
        elif field.kind == "boolean":
            valid = type(item) is bool
        else:
            valid = isinstance(item, list) and len(item) <= MAX_TABLE_ROWS
            if valid and item:
                headers = list(item[0]) if isinstance(item[0], dict) else None
                valid = (
                    headers is not None
                    and len(headers) <= MAX_TABLE_COLUMNS
                    and all(
                        isinstance(key, str) and len(key) <= MAX_HEADER_LENGTH for key in headers
                    )
                    and all(
                        isinstance(row, dict)
                        and set(row) == set(headers)
                        and all(_table_cell(cell) for cell in row.values())
                        for row in item
                    )
                )
                if valid:
                    item = {
                        "headers": headers,
                        "data": [[row[key] for key in headers] for row in item],
                    }
            elif valid:
                item = {"headers": [], "data": []}
        if not valid:
            raise ValueError("Result field has an invalid presentation type")
        output.append(item)
    return output
