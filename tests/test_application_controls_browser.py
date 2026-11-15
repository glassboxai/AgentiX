"""Actual browser cancellation/restart and native owned-process cleanup."""

import hashlib
import json
import os

import pytest
import schema3_package

from agentix.lab.application_artifacts import application_digest, approve_application
from agentix.lab.application_panel import ApplicationPreview


@pytest.mark.browser
@pytest.mark.windows_isolation
def test_native_toolbar_stops_and_restarts_same_reviewed_snapshot(tmp_path):
    """Cancel a slow trusted callback, retain its listener, resume and close its job."""
    from playwright.sync_api import expect, sync_playwright
    from test_composite_browser import check_analysis

    package = schema3_package.package(tmp_path)
    # Slow an application-owned tool, never a maintained runtime member: strict
    # capture compares every SHARED member with the current template and would
    # reject a modified operation.py before the preview starts.
    tool = package / "count_words_in_text_code.py"
    source = tool.read_text(encoding="utf-8")
    assert "    return len(text.split())" in source
    tool.write_text(
        source.replace(
            "    return len(text.split())",
            "    import time\n\n    time.sleep(5)\n    return len(text.split())",
            1,
        ),
        encoding="utf-8",
    )
    manifest = package / "application.json"
    record = json.loads(manifest.read_bytes())
    record["files"] = {
        name: hashlib.sha256((package / name).read_bytes()).hexdigest() for name in record["files"]
    }
    manifest.write_text(json.dumps(record), encoding="utf-8")
    snapshot = approve_application(package, application_digest(package))
    preview = ApplicationPreview(snapshot, None, lifetime=None)
    first_session = preview.session
    try:
        with sync_playwright() as driver:
            browser = driver.chromium.launch(
                executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
            )
            page = browser.new_page()
            page.goto(preview.url)
            page.locator("#application_input_text textarea").fill("Hello World!")
            page.locator("#application_execute").click()
            expect(page.locator("#application_status textarea")).to_have_value(
                "Running", timeout=10000
            )
            expect(page.locator("#application_execute")).to_have_attribute(
                "aria-label", "Stop running application", timeout=5000
            )
            page.locator("#application_execute").click()
            expect(page.locator("#application_paused")).to_have_text(
                "Application stopped.", timeout=45000
            )
            assert not first_session.native_thread.is_alive()
            assert preview.alive and preview.paused and preview.thread.is_alive()
            page.get_by_role("button", name="Resume application", exact=True).click()
            expect(page.locator("#application_input_text textarea")).to_be_visible(timeout=180000)
            assert preview.session is not first_session and not preview.paused
            check_analysis(page, "Hello World!", 2, 3)
            page.get_by_role("button", name="Close application", exact=True).click()
            browser.close()
    finally:
        preview.close()
    assert not preview.thread.is_alive() and not preview.session.native_thread.is_alive()
