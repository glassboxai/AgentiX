"""Real GUI/file review/repair/native checks; model and initial tool grants are doubles."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from test_composite_browser import await_http, check_analysis, free_port

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_readable_review_progress_repair_and_approved_catalog_native_application(tmp_path):
    """Exercise real controls, explicit editing, repair and native framed application."""
    from playwright.sync_api import expect, sync_playwright

    port = free_port()
    url = f"http://127.0.0.1:{port}"
    logpath = tmp_path / "server.log"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "tests/application_review_server.py"),
                str(port),
                str(tmp_path),
            ],
            cwd=ROOT,
            stdout=log,
            stderr=log,
        )
        try:
            await_http(url, process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                first, second = browser.new_page(), browser.new_page()
                first.goto(url)
                expect(first.locator("#llm-provider input")).to_have_value("Ollama")
                expect(
                    first.locator("#agentix-operation-progress .agentix-busy-panel")
                ).to_have_count(0)
                expect(first.locator("#agentix-operation-progress .wrap")).to_be_hidden()
                first.get_by_label("User Query", exact=True).fill("Check background processing")
                first.get_by_role("button", name="Send query", exact=True).click()
                expect(
                    first.locator("#agentix-operation-progress .agentix-busy-panel")
                ).to_be_visible(timeout=10000)
                expect(first.locator("#agentix-chat")).to_contain_text(
                    "Trusted background work completed.", timeout=20000
                )
                expect(
                    first.locator("#agentix-operation-progress .agentix-busy-panel")
                ).to_have_count(0, timeout=10000)
                first.locator("#agentix-sidebar").get_by_role(
                    "button", name="Toggle Sidebar", exact=True
                ).click()
                refresh_models = first.get_by_role("button", name="Refresh models", exact=True)
                expect(refresh_models).to_be_visible()
                refresh_models.click()
                expect(first.locator("#agentix-operation-progress .wrap")).to_be_visible(
                    timeout=10000
                )
                expect(first.locator("#model-status")).to_contain_text("refreshed")
                expect(first.locator("#agentix-operation-progress .wrap")).to_be_hidden(
                    timeout=15000
                )
                first.get_by_role("tab", name="Applications", exact=True).click()
                expect(first.locator("#applications-repair")).to_be_hidden()
                first.locator("#applications-query textarea").fill("Count words and vowels")
                first.locator("#applications-name textarea").fill(
                    "Text analysis"
                    if not first.locator("#applications-name textarea").input_value()
                    else "Another text analysis"
                )
                first.locator("#applications-generate").click()
                first.locator("#application-candidates-accept").click()
                expect(
                    first.locator("#agentix-operation-progress .agentix-busy-panel")
                ).to_be_visible(timeout=15000)
                expect(first.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                # The proposal callback opens review; toggling here would close it.
                expect(first.locator("#applications-files input")).to_be_visible(timeout=15000)
                expect(first.locator("#applications-file-editor .cm-content")).to_contain_text(
                    "create_application"
                )
                expect(first.locator("#applications-review")).to_be_hidden()
                first.locator("#applications-files input").click()
                first.get_by_role(
                    "option", name="count_words_in_text_code.py — tool revision", exact=True
                ).click()
                expect(first.locator("#applications-tool-code")).to_be_visible()
                expect(first.locator("#applications-widget-code")).to_be_visible()
                expect(first.locator("#applications-tool-tests")).to_be_visible()
                expect(first.locator("#applications-save-file")).to_be_enabled()
                # Select a real source file, edit it, explicitly save and require review again.
                first.locator("#applications-files input").click()
                first.get_by_role(
                    "option", name="count_words_in_text_widget.py — editable", exact=True
                ).click()
                code = first.locator("#applications-widget-code .cm-content")
                expect(code).to_contain_text("create_widget")
                code.click()
                first.keyboard.press("Control+End")
                first.keyboard.insert_text("\n# Human reviewed browser edit\n")
                expect(first.locator("#applications-file-hint")).to_contain_text("Unsaved changes")
                first.locator("#applications-save-file").click()
                expect(first.locator("#applications-status")).to_contain_text("Changes saved")
                expect(first.locator("#applications-reviewed input")).not_to_be_checked()
                first.locator("#applications-reviewed input").check()
                first.locator("#applications-approve").click()
                expect(
                    first.locator("#agentix-operation-progress .agentix-busy-panel")
                ).to_be_visible(timeout=15000)
                expect(first.locator("#applications-status")).to_contain_text(
                    "Independent verification failed", timeout=30000
                )
                expect(first.locator("#applications-repair")).to_be_visible(timeout=15000)
                second.goto(url)
                second.get_by_role("tab", name="Applications", exact=True).click()
                expect(second.locator("#applications-repair")).to_be_hidden()
                expect(second.locator("#applications-file-editor")).to_be_hidden()
                first.locator("#applications-repair").click()
                expect(first.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                expect(first.locator("#applications-repair")).to_be_hidden(timeout=10000)
                first.locator("#applications-reviewed input").check()
                first.locator("#applications-approve").click()
                expect(first.locator("#applications-status")).to_contain_text(
                    "Verified.", timeout=300000
                )
                expect(first.locator("#generated-application-heading")).to_contain_text(
                    "Generated Application"
                )
                expect(first.locator("#generated-application")).to_have_count(1)
                expect(first.locator("#applications-repair")).to_be_hidden()
                frame = first.frame_locator("#applications-frame iframe")
                check_analysis(frame, "Hello World!", 2, 3)
                check_analysis(frame, "rhythms", 1, 0)
                assert (
                    first.locator("#generated-application").evaluate(
                        "el => getComputedStyle(el).borderTopStyle"
                    )
                    == "solid"
                )
                # Numeric layout is saved by the maintained host, not executable code.
                edit = frame.locator("#application_edit")
                expect(frame.locator(".application-layout-notice")).to_be_attached(timeout=15000)
                expect(edit).to_be_enabled(timeout=15000)
                edit.click()
                handle = frame.get_by_role(
                    "button", name="move application_words_input", exact=True
                )
                box = handle.bounding_box()
                assert box is not None
                first.mouse.move(box["x"] + 10, box["y"] + 10)
                first.mouse.down()
                first.mouse.move(box["x"] + 40, box["y"] + 25, steps=5)
                first.mouse.up()
                handle.focus()
                first.keyboard.press("ArrowRight")
                first.keyboard.press("ArrowDown")
                frame.get_by_role(
                    "button", name="resize application_words_input", exact=True
                ).focus()
                first.keyboard.press("ArrowRight")
                edit.click()
                expect(frame.locator(".application-layout-notice")).to_have_text("Layout saved")
                configs = list((tmp_path / "installed-apps").glob("*/config.json"))
                assert len(configs) == 1
                saved = json.loads(configs[0].read_bytes())
                assert saved["positions"]["application_words_input"]["x"] >= 10
                assert "application_stop" not in saved["positions"]
                first.screenshot(
                    path=str(ROOT / "docs/reports/v4-031-reviewed-application.png"), full_page=True
                )
                frame.get_by_role("button", name="Close application", exact=True).click()
                expect(first.locator("#applications-frame iframe")).to_have_count(0, timeout=45000)
                expect(
                    first.get_by_text("Use the application as a composite tool", exact=True)
                ).to_be_visible()
                audit = json.loads((tmp_path / "audit.json").read_bytes())
                assert audit["tool_test_runs_during_application_work"] == 0
                assert audit["simulated_verification_failures"] == 1
                assert len(audit["generation_roles"]) == 6
                # A different browser restores the persisted layout and does not
                # regenerate widgets or rerun the old acceptance suite.
                second.locator("#installed-apps-refresh").click()
                second.locator("#installed-apps input").click()
                second.get_by_role("option").filter(has_text="Text analysis").first.click()
                second.locator("#installed-apps-load").click()
                expect(second.locator("#applications-status")).to_contain_text(
                    "Loaded", timeout=15000
                )
                second.locator("#installed-apps-play").click()
                expect(second.locator("#applications-status")).to_contain_text(
                    "Application ready", timeout=180000
                )
                reopened = second.frame_locator("#applications-frame iframe")
                expect(reopened.locator("#application_words_input")).to_have_css(
                    "position", "absolute", timeout=15000
                )
                assert (
                    reopened.locator("#application_words_input").evaluate(
                        "el => parseInt(el.style.left)"
                    )
                    == saved["positions"]["application_words_input"]["x"]
                )
                check_analysis(reopened, "Hello World!", 2, 3)
                reopened.get_by_role("button", name="Close application", exact=True).click()
                expect(second.locator("#applications-frame iframe")).to_have_count(0, timeout=45000)
                assert json.loads((tmp_path / "audit.json").read_bytes()) == audit
                # Publication follows independent success. A new app reuses those
                # exact widgets and requests only a new workflow from the model double.
                first.locator("#applications-query textarea").fill(
                    "Count another text using the same tools"
                )
                first.locator("#applications-name textarea").fill(
                    "Text analysis"
                    if not first.locator("#applications-name textarea").input_value()
                    else "Another text analysis"
                )
                first.locator("#applications-generate").click()
                first.locator("#application-candidates-accept").click()
                expect(first.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                audit = json.loads((tmp_path / "audit.json").read_bytes())
                assert audit["generation_roles"] == [
                    "Widget Designer",
                    "Widget Designer",
                    "Assembler",
                    "Widget Designer",
                    "Widget Designer",
                    "Assembler",
                    "Assembler",
                ]
                expect(first.locator("#applications-reviewed input")).not_to_be_checked()
                first.locator("#applications-reject").click()
                expect(first.locator("#applications-repair")).to_be_hidden()

                browser.close()
        finally:
            if process.poll() is None:
                if os.name == "nt":
                    subprocess.run(
                        ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                        capture_output=True,
                        timeout=15,
                        check=False,
                    )
                else:
                    process.terminate()
                process.wait(timeout=40)
            (ROOT / "docs/reports/v4-031-review-server.log").write_bytes(logpath.read_bytes())


@pytest.mark.parametrize("mode", ["missing", "unapproved"])
def test_missing_or_unapproved_catalog_tool_stops_before_generation(tmp_path, mode):
    """Exercise the real GUI failure path without inference, substitution or execution."""
    from playwright.sync_api import expect, sync_playwright

    port = free_port()
    logpath = tmp_path / "preflight.log"
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
            await_http(f"http://127.0.0.1:{port}", process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                page = browser.new_page()
                page.goto(f"http://127.0.0.1:{port}")
                page.get_by_role("tab", name="Applications", exact=True).click()
                page.locator("#applications-query textarea").fill("Count words and vowels")
                page.locator("#applications-name textarea").fill("Text analysis")
                page.locator("#applications-generate").click()
                expect(page.locator("#application-candidates-status")).to_contain_text(
                    "lack reusable approval", timeout=30000
                )
                expect(page.locator("#application-candidates-accept")).to_be_disabled()
                expect(page.locator("#applications-status")).to_contain_text(
                    "No application has been generated"
                )
                expect(page.locator("#applications-repair")).to_be_hidden()
                expect(page.locator("#applications-frame iframe")).to_have_count(0)
                audit = json.loads((tmp_path / "audit.json").read_bytes())
                assert (
                    audit["generation_roles"] == []
                    and audit["simulated_verification_failures"] == 0
                )
                browser.close()
        finally:
            if process.poll() is None:
                if os.name == "nt":
                    subprocess.run(
                        ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                        capture_output=True,
                        timeout=15,
                        check=False,
                    )
                else:
                    process.terminate()
                process.wait(timeout=40)


def test_modified_tool_requires_normal_gui_approvals(tmp_path):
    """Review changed shared code/tests through Tools before app approval is possible."""
    from playwright.sync_api import expect, sync_playwright

    port = free_port()
    logpath = tmp_path / "tool-revision.log"
    with logpath.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "tests/application_review_server.py"),
                str(port),
                str(tmp_path),
            ],
            cwd=ROOT,
            stdout=log,
            stderr=log,
        )
        try:
            await_http(f"http://127.0.0.1:{port}", process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
                )
                page = browser.new_page()
                page.goto(f"http://127.0.0.1:{port}")
                page.get_by_role("tab", name="Applications", exact=True).click()
                page.locator("#applications-query textarea").fill("Count words and vowels")
                page.locator("#applications-name textarea").fill("Text analysis")
                page.locator("#applications-generate").click()
                page.locator("#application-candidates-accept").click()
                expect(page.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                # The proposal callback opens review; toggling here would close it.
                expect(page.locator("#applications-files input")).to_be_visible(timeout=15000)
                page.locator("#applications-files input").click()
                page.get_by_role(
                    "option", name="count_words_in_text_code.py — tool revision", exact=True
                ).click()
                source = page.locator("#applications-tool-code .cm-content")
                source.click()
                page.keyboard.press("Control+End")
                page.keyboard.insert_text("\n# Explicit reviewed revision\n")
                tests = page.locator("#applications-tool-tests .cm-content")
                tests.click()
                page.keyboard.press("Control+A")
                page.keyboard.insert_text(
                    '"""Reviewed words regression."""\nimport unittest\nfrom count_words_in_text_code import count_words_in_text\nclass Words(unittest.TestCase):\n    def test_normal(self):\n        self.assertEqual(count_words_in_text("Hello World!"),2)\n'
                )
                page.locator("#applications-save-file").click()
                expect(page.locator("#applications-status")).to_contain_text("Changes saved")
                page.locator("#applications-reviewed input").check()
                page.locator("#applications-approve").click()
                expect(page.locator("#applications-status")).to_contain_text(
                    "Review and approve modified tool revisions"
                )
                page.locator("#applications-review-tools").click()
                page.get_by_role("tab", name="Tools", exact=True).click()
                preview = page.get_by_label(
                    "Review and edit file content or acceptance cases before approving", exact=True
                )
                for expected in (
                    "Explicit reviewed revision",
                    "Reviewed words regression",
                    '"cases"',
                ):
                    expect(preview).to_be_visible(timeout=20000)
                    expect(preview).to_have_value(__import__("re").compile(expected), timeout=20000)
                    page.get_by_role("button", name="Approve Reviewed Content", exact=True).click()
                page.get_by_role("tab", name="Applications", exact=True).click()
                expect(page.locator("#applications-status")).to_contain_text(
                    "Tool revisions approved", timeout=45000
                )
                expect(page.locator("#applications-reviewed input")).not_to_be_checked()
                page.screenshot(
                    path=str(ROOT / "docs/reports/v4-036-tool-revision.png"), full_page=True
                )
                browser.close()
        finally:
            if process.poll() is None:
                subprocess.run(
                    ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                    capture_output=True,
                    timeout=20,
                    check=False,
                )
                process.wait(timeout=40)
            (ROOT / "docs/reports/v4-036-tool-revision-server.log").write_bytes(
                logpath.read_bytes()
            )


def test_code_cases_are_visible_editable_and_block_incomplete_approval(tmp_path):
    """V6-045: real Gradio retains missing-case guidance and revokes review on edit."""
    from playwright.sync_api import expect, sync_playwright

    port = free_port()
    url = f"http://127.0.0.1:{port}"
    logpath = tmp_path / "server.log"
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
        )
        try:
            await_http(url, process, logpath)
            with sync_playwright() as driver:
                browser = driver.chromium.launch(
                    executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
                )
                page = browser.new_page()
                page.goto(url)
                page.get_by_role("tab", name="Applications", exact=True).click()
                page.locator("#applications-name textarea").fill("Reviewed cases fixture")
                page.locator("#applications-query textarea").fill("Count words and vowels")
                page.locator("#applications-generate").click()
                page.locator("#application-candidates-accept").click()
                expect(page.locator("#applications-status")).to_contain_text(
                    "Human review required", timeout=45000
                )
                notice = page.locator("#applications-acceptance-notice")
                expect(notice).to_contain_text("expected.second")
                editor = page.locator("#applications-file-editor .cm-content")
                expect(editor).to_be_visible()
                expect(editor).to_contain_text('"amount": 2')
                expect(editor).to_contain_text('"first": 5')
                page.locator("#applications-reviewed input").check()
                page.locator("#applications-approve").click()
                expect(page.locator("#applications-status")).to_contain_text("Verification blocked")
                expect(notice).to_contain_text("expected.second")
                editor.click()
                page.keyboard.press("Control+a")
                page.keyboard.insert_text(
                    json.dumps({"payload": {"amount": 2}, "expected": {"first": 5, "second": 8}})
                )
                expect(page.locator("#applications-reviewed input")).not_to_be_checked()
                page.locator("#applications-save-file").click()
                expect(page.locator("#applications-status")).to_contain_text("Changes saved")
                expect(notice).to_contain_text("structurally valid")
                expect(page.locator("#applications-reviewed input")).not_to_be_checked()
                browser.close()
        finally:
            process.terminate()
            process.wait(timeout=15)
