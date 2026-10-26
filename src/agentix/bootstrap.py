"""Explicit composition root for optional frameworks and application startup.

Importing this module is inert. Only startup functions configure logging and
telemetry, create storage, construct models/agents or install stdout capture.
"""

import logging
import os
from collections.abc import Callable
from dataclasses import dataclass, replace
from functools import lru_cache
from types import SimpleNamespace
from typing import Any
from uuid import uuid4

from .adapters.crewai import build_agents, register_tools
from .approval_store import ApprovalStore, user_approval_store
from .catalog import ToolCatalog
from .contracts import ExecutionBackend
from .diagnostics import activity_output, log_event
from .orchestration import Orchestrator
from .sandbox import WindowsSandbox
from .security import SecurityManager
from .settings import Settings
from .tools import ArtifactTools

logger = logging.getLogger(__name__)


def configure_process() -> None:
    """Apply the legacy startup logging/telemetry policy explicitly and safely.

    Optional vendor hooks are best-effort, matching prior behavior. The Rich
    filter is installed at most once so repeated startup cannot wrap itself.
    """
    os.environ.update(
        {
            "LITELLM_LOG": "ERROR",
            "GRADIO_ANALYTICS_ENABLED": "False",
            "OTEL_SDK_DISABLED": "true",
            "CREWAI_DISABLE_TELEMETRY": "true",
            "CREWAI_DISABLE_TRACKING": "true",
            "CREWAI_TRACING_ENABLED": "false",
        }
    )
    from .credentials import SecretFilter

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    for handler in logging.getLogger().handlers:
        if not any(isinstance(item, SecretFilter) for item in handler.filters):
            handler.addFilter(SecretFilter())
    for name in ("httpx", "litellm", "openai"):
        logging.getLogger(name).setLevel(logging.WARNING)
    try:
        from crewai.events.listeners.tracing.utils import set_suppress_tracing_messages

        set_suppress_tracing_messages(True)
    except Exception:
        logger.debug("Optional CrewAI tracing hook unavailable", exc_info=True)
    try:
        from rich.console import Console
        from rich.panel import Panel

        if not getattr(Console.print, "_agentix_filter", False):
            original_print = Console.print

            def filtered_print(console: Any, *args: Any, **kwargs: Any) -> Any:
                """Suppress only the legacy tracing panel; forward other output."""
                if any(
                    isinstance(arg, Panel) and "Tracing Status" in str(getattr(arg, "title", ""))
                    for arg in args
                ):
                    return None
                return original_print(console, *args, **kwargs)

            filtered_print._agentix_filter = True
            Console.print = filtered_print
    except Exception:
        logger.debug("Optional Rich tracing filter unavailable", exc_info=True)


def create_llm(settings: Settings) -> Any:
    """Construct the existing CrewAI LLM only when explicitly requested."""
    from crewai import LLM

    log_event(logger, "model_adapter_constructing")
    return LLM(
        model=settings.model,
        base_url=settings.ollama_url,
        temperature=settings.temperature,
        timeout=120,
        max_tokens=8192,
        max_retries=0,
    )


@dataclass(frozen=True)
class Runtime:
    """Connected services for one explicit application runtime."""

    settings: Settings
    security: Any
    operations: ArtifactTools
    catalog: ToolCatalog
    registered_tools: SimpleNamespace
    orchestrator: Orchestrator
    llm: Any


