"""Gradio editors for the owning session's explicitly rejected tool proposal."""

from typing import Any


def build_tool_repair(gr: Any, backend: Any, bind: Any, session_state: Any) -> None:
    """Keep source/tests editable while retaining ordinary human acceptance controls."""
    with gr.Accordion("Repair rejected tool", open=False, elem_id="tool-repair-panel"):
        status = gr.Markdown(
            "After rejecting an approval, load its available code and tests here.",
            elem_id="tool-repair-status",
        )
        load = gr.Button("Load rejected tool", elem_id="tool-repair-load")
        name = gr.Textbox(label="Rejected tool", interactive=False, elem_id="tool-repair-name")
        revision = gr.State(value="")
        with gr.Row():
            code = gr.Code(
                label="Tool implementation",
                language="python",
                lines=14,
                interactive=True,
                elem_id="tool-repair-code",
            )
            tests = gr.Code(
                label="Tool tests",
                language="python",
                lines=14,
                interactive=True,
                elem_id="tool-repair-tests",
            )
        restart = gr.Button("Save edits and restart validation", elem_id="tool-repair-restart")

    def load_draft(token: str | None, request: Any):
        """Display a safe fixed error for absent/stale owner proposals."""
        try:
            return backend.load(token, request)
        except ValueError as error:
            return "", "", "", "", str(error), token
        except Exception:
            return "", "", "", "", "Rejected tool could not be loaded.", token

    def resume(revision: str, code: str, tests: str, token: str | None, request: Any):
        """Dispatch explicitly; model/native work runs in the existing owner worker."""
        try:
            return backend.resume(revision, code, tests, token, request)
        except ValueError as error:
            return str(error), token
        except Exception:
            return "Repair could not start. No execution was authorized.", token

    load.click(
        fn=bind(load_draft),
        inputs=[session_state],
        outputs=[name, code, tests, revision, status, session_state],
        api_name=False,
    )
    restart.click(
        fn=bind(resume),
        inputs=[revision, code, tests, session_state],
        outputs=[status, session_state],
        api_name=False,
    )
