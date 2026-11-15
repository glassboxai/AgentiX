"""Compatibility access to lazily registered CrewAI tools.

Import alone is inert; explicitly requesting a registered tool loads CrewAI.
Framework-free operations are available in agentix.tools.ArtifactTools.
"""

from typing import Any

import _agentix_path
from agentix.security import SecurityManager
from agentix.tools import ArtifactTools

_NAMES = (
    "save_specifications_tool",
    "log_specifications_incidence_tool",
    "compile_and_save_code_tool",
    "log_coder_incidence_tool",
    "run_and_save_tests_tool",
    "log_tester_incidence_tool",
    "read_artifact_tool",
    "execute_generated_tool_tool",
)
__all__ = list(_NAMES) + ["append_structured_incidence"]


def append_structured_incidence(tool_name: str, suffix: str, title: str, details: str) -> str:
    """Preserve the non-decorated incidence helper's public contract."""
    return ArtifactTools(SecurityManager).append_structured_incidence(
        tool_name, suffix, title, details
    )


def __getattr__(name: str) -> Any:
    """Return a decorated compatibility tool without constructing any model."""
    if name in _NAMES:
        from agentix.bootstrap import get_default_tools

        return getattr(get_default_tools(), name)
    raise AttributeError(name)
