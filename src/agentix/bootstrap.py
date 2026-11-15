"""Explicit composition root for optional frameworks and application startup.

Importing this module is inert. Only startup functions configure logging and
telemetry, create storage, construct models/agents or install stdout capture.
"""

import logging
import os
from collections.abc import Callable
from dataclasses import dataclass, replace
from functools import lru_cache, partial
from types import SimpleNamespace
from typing import Any
from uuid import uuid4

from agentix.adapters.crewai import build_agents, register_tools
from agentix.application.tool_workflow import Orchestrator
from agentix.diagnostics import activity_output, log_event
from agentix.domain.contracts import ExecutionBackend
from agentix.sandbox import WindowsSandbox
from agentix.security import SecurityManager
from agentix.security.approval_store import ApprovalStore, user_approval_store
from agentix.settings import Settings
from agentix.storage.catalog import ToolCatalog
from agentix.tools import ArtifactTools

logger = logging.getLogger(__name__)


def _install_file_log() -> None:
    """Attach one bounded rotating file handler under data/logs, at most once.

    Payload-free event lines persist across restarts so operators can diagnose
    failed operations after the console closes. Best-effort: a missing or
    unwritable home never blocks startup.
    """
    root = logging.getLogger()
    if any(getattr(handler, "_agentix_file_log", False) for handler in root.handlers):
        return
    try:
        from logging.handlers import RotatingFileHandler

        from agentix.storage.locations import data_directory

        folder = data_directory() / "logs"
        folder.mkdir(parents=True, exist_ok=True)
        handler = RotatingFileHandler(
            folder / "agentix.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )
    except Exception:
        logger.debug("File logging unavailable", exc_info=True)
        return
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
    )
    handler._agentix_file_log = True
    root.addHandler(handler)


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
    from agentix.security.credentials import SecretFilter

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # basicConfig is a no-op when handlers already exist; keep events visible.
    if logging.getLogger().level > logging.INFO:
        logging.getLogger().setLevel(logging.INFO)
    _install_file_log()
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
    log_event(logger, "runtime_composition_started", level=logging.DEBUG)
    from agentix.storage.locations import require_v7_namespace

    require_v7_namespace(settings.tools_root, "tools_root")
    if settings.data_root is not None:
        require_v7_namespace(settings.data_root, "data_root")
    if security is None:
        security = SecurityManager.for_owner(owner_id or uuid4().hex)
        security.TOOLS_ROOT_DIR = str(settings.tools_root)
    configure_storage = getattr(security, "configure_tool_storage", None)
    if callable(configure_storage):
        drafts_root = (settings.data_root or settings.tools_root.parent) / "drafts"
        configure_storage(settings.tools_root, drafts_root)
    settings.tools_root.mkdir(parents=True, exist_ok=True)
    # Select one process boundary at the composition root and share it.
    execution_backend = sandbox if sandbox is not None else WindowsSandbox()
    log_event(logger, "runtime_execution_backend_selected", level=logging.DEBUG)
    if security is not SecurityManager:
        security.strict_tool_contract = sandbox is None
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
    from agentix.application.app_invocation import AppInvocation
    from agentix.storage.application_catalog import CatalogToolRegistry
    from agentix.storage.installed_apps import InstalledApps

    applications = (
        AppInvocation(
            InstalledApps.for_user(), CatalogToolRegistry(catalog, operations.verification)
        )
        if sandbox is None
        else None
    )
    from agentix.application.tool_routing import RoutingModelClient, ToolRouter
    from agentix.storage.locations import data_directory

    router = (
        ToolRouter(
            catalog, data_directory() / "routing", lambda evidence: RoutingModelClient(model)
        )
        if sandbox is None and security is not SecurityManager
        else None
    )
    orchestrator = Orchestrator(
        agents,
        backend,
        catalog.render,
        operations.verification,
        applications=applications,
        router=router,
        operations=operations,
    )
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
def get_default_ui(
    *,
    application_coordinator_factory: Callable | None = None,
    retrieval_service_factory: Callable | None = None,
) -> tuple[Any, Any]:
    """Build the session-owned view with optional explicit application-model wiring.

    The default transport retains its normal resource bounds. Validation launchers
    may inject a bounded client factory without changing other GUI processes or
    replacing model, approval, native execution or session ownership boundaries.
    """
    from agentix.controllers.tool_controller import UiController
    from agentix.ui.view import build_view

    runtime = get_default_runtime()
    import gradio as gr

    controller = UiController(
        runtime.orchestrator.run_system,
        runtime.catalog.render,
        runtime.security,
        gr.update,
        validation=runtime.operations.acceptance,
        tool_operations=runtime.operations,
    )
    from agentix.controllers.sessions import SessionRegistry

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
            tool_operations=owned_runtime.operations,
        )
        from agentix.models.model_profiles import SessionModelConfiguration
        from agentix.storage.locations import data_directory
        from agentix.storage.profile_store import SavedProfiles

        owned_controller.state.session_id = session_id
        owned_controller.model_configuration = SessionModelConfiguration(
            owned_controller,
            lambda client: create_runtime(
                local_settings,
                owner_id=session_id,
                security=owned_controller.security,
                llm=client,
            ),
            client=owned_runtime.llm,
            store_factory=lambda vault: SavedProfiles(
                data_directory() / "model-profiles",
                vault,
            ),
        )
        return owned_controller

    sessions = SessionRegistry(create_session)
    from agentix.application.app_workflow import ApplicationPipeline
    from agentix.controllers.applications import ApplicationsBackend
    from agentix.host_requirements import HostRequirements
    from agentix.retrieval.gui import GuiToolRetrieval

    retrieval = (retrieval_service_factory or GuiToolRetrieval)()
    retrieval.initialize(runtime.catalog)
    application_options = {}
    if application_coordinator_factory is not None:
        application_options["pipeline_factory"] = partial(
            ApplicationPipeline, coordinator_factory=application_coordinator_factory
        )
    applications = ApplicationsBackend(
        sessions,
        retrieval=retrieval,
        host_requirements=HostRequirements(),
        **application_options,
    )
    view = build_view(sessions, gradio_module=gr, applications_backend=applications)
    return controller, view


def run_ui() -> None:
    """Install capture and launch the existing UI; always restore host stdout."""
    from agentix.ui.view import launch

    controller, view = get_default_ui()
    with activity_output():
        log_event(logger, "ui_launching")
        settings = get_default_runtime().settings
        launch(view, server_port=settings.server_port, open_browser=settings.open_browser)
