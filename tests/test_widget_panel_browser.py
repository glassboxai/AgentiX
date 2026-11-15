"""LAB-004 Playwright begins in Lab and operates the actual isolated embedded widget."""

import hashlib
import json
import os
import re
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


def test_lab_opens_native_widget_in_its_own_gui(tmp_path):
    """Verify real iframe counts, owner separation, close/reopen and native receipts."""
    if os.environ.get("AGENTIX_WIDGET_PANEL_LIVE") != "1":
        pytest.skip("Explicit reviewed experimental package activation required")
    from playwright.sync_api import expect, sync_playwright

    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    url = f"http://127.0.0.1:{port}"
    audit = tmp_path / "audit.json"
    logpath = tmp_path / "server.log"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [sys.executable, str(ROOT / "tests/widget_panel_server.py"), str(port), str(audit)],
            cwd=ROOT,
            stdout=log,
            stderr=log,
            env=dict(os.environ, GRADIO_ANALYTICS_ENABLED="False"),
        )
        try:
            deadline = time.monotonic() + 60
            opener = build_opener(ProxyHandler({}))
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    pytest.fail(logpath.read_text())
                try:
                    with opener.open(url, timeout=2):
                        break
                except (URLError, TimeoutError):
                    time.sleep(0.2)
            else:
                pytest.fail("Disposable Lab startup deadline")
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                first = browser.new_page()
                second = browser.new_page()
                first.goto(url)
                second.goto(url)
                expect(first.get_by_text("count_vowels_in_text", exact=False).first).to_be_visible()
                first.locator("#lab_widget_open").click()
                expect(first.locator("#lab_widget_status textarea")).to_have_value(
                    re.compile("^Ready"), timeout=150000
                )
                frame = first.frame_locator("#lab_widget_frame iframe")
                for text, expected in [
                    ("Hello World!", "3"),
                    ("AEIOUaeiou", "10"),
                    ("rhythms", "0"),
                ]:
                    frame.locator("#widget_first_input textarea").fill(text)
                    frame.locator("#widget_first_execute").click()
                    expect(frame.locator("#widget_first_output input")).to_have_value(
                        expected, timeout=45000
                    )
                assert first.get_by_text("Approve Reviewed Content", exact=True).count() == 0
                assert first.get_by_text("Authorization & Review Required", exact=True).count() == 0
                second.locator("#lab_widget_open").click()
                expect(second.locator("#lab_widget_status textarea")).to_have_value(
                    re.compile("^Ready"), timeout=150000
                )
                other = second.frame_locator("#lab_widget_frame iframe")
                other.locator("#widget_first_input textarea").fill("Hello World!")
                other.locator("#widget_first_execute").click()
                expect(other.locator("#widget_first_output input")).to_have_value(
                    "3", timeout=45000
                )
                expect(frame.locator("#widget_first_output input")).to_have_value("0")
                first.screenshot(
                    path=str(ROOT / "docs/reports/lab-004-integrated-widget.png"), full_page=True
                )
                first.locator("#lab_widget_close").click()
                expect(first.locator("#lab_widget_frame iframe")).to_have_count(0, timeout=45000)
                expect(other.locator("#widget_first_output input")).to_have_value("3")
                other.locator("#widget_first_input textarea").fill("AEIOUaeiou")
                other.locator("#widget_first_execute").click()
                expect(other.locator("#widget_first_output input")).to_have_value(
                    "10", timeout=45000
                )
                first.locator("#lab_widget_open").click()
                expect(first.locator("#lab_widget_status textarea")).to_have_value(
                    re.compile("^Ready"), timeout=150000
                )
                reopened = first.frame_locator("#lab_widget_frame iframe")
                reopened.locator("#widget_first_input textarea").fill("AEIOUaeiou")
                reopened.locator("#widget_first_execute").click()
                expect(reopened.locator("#widget_first_output input")).to_have_value(
                    "10", timeout=45000
                )
                first.locator("#lab_widget_close").click()
                second.locator("#lab_widget_close").click()
                expect(first.locator("#lab_widget_frame iframe")).to_have_count(0, timeout=45000)
                expect(second.locator("#lab_widget_frame iframe")).to_have_count(0, timeout=45000)
                browser.close()
            rows = json.loads(audit.read_text())
            assert len(rows) >= 3
            assert all(row["native_stopped"] and row["listener_stopped"] for row in rows)
            assert all("provisional_tests" not in row["diagnostics"] for row in rows)
            receipts = [item for row in rows for item in row["receipts"]]
            for text, value in [("Hello World!", 3), ("AEIOUaeiou", 10), ("rhythms", 0)]:
                assert any(
                    item["input_sha256"] == hashlib.sha256(text.encode()).hexdigest()
                    and item["value"] == value
                    and item["isolated"]
                    for item in receipts
                )
            (ROOT / "docs/reports/lab-004-integrated-receipts.json").write_text(
                json.dumps(rows, indent=2)
            )
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=15)
