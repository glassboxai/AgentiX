"""Read-only routing must select a contract before any tool validation or execution."""

import pytest
from test_v5_tool_contracts import CODE

from agentix.application.tool_routing import ToolRouter
from agentix.domain.tool_schema import extract_tool_schema


class Catalog:
    """Only a calculator exists in this authored fixture."""

    def contracts(self):
        """Return data rather than callable capabilities."""
        return {"calculator": extract_tool_schema("calculator", CODE)}


def test_unmatched_query_can_request_creation_without_validating_existing_tool(tmp_path):
    """The model has no verification or execution tool during semantic selection."""
    seen = []

    def factory(path):
        """Capture the read-only router input."""

        def client(role, content):
            seen.append(content)
            return {
                "action": "CREATE_TOOL",
                "tool_name": "vowel_counter",
                "purpose": "Count English vowels; arithmetic cannot do this",
            }

        return client

    result = ToolRouter(Catalog(), tmp_path, factory).select("Count vowels in Hello World!")
    assert result["action"] == "CREATE_TOOL"
    assert set(seen[0]["requirements"]["catalog"]) == {"calculator"}
    assert "No tools may be called" in seen[0]["system"]


def test_creation_route_accepts_the_serialized_empty_argument_transport(tmp_path):
    """Structured output serializes default arguments; creation must still be selected."""
    from types import SimpleNamespace

    from agentix.application.tool_routing import RoutingModelClient
    from agentix.domain.tool_routing import ToolRoute

    def factory(path):
        """Mirror CrewAI returning the response model as JSON, defaults included."""
        model = SimpleNamespace(
            call=lambda **kwargs: ToolRoute(
                action="CREATE_TOOL",
                tool_name="count_word_occurrences",
                purpose="Count how many times a word appears in a text",
            ).model_dump_json()
        )
        return RoutingModelClient(model)

    result = ToolRouter(Catalog(), tmp_path, factory).select(
        "Create a tool which takes a text and a word and returns the times that word is "
        "contained in the text."
    )
    assert result["action"] == "CREATE_TOOL"
    assert result["tool_name"] == "count_word_occurrences"
    assert result["arguments"] == {}


@pytest.mark.parametrize(
    "arguments", [[{"name": "text", "value": "abc"}], {"text": "abc"}], ids=["pairs", "mapping"]
)
def test_creation_route_still_rejects_execution_arguments(tmp_path, arguments):
    """A creation proposal never carries execution arguments, empty transport aside."""

    def factory(path):
        """Return a creation proposal that smuggles execution arguments."""
        return lambda role, content: {
            "action": "CREATE_TOOL",
            "tool_name": "vowel_counter",
            "purpose": "Count English vowels",
            "arguments": arguments,
        }

    with pytest.raises(ValueError, match="Creation route contains execution arguments"):
        ToolRouter(Catalog(), tmp_path, factory).select("Count vowels")


@pytest.mark.parametrize("arguments", [{"text": "Hello World!"}, {"a": True, "b": 3}, {"a": 2}])
def test_reuse_with_incompatible_arguments_stops_before_validation(tmp_path, arguments):
    """Unknown/missing/type-incompatible ports fail closed."""

    def factory(path):
        """Return a deliberately invalid model routing proposal."""
        return lambda role, content: {
            "action": "REUSE_TOOL",
            "tool_name": "calculator",
            "purpose": "bad selection",
            "arguments": arguments,
        }

    with pytest.raises(ValueError):
        ToolRouter(Catalog(), tmp_path, factory).select("Count vowels")


def test_creation_route_does_not_invoke_manager_execution_tools():
    """The unmatched route must reach creation without validating another catalog item."""
    from types import SimpleNamespace
    from unittest.mock import Mock

    from agentix.application.tool_workflow import Orchestrator

    service = object.__new__(Orchestrator)
    service.get_installed_tools_catalog = lambda: "calculator exists"
    service.applications = None
    service.router = SimpleNamespace(
        select=lambda query: {
            "action": "CREATE_TOOL",
            "tool_name": "vowel_counter",
            "purpose": "Count vowels",
            "arguments": {},
        }
    )
    service.verification = SimpleNamespace(invalidate=Mock())
    service.build_tool_pipeline = Mock(
        return_value="PIPELINE_STAGE_FAILED: controlled fixture stop"
    )
    assert service._run_system("Count vowels").startswith("PIPELINE_STAGE_FAILED")
    service.verification.invalidate.assert_called_once_with("vowel_counter")
    assert service.build_tool_pipeline.call_args.kwargs["tool_name"] == "vowel_counter"


