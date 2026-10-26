"""Legacy CLI and workflow entrypoints backed by explicit package services."""

from typing import Any

import _agentix_path
from agentix.adapters.crewai import SECURITY_GUARDRAILS
from agentix.catalog import ToolCatalog
from agentix.settings import Settings


def __getattr__(name: str) -> Any:
    """Retain legacy agent/factory access without eager framework initialization."""
    if name in (
        "manager_agent",
        "architect_agent",
        "coder_agent",
        "tester_agent",
        "Task",
        "Crew",
        "Process",
    ):
        from agentix.bootstrap import get_default_runtime

        return getattr(get_default_runtime().orchestrator, name)
    raise AttributeError(name)


def get_installed_tools_catalog() -> str:
    """Inspect the configured catalog on demand, without constructing agents."""
    return ToolCatalog(Settings.from_environment().tools_root).render()


def build_tool_pipeline(tool_name: str, user_requirement: str) -> Any:
    """Start the original creation pipeline through the lazy default runtime."""
    from agentix.bootstrap import get_default_runtime

    return get_default_runtime().orchestrator.build_tool_pipeline(tool_name, user_requirement)


def run_system(user_query: str) -> str:
    """Process one query using the existing manager decision semantics."""
    from agentix.bootstrap import get_default_runtime

    return get_default_runtime().orchestrator.run_system(user_query)


def main() -> None:
    """Start the interactive command-line loop."""
    from agentix.cli import run_cli

    run_cli()


if __name__ == "__main__":
    main()
