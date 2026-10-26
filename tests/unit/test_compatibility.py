"""Validate lazy legacy entrypoints against injected runtime boundaries."""

import importlib
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from agentix import bootstrap


def test_security_exception_is_exported_from_legacy_and_package_facades():
    """Public exception re-exports must survive unused-import cleanup."""
    from agentix.paths import SecurityViolationError
    from agentix.security import SecurityViolationError as PackageError
    from security_manager import SecurityViolationError as LegacyError

    assert PackageError is SecurityViolationError
    assert LegacyError is SecurityViolationError


def test_legacy_workflow_calls_share_the_injected_runtime(monkeypatch):
    """Verify legacy workflow calls share the injected runtime."""
    entry = importlib.import_module("main")
    orchestrator = Mock()
    orchestrator.run_system.return_value = "answer"
    orchestrator.build_tool_pipeline.return_value = "created"
    monkeypatch.setattr(
        bootstrap, "get_default_runtime", lambda: SimpleNamespace(orchestrator=orchestrator)
    )
    assert entry.run_system("query") == "answer"
    assert entry.build_tool_pipeline("adder", "addition") == "created"
    orchestrator.run_system.assert_called_once_with("query")
    orchestrator.build_tool_pipeline.assert_called_once_with("adder", "addition")
    assert entry.manager_agent is orchestrator.manager_agent


def test_legacy_app_exports_callbacks_without_starting_server(monkeypatch):
    """Verify legacy app exports callbacks without starting server."""
    entry = importlib.import_module("app")
    controller, view = Mock(), Mock()
    monkeypatch.setattr(bootstrap, "get_default_ui", lambda: (controller, view))
    assert entry.process_user_query is controller.process_user_query
    assert entry.demo is view.demo
    assert entry.custom_theme is view.theme


@pytest.mark.parametrize("name", ["app", "main", "config", "custom_tools"])
def test_unknown_compatibility_attribute_is_not_a_startup_request(name):
    """Verify unknown compatibility attribute is not a startup request."""
    entry = importlib.import_module(name)
    with pytest.raises(AttributeError):
        getattr(entry, "not_an_agentix_export")


def test_ui_startup_restores_stdout_on_launch_error(monkeypatch):
    """Verify ui startup restores stdout on launch error."""
    import sys

    controller = SimpleNamespace(captured_stdout=object())
    monkeypatch.setattr(bootstrap, "get_default_ui", lambda: (controller, object()))
    view_module = importlib.import_module("agentix.ui.view")
    monkeypatch.setattr(view_module, "launch", Mock(side_effect=RuntimeError("port unavailable")))
    before = sys.stdout
    with pytest.raises(RuntimeError, match="port unavailable"):
        bootstrap.run_ui()
    assert sys.stdout is before
