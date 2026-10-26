"""Bounded, escaped UI renderers for observations, catalogs and review evidence.

These helpers perform no execution or authorization. Literal result decoding is
data-only, bounded before parsing, and never substitutes model prose for evidence.
Unknown output remains readable text with the exact record in a disclosure.
"""

import ast
import html
import json
import re
from typing import Any


def _text(value: Any) -> str:
    """Escape bounded display text, including Markdown control punctuation."""
    text = str(value)
    shortened = text[:16384] + (" [Display truncated]" if len(text) > 16384 else "")
    return html.escape(shortened).replace("`", "&#96;")


def _label(value: str) -> str:
    """Turn machine field names into readable headings without adding meaning."""
    return _text(value.replace("_", " ").capitalize())


def _disclosure(title: str, body: str) -> str:
    """Render one initially collapsed native, keyboard-operable disclosure."""
    return f"<details><summary>{_text(title)}</summary>{body}</details>"


def _value(value: Any, key: str = "", currency: str = "") -> str:
    """Format explicit monetary fields only when the query identifies currency."""
    if (
        type(value) in (int, float)
        and currency
        and key
        in {
            "total_cost",
            "cost",
            "rate",
            "total_cost_euros",
            "cost_euros",
            "rate_euros_per_kwh",
        }
    ):
        # Preserve finer-grained observations and avoid overflowing large integers.
        if abs(value) < 10**18 and value == round(value, 2):
            return f"{currency}{value:,.2f}"
        return currency + _text(value)
    return _text(value)


def _data(value: Any, currency: str = "", depth: int = 0) -> str:
    """Render a bounded structured result; preserve overflow in raw evidence."""
    if depth > 4:
        return "<p>Additional nested data is available in execution details.</p>"
    if isinstance(value, dict):
        parts = []
        for key, item in list(value.items())[:40]:
            if isinstance(item, (list, dict)):
                parts.append(f"<h3>{_label(str(key))}</h3>" + _data(item, currency, depth + 1))
            else:
                parts.append(
                    f"<p><strong>{_label(str(key))}</strong>: {_value(item, str(key), currency)}</p>"
                )
        return "".join(parts)
    if isinstance(value, list) and value and all(isinstance(row, dict) for row in value):
        keys = list(dict.fromkeys(key for row in value[:50] for key in row))[:12]
        header = "".join(f"<th>{_label(str(key))}</th>" for key in keys)
        rows = "".join(
            "<tr>"
            + "".join(f"<td>{_value(row.get(key, ''), str(key), currency)}</td>" for key in keys)
            + "</tr>"
            for row in value[:50]
        )
        return f'<div class="result-table"><table><thead><tr>{header}</tr></thead><tbody>{rows}</tbody></table></div>'
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{_text(item)}</li>" for item in value[:50]) + "</ul>"
    return f"<p>{_value(value)}</p>"


def format_result(response: str, query: str = "") -> str:
    """Display an existing host record without executing or certifying its payload.

    Ordinary chat/error responses are escaped too. The recognized prefix is a
    presentation convention, not a security capability; authorization stays in
    the ledger. Original record text remains available, including undecodable data.
    """
    if not response.startswith("Host-observed execution:"):
        return f"<p>{_text(response)}</p>"
    raw = _disclosure("Execution details", f"<pre>{_text(response)}</pre>")
    match = re.search(r"^Result: (.*)$", response, re.MULTILINE)
    if match is None or len(match[1]) > 32768:
        return "<h3>Result</h3><p>Open execution details to view the output.</p>" + raw
    try:
        tree = ast.parse(match[1], mode="eval")
        if sum(1 for _ in ast.walk(tree)) > 2048:
            raise ValueError("Display structure exceeds limit")
        value = ast.literal_eval(tree)
    except (ValueError, SyntaxError, RecursionError, MemoryError):
        return f"<h3>Result</h3><p>{_text(match[1])}</p>" + raw
    currency = "€" if "€" in query or re.search(r"\b(euros?|EUR)\b", query, re.I) else ""
    return '<div class="execution-result"><h3>Result</h3>' + _data(value, currency) + raw + "</div>"


def format_catalog(markdown: str) -> str:
    """Fold UI function details while leaving the agent/CLI catalog unchanged."""
    entries = re.split(r"(?m)^- Tool Name: `", markdown)
    if len(entries) == 1:
        return f"<p>{_text(markdown)}</p>"
    rendered = []
    for entry in entries[1:]:
        name, separator, details = entry.partition("`")
        if separator:
            rendered.append(_disclosure(name, f"<pre>{_text(details.strip())}</pre>"))
    return '<div class="catalog-list">' + "".join(rendered) + "</div>"


def render_validation(status: dict[str, Any]) -> str:
    """Summarize owner-scoped verdicts; expand expected/observed evidence on demand."""
    labels = {
        "not_started": "No validation started",
        "provisional_passed": "Automatically checked — provisional",
        "provisional_failed": "Automatic checks failed",
        "pending_review": "Awaiting human acceptance review",
        "evaluating": "Human approved — evaluating cases",
        "verified": "Verified against approved cases",
        "failed": "Acceptance failed",
        "rejected": "Human review rejected, expired or cancelled",
        "invalidated": "Previous acceptance invalidated by changes",
    }
    stage = status.get("stage", "not_started")
    result = f"<h3>Tool validation</h3><p>{_text(labels.get(stage, stage))}</p>"
    if status.get("tool"):
        result += f"<p>Tool: {_text(status['tool'])}</p>"
    cases = status.get("cases", [])
    if cases:
        passed = sum(bool(case["passed"]) for case in cases)
        result += f'<p class="case-count">{passed} passed · {len(cases) - passed} failed · {len(cases)} checked</p>'
        result += '<div class="validation-cases">'
        for case in cases:
            title = str(case["id"]) + (": PASS" if case["passed"] else ": FAIL")
            evidence = json.dumps(
                {key: case.get(key) for key in ("expected", "observed", "process_failure")},
                indent=2,
                ensure_ascii=True,
            )
            result += _disclosure(title, f"<pre>{_text(evidence[:8192])}</pre>")
        result += "</div>"
    return result
