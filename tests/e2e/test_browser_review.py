"""E2E-001: real browser review, edited host verdicts and session separation.

No Ollama or existing generated tools participate. The server's execution double
only runs independently authored trusted fixtures, without isolation claims.
"""

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
ROOT = Path(__file__).resolve().parents[2]
EDITOR = "Review and edit file content or acceptance cases before approving"


@pytest.fixture(scope="module")
def server(tmp_path_factory):
    """Own one disposable server; fail visibly on startup errors and always stop it."""
    folder = tmp_path_factory.mktemp("agentix-browser")
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    url = f"http://127.0.0.1:{port}"
    with (folder / "server.log").open("w", encoding="utf-8") as log:
        process = None

        def stop():
            """Stop only the currently owned disposable process tree."""
            nonlocal process
            if process is None:
                return
            if process.poll() is None:
                if os.name == "nt":
                    subprocess.run(
                        ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                        capture_output=True,
                        timeout=10,
                        check=False,
                    )
                else:
                    process.terminate()
                process.wait(timeout=15)
            process = None

        def start():
            """Start the same fixture deployment with retained temporary storage."""
            nonlocal process
            process = subprocess.Popen(
                [
                    sys.executable,
                    str(Path(__file__).with_name("server.py")),
                    str(folder / "artifacts"),
                    str(port),
                ],
                cwd=ROOT,
                stdout=log,
                stderr=log,
            )
            deadline = time.monotonic() + 90
            opener = build_opener(ProxyHandler({}))
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    pytest.fail((folder / "server.log").read_text(encoding="utf-8"))
                try:
                    with opener.open(url, timeout=1) as response:
                        if response.status == 200:
                            return process.pid
                except (URLError, TimeoutError):
                    time.sleep(0.2)
            pytest.fail("Disposable Gradio server did not start within 90 seconds")

        def restart():
            """Replace the owned server process, never the user's live instance."""
            old_pid = process.pid
            stop()
            new_pid = start()
            assert old_pid != new_pid
            return old_pid, new_pid

        try:
            start()
            yield url, folder / "artifacts", restart
        finally:
            stop()


