"""Exercise real package services with explicit offline dependency wiring.

Only framework/LLM constructors and Gradio update payloads are substituted.
Artifact operations, storage, approval coordination, catalog and execution are
real; fixtures never access the project artifact directory.
"""

import subprocess
import threading
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from trusted_sandbox import TrustedFixtureSandbox

from agentix import security as security_module
from agentix.adapters.crewai import build_agents, register_tools
from agentix.catalog import ToolCatalog
from agentix.orchestration import Orchestrator
from agentix.security import SecurityManager
from agentix.tools import ArtifactTools
from agentix.ui.controller import UiController, format_thoughts_markdown
from agentix.ui.state import ConsoleThoughtsCapture, ExecutionState


@pytest.fixture
def system(tmp_path):
    """Compose isolated services; constructor wiring replaces import patching."""
    root = tmp_path / "generated_tools"
    security = type(
        "TestSecurity",
        (SecurityManager,),
        {
            "TOOLS_ROOT_DIR": str(root),
            "auto_approve": False,
            "_approval_event": threading.Event(),
            "_lock": threading.Lock(),
            "_pending_request": None,
            "_edited_content": None,
            "_approval_decision": False,
        },
    )
    operations = ArtifactTools(security, sandbox=TrustedFixtureSandbox())
    backend = SimpleNamespace(
        **{
            name: Mock(side_effect=lambda **kw: SimpleNamespace(**kw))
            for name in ("Agent", "Task", "Crew")
        },
        Process=SimpleNamespace(sequential="sequential"),
    )
    registered = register_tools(operations, decorator=lambda name: lambda fn: fn)
    agents = build_agents(object(), registered, agent_factory=backend.Agent)
    catalog = ToolCatalog(root)
    orchestrator = Orchestrator(agents, backend, catalog.render, operations.verification)
    controller = UiController(
        orchestrator.run_system, catalog.render, security, update=lambda **kw: kw
    )
    return SimpleNamespace(
        root=root,
        security=security,
        security_manager=security_module,
        custom_tools=operations,
        main=orchestrator,
        app=controller,
        crewai=backend,
        threading=threading,
        test_process=subprocess,
        capture_type=ConsoleThoughtsCapture,
        state_type=ExecutionState,
        format_thoughts_markdown=format_thoughts_markdown,
    )
