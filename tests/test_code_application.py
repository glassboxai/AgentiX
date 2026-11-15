"""V5-043: generated connection code persists without a graph or host imports."""

import json
from pathlib import Path

import pytest
from test_application_crews import approved_tool

LOGIC = "\n".join(
    [
        '"""Connect approved arithmetic calls."""',
        "def run(payload: dict, call) -> None:",
        '    """Compute two dependent results from one application input."""',
        '    first = call("first", a=payload["amount"], b=3)',
        '    call("second", a=first, b=3)',
        "",
    ]
)


def proposal() -> dict:
    """Provide independently authored code and presentation metadata, without edges."""
    return {
        "inputs": {"amount": {"type": "integer"}},
        "widgets": [{"id": "first", "tool": "calculator"}, {"id": "second", "tool": "calculator"}],
        "connection_code": LOGIC,
        "notes": "Two dependent approved calls",
    }


def test_proposal_checks_source_without_importing_it(tmp_path: Path) -> None:
    """Host inspection must not run module-level generated code."""
    from agentix.domain.application_code import ApplicationCode

    value = proposal()
    value["connection_code"] = 'raise RuntimeError("HOST EXECUTED")\n' + LOGIC
    with pytest.raises(ValueError):
        ApplicationCode.model_validate(value).validate_catalog(
            {"calculator": approved_tool().schema}
        )
    assert (
        ApplicationCode.model_validate(proposal()).validate_catalog(
            {"calculator": approved_tool().schema}
        )["connection_code"]
        == LOGIC
    )


def test_public_input_schema_rejects_numeric_bounds_with_a_named_key() -> None:
    """V7-059: a model-supplied bound is rejected by name, never silently accepted."""
    from agentix.domain.application_code import ApplicationCode, ApplicationContractError

    value = proposal()
    value["inputs"] = {"amount": {"type": "integer", "description": "How many times", "minimum": 0}}
    with pytest.raises(ApplicationContractError, match=r"amount.*minimum"):
        ApplicationCode.model_validate(value).validate_catalog(
            {"calculator": approved_tool().schema}
        )


def test_public_input_schema_names_every_unsupported_key() -> None:
    """The bounded message lists all offending keys of one input in sorted order."""
    from agentix.domain.application_code import ApplicationCode, ApplicationContractError

    value = proposal()
    value["inputs"] = {
        "amount": {"type": "integer", "maximum": 9, "minimum": 0, "pattern": "^[0-9]+$"}
    }
    with pytest.raises(ApplicationContractError) as caught:
        ApplicationCode.model_validate(value).validate_catalog(
            {"calculator": approved_tool().schema}
        )
    message = str(caught.value)
    assert "amount" in message
    assert "maximum, minimum, pattern" in message
    assert "type, description, enum, items" in message


def test_contract_error_never_carries_the_rejected_value() -> None:
    """A closed diagnostic must not leak model or user payload into UI or logs."""
    from agentix.domain.application_code import ApplicationCode, ApplicationContractError

    value = proposal()
    value["inputs"] = {"amount": {"type": "integer", "minimum": "PRIVATE_MODEL_BODY"}}
    with pytest.raises(ApplicationContractError) as caught:
        ApplicationCode.model_validate(value).validate_catalog(
            {"calculator": approved_tool().schema}
        )
    assert "PRIVATE_MODEL_BODY" not in str(caught.value)


def test_supported_input_shapes_still_validate() -> None:
    """The closed key list keeps accepting the four documented keys and arrays."""
    from agentix.domain.application_code import ApplicationCode

    value = proposal()
    value["inputs"] = {
        "amount": {"type": "integer", "description": "How many times", "enum": [1, 2]},
        "labels": {"type": "array", "items": {"type": "string"}},
    }
    assert (
        ApplicationCode.model_validate(value).validate_catalog(
            {"calculator": approved_tool().schema}
        )["inputs"]
        == value["inputs"]
    )


