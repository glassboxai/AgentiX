"""Floating Gradio code-help view; movement/resize behavior lives in chathelper.js."""

from agentix.controllers.chathelper import ChatHelperBackend


def build_chathelper(gr, backend, bind, selected_file, session_state, panes):
    """Build one session-owned read-only helper, initially hidden by maintained CSS."""
    helper = ChatHelperBackend(backend.sessions, backend)
    pane = gr.Textbox(
        value="code", elem_classes=["agentix-internal-input"], elem_id="chathelper-pane"
    )
    with gr.Column(elem_id="chathelper-window"):
        gr.HTML(
            '<div id="chathelper-title" tabindex="0">Code help <button type="button" id="chathelper-minimize" aria-label="Minimize code help">−</button><button type="button" id="chathelper-close" aria-label="Close code help">×</button></div>'
            '<div id="chathelper-file" role="status" aria-live="polite">No file selected</div>'
        )
        transcript = gr.Markdown(
            value="",
            elem_id="chathelper-transcript",
        )
        question = gr.Textbox(
            label="Question about this code", lines=2, elem_id="chathelper-question"
        )
        send = gr.Button("Ask", elem_id="chathelper-send")
        status = gr.Markdown(
            "Read-only assistance. Nothing is executed or modified.", elem_id="chathelper-status"
        )

    def ask(pane, selected, code, widget, tool_tests, widget_tests, question, token, request):
        """Use fixed safe errors; vendor messages, code and credentials are never echoed."""
        try:
            buffers = {
                "code": code,
                "widget": widget,
                "tool_tests": tool_tests,
                "widget_tests": widget_tests,
            }
            text, cleared, owned = helper.ask(
                pane, selected, buffers.get(pane), question, token, request
            )
            return text, cleared, owned, "Explanation ready. Review advice before using it."
        except Exception:
            return (
                "",
                question,
                token,
                "Code help unavailable. Select a tool-related file with specifications and check the model settings and remote consent.",
            )

    send.click(
        fn=bind(ask),
        inputs=[pane, selected_file, *panes, question, session_state],
        outputs=[transcript, question, session_state, status],
        api_name=False,
    )
