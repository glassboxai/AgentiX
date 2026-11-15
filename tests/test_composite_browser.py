"""Real Playwright acceptance of the independent native application."""

import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import pytest
import schema3_package

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def free_port():
    """Choose a disposable test port; production launchers require an explicit port."""
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        return listener.getsockname()[1]


def await_http(url, process, logpath):
    """Wait for an owned listener without touching any live Lab process."""
    opener = build_opener(ProxyHandler({}))
    deadline = time.monotonic() + 150
    while time.monotonic() < deadline:
        if process.poll() is not None:
            pytest.fail(logpath.read_text(errors="replace"))
        try:
            with opener.open(url, timeout=2):
                return
        except (URLError, TimeoutError):
            time.sleep(0.2)
    pytest.fail("Disposable application readiness deadline")


def check_analysis(frame, text, words, vowels):
    """Use literal independent expected values, read from the visible application result."""
    from playwright.sync_api import expect

    frame.locator("#application_input_text textarea").fill(text)
    frame.locator("#application_execute").click()
    expect(frame.locator("#application_status textarea")).to_have_value("Completed", timeout=45000)
    expect(frame.locator("#application_count_words_in_text_output input")).to_have_value(
        str(words), timeout=10000
    )
    expect(frame.locator("#application_count_vowels_in_text_output input")).to_have_value(
        str(vowels), timeout=10000
    )


def test_standalone_launcher_gui_without_lab(tmp_path):
    """Launch the same package without Lab, operate it and observe automatic native expiry."""
    from playwright.sync_api import sync_playwright

    from agentix.lab.application_artifacts import application_digest

    package = schema3_package.package(tmp_path)
    port = free_port()
    logpath, evidence = tmp_path / "standalone.log", tmp_path / "standalone.json"
    with logpath.open("w") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "application_launch.py"),
                "--package",
                str(package),
                "--reviewed-digest",
                application_digest(package),
                "--port",
                str(port),
                "--duration",
                "60",
                "--evidence",
                str(evidence),
            ],
            cwd=tmp_path,
            stdout=log,
            stderr=log,
        )
        try:
            url = f"http://127.0.0.1:{port}"
            await_http(url, process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                page = browser.new_page()
                page.goto(url)
                check_analysis(page, "Hello World!", 2, 3)
                check_analysis(page, "rhythms", 1, 0)
                browser.close()
            process.wait(timeout=100)
            assert process.returncode == 0, logpath.read_text()
            assert json.loads(evidence.read_text())["host_timings"]["cleanup"] >= 0
            with pytest.raises(OSError):
                socket.create_connection(("127.0.0.1", port), timeout=1)
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=20)
