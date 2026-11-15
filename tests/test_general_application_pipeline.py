"""General application packaging never imports model modules on the host."""

import hashlib
import json

import pytest
from test_v5_tool_contracts import CODE

from agentix.application.app_workflow import ApplicationPipeline
from agentix.domain.tool_schema import extract_tool_schema
from agentix.lab.application_artifacts import application_digest
from agentix.storage.application_catalog import ApprovedTool

WIDGET = "\n".join(
    [
        '"""Trusted widget fixture."""',
        "import gradio as gr",
        "from calculator_code import calculator",
        "def create_widget(context):",
        '    """Create fixture controls."""',
        "    with gr.Group():",
        '        a = gr.Number(elem_id=context.elem_id("a"))',
        '        b = gr.Number(elem_id=context.elem_id("b"))',
        '        output = gr.Number(elem_id=context.elem_id("output"))',
        '        button = gr.Button("Calculate", elem_id=context.elem_id("execute"))',
        "        button.click(calculator, [a,b], output, api_name=context.api_name)",
        '    return {"inputs": {"a": a, "b": b}, "output": output, "button": button, "render": lambda value: value}',
    ]
)


def make_candidate(tmp_path, widget_tests="# proposed widget tests", widget_store=None, code=None):
    """Canonical arbitrary names must replace the fixed count-tools dependency."""
    source = CODE.encode() if code is None else code
    schema = extract_tool_schema("calculator", source.decode("utf-8"))
    contract = {
        "version": 1,
        "cases": [
            {
                "id": "sum",
                "purpose": "Known sum",
                "function": "calculator",
                "kwargs": {"a": 2, "b": 3},
                "expect": {"kind": "value", "value": 5},
            }
        ],
    }
    tool = ApprovedTool(
        "calculator",
        "calculator",
        "calculator",
        source,
        b"# reviewed tests",
        "a" * 64,
        contract,
        schema,
    )
    calls = []

    def factory(folder):
        """Return authored proposals without importing widget source."""

        def client(role, content):
            calls.append(role)
            if "Widget" in role:
                return {
                    "widget_code": WIDGET,
                    "tests_code": widget_tests,
                    "notes": "fixture",
                }
            return {
                "inputs": {
                    "a": {"type": "integer", "description": "First addend"},
                    "b": {"type": "integer", "description": "Second addend"},
                },
                "widgets": [{"id": "calculator", "tool": "calculator"}],
                "connection_code": (
                    '"""Connect the approved calculator."""\n'
                    "def run(payload: dict, call) -> None:\n"
                    '    """Call the approved calculator once."""\n'
                    '    call("calculator", a=payload["a"], b=payload["b"])\n'
                ),
                "notes": "fixture",
            }

        return client

    item = ApplicationPipeline(tmp_path, factory, widget_store=widget_store).generate(
        "Make a calculator application", tools={"calculator": tool}
    )
    return item, calls


def test_general_package_uses_only_catalog_tools_and_model_widgets(tmp_path):
    """The selected arbitrary catalog closure replaces fixed word/vowel files."""
    item, calls = make_candidate(tmp_path)
    files = json.loads((item.package / "application.json").read_bytes())["files"]
    assert "calculator_code.py" in files and "calculator_widget.py" in files
    assert not any("count_words" in name for name in files)
    assert application_digest(item.package) == item.digest
    assert not item.approved and not item.verified
    assert calls == ["General Assembler", "General Widget Designer"]


@pytest.mark.windows_isolation
def test_general_operation_executes_inside_native_boundary(tmp_path):
    """A real AppContainer returns the expected arbitrary-tool result."""
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import execute_application

    item, _ = make_candidate(tmp_path)
    snapshot = approve_application(item.package, item.digest)
    assert execute_application(snapshot, {"calculator": {"a": 2, "b": 3}}) == {"calculator": 5}


def test_general_package_rejects_modified_maintained_runtime(tmp_path):
    """Even updated manifest hashes cannot authorize a rewritten compositor."""
    item, _ = make_candidate(tmp_path)
    member = item.package / "app.py"
    member.write_text('raise RuntimeError("unreviewed compositor")', encoding="utf-8")
    manifest_path = item.package / "application.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"]["app.py"] = hashlib.sha256(member.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ValueError, match="Maintained compositor"):
        application_digest(item.package)


