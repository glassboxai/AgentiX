"""Real CrewAI verbose events must reach only their owning GUI conversation."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.frameworks
def test_real_verbose_messages_and_diagnostics_reach_separate_controllers():
    """Use the SDK event renderer and workers, without a model or HTTP server."""
    script = r"""
import os
os.environ.update(OTEL_SDK_DISABLED='true', CREWAI_DISABLE_TELEMETRY='true',
    CREWAI_DISABLE_TRACKING='true', CREWAI_TRACING_ENABLED='false',
    CREWAI_DISABLE_VERSION_CHECK='true', GRADIO_ANALYTICS_ENABLED='False')
import _agentix_path
import threading, time
from agentix.bootstrap import configure_process
configure_process()
from agentix.diagnostics import activity_output
from agentix.approvals import ApprovalCoordinator
from agentix.ui.controller import UiController
from crewai.events.event_bus import crewai_event_bus
from crewai.events.event_listener import EventListener
from crewai.events.types.logging_events import AgentLogsStartedEvent, AgentLogsExecutionEvent
from crewai.agents.parser import AgentAction, AgentFinish
listener = EventListener()
barrier = threading.Barrier(2)
def create(owner):
    def workflow(query):
        barrier.wait(5)
        events = [
            AgentLogsStartedEvent(agent_role=owner+' Architect', task_description=owner+' task', verbose=True),
            AgentLogsExecutionEvent(agent_role=owner+' Architect', verbose=True,
                formatted_answer=AgentAction(thought='', tool='fixture',tool_input='{}',text='',result=owner+' tool result')),
            AgentLogsExecutionEvent(agent_role=owner+' Architect', verbose=True,
                formatted_answer=AgentFinish(thought='',output=owner+' final answer',text='')),
        ]
        for event in events:
            future = crewai_event_bus.emit(None, event)
            assert future is not None
            future.result(timeout=10)
        return owner+' completed'
    return UiController(workflow, lambda:'Temporary catalog', ApprovalCoordinator.for_owner(owner), lambda **kw:kw)
with activity_output():
    alice, bob = create('Alice'), create('Bob')
    alice.process_user_query('Alice query')
    bob.process_user_query('Bob query')
    deadline=time.monotonic()+30
    while (alice.state.is_running or bob.state.is_running) and time.monotonic()<deadline:
        time.sleep(.02)
    assert not alice.state.is_running and not bob.state.is_running
    for owner, other, controller in [('Alice','Bob',alice),('Bob','Alice',bob)]:
        content=controller.poll_system_status()[0][-1]['content']
        for expected in [owner+' Architect',owner+' task',owner+' tool result',owner+' final answer','workflow_started',owner+' completed']:
            assert expected in content, (expected,content)
        assert other not in content, content
        assert '\x1b' not in content
print('real-verbose-owned-output-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "real-verbose-owned-output-ok" in result.stdout