def create_runtime(
    settings: Settings,
    *,
    llm_factory: Callable = create_llm,
    tool_factory: Callable = register_tools,
    agent_factory: Callable = build_agents,
    backend: Any = None,
    security: Any = None,
    llm: Any = None,
    owner_id: str | None = None,
    sandbox: ExecutionBackend | None = None,
    approval_store: ApprovalStore | None = None,
) -> Runtime:
    """Wire services at startup, without running agents or constructing a UI.

    Injectable factories keep framework imports and external work out of service
    tests. Production process configuration is the caller's explicit decision.
    """
    if security is None:
        security = SecurityManager.for_owner(owner_id or uuid4().hex)
        security.TOOLS_ROOT_DIR = str(settings.tools_root)
    settings.tools_root.mkdir(parents=True, exist_ok=True)
    # Select one process boundary at the composition root and share it.
    execution_backend = sandbox if sandbox is not None else WindowsSandbox()
    operations = ArtifactTools(
        security,
        sandbox=execution_backend,
        approval_store=approval_store
        if approval_store is not None
        else (user_approval_store(settings.tools_root) if sandbox is None else None),
    )
    catalog = ToolCatalog(settings.tools_root)
    model = llm_factory(settings) if llm is None else llm
    registered = tool_factory(operations)
    agents = agent_factory(model, registered)
    if backend is None:
        import crewai as backend
    orchestrator = Orchestrator(agents, backend, catalog.render, operations.verification)
    log_event(logger, "runtime_composed")
    return Runtime(settings, security, operations, catalog, registered, orchestrator, model)


@lru_cache(maxsize=1)
def get_default_llm() -> Any:
    """Lazily provide the compatibility model, applying startup policy first."""
    configure_process()
    return create_llm(Settings.from_environment())


@lru_cache(maxsize=1)
def get_default_runtime() -> Runtime:
    """Provide the single legacy runtime on first explicit workflow access."""
    # Sharing this facade preserves legacy SecurityManager toggles/approvals.
    return create_runtime(
        Settings.from_environment(), security=SecurityManager, llm=get_default_llm()
    )


@lru_cache(maxsize=1)
def get_default_tools() -> SimpleNamespace:
    """Register legacy tools without creating an LLM or running any agents."""
    configure_process()
    return register_tools(ArtifactTools(SecurityManager))


@lru_cache(maxsize=1)
def get_default_ui() -> tuple[Any, Any]:
    """Build the session-aware view and a separate legacy compatibility controller."""
    from .ui.controller import UiController
    from .ui.view import build_view

    runtime = get_default_runtime()
    import gradio as gr

    controller = UiController(
        runtime.orchestrator.run_system,
        runtime.catalog.render,
        runtime.security,
        gr.update,
        validation=runtime.operations.acceptance,
    )
    from .ui.sessions import SessionRegistry

    def create_session(session_id: str) -> UiController:
        """Create independent role objects, approvals and controller for one browser."""
        # Mutable provider clients and agents belong to one session. The Ollama
        # service may still share its resident model weights behind these clients.
        # Legacy CLI environment overrides must not authorize remote GUI task transfer.
        local_settings = replace(
            runtime.settings, model="ollama/qwen3-coder:30b", ollama_url="http://127.0.0.1:11434"
        )
        owned_runtime = create_runtime(local_settings, owner_id=session_id)
        owned_controller = UiController(
            owned_runtime.orchestrator.run_system,
            owned_runtime.catalog.render,
            owned_runtime.security,
            gr.update,
            validation=owned_runtime.operations.acceptance,
        )
        from pathlib import Path

        from .model_profiles import SessionModelConfiguration
        from .profile_store import SavedProfiles

        owned_controller.state.session_id = session_id
        owned_controller.model_configuration = SessionModelConfiguration(
            owned_controller,
            lambda client: create_runtime(
                local_settings,
                owner_id=session_id,
                security=owned_controller.security,
                llm=client,
            ),
            store_factory=lambda vault: SavedProfiles(
                Path(
                    os.path.realpath(
                        os.path.join(
                            os.environ["LOCALAPPDATA"], "AgentiX", "v3", "data", "model-profiles"
                        )
                    )
                ),
                vault,
            ),
        )
        return owned_controller

    view = build_view(SessionRegistry(create_session), gradio_module=gr)
    return controller, view


def run_ui() -> None:
    """Install capture and launch the existing UI; always restore host stdout."""
    from .ui.view import launch

    controller, view = get_default_ui()
    with activity_output():
        log_event(logger, "ui_launching")
        settings = get_default_runtime().settings
        launch(view, server_port=settings.server_port, open_browser=settings.open_browser)
