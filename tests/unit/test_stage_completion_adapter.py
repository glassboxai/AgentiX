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


def test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution(system):
    """Verify qa finishes on acceptance but reuse manager continues to execution."""
    assert getattr(system.main.tester_agent.tools[1], "result_as_answer", False) is True
    assert getattr(system.main.manager_agent.tools[1], "result_as_answer", False) is False
