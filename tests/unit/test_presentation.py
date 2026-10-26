"""UI-012 presentation contracts use independent data, never generated artifacts."""

from agentix.ui.presentation import format_catalog, format_result, render_validation


def test_observed_bill_has_readable_currency_and_collapsed_raw_evidence():
    """Verify observed bill has readable currency and collapsed raw evidence."""
    response = (
        'Host-observed execution: bill.calculate\nArguments: {"usage":350}\n'
        "Result: {'total_cost': 67.5, 'breakdown': [{'tier': 1, 'kwh': 100, 'cost': 12.0}]}"
    )
    rendered = format_result(response, "Calculate my bill in euros (€).")
    assert "€67.50" in rendered
    assert "<table" in rendered and "Breakdown" in rendered
    assert "<summary>Execution details</summary>" in rendered
    assert "<details open" not in rendered


def test_no_currency_is_invented_for_an_arbitrary_result():
    """Verify no currency is invented for an arbitrary result."""
    rendered = format_result(
        "Host-observed execution: math.f\nArguments: {}\nResult: 67.5", "Calculate"
    )
    assert "67.5" in rendered and "€" not in rendered and "$" not in rendered


def test_presentation_never_rounds_away_an_observed_rate():
    """Verify presentation never rounds away an observed rate."""
    rendered = format_result(
        "Host-observed execution: f\nArguments: {}\nResult: {'rate': 0.12345}",
        "Show the rate in euros",
    )
    assert "€0.12345" in rendered


def test_result_payload_is_data_never_markup_or_executable():
    """Verify result payload is data never markup or executable."""
    rendered = format_result(
        "Host-observed execution: x.f\nArguments: {}\nResult: {'value': '<img src=x onerror=alert(1)>'}",
        "",
    )
    assert "<img" not in rendered and "&lt;img" in rendered
    assert "Verified" not in format_result("No current execution evidence", "")


def test_catalog_details_are_collapsed_and_escape_untrusted_descriptions():
    """Verify catalog details are collapsed and escape untrusted descriptions."""
    original = "- Tool Name: `adder`\n    * Function: `add(a, b)`\n      Description: <script>bad()</script>"
    rendered = format_catalog(original)
    assert "<summary>adder</summary>" in rendered
    assert "<details open" not in rendered
    assert "add(a, b)" in rendered and "<script>" not in rendered


def test_validation_summarizes_and_collapses_case_evidence():
    """Verify validation summarizes and collapses case evidence."""
    status = {
        "stage": "verified",
        "contract_digest": "secret-digest",
        "cases": [
            {
                "id": "normal",
                "passed": True,
                "expected": {"value": "<unsafe>"},
                "observed": {"value": 3},
            },
            {"id": "invalid", "passed": False},
        ],
    }
    rendered = render_validation(status)
    assert "1 passed" in rendered and "1 failed" in rendered
    assert "<summary>normal: PASS</summary>" in rendered
    assert "<details open" not in rendered
    assert "secret-digest" not in rendered and "&lt;unsafe&gt;" in rendered


def test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded():
    """Verify literal calls are never evaluated and oversized data is bounded."""
    payload = "__import__('os').environ.clear()"
    rendered = format_result("Host-observed execution: f\nArguments: {}\nResult: " + payload)
    assert "__import__" in rendered
    oversized = format_result("Host-observed execution: f\nResult: " + "x" * 40000)
    assert len(oversized) < 20000


def test_brand_has_requested_order_and_local_assets():
    """Verify brand has requested order and local assets."""
    from agentix.ui.branding import header, launch_options

    brand = header()
    assert (
        brand.index("<img")
        < brand.index("<h1>AgentiX</h1>")
        < brand.index("Agentic Software Engineering.")
    )
    assert "Developer-in-the-Loop." in brand
    assert "AI-generated code. Software engineer-supervised." in brand
    options = launch_options()
    assert "Inter" in options["css"] and "#050608" in options["css"]
    assert 'href="https://glassboxai.dev/"' in brand
    assert brand.index("production-quality software.") < brand.index("The Glass Box AI Project")
    assert "@import" not in options["css"]


def test_controller_formats_result_and_keeps_catalog_disclosure(system):
    """Verify controller formats result and keeps catalog disclosure."""
    system.app.state.chat_history = [
        {"role": "user", "content": "Calculate in euros"},
        {"role": "assistant", "content": "**Agents are actively solving your request...**"},
    ]
    system.app.state.last_response = (
        "Host-observed execution: f\nArguments: {}\nResult: {'total_cost': 67.5}"
    )
    system.app.state.is_running = False
    result = system.app.poll_system_status()[0][-1]["content"]
    assert "€67.50" in result and "Execution details" in result