def test_new_package_has_no_graph_and_requires_independent_cases(tmp_path: Path) -> None:
    """Creation succeeds before acceptance; approval cannot accept missing host cases."""
    from test_general_application_pipeline import WIDGET

    from agentix.application.app_review import ApplicationReview
    from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor

    class Coordinator:
        """Return inert authored artifacts across the production coordinator boundary."""

        def plan(self, *args):
            """Return generated connection code."""
            return proposal()

        def widgets(self, tools, feedback):
            """Return a reusable widget contract."""
            return {
                name: {"widget_code": WIDGET, "tests_code": "# provisional", "notes": "fixture"}
                for name in tools
            }

    item = ApplicationPipeline(tmp_path, coordinator_factory=lambda _: Coordinator()).generate(
        "Add three twice", tools={"calculator": approved_tool()}
    )
    manifest = json.loads((item.package / "application.json").read_bytes())
    assert manifest["schema_version"] == 3
    assert not {"workflow", "order", "binding_version"} & set(manifest)
    assert (item.package / "application_logic.py").read_text(encoding="utf-8") == LOGIC
    assert not (item.package / "bindings.py").exists()
    supervisor = ApplicationSupervisor()
    with pytest.raises(ValueError, match="acceptance"):
        supervisor.approve(item, item.identity, True)
    review = ApplicationReview()
    assert review.read(item, "application_logic.py")[1]
    assert review.read(item, "application_acceptance.json")[1]
    cases = {"payload": {"amount": 2}, "expected": {"first": 5, "second": 8}}
    review.save(item, "application_acceptance.json", json.dumps(cases), item.identity)
    supervisor.approve(item, item.identity, True)
    assert item.approved
    review.save(item, "application_logic.py", LOGIC.replace("b=3)", "b=4)"), item.identity)
    assert not item.approved and item.snapshot is None


@pytest.mark.parametrize(
    "change",
    [
        {"widgets": [{"id": "x", "tool": "missing"}]},
        {"widgets": [{"id": "x", "tool": "calculator"}, {"id": "x", "tool": "calculator"}]},
        {"connection_code": "import os\ndef run(payload, call):\n    pass\n"},
    ],
)
def test_invalid_code_contract_is_rejected(change: dict) -> None:
    """Reject unknown dependencies, duplicate widget IDs and forbidden imports."""
    from agentix.domain.application_code import ApplicationCode

    with pytest.raises(ValueError):
        ApplicationCode.model_validate(proposal() | change).validate_catalog(
            {"calculator": approved_tool().schema}
        )


def make_code_candidate(tmp_path: Path, logic: str = LOGIC):
    """Create a trusted temporary package and independently supply expected values."""
    from types import SimpleNamespace

    from test_general_application_pipeline import WIDGET

    from agentix.application.app_review import ApplicationReview
    from agentix.application.app_workflow import ApplicationPipeline

    coordinator = SimpleNamespace(
        plan=lambda *args: proposal() | {"connection_code": logic},
        widgets=lambda tools, feedback: {
            name: {"widget_code": WIDGET, "tests_code": "# provisional", "notes": "fixture"}
            for name in tools
        },
    )
    item = ApplicationPipeline(tmp_path, coordinator_factory=lambda _: coordinator).generate(
        "Add three twice", tools={"calculator": approved_tool()}
    )
    ApplicationReview().save(
        item,
        "application_acceptance.json",
        json.dumps({"payload": {"amount": 2}, "expected": {"first": 5, "second": 8}}),
        item.identity,
    )
    return item


def test_manifest_tampering_and_strict_public_contracts(tmp_path: Path) -> None:
    """Reject altered maintained runtime bytes, coercion and changed call output types."""
    import hashlib

    from agentix.application.code_package import validate_payload, validate_results
    from agentix.lab.application_artifacts import application_digest

    item = make_code_candidate(tmp_path)
    path = item.package / "application.json"
    manifest = json.loads(path.read_bytes())
    for bad in ({}, {"amount": True}, {"amount": 2.5}, {"amount": "2"}):
        with pytest.raises(ValueError):
            validate_payload(bad, manifest)
    with pytest.raises(ValueError):
        validate_results({"first": 5, "second": "8"}, manifest)
    member = item.package / "application_values.py"
    member.write_text('raise RuntimeError("changed")', encoding="utf-8")
    manifest["files"][member.name] = hashlib.sha256(member.read_bytes()).hexdigest()
    path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ValueError, match="Maintained"):
        application_digest(item.package)


