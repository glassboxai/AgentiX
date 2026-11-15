"""Tools-tab queries execute approved tools and never an installed application."""

from types import SimpleNamespace
from unittest.mock import Mock

from test_execution_handoff import authorize_fixture

VOWEL_CODE = "def count_vowels(text: str) -> int: return sum(c in 'aeiou' for c in text.lower())"
CALCULATOR_CODE = (
    "def basic_calculator(operation: str, num1: float, num2: float) -> float:\n"
    "    return {'add': num1 + num2, 'multiply': num1 * num2}[operation]"
)


def _router(tool_name: str, arguments: dict) -> SimpleNamespace:
    """Return only the exact-contract decision; acceptance must never rerun."""
    return SimpleNamespace(
        select=Mock(
            return_value={
                "action": "REUSE_TOOL",
                "tool_name": tool_name,
                "arguments": arguments,
                "purpose": "reuse",
            }
        ),
        acceptance=Mock(side_effect=AssertionError("no acceptance rerun")),
    )


def _applications() -> SimpleNamespace:
    """Fail on any application suggestion or execution attempt."""
    return SimpleNamespace(
        candidates=Mock(side_effect=AssertionError("must not suggest")),
        observed_answer=Mock(side_effect=AssertionError("must not execute")),
        execute=Mock(side_effect=AssertionError("must not execute")),
    )


def test_vowel_query_reuses_the_installed_tool_without_application_routing(system):
    """A compatible installed tool answers the query; no application path is reached."""
    authorize_fixture(
        system,
        name="count_vowels",
        function="count_vowels",
        code=VOWEL_CODE,
        cases=[
            {
                "id": "vowels",
                "purpose": "Count English vowels",
                "function": "count_vowels",
                "kwargs": {"text": "Hola"},
                "expect": {"kind": "value", "value": 2},
            }
        ],
    )
    assert system.custom_tools.execute_generated_tool_tool(
        "count_vowels", "count_vowels", '{"text": "hola"}'
    ).endswith("2")
    system.main.operations = system.custom_tools
    system.main.applications = _applications()
    system.main.router = _router("count_vowels", {"text": "Hola caracola"})
    system.main.Crew = Mock(side_effect=AssertionError("no model turn"))
    result = system.main.run_system("Tell me how many vowels there are in 'Hola caracola'")
    assert "Result: 6" in result and '"text": "Hola caracola"' in result
    system.main.applications.candidates.assert_not_called()
    system.main.applications.observed_answer.assert_not_called()
    system.main.applications.execute.assert_not_called()


def test_calculator_query_reuses_the_installed_tool_without_application_routing(system):
    """A compatible calculator tool answers the query; no application path is reached."""
    authorize_fixture(
        system,
        name="basic_calculator",
        function="basic_calculator",
        code=CALCULATOR_CODE,
        cases=[
            {
                "id": "multiply",
                "purpose": "Multiply two numbers",
                "function": "basic_calculator",
                "kwargs": {"operation": "multiply", "num1": 2, "num2": 3},
                "expect": {"kind": "value", "value": 6},
            }
        ],
    )
    assert system.custom_tools.execute_generated_tool_tool(
        "basic_calculator",
        "basic_calculator",
        '{"operation": "multiply", "num1": 2, "num2": 3}',
    ).endswith("6")
    system.main.operations = system.custom_tools
    system.main.applications = _applications()
    system.main.router = _router(
        "basic_calculator", {"operation": "multiply", "num1": 2, "num2": 80}
    )
    system.main.Crew = Mock(side_effect=AssertionError("no model turn"))
    result = system.main.run_system("Give me the result of multiplying 2 by 80")
    assert "Result: 160" in result and '"num2": 80' in result
    system.main.applications.candidates.assert_not_called()
    system.main.applications.observed_answer.assert_not_called()
    system.main.applications.execute.assert_not_called()
