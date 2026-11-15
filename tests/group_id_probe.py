"""Trusted minimal Gradio structural-ID diagnostic; contains no generated source."""

import os
import sys

os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
from pathlib import Path

import gradio as gr

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src/agentix/application/templates/code")
)
from application_context import Context, ElementIds

if __name__ == "__main__":

    def count(text):
        """Exercise numeric and empty postprocessing with a trusted deterministic fixture."""
        return None if len(text) > 16000 else len(text.split())

    ids = ElementIds()
    with gr.Blocks() as demo:
        with gr.Row():
            for name in ("words", "vowels", "words"):
                context = Context(name, ids, [])
                with gr.Group(elem_id=context.elem_id("group")):
                    value = gr.Textbox(elem_id=context.elem_id("input"))
                    result = gr.Number(elem_id=context.elem_id("output"))
                    button = gr.Button("Count", elem_id=context.elem_id("execute"))
                    button.click(count, inputs=value, outputs=result)
    with demo:
        gr.Button("Close", elem_id="application_stop")
    import uvicorn
    from fastapi import FastAPI

    app = gr.mount_gradio_app(
        FastAPI(), demo, path="/", ssr_mode=False, theme=gr.themes.Base(primary_hue="cyan")
    )
    uvicorn.run(app, host="127.0.0.1", port=int(sys.argv[1]))
