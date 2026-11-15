"""V7-067: separate web tab, Edit affordances, legend and code-help file identity."""

from pathlib import Path

import pytest


def test_v7_067_frame_offers_a_separate_tab_and_labels_the_section() -> None:
    """The heading link reuses the validated origin and the name only labels the section."""
    from agentix.ui.application_presentation import generated_application_frame

    frame = generated_application_frame("http://127.0.0.1:50461/", "Vowel counter")
    assert 'id="generated-application-web"' in frame
    assert 'target="_blank"' in frame and 'rel="noopener noreferrer"' in frame
    assert 'href="http://127.0.0.1:50461/"' in frame
    assert 'aria-label="Vowel counter"' in frame
    assert 'title="Open Vowel counter in a new tab"' in frame
    assert "application_name=" not in frame
    assert "<script" not in frame
    injected = generated_application_frame("http://127.0.0.1:50461/", '"><img src=x>')
    assert "&quot;&gt;&lt;img src=x&gt;" in injected and "<img" not in injected
    with pytest.raises(ValueError):
        generated_application_frame("https://untrusted.example/", "Name")


@pytest.mark.windows_isolation
def test_v7_067_isolated_page_titles_itself_from_the_staged_name(tmp_path) -> None:
    """The child renders the owner's name server-side; no query string or eval is involved."""
    import json

    from test_code_application import make_code_candidate

    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import ApplicationSession

    item = make_code_candidate(tmp_path)
    approved = approve_application(item.package, item.digest)
    named = ApplicationSession(approved, display_name="Vowel counter")
    try:
        named.__enter__()
        config = json.loads(named.request("GET", "/config").body)
        heading = next(component for component in config["components"] if component["id"] == 1)
        assert heading["props"]["value"] == "## Vowel counter"
        assert all(dependency.get("js") is None for dependency in config["dependencies"])
    finally:
        named.close()
    unnamed = ApplicationSession(approved)
    try:
        unnamed.__enter__()
        config = json.loads(unnamed.request("GET", "/config").body)
        heading = next(component for component in config["components"] if component["id"] == 1)
        assert heading["props"]["value"] == "## Generated Application"
    finally:
        unnamed.close()


