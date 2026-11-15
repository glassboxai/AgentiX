"""Maintained reference widget for native feasibility tests, not LLM evidence."""

import gradio as gr


def create_widget(context):
    """Build one isolated instance and bind only its injected approved tool callback."""
    with gr.Group():
        text = gr.Textbox(label="Text to analyze", elem_id=context.elem_id("input"))
        output = gr.Number(label="Vowel count", precision=0, elem_id=context.elem_id("output"))
        button = gr.Button("Count vowels", elem_id=context.elem_id("execute"))
        button.click(
            fn=context.invoke, inputs=text, outputs=output, queue=False, api_name=context.api_name
        )
    return {"input": text, "output": output, "button": button}