@pytest.fixture
def browser():
    """Use installed Edge by default, or an explicitly configured browser channel."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as driver:
        channel = os.environ.get("AGENTIX_BROWSER_CHANNEL", "msedge")
        instance = driver.chromium.launch(channel=channel or None, headless=True)
        try:
            yield instance
        finally:
            instance.close()


def submit(page, text):
    """Submit through the public browser controls only."""
    if page.viewport_size and page.viewport_size["width"] < 700:
        sidebar = page.locator("#agentix-sidebar.open")
        if sidebar.count():
            sidebar.get_by_role("button", name="Toggle Sidebar").click()
    page.get_by_role("textbox", name="User Query").fill(text)
    page.get_by_role("button", name="Send query", exact=True).click()


def test_edited_acceptance_is_compared_by_host_and_private(browser, server):
    """Verify edited acceptance is compared by host and private."""
    from playwright.sync_api import expect

    alice, bob = browser.new_context(), browser.new_context()
    try:
        page, other = alice.new_page(), bob.new_page()
        page.goto(server[0])
        other.goto(server[0])
        page.get_by_role("checkbox", name="Auto-approve file writes for this session").check()
        submit(page, "acceptance")
        editor = page.get_by_role("textbox", name=EDITOR)
        expect(editor).to_be_visible(timeout=30000)
        page.get_by_text(
            "Generated Python tests (read-only; reject to request changes)", exact=True
        ).click()
        expect(page.get_by_text("class Checks", exact=False)).to_be_visible()
        # A second independent browser must not receive Alice's review or chat.
        submit(other, "Bob private response")
        expect(
            other.get_by_text("Fixture response: Bob private response", exact=False)
        ).to_be_visible(timeout=15000)
        expect(other.get_by_role("textbox", name=EDITOR)).not_to_be_visible()
        expect(page.get_by_text("Bob private response", exact=False)).not_to_be_visible()
        contract = json.loads(editor.input_value())
        contract["cases"][0]["expect"]["value"] = 3
        editor.fill(json.dumps(contract))
        page.get_by_role("button", name="Approve Reviewed Content", exact=False).click()
        expect(page.get_by_text("Verified against approved cases", exact=False)).to_be_visible(
            timeout=30000
        )
        expect(page.get_by_text("sum_case: PASS", exact=False)).to_be_visible()
        page.get_by_text("sum_case: PASS", exact=True).click()
        expect(page.get_by_text('"observed"', exact=False)).to_be_visible()
        if output := os.environ.get("AGENTIX_E2E_ARTIFACTS"):
            destination = Path(output)
            destination.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(destination / "browser-acceptance.png"), full_page=True)
    finally:
        alice.close()
        bob.close()


def test_rejected_acceptance_never_verifies(browser, server):
    """Verify rejected acceptance never verifies."""
    from playwright.sync_api import expect

    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(server[0])
        page.get_by_role("checkbox", name="Auto-approve file writes for this session").check()
        submit(page, "acceptance")
        expect(page.get_by_role("textbox", name=EDITOR)).to_be_visible(timeout=30000)
        page.get_by_role("button", name="Reject Operation", exact=False).click()
        expect(
            page.get_by_text("Human review rejected, expired or cancelled", exact=False)
        ).to_be_visible(timeout=15000)
        expect(page.get_by_text("Verified against approved cases", exact=False)).not_to_be_visible()
    finally:
        context.close()


def test_file_review_uses_edited_content(browser, server):
    """Verify file review uses edited content."""
    from playwright.sync_api import expect

    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(server[0])
        submit(page, "file")
        editor = page.get_by_role("textbox", name=EDITOR)
        # Storage asks separately for directory creation before the file write.
        expect(editor).to_be_visible(timeout=15000)
        expect(editor).to_have_value(re.compile(r"Directory: .*fixture"))
        page.get_by_role("button", name="Approve Reviewed Content", exact=False).click()
        expect(editor).to_have_value("Original specification", timeout=15000)
        editor.fill("Reviewed specification")
        page.get_by_role("button", name="Approve Reviewed Content", exact=False).click()
        expect(editor).not_to_be_visible(timeout=15000)
        expect(page.get_by_text("Success: Content written", exact=False)).to_be_visible(
            timeout=15000
        )
        saved = list(server[1].glob("*/fixture/fixture_specifications.md"))
        assert any(path.read_text(encoding="utf-8") == "Reviewed specification" for path in saved)
    finally:
        context.close()


@pytest.mark.parametrize("width", [1440, 390])
def test_brand_readable_result_and_bounded_disclosures(browser, server, width):
    """Verify actual layout, accessible send control and timer-stable disclosures."""
    from playwright.sync_api import expect

    context = browser.new_context(viewport={"width": width, "height": 1000})
    try:
        page = context.new_page()
        page.goto(server[0])
        expect(page.get_by_role("heading", name="AgentiX", exact=True)).to_be_visible()
        expect(page.get_by_text("Developer-in-the-Loop.", exact=True)).to_be_visible()
        expect(page.get_by_role("img", name="AgentiX logo")).to_be_visible()
        project = page.get_by_role("link", name="The Glass Box AI Project", exact=True)
        expect(project).to_have_attribute("href", "https://glassboxai.dev/")
        expect(project).to_be_visible()
        assert page.locator("h1").evaluate("el => getComputedStyle(el).fontWeight") == "500"
        for selector in ("#agentix-chat", "#send-query", "#validation-panel", "textarea"):
            assert (
                page.locator(selector).first.evaluate("el => getComputedStyle(el).borderRadius")
                == "0px"
            )
        checkbox = page.get_by_role("checkbox", name="Auto-approve file writes for this session")
        expect(checkbox).not_to_be_checked()
        assert checkbox.evaluate("el => getComputedStyle(el).width") == "20px"
        assert checkbox.evaluate("el => getComputedStyle(el).borderWidth") == "2px"
        assert checkbox.evaluate("el => getComputedStyle(el).backgroundColor") == "rgb(11, 13, 17)"
        checkbox.press("Space")
        expect(checkbox).to_be_checked()
        assert (
            checkbox.evaluate("el => getComputedStyle(el).backgroundColor") == "rgb(126, 231, 255)"
        )
        assert checkbox.evaluate("el => getComputedStyle(el).outlineWidth") == "2px"
        checkbox.press("Space")
        expect(checkbox).not_to_be_checked()
        send = page.get_by_role("button", name="Send query", exact=True)
        expect(send).to_be_visible()
        assert send.bounding_box()["width"] < 65
        submit(page, "presentation in euros (€)")
        expect(page.get_by_text("€67.50", exact=False)).to_be_visible(timeout=15000)
        expect(page.locator(".execution-result table")).to_be_visible()
        colors = page.locator(".execution-result > p").first.evaluate("""el => {
            const foreground = getComputedStyle(el).color;
            let node = el, background = '';
            const ancestors = [];
            while (node) {
                const style = getComputedStyle(node);
                ancestors.push({tag:node.tagName, classes:node.className, width:node.clientWidth,
                    background:style.backgroundColor});
                if (!background && style.backgroundColor !== 'rgba(0, 0, 0, 0)') background = style.backgroundColor;
                node = node.parentElement;
            }
            return {foreground, background, ancestors};
        }""")
        if output := os.environ.get("AGENTIX_E2E_ARTIFACTS"):
            Path(output).mkdir(parents=True, exist_ok=True)
            Path(output, f"ui012-colors-{width}.json").write_text(
                json.dumps(colors, indent=2), encoding="utf-8"
            )

        def luminance(color):
            """Provide luminance for the enclosing trusted test fixture."""
            channels = [int(x) / 255 for x in re.findall(r"\d+", color)[:3]]
            values = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in channels]
            return sum(a * b for a, b in zip(values, (0.2126, 0.7152, 0.0722), strict=True))

        lights = sorted([luminance(colors["foreground"]), luminance(colors["background"])])
        assert (lights[1] + 0.05) / (lights[0] + 0.05) >= 4.5, colors
        expect(page.get_by_text("16 passed", exact=False)).to_be_visible()
        expect(page.get_by_text("case_0: PASS", exact=True)).to_be_visible()
        cases = page.locator(".validation-cases")
        assert cases.evaluate("el => el.clientHeight") <= 360
        expect(cases.locator("pre").first).not_to_be_visible()
        page.get_by_text("case_0: PASS", exact=True).click()
        expect(cases.locator("pre").first).to_be_visible()
        # Wait for two public timer updates: disclosures must remain usable.
        page.wait_for_timeout(2200)
        expect(cases.locator("pre").first).to_be_visible()
        catalog = page.locator(".catalog-list")
        expect(catalog.get_by_text("calculate(consumption_kwh)", exact=False)).not_to_be_visible()
        catalog.get_by_text("electricity_bill_calculator", exact=True).click()
        expect(catalog.get_by_text("calculate(consumption_kwh)", exact=False)).to_be_visible()
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        assert "Inter" in page.locator("h1").evaluate("el => getComputedStyle(el).fontFamily")
        if output := os.environ.get("AGENTIX_E2E_ARTIFACTS"):
            destination = Path(output)
            destination.mkdir(parents=True, exist_ok=True)
            page.get_by_role("heading", name="AgentiX", exact=True).scroll_into_view_if_needed()
            page.screenshot(path=str(destination / f"ui012-{width}.png"), full_page=True)
    finally:
        context.close()


def test_model_sidebar_is_hideable_and_key_input_clears(browser, server):
    """Use the native sidebar toggle and validate session-owned model settings."""
    from playwright.sync_api import expect

    context = browser.new_context(viewport={"width": 1440, "height": 1100})
    try:
        page = context.new_page()
        page.goto(server[0])
        sidebar = page.locator("#agentix-sidebar")
        expect(sidebar).to_be_visible()
        expect(sidebar.get_by_text("Model configuration", exact=True)).to_be_visible()
        assert sidebar.get_by_text("Authorization & Test Review", exact=True).count() == 0
        expect(page.get_by_text("Authorization & Test Review", exact=True)).to_be_visible()
        assert page.get_by_text("Authorization & Test Review", exact=True).count() == 1
        page.locator("#refresh-models").click()
        expect(page.locator("#model-status")).to_contain_text("models refreshed", timeout=15000)
        page.locator("#llm-model").get_by_role("combobox").click()
        page.get_by_role("option", name="qwen3:14b", exact=True).click()
        expect(page.locator("#llm-api-key")).not_to_be_visible()
        expect(page.locator("#llm-remote-consent")).not_to_be_visible()
        page.locator("#apply-model").click()
        expect(page.locator("#model-status")).to_contain_text("Ollama", timeout=15000)
        expect(page.locator("#model-status")).to_contain_text("qwen3:14b", timeout=15000)
        submit(page, "model identity")
        expect(page.get_by_text("Configured model: ollama/qwen3:14b", exact=False)).to_be_visible(
            timeout=15000
        )
        destination = Path(os.environ.get("AGENTIX_E2E_ARTIFACTS", str(server[1].parent)))
        destination.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(destination / "model-sidebar.png"), full_page=True)
        toggle = sidebar.get_by_role("button", name="Toggle Sidebar")
        toggle.click()
        expect(page.locator("#apply-model")).not_to_be_visible()
        sidebar.get_by_role("button", name="Toggle Sidebar").click()
        expect(page.locator("#apply-model")).to_be_visible()
    finally:
        context.close()


def test_saved_profile_lifecycle_and_session_consent(browser, server):
    """Create/update/reload/delete a synthetic profile through actual browser UI."""
    from playwright.sync_api import expect

    first = browser.new_context(viewport={"width": 1440, "height": 1100})
    second = browser.new_context(viewport={"width": 1440, "height": 1100})

    def choose(page, selector, label):
        """Select a visible native Gradio dropdown option by its accessible role."""
        page.locator(selector).get_by_role("combobox").click()
        page.get_by_role("option", name=label, exact=True).click()

    try:
        page = first.new_page()
        page.goto(server[0])
        expect(page.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        other = second.new_page()
        other.goto(server[0])
        expect(other.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        choose(page, "#llm-provider", "OpenAI")
        expect(page.get_by_role("textbox", name="API endpoint", exact=True)).to_have_value(
            "https://api.openai.com/v1"
        )
        page.get_by_role("textbox", name="Profile name", exact=True).fill("Synthetic provider")
        page.get_by_role("textbox", name="External model", exact=True).fill("test-model")
        key = page.locator("#llm-api-key input")
        expect(page.get_by_role("textbox", name="API endpoint", exact=True)).to_have_value(
            "https://api.openai.com/v1"
        )
        expect(page.get_by_role("textbox", name="External model", exact=True)).to_have_value(
            "test-model"
        )
        key.fill("synthetic-browser-profile-key")
        page.locator("#save-profile").click()
        expect(key).to_have_value("", timeout=15000)
        expect(page.locator("#model-status")).to_contain_text("Profile saved", timeout=15000)
        assert not page.locator("#llm-remote-consent input").is_checked()
        page.locator("#apply-model").click()
        expect(page.locator("#model-status")).to_contain_text("not applied", timeout=15000)
        page.locator("#llm-remote-consent input").check()
        page.locator("#apply-model").click()
        expect(page.locator("#model-status")).to_contain_text(
            "Active provider: OpenAI", timeout=15000
        )
        other.locator("#refresh-profiles").click()
        expect(other.locator("#model-status")).to_contain_text(
            "Saved profiles refreshed", timeout=15000
        )
        choose(other, "#saved-profiles", "Synthetic provider")
        expect(other.get_by_role("textbox", name="Profile name", exact=True)).to_have_value(
            "Synthetic provider", timeout=15000
        )
        expect(other.locator("#llm-api-key input")).to_have_value("")
        assert not other.locator("#llm-remote-consent input").is_checked()
        submit(page, "model identity")
        expect(page.get_by_text("Configured model: openai/test-model", exact=False)).to_be_visible(
            timeout=15000
        )
        other.get_by_role("textbox", name="Profile name", exact=True).fill("Updated synthetic")
        other.locator("#save-profile").click()
        expect(other.locator("#model-status")).to_contain_text("Profile saved", timeout=15000)
        other.locator("#delete-profile").click()
        expect(other.locator("#model-status")).to_contain_text("credentials deleted", timeout=15000)
        other.locator("#refresh-profiles").click()
        expect(other.locator("#model-status")).to_contain_text(
            "Saved profiles refreshed", timeout=15000
        )
        other.locator("#saved-profiles").get_by_role("combobox").click()
        expect(other.get_by_role("option", name="Updated synthetic", exact=True)).to_have_count(0)
        other.locator("#saved-profiles").get_by_role("combobox").press("Escape")
        assert not list((server[1] / "model-profiles").glob("*.json"))
        assert "synthetic-browser-profile-key" not in page.locator("body").inner_text()
    finally:
        first.close()
        second.close()


def test_local_secret_controls_and_sidebar_button_colors(browser, server):
    """Match the reference palette and clear external-only inputs on provider changes."""
    from playwright.sync_api import expect

    context = browser.new_context(viewport={"width": 1440, "height": 1100})
    try:
        page = context.new_page()
        page.goto(server[0])
        expect(page.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        expect(page.locator("#llm-api-key")).not_to_be_visible()
        expect(page.locator("#llm-remote-consent")).not_to_be_visible()
        for identifier in (
            "refresh-models",
            "save-profile",
            "delete-profile",
            "refresh-profiles",
            "apply-model",
        ):
            button = page.locator("#" + identifier)
            assert (
                button.evaluate("el => getComputedStyle(el).backgroundColor")
                == "rgba(255, 255, 255, 0.035)"
            )
            assert button.evaluate("el => getComputedStyle(el).color") == "rgb(241, 243, 245)"
        page.locator("#llm-provider").get_by_role("combobox").click()
        page.get_by_role("option", name="OpenAI", exact=True).click()
        expect(page.locator("#llm-api-key")).to_be_visible()
        expect(page.locator("#llm-api-key input")).to_have_attribute("type", "password")
        expect(page.locator("#llm-remote-consent")).to_be_visible()
        page.locator("#llm-api-key input").fill("synthetic-switch-key")
        page.locator("#llm-remote-consent input").check()
        page.locator("#llm-provider").get_by_role("combobox").click()
        page.get_by_role("option", name="Ollama", exact=True).click()
        expect(page.locator("#llm-api-key")).not_to_be_visible()
        expect(page.locator("#llm-remote-consent")).not_to_be_visible()
        page.locator("#llm-provider").get_by_role("combobox").click()
        page.get_by_role("option", name="OpenAI", exact=True).click()
        expect(page.locator("#llm-api-key input")).to_have_value("")
        expect(page.locator("#llm-remote-consent input")).not_to_be_checked()
    finally:
        context.close()


def test_local_profile_save_refresh_reload_and_delete(browser, server):
    """Reproduce the user's local Save then Refresh flow with persistent metadata."""
    from playwright.sync_api import expect

    first, second = browser.new_context(), browser.new_context()
    try:
        page = first.new_page()
        page.goto(server[0])
        expect(page.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        page.get_by_role("textbox", name="Profile name", exact=True).fill("Qwen3-coder:30b")
        page.locator("#save-profile").click()
        expect(page.locator("#model-status")).to_contain_text("Profile saved", timeout=15000)
        page.locator("#refresh-profiles").click()
        expect(page.locator("#model-status")).to_contain_text(
            "Saved profiles refreshed", timeout=15000
        )
        other = second.new_page()
        other.goto(server[0])
        expect(other.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        other.locator("#saved-profiles").get_by_role("combobox").click()
        other.get_by_role("option", name="Qwen3-coder:30b", exact=True).click()
        expect(other.get_by_role("textbox", name="Profile name", exact=True)).to_have_value(
            "Qwen3-coder:30b", timeout=15000
        )
        expect(other.locator("#llm-api-key")).not_to_be_visible()
        other.locator("#apply-model").click()
        expect(other.locator("#model-status")).to_contain_text(
            "Active provider: Ollama", timeout=15000
        )
        submit(other, "model identity")
        expect(
            other.get_by_text("Configured model: ollama/qwen3-coder:30b", exact=False)
        ).to_be_visible(timeout=15000)
        other.locator("#delete-profile").click()
        expect(other.locator("#model-status")).to_contain_text("credentials deleted", timeout=15000)
        assert not list((server[1] / "model-profiles").glob("*.json"))
    finally:
        first.close()
        second.close()


def test_external_save_failure_survives_refresh_with_safe_reason(browser, server):
    """A simulated vault denial is visible after the user's Save then Refresh sequence."""
    from playwright.sync_api import expect

    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(server[0])
        expect(page.locator("#model-status")).to_contain_text("refreshed", timeout=15000)
        page.locator("#llm-provider").get_by_role("combobox").click()
        page.get_by_role("option", name="OpenAI", exact=True).click()
        expect(page.get_by_role("textbox", name="API endpoint", exact=True)).to_have_value(
            "https://api.openai.com/v1"
        )
        page.get_by_role("textbox", name="Profile name", exact=True).fill(
            "Denied synthetic profile"
        )
        page.get_by_role("textbox", name="External model", exact=True).fill("test-model")
        page.locator("#llm-api-key input").fill("synthetic-denied-vault-key")
        page.locator("#save-profile").click()
        expect(page.locator("#model-status")).to_contain_text("[credential_write]", timeout=15000)
        expect(page.locator("#llm-api-key input")).to_have_value("")
        page.locator("#refresh-profiles").click()
        expect(page.locator("#model-status")).to_contain_text("Last save failed", timeout=15000)
        expect(page.locator("#model-status")).to_contain_text("[credential_write]")
        assert "private-vault-diagnostic" not in page.locator("body").inner_text()
    finally:
        context.close()


def test_reviewed_tool_reuse_has_fresh_result_without_review(browser, server):
    """Exercise first review and later new inputs through actual Gradio controls."""
    from playwright.sync_api import expect

    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(server[0])
        page.get_by_role("checkbox", name="Auto-approve file writes for this session").check()
        submit(page, "reuse create")
        editor = page.get_by_role("textbox", name=EDITOR)
        expect(editor).to_be_visible(timeout=10000)
        # Review remains in the right workspace when model settings are closed.
        assert page.locator("#agentix-sidebar").get_by_role("textbox", name=EDITOR).count() == 0
        validation_box = page.locator("#validation-panel").bounding_box()
        editor_box = editor.bounding_box()
        assert editor_box["y"] >= validation_box["y"] + validation_box["height"]
        page.locator("#agentix-sidebar").get_by_role("button", name="Toggle Sidebar").click()
        expect(editor).to_be_visible()
        contract = json.loads(editor.input_value())
        assert contract["cases"][0]["expect"]["value"] == 12
        page.get_by_role("button", name="Approve Reviewed Content", exact=False).click()
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(1, timeout=20000)
        expect(page.locator("#agentix-chat .execution-result").last).to_contain_text("12")
        submit(page, "reuse next")
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(2, timeout=20000)
        expect(page.locator("#agentix-chat .execution-result").last).to_contain_text("42")
        expect(editor).not_to_be_visible()
        result = page.locator("#agentix-chat .execution-result").last
        expect(result).to_contain_text("Review requests: 1")
        expect(result).to_contain_text("Test runs: 1")
    finally:
        context.close()


def test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift(browser, server):
    """Use actual GUI approval and native protected storage across runtime loss."""
    from playwright.sync_api import expect

    context, other_context = browser.new_context(), browser.new_context()
    try:
        page = context.new_page()
        page.goto(server[0])
        page.get_by_role("checkbox", name="Auto-approve file writes for this session").check()
        submit(page, "durable create")
        editor = page.get_by_role("textbox", name=EDITOR)
        expect(editor).to_be_visible(timeout=15000)
        assert json.loads(editor.input_value())["cases"][0]["expect"]["value"] == 12
        expect(
            page.get_by_text("Approval will be remembered for future sessions", exact=False)
        ).to_be_visible()
        contrast = page.get_by_role("heading", name="Human acceptance review", exact=True).evaluate("""el => {
            const rgb = text => text.match(/[0-9.]+/g).map(Number);
            const luminance = values => values.slice(0,3).map(v => { v/=255; return v<=0.04045 ? v/12.92 : ((v+0.055)/1.055)**2.4; }).reduce((sum,v,i) => sum+v*[0.2126,0.7152,0.0722][i],0);
            const foreground = luminance(rgb(getComputedStyle(el).color));
            for (let node=el; node; node=node.parentElement) {
                const background=rgb(getComputedStyle(node).backgroundColor);
                if (background.length===3 || background[3]>=0.99) {
                    const value=luminance(background);
                    return (Math.max(foreground,value)+0.05)/(Math.min(foreground,value)+0.05);
                }
            }
            return 0;
        }""")
        background_chain = page.get_by_role(
            "heading", name="Human acceptance review", exact=True
        ).evaluate("""el => {
            const result=[];
            for (let node=el; node; node=node.parentElement) result.push({tag:node.tagName,id:node.id,classes:node.className,background:getComputedStyle(node).backgroundColor});
            return result;
        }""")
        assert contrast >= 4.5, "Human review must remain readable: " + json.dumps(background_chain)

        if capture := os.environ.get("AGENTIX_E2E_ARTIFACTS"):
            Path(capture).mkdir(parents=True, exist_ok=True)
            page.screenshot(
                path=str(Path(capture) / "readable-review-below-validation.png"), full_page=True
            )

        page.get_by_role("button", name="Approve Reviewed Content", exact=False).click()
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(1, timeout=20000)
        expect(page.locator("#agentix-chat .execution-result")).to_contain_text("12")
        page.reload()
        submit(page, "durable next")
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(1, timeout=20000)
        expect(page.locator("#agentix-chat .execution-result")).to_contain_text("42")
        expect(editor).not_to_be_visible()
        expect(page.locator("#agentix-chat .execution-result")).to_contain_text("Test runs: 0")
        other = other_context.new_page()
        other.goto(server[0])
        submit(other, "durable next")
        expect(other.locator("#agentix-chat .execution-result")).to_have_count(1, timeout=20000)
        expect(other.locator("#agentix-chat .execution-result")).to_contain_text("42")
        expect(other.get_by_role("textbox", name=EDITOR)).not_to_be_visible()
        server[2]()
        page.reload()
        submit(page, "durable next")
        expect(page.locator("#agentix-chat .execution-result")).to_have_count(1, timeout=20000)
        expect(page.locator("#agentix-chat .execution-result")).to_contain_text("42")
        expect(page.locator("#agentix-chat .execution-result")).to_contain_text(
            "Review requests: 0"
        )
        expect(editor).not_to_be_visible()
        output = Path(os.environ.get("AGENTIX_E2E_ARTIFACTS", str(server[1].parent)))
        output.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(output / "durable-reuse-after-restart.png"), full_page=True)
        page.get_by_role("checkbox", name="Auto-approve file writes for this session").check()
        submit(page, "durable mutate")
        expect(page.get_by_text("Trusted fixture source changed", exact=False)).to_be_visible(
            timeout=10000
        )
        submit(page, "durable next")
        expect(editor).to_be_visible(timeout=20000)
        assert page.locator("#agentix-sidebar").get_by_role("textbox", name=EDITOR).count() == 0
        page.screenshot(
            path=str(output / "review-required-after-source-change.png"), full_page=True
        )
        page.get_by_role("button", name="Reject Operation", exact=False).click()
        expect(
            page.get_by_text("Human review rejected, expired or cancelled", exact=False)
        ).to_be_visible(timeout=10000)
    finally:
        context.close()
        other_context.close()