@pytest.mark.browser
def test_v7_067_editor_legend_surfaces_and_visible_checkbox() -> None:
    """Edit shows the legend, the default surface, the shifted label and a visible checkbox."""
    import os

    from playwright.sync_api import expect, sync_playwright

    from agentix.layout_contracts import application_layout_groups, application_layout_ids

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [
            {"id": "first", "tool": "calculator"},
            {"id": "second", "tool": "calculator"},
            {"id": "third", "tool": "counter"},
        ],
        "tools": {
            "calculator": {"parameters": {"a": {}}},
            "counter": {"parameters": {"b": {}}},
        },
    }
    allowed = application_layout_ids(manifest)
    groups = application_layout_groups(manifest)
    positions = {
        name: {"x": 10, "y": 10 + index * 80, "width": 200, "height": 60}
        for index, name in enumerate(sorted(allowed))
    }
    html = (
        '<div class="gradio-container">'
        '<button id="application_edit">Edit</button><div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px">'
            f'<label>{name}</label><input value="x"></div>'
            for name in sorted(allowed)
        )
        + "</div></div>"
    )

    def route(request_route) -> None:
        """Serve inert HTML and one fixed authorized layout payload."""
        request = request_route.request
        if request.url.endswith("/_agentix/layout"):
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

    def style(page, selector: str, prop: str) -> str:
        """Read one computed style value from the real maintained stylesheet."""
        return page.evaluate(
            "([selector, prop]) => getComputedStyle(document.querySelector(selector))"
            ".getPropertyValue(prop)",
            [selector, prop],
        )

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_style_tag(path=str(Path("src/agentix/ui/assets/style.css").resolve()))
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            assert style(page, "#application_first_output", "background-color") == (
                "rgba(0, 0, 0, 0)"
            )
            page.get_by_label("Edit application layout").click()
            expect(page.locator("#application-color-legend")).to_be_visible()
            assert page.locator(
                "#application-color-legend .application-legend-title"
            ).inner_text() == ("Tools")
            legend = page.locator("#application-color-legend").bounding_box()
            canvas = page.locator(".application-canvas").bounding_box()
            edit = page.locator("#application_edit").bounding_box()
            assert legend["width"] < 300
            assert abs((canvas["x"] + canvas["width"]) - (legend["x"] + legend["width"]) - 12) <= 2
            assert legend["y"] >= edit["y"] + edit["height"]
            rows = page.locator("#application-color-legend .application-legend-row")
            assert rows.count() == len(set(groups.values()))
            assert style(page, "#application_first_output", "background-color") == (
                "rgb(11, 13, 17)"
            )
            assert style(page, "#application_first_output > label", "padding-left") == "28px"
            toggle = page.get_by_label("visible application_first_output")
            expect(toggle).to_be_visible()
            assert toggle.is_checked()
            assert style(
                page,
                ".application-visibility-toggle[aria-label='visible application_first_output']",
                "background-color",
            ) == ("rgb(126, 231, 255)")
            assert (
                style(
                    page,
                    ".application-visibility-toggle[aria-label='visible application_first_output']",
                    "border-top-width",
                )
                == "2px"
            )
            assert style(
                page,
                ".application-visibility-toggle[aria-label='visible application_first_output']",
                "border-top-color",
            ) == ("rgb(126, 231, 255)")
            toggle.click()
            assert not toggle.is_checked()
            assert style(
                page,
                ".application-visibility-toggle[aria-label='visible application_first_output']",
                "background-color",
            ) == ("rgb(5, 6, 8)")
            handle = style(
                page,
                "#application_first_output .application-layout-handle.move",
                "background-color",
            )
            swatches = rows.locator(".application-legend-swatch")
            colors = swatches.evaluate_all(
                "nodes => nodes.map(node => getComputedStyle(node).backgroundColor)"
            )
            assert handle in colors
            assert len(colors) == len(set(colors))
            page.get_by_label("Edit application layout").click()
            page.get_by_role("status").filter(has_text="Layout saved").wait_for()
            expect(page.locator("#application-color-legend")).to_have_count(0)
            assert style(page, "#application_first_output", "background-color") == (
                "rgba(0, 0, 0, 0)"
            )
            expect(toggle).to_be_hidden()
            assert style(page, "#application_first_output", "display") == "none"
            page.get_by_label("Edit application layout").click()
            assert style(page, "#application_first_output", "display") == "block"
            assert not page.get_by_label("visible application_first_output").is_checked()
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_067_code_help_names_the_selected_file() -> None:
    """The helper names the pane's real file and follows a later file selection."""
    import os

    from playwright.sync_api import expect, sync_playwright

    html = (
        '<div id="applications-files"><input value="count_words_in_text_widget.py"></div>'
        '<div id="applications-tool-code"><div class="cm-editor"><div class="cm-content">x</div></div></div>'
        '<div id="chathelper-pane"><textarea>code</textarea></div>'
        '<div id="chathelper-window"><div id="chathelper-title">Code help</div>'
        '<div id="chathelper-file">No file selected</div>'
        '<div id="chathelper-question"><textarea></textarea></div></div>'
    )

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE"), headless=True
        )
        try:
            page = browser.new_page()
            page.set_content(html)
            page.add_script_tag(path=str(Path("src/agentix/ui/assets/chathelper.js").resolve()))
            expect(page.locator("#chathelper-file")).to_have_text("No file selected")
            page.locator("#applications-tool-code .cm-content").click(button="right")
            page.get_by_role("button", name="Ask about this code", exact=True).click()
            expect(page.locator("#chathelper-file")).to_have_text("count_words_in_text_code.py")
            page.evaluate(
                "() => {const field = document.querySelector('#applications-files input');"
                "Object.getOwnPropertyDescriptor(Object.getPrototypeOf(field), 'value')"
                ".set.call(field, 'other_tool_widget.py');"
                "field.dispatchEvent(new Event('input', {bubbles: true}));}"
            )
            expect(page.locator("#chathelper-file")).to_have_text("other_tool_code.py")
        finally:
            browser.close()
