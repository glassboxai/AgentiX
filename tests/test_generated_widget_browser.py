"""Actual reviewed generated-widget GUI, native callbacks and independent acceptance."""

import hashlib
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

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_reviewed_generated_widget_through_bridge(tmp_path):
    """Browser clicks must produce literal results and matching native host receipts."""
    from playwright.sync_api import expect, sync_playwright

    folder = os.environ.get("AGENTIX_WIDGET_PACKAGE")
    digest = os.environ.get("AGENTIX_WIDGET_REVIEW_DIGEST")
    if not folder or not digest:
        pytest.skip("Explicit experimental package and engineer-reviewed digest required")
    if any(part.lower() == "generated_tools" for part in Path(folder).parts):
        pytest.fail("Existing generated_tools is excluded")
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    evidence = tmp_path / "native-receipts.json"
    logpath = tmp_path / "server.log"
    url = f"http://127.0.0.1:{port}"
    with logpath.open("w") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                "widget_preview.py",
                "--package",
                folder,
                "--approved-digest",
                digest,
                "--port",
                str(port),
                "--duration",
                "120",
                "--evidence",
                str(evidence),
            ],
            cwd=ROOT,
            stdout=log,
            stderr=log,
        )
        try:
            opener = build_opener(ProxyHandler({}))
            deadline = time.monotonic() + 180
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    pytest.fail(logpath.read_text())
                try:
                    with opener.open(url, timeout=2):
                        break
                except (URLError, TimeoutError):
                    time.sleep(0.2)
            else:
                pytest.fail("Bridge startup deadline: " + logpath.read_text())
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                page = browser.new_page()
                page.goto(url)
                for text, expected in [
                    ("Hello World!", "3"),
                    ("AEIOUaeiou", "10"),
                    ("rhythms", "0"),
                ]:
                    page.locator("#widget_first_input textarea").fill(text)
                    page.locator("#widget_first_execute").click()
                    expect(page.locator("#widget_first_output input")).to_have_value(
                        expected, timeout=45000
                    )
                page.locator("#widget_second_input textarea").fill("Hello World!")
                page.locator("#widget_second_execute").click()
                expect(page.locator("#widget_second_output input")).to_have_value(
                    "3", timeout=45000
                )
                expect(page.locator("#widget_first_output input")).to_have_value("0")
                page.screenshot(
                    path=str(ROOT / "docs/reports/lab-003-generated-widget.png"), full_page=True
                )
                browser.close()
            with pytest.raises(URLError):
                opener.open(url + "/gradio_api/file=/secret", timeout=2)
            # Wait for the finite native worker lifetime; do not terminate another server.
            process.wait(timeout=150)
            assert process.returncode == 0, logpath.read_text()
            observations = json.loads(evidence.read_text())
            (ROOT / "docs/reports/lab-003-browser-receipts.json").write_text(
                json.dumps(observations, indent=2)
            )
            receipts = observations["tool_receipts"]
            for text, expected in [("Hello World!", 3), ("AEIOUaeiou", 10), ("rhythms", 0)]:
                assert any(
                    item["instance"] == "first"
                    and item["input_sha256"] == hashlib.sha256(text.encode()).hexdigest()
                    and item["value"] == expected
                    and item["isolated"]
                    for item in receipts
                )
            assert observations["diagnostics"]["provisional_tests"]["successful"]
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=15)
