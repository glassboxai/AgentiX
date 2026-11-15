"""Opt-in real model GUI trial with a separate explicit engineer-review gate.

The test cannot approve generated code on its own. An operator must read the
captured snapshot and provide its exact SHA-256 and explicit decision externally.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest
from test_composite_browser import await_http, free_port

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


def test_live_v4_application_with_human_review(tmp_path):
    """Use an English problem-only query and actual local model/native/browser gates."""
    if os.environ.get("AGENTIX_V4_LIVE") != "1":
        pytest.skip("Explicit real-model trial required")
    from playwright.sync_api import expect, sync_playwright

    trial = os.environ.get("AGENTIX_V4_TRIAL", "v4-live")
    assert re.fullmatch(r"[a-z0-9-]{1,48}", trial)
    recovery_package = os.environ.get("AGENTIX_V4_RECOVER_PACKAGE")
    recovery_review = os.environ.get("AGENTIX_V4_RECOVER_REVIEW")
    assert bool(recovery_package) == bool(recovery_review)
    port = free_port()
    capture = ROOT / ("docs/reports/" + trial + "-review.json")
    decision = ROOT / ("docs/reports/" + trial + "-review-decision.json")
    if capture.exists() or decision.exists():
        pytest.fail("Preserve prior evidence and select a fresh trial before rerunning")
    logpath = tmp_path / "live-server.log"
    with logpath.open("w", encoding="utf-8") as log:
        env = dict(
            os.environ,
            AGENTIX_SERVER_PORT=str(port),
            AGENTIX_OPEN_BROWSER="false",
            AGENTIX_TOOLS_ROOT=str(tmp_path / "new-tools"),
            GRADIO_ANALYTICS_ENABLED="False",
        )
        process = subprocess.Popen(
            (
                [
                    sys.executable,
                    str(ROOT / "tests/recover_review_server.py"),
                    str(port),
                    str(tmp_path / "recovered"),
                    recovery_package,
                    recovery_review,
                ]
                if recovery_package
                else [sys.executable, str(ROOT / "app.py")]
            ),
            cwd=ROOT,
            env=env,
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
                page.get_by_role("tab", name="Applications", exact=True).click()
                query = "I need an app where I can enter some text and see how many words and vowels it contains."
                page.locator("#applications-query textarea").fill(query)
                page.locator("#applications-generate").click()
                expect(page.locator("#applications-status")).to_contain_text(
                    re.compile("Human review required|generation failed"), timeout=420000
                )
                assert "Human review required" in page.locator("#applications-status").inner_text()
                page.get_by_text(
                    "Application source, proposed tests and acceptance review", exact=True
                ).click()
                snapshot = page.locator("#applications-review textarea").input_value()
                capture.write_bytes(snapshot.encode("utf-8"))
                review_hash = hashlib.sha256(snapshot.encode("utf-8")).hexdigest()
                deadline = time.monotonic() + 1200
                while not decision.exists() and time.monotonic() < deadline:
                    time.sleep(1)
                assert decision.exists(), "Independent engineer decision was not supplied"
                reviewed = json.loads(decision.read_bytes())
                assert reviewed == {"decision": "approve", "review_sha256": review_hash}, (
                    "Engineer rejected the generated candidate"
                )
                page.locator("#applications-reviewed input").check()
                page.locator("#applications-approve").click()
                expect(page.locator("#applications-status")).to_contain_text(
                    re.compile(r"Verified\.|Independent verification failed"), timeout=300000
                )
                assert "Verified." in page.locator("#applications-status").inner_text()
                frame = page.frame_locator("#applications-frame iframe")
                for text, expected in [
                    ("Hello World!", "3"),
                    ("AEIOUaeiou", "10"),
                    ("rhythms", "0"),
                ]:
                    frame.locator("#application_vowels_input textarea").fill(text)
                    frame.locator("#application_vowels_execute").click()
                    expect(frame.locator("#application_vowels_output input")).to_have_value(
                        expected, timeout=45000
                    )
                # The common sidebar opens on demand and survives tab switches.
                page.get_by_role("tab", name="Tools", exact=True).click()
                page.locator("#agentix-sidebar").get_by_role(
                    "button", name="Toggle Sidebar"
                ).click()
                expect(page.locator("#llm-provider")).to_be_visible()
                page.get_by_role("tab", name="Applications", exact=True).click()
                expect(frame.locator("#application_vowels_input textarea")).to_have_value("rhythms")
                page.screenshot(
                    path=str(ROOT / ("docs/reports/" + trial + "-gui.png")), full_page=True
                )
                frame.get_by_role("button", name="Close application", exact=True).click()
                expect(page.locator("#applications-frame iframe")).to_have_count(0, timeout=45000)
                (ROOT / ("docs/reports/" + trial + "-result.json")).write_text(
                    json.dumps(
                        {
                            "query": query,
                            "review_sha256": review_hash,
                            "model": "qwen3-coder:30b",
                            "browser": browser.version,
                            "status": "passed",
                            "independent_review": True,
                            "fresh_model_generation": not bool(recovery_package),
                            "recovered_review": recovery_review,
                        }
                    ),
                    encoding="utf-8",
                )
                browser.close()
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=35)
            (ROOT / ("docs/reports/" + trial + "-server.log")).write_bytes(logpath.read_bytes())
