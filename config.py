"""Legacy configuration constants with lazy model construction.

Importing constants is inert; accessing local_llm explicitly initializes the
existing provider. New code should use Settings and the composition root.
"""

from typing import Any

import _agentix_path
from agentix.settings import Settings

_settings = Settings.from_environment()
BASE_DIR = str(_settings.base_dir)
TOOLS_ROOT_DIR = str(_settings.tools_root)
OLLAMA_MODEL = _settings.model
OLLAMA_BASE_URL = _settings.ollama_url


def __getattr__(name: str) -> Any:
    """Resolve the former eager local_llm only when specifically requested."""
    if name == "local_llm":
        from agentix.bootstrap import get_default_llm

        return get_default_llm()
    raise AttributeError(name)