@pytest.mark.windows_isolation
def test_general_widget_tests_run_natively_without_tool_test_files(tmp_path):
    """Only reviewed widget tests are executed, separately from host acceptance."""
    from agentix.lab.application_artifacts import approve_application
    from agentix.lab.application_session import run_application_widget_tests

    item, _ = make_candidate(tmp_path)
    snapshot = approve_application(item.package, item.digest)
    # The fixture proposal intentionally has no tests; it must not count as success.
    with pytest.raises(RuntimeError):
        run_application_widget_tests(snapshot, ["calculator"])


@pytest.mark.browser
@pytest.mark.windows_isolation
def test_general_compositor_with_real_native_browser(tmp_path):
    """Exercise a non-counter model boundary fixture through the real native GUI."""
    from agentix.application.app_workflow import ApplicationSupervisor

    widget_tests = "\n".join(
        [
            '"""Trusted widget interface tests."""',
            "import unittest",
            "import gradio as gr",
            "from calculator_widget import create_widget",
            "from application_context import Context",
            "from element_ids import ElementIds",
            "class WidgetTests(unittest.TestCase):",
            '    """Check control contracts and actual callback."""',
            "    def test_controls_and_callback(self):",
            '        """Use actual Gradio construction inside isolation."""',
            "        with gr.Blocks() as demo:",
            '            refs = create_widget(Context("calculator",ElementIds(),["a","b"]))',
            '        self.assertEqual(set(refs["inputs"]), {"a","b"})',
            '        self.assertIsInstance(refs["output"], gr.Number)',
            "        self.assertEqual(demo.fns[0].fn(2,3),5)",
        ]
    )
    item, _ = make_candidate(tmp_path, widget_tests)
    supervisor = ApplicationSupervisor()
    supervisor.approve(item, item.identity, True)
    try:
        supervisor.verify(item, "http://127.0.0.1:7879")
        assert item.verified
        assert (item.folder / "browser-acceptance.json").is_file()
    finally:
        item.close()


def test_widget_publication_rebinds_dependency_and_preserves_exact_bytes(tmp_path):
    """Publishing the newly approved widget must not look like concurrent tampering."""
    from agentix.storage.widget_store import StoredWidget

    class Store:
        """Authored metadata double; real persistence is checked separately."""

        def __init__(self):
            """Start without a prior widget grant."""
            self.value = None
            self.published = 0

        def load(self, tool):
            """Return the current recorded widget identity."""
            return self.value

        def publish(self, tool, proposal, *, css):
            """Record exactly the reviewed proposal bytes and style."""
            self.value = StoredWidget(dict(proposal), True, css)
            self.published += 1

    store = Store()
    item, _ = make_candidate(tmp_path, widget_store=store)
    assert (item.package / "calculator_widget.py").read_bytes() == WIDGET.encode("utf-8")
    item.widget_commit(item)
    item.dependency_check()
    item.widget_commit(item)
    assert store.published == 1


def test_general_widget_test_file_has_one_editable_grouped_review_entry(tmp_path):
    """The real co-located filename must open the widget-test pane without duplicate aliases."""
    from agentix.application.app_review import ApplicationReview

    item, _ = make_candidate(tmp_path)
    review = ApplicationReview()
    entries = review.entries(item)
    assert not any(key.startswith("proposed_tests/") for _, key in entries)
    assert (
        review.panes(item, "calculator_widget_tests.py")["widget_tests"]
        == "# proposed widget tests"
    )
    assert review.read(item, "calculator_widget_tests.py")[1] is True
    before = item.digest
    code = (item.package / "calculator_code.py").read_bytes()
    review.save(
        item, "calculator_widget_tests.py", '"""Explicit test revision."""\n', item.identity
    )
    assert item.digest != before and not item.approved
    assert (
        item.package / "calculator_widget_tests.py"
    ).read_bytes() == b'"""Explicit test revision."""\n'
    assert (item.package / "calculator_code.py").read_bytes() == code


