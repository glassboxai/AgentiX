"""Opt-in real Windows DPAPI widget record reload using trusted temporary fixtures."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from test_application_catalog import installed, registry

pytestmark = [
    pytest.mark.windows_credentials,
    pytest.mark.skipif(os.name != "nt", reason="Windows only"),
]


def test_real_widget_approval_can_be_reloaded_by_a_new_process(tmp_path):
    """No existing credential/artifact is read; metadata survives a fresh process."""
    from agentix.storage.widget_store import WidgetStore

    root = tmp_path / "trusted-tools"
    root.mkdir()
    fixture = installed(root)
    tool = registry(fixture).resolve()["count_words_in_text"]
    directory = tmp_path / "protected-records"
    service = WidgetStore(fixture.ledger.security, directory, policy="test-policy")
    service.publish(
        tool,
        {
            "widget_code": "def create_widget(context): pass",
            "tests_code": "",
            "notes": "Trusted test approval boundary",
        },
    )
    payload = {
        key: value.decode() if isinstance(value, bytes) else value
        for key, value in vars(tool).items()
    }
    script = """
import _agentix_path, json, sys
from pathlib import Path
from agentix.storage.application_catalog import ApprovedTool
from agentix.security import SecurityManager
from agentix.storage.widget_store import WidgetStore
fields=json.load(sys.stdin)
fields['code']=fields['code'].encode()
fields['tests']=fields['tests'].encode()
security=SecurityManager.for_owner('new-fixture-process')
security.TOOLS_ROOT_DIR=sys.argv[1]
store=WidgetStore(security,Path(sys.argv[2]),policy='test-policy')
print(store.load(ApprovedTool(**fields)).approved)
"""
    child = subprocess.run(
        [sys.executable, "-c", script, str(root), str(directory)],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        timeout=30,
        cwd=Path(__file__).resolve().parents[2],
    )
    assert child.returncode == 0, child.stderr
    assert child.stdout.strip() == "True"
