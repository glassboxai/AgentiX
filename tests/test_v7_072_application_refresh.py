"""V7-072: a refresh control reloads the already validated generated application."""

from pathlib import Path

import pytest


def test_v7_072_worker_registers_a_refresh_toolbar_control() -> None:
    """The isolated child owns the control; it adds no callback, route or capability."""
    source = Path("src/agentix/lab/widget_worker.py").read_text(encoding="utf-8")
    assert 'elem_id="application_refresh"' in source
    assert 'elem_classes=["application-refresh-button"]' in source
    block = source.split('elem_id="application_refresh"')[1].split("gr.Button")[0]
    assert ".click(" not in block


def test_v7_072_refresh_stays_outside_the_movable_layout_allowlist() -> None:
    """Toolbar identity must never become persisted geometry or a hidden control."""
    from agentix.layout_contracts import application_layout_ids, validate_layout

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    assert "application_refresh" not in allowed
    rectangle = {"x": 0, "y": 0, "width": 100, "height": 100}
    with pytest.raises(ValueError, match="Unknown movable"):
        validate_layout(
            {"version": 1, "positions": {"application_refresh": rectangle}}, allowed=allowed
        )
    with pytest.raises(ValueError):
        validate_layout(
            {"version": 1, "positions": {}, "hidden": ["application_refresh"]}, allowed=allowed
        )


def test_v7_072_stylesheet_places_refresh_left_of_play() -> None:
    """The maintained sheet keeps one compact toolbar row with the refresh icon."""
    from agentix.ui.branding import stylesheet

    css = stylesheet()
    assert (
        "#application_execute, #application_edit, #application_stop, #application_refresh {" in css
    )
    assert "#application_refresh {right: 126px !important;}" in css
    assert "#application_refresh::after {content: '⟳'; font-size: 20px;}" in css


@pytest.mark.browser
def test_v7_072_refresh_reloads_the_page_and_sits_left_of_play() -> None:
    """A real Chromium click reloads the document and re-runs the maintained editor."""
    import os

    from playwright.sync_api import expect, sync_playwright

    from agentix.layout_contracts import application_layout_ids

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    positions = {
        name: {"x": 10, "y": 10 + index * 80, "width": 200, "height": 60}
        for index, name in enumerate(sorted(allowed))
    }
    html = (
        '<div class="gradio-container">'
        '<button id="application_execute">Run</button>'
        '<button id="application_refresh">Reload</button>'
        '<button id="application_edit">Edit</button>'
        '<button id="application_stop">Close</button>'
        '<div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px"><input value="x"></div>'
            for name in sorted(allowed)
        )
        + "</div></div>"
    )
    documents = []

    def route(request_route) -> None:
        """Serve inert HTML, count document loads and answer the layout probe."""
        request = request_route.request
        if request.url.endswith("/_agentix/layout"):
            request_route.fulfill(
                json={
                    "editable": True,
                    "token": "fixture",
                    "controls": sorted(allowed),
                    "groups": {},
                    "layout": {"version": 1, "positions": positions},
                }
            )
            return
        if request.resource_type == "document":
            documents.append(request.url)
        request_route.fulfill(content_type="text/html", body=html)

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
            refresh = page.get_by_role("button", name="Reload application", exact=True)
            expect(refresh).to_be_visible()
            play_box = page.locator("#application_execute").bounding_box()
            assert refresh.bounding_box()["x"] < play_box["x"]
            assert page.locator("#application_refresh").evaluate(
                "node => getComputedStyle(node, '::after').content"
            ) == ('"⟳"')
            assert len(documents) == 1
            page.evaluate("() => {window.__agentixReloadMarker = 'present';}")
            refresh.click()
            page.wait_for_function("() => window.__agentixReloadMarker === undefined")
            page.wait_for_load_state("load")
            assert len(documents) == 2
            page.add_style_tag(path=str(Path("src/agentix/ui/assets/style.css").resolve()))
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            expect(
                page.get_by_role("button", name="Reload application", exact=True)
            ).to_be_visible()
        finally:
            browser.close()