@pytest.mark.windows_isolation
def test_native_connection_code_runs_without_agents_or_graph(tmp_path: Path) -> None:
    """Real AppContainer executes dependent calls from persisted Python only."""
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import execute_application

    item = make_code_candidate(tmp_path)
    approved = approve_application(item.package, item.digest)
    assert execute_application(approved, {"amount": 2}) == {"first": 5, "second": 8}
    assert execute_application(approved, {"amount": 7}) == {"first": 10, "second": 13}


@pytest.mark.windows_isolation
@pytest.mark.parametrize(
    "logic",
    [
        LOGIC.replace('    call("second", a=first, b=3)', ""),
        LOGIC.replace('    call("second", a=first, b=3)', '    call("first", a=first, b=3)'),
    ],
)
def test_native_missing_or_repeated_calls_fail(tmp_path: Path, logic: str) -> None:
    """Incomplete/repeated execution cannot publish partial results or run on host."""
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import ApplicationSession

    item = make_code_candidate(tmp_path, logic)
    session = ApplicationSession(
        approve_application(item.package, item.digest), payload={"amount": 2}
    )
    with pytest.raises(RuntimeError):
        with session:
            raise AssertionError("Invalid connection code published a result")
    observation = session.diagnostics.get("native")
    assert observation is not None, (
        "Infrastructure failure cannot establish a call-contract rejection"
    )
    assert observation[0] != 0 and not observation[2]
    detail = observation[1].decode("utf-8", errors="replace")
    assert (
        "skipped a required tool call" in detail or "Unknown or repeated application call" in detail
    )
    assert "application_result" not in session.diagnostics


@pytest.mark.browser
@pytest.mark.windows_isolation
def test_native_browser_for_code_package(tmp_path: Path) -> None:
    """Real isolated widgets show results and arguments from generated code on repeat runs."""
    from agentix.application.general_acceptance import browser_verify
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_panel import ApplicationPreview

    item = make_code_candidate(tmp_path)
    preview = ApplicationPreview(approve_application(item.package, item.digest), None)
    try:
        browser_verify(preview, item, json.loads(item.review_text))
        report = json.loads((item.folder / "browser-acceptance.json").read_bytes())
        assert report["managed_widgets_verified_in_application"] == 2
        assert report["fresh_completed_events"] == 2
    finally:
        preview.close()


