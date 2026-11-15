"""Independent host comparisons for generic model widgets inside native previews."""

import json
import logging
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

logger = logging.getLogger(__name__)


def launch_acceptance_browser(driver, evidence: Path | None = None):
    """Launch the acceptance Chromium, retaining bounded evidence on launch failure.

    A configured but missing AGENTIX_PLAYWRIGHT_EXECUTABLE fails with clear guidance
    instead of a raw driver error. Launch errors never carry page or payload data.
    """
    executable = os.environ.get("AGENTIX_PLAYWRIGHT_EXECUTABLE")
    if executable is not None and not Path(executable).is_file():
        raise ValueError(
            "AGENTIX_PLAYWRIGHT_EXECUTABLE does not point to an existing browser executable"
        )
    try:
        return driver.chromium.launch(executable_path=executable)
    except Exception as error:
        logger.warning(
            "event=application_browser_launch_failed error_type=%s",
            type(error).__name__,
            exc_info=True,
        )
        if evidence is not None:
            (Path(evidence) / "browser-failure.json").write_text(
                json.dumps(
                    {
                        "type": type(error).__name__,
                        "stage": "browser_launch",
                        "detail": str(error)[:4000],
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
        raise


if TYPE_CHECKING:
    from agentix.application.app_workflow import Candidate
    from agentix.lab.widget_panel import Preview


def fill_input(page, identity: str, parameter: str, value):
    """Drive the actual browser control, never call the generated callback on host."""
    control = page.locator(f"#application_{identity}_{parameter}")
    if control.locator('input[type="radio"]').count():
        control.get_by_role("radio", name=str(value), exact=True).check()
    elif type(value) is bool:
        control.locator('input[type="checkbox"]').set_checked(value)
    elif type(value) in {str, int, float}:
        control.locator("textarea,input").first.fill(str(value))
    else:
        raise ValueError("Independent GUI acceptance requires supported scalar input controls")


def click_and_wait(page, button_id: str, output_ids: list[str]) -> str:
    """Wait for a fresh Gradio queue acknowledgement and completed loading state.

    Equal previous values cannot establish callback completion. Gradio marks
    outputs pending before submitting /queue/join and hides status trackers only
    after completion. No predicted output or arbitrary sleep replaces these signals.
    """
    from playwright.sync_api import expect

    with page.expect_response(
        lambda response: "/queue/join" in response.url and response.request.method == "POST",
        timeout=45000,
    ) as acknowledgement:
        page.locator("#" + button_id).click()
    response = acknowledgement.value
    identity = response.json().get("event_id") if response.status == 200 else None
    if not isinstance(identity, str) or not identity:
        raise ValueError("Gradio did not acknowledge a fresh callback")
    for output in output_ids:
        expect(page.locator("#" + output).get_by_test_id("status-tracker")).to_have_class(
            re.compile(r".*\bhide\b.*"), timeout=45000
        )
    return identity


def display_expectation(value: object) -> str | re.Pattern[str]:
    """Compare numeric presentation exactly while allowing omitted integer decimals.

    Gradio tables can render 3.0 as 3. Anchors reject numeric prefixes and suffixes;
    padding is presentation whitespace, never a numeric tolerance or rounding rule.
    """
    if type(value) in {int, float}:
        text = str(int(value)) if type(value) is float and value.is_integer() else str(value)
        suffix = r"(?:\.0+)?" if "." not in text and "e" not in text.lower() else ""
        return re.compile(r"^\s*" + re.escape(text) + suffix + r"\s*$")
    return str(value)


def assert_output(page, identity: str, value):
    """Compare rendered scalar/table values with reviewed expectations outside the child."""
    from playwright.sync_api import expect

    control = page.locator(f"#application_{identity}_output")
    if isinstance(value, list):
        # The tbody is an aria-hidden sizing table, not the displayed data.
        # Read the actual accessible virtual grid and scroll every expected row.
        grid = control.get_by_role("grid")
        expect(grid).to_have_attribute("aria-colcount", "1", timeout=45000)
        expect(grid).to_have_attribute("aria-rowcount", str(len(value) + 1), timeout=45000)
        viewport = grid.locator(".virtual-table-viewport")
        for index, item in enumerate(value):
            fraction = index / max(1, len(value) - 1)
            viewport.evaluate(
                "(element, fraction) => { element.scrollTop = fraction * Math.max(0, element.scrollHeight - element.clientHeight); }",
                fraction,
            )
            expect(grid.get_by_test_id(f"cell-{index}-0")).to_have_text(
                display_expectation(item), timeout=45000
            )
        if not value:
            expect(grid.get_by_role("gridcell")).to_have_count(0)
    else:
        inputs = control.locator("input,textarea")
        if inputs.count():
            expected = display_expectation(value)
            expect(inputs.first).to_have_value(expected, timeout=45000)
        else:
            expect(control).to_contain_text(str(value), timeout=45000)


def browser_verify(preview: "Preview", candidate: "Candidate", review: dict) -> None:
    """Verify individual widget callbacks, repeated combined execution and unique IDs."""
    from playwright.sync_api import expect, sync_playwright

    origin = urlsplit(preview.url)
    with sync_playwright() as driver:
        browser = launch_acceptance_browser(driver, candidate.folder)
        context = browser.new_context(viewport={"width": 1700, "height": 1100})

        def restrict(route):
            """Only the owned native bridge origin is reachable by this test browser."""
            url = urlsplit(route.request.url)
            if (url.scheme, url.netloc) == (origin.scheme, origin.netloc) or url.scheme in {
                "data",
                "blob",
            }:
                route.continue_()
            else:
                route.abort()

        context.route("**/*", restrict)
        page = context.new_page()
        try:
            page.goto(preview.url, wait_until="domcontentloaded")
            completed_events = []
            manifest = review.get("manifest", {})
            connected = {widget["id"] for widget in manifest.get("widgets", [])}
            for identity, cases in review["independent_acceptance"]["widgets"].items():
                # Managed inputs are exercised through the full application below;
                # never unlock controls or overwrite reviewed constants to test a widget.
                if identity in connected:
                    continue
                for case in cases[:5]:
                    for parameter, value in case["kwargs"].items():
                        fill_input(page, identity, parameter, value)
                    completed_events.append(
                        click_and_wait(
                            page,
                            f"application_{identity}_execute",
                            [f"application_{identity}_output"],
                        )
                    )
                    assert_output(page, identity, case["expect"]["value"])
            acceptance = review["independent_acceptance"]
            for _ in range(2):
                for name, value in acceptance["payload"].items():
                    fill_input(
                        page, "input", name, json.dumps(value) if type(value) is list else value
                    )
                completed_events.append(
                    click_and_wait(
                        page,
                        "application_execute",
                        ["application_status"]
                        + [f"application_{identity}_output" for identity in acceptance["expected"]],
                    )
                )
                expect(page.locator("#application_status textarea")).to_have_value(
                    "Completed", timeout=45000
                )
                for identity, value in acceptance["expected"].items():
                    assert_output(page, identity, value)
            if len(completed_events) != len(set(completed_events)):
                raise ValueError("A previous callback acknowledgement was reused")
            ids = page.locator('[id^="application_"]').evaluate_all("nodes=>nodes.map(n=>n.id)")
            if len(ids) != len(set(ids)):
                raise ValueError("Duplicated application control IDs")
            page.screenshot(path=str(candidate.folder / "accepted-gui.png"), full_page=True)
            (candidate.folder / "browser-acceptance.json").write_text(
                json.dumps(
                    {
                        "status": "passed",
                        "widgets": len(manifest.get("widgets", [])),
                        "standalone_widgets": 0,
                        "managed_widgets_verified_in_application": len(connected),
                        "expectations": "host-held reviewed tool cases",
                        "repeated_combined_runs": 2,
                        "fresh_completed_events": len(completed_events),
                    }
                ),
                encoding="utf-8",
            )
        except Exception as error:
            page.screenshot(path=str(candidate.folder / "failed-gui.png"), full_page=True)
            (candidate.folder / "browser-failure.json").write_text(
                json.dumps({"type": type(error).__name__, "detail": str(error)[:4000]}),
                encoding="utf-8",
            )
            raise
        finally:
            browser.close()


def verify(supervisor, candidate, parent_origin):
    """Hold expected results outside native execution; publish only after GUI comparison."""
    review = json.loads(candidate.review_text)
    acceptance = review["independent_acceptance"]
    preview = None
    try:
        from agentix.lab.application_session import WidgetTestsFailed, run_application_widget_tests

        new_widgets = [
            name
            for name, status in review["widget_reuse"].items()
            if status != "approved widget reused"
        ]
        if new_widgets:
            logger.info("event=application_widget_tests_started widgets=%s", sorted(new_widgets))
            try:
                test_report = run_application_widget_tests(candidate.snapshot, new_widgets)
            except WidgetTestsFailed as error:
                logger.warning(
                    "event=application_widget_tests_failed widgets=%s", sorted(new_widgets)
                )
                (candidate.folder / "provisional-widget-tests-failed.json").write_text(
                    json.dumps(error.report), encoding="utf-8"
                )
                raise
            logger.info("event=application_widget_tests_passed widgets=%s", sorted(new_widgets))
            (candidate.folder / "provisional-widget-tests.json").write_text(
                json.dumps(test_report), encoding="utf-8"
            )
        logger.info("event=application_native_acceptance_started")
        if supervisor.native(candidate.snapshot, acceptance["payload"]) != acceptance["expected"]:
            logger.warning("event=application_native_acceptance_mismatch")
            raise ValueError("Independent native application acceptance failed")
        logger.info("event=application_native_acceptance_passed")
        preview = supervisor.preview_factory(
            candidate.snapshot, parent_origin, display_name=candidate.display_name
        )
        candidate.preview = preview
        logger.info("event=application_browser_acceptance_started")
        (supervisor.browser or browser_verify)(preview, candidate, review)
        logger.info("event=application_browser_acceptance_passed")
        supervisor._snapshot(candidate)
        if candidate.widget_commit is not None:
            candidate.widget_commit(candidate)
        candidate.verified = True
        (candidate.folder / "validation.json").write_text(
            json.dumps({"status": "passed", "stage": "catalog_native_browser_acceptance"}),
            encoding="utf-8",
        )
        return preview
    except BaseException as error:
        logger.warning(
            "event=application_acceptance_failed error_type=%s",
            type(error).__name__,
            exc_info=True,
        )
        if preview is not None:
            preview.close()
        candidate.preview = None
        candidate.verified = False
        raise
