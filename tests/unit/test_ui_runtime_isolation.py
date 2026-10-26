"""Verify production session composition does not reuse mutable provider clients."""

import sys
from types import ModuleType, SimpleNamespace
from uuid import uuid4

from agentix import bootstrap


def test_default_view_creates_independent_runtime_clients(monkeypatch, tmp_path):
    """Verify default view creates independent runtime clients."""
    bootstrap.get_default_ui.cache_clear()
    from agentix.settings import Settings

    shared = SimpleNamespace(identity="legacy-client")
    legacy = SimpleNamespace(
        settings=Settings(tmp_path, tmp_path / "trusted-fixture-tools"),
        security=SimpleNamespace(),
        orchestrator=SimpleNamespace(run_system=lambda query: "legacy"),
        catalog=SimpleNamespace(render=lambda: "catalog"),
        operations=SimpleNamespace(acceptance=object()),
    )
    monkeypatch.setattr(bootstrap, "get_default_runtime", lambda: legacy)
    monkeypatch.setattr(bootstrap, "get_default_llm", lambda: shared)

    def runtime(settings, **kwargs):
        """Provide runtime for the enclosing trusted test fixture."""
        client = kwargs.get("llm") or SimpleNamespace(identity=uuid4().hex)
        return SimpleNamespace(
            security=SimpleNamespace(owner_id=kwargs["owner_id"]),
            orchestrator=SimpleNamespace(run_system=lambda query: client.identity),
            catalog=SimpleNamespace(render=lambda: "catalog"),
            operations=SimpleNamespace(acceptance=object()),
        )

    monkeypatch.setattr(bootstrap, "create_runtime", runtime)
    gradio = ModuleType("gradio")
    gradio.update = lambda **kw: kw
    monkeypatch.setitem(sys.modules, "gradio", gradio)
    monkeypatch.setattr("agentix.ui.view.build_view", lambda registry, **kwargs: registry)
    try:
        _, registry = bootstrap.get_default_ui()
        first, second = registry.resolve(None, "browser-a"), registry.resolve(None, "browser-b")
        assert first.controller.run_system("query") != second.controller.run_system("query")
        assert first.controller.security is not second.controller.security
    finally:
        bootstrap.get_default_ui.cache_clear()


def test_gui_sessions_start_local_despite_legacy_remote_environment(monkeypatch, tmp_path):
    """Legacy configuration cannot activate an external GUI model without consent."""
    from agentix.settings import Settings

    bootstrap.get_default_ui.cache_clear()
    settings = Settings(
        tmp_path,
        tmp_path / "trusted-fixture-tools",
        model="openai/remote-model",
        ollama_url="https://external.example",
    )
    legacy = SimpleNamespace(
        settings=settings,
        security=SimpleNamespace(),
        orchestrator=SimpleNamespace(run_system=lambda query: "legacy"),
        catalog=SimpleNamespace(render=lambda: "catalog"),
        operations=SimpleNamespace(acceptance=object()),
    )
    calls = []

    def create(settings, **kwargs):
        """Capture the provider settings handed to each actual session factory."""
        calls.append(settings)
        return SimpleNamespace(
            security=SimpleNamespace(),
            orchestrator=SimpleNamespace(run_system=lambda query: "local"),
            catalog=SimpleNamespace(render=lambda: "catalog"),
            operations=SimpleNamespace(acceptance=object()),
        )

    monkeypatch.setattr(bootstrap, "get_default_runtime", lambda: legacy)
    monkeypatch.setattr(bootstrap, "create_runtime", create)
    gradio = ModuleType("gradio")
    gradio.update = lambda **kwargs: kwargs
    monkeypatch.setitem(sys.modules, "gradio", gradio)
    monkeypatch.setattr("agentix.ui.view.build_view", lambda registry, **kwargs: registry)
    try:
        _, registry = bootstrap.get_default_ui()
        registry.resolve(None, "fresh-browser")
        assert calls[0].model == "ollama/qwen3-coder:30b"
        assert calls[0].ollama_url == "http://127.0.0.1:11434"
    finally:
        bootstrap.get_default_ui.cache_clear()
