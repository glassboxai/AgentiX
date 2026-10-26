"""Use real Gradio server-side preprocessing without launching an HTTP server."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.frameworks
def test_real_gradio_state_owner_and_editor_request_transport():
    """Verify real gradio state owner and editor request transport."""
    root = Path(__file__).resolve().parents[2]
    script = """
import os
os.environ.update(OTEL_SDK_DISABLED='true', CREWAI_DISABLE_TELEMETRY='true', CREWAI_DISABLE_TRACKING='true', CREWAI_TRACING_ENABLED='false', GRADIO_ANALYTICS_ENABLED='False')
import _agentix_path
import asyncio
import gradio as gr
from gradio.state_holder import SessionState
from agentix.security import SecurityManager
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionRegistry, SessionAccessError
from agentix.ui.view import build_view

def create(identity):
    security = SecurityManager.for_owner(identity)
    controller = UiController(lambda query: 'answer-' + query, lambda: 'catalog', security, gr.update)
    controller.state.session_id = identity
    return controller

registry = SessionRegistry(create)
view = build_view(registry, gradio_module=gr)
demo = view.demo
indices = {function.fn.__name__: index for index, function in demo.fns.items()}
token_component = next(block for block in demo.blocks.values() if isinstance(block, gr.State))

async def verify():
    first, second = SessionState(demo), SessionState(demo)
    alice, bob = gr.Request(session_hash='alice-browser'), gr.Request(session_hash='bob-browser')
    await demo.process_api(indices['submit'], ['alice-private', None], state=first, request=alice, session_hash='alice-browser')
    await demo.process_api(indices['submit'], ['bob-private', None], state=second, request=bob, session_hash='bob-browser')
    result_a = await demo.process_api(indices['poll'], [None], state=first, request=alice, session_hash='alice-browser')
    result_b = await demo.process_api(indices['poll'], [None], state=second, request=bob, session_hash='bob-browser')
    assert 'alice-private' in str(result_a['data'][0]) and 'bob-private' not in str(result_a['data'][0])
    assert 'bob-private' in str(result_b['data'][0]) and 'alice-private' not in str(result_b['data'][0])
    token_a = first[token_component._id]
    session = registry.resolve(token_a, 'alice-browser')
    security = session.controller.security
    security._pending_request = dict(request_id='request-1', owner_id=security.owner_id, filepath='fixture.py', action='write', content='original', expires_at=float('inf'))
    await demo.process_api(indices['poll'], [None], state=first, request=alice, session_hash='alice-browser')
    await demo.process_api(indices['approve'], ['edited', 'old-request', None], state=first, request=alice, session_hash='alice-browser')
    assert not security._approval_event.is_set()
    await demo.process_api(indices['approve'], ['edited', 'request-1', None], state=first, request=alice, session_hash='alice-browser')
    assert security._approval_event.is_set() and security._edited_content == 'edited'
    second[token_component._id] = token_a
    try:
        await demo.process_api(indices['poll'], [None], state=second, request=bob, session_hash='bob-browser')
    except SessionAccessError:
        pass
    else:
        raise AssertionError('Foreign owner received another browser session')
    await demo.process_api(indices['unload'], [], state=first, request=alice, session_hash='alice-browser')
    try:
        registry.resolve(token_a, 'alice-browser')
    except SessionAccessError:
        pass
    else:
        raise AssertionError('Unloaded browser retained a live session')

asyncio.run(verify())
print('real-session-routing-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", script], cwd=root, capture_output=True, text=True, timeout=90
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "real-session-routing-ok" in result.stdout
