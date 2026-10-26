"""V3-001 regressions for explicit policy, release identity and backend injection."""

from types import SimpleNamespace
from unittest.mock import Mock


def test_explicit_startup_disables_gradio_analytics(monkeypatch):
    """Apply the same no-analytics policy to normal startup and test launchers."""
    from agentix.bootstrap import configure_process

    monkeypatch.setenv("GRADIO_ANALYTICS_ENABLED", "True")
    configure_process()
    assert __import__("os").environ["GRADIO_ANALYTICS_ENABLED"] == "False"


def test_composition_injects_one_execution_boundary_into_all_services(tmp_path):
    """Use a caller-provided boundary instead of constructing an implicit backend."""
    from agentix.bootstrap import create_runtime
    from agentix.settings import Settings

    agents = SimpleNamespace(
        manager=object(),
        architect=object(),
        coder=object(),
        tester=object(),
        creation_manager=object(),
    )
    boundary = object()
    runtime = create_runtime(
        Settings.from_environment({}, base_dir=tmp_path),
        llm=object(),
        tool_factory=lambda operations: SimpleNamespace(),
        agent_factory=lambda model, tools: agents,
        backend=SimpleNamespace(
            Task=Mock(), Crew=Mock(), Process=SimpleNamespace(sequential="sequential")
        ),
        sandbox=boundary,
    )
    assert runtime.operations.executor.sandbox is boundary
    assert runtime.operations.runner.sandbox is boundary
    assert runtime.operations.acceptance.sandbox is boundary


def test_release_identity_is_v3():
    """Identify the curated release while retaining its public import package."""
    from agentix import __version__

    assert __version__ == "3.0.0"
