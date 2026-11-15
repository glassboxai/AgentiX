"""V5-ERR-041-01: general dataflow must preserve shared values and typed sources."""

from collections.abc import Callable
from pathlib import Path

import pytest

from agentix.application.app_workflow import Candidate

SCHEMAS = {
    "measure": {"parameters": {"text": {"type": "string"}}, "returns": {"type": "integer"}},
    "samples": {
        "parameters": {"size": {"type": "integer"}},
        "returns": {"type": "array", "items": {"type": "number"}},
    },
    "combine": {
        "parameters": {"x": {"type": "number"}, "y": {"type": "number"}},
        "returns": {"type": "number"},
    },
}


def workflow() -> dict:
    """Return a fork with repeated tools, one shared source and one sampled item."""
    return {
        "nodes": [
            {
                "id": "left",
                "tool": "measure",
                "inputs": {"text": {"node": None, "input": "document"}},
            },
            {
                "id": "right",
                "tool": "measure",
                "inputs": {"text": {"node": None, "input": "document"}},
            },
            {"id": "draw", "tool": "samples", "inputs": {"size": {"node": None, "value": 1}}},
            {
                "id": "first",
                "tool": "combine",
                "inputs": {"x": {"node": "left"}, "y": {"node": "draw", "index": 0}},
            },
            {
                "id": "second",
                "tool": "combine",
                "inputs": {"x": {"node": "right"}, "y": {"node": "draw", "index": 0}},
            },
        ]
    }


def reviewed_tools() -> dict:
    """Author independent values with an early incompatible choice requiring backtracking."""
    from types import SimpleNamespace

    tables = {
        "measure": [({"text": "a"}, 1), ({"text": "bb"}, 2)],
        "samples": [({"size": 1}, [3.0])],
        "combine": [({"x": 2, "y": 3.0}, 6.0)],
    }
    return {
        name: SimpleNamespace(
            function=name,
            schema=SCHEMAS[name],
            reviewed_contract={
                "cases": [
                    {
                        "function": name,
                        "kwargs": kwargs,
                        "expect": {"kind": "value", "value": value},
                    }
                    for kwargs, value in table
                ]
            },
        )
        for name, table in tables.items()
    }


def make_workflow_candidate(tmp_path: Path) -> Candidate:
    """Package only independently authored trusted fixtures, never existing artifacts."""
    from agentix.application.app_workflow import ApplicationPipeline
    from agentix.domain.tool_schema import extract_tool_schema
    from agentix.storage.application_catalog import ApprovedTool

    bodies = {
        "measure": 'def measure(text: Annotated[str, "Document"]) -> Annotated[int, "Length"]:\n    """Measure fixture text."""\n    return len(text)\n',
        "samples": 'def samples(size: Annotated[int, "Sample count"]) -> Annotated[list[float], "Fixture samples"]:\n    """Return controlled samples for independent dataflow testing."""\n    return [3.0] * size\n',
        "combine": 'def combine(x: Annotated[float, "First factor"], y: Annotated[float, "Second factor"]) -> Annotated[float, "Product"]:\n    """Multiply fixture factors."""\n    return x * y\n',
    }
    tools = reviewed_tools()
    widgets = {}
    for name, body in bodies.items():
        code = (
            '"""Independent trusted fixture."""\nfrom typing import Annotated\n\n\n' + body
        ).encode()
        schema = extract_tool_schema(name, code.decode())
        tools[name] = ApprovedTool(
            name,
            name,
            name,
            code,
            b"# fixture tests",
            "a" * 64,
            tools[name].reviewed_contract,
            schema,
        )
        params = list(schema["parameters"])
        controls = [
            f'        {parameter} = gr.{"Textbox" if shape["type"] == "string" else "Number"}(elem_id=context.elem_id("{parameter}"))'
            for parameter, shape in schema["parameters"].items()
        ]
        widgets[name] = "\n".join(
            [
                '"""Independent trusted fixture widget."""',
                "import gradio as gr",
                f"from {name}_code import {name}",
                "def create_widget(context):",
                '    """Expose fixture controls and a reviewed callback."""',
                "    with gr.Group():",
                *controls,
                (
                    '        output = gr.Dataframe(headers=["Value"], datatype=["number"], column_count=(1, "fixed"), row_count=(0, "dynamic"), interactive=False, elem_id=context.elem_id("output"))'
                    if name == "samples"
                    else '        output = gr.Textbox(elem_id=context.elem_id("output"))'
                ),
                '        button = gr.Button("Run", elem_id=context.elem_id("execute"))',
                f"        button.click({name}, [{', '.join(params)}], output, api_name=context.api_name)",
                '    return {"inputs": {'
                + ", ".join(f'"{parameter}": {parameter}' for parameter in params)
                + '}, "output": output, "button": button, "render": '
                + ("lambda values: [[value] for value in values]" if name == "samples" else "str")
                + "}",
            ]
        )

    def factory(folder: Path) -> Callable[[str, dict], dict]:
        """Inject fixture proposals without a model or subprocess."""

        def client(role: str, content: dict) -> dict:
            """Return independently authored proposals for the requested fixture role."""
            if role == "General Assembler":
                return {
                    "inputs": {"document": {"type": "string", "description": "Document"}},
                    "widgets": [
                        {"id": node["id"], "tool": node["tool"]} for node in workflow()["nodes"]
                    ],
                    "connection_code": (
                        '"""Connect fixture measurements and sampled products."""\n'
                        "def run(payload: dict, call) -> None:\n"
                        '    """Call each fixture widget once with the shared document."""\n'
                        '    left = call("left", text=payload["document"])\n'
                        '    right = call("right", text=payload["document"])\n'
                        '    draw = call("draw", size=1)\n'
                        '    call("first", x=left, y=draw[0])\n'
                        '    call("second", x=right, y=draw[0])\n'
                    ),
                    "notes": "One shared document, two measurements and one reused sample feed two products.",
                }
            name = content["requirements"]["approved_tool_contract"]["function"]
            return {"widget_code": widgets[name], "tests_code": "# fixture", "notes": "fixture"}

        return client

    return ApplicationPipeline(tmp_path, factory).generate(
        "Compose fixture measurements and sampled products", tools=tools
    )


