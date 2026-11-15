"""The right-click style window is driven by the framed widget and the parent bridge."""

from pathlib import Path

import pytest

ASSETS = Path("src/agentix/ui/assets")


@pytest.mark.browser
def test_v7_076_editor_posts_the_right_clicked_widget_tool() -> None:
    """Only a widget control of one tool reports its tool name for styling."""
    import os

    from playwright.sync_api import sync_playwright

    from agentix.layout_contracts import application_layout_groups, application_layout_ids

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    groups = application_layout_groups(manifest)
    positions = {
        name: {"x": 10, "y": 10 + index * 80, "width": 200, "height": 60}
        for index, name in enumerate(sorted(allowed))
    }
    html = (
        '<button id="application_edit">Edit</button>'
        '<div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px"><input value="x"></div>'
            for name in sorted(allowed)
        )
        + "</div>"
    )

    def route(request_route) -> None:
        """Serve inert HTML and the authorized layout payload."""
        if request_route.request.url.endswith("/_agentix/layout"):
            request_route.fulfill(
                json={
                    "editable": True,
                    "token": "fixture",
                    "controls": sorted(allowed),
                    "groups": groups,
                    "layout": {"version": 1, "positions": positions},
                }
            )
        else:
            request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.add_init_script(
                "window.__style = [];"
                "addEventListener('message', event => {"
                "if (event.data && event.data.type === 'agentix-widget-style') "
                "window.__style.push(event.data);});"
            )
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(path=str((ASSETS / "application_editor.js").resolve()))
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            page.locator("#application_first_output input").click(button="right")
            page.wait_for_timeout(300)
            assert page.evaluate("window.__style") == []
            page.locator("#application_edit").click()
            page.wait_for_timeout(200)
            page.locator("#application_first_output input").click(button="right")
            page.wait_for_function("window.__style.length === 1")
            assert page.evaluate("window.__style") == [
                {"type": "agentix-widget-style", "tool": "calculator"}
            ]
            page.locator("#application_status input").click(button="right")
            page.locator("#application_input_text input").click(button="right")
            page.wait_for_timeout(200)
            assert len(page.evaluate("window.__style")) == 1
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_076_saved_stylesheet_is_applied_to_the_live_widget() -> None:
    """The parent bridge pushes the merged CSS and the framed widget restyles."""
    import json
    import os

    from playwright.sync_api import sync_playwright

    from agentix.layout_contracts import application_layout_groups, application_layout_ids

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    groups = application_layout_groups(manifest)
    positions = {
        name: {"x": 10, "y": 10 + index * 80, "width": 200, "height": 60}
        for index, name in enumerate(sorted(allowed))
    }
    child = (
        f"<style>{(ASSETS / 'style.css').read_text(encoding='utf-8')}</style>"
        '<button id="application_edit">Edit</button>'
        '<div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" class="application-editable-element" '
            'style="width:200px;height:60px"><label><span>Caption</span>'
            '<input value="x"></label></div>'
            for name in sorted(allowed)
        )
        + "</div>"
    )
    parent = (
        '<div id="applications-frame"><iframe id="child" src="/child"></iframe></div>'
        '<div id="applications-widget-style-apply"><textarea></textarea></div>'
    )

    def route(request_route) -> None:
        """Serve the parent shell, the framed preview and its layout payload."""
        url = request_route.request.url
        if url.endswith("/_agentix/layout"):
            request_route.fulfill(
                json={
                    "editable": True,
                    "token": "fixture",
                    "controls": sorted(allowed),
                    "groups": groups,
                    "layout": {"version": 1, "positions": positions},
                }
            )
        elif url.endswith("/child"):
            request_route.fulfill(content_type="text/html", body=child)
        else:
            request_route.fulfill(content_type="text/html", body=parent)

    css = (
        ':where([id^="application_calculator_"]) { border-radius: 12px; '
        "background-color: #26177d; font-family: Tahoma; font-size: 20px; }"
        '\n:where([id^="application_calculator_"]) label { font-family: Georgia; font-size: 27px; }'
    )
    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(path=str((ASSETS / "widget_style.js").resolve()))
            frame = page.frame_locator("#child")
            frame.locator("body").evaluate(
                "body => body.ownerDocument.defaultView.eval("
                + json.dumps((ASSETS / "application_editor.js").read_text(encoding="utf-8"))
                + ")"
            )
            frame.locator("#application_first_output").wait_for(state="attached")
            page.evaluate(
                "payload => {const field = document.querySelector("
                "'#applications-widget-style-apply textarea');"
                "field.value = payload;}",
                json.dumps({"tool": "calculator", "ids": ["first"], "css": css}),
            )
            page.wait_for_timeout(900)
            applied = frame.locator("#application_first_output").evaluate(
                "node => {const s = getComputedStyle(node);"
                "return [s.borderRadius, s.backgroundColor, s.fontFamily, s.fontSize];}"
            )
            assert applied == ["12px", "rgb(38, 23, 125)", "Tahoma", "20px"]
            value_and_caption = frame.locator("#application_first_output").evaluate(
                "node => [getComputedStyle(node.querySelector('input')).fontSize,"
                "getComputedStyle(node.querySelector('label span')).fontSize]"
            )
            assert value_and_caption == ["20px", "27px"]
            changed = css.replace("font-size: 20px", "font-size: 13px").replace(
                "font-size: 27px", "font-size: 30px"
            )
            page.evaluate(
                "payload => document.querySelector("
                "'#applications-widget-style-apply textarea').value = payload",
                json.dumps({"tool": "calculator", "ids": ["first"], "css": changed}),
            )
            page.wait_for_timeout(900)
            assert frame.locator("#application_first_output").evaluate(
                "node => [getComputedStyle(node.querySelector('input')).fontSize,"
                "getComputedStyle(node.querySelector('label span')).fontSize]"
            ) == ["13px", "30px"]
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_076_window_can_be_dragged_by_its_title() -> None:
    """The overlay follows the pointer from its title bar and stays on screen.

    The real ``style.css`` is loaded on purpose: its ``!important`` position rules
    are what made an inline left/top drag jump and freeze.
    """
    import os

    from playwright.sync_api import sync_playwright

    stylesheet = (ASSETS / "style.css").read_text(encoding="utf-8")
    html = (
        f"<style>{stylesheet}</style>"
        '<div id="agentix-widget-style-dialog"><div id="agentix-widget-style-title">'
        "Widget style</div></div>"
    )

    def route(request_route) -> None:
        """Serve one inert overlay page with the maintained stylesheet."""
        request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page(viewport={"width": 1400, "height": 900})
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(path=str((ASSETS / "widget_style.js").resolve()))
            dialog = page.locator("#agentix-widget-style-dialog")
            title = page.locator("#agentix-widget-style-title")
            start = dialog.bounding_box()
            box = title.bounding_box()
            page.mouse.move(box["x"] + 20, box["y"] + 10)
            page.mouse.down()
            page.mouse.move(box["x"] + 40, box["y"] + 40, steps=3)
            nudged = dialog.bounding_box()
            assert round(nudged["x"] - start["x"]) == 20
            assert round(nudged["y"] - start["y"]) == 30
            page.mouse.move(box["x"] + 120, box["y"] + 70, steps=5)
            page.mouse.up()
            moved = dialog.bounding_box()
            assert round(moved["x"] - start["x"]) == 100
            assert round(moved["y"] - start["y"]) == 60
            box = title.bounding_box()
            page.mouse.move(box["x"] + 20, box["y"] + 10)
            page.mouse.down()
            page.mouse.move(-900, -900, steps=5)
            page.mouse.up()
            clamped = dialog.bounding_box()
            assert clamped["x"] == 0 and clamped["y"] == 0
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_076_served_stylesheet_applies_without_the_parent_bridge() -> None:
    """The standalone page behind "View as web" renders the saved style on its own."""
    import os

    from playwright.sync_api import sync_playwright

    from agentix.lab.application_session import served_style

    css = (
        b':where([id^="application_calculator_"]) { border-radius: 22px; '
        b"background-color: #26177d; font-family: Georgia; font-size: 28px; }"
    )
    served = served_style(css, "calculator", "multiplier").decode()
    html = (
        f"<style>{(ASSETS / 'style.css').read_text(encoding='utf-8')}</style>"
        f"<style>{served}</style>"
        '<div id="application_multiplier_output" class="application-editable-element">'
        '<label>First number</label><input value="3"></div>'
    )

    def route(request_route) -> None:
        """Serve one inert standalone page with the served stylesheet only."""
        request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page(viewport={"width": 1200, "height": 900})
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.wait_for_selector("#application_multiplier_output")
            node = page.locator("#application_multiplier_output").evaluate(
                "n => {const s = getComputedStyle(n);"
                "return [s.borderRadius, s.backgroundColor, s.fontFamily, s.fontSize];}"
            )
            assert node == ["22px", "rgb(38, 23, 125)", "Georgia", "28px"]
            control = page.locator("#application_multiplier_output input").evaluate(
                "n => {const s = getComputedStyle(n); return [s.fontFamily, s.fontSize];}"
            )
            assert control == ["Georgia", "28px"]
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_077_field_and_caption_are_styled_in_the_served_page() -> None:
    """The field box and the caption get their own colour, family and size."""
    import os

    from playwright.sync_api import sync_playwright

    from agentix.lab.application_session import served_style
    from agentix.widgets.style_editor import StyleValues, merge_style
    from agentix.widgets.styles import default_widget_css

    merged = merge_style(
        default_widget_css("calculator"),
        "calculator",
        StyleValues(12, 2, "#abcdef", "#10141c", "Arial", 20, "#26177d", "Georgia", 28),
    )
    served = served_style(merged.encode(), "calculator", "multiplier").decode()
    html = (
        f"<style>{(ASSETS / 'style.css').read_text(encoding='utf-8')}</style>"
        f"<style>{served}</style>"
        '<div id="application_multiplier_output" class="application-editable-element">'
        '<label><span>First number</span></label><input value="3"></div>'
    )

    def route(request_route) -> None:
        """Serve one inert standalone page with the served stylesheet only."""
        request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page(viewport={"width": 1200, "height": 900})
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.wait_for_selector("#application_multiplier_output")
            field = page.locator("#application_multiplier_output input").evaluate(
                "n => getComputedStyle(n).backgroundColor"
            )
            assert field == "rgb(38, 23, 125)"
            caption = page.locator("#application_multiplier_output label").evaluate(
                "n => {const s = getComputedStyle(n); return [s.fontFamily, s.fontSize];}"
            )
            assert caption == ["Georgia", "28px"]
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_076_saved_web_style_overrides_gradio_startup_snapshot(tmp_path) -> None:
    """A web reload must beat Gradio's earlier, more specific startup copy."""
    import os
    from types import SimpleNamespace

    from playwright.sync_api import sync_playwright

    from agentix.lab.application_session import STYLE_MARKER, ApplicationSession, served_style
    from agentix.widgets.style_editor import StyleValues, merge_style
    from agentix.widgets.styles import default_widget_css

    original = merge_style(
        default_widget_css("calculator"),
        "calculator",
        StyleValues(44, 2, "#abcdef", "#10141c", "Verdana", 8, "#26177d", "system-ui", 20),
    )
    updated = merge_style(
        original,
        "calculator",
        StyleValues(44, 2, "#abcdef", "#10141c", "Verdana", 8, "#224466", "Georgia", 31),
    )
    startup = served_style(original.encode(), "calculator", "multiplier").decode()
    session = object.__new__(ApplicationSession)
    session.root = tmp_path
    session.application = SimpleNamespace(files=(("calculator_widget.css", original.encode()),))
    session.manifest = {"widgets": [{"id": "multiplier", "tool": "calculator"}]}
    (tmp_path / "application.css").write_bytes(b"/* base */\n" + STYLE_MARKER + startup.encode())
    session.restage_styles("calculator_widget.css", updated)
    latest = (tmp_path / "application.css").read_bytes().split(STYLE_MARKER, 1)[1].decode()
    prefixed = startup.replace(
        '[id^="application_multiplier_"]',
        '.gradio-container.gradio-container-6-30-0 .contain [id^="application_multiplier_"]',
    )
    html = (
        f"<style>{prefixed}</style><style>{latest}</style>"
        '<div class="gradio-container gradio-container-6-30-0"><div class="contain">'
        '<div id="application_multiplier_output"><label><span>Result</span></label>'
        '<input value="8"></div></div></div>'
    )
    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.set_content(html)
            assert page.locator("#application_multiplier_output label span").evaluate(
                "e => [getComputedStyle(e).fontFamily, getComputedStyle(e).fontSize]"
            ) == ["Georgia", "31px"]
            assert (
                page.locator("#application_multiplier_output input").evaluate(
                    "e => getComputedStyle(e).backgroundColor"
                )
                == "rgb(34, 68, 102)"
            )
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_077_window_is_compact_and_scrolls_inside_itself() -> None:
    """The window stays narrow and scrolls with the shared thin scrollbar."""
    import os

    from playwright.sync_api import sync_playwright

    stylesheet = (ASSETS / "style.css").read_text(encoding="utf-8")
    rows = "".join(
        f'<div class="block"><label>Field {index}</label><input value="{index}"></div>'
        for index in range(30)
    )
    html = (
        f"<style>{stylesheet}</style>"
        '<div id="agentix-widget-style-dialog"><div id="agentix-widget-style-title">'
        f"Widget style</div>{rows}</div>"
    )

    def route(request_route) -> None:
        """Serve one inert overlay page with the maintained stylesheet."""
        request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page(viewport={"width": 1400, "height": 900})
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            measured = page.locator("#agentix-widget-style-dialog").evaluate(
                """node => {const s = getComputedStyle(node);
                    return [Math.round(node.getBoundingClientRect().width),
                            s.overflowY, node.scrollHeight > node.clientHeight,
                            s.scrollbarWidth];}"""
            )
            assert measured[0] <= 470
            assert measured[1] == "auto"
            assert measured[2] is True
            assert measured[3] == "thin"
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_077_caption_font_reaches_the_span_and_spares_the_grip() -> None:
    """The served sheet styles the caption text, not the layout grip glyph."""
    import os

    from playwright.sync_api import sync_playwright

    from agentix.lab.application_session import served_style

    css = (
        b':where([id^="application_calculator_"]) { font-family: Georgia; font-size: 28px; }\n'
        b':where([id^="application_calculator_"]) label { font-family: Tahoma; font-size: 27px; }'
    )
    served = served_style(css, "calculator", "multiplier").decode()
    html = (
        f"<style>{(ASSETS / 'style.css').read_text(encoding='utf-8')}</style>"
        f"<style>{served}</style>"
        '<div id="application_multiplier_output" class="application-editable-element">'
        '<label><span>Result</span><input value="3"></label>'
        '<button class="application-layout-handle move">⠿</button></div>'
    )

    def route(request_route) -> None:
        """Serve one inert standalone page with the served stylesheet only."""
        request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page(viewport={"width": 1200, "height": 900})
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.wait_for_selector("#application_multiplier_output")
            caption = page.locator("#application_multiplier_output label span").evaluate(
                "n => {const s = getComputedStyle(n); return [s.fontFamily, s.fontSize];}"
            )
            assert caption == ["Tahoma", "27px"]
            grip = page.locator("#application_multiplier_output .application-layout-handle")
            assert grip.evaluate("n => getComputedStyle(n).fontSize") == "12px"
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_076_parent_opens_the_window_from_a_frame_message() -> None:
    """Only the framed application's valid tool name reaches the hidden opener."""
    import os

    from playwright.sync_api import expect, sync_playwright

    html = (
        '<div id="applications-frame"><iframe id="child" src="/child"></iframe></div>'
        '<div id="applications-widget-style-tool"><textarea></textarea></div>'
        '<button id="applications-widget-style-open">open</button>'
        "<script>document.getElementById('applications-widget-style-open')"
        ".addEventListener('click', () => {document.body.dataset.opened = "
        "document.querySelector('#applications-widget-style-tool textarea').value;});</script>"
    )
    child = (
        "<script>window.send = tool => parent.postMessage("
        "{type: 'agentix-widget-style', tool}, '*');</script>"
    )

    def route(request_route) -> None:
        """Serve the parent page and one inert framed child."""
        if request_route.request.url.endswith("/child"):
            request_route.fulfill(content_type="text/html", body=child)
        else:
            request_route.fulfill(content_type="text/html", body=html)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(path=str((ASSETS / "widget_style.js").resolve()))
            page.evaluate(
                "document.getElementById('child').contentWindow.send('count_words_in_text')"
            )
            expect(page.locator("body")).to_have_attribute("data-opened", "count_words_in_text")
            page.evaluate("document.getElementById('child').contentWindow.send('../evil')")
            page.evaluate(
                "window.postMessage({type: 'agentix-widget-style', tool: 'other_tool'}, '*')"
            )
            page.wait_for_timeout(200)
            assert page.locator("body").get_attribute("data-opened") == "count_words_in_text"
        finally:
            browser.close()
