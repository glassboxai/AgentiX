"""Real Gradio request preprocessing for mandatory acceptance approval, no server."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.frameworks
def test_real_gradio_human_acceptance_edit_and_owner_boundary():
    """Verify real gradio human acceptance edit and owner boundary."""
    root = Path(__file__).resolve().parents[2]
    script = r"""
import os
os.environ.update(GRADIO_ANALYTICS_ENABLED='False', OTEL_SDK_DISABLED='true')
import _agentix_path
import sys, asyncio, json, tempfile, threading
from pathlib import Path
sys.path.insert(0, 'tests')
from trusted_sandbox import TrustedFixtureSandbox
import gradio as gr
from gradio.state_holder import SessionState
from agentix.security import SecurityManager
from agentix.tools import ArtifactTools
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionRegistry
from agentix.ui.view import build_view

with tempfile.TemporaryDirectory() as folder:
    operations = {}
    def create(identity):
        security = SecurityManager.for_owner(identity, timeout=10)
        security.TOOLS_ROOT_DIR = str(Path(folder)/identity)
        security.auto_approve = True
        service = ArtifactTools(security, sandbox=TrustedFixtureSandbox())
        operations[identity] = service
        return UiController(lambda query:'unused', lambda:'catalog', security, gr.update,
                            validation=service.acceptance)
    registry = SessionRegistry(create)
    demo = build_view(registry, gradio_module=gr).demo
    indices = {f.fn.__name__:i for i,f in demo.fns.items()}
    token_component = next(b for b in demo.blocks.values() if isinstance(b,gr.State))
    async def verify():
        state = SessionState(demo)
        request = gr.Request(session_hash='acceptance-alice')
        await demo.process_api(indices['poll'],[None],state=state,request=request,session_hash='acceptance-alice')
        session = registry.resolve(state[token_component._id],'acceptance-alice')
        service = operations[session.session_id]
        service.compile_and_save_code_tool('adder','def add(): return 3')
        tests = 'import unittest\nclass Checks(unittest.TestCase):\n def test_constant(self): self.assertEqual(1,1)\n'
        assert service.run_and_save_tests_tool('adder',tests).startswith('TESTS_PROVISIONAL_PASSED:')
        case = {'version':1,'cases':[{'id':'private_case','purpose':'Check sum','function':'add','kwargs':{},'expect':{'kind':'value','value':99}}]}
        results = []
        thread = threading.Thread(target=lambda:results.append(service.submit_acceptance_cases_tool('adder',json.dumps(case))))
        thread.start()
        for _ in range(1000):
            pending = service.security.get_pending_request()
            if pending: break
            await asyncio.sleep(.005)
        assert pending and pending['action']=='review_acceptance'
        snapshot = await demo.process_api(indices['poll'],[None],state=state,request=request,session_hash='acceptance-alice')
        assert 'Human acceptance review' in snapshot['data'][2] and 'class Checks' in snapshot['data'][2]
        status = await demo.process_api(indices['validation_status'],[None],state=state,request=request,session_hash='acceptance-alice')
        assert 'Awaiting human' in str(status['data'])
        case['cases'][0]['expect']['value'] = 3
        await demo.process_api(indices['approve'],[json.dumps(case),'stale-id',None],state=state,request=request,session_hash='acceptance-alice')
        assert not service.security._approval_event.is_set()
        await demo.process_api(indices['approve'],[json.dumps(case),pending['request_id'],None],state=state,request=request,session_hash='acceptance-alice')
        await asyncio.to_thread(thread.join,10)
        assert results and results[0].startswith('ACCEPTANCE_VERIFIED:'),results
        assert service.verification.is_verified('adder','add')
        status = await demo.process_api(indices['validation_status'],[None],state=state,request=request,session_hash='acceptance-alice')
        assert 'Verified against approved cases' in str(status['data'])
        bob = SessionState(demo)
        status_b = await demo.process_api(indices['validation_status'],[None],state=bob,request=gr.Request(session_hash='bob'),session_hash='bob')
        assert 'private_case' not in str(status_b['data'])
        await demo.process_api(indices['unload'],[],state=state,request=request,session_hash='acceptance-alice')
        assert not service.verification.is_verified('adder')
    asyncio.run(verify())
print('human-acceptance-gradio-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", script], cwd=root, capture_output=True, text=True, timeout=90
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "human-acceptance-gradio-ok" in result.stdout
