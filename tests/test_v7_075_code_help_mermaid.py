"""V7-075: code help renders fenced Mermaid diagrams from a local, pinned bundle."""

import hashlib
from pathlib import Path

import pytest

ASSETS = Path("src/agentix/ui/assets")
MERMAID_BUNDLE = ASSETS / "mermaid.min.js"
MERMAID_RENDERER = ASSETS / "mermaid_render.js"
MERMAID_DIGEST = "d0830a6c05546e9edb8fe20a8f545f3e0dc7c4c3134d584bad9c13a99d7a71e0"


@pytest.mark.frameworks
def test_transcript_component_type_is_markdown():
    """Catch a regression back to a Textbox, which cannot render a diagram."""
    import gradio as gr

    from agentix.ui.chathelper import build_chathelper

    class Backend:
        """Minimal composition boundary; the helper only stores it."""

        sessions = None

    with gr.Blocks() as blocks:
        build_chathelper(
            gr,
            Backend(),
            lambda callback: callback,
            gr.Textbox(),
            gr.State(),
            [gr.Code(), gr.Code(), gr.Code(), gr.Code()],
        )
    components = {
        component["props"].get("elem_id"): component
        for component in blocks.get_config_file()["components"]
    }
    assert components["chathelper-transcript"]["type"] == "markdown"


def test_launch_options_embed_the_local_bundle_without_a_network_url():
    """Catch a CDN reference or a renderer that never reaches the page."""
    from agentix.ui.branding import launch_options

    script = launch_options()["js"]
    assert 'globalThis["mermaid"]' in script
    assert "agentix-mermaid-render" in script
    assert "(() => {\n" in script
    for host in ("cdn.jsdelivr.net", "unpkg.com", "cdnjs.cloudflare.com", "esm.sh"):
        assert host not in script
    assert "<script src=" not in script


def test_vendored_bundle_matches_the_pinned_digest():
    """Catch an unreviewed replacement of the third-party bundle."""
    assert MERMAID_BUNDLE.is_file(), "the pinned Mermaid bundle is missing"
    assert hashlib.sha256(MERMAID_BUNDLE.read_bytes()).hexdigest() == MERMAID_DIGEST


def test_renderer_only_targets_the_code_help_transcript():
    """Catch a global selector that would render untrusted application output."""
    source = MERMAID_RENDERER.read_text(encoding="utf-8")
    assert "#chathelper-transcript" in source
    assert "securityLevel" in source and "strict" in source
    assert "document.querySelectorAll('code.language-mermaid')" not in source


@pytest.mark.browser
def test_real_gradio_launch_publishes_mermaid_and_renders_a_fence(tmp_path):
    """Catch the eval-scope defect where the bundle's global assignment throws."""
    import os

    import gradio as gr
    from playwright.sync_api import expect, sync_playwright
    from test_composite_browser import free_port

    from agentix.ui.branding import launch_options

    port = free_port()
    with gr.Blocks() as demo:
        gr.Markdown(
            "```mermaid\ngraph TD; A[Start] --> B[End];\n```",
            elem_id="chathelper-transcript",
        )
    demo.launch(
        server_name="127.0.0.1",
        server_port=port,
        inbrowser=False,
        prevent_thread_lock=True,
        **launch_options(),
    )
    try:
        with sync_playwright() as driver:
            browser = driver.chromium.launch(
                executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
            )
            try:
                page = browser.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.goto(f"http://127.0.0.1:{port}")
                expect(page.locator("#chathelper-transcript svg")).to_have_count(1, timeout=30000)
                assert page.evaluate("() => typeof window.mermaid") == "object"
                assert errors == []
                page.screenshot(path=str(tmp_path / "v7-075-launch.png"))
            finally:
                browser.close()
    finally:
        demo.close()


@pytest.mark.browser
def test_fenced_mermaid_renders_as_svg_inside_the_helper(tmp_path):
    """Render a real diagram, keep other code blocks inert and re-render on update."""
    import os

    from playwright.sync_api import expect, sync_playwright

    html = (
        '<div id="chathelper-window"><div id="chathelper-transcript">'
        '<pre><code class="language-mermaid">graph TD; A[Start] --&gt; B[End];</code></pre>'
        "</div></div>"
        '<div id="outside"><pre><code class="language-mermaid">graph TD; X--&gt;Y;</code></pre></div>'
    )
    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.set_content(html)
            page.add_script_tag(path=str(MERMAID_BUNDLE.resolve()))
            page.add_script_tag(path=str(MERMAID_RENDERER.resolve()))
            expect(page.locator("#chathelper-transcript svg")).to_have_count(1, timeout=20000)
            assert page.locator("#outside svg").count() == 0
            page.evaluate(
                "() => {document.getElementById('chathelper-transcript').innerHTML ="
                "'<pre><code class=\"language-mermaid\">graph LR; C--&gt;D;</code></pre>';}"
            )
            expect(page.locator("#chathelper-transcript svg")).to_have_count(1, timeout=20000)
            assert "C" in (page.locator("#chathelper-transcript svg").text_content() or "")
            page.screenshot(path=str(tmp_path / "v7-075-mermaid.png"))
        finally:
            browser.close()
