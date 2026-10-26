"""LIVE-UI-001: no-output Gradio callbacks must not return ignored values."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.frameworks
def test_approval_callback_respects_real_gradio_output_contract():
    """Exercise the registered callback rather than matching its source text."""
    script = """
import os
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
import _agentix_path
import gradio as gr
from agentix.approvals import ApprovalCoordinator
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionRegistry
from agentix.ui.view import build_view
def create(identity):
    return UiController(lambda query:'unused', lambda:'temporary catalog',
                        ApprovalCoordinator.for_owner(identity), gr.update)
view = build_view(SessionRegistry(create), gradio_module=gr)
approval = next(f for f in view.demo.fns.values() if f.fn.__name__ == 'approve')
result = approval.fn('', 'expired-request', None, gr.Request(session_hash='temporary-owner'))
assert approval.outputs == []
assert result is None, 'Gradio no-output approval callback returned an ignored value: ' + repr(result)
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
