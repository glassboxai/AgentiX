"""Real native browser verification of the shared CSS and accessible corner close."""

import os
import subprocess
import sys
from pathlib import Path

import pytest
import schema3_package
from test_composite_browser import await_http, free_port

from agentix.lab.application_artifacts import application_digest

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_native_application_matches_parent_palette_and_closes(tmp_path):
    """Catch iframe style isolation, inaccessible close or a close that leaks the worker."""
    from playwright.sync_api import expect, sync_playwright

    package = schema3_package.package(tmp_path)
    port = free_port()
    logpath = tmp_path / "style-server.log"
    with logpath.open("w", encoding="utf-8") as log:
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
                page = browser.new_page(viewport={"width": 1280, "height": 900})
                page.goto(url)
                container = page.locator(".gradio-container")
                assert (
                    container.evaluate("el => getComputedStyle(el).backgroundColor")
                    == "rgb(5, 6, 8)"
                )
                button = page.get_by_role("button", name="Close application", exact=True)
                expect(button).to_be_visible()
                assert "×" in button.evaluate('el => getComputedStyle(el, "::after").content')
                bounds = button.bounding_box()
                assert bounds["x"] > 1100 and bounds["y"] < 80
                assert button.evaluate("el => getComputedStyle(el).borderRadius") == "0px"
                page.screenshot(
                    path=str(ROOT / "docs/reports/v4-application-style.png"), full_page=True
                )
                button.click()
                browser.close()
            process.wait(timeout=45)
            assert process.returncode == 0, logpath.read_text(encoding="utf-8", errors="replace")
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=35)
