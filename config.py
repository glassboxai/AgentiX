"""Legacy configuration constants with lazy model construction.

Importing constants is inert; accessing local_llm explicitly initializes the
existing provider. New code should use Settings and the composition root.
"""

from pathlib import Path
from typing import Any

import _agentix_path
from agentix.settings import Settings

BASE_DIR = str(Path(__file__).resolve().parent)
OLLAMA_MODEL = "ollama/qwen3-coder:30b"
OLLAMA_BASE_URL = "http://localhost:11434"


def __getattr__(name: str) -> Any:
    """Resolve deployment-dependent values only when specifically requested."""
    if name == "local_llm":
        from agentix.bootstrap import get_default_llm

        return get_default_llm()
    if name == "TOOLS_ROOT_DIR":
        return str(Settings.from_environment().tools_root)
    raise AttributeError(name)
