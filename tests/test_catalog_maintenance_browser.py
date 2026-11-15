"""Real GUI deletion and rejected-file repair; model boundary and initial catalog grants are explicit doubles."""

import json
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest
from disposable import stop_process_tree
from test_composite_browser import await_http, free_port

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]
CODE = '"""Reviewed doubling fixture."""\ndef double(value):\n    if not isinstance(value, int) or isinstance(value, bool):\n        raise ValueError("Invalid value")\n    return value * 2\n'
TESTS = 'import unittest\nfrom repair_demo_code import double\nclass Repaired(unittest.TestCase):\n    def test_normal(self):\n        self.assertEqual(double(2), 4)\n    def test_zero(self):\n        self.assertEqual(double(0), 0)\n    def test_invalid(self):\n        with self.assertRaises(ValueError):\n            double("2")\n'


@contextmanager
def server(tmp_path, mode="normal"):
    """Own one disposable server and its complete process tree."""
    port = free_port()
    logpath = tmp_path / "server.log"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "tests/application_review_server.py"),
                str(port),
                str(tmp_path),
                mode,
            ],
            cwd=ROOT,
            stdout=log,
            stderr=log,
        )
        try:
            url = f"http://127.0.0.1:{port}"
            await_http(url, process, logpath)
            yield url
        finally:
            stop_process_tree(process)


def choose(page, selector, label):
    """Select a real Gradio option by its user-facing identity."""
    page.locator(selector + " input").click()
    page.get_by_role("option", name=label, exact=True).click()


def replace_code(page, selector, text):
    """Edit the actual CodeMirror control, not hidden server data."""
    page.locator(selector + " .cm-content").click()
    page.keyboard.press("Control+A")
    page.keyboard.insert_text(text)


def test_delete_confirmation_dependencies_and_open_app(tmp_path):
    """Exercise dependency blocking, cancellation, cross-session use and permanent removal."""
    from playwright.sync_api import expect, sync_playwright

    with server(tmp_path, "maintenance") as url, sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
        )
        first, second = browser.new_page(), browser.new_page()
        first.goto(url)
        choose(first, "#installed-tool-selection", "count_words_in_text")
        first.locator("#tools-delete").click()
        expect(first.locator("#tools-delete-status")).to_contain_text("dependencies")
        expect(first.locator("#tools-delete-confirmation")).to_be_hidden()
        first.get_by_role("tab", name="Applications", exact=True).click()
        first.locator("#installed-apps-refresh").click()
        choose(first, "#installed-apps", "Maintenance demo")
        first.locator("#apps-delete").click()
        expect(first.locator("#apps-delete-confirmation")).to_be_visible()
        first.locator("#apps-delete-cancel").click()
        expect(first.locator("#applications-status")).to_contain_text("cancelled")
        first.locator("#installed-apps-play").click()
        expect(first.locator("#applications-status")).to_contain_text(
            "Application ready", timeout=180000
        )
        second.goto(url)
        second.get_by_role("tab", name="Applications", exact=True).click()
        second.locator("#installed-apps-refresh").click()
        choose(second, "#installed-apps", "Maintenance demo")
        second.locator("#apps-delete").click()
        expect(second.locator("#applications-status")).to_contain_text("Close the open application")
        expect(second.locator("#apps-delete-confirmation")).to_be_hidden()
        first.frame_locator("#applications-frame iframe").get_by_role(
            "button", name="Close application", exact=True
        ).click()
        expect(first.locator("#applications-frame iframe")).to_have_count(0, timeout=45000)
        second.locator("#apps-delete").click()
        expect(second.locator("#apps-delete-confirmation")).to_be_visible()
        second.locator("#apps-delete-confirm").click()
        expect(second.locator("#applications-status")).to_contain_text("permanently deleted")
        assert not (tmp_path / "installed-apps/maintenance-demo").exists()
        first.get_by_role("tab", name="Tools", exact=True).click()
        first.locator("#tools-delete").click()
        expect(first.locator("#tools-delete-confirmation")).to_be_visible()
        first.locator("#tools-delete-cancel").click()
        first.locator("#tools-delete").click()
        first.locator("#tools-delete-confirm").click()
        expect(first.locator("#tools-delete-status")).to_contain_text("permanently deleted")
        first.locator("#installed-tool-selection input").click()
        expect(first.get_by_role("option", name="count_words_in_text", exact=True)).to_have_count(0)
        expect(first.get_by_role("option", name="count_vowels_in_text", exact=True)).to_be_visible()
        first.screenshot(path=str(ROOT / "docs/reports/v5-038-catalog-removal.png"), full_page=True)
        browser.close()


@pytest.mark.windows_isolation
def test_reject_edit_revalidate_and_reuse_from_user_query(tmp_path):
    """No file approval rejection may force a new tool or silently bypass acceptance."""
    from playwright.sync_api import expect, sync_playwright

    with server(tmp_path, "native-repair") as url, sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
        )
        page = browser.new_page(viewport={"width": 1500, "height": 1000})
        page.goto(url)
        page.get_by_label("User Query", exact=True).fill(
            "Please create a calculator that doubles numbers."
        )
        page.get_by_role("button", name="Send query", exact=True).click()
        review = page.get_by_label(
            "Review and edit file content or acceptance cases before approving", exact=True
        )
        expect(review).to_have_value(__import__("re").compile(r"value \* 3"), timeout=20000)
        page.get_by_role("button", name="Reject Operation", exact=True).click()
        expect(page.locator("#agentix-chat")).to_contain_text("Operation aborted", timeout=15000)
        page.locator("#tool-repair-panel").get_by_text("Repair rejected tool", exact=True).click()
        page.locator("#tool-repair-load").click()
        expect(page.locator("#tool-repair-name textarea")).to_have_value("repair_demo")
        expect(page.locator("#tool-repair-code .cm-content")).to_contain_text("value * 3")
        replace_code(page, "#tool-repair-code", CODE)
        replace_code(page, "#tool-repair-tests", TESTS)
        page.locator("#tool-repair-restart").click()
        expect(review).to_have_value(__import__("re").compile('"cases"'), timeout=30000)
        proposed = json.loads(review.input_value())
        cases = {case["id"]: case for case in proposed["cases"]}
        assert cases["normal"]["expect"] == {"kind": "value", "value": 4}
        assert cases["zero"]["expect"] == {"kind": "value", "value": 0}
        assert cases["invalid"]["expect"] == {"kind": "raises", "type": "ValueError"}
        page.get_by_role("button", name="Approve Reviewed Content", exact=True).click()
        expect(page.locator("#validation-panel")).to_contain_text(
            "Verified against approved cases", timeout=30000
        )
        expect(review).to_be_hidden(timeout=15000)
        expect(page.locator("#agentix-chat .execution-result").last).to_contain_text(
            "4", timeout=30000
        )
        expect(page.locator("#agentix-operation-progress .agentix-busy-panel")).to_have_count(
            0, timeout=15000
        )
        before = json.loads((tmp_path / "audit.json").read_text(encoding="utf-8"))["tool_test_runs"]
        assert before == 1
        page.get_by_label("User Query", exact=True).fill("What is twice five?")
        page.get_by_role("button", name="Send query", exact=True).click()
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(2, timeout=30000)
        expect(page.locator("#agentix-chat .execution-result").last).to_contain_text("10")
        expect(review).to_be_hidden()
        assert (
            json.loads((tmp_path / "audit.json").read_text(encoding="utf-8"))["tool_test_runs"]
            == before
        )
        page.screenshot(path=str(ROOT / "docs/reports/v5-038-repaired-tool.png"), full_page=True)
        browser.close()
