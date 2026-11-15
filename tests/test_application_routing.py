"""Application suggestions are bounded recommendations, never execution grants."""

import json
import logging
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

APP = "a" * 32
OTHER = "b" * 32
CANDIDATES = [{"id": APP, "name": "Vowel Counter", "description": "Counts vowels in text"}]
MESSAGE = (
    "This request appears to match the application 'Vowel Counter'. "
    "Please open it from the Applications tab."
)


def test_application_selector_has_no_tools_and_keeps_budgets(system):
    """Prevent SDK tool-call bias from bypassing the catalog-only decision."""
    selector = system.main.application_selector_agent
    assert selector is not system.main.manager_agent
    assert selector.tools == [] and selector.verbose is True
    assert (
        selector.max_iter == 12
        and selector.max_execution_time == 600
        and selector.max_retry_limit == 0
    )


@pytest.mark.parametrize(
    "raw",
    [
        "ordinary answer",
        '{"action":"NO_APPLICATION_MATCH","extra":true}',
        '{"action":"NO_APPLICATION_MATCH","action":"NO_APPLICATION_MATCH"}',
        json.dumps({"action": "SUGGEST_APPLICATION", "app_id": OTHER}),
        json.dumps({"action": "SUGGEST_APPLICATION", "app_id": APP, "arguments": {"text": "x"}}),
        json.dumps({"action": "SUGGEST_APPLICATION", "app_ids": [APP, OTHER]}),
        json.dumps({"action": "RUN_APPLICATION", "app_id": APP, "arguments": {"text": "x"}}),
        json.dumps({"action": "CREATE_TOOL", "tool_name": "unexpected", "purpose": "no"}),
    ],
)
def test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments(raw):
    """Malformed or ambiguous decisions fail closed instead of becoming a suggestion."""
    from agentix.decisions import parse_application_suggestion

    with pytest.raises(ValueError):
        parse_application_suggestion(raw, {APP})


def test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match():
    """A recommendation names one current catalog row and carries no arguments."""
    from agentix.decisions import parse_application_suggestion

    assert parse_application_suggestion('{"action":"NO_APPLICATION_MATCH"}', {APP}) is None
    suggestion = parse_application_suggestion(
        json.dumps({"action": "SUGGEST_APPLICATION", "app_id": APP}), {APP}
    )
    assert suggestion.app_id == APP


def test_single_matching_application_is_only_recommended(system, caplog):
    """A complete match yields a safe message; no execution path is reachable."""
    system.main.applications = SimpleNamespace(
        candidates=Mock(return_value=CANDIDATES),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    system.main.Crew = Mock(
        side_effect=[
            SimpleNamespace(
                kickoff=lambda: '{"action":"CREATE_TOOL","tool_name":"vowels","purpose":"count"}'
            ),
            SimpleNamespace(
                kickoff=lambda: json.dumps({"action": "SUGGEST_APPLICATION", "app_id": APP})
            ),
        ]
    )
    system.main.build_tool_pipeline = Mock(side_effect=AssertionError("no creation"))
    with caplog.at_level(logging.DEBUG):
        result = system.main.run_system("Tell me how many vowels there are in 'Hola caracola'")
    assert result == MESSAGE
    assert APP not in result and "text" not in result and "arguments" not in result
    system.main.applications.observed_answer.assert_not_called()
    system.main.applications.execute.assert_not_called()
    assert "Hola caracola" not in caplog.text
    assert "application_suggested" in caplog.text


@pytest.mark.parametrize(
    "raw",
    [
        "ordinary answer",
        json.dumps({"action": "SUGGEST_APPLICATION", "app_id": OTHER}),
        json.dumps({"action": "SUGGEST_APPLICATION", "app_ids": [APP, OTHER]}),
        json.dumps({"action": "RUN_APPLICATION", "app_id": APP, "arguments": {"text": "x"}}),
    ],
)
def test_invalid_or_ambiguous_suggestion_keeps_the_creation_route(system, raw):
    """A rejected suggestion never blocks creation and never executes an application."""
    system.main.applications = SimpleNamespace(
        candidates=Mock(return_value=CANDIDATES),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    system.main.Crew = Mock(
        side_effect=[
            SimpleNamespace(
                kickoff=lambda: '{"action":"CREATE_TOOL","tool_name":"vowels","purpose":"count"}'
            ),
            SimpleNamespace(kickoff=lambda: raw),
        ]
    )
    system.main.build_tool_pipeline = Mock(return_value="PIPELINE_STAGE_FAILED: specification: x")
    assert system.main.run_system("Count the vowels").startswith("PIPELINE_STAGE_FAILED:")
    system.main.build_tool_pipeline.assert_called_once()
    system.main.applications.observed_answer.assert_not_called()
    system.main.applications.execute.assert_not_called()


def test_explicit_no_match_keeps_the_creation_route(system):
    """Only an explicit no-match continues to the existing new-tool flow."""
    system.main.applications = SimpleNamespace(
        candidates=Mock(return_value=CANDIDATES),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    system.main.Crew = Mock(
        side_effect=[
            SimpleNamespace(
                kickoff=lambda: '{"action":"CREATE_TOOL","tool_name":"vowels","purpose":"count"}'
            ),
            SimpleNamespace(kickoff=lambda: '{"action":"NO_APPLICATION_MATCH"}'),
        ]
    )
    system.main.build_tool_pipeline = Mock(return_value="PIPELINE_STAGE_FAILED: specification: x")
    assert system.main.run_system("Count the vowels").startswith("PIPELINE_STAGE_FAILED:")
    system.main.build_tool_pipeline.assert_called_once()


def test_no_installed_application_skips_the_suggestion_model_call(system):
    """An empty catalog must not spend a model turn on application classification."""
    system.main.applications = SimpleNamespace(
        candidates=Mock(return_value=[]),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    system.main.Crew = Mock(
        return_value=SimpleNamespace(
            kickoff=lambda: '{"action":"CREATE_TOOL","tool_name":"vowels","purpose":"count"}'
        )
    )
    system.main.build_tool_pipeline = Mock(return_value="PIPELINE_STAGE_FAILED: specification: x")
    assert system.main.run_system("Count the vowels").startswith("PIPELINE_STAGE_FAILED:")
    assert system.main.Crew.call_count == 1
    assert system.main.Crew.call_args.kwargs["agents"] == [system.main.creation_manager_agent]


def test_suggestion_prompt_carries_only_identity_name_and_description(system):
    """Node IDs, parameter names and arguments must never reach the suggestion prompt."""
    system.main.applications = SimpleNamespace(
        candidates=Mock(return_value=CANDIDATES),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )
    system.main.Crew = Mock(
        side_effect=[
            SimpleNamespace(
                kickoff=lambda: '{"action":"CREATE_TOOL","tool_name":"vowels","purpose":"count"}'
            ),
            SimpleNamespace(kickoff=lambda: '{"action":"NO_APPLICATION_MATCH"}'),
        ]
    )
    system.main.build_tool_pipeline = Mock(return_value="PIPELINE_STAGE_FAILED: specification: x")
    system.main.run_system("Count the vowels")
    description = system.main.Task.call_args.kwargs["description"]
    assert APP in description and "Vowel Counter" in description
    for forbidden in ('"input_operation"', '"num1"', '"text":'):
        assert forbidden not in description
