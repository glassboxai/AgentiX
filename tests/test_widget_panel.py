"""LAB-004 per-browser preview lifecycle using a boundary double, not native execution."""

import pytest

from agentix.lab.widget_panel import WidgetPanel, iframe_html


class Preview:
    """A finite listener/process boundary double with observable ownership."""

    def __init__(self):
        self.url = "http://127.0.0.1:50001/"
        self.alive = True

    def close(self):
        self.alive = False


def test_panel_reuses_only_own_live_preview_and_closes_only_owner():
    """Catch cross-session sharing and accidental sibling shutdown."""
    panel = WidgetPanel(lambda: object(), lambda approved, origin: Preview())
    first = panel.open("first", "http://127.0.0.1:7874")
    second = panel.open("second", "http://127.0.0.1:7874")
    assert first is panel.open("first", "http://127.0.0.1:7874")
    assert first is not second
    panel.close("first")
    assert not first.alive and second.alive
    panel.close_all()
    assert not second.alive


def test_panel_capacity_and_expiry_reopen():
    """Catch unbounded workers and stale dead-preview reuse."""
    panel = WidgetPanel(lambda: object(), lambda approved, origin: Preview(), capacity=1)
    first = panel.open("first", "http://127.0.0.1:7874")
    with pytest.raises(RuntimeError):
        panel.open("second", "http://127.0.0.1:7874")
    first.close()
    assert panel.open("first", "http://127.0.0.1:7874") is not first
    panel.close_all()


@pytest.mark.parametrize(
    "url",
    ["https://untrusted.example/", "javascript:alert(1)", 'http://127.0.0.1:1234/" onload="bad'],
)
def test_iframe_rejects_nonlocal_or_injected_urls(url):
    """Only supervisor-created loopback URLs can enter the maintained HTML."""
    with pytest.raises(ValueError):
        iframe_html(url)


def test_iframe_never_accepts_a_display_name_parameter():
    """The isolated page titles itself from its snapshot; the frame carries only the URL."""
    with pytest.raises(TypeError):
        iframe_html("http://127.0.0.1:50461/", application_name="Vowel counter")
    assert 'src="http://127.0.0.1:50461/"' in iframe_html("http://127.0.0.1:50461/")


def test_expired_other_owner_does_not_exhaust_capacity():
    """A dead session must not prevent another browser from opening the widget."""
    panel = WidgetPanel(lambda: object(), lambda approved, origin: Preview(), capacity=1)
    first = panel.open("first", "http://127.0.0.1:7874")
    first.close()
    try:
        assert panel.open("second", "http://127.0.0.1:7874").alive
    finally:
        panel.close_all()


def test_close_during_startup_never_publishes_or_leaks_worker():
    """A late startup cannot recreate a widget after its owner clicked Close."""
    import threading

    entered, release = threading.Event(), threading.Event()
    created, errors = [], []

    def start(approved, origin):
        entered.set()
        assert release.wait(5)
        preview = Preview()
        created.append(preview)
        return preview

    panel = WidgetPanel(lambda: object(), start)

    def open_widget():
        try:
            panel.open("owner", "http://127.0.0.1:7874")
        except RuntimeError as error:
            errors.append(type(error).__name__)

    thread = threading.Thread(target=open_widget)
    thread.start()
    try:
        assert entered.wait(5)
        panel.close("owner")
    finally:
        release.set()
        thread.join(5)
        panel.close_all()
    assert errors == ["RuntimeError"]
    assert created and not created[0].alive
    assert not panel.slots