@pytest.mark.frameworks
def test_real_gradio_code_compositor_with_trusted_fixtures(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Only authored fixtures run in memory; production generated imports stay native."""
    import importlib.util
    import sys

    from agentix.application.code_package import runtime_template

    item = make_code_candidate(tmp_path)
    names = (
        "operation",
        "application_context",
        "element_ids",
        "application_values",
        "application_logic",
        "calculator_code",
        "calculator_widget",
    )
    monkeypatch.syspath_prepend(str(item.package))
    for name in names:
        monkeypatch.delitem(sys.modules, name, raising=False)
    spec = importlib.util.spec_from_file_location(
        "trusted_code_compositor", runtime_template("app.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    demo = module.create_application()
    try:
        callback = next(event for event in demo.fns.values() if event.api_name == "run_application")
        assert len(callback.inputs) == 1
        canvas = next(
            block
            for block in demo.blocks.values()
            if "application-canvas" in (getattr(block, "elem_classes", None) or [])
        )
        descendants = list(canvas.children)
        for child in descendants:
            descendants.extend(getattr(child, "children", []))
        assert callback.inputs[0] in descendants
        assert callback.inputs[0].elem_id == "application_input_amount"
        output = list(callback.fn(2))
        assert output[0] == [None] * 6 + ["Running"]
        assert output[-1] == [5, 8, 2, 3, 5, 3, "Completed"]
        assert all(component.interactive is False for component in callback.outputs[2:-1])
        assert list(callback.fn("bad"))[-1][:-1] == [None] * 6
    finally:
        demo.close()
        for name in names:
            monkeypatch.delitem(sys.modules, name, raising=False)


@pytest.mark.frameworks
@pytest.mark.parametrize(
    "logic,message",
    [
        (LOGIC.replace('    call("second", a=first, b=3)', ""), "skipped"),
        (
            LOGIC.replace('    call("second", a=first, b=3)', '    call("first", a=first, b=3)'),
            "repeated",
        ),
    ],
)
def test_trusted_code_runtime_rejects_partial_calls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, logic: str, message: str
) -> None:
    """Authored fixture calls exercise failure contracts independently of OS readiness."""
    import importlib
    import sys

    item = make_code_candidate(tmp_path, logic)
    names = ("operation", "application_values", "application_logic", "calculator_code")
    monkeypatch.syspath_prepend(str(item.package))
    for name in names:
        monkeypatch.delitem(sys.modules, name, raising=False)
    try:
        operation = importlib.import_module("operation")
        with pytest.raises(ValueError, match=message):
            operation.analyze_text({"amount": 2})
    finally:
        for name in names:
            monkeypatch.delitem(sys.modules, name, raising=False)


def test_v6_044_code_widgets_have_editable_persistable_geometry() -> None:
    """V6-044: named widget controls move/resize while toolbar IDs stay forbidden."""
    from agentix.layout_contracts import application_layout_ids, validate_layout

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}, {"id": "second", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}, "b": {}}}},
    }
    allowed = application_layout_ids(manifest)
    assert allowed == {"application_status", "application_input_text"} | {
        f"application_{instance}_{role}"
        for instance in ("first", "second")
        for role in ("a", "b", "input", "output", "execute")
    }
    positions = {name: {"x": 10, "y": 20, "width": 300, "height": 100} for name in allowed}
    layout = {"version": 1, "positions": positions}
    assert validate_layout(layout, allowed=allowed) == layout
    for forbidden in (
        "application_edit",
        "application_execute",
        "application_stop",
        "application_unknown_output",
        "application_input_unknown",
    ):
        with pytest.raises(ValueError, match="Unknown movable"):
            validate_layout(
                {"positions": {forbidden: positions["application_status"]}}, allowed=allowed
            )


def test_v7_062_layout_hidden_visibility_contract() -> None:
    """V7-062: hidden controls share the movable allowlist and stay optional."""
    from agentix.layout_contracts import application_layout_ids, validate_layout

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    layout = {
        "version": 1,
        "positions": {"application_status": {"x": 0, "y": 0, "width": 300, "height": 100}},
        "hidden": ["application_status", "application_first_output"],
    }
    assert validate_layout(layout, allowed=allowed) == layout
    assert validate_layout({"version": 1, "positions": {}}, allowed=allowed) == {
        "version": 1,
        "positions": {},
    }
    for forbidden in (
        ["application_edit"],
        ["application_stop"],
        ["application_status", "application_status"],
        ["application_unknown_output"],
    ):
        with pytest.raises(ValueError):
            validate_layout({"version": 1, "positions": {}, "hidden": forbidden}, allowed=allowed)


def test_v7_063_layout_groups_bind_widget_controls_to_their_tool() -> None:
    """V7-063: handles of one tool share a group; public inputs and Status stay separate."""
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
    groups = application_layout_groups(manifest)
    assert set(groups) == application_layout_ids(manifest)
    assert groups["application_first_output"] == groups["application_second_output"]
    assert groups["application_first_output"] != groups["application_third_output"]
    assert groups["application_status"] != groups["application_input_text"]
    assert groups["application_status"] != groups["application_first_output"]
    assert application_layout_groups({"schema_version": 2}) == {}


@pytest.mark.browser
def test_v7_062_editor_hides_unchecked_controls_after_edit() -> None:
    """Unchecking a control in Edit hides it outside Edit and survives a reload."""
    import os

    from playwright.sync_api import expect, sync_playwright

    from agentix.layout_contracts import application_layout_ids, validate_layout

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    state = {
        "version": 1,
        "positions": {
            name: {"x": 10, "y": 10 + index * 80, "width": 200, "height": 60}
            for index, name in enumerate(sorted(allowed))
        },
    }
    saves = []
    html = (
        '<button id="application_edit">Edit</button><div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px"><input value="Hello World!"></div>'
            for name in sorted(allowed)
        )
        + "</div>"
    )

    def route(request_route) -> None:
        """Return inert HTML or validate the editor's data-only layout request."""
        nonlocal state
        request = request_route.request
        if request.url.endswith("/_agentix/layout"):
            if request.method == "POST":
                state = validate_layout(request.post_data_json, allowed=allowed)
                saves.append(state)
                request_route.fulfill(json={})
            else:
                request_route.fulfill(
                    json={
                        "editable": True,
                        "token": "fixture",
                        "controls": sorted(allowed),
                        "layout": state,
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
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_style_tag(path=str(Path("src/agentix/ui/assets/style.css").resolve()))
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            expect(page.locator("#application_first_output")).to_be_visible()
            page.get_by_label("Edit application layout").click()
            toggle = page.get_by_label("visible application_first_output")
            expect(toggle).to_be_checked()
            toggle.uncheck()
            page.get_by_label("Edit application layout").click()
            page.get_by_role("status").filter(has_text="Layout saved").wait_for()
            assert saves[-1]["hidden"] == ["application_first_output"]
            expect(page.locator("#application_first_output")).to_be_hidden()
            expect(page.locator("#application_first_a")).to_be_visible()
            page.reload()
            page.add_style_tag(path=str(Path("src/agentix/ui/assets/style.css").resolve()))
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            expect(page.locator("#application_first_output")).to_be_hidden()
            page.get_by_label("Edit application layout").click()
            expect(page.get_by_label("visible application_first_output")).not_to_be_checked()
            expect(page.locator("#application_first_output")).to_be_visible()
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_063_editor_colors_only_the_move_handle_per_tool() -> None:
    """Same tool shares one handle color; leaving Edit restores the base color."""
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
        '<button id="application_edit">Edit</button><div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px"><input value="x"></div>'
            for name in sorted(allowed)
        )
        + "</div>"
    )

    def route(request_route) -> None:
        """Serve inert HTML and a fixed authorized layout payload."""
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

    def color(page, identity: str) -> str:
        """Read the computed handle background, not the widget surface."""
        return page.evaluate(
            """id => getComputedStyle(
                document.querySelector('#' + id + ' .application-layout-handle.move')
            ).backgroundColor""",
            identity,
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
            page.get_by_label("Edit application layout").click()
            expect(
                page.locator("#application_first_output .application-layout-handle.move")
            ).to_be_visible()
            first = color(page, "application_first_output")
            second = color(page, "application_second_output")
            third = color(page, "application_third_output")
            assert first == second
            assert first != third
            assert color(page, "application_status") not in {first, third}
            page.get_by_label("Edit application layout").click()
            page.get_by_role("status").filter(has_text="Layout saved").wait_for()
            assert color(page, "application_first_output") == "rgb(22, 38, 48)"
        finally:
            browser.close()


@pytest.mark.browser
def test_v6_044_editor_moves_resizes_and_restores_code_widget_controls() -> None:
    """Exercise the real editor with inert DOM controls and an isolated layout route."""
    import os

    from playwright.sync_api import sync_playwright

    from agentix.layout_contracts import application_layout_ids, validate_layout

    manifest = {
        "schema_version": 3,
        "inputs": {"text": {"type": "string"}},
        "widgets": [{"id": "first", "tool": "calculator"}],
        "tools": {"calculator": {"parameters": {"a": {}}}},
    }
    allowed = application_layout_ids(manifest)
    state = {"version": 1, "positions": {}}
    saves = []
    html = (
        '<button id="application_edit">Edit</button><div class="application-canvas" style="position:relative">'
        + "".join(
            f'<div id="{name}" style="width:200px;height:60px"><input value="Hello World!"></div>'
            for name in sorted(allowed)
        )
        + "</div>"
    )

    def route(request_route) -> None:
        """Return inert HTML or validate the editor's data-only layout request."""
        nonlocal state
        request = request_route.request
        if request.url.endswith("/_agentix/layout"):
            if request.method == "POST":
                state = validate_layout(request.post_data_json, allowed=allowed)
                saves.append(state)
                request_route.fulfill(json={})
            else:
                request_route.fulfill(
                    json={
                        "editable": True,
                        "token": "fixture",
                        "controls": sorted(allowed),
                        "layout": state,
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
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("move application_first_output").wait_for()
            page.get_by_label("Edit application layout").click()
            for name in (
                "application_input_text",
                "application_status",
                "application_first_a",
                "application_first_output",
            ):
                control = page.locator("#" + name)
                before = control.bounding_box()
                page.get_by_label("move " + name, exact=True).press("ArrowRight")
                page.get_by_label("resize " + name, exact=True).press("ArrowRight")
                after = control.bounding_box()
                assert after["x"] == before["x"] + 10
                assert after["width"] == before["width"] + 10
                assert control.locator("input").input_value() == "Hello World!"
            page.get_by_label("Edit application layout").click()
            page.get_by_role("status").filter(has_text="Layout saved").wait_for()
            assert len(saves) == 1
            assert set(state["positions"]) == allowed
            page.reload()
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("move application_first_output").wait_for()
            for name, box in state["positions"].items():
                restored = page.locator("#" + name).bounding_box()
                assert (
                    restored["x"]
                    == box["x"] + page.locator(".application-canvas").bounding_box()["x"]
                )
                assert page.locator("#" + name + " input").input_value() == "Hello World!"
                assert (
                    page.locator("#" + name).evaluate("(el) => parseFloat(el.style.width)")
                    == box["width"]
                )
        finally:
            browser.close()


def test_v7_066_widget_source_name_accepts_only_a_tool_identifier() -> None:
    """A double-clicked widget resolves to <tool>_widget.py and nothing else."""
    from agentix.ui.applications import widget_source_name

    assert widget_source_name("count_words_in_text") == "count_words_in_text_widget.py"
    for value in ("", " Count", "../evil", "Count", "tool-name", "a" * 65, None):
        with pytest.raises(ValueError):
            widget_source_name(value)


@pytest.mark.browser
def test_v7_066_editor_posts_the_double_clicked_widget_tool() -> None:
    """Only a widget control of one tool reports its tool name to the parent page."""
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
        '<button id="application_edit">Edit</button><div class="application-canvas" style="position:relative">'
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
                "window.__selection = [];"
                "addEventListener('message', event => window.__selection.push(event.data));"
            )
            page.route("http://127.0.0.1:5874/**", route)
            page.goto("http://127.0.0.1:5874/")
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/application_editor.js").resolve())
            )
            page.get_by_label("visible application_first_output").wait_for(state="attached")
            page.locator("#application_first_output input").dblclick()
            page.wait_for_function("window.__selection.length === 1")
            assert page.evaluate("window.__selection") == [
                {"type": "agentix-widget-selection", "tool": "calculator"}
            ]
            page.locator("#application_status input").dblclick()
            page.locator("#application_input_text input").dblclick()
            page.wait_for_timeout(200)
            assert len(page.evaluate("window.__selection")) == 1
        finally:
            browser.close()


@pytest.mark.browser
def test_v7_066_parent_selects_the_widget_file_from_a_frame_message() -> None:
    """Only the framed application's valid tool name reaches the hidden selector."""
    import os

    from playwright.sync_api import expect, sync_playwright

    html = (
        '<div id="applications-frame"><iframe id="child" src="/child"></iframe></div>'
        '<div id="applications-widget-selection"><textarea></textarea></div>'
        '<button id="applications-widget-select">select</button>'
        "<script>document.getElementById('applications-widget-select')"
        ".addEventListener('click', () => {document.body.dataset.selected = "
        "document.querySelector('#applications-widget-selection textarea').value;});</script>"
    )
    child = (
        "<script>window.send = tool => parent.postMessage("
        "{type: 'agentix-widget-selection', tool}, '*');</script>"
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
            page.add_script_tag(
                path=str(Path("src/agentix/ui/assets/widget_selection.js").resolve())
            )
            page.evaluate(
                "document.getElementById('child').contentWindow.send('count_words_in_text')"
            )
            expect(page.locator("body")).to_have_attribute("data-selected", "count_words_in_text")
            page.evaluate("document.getElementById('child').contentWindow.send('../evil')")
            page.evaluate(
                "window.postMessage({type: 'agentix-widget-selection', tool: 'other_tool'}, '*')"
            )
            page.wait_for_timeout(200)
            assert page.locator("body").get_attribute("data-selected") == "count_words_in_text"
        finally:
            browser.close()
