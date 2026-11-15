"""Real native Gradio edit handles for text, numeric output and action controls."""

import os

import pytest

pytestmark = [pytest.mark.browser, pytest.mark.windows_isolation]


def test_all_controls_have_unclipped_edit_handles(tmp_path):
    """Catch input/output overflow clipping and visible empty container borders."""
    from playwright.sync_api import expect, sync_playwright
    from test_installed_apps import published_with_tools

    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_panel import ApplicationPreview

    service, app, fixture = published_with_tools(tmp_path)
    preview = ApplicationPreview(approve_application(app.package, app.digest), None, lifetime=None)
    preview.configure_layout(service, app.id, lambda: None)
    session = preview.session
    try:
        with sync_playwright() as driver:
            browser = driver.chromium.launch(
                executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
            )
            page = browser.new_page(viewport={"width": 1400, "height": 1000})
            page.goto(preview.url)
            expect(page.locator("#application_edit")).to_be_visible()
            page.wait_for_function(
                "() => document.querySelector('.application-canvas')"
                "?.classList.contains('application-layout-active')"
                " || document.querySelector('.application-layout-notice') !== null"
            )
            page.locator("#application_edit").click()
            expect(page.locator("#application_edit")).to_have_attribute("aria-pressed", "true")
            for identity in [
                "application_input_text",
                "application_count_words_in_text_input",
                "application_count_words_in_text_output",
                "application_count_vowels_in_text_input",
                "application_count_vowels_in_text_output",
                "application_status",
            ]:
                control = page.locator("#" + identity)
                handle = control.locator(".application-layout-handle.move")
                expect(handle).to_be_visible()
                expect(page.get_by_label("visible " + identity)).to_be_visible()
                assert control.evaluate("e => getComputedStyle(e).overflow") == "visible"
                control.hover()
                assert control.evaluate("e => getComputedStyle(e).boxShadow") != "none"
                bounds = control.bounding_box()
                grip = handle.bounding_box()
                assert grip["y"] >= bounds["y"]
            assert page.locator(".application-canvas .form").evaluate_all(
                "nodes => nodes.every(e => getComputedStyle(e).borderTopWidth === '0px')"
            )
            groups = page.locator(".application-canvas .gr-group")
            assert groups.count() > 0
            assert groups.evaluate_all(
                "nodes => nodes.every(e => getComputedStyle(e).borderTopWidth === '0px'"
                " && getComputedStyle(e).backgroundColor === 'rgba(0, 0, 0, 0)')"
            )
            page.screenshot(
                path=str(
                    __import__("pathlib").Path(__file__).resolve().parents[1]
                    / "docs/reports/v5-037-edit-handles.png"
                ),
                full_page=True,
            )
            browser.close()
    finally:
        preview.close()
    assert not session.native_thread.is_alive()
