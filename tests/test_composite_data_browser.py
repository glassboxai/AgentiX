"""Rendered-page regression for the composite data-operation accordion.

The backend is an explicit double: this test proves the maintained Gradio view
renders the contract, the named-result table and the bounded rejection message in
a real browser. Native isolation and the supervisor contract are covered by the
offline and Windows-isolation suites, never by this page check.
"""

import os
import socket

import pytest

from agentix.controllers.sessions import SessionRegistry
from agentix.ui.view import build_view


@pytest.mark.browser
def test_composite_accordion_renders_contract_table_and_rejection(tmp_path, monkeypatch):
    """Catch a hidden contract, a stale table or a swallowed JSON diagnostic."""
    from playwright.sync_api import expect, sync_playwright

    from agentix.controllers.applications import ApplicationsBackend

    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path / "home"))
    sessions = SessionRegistry(lambda identity: None)
    backend = ApplicationsBackend(sessions)
    contract = (
        "**Data operation inputs** — send one JSON object with exactly these keys:\n\n"
        "| Key | Type | Description |\n| --- | --- | --- |\n"
        "| `text` | string | Text to analyze |\n\n"
        'Example payload: `{"text": "Hello World!"}`'
    )
    backend.data_contract = lambda token, request: (contract, token)
    backend.data = lambda text, token, request: (
        None,
        "Data operation failed (JSONDecodeError): Expecting value: line 1 column 1 (char 0).",
        token,
    )
    demo = build_view(sessions, applications_backend=backend).demo

    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
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
                page.get_by_role("tab", name="Applications", exact=True).click()
                page.get_by_role("button", name="Use the application as a composite tool").click()
                page.locator("#applications-data-schema").click()
                expect(page.locator("#applications-data-contract")).to_contain_text(
                    "Data operation inputs", timeout=15000
                )
                expect(page.locator("#applications-data-contract")).to_contain_text(
                    "Example payload"
                )
                contract_view = page.locator("#applications-data-contract")
                expect(contract_view.get_by_role("cell", name="text", exact=True)).to_have_count(1)
                expect(contract_view.get_by_role("cell", name="string", exact=True)).to_have_count(
                    1
                )
                expect(
                    contract_view.get_by_role("cell", name="Text to analyze", exact=True)
                ).to_have_count(1)
                page.locator("#applications-data-input textarea").fill("hola gola")
                page.locator("#applications-data-run").click()
                expect(page.locator("#applications-data-table")).to_be_hidden(timeout=15000)
                expect(page.locator("#applications-general-data-result")).to_be_hidden()
                expect(page.locator("#applications-data-contract")).to_contain_text(
                    "Text to analyze"
                )
                expect(page.locator("#applications-status")).to_contain_text(
                    "JSONDecodeError", timeout=15000
                )
                # The callback must hand the real session token back to the state.
                expect(page.locator("#applications-status")).not_to_contain_text("Session expired")
            finally:
                browser.close()
    finally:
        demo.close()
