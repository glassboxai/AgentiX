"""Real Chromium regression for reviewed Gradio radio-control interaction."""

import json
import os

import pytest

from agentix.application.general_acceptance import fill_input


@pytest.mark.browser
def test_browser_acceptance_can_select_radio_without_filling_it():
    """Radio inputs are selected, not filled as text; other tool values stay separate."""
    from playwright.sync_api import expect, sync_playwright

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
        )
        try:
            page = browser.new_page()
            page.set_content(
                '<div id="application_calculator_operation"><label><input type="radio" name="op" value="add">add</label><label><input type="radio" name="op" value="multiply">multiply</label></div>'
            )
            fill_input(page, "calculator", "operation", "multiply")
            expect(page.get_by_role("radio", name="multiply", exact=True)).to_be_checked()
            expect(page.get_by_role("radio", name="add", exact=True)).not_to_be_checked()
        finally:
            browser.close()


@pytest.mark.browser
def test_equal_results_wait_for_completed_gradio_callbacks(tmp_path):
    """A visible old zero must not finish a new event or suppress the next click."""
    import re
    import socket
    import time
    from types import SimpleNamespace

    import gradio as gr

    from agentix.application.general_acceptance import browser_verify

    def count(text):
        """Trusted delayed fixture exposes the default once-trigger event boundary."""
        time.sleep(0.2)
        return len(re.findall("[aeiou]", text, re.I))

    def run(text):
        """Return the same trusted result and a real completion status."""
        return count(text), "Completed"

    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    with gr.Blocks(analytics_enabled=False) as demo:
        text = gr.Textbox(elem_id="application_case_text")
        result = gr.Number(value=0, elem_id="application_case_output")
        button = gr.Button("Count", elem_id="application_case_execute")
        button.click(count, text, result)
        shared = gr.Textbox(elem_id="application_input_case")
        status = gr.Textbox(elem_id="application_status")
        execute = gr.Button("Run", elem_id="application_execute")
        execute.click(run, shared, [result, status])
    cases = [
        {"kwargs": {"text": text}, "expect": {"value": expected}}
        for text, expected in [("rhythms", 0), ("", 0), ("caf\u00e9", 1)]
    ]
    review = {
        "independent_acceptance": {
            "widgets": {"case": cases},
            "payload": {"case": "a"},
            "expected": {"case": 1},
        }
    }
    demo.launch(
        server_name="127.0.0.1",
        server_port=port,
        prevent_thread_lock=True,
        quiet=True,
        inbrowser=False,
    )
    try:
        browser_verify(
            SimpleNamespace(url=f"http://127.0.0.1:{port}/"),
            SimpleNamespace(folder=tmp_path),
            review,
        )
        assert (tmp_path / "browser-acceptance.json").is_file()
        assert (
            json.loads((tmp_path / "browser-acceptance.json").read_text())["fresh_completed_events"]
            == 5
        )
    finally:
        demo.close()


@pytest.mark.browser
def test_dataframe_verification_reads_real_virtual_grid_and_all_rows():
    """Hidden sizing cells cannot substitute for visible data, including long/empty tables."""
    import socket

    import gradio as gr
    from playwright.sync_api import sync_playwright

    from agentix.application.general_acceptance import assert_output, click_and_wait

    samples = [[6, 3, 7, 1, 2, 9], list(range(100)), []]
    pending = iter(samples)

    def draw():
        """Return independent fixture rows without invoking any generated source."""
        return [[item] for item in next(pending)]

    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    with gr.Blocks(analytics_enabled=False) as demo:
        table = gr.Dataframe(
            headers=["Number"],
            datatype=["number"],
            column_count=(1, "fixed"),
            row_count=(0, "dynamic"),
            interactive=False,
            elem_id="application_case_output",
        )
        button = gr.Button("Draw", elem_id="application_case_execute")
        button.click(draw, None, table)
    demo.launch(
        server_name="127.0.0.1",
        server_port=port,
        prevent_thread_lock=True,
        quiet=True,
        inbrowser=False,
    )
    try:
        with sync_playwright() as driver:
            browser = driver.chromium.launch(
                executable_path=os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
            )
            try:
                page = browser.new_page()
                page.goto(f"http://127.0.0.1:{port}/")
                for sample in samples:
                    click_and_wait(page, "application_case_execute", ["application_case_output"])
                    assert_output(page, "case", sample)
            finally:
                browser.close()
    finally:
        demo.close()
