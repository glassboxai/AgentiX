"""Real native callback watchdog and cleanup evidence, without model inference."""

import json
import time

import pytest
import schema3_package

from agentix.lab.application_artifacts import (
    ApprovedApplication,
    application_digest,
    approve_application,
)
from agentix.lab.application_session import ApplicationSession

pytestmark = pytest.mark.windows_isolation


def test_blocked_callback_stops_the_owned_persistent_job(tmp_path):
    """A GUI with no idle TTL still terminates a callback exceeding 45 seconds."""
    package = schema3_package.package(tmp_path)
    capability = approve_application(package, application_digest(package))
    probe = b'''"""Reviewed maintained infinite-callback probe; never a user artifact."""
import gradio as gr

def blocked():
    """Deliberately consume the operation budget inside native isolation."""
    while True:
        pass

def create_application():
    """Expose a single maintained blocked operation for the watchdog test."""
    with gr.Blocks() as demo:
        button = gr.Button("Run")
        output = gr.Number()
        button.click(blocked, inputs=None, outputs=output, queue=False, api_name="blocked")
    return demo
'''
    files = tuple((name, probe if name == "app.py" else body) for name, body in capability.files)
    observed = ApprovedApplication(files, "explicitly-reviewed-maintained-timeout-probe")
    with ApplicationSession(observed, lifetime=None) as session:
        root = session.root
        started = time.monotonic()
        with pytest.raises(RuntimeError):
            session.request("POST", "/gradio_api/run/blocked", json.dumps({"data": []}).encode())
        session.native_thread.join(12)
        assert not session.native_thread.is_alive()
        assert session.diagnostics.get("failure") == "callback_timeout"
        assert 44 <= time.monotonic() - started < 65
    assert not root.exists()
