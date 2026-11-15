"""Exercise real package services with explicit offline dependency wiring.

Only framework/LLM constructors and Gradio update payloads are substituted.
Artifact operations, storage, approval coordination, catalog and execution are
real; fixtures never access the project artifact directory.
"""

import logging
import os
import subprocess
import threading
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from trusted_sandbox import TrustedFixtureSandbox

from agentix import security as security_module
from agentix.adapters.crewai import build_agents, register_tools
from agentix.application.tool_workflow import Orchestrator
from agentix.controllers.state import ConsoleThoughtsCapture, ExecutionState
from agentix.controllers.tool_controller import UiController, format_thoughts_markdown
from agentix.security import SecurityManager
from agentix.storage.catalog import ToolCatalog
from agentix.storage.locations import data_directory
from agentix.tools import ArtifactTools


def agentix_file_handlers(logger: logging.Logger | None = None) -> list[logging.Handler]:
    """Return the AgentiX rotating file handlers attached to ``logger``.

    ``logger`` defaults to the root logger. The returned list is a snapshot, so
    callers may detach handlers while iterating it. Nothing is flushed, closed
    or removed here; the caller owns that decision.
    """
    target = logging.getLogger() if logger is None else logger
    return [handler for handler in target.handlers if getattr(handler, "_agentix_file_log", False)]


def release_agentix_file_handlers(
    handlers: list[logging.Handler],
    logger: logging.Logger | None = None,
    *,
    keep: tuple[logging.Handler, ...] | list[logging.Handler] = (),
) -> list[logging.Handler]:
    """Flush, close and detach owned handlers exactly once.

    Handlers in ``keep`` stay attached and open, so a session can preserve
    handlers that existed before it started. Each released handler is detached
    before it is flushed, so no record can reach it afterwards, an object listed
    twice is closed once, and an already closed handler is only detached again.
    Returns the handlers this call closed, so a repeated call returns ``[]``.
    """
    target = logging.getLogger() if logger is None else logger
    retained = {id(handler) for handler in keep}
    released: list[logging.Handler] = []
    seen: set[int] = set()
    for handler in handlers:
        identity = id(handler)
        if identity in retained or identity in seen:
            continue
        seen.add(identity)
        target.removeHandler(handler)
        if getattr(handler, "_closed", False):
            continue
        handler.flush()
        handler.close()
        released.append(handler)
    return released


@pytest.fixture(scope="session", autouse=True)
def isolated_user_storage(tmp_path_factory):
    """Keep every test away from real v5 and v7 user storage.

    Production now requires both variables, so tests must supply them. Explicit
    per-test overrides still win because monkeypatch applies afterwards. The
    resolved data root is validated against the pytest temporary root before any
    test runs, and every AgentiX file handler created during the session is
    flushed, closed and detached at teardown. Handlers that already existed are
    preserved. Raises ``RuntimeError`` when a destination escapes the temporary
    root, after the escaping handlers have been closed.
    """
    root = tmp_path_factory.mktemp("agentix-storage")
    authorized = Path(tmp_path_factory.getbasetemp()).resolve()
    previous = {name: os.environ.get(name) for name in ("AGENTIX_HOME", "AGENTIX_TOOLS_ROOT")}
    os.environ["AGENTIX_HOME"] = str(root / "home")
    os.environ["AGENTIX_TOOLS_ROOT"] = str(root / "tools")
    resolved = data_directory().resolve()
    if not resolved.is_relative_to(authorized):
        raise RuntimeError(f"Test storage escapes the pytest temporary root: {resolved}")
    logger = logging.getLogger()
    preexisting = agentix_file_handlers(logger)
    try:
        yield root
    finally:
        escaped = [
            Path(getattr(handler, "baseFilename", "")).resolve()
            for handler in agentix_file_handlers(logger)
            if id(handler) not in {id(item) for item in preexisting}
            and not Path(getattr(handler, "baseFilename", "")).resolve().is_relative_to(authorized)
        ]
        release_agentix_file_handlers(agentix_file_handlers(logger), logger, keep=preexisting)
        for name, value in previous.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value
        if escaped:
            raise RuntimeError(f"AgentiX file handlers escaped the temporary root: {escaped}")


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
