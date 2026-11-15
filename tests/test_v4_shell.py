"""Real Gradio structure regressions for the integrated v4 shell."""

import pytest

from agentix.controllers.sessions import SessionRegistry
from agentix.ui.view import build_view


def ancestors(layout, identity, path=()):
    """Return component ancestors from actual Gradio layout data."""
    if layout["id"] == identity:
        return path
    for child in layout.get("children", []):
        found = ancestors(child, identity, (*path, layout["id"]))
        if found is not None:
            return found
    return None


def test_sidebar_is_shared_outside_both_tabs():
    """Catch placing model controls in one tab or duplicating their session state."""
    demo = build_view(SessionRegistry(lambda identity: None)).demo
    components = demo.config["components"]
    all_tabs = [c for c in components if c["type"] == "tabitem"]
    tabs = [
        c
        for c in all_tabs
        if not {t["id"] for t in all_tabs}.intersection(ancestors(demo.config["layout"], c["id"]))
    ]
    assert {c["props"]["label"] for c in all_tabs} == {
        "Tools",
        "Applications",
        "Tool tests",
        "Widget tests",
    }
    assert {c["props"]["label"] for c in tabs} == {"Tools", "Applications"}
    sidebars = [c for c in components if c["type"] == "sidebar"]
    # V7-068: one shared model sidebar plus one right sidebar per tab.
    assert len(sidebars) == 3
    shared = [
        c
        for c in sidebars
        if not {t["id"] for t in tabs}.intersection(ancestors(demo.config["layout"], c["id"]))
    ]
    assert len(shared) == 1
    assert shared[0]["props"]["elem_id"] == "agentix-sidebar"
    assert shared[0]["props"]["position"] == "left"
    per_tab = {
        c["props"]["elem_id"]: c
        for c in sidebars
        if c["props"].get("elem_id") in {"tools-sidebar", "applications-sidebar"}
    }
    assert set(per_tab) == {"tools-sidebar", "applications-sidebar"}
    for sidebar in per_tab.values():
        assert sidebar["props"]["position"] == "right"
        assert sidebar["props"]["open"] is False
        owners = {c["id"] for c in tabs}.intersection(
            ancestors(demo.config["layout"], sidebar["id"])
        )
        assert len(owners) == 1
    assert len([c for c in components if c["props"].get("elem_id") == "llm-provider"]) == 1
    assert len([c for c in components if c["props"].get("elem_id") == "agentix-chat"]) == 1
    assert any(c["props"].get("elem_id") == "applications-query" for c in components)


def test_tools_callback_names_remain_unambiguous():
    """Catch Applications callbacks shadowing public Tools compatibility names."""
    demo = build_view(SessionRegistry(lambda identity: None)).demo
    names = [block.fn.__name__ for block in demo.fns.values() if block.fn is not None]
    assert names.count("approve") == 1
    assert names.count("poll") == 1
    assert "application_approve" in names


def test_sidebar_uses_its_own_backend_for_profile_actions():
    """Catch retaining model-profile operations inside the Tools tab backend."""
    from agentix.controllers.sidebar import SidebarBackend
    from agentix.controllers.tools import ToolsBackend

    assert not hasattr(ToolsBackend, "configure_model")
    demo = build_view(SessionRegistry(lambda identity: None)).demo
    methods = [block.fn for block in demo.fns.values() if block.fn is not None]
    assert any(
        getattr(getattr(method, "__wrapped__", None), "__name__", "") == "profile_action"
        for method in methods
    )
    assert hasattr(SidebarBackend, "configure_model")


@pytest.mark.frameworks
def test_general_composite_callback_matches_declared_outputs(tmp_path, monkeypatch):
    """Actual Gradio callbacks must hide legacy fields and render general results."""
    from agentix.controllers.applications import ApplicationsBackend

    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path / "home"))
    sessions = SessionRegistry(lambda identity: None)
    backend = ApplicationsBackend(sessions)
    backend.data = lambda text, token, request: (
        {"calculator": 5, "random_draw": [2, 4]},
        "Completed",
        "owned",
    )
    backend.data_contract = lambda token, request: ('{"text": "Hello World!"}', "owned")
    demo = build_view(sessions, applications_backend=backend).demo
    callback = next(
        block
        for block in demo.fns.values()
        if block.fn is not None and block.fn.__name__ == "run_typed_data"
    )
    values = callback.fn("{}", None, None)
    assert len(values) == len(callback.outputs)
    assert values[2]["visible"] is False
    assert values[3]["visible"] is True
    assert "calculator" in values[3]["value"] and "5" in values[3]["value"]
    assert values[4]["visible"] is True
    assert values[4]["value"]["headers"] == ["Result", "Type", "Value"]
    assert ["calculator", "integer", "5"] in values[4]["value"]["data"]
    assert values[5] == '{"text": "Hello World!"}'
    assert values[6] == "Completed"


@pytest.mark.frameworks
def test_composite_callback_clears_stale_table_and_shows_the_contract(tmp_path, monkeypatch):
    """A rejected payload must clear named results and still explain the input schema."""
    from agentix.controllers.applications import ApplicationsBackend

    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path / "home"))
    sessions = SessionRegistry(lambda identity: None)
    backend = ApplicationsBackend(sessions)
    backend.data = lambda text, token, request: (
        None,
        "Data operation failed (JSONDecodeError): Expecting value: line 1 column 1 (char 0).",
        "owned",
    )
    backend.data_contract = lambda token, request: ("`text` (string)", "owned")
    demo = build_view(sessions, applications_backend=backend).demo
    callback = next(
        block
        for block in demo.fns.values()
        if block.fn is not None and block.fn.__name__ == "run_typed_data"
    )
    values = callback.fn("hola gola", None, None)
    assert values[2]["visible"] is False and values[3]["visible"] is False
    assert values[4]["visible"] is False and values[4]["value"]["data"] == []
    assert values[5] == "`text` (string)"
    assert "JSONDecodeError" in values[6]
