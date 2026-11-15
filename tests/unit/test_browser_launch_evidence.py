"""Browser launch failures must retain bounded evidence for operator diagnosis."""

import json

import pytest

from agentix.application.general_acceptance import launch_acceptance_browser


class _FailingDriver:
    def __init__(self, error: BaseException) -> None:
        self.chromium = self
        self.error = error

    def launch(self, executable_path=None):
        raise self.error


class _OkDriver:
    def __init__(self) -> None:
        self.chromium = self
        self.seen = None

    def launch(self, executable_path=None):
        self.seen = executable_path
        return "browser"


def test_launch_failure_writes_bounded_evidence(tmp_path, monkeypatch):
    """A launch error retains type/detail in browser-failure.json and re-raises."""
    monkeypatch.delenv("AGENTIX_PLAYWRIGHT_EXECUTABLE", raising=False)
    with pytest.raises(RuntimeError):
        launch_acceptance_browser(_FailingDriver(RuntimeError("no executable")), tmp_path)
    evidence = json.loads((tmp_path / "browser-failure.json").read_text(encoding="utf-8"))
    assert evidence["type"] == "RuntimeError"
    assert evidence["stage"] == "browser_launch"
    assert "no executable" in evidence["detail"]


def test_missing_configured_executable_fails_clearly(tmp_path, monkeypatch):
    """A configured but absent executable raises a clear actionable ValueError."""
    monkeypatch.setenv("AGENTIX_PLAYWRIGHT_EXECUTABLE", str(tmp_path / "missing.exe"))
    with pytest.raises(ValueError, match="AGENTIX_PLAYWRIGHT_EXECUTABLE"):
        launch_acceptance_browser(_OkDriver(), tmp_path)


def test_launch_uses_configured_executable(tmp_path, monkeypatch):
    """A valid configured executable is passed through to the driver."""
    executable = tmp_path / "browser.exe"
    executable.write_bytes(b"")
    monkeypatch.setenv("AGENTIX_PLAYWRIGHT_EXECUTABLE", str(executable))
    driver = _OkDriver()
    assert launch_acceptance_browser(driver, tmp_path) == "browser"
    assert driver.seen == str(executable)