def test_router_client_never_exposes_framework_tools():
    """Use the session client, but pass an explicitly empty tool list."""
    from types import SimpleNamespace
    from unittest.mock import Mock

    from agentix.application.tool_routing import RoutingModelClient

    call = Mock(
        return_value='{"action":"CREATE_TOOL","tool_name":"x","purpose":"New capability","arguments":{}}'
    )
    RoutingModelClient(SimpleNamespace(call=call))(
        "Tool Router", {"system": "Select only", "requirements": {}}
    )
    assert call.call_args.kwargs["tools"] == []
    assert call.call_args.kwargs["response_model"] is not None


def test_real_owner_composition_enables_strict_contract_and_router(tmp_path, monkeypatch):
    """Owned coordinators are subclasses, not instances; they must enable production gates."""
    from types import SimpleNamespace

    from agentix.bootstrap import create_runtime
    from agentix.security import SecurityManager
    from agentix.settings import Settings

    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path / "home"))
    agents = SimpleNamespace(
        manager=object(),
        creation_manager=object(),
        application_selector=None,
        architect=object(),
        coder=object(),
        tester=object(),
    )
    backend = SimpleNamespace(Task=object, Crew=object, Process=object)
    runtime = create_runtime(
        Settings(tmp_path, tmp_path / "tools"),
        owner_id="routing-owner",
        llm=SimpleNamespace(call=lambda **kwargs: "{}"),
        backend=backend,
        tool_factory=lambda operations: object(),
        agent_factory=lambda model, tools: agents,
    )
    assert runtime.security is not SecurityManager
    assert runtime.security.strict_tool_contract is True
    assert runtime.orchestrator.router is not None


def test_router_model_errors_do_not_reveal_response_or_credentials():
    """Provider errors may contain request secrets and must not reach the GUI."""
    from types import SimpleNamespace
    from unittest.mock import Mock

    from agentix.application.tool_routing import RoutingModelClient

    client = RoutingModelClient(
        SimpleNamespace(call=Mock(side_effect=RuntimeError("private-response-token")))
    )
    with pytest.raises(ValueError) as error:
        client("Tool Router", {"system": "Select", "requirements": {}})
    assert "private-response-token" not in str(error.value)


