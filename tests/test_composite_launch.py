"""LAB-005 standalone validation and GUI integration contract tests."""

import socket

import pytest


def test_launcher_rejects_occupied_port_before_staging(monkeypatch, tmp_path):
    """Catch expensive native startup and accidental fallback when a requested port is busy."""
    from schema3_package import package

    from agentix.lab.application_artifacts import application_digest, approve_application
    from agentix.lab.application_panel import ApplicationPreview

    folder = package(tmp_path)
    approved = approve_application(folder, application_digest(folder))
    entered = []
    monkeypatch.setattr(
        ApplicationPreview, "_create_session", lambda self, capability: entered.append(True)
    )
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen()
        with pytest.raises(OSError):
            ApplicationPreview(approved, None, port=listener.getsockname()[1])
    assert not entered


def test_application_panel_does_not_leak_error_bodies(caplog):
    """Startup errors must not publish application code or exception text in UI/logs."""
    from agentix.lab.application_panel import open_application

    class Broken:
        def open(self, owner, origin):
            raise SyntaxError("SYNTHETIC_PRIVATE_SOURCE")

    rows = list(open_application(Broken(), "owner", "http://127.0.0.1:7874"))
    assert "SYNTHETIC_PRIVATE_SOURCE" not in str(rows) + caplog.text
    assert rows[-1][1] == ""
