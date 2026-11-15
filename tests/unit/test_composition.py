"""Specify explicit startup and independent service wiring before extraction."""

import logging
from types import SimpleNamespace
from unittest.mock import Mock


def test_settings_are_immutable_and_do_not_create_storage(tmp_path):
    """Verify settings are immutable and do not create storage."""
    from agentix.settings import Settings

    settings = Settings.from_environment(
        {
            "AGENTIX_HOME": str(tmp_path / "deployment"),
            "AGENTIX_TOOLS_ROOT": str(tmp_path / "deployment/data/tools"),
        },
        base_dir=tmp_path,
    )
    assert settings.model == "ollama/qwen3-coder:30b"
    assert settings.ollama_url == "http://localhost:11434"
    assert settings.tools_root == tmp_path / "deployment/data/tools"
    assert not settings.tools_root.exists()


def test_settings_keep_non_artifact_state_under_home_when_tools_are_external(tmp_path):
    """IAC-010: an external artifact root does not relocate drafts into the checkout."""
    from agentix.settings import Settings

    home = tmp_path / "agentix-data" / "v7"
    tools = tmp_path / "checkout" / "generated_tools"
    settings = Settings.from_environment(
        {"AGENTIX_HOME": str(home), "AGENTIX_TOOLS_ROOT": str(tools)}, base_dir=tmp_path
    )

    assert settings.tools_root == tools
    assert settings.data_root == home / "data"


def test_explicit_runtime_connects_llm_agents_and_services(tmp_path, caplog):
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
    with caplog.at_level(logging.DEBUG):
        runtime = create_runtime(
            Settings.from_environment(
                {
                    "AGENTIX_HOME": str(tmp_path / "deployment"),
                    "AGENTIX_TOOLS_ROOT": str(tmp_path / "deployment/data/tools"),
                },
                base_dir=tmp_path,
            ),
            llm_factory=factory,
            tool_factory=register,
            agent_factory=agent_factory,
            backend=backend,
        )
    factory.assert_called_once()
    assert agent_factory.call_args.args[0] is llm
    assert runtime.orchestrator.manager_agent is agents.manager
    assert runtime.security.TOOLS_ROOT_DIR == str(tmp_path / "deployment/data/tools")
    assert runtime.catalog.render() == "No tools installed yet."
    assert "event=runtime_composition_started" in caplog.text
    assert "event=runtime_execution_backend_selected" in caplog.text


def test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout(tmp_path):
    """IAC-010: runtime wiring must not derive draft storage from an external tool root."""
    from agentix.bootstrap import create_runtime
    from agentix.settings import Settings

    home = tmp_path / "agentix-data" / "v7"
    tools = tmp_path / "checkout" / "generated_tools"
    settings = Settings.from_environment(
        {"AGENTIX_HOME": str(home), "AGENTIX_TOOLS_ROOT": str(tools)}, base_dir=tmp_path
    )
    security = SimpleNamespace(TOOLS_ROOT_DIR="", strict_tool_contract=False, owner_id="fixture")
    security.configure_tool_storage = Mock()
    agents = SimpleNamespace(
        manager=object(),
        architect=object(),
        coder=object(),
        tester=object(),
        creation_manager=object(),
    )
    backend = SimpleNamespace(
        Task=Mock(), Crew=Mock(), Process=SimpleNamespace(sequential="sequential")
    )

    create_runtime(
        settings,
        llm=object(),
        tool_factory=Mock(return_value=SimpleNamespace()),
        agent_factory=Mock(return_value=agents),
        backend=backend,
        security=security,
        sandbox=object(),
    )

    security.configure_tool_storage.assert_called_once_with(tools, home / "data" / "drafts")


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
                "Tabs",
                "Tab",
                "JSON",
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
                "CheckboxGroup",
                "ColorPicker",
                "Group",
                "TextArea",
                "Code",
                "Number",
                "Dataframe",
                "Timer",
            )
        },
        themes=SimpleNamespace(Base=Component),
        Request=type("Request", (), {}),
    )
    controller = Mock()
    controller.get_installed_tools_catalog.return_value = "No tools installed yet."
    from agentix.controllers.sessions import SessionRegistry

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
