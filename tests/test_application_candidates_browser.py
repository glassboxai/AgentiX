"""Real disposable GUI validation of retrieval preview, spinner and explicit acceptance."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from test_composite_browser import await_http, free_port

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_candidate_preview_spinner_and_acceptance(tmp_path: Path) -> None:
    """Use actual Gradio callbacks and two browsers with explicit model/approval doubles."""
    from playwright.sync_api import expect, sync_playwright

    port = free_port()
    logpath = tmp_path / "candidate-server.log"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "tests/application_review_server.py"),
                str(port),
                str(tmp_path),
                "code-cases",
            ],
            cwd=ROOT,
            stdout=log,
            stderr=log,
            env=dict(os.environ, PYTHONIOENCODING="utf-8", GRADIO_ANALYTICS_ENABLED="False"),
        )
        try:
            url = f"http://127.0.0.1:{port}"
            await_http(url, process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                first, second = browser.new_page(), browser.new_page()
                first.goto(url)
                first.get_by_role("tab", name="Applications", exact=True).click()
                panel = first.locator("#application-candidates-panel")
                expect(panel).to_be_visible()
                assert panel.bounding_box()["y"] > first.locator("#apps-delete").bounding_box()["y"]
                first.locator("#applications-name textarea").fill("Candidate calculator")
                first.locator("#applications-query textarea").fill("Add two numbers")
                first.locator("#applications-generate").click()
                accept = first.locator("#application-candidates-accept")
                expect(first.locator("#application-candidates-status")).to_contain_text(
                    "limit 5", timeout=30000
                )
                expect(accept).to_be_enabled(timeout=15000)
                checks = first.locator("#application-candidates-list input[type=checkbox]")
                expect(checks).to_have_count(1)
                expect(checks.first).to_be_checked()
                colors = checks.first.locator("..").evaluate(
                    "element => ({background: getComputedStyle(element).backgroundColor, color: getComputedStyle(element).color})"
                )
                assert colors == {"background": "rgb(16, 20, 28)", "color": "rgb(232, 243, 255)"}
                checks.first.uncheck()
                expect(accept).to_be_disabled()
                expect(accept).to_contain_text("0 selected")
                checks.first.check()
                expect(accept).to_be_enabled()
                audit = json.loads((tmp_path / "audit.json").read_text())
                assert audit.get("candidate_generation_tools", []) == []
                assert audit["generation_roles"] == []
                first.locator("#applications-query textarea").fill("Add two integer numbers")
                # Description edits leave the preview and checkboxes unchanged.
                expect(checks).to_have_count(1)
                expect(checks.first).to_be_checked()
                expect(first.locator("#application-candidates-status")).to_contain_text("limit 5")
                assert json.loads((tmp_path / "audit.json").read_text())["candidate_limits"] == [5]
                # Acceptance still rejects a description that differs from the snapshot.
                accept.click()
                expect(first.locator("#application-candidates-status")).to_contain_text(
                    "Search again"
                )
                assert (
                    json.loads((tmp_path / "audit.json").read_text()).get(
                        "candidate_generation_tools", []
                    )
                    == []
                )
                first.locator("#applications-generate").click()
                expect(first.locator("#application-candidates-status")).to_contain_text(
                    "limit 5", timeout=30000
                )
                expect(accept).to_be_enabled(timeout=15000)
                spinner = first.locator("#application-candidate-limit input")
                checks.first.uncheck()
                spinner.focus()
                spinner.press("ArrowDown")
                expect(spinner).to_have_value("4")
                expect(first.locator("#application-candidates-status")).to_contain_text(
                    "limit 4", timeout=30000
                )
                expect(checks.first).to_be_checked()
                spinner.focus()
                spinner.press("ArrowUp")
                expect(spinner).to_have_value("5")
                expect(first.locator("#application-candidates-status")).to_contain_text(
                    "limit 5", timeout=30000
                )
                second.goto(url)
                second.get_by_role("tab", name="Applications", exact=True).click()
                expect(second.locator("#application-candidates-accept")).to_be_disabled()
                expect(
                    second.locator("#application-candidates-list input[type=checkbox]")
                ).to_have_count(0)
                expect(accept).to_be_enabled(timeout=15000)
                accept.click()
                expect(first.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                audit = json.loads((tmp_path / "audit.json").read_text())
                assert audit["candidate_limits"] == [5, 5, 4, 5]
                assert audit["candidate_generation_tools"] == [["calculator"]]
                assert "candidate_accepted" in logpath.read_text(encoding="utf-8", errors="replace")
                first.screenshot(path=str(tmp_path / "candidate-panel.png"), full_page=True)
                panel.screenshot(path=str(tmp_path / "candidate-panel-detail.png"))
                browser.close()
        finally:
            from test_catalog_maintenance_browser import stop_process_tree

            stop_process_tree(process)
