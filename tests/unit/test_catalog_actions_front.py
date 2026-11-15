"""Catalog action controls: selection pre-checks must open the modal dialog."""

from types import SimpleNamespace

import pytest


def _fake_gr(events):
    """Record constructor kwargs and capture every event binding's fn."""

    class Component:
        """Absorb constructor kwargs and record event registrations."""

        def __init__(self, *args, **kwargs):
            self.kwargs = kwargs

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def __getattr__(self, name):
            def event(**kwargs):
                events.append(kwargs)
                return self

            return event

    return SimpleNamespace(
        **{name: Component for name in ("Button", "State", "Column", "Markdown", "Row")},
        update=lambda **kwargs: kwargs,
    )


class _DialogStub:
    """Record modal requests without building real components."""

    def __init__(self):
        self.shown = []

    def outputs(self):
        return []

    def skip(self):
        return ("skip", "skip")

    def show(self, text):
        self.shown.append(text)
        return ("show", text)


def test_delete_prepare_requires_selection_and_opens_modal():
    """Deletion with no selection shows the friendly modal before any backend call."""
    from agentix.ui.catalog_actions import build_delete_controls

    events = []
    dialog = _DialogStub()

    class Backend:
        """Fail loudly if the backend is reached without a selection."""

        def prepare(self, kind, identity, token, request):
            raise AssertionError("backend must not be called without a selection")

    build_delete_controls(
        _fake_gr(events), Backend(), lambda fn: fn, "application", None, None, dialog=dialog
    )
    prepare = events[0]["fn"]
    row = prepare("", "token", None)
    assert row[0] == "Please, select an installed application."
    assert row[1]["visible"] is False
    assert dialog.shown == ["Please, select an installed application."]


def test_delete_backend_errors_open_the_modal_with_the_safe_message():
    """Backend validation and unexpected failures open the modal, not a toast."""
    from agentix.ui.catalog_actions import build_delete_controls

    events = []
    dialog = _DialogStub()

    class Backend:
        """Raise one validation error and one unexpected error."""

        def prepare(self, kind, identity, token, request):
            if identity == "bad":
                raise ValueError("Deletion confirmation expired or changed")
            raise RuntimeError("native details never echoed")

    build_delete_controls(
        _fake_gr(events), Backend(), lambda fn: fn, "application", None, None, dialog=dialog
    )
    prepare = events[0]["fn"]
    row = prepare("bad", "token", None)
    assert row[0] == "Deletion confirmation expired or changed"
    assert dialog.shown == ["Deletion confirmation expired or changed"]
    row = prepare("other", "token", None)
    assert dialog.shown[-1] == "Deletion unavailable; dependency or storage checks failed."


def test_delete_success_leaves_the_modal_hidden():
    """A successful prepare keeps the dialog outputs untouched."""
    from agentix.ui.catalog_actions import build_delete_controls

    events = []
    dialog = _DialogStub()

    class Backend:
        """Return a normal confirmation prompt."""

        def prepare(self, kind, identity, token, request):
            return "Confirm deletion of app", "nonce", "owned"

    build_delete_controls(
        _fake_gr(events), Backend(), lambda fn: fn, "application", None, None, dialog=dialog
    )
    prepare = events[0]["fn"]
    row = prepare("app", "token", None)
    assert row[:5] == (
        "Confirm deletion of app",
        {"visible": True},
        "Confirm deletion of app",
        "nonce",
        "owned",
    )
    assert dialog.shown == []


def test_load_and_play_reject_empty_selection_before_backend():
    """The catalog pre-check raises the friendly validation message."""
    from agentix.ui.apps_catalog import require_selected_app

    with pytest.raises(ValueError, match="Please, select an installed application."):
        require_selected_app("")
    with pytest.raises(ValueError, match="Please, select an installed application."):
        require_selected_app(None)
    require_selected_app("app-identity")
