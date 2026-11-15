"""Owned application presentation routes require origin/token and bounded geometry."""

import json
from types import SimpleNamespace

import pytest
from test_installed_apps import library, verified


def controls(tmp_path):
    """Inject a protected temporary app and inert owned lifecycle methods."""
    from agentix.application.app_controls import ApplicationControls

    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    actions = []
    preview = SimpleNamespace(
        port=5874,
        paused=False,
        cancel_execution=lambda: actions.append("cancel"),
        restart_execution=lambda: actions.append("restart"),
        request_close=lambda: actions.append("close"),
    )
    router = ApplicationControls(preview, library=service, identity=app.id)
    return router, service, app, actions


def test_layout_save_requires_exact_origin_and_private_preview_token(tmp_path):
    """A foreign page cannot write an app's presentation through loopback CSRF."""
    router, service, app, _ = controls(tmp_path)
    status, _, body = router.handle("GET", "/_agentix/layout", {}, b"")
    assert status == 200
    token = json.loads(body)["token"]
    layout = {
        "version": 1,
        "positions": {
            "application_count_words_in_text_input": {"x": 10, "y": 20, "width": 300, "height": 100}
        },
    }
    for headers in (
        {"origin": "https://evil.example", "x-agentix-token": token},
        {"origin": "http://127.0.0.1:5874"},
    ):
        assert (
            router.handle("POST", "/_agentix/layout", headers, json.dumps(layout).encode())[0]
            == 403
        )
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    assert router.handle("POST", "/_agentix/layout", headers, json.dumps(layout).encode())[0] == 200
    assert service.read_layout(app.id) == layout


def test_layout_cannot_move_toolbar_or_execute_code(tmp_path):
    """Only known canvas control IDs and numeric rectangles are persisted."""
    router, _, _, actions = controls(tmp_path)
    token = json.loads(router.handle("GET", "/_agentix/layout", {}, b"")[2])["token"]
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    for payload in (
        {
            "version": 1,
            "positions": {"application_stop": {"x": 0, "y": 0, "width": 100, "height": 100}},
        },
        {"version": 1, "positions": {}, "python": "exec(...)"},
    ):
        assert (
            router.handle("POST", "/_agentix/layout", headers, json.dumps(payload).encode())[0]
            == 403
        )
    assert actions == []


def test_layout_hidden_controls_roundtrip_and_reject_toolbar(tmp_path):
    """V7-062: persisted visibility uses the same allowlist as geometry."""
    router, service, app, _ = controls(tmp_path)
    token = json.loads(router.handle("GET", "/_agentix/layout", {}, b"")[2])["token"]
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    layout = {
        "version": 1,
        "positions": {
            "application_count_words_in_text_output": {
                "x": 10,
                "y": 20,
                "width": 300,
                "height": 100,
            }
        },
        "hidden": ["application_count_words_in_text_output"],
    }
    assert router.handle("POST", "/_agentix/layout", headers, json.dumps(layout).encode())[0] == 200
    assert service.read_layout(app.id) == layout
    for forbidden in ("application_edit", "application_stop"):
        payload = {"version": 1, "positions": {}, "hidden": [forbidden]}
        assert (
            router.handle("POST", "/_agentix/layout", headers, json.dumps(payload).encode())[0]
            == 403
        )
    assert service.read_layout(app.id) == layout


def test_owned_stop_restart_and_close_never_accept_a_path(tmp_path):
    """Lifecycle controls act on this preview only and reject user-selected entries."""
    router, _, _, actions = controls(tmp_path)
    token = json.loads(router.handle("GET", "/_agentix/layout", {}, b"")[2])["token"]
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    for action in ("cancel", "restart", "close"):
        assert router.handle("POST", "/_agentix/" + action, headers, b"{}")[0] == 200
    assert actions == ["cancel", "restart", "close"]
    assert router.handle("POST", "/_agentix/restart", headers, b'{"path":"elsewhere"}')[0] == 403


