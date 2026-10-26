"""Specify explicit startup and independent service wiring before extraction."""

from types import SimpleNamespace
from unittest.mock import Mock


def test_settings_are_immutable_and_do_not_create_storage(tmp_path):
    """Verify settings are immutable and do not create storage."""
    from agentix.settings import Settings

    settings = Settings.from_environment({}, base_dir=tmp_path)
    assert settings.model == "ollama/qwen3-coder:30b"
    assert settings.ollama_url == "http://localhost:11434"
    assert settings.tools_root == tmp_path / "generated_tools"
    assert not settings.tools_root.exists()


def test_explicit_runtime_connects_llm_agents_and_services(tmp_path):
    """Verify explicit runtime connects llm agents and services."""
    from agentix.bootstrap import create_runtime
    from agentix.settings import Settings

    llm = object()
    factory = Mock(return_value=llm)
    register = Mock(side_effect=lambda operations: SimpleNamespace(operations=operations))
    agents = SimpleNamespace(
        manager=object(),
        architect=object(),
        coder=object(),
        tester=object(),
        creation_manager=object(),
    )
    agent_factory = Mock(return_value=agents)
    backend = SimpleNamespace(
        Task=Mock(), Crew=Mock(), Process=SimpleNamespace(sequential="sequential")
    )
    runtime = create_runtime(
        Settings.from_environment({}, base_dir=tmp_path),
        llm_factory=factory,
        tool_factory=register,
        agent_factory=agent_factory,
        backend=backend,
    )
    factory.assert_called_once()
    assert agent_factory.call_args.args[0] is llm
    assert runtime.orchestrator.manager_agent is agents.manager
    assert runtime.security.TOOLS_ROOT_DIR == str(tmp_path / "generated_tools")
    assert runtime.catalog.render() == "No tools installed yet."


def test_view_binds_controller_and_preserves_launch_options():
    """Verify view binds controller and preserves launch options."""
    from agentix.ui.view import build_view, launch

    events = []

    class Component:
        """Provide Component for the enclosing trusted test fixture."""

        def __init__(self, *args, **kwargs):
            """Provide init for the enclosing trusted test fixture."""
            self.kwargs = kwargs

        def __enter__(self):
            """Provide enter for the enclosing trusted test fixture."""
            return self

        def __exit__(self, *args):
            """Provide exit for the enclosing trusted test fixture."""
            return False

        def __getattr__(self, name):
            """Provide getattr for the enclosing trusted test fixture."""

            def event(**kwargs):
                """Provide event for the enclosing trusted test fixture."""
                events.append((name, kwargs))
                return self

            return event

    gr = SimpleNamespace(
        **{
            name: Component
            for name in (
                "State",
                "Sidebar",
                "Dropdown",
                "InputHTMLAttributes",
                "Blocks",
                "Row",
                "Column",
                "Markdown",
                "HTML",
                "Chatbot",
                "Textbox",
                "Button",
                "Accordion",
                "Checkbox",
                "Group",
                "TextArea",
                "Timer",
            )
        },
        themes=SimpleNamespace(Base=Component),
        Request=type("Request", (), {}),
    )
    controller = Mock()
    controller.get_installed_tools_catalog.return_value = "No tools installed yet."
    from agentix.ui.sessions import SessionRegistry

    view = build_view(SessionRegistry(lambda session_id: controller), gradio_module=gr)
    assert any(getattr(data.get("fn"), "__name__", "") == "approve" for _, data in events)
    assert any(getattr(data.get("fn"), "__name__", "") == "poll" for _, data in events)
    launch(view)
    options = [data for name, data in events if name == "launch"][0]
    assert options["server_name"] == "127.0.0.1"
    assert options["server_port"] == 7860
    assert options["inbrowser"] is True
    assert "Inter" in options["css"]
    assert options["favicon_path"].endswith("Agentix.png")