def test_designer_receives_typed_context_and_real_test_framework_contract():
    """The model needs an interface contract, not a reference widget implementation."""
    from agentix.agents.catalog_agents import CatalogWidgetDesigner

    seen = []

    def client(role, content):
        """Capture data-only requirements, returning an authored widget fixture."""
        seen.append(content)
        return {"widget_code": WIDGET, "tests_code": "# provisional", "notes": "fixture"}

    tool = ApprovedTool(
        "calculator",
        "calculator",
        "calculator",
        CODE.encode(),
        b"# tests",
        "a" * 64,
        {},
        extract_tool_schema("calculator", CODE),
    )
    CatalogWidgetDesigner(client).generate(tool)
    context = seen[0]["requirements"]["context_contract"]
    assert context["api_name"] == {"type": "string", "callable": False}
    assert context["elem_id"]["callable"] is True
    assert "no precision=0" in seen[0]["requirements"]["integer_input_policy"]
    assert "return None" in seen[0]["requirements"]["error_policy"]
    assert "demo.fns" in seen[0]["requirements"]["testing_contract"]
    assert "gr.Context" in seen[0]["requirements"]["testing_contract"]
    contract = seen[0]["requirements"]["testing_contract"]
    assert "Context(instance, ids, parameters)" in contract
    assert "ElementIds()" in contract
    assert "no api_name constructor argument" in contract
    assert "from element_ids import ElementIds" in contract
    assert "ids = ElementIds()" in contract
    assert "argument order" in contract
    assert "do not swap" in contract
    assert "with gr.Blocks() as demo:" in contract
    assert "create_widget(context) must be called INSIDE" in contract
    assert "outside a Blocks context" in contract
    assert "unittest.TestCase" in contract
    assert "test_* methods" in contract
    assert "pytest-style" in contract
    assert "demo.fns[0].fn(" in contract
    assert "self.assert" in contract
    assert "do not exist" in contract
    system = seen[0]["system"]
    assert "NEVER return the gr.Group" in system
    assert "return value MUST be the dictionary" in system
    assert "import gradio as gr" in system
    assert "no 'gr' package" in system
    assert "never import application_context or element_ids" in system
    assert "never hardcode expected elem_id strings" in contract
    assert "host-allocated" in contract
    assert "api_name" in contract.split("host-allocated")[1][:400]
    assert WIDGET not in str(seen[0])


def test_failed_widget_gate_retains_bounded_private_diagnostics(monkeypatch):
    """An untrusted failed report is diagnostic data, never a passing verdict."""
    from types import SimpleNamespace

    from agentix.lab import application_session as module

    class FailedSession:
        """Explicit native-session double with one reported test error."""

        def __init__(self, *args, **kwargs):
            """Expose a failure without launching native processes."""
            self.diagnostics = {
                "native": (1, "unused", False),
                "provisional_tests": {
                    "run": 1,
                    "successful": False,
                    "detail": "Synthetic callback failure",
                },
            }
            self.native_thread = SimpleNamespace(join=lambda timeout: None)

        def __enter__(self):
            """Return the controlled diagnostics."""
            return self

        def __exit__(self, *args):
            """No external resource was allocated."""

    monkeypatch.setattr(module, "ApplicationSession", FailedSession)
    with pytest.raises(RuntimeError) as failure:
        module.run_application_widget_tests(object(), ["calculator"])
    assert failure.value.report["untrusted_report"]["detail"] == "Synthetic callback failure"
    assert failure.value.report["native_exit_code"] == 1
    assert "Synthetic callback failure" not in str(failure.value)


def test_widget_only_group_edit_preserves_exact_approved_tool_line_endings(tmp_path):
    """Saving related widget buffers must not rewrite an unchanged CRLF tool."""
    from agentix.application.app_review import ApplicationReview

    code = CODE.replace("\n", "\r\n").encode()
    item, _ = make_candidate(tmp_path, code=code)
    review = ApplicationReview()
    panes = review.panes(item, "calculator_widget.py")
    changed = review.save_group(
        item,
        {
            "role": panes["role"],
            "code": panes["code"],
            "widget": panes["widget"] + "\n# Reviewed widget-only change\n",
            "tool_tests": panes["tool_tests"],
            "widget_tests": panes["widget_tests"],
        },
        item.identity,
    )
    assert changed
    assert not json.loads(item.review_text).get("pending_tool_revisions")
    assert (item.package / "calculator_code.py").read_bytes() == code