def test_packaged_plan_retains_sources_and_independent_acceptance(tmp_path: Path) -> None:
    """The exact review binds flat inputs, the widget inventory and final results."""
    import json

    candidate = make_workflow_candidate(tmp_path)
    review = json.loads(candidate.review_text)
    manifest = review["manifest"]
    assert manifest["schema_version"] == 3
    assert manifest["inputs"] == {"document": {"type": "string", "description": "Document"}}
    assert manifest["widgets"] == [
        {"id": "left", "tool": "measure"},
        {"id": "right", "tool": "measure"},
        {"id": "draw", "tool": "samples"},
        {"id": "first", "tool": "combine"},
        {"id": "second", "tool": "combine"},
    ]
    assert review["independent_acceptance"]["payload"] == {"document": "bb"}
    assert review["independent_acceptance"]["expected"] == {
        "left": 2,
        "right": 2,
        "draw": [3.0],
        "first": 6.0,
        "second": 6.0,
    }
    assert review["acceptance_proposal"]["pending"] == []
    assert (candidate.package / "application_logic.py").is_file()
    assert not (candidate.package / "bindings.py").exists()


@pytest.mark.windows_isolation
def test_native_shared_projected_fork_has_independent_results(tmp_path: Path) -> None:
    """Host-observed native results match authored expectations without live servers."""
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import execute_application

    candidate = make_workflow_candidate(tmp_path)
    approved = approve_application(candidate.package, candidate.digest)
    assert execute_application(approved, {"document": "bb"}) == {
        "left": 2,
        "right": 2,
        "draw": [3.0],
        "first": 6.0,
        "second": 6.0,
    }


@pytest.mark.frameworks
def test_real_gradio_shares_one_input_and_updates_connected_controls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Execute maintained callbacks in memory using only trusted fixture modules."""
    import importlib
    import sys

    from agentix.application.code_package import runtime_template
    from agentix.application.templates import bindings

    candidate = make_workflow_candidate(tmp_path)
    monkeypatch.syspath_prepend(str(candidate.package))
    for name in (
        "operation",
        "application_context",
        "element_ids",
        "measure_code",
        "samples_code",
        "combine_code",
        "measure_widget",
        "samples_widget",
        "combine_widget",
    ):
        monkeypatch.delitem(sys.modules, name, raising=False)
    monkeypatch.setitem(sys.modules, "bindings", bindings)
    spec = importlib.util.spec_from_file_location("trusted_compositor", runtime_template("app.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    demo = module.create_application()
    try:
        callback = next(event for event in demo.fns.values() if event.api_name == "run_application")
        assert len(callback.inputs) == 1
        updates = list(callback.fn("bb"))
        assert updates[0][-1] == "Running"
        assert updates[-1][:5] == ["2", "2", [[3.0]], "6.0", "6.0"]
        assert updates[-1][5:] == ["bb", "bb", 1, 2, 3.0, 2, 3.0, "Completed"]
        assert all(component.interactive is False for component in callback.outputs[5:-1])
        failed = list(callback.fn(None))[-1]
        assert failed[:-1] == [None] * 12
        assert failed[-1] == "Execution failed; check inputs and reviewed contracts"
    finally:
        demo.close()
        for name in (
            "operation",
            "application_context",
            "element_ids",
            "measure_code",
            "samples_code",
            "combine_code",
            "measure_widget",
            "samples_widget",
            "combine_widget",
        ):
            monkeypatch.delitem(sys.modules, name, raising=False)


@pytest.mark.browser
@pytest.mark.windows_isolation
def test_native_browser_composition_uses_only_the_shared_external_input(tmp_path: Path) -> None:
    """A disposable native preview verifies real controls and every connected result."""
    import json

    from agentix.application.general_acceptance import browser_verify
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_panel import ApplicationPreview

    candidate = make_workflow_candidate(tmp_path)
    preview = ApplicationPreview(approve_application(candidate.package, candidate.digest), None)
    review = json.loads(candidate.review_text)
    review["independent_acceptance"].update(
        payload={"document": "abc"},
        expected={
            "left": "3",
            "right": "3",
            "draw": [3.0],
            "first": "9.0",
            "second": "9.0",
        },
    )
    try:
        browser_verify(preview, candidate, review)
        evidence = json.loads((candidate.folder / "browser-acceptance.json").read_bytes())
        assert evidence["managed_widgets_verified_in_application"] == 5
        assert evidence["standalone_widgets"] == 0
        assert evidence["fresh_completed_events"] == 2
    finally:
        preview.close()


@pytest.mark.parametrize("expected", [3, 3.0])
def test_numeric_display_comparison_preserves_exact_value(expected: int | float) -> None:
    """V5-ERR-041-02: integer-formatted floats match without accepting numeric prefixes."""
    from agentix.application.general_acceptance import display_expectation

    matcher = display_expectation(expected)
    assert matcher.fullmatch(" 3 ")
    assert matcher.fullmatch("3.0")
    assert matcher.fullmatch("3.00")
    for wrong in ("30", "3.1", "13", "3junk", "nan"):
        assert not matcher.fullmatch(wrong)
