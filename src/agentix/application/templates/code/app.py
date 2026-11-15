"""Native compositor for persisted connection code and approved reusable widgets."""

import importlib
from collections.abc import Iterator

import gradio as gr
from application_context import Context
from element_ids import ElementIds
from operation import MANIFEST, execute


def application_title() -> str:
    """Read the host-staged display name; never accept markup or a missing snapshot.

    The supervisor writes application_display.json beside this module only when the
    owner named the application. Markdown-active characters are dropped so a name
    cannot restyle the heading, and any read or shape failure keeps the default.
    """
    import json
    from pathlib import Path

    try:
        record = json.loads(
            Path(__file__).with_name("application_display.json").read_text(encoding="utf-8")
        )
        name = record["name"]
    except (OSError, ValueError, KeyError, TypeError):
        return "Generated Application"
    if type(name) is not str:
        return "Generated Application"
    cleaned = "".join(
        character
        for character in name
        if character.isprintable() and character not in "\\*_#[]<>|`"
    ).strip()
    return cleaned[:120] or "Generated Application"


def input_component(name: str, shape: dict) -> gr.components.Component:
    """Build a typed public application control with a stable non-widget identity."""
    options = {"label": name, "elem_id": "application_input_" + name}
    if "enum" in shape:
        return gr.Dropdown(choices=shape["enum"], **options)
    if shape["type"] == "boolean":
        return gr.Checkbox(**options)
    if shape["type"] in {"number", "integer"}:
        return gr.Number(**options)
    if shape["type"] == "array":
        return gr.Textbox(info="Enter a JSON array", **options)
    return gr.Textbox(**options)


def create_application() -> gr.Blocks:
    """Render inputs/widgets and connect Run directly to generated Python in isolation."""
    import json

    ids = ElementIds()
    widgets, managed = {}, []
    with gr.Blocks(title="Generated application") as demo:
        gr.Markdown("## " + application_title())
        button = gr.Button(
            "Run application",
            elem_id="application_execute",
            elem_classes=["application-run-button"],
        )
        with gr.Column(elem_classes=["application-canvas"]):
            inputs = {
                name: input_component(name, shape) for name, shape in MANIFEST["inputs"].items()
            }
            for widget in MANIFEST["widgets"]:
                identity, name = widget["id"], widget["tool"]
                contract = MANIFEST["tools"][name]
                refs = importlib.import_module(name + "_widget").create_widget(
                    Context(identity, ids, list(contract["parameters"]))
                )
                if (
                    type(refs) is not dict
                    or not {"inputs", "output", "button", "render"} <= set(refs)
                    or set(refs["inputs"]) != set(contract["parameters"])
                    or not callable(refs["render"])
                ):
                    raise ValueError("Widget references violate the reviewed interface")
                widgets[identity] = refs
                refs["button"].visible = False
                for name, component in refs["inputs"].items():
                    component.interactive = False
                    managed.append((identity, name, component))
            status = gr.Textbox(label="Status", interactive=False, elem_id="application_status")

        def run_all(*values: object) -> Iterator[list[object]]:
            """Clear stale displays, run complete code and populate observed widget arguments."""
            yield [None] * (len(widgets) + len(managed)) + ["Running"]
            try:
                payload = dict(zip(inputs, values, strict=True))
                for name, shape in MANIFEST["inputs"].items():
                    if shape["type"] == "array":
                        payload[name] = json.loads(payload[name])
                results, arguments = execute(payload)
                yield (
                    [refs["render"](results[identity]) for identity, refs in widgets.items()]
                    + [arguments[identity][name] for identity, name, _ in managed]
                    + ["Completed"]
                )
            except Exception:
                yield [None] * (len(widgets) + len(managed)) + [
                    "Execution failed; check inputs and reviewed contracts"
                ]

        button.click(
            run_all,
            list(inputs.values()),
            [refs["output"] for refs in widgets.values()]
            + [component for _, _, component in managed]
            + [status],
            api_name="run_application",
            concurrency_limit=1,
        )
    return demo
