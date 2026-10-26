"""Test the new inert-import contract before moving legacy initialization."""

import subprocess
import sys
from pathlib import Path


def test_legacy_imports_do_not_initialize_application():
    """Compatibility imports must not need installed UI/LLM packages or storage."""
    root = Path(__file__).resolve().parents[2]
    script = """
import os, sys
from unittest.mock import Mock
before_env = dict(os.environ)
before_stdout = sys.stdout
os.makedirs = Mock(side_effect=AssertionError("import created storage"))
from pathlib import Path
Path.mkdir = Mock(side_effect=AssertionError("import created storage"))
import config, security_manager, custom_tools, main, app
import agentix.bootstrap, agentix.cli, agentix.storage, agentix.approvals
import agentix.adapters.crewai, agentix.ui.view
assert sys.stdout is before_stdout, "import replaced stdout"
assert dict(os.environ) == before_env, "import modified environment"
assert "crewai" not in sys.modules, "import loaded CrewAI"
assert "gradio" not in sys.modules, "import loaded Gradio"
print("inert")
"""
    result = subprocess.run(
        [sys.executable, "-c", script], cwd=root, capture_output=True, text=True, timeout=30
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "inert"