def test_duplicate_layout_keys_and_oversize_requests_are_rejected(tmp_path):
    """Ambiguous or unbounded presentation input cannot reach persistent storage."""
    router, _, _, _ = controls(tmp_path)
    token = json.loads(router.handle("GET", "/_agentix/layout", {}, b"")[2])["token"]
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    for body in (b'{"version":1,"version":1,"positions":{}}', b" " * 65537):
        assert router.handle("POST", "/_agentix/layout", headers, body)[0] == 403


def test_paused_preview_restarts_only_owned_snapshot():
    """Lifecycle doubles establish ownership and cleanup, not native isolation."""
    import threading

    from agentix.lab.application_panel import ApplicationPreview

    preview = object.__new__(ApplicationPreview)
    preview.lifecycle_lock = threading.Lock()
    preview.stop = threading.Event()
    preview.paused = False
    preview.approved = object()
    actions = []
    preview.session = SimpleNamespace(close=lambda: actions.append("old closed"))
    preview.bridge = SimpleNamespace(session=preview.session)
    new = SimpleNamespace(
        __enter__=lambda: actions.append("new started"), close=lambda: actions.append("new closed")
    )
    preview._create_session = lambda approved: new if approved is preview.approved else None
    preview.cancel_execution()
    assert preview.paused and actions == ["old closed"]
    preview.restart_execution()
    assert not preview.paused and preview.session is new and preview.bridge.session is new
    assert actions == ["old closed", "new started"]
    with pytest.raises(ValueError):
        preview.restart_execution()


def test_revoked_dependencies_still_allow_owned_stop_and_close(tmp_path):
    """A stale app must remain cancellable; only restart/save require its grant."""
    router, _, _, actions = controls(tmp_path)

    def revoked():
        """Represent a changed tool approval without modifying user storage."""
        raise ValueError("revoked")

    router.check = revoked
    token = json.loads(router.handle("GET", "/_agentix/layout", {}, b"")[2])["token"]
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": token,
        "content-type": "application/json",
    }
    assert router.handle("POST", "/_agentix/close", headers, b"{}")[0] == 200
    assert router.handle("POST", "/_agentix/restart", headers, b"{}")[0] == 403
    assert actions == ["close"]


def test_changed_app_still_exposes_an_owned_close_token(tmp_path, monkeypatch):
    """A tampered source disables layout editing but cannot strand the stopped page."""
    router, service, _, actions = controls(tmp_path)

    def unavailable(identity):
        """Simulate a protected source identity mismatch."""
        raise ValueError("source changed")

    monkeypatch.setattr(service, "read_layout", unavailable)
    status, _, body = router.handle("GET", "/_agentix/layout", {}, b"")
    assert status == 200
    data = json.loads(body)
    assert not data["editable"] and data["layout"]["positions"] == {}
    headers = {
        "origin": "http://127.0.0.1:5874",
        "x-agentix-token": data["token"],
        "content-type": "application/json",
    }
    assert router.handle("POST", "/_agentix/close", headers, b"{}")[0] == 200
    assert actions == ["close"]


def test_application_stylesheet_is_served_per_request_from_the_staging_root(tmp_path):
    """V7-077: a saved widget style reaches reloads instead of the startup copy."""
    from agentix.application.app_controls import ApplicationControls

    staging = tmp_path / "staging"
    staging.mkdir()
    stylesheet = staging / "application.css"
    stylesheet.write_bytes(b"/* startup */")
    preview = SimpleNamespace(port=5874, paused=False)
    router = ApplicationControls(preview, root=lambda: staging)
    status, media, body = router.handle("GET", "/_agentix/application.css", {}, b"")
    assert (status, media, body) == (200, "text/css", b"/* startup */")
    stylesheet.write_bytes(b"/* saved */")
    assert router.handle("GET", "/_agentix/application.css", {}, b"")[2] == b"/* saved */"
    assert ApplicationControls(preview).handle("GET", "/_agentix/application.css", {}, b"")[0] == 403
