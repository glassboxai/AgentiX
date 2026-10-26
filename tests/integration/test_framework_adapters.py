"""Check real optional adapters without models, servers or project artifact reads."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.frameworks
def test_real_crewai_schemas_and_gradio_bindings():
    """Catch bound-method schema errors and invalid real widget registrations."""
    root = Path(__file__).resolve().parents[2]
    script = """
import os
os.environ.update(OTEL_SDK_DISABLED='true', CREWAI_DISABLE_TELEMETRY='true', CREWAI_DISABLE_TRACKING='true', CREWAI_TRACING_ENABLED='false', GRADIO_ANALYTICS_ENABLED='False')
import _agentix_path
from types import SimpleNamespace
from agentix.adapters.crewai import register_tools, build_agents
from agentix.tools import ArtifactTools
from agentix.ui.controller import UiController
from agentix.ui.view import build_view
from agentix.ui.sessions import SessionRegistry
import gradio as gr
operations = ArtifactTools(SimpleNamespace(owner_id='framework-fixture'))
tools = register_tools(operations)
assert tools.save_specifications_tool.result_as_answer is True
assert tools.compile_and_save_code_tool.result_as_answer is True
assert tools.run_and_save_tests_tool.result_as_answer is False
assert tools.execute_generated_tool_tool.result_as_answer is True
assert tools.finish_acceptance_tool.result_as_answer is True
assert tools.submit_acceptance_cases_tool.result_as_answer is False
schema = tools.execute_generated_tool_tool.args_schema.model_json_schema()
assert set(schema['properties']) == {'tool_name', 'function_name', 'kwargs_json'}, schema
assert set(tools.compile_and_save_code_tool.args_schema.model_json_schema()['properties']) == {'tool_name', 'code'}
from crewai import LLM
from crewai.utilities.prompts import Prompts
agents = build_agents(LLM(model='ollama/qwen3-coder:30b', base_url='http://127.0.0.1:11434'), tools)
assert agents.creation_manager.tools == [] and agents.manager.tools
for agent in (agents.manager, agents.architect, agents.coder, agents.tester, agents.creation_manager):
    system = Prompts(agent=agent, has_tools=True, use_system_prompt=True).task_execution().system
    assert 'APPLICATION WORKFLOW POLICY' in system
    assert 'exact tier boundaries' in system and 'invalid types' in system
    assert 'human review' in system and 'EXECUTE' in system
view = build_view(SessionRegistry(lambda session_id: UiController(lambda query: 'unused', lambda: 'No tools installed yet.', SimpleNamespace(), gr.update)), gradio_module=gr)
assert len(view.demo.get_config_file()['components']) > 0
approval = next(function for function in view.demo.fns.values() if function.fn.__name__ == 'approve')
assert not approval.inputs[1].stateful, 'Displayed request ID must travel with the browser snapshot, not mutable server State'
print('real-adapters-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", script], cwd=root, capture_output=True, text=True, timeout=90
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "real-adapters-ok" in result.stdout
