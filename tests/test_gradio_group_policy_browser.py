"""Real Gradio callback/DOM regression for maintained structural-ID policy."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.browser


def test_callback_updates_do_not_duplicate_structural_ids():
    """Catch repeated DOM IDs after count/null updates without changing model source."""
    root = Path(__file__).resolve().parents[1]
    process = subprocess.run(
        [sys.executable, str(root / "tools/probe_group_ids.py")],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=60,
        env=dict(os.environ),
    )
    assert process.returncode == 0, process.stderr
    result = json.loads((root / "docs/reports/v4-group-id-probe.json").read_bytes())
    assert result["duplicates"] == {}
