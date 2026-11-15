"""Bounded fail-closed routing and creation decisions, independent of LLM libraries."""

import json
import re
from dataclasses import dataclass
from typing import Any


class DecisionValidationError(ValueError):
    """Model output cannot safely authorize a routing or creation decision."""


@dataclass(frozen=True)
class CreateToolDecision:
    """Validated exact creation action, portable name and nonblank purpose."""

    tool_name: str
    purpose: str


@dataclass(frozen=True)
class RunApplicationDecision:
    """A catalog-only opaque application ID and the supported typed data input."""

    app_id: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class ApplicationSuggestion:
    """A catalog-only recommendation that never authorizes application execution."""

    app_id: str


def _unique_fields(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate fields instead of silently accepting the last value."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DecisionValidationError("Manager decision contains duplicate fields")
        result[key] = value
    return result


def parse_manager_response(response: str) -> CreateToolDecision | RunApplicationDecision | str:
    """Accept ordinary answers or exact creation/application JSON contracts.

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
    if isinstance(data, dict) and data.get("action") == "RUN_APPLICATION":
        if (
            set(data) != {"action", "app_id", "arguments"}
            or not isinstance(data["app_id"], str)
            or not re.fullmatch(r"[0-9a-f]{32}", data["app_id"])
        ):
            raise DecisionValidationError("Invalid installed application ID")
        arguments = data["arguments"]
        if (
            not isinstance(arguments, dict)
            or set(arguments) != {"text"}
            or not isinstance(arguments["text"], str)
            or len(arguments["text"]) > 16000
        ):
            raise DecisionValidationError("Invalid application input contract")
        return RunApplicationDecision(data["app_id"], dict(arguments))
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


def parse_application_suggestion(
    response: str, catalog_ids: set[str]
) -> ApplicationSuggestion | None:
    """Parse a tool-free recommendation; only one exact catalog ID may be suggested.

    The decision carries no arguments, so it cannot reach an execution path.
    Prose, unknown IDs, duplicate keys, extra fields, several candidates and the
    legacy ``RUN_APPLICATION`` shape all fail closed instead of degrading into an
    execution or an implicit fallback.
    """
    if not isinstance(response, str) or not response.strip() or len(response) > 100000:
        raise DecisionValidationError("Invalid application suggestion response")
    text = response.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*\n?(.*?)\s*```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    try:
        data = json.loads(text, object_pairs_hook=_unique_fields)
    except (ValueError, RecursionError) as error:
        raise DecisionValidationError("Invalid application suggestion JSON") from error
    if data == {"action": "NO_APPLICATION_MATCH"}:
        return None
    if not isinstance(data, dict) or set(data) != {"action", "app_id"}:
        raise DecisionValidationError("Application suggestion fields do not match the contract")
    if data["action"] != "SUGGEST_APPLICATION":
        raise DecisionValidationError("Application suggestion action is unsupported")
    identity = data["app_id"]
    if not isinstance(identity, str) or identity not in catalog_ids:
        raise DecisionValidationError("Application suggestion must use a current catalog ID")
    return ApplicationSuggestion(identity)
