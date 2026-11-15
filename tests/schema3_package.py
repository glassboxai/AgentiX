"""Build a real schema-3 application package from approved catalog fixtures.

The helper replaces the retired fixed text-analysis package. It performs no model
inference: the coordinator boundary returns authored artifacts, and the pipeline
still validates manifests, connection code and widget contracts.
"""

from pathlib import Path

CONNECTION_CODE = "\n".join(
    [
        '"""Connect approved catalog calls."""',
        "def run(payload: dict, call) -> None:",
        '    """Call every approved tool with the shared text input."""',
        '    call("count_words_in_text", text=payload["text"])',
        '    call("count_vowels_in_text", text=payload["text"])',
        "",
    ]
)

WIDGET_TESTS = (
    "import unittest\n\n\n"
    "class WidgetTests(unittest.TestCase):\n"
    "    def test_placeholder(self):\n"
    "        self.assertTrue(True)\n"
)


def build(root: Path, *, query: str = "Count words and vowels"):
    """Return a generated candidate whose package is a valid schema-3 application."""
    from test_application_catalog import installed, registry

    from agentix.application.app_workflow import ApplicationPipeline

    tools_root = root / "tools"
    tools_root.mkdir(parents=True, exist_ok=True)
    tools = registry(installed(tools_root)).resolve()

    def factory(folder):
        """Return authored artifacts across the production coordinator boundary."""

        def client(role, content):
            """Never infer with a real model in package fixtures."""
            if role == "General Widget Designer":
                module = content["requirements"]["approved_tool_contract"]["module"]
                return {
                    "widget_code": widget_source(module),
                    "tests_code": WIDGET_TESTS,
                    "notes": "fixture",
                }
            catalog = content["requirements"]["approved_catalog"]
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [{"id": name, "tool": name} for name in sorted(catalog)],
                "connection_code": CONNECTION_CODE,
                "notes": "fixture",
            }

        return client

    return ApplicationPipeline(root / "applications", factory).generate(query, tools=tools)


def widget_source(module: str) -> str:
    """Render a minimal approved widget importing the exact tool module."""
    function = module.removesuffix("_code")
    return (
        '"""Reviewed widget fixture."""\n'
        "import gradio as gr\n"
        f"from {module} import {function}\n\n\n"
        "def create_widget(context):\n"
        '    """Build the reviewed input, action and output group."""\n'
        "    with gr.Group() as group:\n"
        f'        value = gr.Textbox(label="Text", elem_id=context.elem_id("input"))\n'
        f'        run = gr.Button("Run", elem_id=context.elem_id("execute"))\n'
        f'        output = gr.Number(label="Result", elem_id=context.elem_id("output"))\n'
        "    run.click(\n"
        f"        lambda text: {function}(text) if isinstance(text, str) else None,\n"
        "        inputs=value,\n"
        "        outputs=output,\n"
        "        api_name=context.api_name,\n"
        "    )\n"
        "    return {\n"
        '        "inputs": {"text": value},\n'
        '        "output": output,\n'
        '        "button": run,\n'
        '        "render": lambda result: result,\n'
        "    }\n"
    )


def package(root: Path) -> Path:
    """Return only the generated package directory for capture-level tests."""
    return build(root).package
