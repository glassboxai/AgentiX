"""V7-068: each tab owns a right-hand sidebar for its catalog, validation and review controls."""

from types import SimpleNamespace
from unittest.mock import Mock

import pytest

TOOLS_SIDEBAR_WIDTH = 420
APPLICATIONS_SIDEBAR_WIDTH = 380
MINIMUM_SIDEBAR_WIDTH = 280


class Registry:
    """Record component creation, nesting and event wiring without a browser."""

    def __init__(self) -> None:
        """Start an empty creation log and an empty container stack."""
        self.created: list = []
        self.parents: dict[int, int | None] = {}
        self.stack: list[int] = []
        self._identities = 0

    def next_identity(self) -> int:
        """Return a stable component identity for nesting assertions."""
        self._identities += 1
        return self._identities

    def factory(self, name: str):
        """Return a Gradio-like constructor that records its parent container."""

        def build(*args, **kwargs):
            return Component(self, name, *args, **kwargs)

        return build

    def by_elem_id(self, elem_id: str):
        """Return the single component carrying an exact maintained element id."""
        matches = [item for item in self.created if item.kwargs.get("elem_id") == elem_id]
        assert len(matches) == 1, f"expected one #{elem_id}, found {len(matches)}"
        return matches[0]

    def is_inside(self, child, ancestor) -> bool:
        """Walk recorded parents to prove real container nesting."""
        current = self.parents[child.identity]
        while current is not None:
            if current == ancestor.identity:
                return True
            current = self.parents[current]
        return False


class Component:
    """Minimal Gradio component double supporting context managers and event wiring."""

    def __init__(self, registry: Registry, name: str, *args, **kwargs) -> None:
        """Record the component and the container that currently owns it."""
        self.registry = registry
        self.name = name
        self.kwargs = kwargs
        self.identity = registry.next_identity()
        registry.created.append(self)
        registry.parents[self.identity] = registry.stack[-1] if registry.stack else None

    def __enter__(self):
        """Push this component as the active container."""
        self.registry.stack.append(self.identity)
        return self

    def __exit__(self, *args):
        """Pop the active container without suppressing exceptions."""
        self.registry.stack.pop()
        return False

    def __getattr__(self, name):
        """Absorb any Gradio event registration and return this component."""

        def event(*args, **kwargs):
            return self

        return event


def _gradio(registry: Registry) -> SimpleNamespace:
    """Build the component surface used by the two tab frontends."""
    names = (
        "Accordion",
        "Button",
        "Chatbot",
        "Checkbox",
        "CheckboxGroup",
        "Code",
        "ColorPicker",
        "Column",
        "Dataframe",
        "Dropdown",
        "Group",
        "HTML",
        "JSON",
        "Markdown",
        "Number",
        "Row",
        "Sidebar",
        "State",
        "Tab",
        "Tabs",
        "TextArea",
        "Textbox",
        "Timer",
    )
    return SimpleNamespace(
        **{name: registry.factory(name) for name in names},
        update=lambda **kwargs: kwargs,
        skip=lambda: None,
        Request=type("Request", (), {}),
    )


def _bind(handler, **kwargs):
    """Keep the handler identity so event names remain assertable."""
    return handler


def _dialog(gr: SimpleNamespace):
    """Use the real modal so its own components participate in nesting checks."""
    from agentix.ui.message_dialog import MessageDialog

    return MessageDialog(gr)


def _build_tools(registry: Registry, gr: SimpleNamespace) -> None:
    """Render the Tools tab with catalog maintenance enabled."""
    from agentix.ui.tools import build_tools_frontend

    maintenance = SimpleNamespace(
        choices=Mock(), reveal=Mock(), prepare=Mock(), confirm=Mock(), cancel=Mock()
    )
    build_tools_frontend(
        gr,
        Mock(),
        _bind,
        Component(registry, "State"),
        Component(registry, "State"),
        maintenance=maintenance,
        dialog=_dialog(gr),
    )


def _build_applications(registry: Registry, gr: SimpleNamespace) -> None:
    """Render the Applications tab with catalog maintenance enabled."""
    from agentix.ui.applications import build_applications_frontend

    backend = Mock()
    backend.sessions = object()
    backend.retrieval.startup_message = "Search for candidates."
    maintenance = SimpleNamespace(
        choices=Mock(), reveal=Mock(), prepare=Mock(), confirm=Mock(), cancel=Mock()
    )
    build_applications_frontend(
        gr,
        backend,
        _bind,
        Component(registry, "State"),
        maintenance=maintenance,
        dialog=_dialog(gr),
    )


def test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review():
    """The Tools catalog, validation and review live in one collapsible right sidebar."""
    registry = Registry()
    gr = _gradio(registry)
    _build_tools(registry, gr)

    sidebar = registry.by_elem_id("tools-sidebar")
    assert sidebar.name == "Sidebar"
    assert sidebar.kwargs["position"] == "right"
    assert sidebar.kwargs["open"] is False
    assert sidebar.kwargs["width"] == TOOLS_SIDEBAR_WIDTH
    for elem_id in (
        "tools-reveal",
        "installed-tool-selection",
        "tools-delete",
        "validation-panel",
        "authorization-review",
    ):
        assert registry.is_inside(registry.by_elem_id(elem_id), sidebar), elem_id
    assert not registry.is_inside(registry.by_elem_id("agentix-chat"), sidebar)


