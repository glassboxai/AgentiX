"""Opt-in real Gradio profile callback with native Windows secret persistence."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = [
    pytest.mark.windows_credentials,
    pytest.mark.skipif(os.name != "nt", reason="Windows only"),
]


def test_gradio_save_refresh_uses_real_windows_vault_and_temporary_metadata():
    """Cover the production callback/store/vault combination with a disposable key."""
    script = r"""
import _agentix_path,asyncio,tempfile
from pathlib import Path
from types import SimpleNamespace
import gradio as gr
from gradio.state_holder import SessionState
from agentix.credentials import WindowsCredentialVault
from agentix.profile_store import SavedProfiles
from agentix.model_profiles import SessionModelConfiguration
from agentix.security import SecurityManager
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionRegistry
from agentix.ui.view import build_view
with tempfile.TemporaryDirectory(prefix='agentix-native-profile-') as folder:
    stores=[]
    def create(identity):
        security=SecurityManager.for_owner(identity,timeout=5)
        security.TOOLS_ROOT_DIR=str(Path(folder)/'trusted-tool-fixtures')
        controller=UiController(lambda query:'unused',lambda:'No tools installed yet.',security,gr.update)
        controller.state.session_id=identity
        def repository(vault):
            store=SavedProfiles(Path(folder)/'profiles',vault,resolver=lambda host:['93.184.216.34'])
            stores.append(store)
            return store
        controller.model_configuration=SessionModelConfiguration(controller,lambda llm:None,store_factory=repository)
        return controller
    registry=SessionRegistry(create)
    demo=build_view(registry,gradio_module=gr).demo
    save=next(index for index,fn in demo.fns.items() if fn.fn.__name__=='profile_action' and fn.inputs[0].value=='save')
    refresh=next(index for index,fn in demo.fns.items() if fn.fn.__name__=='profile_action' and fn.inputs[0].value=='refresh')
    async def verify():
        state=SessionState(demo)
        request=gr.Request(session_hash='native-profile-owner')
        try:
            args=[None,'','Native synthetic profile','OpenAI',None,'test-model','https://api.openai.com/v1','synthetic-native-profile-test-key',None]
            result=await demo.process_api(save,args,state=state,request=request,session_hash='native-profile-owner')
            assert 'Profile saved' in result['data'][8],result['data'][8]
            record=stores[0].list()[0]
            assert WindowsCredentialVault().read(record['credential_ref'])=='synthetic-native-profile-test-key'
            args[0]=None;args[1]=record['id'];args[7]=''
            again=await demo.process_api(refresh,args,state=state,request=request,session_hash='native-profile-owner')
            assert 'Native synthetic profile' in str(again['data'][0])
            assert 'synthetic-native-profile-test-key' not in str(again['data'])
        finally:
            for store in stores:
                for record in store.list():
                    store.delete(record['id'],record['version'])
    asyncio.run(verify())
print('native-profile-callback-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "native-profile-callback-ok" in result.stdout