def test_tool_routing_decides_before_any_application_suggestion():
    """The exact-contract router is authoritative; suggestions run only on CREATE_TOOL."""
    from types import SimpleNamespace
    from unittest.mock import Mock

    from agentix.application.tool_workflow import Orchestrator

    order = []
    agent = object()
    agents = SimpleNamespace(
        manager=agent, creation_manager=agent, architect=agent, coder=agent, tester=agent
    )
    router = SimpleNamespace(
        select=Mock(
            side_effect=lambda query: (
                order.append("router"),
                {"action": "REUSE_TOOL", "tool_name": "count_vowels"},
            )[1]
        )
    )
    applications = SimpleNamespace(
        candidates=Mock(side_effect=lambda: order.append("candidates") or []),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    orchestrator = Orchestrator(
        agents,
        SimpleNamespace(
            Task=Mock(return_value=object()),
            Crew=Mock(side_effect=AssertionError("no model turn")),
            Process=SimpleNamespace(sequential="sequential"),
        ),
        lambda: "approved tools",
        applications=applications,
        router=router,
    )
    orchestrator._reuse_selected = Mock(return_value="observed tool result")
    assert orchestrator.run_system("Tell me how many vowels there are in 'Hola caracola'") == (
        "observed tool result"
    )
    assert order == ["router"]
    applications.candidates.assert_not_called()
    applications.observed_answer.assert_not_called()
    applications.execute.assert_not_called()


def test_malformed_acceptance_is_reviewable_but_routing_remains_strict(tmp_path):
    """Nonfinite model proposals reach only human review, never selected execution."""
    from types import SimpleNamespace
    from unittest.mock import Mock

    from agentix.application.tool_routing import RoutingModelClient

    raw = '{"version":1,"cases":[{"invalid":NaN}]}'
    client = RoutingModelClient(SimpleNamespace(call=Mock(return_value=raw)))
    assert client("Acceptance Planner", {"system": "Propose", "requirements": {}}) == raw
    with pytest.raises(ValueError):
        client("Tool Router", {"system": "Select", "requirements": {}})
    router = ToolRouter(Catalog(), tmp_path, lambda path: client)
    assert router.acceptance("calculator", CODE, "Reviewed arithmetic contract") == raw


def test_routing_grammar_is_accepted_by_strict_external_providers():
    """Strict providers reject empty schemas, open maps, unions and recursive refs."""
    from agentix.domain.tool_routing import ToolRoute

    def violations(node, path="$"):
        """Collect every construct the external structured-output subset forbids."""
        found = []
        if isinstance(node, dict):
            if not node:
                found.append(("empty", path))
            if node.get("type") == "object" and isinstance(node.get("additionalProperties"), dict):
                found.append(("open_object", path))
            if node.get("type") == "object" and "additionalProperties" not in node:
                found.append(("implicit_open_object", path))
            if "oneOf" in node or "anyOf" in node and node.get("type") == "object":
                found.append(("union_object", path))
            if "discriminator" in node:
                found.append(("discriminator", path))
            for key, value in node.items():
                found.extend(violations(value, f"{path}/{key}"))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                found.extend(violations(value, f"{path}/{index}"))
        return found

    schema = ToolRoute.model_json_schema()
    assert violations(schema) == []
    arguments = schema["properties"]["arguments"]
    assert arguments["type"] == "array"
    assert arguments["maxItems"] == 12
    pair = schema["$defs"]["ArgumentPair"]
    assert pair["additionalProperties"] is False
    assert set(pair["properties"]) == {"name", "value"}


def test_reuse_arguments_accept_scalars_and_nested_lists_only():
    """Objects and nulls are not tool argument values; reject them before execution."""
    from pydantic import ValidationError

    from agentix.domain.tool_routing import ReuseRoute

    route = ReuseRoute(
        action="REUSE_TOOL",
        tool_name="count_vowels",
        purpose="Count vowels",
        arguments=[
            {"name": "text", "value": "Hello"},
            {"name": "rows", "value": [["a"], ["b"]]},
            {"name": "limit", "value": 3},
            {"name": "flag", "value": True},
        ],
    )
    assert route.arguments[1].value == [["a"], ["b"]]
    for invalid in ({"name": "text", "value": {"nested": 1}}, {"name": "text", "value": None}):
        with pytest.raises(ValidationError):
            ReuseRoute(
                action="REUSE_TOOL",
                tool_name="count_vowels",
                purpose="Count vowels",
                arguments=[invalid],
            )


def test_router_converts_argument_pairs_and_rejects_duplicate_names(tmp_path):
    """The pair list becomes the reviewed keyword mapping; duplicates fail closed."""
    from agentix.application.tool_routing import ToolRouter

    def factory(path):
        """Return a valid pair list for the authored calculator contract."""
        return lambda role, content: {
            "action": "REUSE_TOOL",
            "tool_name": "calculator",
            "purpose": "Add two numbers",
            "arguments": [{"name": "a", "value": 1}, {"name": "b", "value": 2}],
        }

    route = ToolRouter(Catalog(), tmp_path, factory).select("add 1 and 2")
    assert route["arguments"] == {"a": 1, "b": 2}

    def duplicate(path):
        """Repeat one parameter name with conflicting values."""
        return lambda role, content: {
            "action": "REUSE_TOOL",
            "tool_name": "calculator",
            "purpose": "Add two numbers",
            "arguments": [{"name": "a", "value": 1}, {"name": "a", "value": 2}],
        }

    with pytest.raises(ValueError, match="Duplicate tool argument name"):
        ToolRouter(Catalog(), tmp_path, duplicate).select("add 1 and 2")


def test_acceptance_provider_failure_still_requires_manual_valid_cases(tmp_path):
    """A failed proposer may expose an empty review, never fabricated accepted evidence."""
    seen = []

    def factory(path):
        """Fail the injected read-only provider with a secret-like body."""

        def client(role, content):
            seen.append(content)
            raise ValueError("private-provider-detail")

        return client

    result = ToolRouter(Catalog(), tmp_path, factory).acceptance(
        "calculator", CODE, "Approved arithmetic"
    )
    assert "unavailable" in result.lower()
    assert "private-provider-detail" not in result
    assert "at most four" in seen[0]["system"]
    from agentix.security.acceptance import parse_contract

    with pytest.raises(ValueError):
        parse_contract(result)
