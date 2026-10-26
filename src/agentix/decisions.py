"""Bounded fail-closed manager creation decisions, independent of LLM libraries."""

import json
import re
from dataclasses import dataclass
from typing import Any


class DecisionValidationError(ValueError):
    """Manager output cannot safely authorize tool creation."""


@dataclass(frozen=True)
class CreateToolDecision:
    """Validated exact creation action, portable name and nonblank purpose."""

    tool_name: str
    purpose: str


def _unique_fields(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate fields instead of silently accepting the last value."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DecisionValidationError("Manager decision contains duplicate fields")
        result[key] = value
    return result


def parse_manager_response(response: str) -> CreateToolDecision | str:
    """Accept ordinary answers or a complete exact creation JSON object.

    Creation-like, structured or fenced output must obey the full contract.
    Names are never normalized into another identifier. Invalid output raises
    an error without exposing the original response in logs or error text.
    """
    text = response.strip()
    if not text or len(text) > 100_000:
        raise DecisionValidationError("Manager response is empty or exceeds its limit")
    structured = text.startswith(("{", "[", "```")) or "CREATE_TOOL" in text
    if not structured:
        answer = text.replace("<tool_call>", "").strip()
        if not answer:
            raise DecisionValidationError("Manager returned an empty answer")
        return answer
    fenced = re.fullmatch(r"```(?:json)?\s*\n?(.*?)\s*```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    try:
        data = json.loads(text, object_pairs_hook=_unique_fields)
    except (ValueError, RecursionError) as exc:
        raise DecisionValidationError("Manager returned invalid creation JSON") from exc
    if not isinstance(data, dict) or set(data) != {"action", "tool_name", "purpose"}:
        raise DecisionValidationError("Manager creation fields do not match the contract")
    name, purpose = data["tool_name"], data["purpose"]
    if data["action"] != "CREATE_TOOL":
        raise DecisionValidationError("Manager action is unsupported")
    if (
        not isinstance(name, str)
        or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", name)
        or re.fullmatch(r"(con|prn|aux|nul|com[1-9]|lpt[1-9])", name)
    ):
        raise DecisionValidationError("Manager tool name is invalid")
    if not isinstance(purpose, str) or not purpose.strip() or len(purpose) > 4000:
        raise DecisionValidationError("Manager purpose is invalid")
    return CreateToolDecision(name, purpose.strip())
