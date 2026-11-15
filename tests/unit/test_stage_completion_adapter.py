"""Stage-ending tools must return control to host gates after a reviewed save."""

from types import SimpleNamespace

from agentix.adapters.crewai import register_tools


def test_reviewed_specification_and_code_saves_end_the_agent_stage(system):
    """Catch an adapter that asks the model again after the approved stage result."""
    registered = register_tools(
        system.custom_tools,
        decorator=lambda name: lambda fn: SimpleNamespace(run=fn, result_as_answer=False),
    )
    assert registered.save_specifications_tool.result_as_answer is True
    assert registered.compile_and_save_code_tool.result_as_answer is True
    assert registered.execute_generated_tool_tool.result_as_answer is True
    # QA must still propose acceptance after provisional unittest execution.
    assert registered.run_and_save_tests_tool.result_as_answer is False
    # Existing-tool manager must still execute after reviewing acceptance.
    assert registered.submit_acceptance_cases_tool.result_as_answer is False


def test_contract_rejection_keeps_the_coder_turn_open(system):
    """A rejected contract is repairable inside the turn; only a save ends it."""
    system.security.strict_tool_contract = True
    registered = register_tools(
        system.custom_tools,
        decorator=lambda name: lambda fn: SimpleNamespace(run=fn, result_as_answer=False),
    )
    tool = registered.compile_and_save_code_tool
    assert tool.result_as_answer is True

    rejection = tool.run(
        tool_name="adder", code='"""Missing function docstring."""\ndef adder(value): return value'
    )
    assert rejection.startswith("CONTRACT_ERROR:")
    assert tool.result_as_answer is False

    system.security.auto_approve = True
    saved = tool.run(
        tool_name="adder",
        code="\n".join(
            [
                '"""Trusted adder fixture."""',
                "from typing import Annotated",
                'def adder(value: Annotated[int, "Supplied value"]) -> Annotated[int, "Same value"]:',
                '    """Return the supplied value unchanged."""',
                "    return value",
            ]
        ),
    )
    assert saved.startswith("Success:")
    assert tool.result_as_answer is True


def test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution(system):
    """Verify qa finishes on acceptance but reuse manager continues to execution."""
    assert getattr(system.main.tester_agent.tools[1], "result_as_answer", False) is True
    assert getattr(system.main.manager_agent.tools[1], "result_as_answer", False) is False
