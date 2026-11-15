"""Opt-in independent browser acceptance of an operator-reviewed model candidate.

Never imports candidate Python on the host. The operator must supply the digest
from a separate code review; tests cannot grant or persist production approval.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from test_composite_browser import await_http, free_port

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_model_generated_widget_in_real_native_gui(tmp_path):
    """Catch incorrect callbacks, zero handling, stale outputs and ID collisions."""
    from playwright.sync_api import expect, sync_playwright

    package = os.environ.get("AGENTIX_DESIGNER_REVIEWED_PACKAGE")
    digest = os.environ.get("AGENTIX_DESIGNER_REVIEWED_DIGEST")
    if not package or not digest:
        pytest.skip("Explicit independently reviewed candidate required")
    port = free_port()
    logpath = tmp_path / "designer-gui.log"
    evidence = tmp_path / "native.json"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "application_launch.py"),
                "--package",
                package,
                "--reviewed-digest",
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
            url = f"http://127.0.0.1:{port}"
            await_http(url, process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                page = browser.new_page()
                page.goto(url)
                for text, expected in [
                    ("Hello World!", "3"),
                    ("AEIOUaeiou", "10"),
                    ("rhythms", "0"),
                    ("", "0"),
                    ("Hello World!", "3"),
                ]:
                    page.locator("#application_vowels_input textarea").fill(text)
                    page.locator("#application_vowels_execute").click()
                    expect(page.locator("#application_vowels_output input")).to_have_value(
                        expected, timeout=45000
                    )
                page.locator("#application_vowels_input textarea").fill("x" * 16001)
                page.locator("#application_vowels_execute").click()
                expect(page.locator("#application_vowels_output input")).to_have_value(
                    "", timeout=45000
                )
                ids = page.locator('[id^="application_"]').evaluate_all(
                    "items => items.map(item => item.id)"
                )
                assert len(ids) == len(set(ids))
                page.screenshot(
                    path=str(ROOT / "docs/reports/lab-006-generated-widget.png"), full_page=True
                )
                (ROOT / "docs/reports/lab-006-browser.json").write_text(
                    json.dumps(
                        {
                            "browser": browser.version,
                            "package": package,
                            "reviewed_digest": digest,
                            "literal_cases": 6,
                            "host_execution": False,
                        }
                    ),
                    encoding="utf-8",
                )
                browser.close()
            process.wait(timeout=150)
            assert process.returncode == 0, logpath.read_text(encoding="utf-8", errors="replace")
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=30)
