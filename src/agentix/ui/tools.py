"""Tools tab Gradio controls and bindings; business behavior lives in agentix.controllers.tools."""

from typing import Any

CHATBOT_HEIGHT_PIXELS = 580
QUERY_INPUT_LINES = 2
QUERY_INPUT_SCALE = 4
SEND_BUTTON_MIN_WIDTH = 46
CHAT_COLUMN_SCALE = 1
TOOLS_SIDEBAR_WIDTH_PIXELS = 420
APPROVAL_PREVIEW_LINES = 14
STATUS_TIMER_SECONDS = 1.0  # Session polling without progress flicker.
REFRESH_OUTPUT_COUNT = 2
SUBMIT_OUTPUT_COUNT = 3
READINESS_OUTPUT_COUNT = 2
POLL_OUTPUT_COUNT = 7
VALIDATION_OUTPUT_COUNT = 1


def build_tools_frontend(
    gr: Any,
    callbacks: Any,
    bind: Any,
    session_state: Any,
    request_state: Any,
    progress: Any = None,
    maintenance: Any = None,
    repair_backend: Any = None,
    dialog: Any = None,
) -> None:
    """Render the conversation plus one collapsible right sidebar for catalog and review."""
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    if dialog is None:
        from agentix.ui.message_dialog import MessageDialog

        dialog = MessageDialog(gr)
    with gr.Row(elem_id="agentix-workspace"):
        # ----------------------------------------------------------------------
        # WORK AREA: Conversational Chat
        # ----------------------------------------------------------------------
        with gr.Column(scale=CHAT_COLUMN_SCALE):
            chatbot = gr.Chatbot(
                label="Conversation",
                height=CHATBOT_HEIGHT_PIXELS,
                elem_id="agentix-chat",
                buttons=[],
            )
            with gr.Row(elem_id="query-composer"):
                msg_input = gr.Textbox(
                    placeholder="Enter your calculation or query here...",
                    label="User Query",
                    lines=QUERY_INPUT_LINES,
                    scale=QUERY_INPUT_SCALE,
                )
                submit_btn = gr.Button(
                    "Send query",
                    variant="primary",
                    scale=0,
                    min_width=SEND_BUTTON_MIN_WIDTH,
                    elem_id="send-query",
                )

    # ----------------------------------------------------------------------
    # RIGHT SIDEBAR: Security Sandbox & Catalog
    # ----------------------------------------------------------------------
    with gr.Sidebar(
        label="Tools panel",
        position="right",
        open=False,
        width=TOOLS_SIDEBAR_WIDTH_PIXELS,
        elem_id="tools-sidebar",
    ):
        with gr.Accordion("Installed Tools Catalog", open=True):
            if maintenance is not None:
                reveal_tools = gr.Button(
                    "View in explorer", elem_id="tools-reveal", scale=0, size="sm"
                )
            catalog_display = gr.Markdown(value="Catalog loads for the current session.")
        if maintenance is not None:
            from agentix.ui.catalog_actions import build_delete_controls

            reseal_tools = gr.Button(
                "Autovalidate all tools (reseal unchanged, run changed)",
                elem_id="tools-reseal",
                size="sm",
            )
            reseal_status = gr.Markdown("", elem_id="tools-reseal-status")
            selected_tool = gr.Dropdown(
                choices=[], label="Installed tool", elem_id="installed-tool-selection"
            )

            def reseal_all(token: str | None, request: Any):
                """Rebind intact approvals under the current policy; never execute here."""
                message, owned = maintenance.reseal_tools(token, request)
                return message, owned

            reseal_tools.click(
                fn=bind(dialog.guard_result(reseal_all, 1)),
                inputs=[session_state],
                outputs=[reseal_status, session_state, *dialog.outputs()],
                api_name=False,
                show_progress="hidden",
            )
            build_delete_controls(
                gr, maintenance, bind, "tool", selected_tool, session_state, dialog=dialog
            )

            def refresh_tools(selected: str, token: str | None, request: Any):
                """Refresh selectable installed tool IDs without importing source."""
                choices, owned = maintenance.choices("tool", token, request)
                names = {identity for _, identity in choices}
                return gr.Dropdown(
                    choices=choices, value=selected if selected in names else None
                ), owned

            catalog_display.change(
                fn=bind(dialog.guard_result(refresh_tools, REFRESH_OUTPUT_COUNT)),
                inputs=[selected_tool, session_state],
                outputs=[selected_tool, session_state, *dialog.outputs()],
                api_name=False,
                show_progress="hidden",
            )

            def reveal_tools_folder(token: str | None, request: Any):
                """Open this owner's installed tools folder; no browser path is accepted."""
                maintenance.reveal("tool", token, request)

            reveal_tools.click(
                fn=bind(dialog.guard_result(reveal_tools_folder, 0)),
                inputs=[session_state],
                outputs=[*dialog.outputs()],
                api_name=False,
                show_progress="hidden",
            )

        validation_display = gr.Markdown(
            "### Tool validation\n\nNo validation started.", elem_id="validation-panel"
        )
        with gr.Accordion("Authorization & Test Review", open=True):
            auto_approve_check = gr.Checkbox(
                label="Auto-approve file writes for this session",
                value=False,
                info="If checked, file writes within generated_tools/ are authorized automatically.",
            )

            # Interactive Approval Panel with Editable Text Box
            with gr.Column(visible=False, elem_id="authorization-review") as approval_group:
                gr.Markdown("### Authorization & Review Required")
                pending_info = gr.Markdown("No pending approval requests.")
                preview_box = gr.TextArea(
                    label="Review and edit file content or acceptance cases before approving",
                    lines=APPROVAL_PREVIEW_LINES,
                    interactive=True,  # Enables manual editing
                )
                approval_validation = gr.Markdown(
                    "Waiting for proposal validation.", elem_id="approval-validation"
                )
                with gr.Row():
                    approve_btn = gr.Button(
                        "Approve Reviewed Content", variant="primary", interactive=False
                    )
                    reject_btn = gr.Button("Reject Operation", variant="stop")

    if repair_backend is not None:
        from agentix.ui.tool_repair import build_tool_repair

        build_tool_repair(gr, repair_backend, bind, session_state)

    auto_approve_check.change(
        fn=bind(dialog.guard_result(callbacks.toggle, 1)),
        inputs=[auto_approve_check, session_state],
        outputs=[session_state, *dialog.outputs()],
    )
    submit_btn.click(
        fn=bind(dialog.guard_result(callbacks.submit, SUBMIT_OUTPUT_COUNT)),
        inputs=[msg_input, session_state],
        outputs=[msg_input, chatbot, session_state, *dialog.outputs()],
        **operation,
    )
    msg_input.submit(
        fn=bind(dialog.guard_result(callbacks.submit, SUBMIT_OUTPUT_COUNT)),
        inputs=[msg_input, session_state],
        outputs=[msg_input, chatbot, session_state, *dialog.outputs()],
        **operation,
    )
    preview_box.input(
        fn=bind(dialog.guard_result(callbacks.approval_readiness, READINESS_OUTPUT_COUNT)),
        inputs=[preview_box, request_state, session_state],
        outputs=[approve_btn, approval_validation, *dialog.outputs()],
        show_progress="hidden",
    )
    approve_btn.click(
        fn=dialog.guard_result(bind(callbacks.approve, discard_result=True), 0),
        inputs=[preview_box, request_state, session_state],
        outputs=dialog.outputs(),
        **operation,
    )
    reject_btn.click(
        fn=dialog.guard_result(bind(callbacks.reject, discard_result=True), 0),
        inputs=[request_state, session_state],
        outputs=dialog.outputs(),
        **operation,
    )
    status_timer = gr.Timer(value=STATUS_TIMER_SECONDS)
    poll_event = status_timer.tick(
        fn=bind(dialog.guard_history(callbacks.poll, POLL_OUTPUT_COUNT, 0)),
        inputs=[session_state],
        outputs=[
            chatbot,
            approval_group,
            pending_info,
            preview_box,
            catalog_display,
            request_state,
            session_state,
            *dialog.outputs(),
        ],
        show_progress="hidden",
    )
    poll_event.then(
        fn=bind(dialog.guard_result(callbacks.approval_readiness, READINESS_OUTPUT_COUNT)),
        inputs=[preview_box, request_state, session_state],
        outputs=[approve_btn, approval_validation, *dialog.outputs()],
        show_progress="hidden",
    )
    status_timer.tick(
        fn=bind(dialog.guard_result(callbacks.validation_status, VALIDATION_OUTPUT_COUNT)),
        inputs=[session_state],
        outputs=[validation_display, *dialog.outputs()],
        show_progress="hidden",
    )