def test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog():
    """The installed-app catalog, its refresh and explorer actions live in the right sidebar."""
    registry = Registry()
    gr = _gradio(registry)
    _build_applications(registry, gr)

    sidebar = registry.by_elem_id("applications-sidebar")
    assert sidebar.name == "Sidebar"
    assert sidebar.kwargs["position"] == "right"
    assert sidebar.kwargs["open"] is False
    assert sidebar.kwargs["width"] == APPLICATIONS_SIDEBAR_WIDTH
    for elem_id in (
        "apps-reveal",
        "installed-apps",
        "installed-apps-refresh",
        "apps-delete",
        "application-candidates-panel",
    ):
        assert registry.is_inside(registry.by_elem_id(elem_id), sidebar), elem_id
    assert not registry.is_inside(registry.by_elem_id("applications-query"), sidebar)


def test_both_tabs_keep_one_sidebar_each_and_no_second_column():
    """Each tab owns exactly one right sidebar; the work area is no longer split in two."""
    registry = Registry()
    gr = _gradio(registry)
    _build_tools(registry, gr)
    _build_applications(registry, gr)

    sidebars = [item for item in registry.created if item.name == "Sidebar"]
    assert sorted(item.kwargs["elem_id"] for item in sidebars) == [
        "applications-sidebar",
        "tools-sidebar",
    ]
    assert all(item.kwargs["position"] == "right" for item in sidebars)


@pytest.mark.parametrize("width", [TOOLS_SIDEBAR_WIDTH, APPLICATIONS_SIDEBAR_WIDTH])
def test_approved_sidebar_widths_stay_above_the_resize_minimum(width):
    """Approved defaults must be reachable by the maintained resize minimum."""
    assert width >= MINIMUM_SIDEBAR_WIDTH


def test_sidebar_resizer_has_no_maximum_width():
    """The user may widen a tab sidebar without an upper bound."""
    from agentix.ui.branding import launch_options

    script = launch_options()["js"]
    assert "MAXIMUM" not in script
    assert "VIEWPORT_SHARE" not in script
    assert "aria-valuemax" not in script
    assert "Math.max(value, MINIMUM)" in script


def test_left_sidebar_is_not_resizable_and_owns_its_overlap():
    """V7-070: the shared model sidebar keeps its fixed width and native padding."""
    from agentix.ui.branding import launch_options, stylesheet

    script = launch_options()["js"]
    css = stylesheet()
    assert "id: 'agentix-sidebar'" not in script
    assert "#agentix-sidebar .agentix-sidebar-resizer" not in css
    assert "#agentix-sidebar:not(.open) .agentix-sidebar-resizer" not in css
    assert "const syncOverlap = () => {" in script
    assert "width - offset + 30" in script


def test_right_sidebars_keep_a_small_inset_from_the_workspace():
    """V7-070/V7-071: both tab panels pad their content and keep a real gap."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    rule = css.split("#applications-sidebar .sidebar-content { padding:", 1)[1].split("}", 1)[0]
    assert rule.strip() == "22px 22px 22px 40px;"
    assert (
        "#tools-sidebar .sidebar-content,\n#applications-sidebar .sidebar-content { padding:" in css
    )
    assert "right: var(--agentix-sidebar-gap) !important;" in css
    assert "--agentix-sidebar-gap: 12px;" in css


def test_tools_legend_sits_below_the_application_toolbar():
    """The legend must render under play/edit/close, not over the canvas top-left."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    legend = css.split("#application-color-legend", 1)[1].split("}", 1)[0]
    assert "position: absolute;" in legend
    assert "top: 48px;" in legend
    assert "right: 12px;" in legend
    assert "position: fixed;" not in legend


def test_browser_title_has_no_version_suffix():
    """The browser tab must read AgentiX, not the inherited v5 label."""
    from agentix.controllers.sessions import SessionRegistry
    from agentix.ui.view import build_view

    view = build_view(SessionRegistry(lambda identity: None))
    assert view.demo.title == "AgentiX"


def test_tab_sidebars_are_contained_by_their_tab_not_the_viewport():
    """Catch a fixed full-height overlay that covers the header and the tab bar."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert "#tools-sidebar,\n#applications-sidebar {\n  position: absolute !important;" in css
    assert "right: calc(var(--agentix-sidebar-width, 420px) * -1) !important;" in css
    assert "transform: none !important;" in css
    assert (
        "#tools-sidebar.open,\n#applications-sidebar.open { right: var(--agentix-sidebar-gap) !important; }"
        in css
    )
    assert "#tools-tab,\n#applications-tab { --agentix-sidebar-gap: 12px; }" in css
    assert "#tools-tab { overflow-x: clip; }" in css
    assert "#applications-tab { overflow-x: clip; }" in css
    assert "#tools-tab > .column:has(> #tools-sidebar.open) > #agentix-workspace," in css
    assert "padding-right: calc(" in css
    assert "var(--agentix-sidebar-width, 420px) + var(--agentix-sidebar-gap) * 2" in css
    assert "var(--agentix-sidebar-width, 380px) + var(--agentix-sidebar-gap) * 2" in css
    assert ".wrap.sidebar-parent:has(#tools-sidebar.open)," in css


def test_widgets_paint_above_the_tools_legend():
    """A generated widget must never be covered by the tools color legend."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert "z-index: 1;" in css.split("#application-color-legend", 1)[1].split("}", 1)[0]
    assert '.application-layout-active [id^="application_"] {z-index: 2;}' in css


def test_right_sidebar_assets_are_registered_for_the_browser():
    """Styling and the resize behavior ship with the maintained launch options."""
    from agentix.ui.branding import launch_options, stylesheet

    css = stylesheet()
    for elem_id in ("#tools-sidebar", "#applications-sidebar"):
        assert elem_id in css
    assert "agentix-sidebar-resizer" in css
    options = launch_options()
    assert "agentix-sidebar-resizer" in options["js"]
    assert "--agentix-sidebar-width" in options["js"]
