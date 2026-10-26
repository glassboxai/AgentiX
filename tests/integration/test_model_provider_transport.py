"""Opt-in installed SDK transport validation; no server or model is contacted."""

import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.frameworks


def test_native_remote_client_enforces_sync_and_async_request_guards():
    """Use synthetic credentials and check installed CrewAI transport contracts."""
    code = r"""
import _agentix_path
import asyncio
import httpx
from types import SimpleNamespace
from agentix.model_profiles import ModelProfile, create_profile_llm
profile = ModelProfile('OpenAI', 'test-model', 'https://api.openai.com/v1', 'synthetic-ref', True)
client = create_profile_llm(profile, SimpleNamespace(read=lambda ref: 'synthetic-never-sent-key'), resolver=lambda host: ['93.184.216.34'])
assert client.max_tokens == 8192 and client.timeout == 120 and client.max_retries == 0
assert client.interceptor is not None
request = httpx.Request('POST', 'https://api.openai.com/v1/chat/completions')
assert client.interceptor.on_outbound(request) is request
for url in ('http://api.openai.com/v1/chat/completions', 'https://elsewhere.example/v1/chat/completions'):
    try:
        client.interceptor.on_outbound(httpx.Request('POST', url))
    except ValueError:
        pass
    else:
        raise AssertionError('Changed request destination accepted')
try:
    client.interceptor.on_inbound(httpx.Response(302))
except ValueError:
    pass
else:
    raise AssertionError('Redirect accepted')
assert asyncio.run(client.interceptor.aon_outbound(request)) is request
sync = client._get_sync_client()
assert sync.max_retries == 0
assert not sync._client.follow_redirects
assert not sync._client._mounts, 'Environment proxies must not bypass explicit transport'
sync.close()
asyncio.run(client._get_async_client().close())
print('remote-transport-contract-ok')
"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "remote-transport-contract-ok" in result.stdout
