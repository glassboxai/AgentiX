"""Applications controls; owner-bound review and execution live in the backend."""

from typing import Any

from agentix.ui.apps_catalog_frontend import build_apps_catalog
from agentix.ui.result_components import ResultField, build_results, result_values


def _build_application_workspace(
    gr: Any, backend: Any, bind: Any, session_state: Any, progress: Any = None
) -> None:
    """Present approved catalog dependencies, readable review and the framed preview."""
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    gr.Markdown(
        "## Applications\nCreate a reviewed application using approved tools from Installed Tools Catalog. The current supported workflow combines word and vowel counts; missing or unapproved tools must be created and approved in Tools first."
    )
    application_name = gr.Textbox(label="Application name", elem_id="applications-name")
    query = gr.Textbox(
        label="Describe the application you need",
        lines=3,
        elem_id="applications-query",
        placeholder="I need an app where I can enter text and see its word and vowel counts.",
    )
    generate = gr.Button("Generate application", elem_id="applications-generate")
    status = gr.Markdown("No application has been generated.", elem_id="applications-status")
    identity = gr.Textbox(value="", visible=False, interactive=False)
    # Exact server snapshot is internal transport, never the user's review surface.
    review = gr.Textbox(value="", visible=False, interactive=False, elem_id="applications-review")
    with gr.Accordion(
        "Application source, proposed tests and acceptance review",
        open=False,
        elem_id="applications-review-panel",
    ):
        requirements = gr.Textbox(label="Original requirements", interactive=False, lines=3)
        files = gr.Dropdown(
            choices=[], label="Application files and proposed tests", elem_id="applications-files"
        )
        file_hint = gr.Markdown(
            "Select a file to inspect its source.", elem_id="applications-file-hint"
        )
        editor = gr.Code(
            label="Selected file",
            language="python",
            lines=22,
            interactive=True,
            elem_id="applications-file-editor",
        )
        with gr.Row(visible=False, elem_id="applications-tool-panes") as tool_panes:
            with gr.Column():
                code_pane = gr.Code(
                    label="Tool implementation â€” pending revision",
                    language="python",
                    lines=22,
                    interactive=True,
                    elem_id="applications-tool-code",
                )
            with gr.Column():
                widget_pane = gr.Code(
                    label="Tool widget",
                    language="python",
                    lines=22,
                    interactive=True,
                    elem_id="applications-widget-code",
                )
            with gr.Column():
                with gr.Tabs():
                    with gr.Tab("Tool tests"):
                        tool_tests_pane = gr.Code(
                            label="Tool tests â€” pending revision",
                            language="python",
                            lines=22,
                            interactive=True,
                            elem_id="applications-tool-tests",
                        )
                    with gr.Tab("Widget tests"):
                        widget_tests_pane = gr.Code(
                            label="Proposed widget tests",
                            language="python",
                            lines=22,
                            interactive=True,
                            elem_id="applications-widget-tests",
                        )
        save = gr.Button(
            "Save reviewed changes", interactive=False, elem_id="applications-save-file"
        )
        gr.Markdown(
            "Saving edited tool code/tests creates a pending revision; normal tool review and validation must succeed before application approval. Unchanged approved tools are reused without rerunning their unittest suites. Widget tests and application connections remain independently checked."
        )
        cases = gr.JSON(label="Independent acceptance cases", elem_id="applications-acceptance")
    reviewed = gr.Checkbox(
        label="I have reviewed the source, proposed tests and independent acceptance cases",
        value=False,
        elem_id="applications-reviewed",
    )
    with gr.Row():
        approve = gr.Button("Approve and verify", elem_id="applications-approve")
        reject = gr.Button("Reject proposal", elem_id="applications-reject")
    frame = gr.HTML(value="", elem_id="applications-frame")
    with gr.Accordion("Use the application as a composite tool", open=False):
        gr.Markdown(
            "A composite tool combines approved tools into one reusable data operation. This runs the reviewed operation without opening its interface; it does not yet publish it as an installed tool."
        )
        data_input = gr.Textbox(label="Text", elem_id="applications-data-input")
        run_data = gr.Button("Run data operation", elem_id="applications-data-run")
        fields = [
            ResultField("words", "Words", "number"),
            ResultField("vowels", "Vowels", "number"),
        ]
        with gr.Row(elem_id="applications-data-result"):
            data_outputs = build_results(gr, fields, "applications-data")
    outputs = [status, review, identity, frame, reviewed, session_state]
    generate.click(
        fn=bind(backend.generate_named),
        inputs=[application_name, query, session_state],
        outputs=outputs,
        api_name=False,
        **operation,
    )
    approve.click(
        fn=bind(backend.approve),
        inputs=[reviewed, identity, session_state],
        outputs=[status, frame, session_state],
        api_name=False,
        **operation,
    )
    reject.click(
        fn=bind(backend.stop),
        inputs=[session_state],
        outputs=[status, frame, session_state],
        api_name=False,
        **operation,
    )

    def run_typed_data(text: str, token: str | None, request: Any):
        """Present approved structured data as typed results, without generating a tool."""
        value, message, owned = backend.data(text, token, request)
        return (*result_values(value, fields), message, owned)

    run_data.click(
        fn=bind(run_typed_data),
        inputs=[data_input, session_state],
        outputs=[*data_outputs, status, session_state],
        api_name=False,
        **operation,
    )
    repair = gr.Button(
        "Propose repair after failed verification",
        visible=False,
        interactive=False,
        elem_id="applications-repair",
    )
    review_tools = gr.Button(
        "Review modified tool revisions", visible=False, elem_id="applications-review-tools"
    )
    review_tools.click(
        fn=bind(backend.review_tools),
        inputs=[session_state],
        outputs=outputs,
        api_name=False,
        **operation,
    )
    repair.click(
        fn=bind(backend.repair),
        inputs=[session_state],
        outputs=outputs,
        api_name=False,
        **operation,
    )

    def refresh_review(token: str | None, request: Any):
        """Reset to a readable composition file after generating/saving a revision."""
        entries, first, text, editable, hint, original, acceptance, owned = backend.review_files(
            token, request
        )
        return (
            gr.Dropdown(choices=entries, value=first),
            gr.Code(value=text, interactive=editable, visible=True),
            gr.Button(interactive=editable),
            hint,
            original,
            acceptance,
            gr.Row(visible=False),
            owned,
        )

    def select_file(name: str, token: str | None, request: Any):
        """Show a coherent triplet for any implementation/widget/tests selection."""
        if not name:
            return [gr.skip()] * 9 + [token]
        try:
            panes = backend.review_panes(name, token, request)
        except ValueError as error:
            if str(error) != "Select a tool implementation, widget or tests for the grouped view":
                # Ordinary non-tool files still use the single-file editor.
                if name.startswith("count_") or name.startswith("proposed_tests/"):
                    raise
            text, editable, hint, owned = backend.read_file(name, token, request)
            return (
                gr.Code(value=text, interactive=editable, visible=True),
                gr.Button(interactive=editable),
                hint,
                gr.Row(visible=False),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                gr.skip(),
                owned,
            )
        updates = (
            [gr.skip()] * 4
            if panes["retain_buffers"]
            else [
                gr.Code(value=panes[key], interactive=True)
                for key in ("code", "widget", "tool_tests", "widget_tests")
            ]
        )
        return (
            gr.Code(visible=False),
            gr.Button(interactive=True),
            "Edit the related files together. Tool implementation/test changes require a separate tool approval; no shared tool is overwritten by Save.",
            gr.Row(visible=True),
            *updates,
            gr.skip(),
            token,
        )

    def edited_file(name: str, token: str | None, request: Any):
        """Require explicit save rather than approving an older displayed snapshot."""
        hint = backend.mark_edited(name, token, request)
        return False, hint

    editor.input(
        fn=bind(edited_file),
        inputs=[files, session_state],
        outputs=[reviewed, file_hint],
        api_name=False,
        show_progress="hidden",
    )

    def edited_group(name: str, token: str | None, request: Any):
        """A change in any pane clears the old review checkbox."""
        return False, backend.mark_group_edited(name, token, request)

    for pane in (code_pane, widget_pane, tool_tests_pane, widget_tests_pane):
        pane.input(
            fn=bind(edited_group),
            inputs=[files, session_state],
            outputs=[reviewed, file_hint],
            api_name=False,
            show_progress="hidden",
        )

    review.change(
        fn=bind(refresh_review),
        inputs=[session_state],
        outputs=[files, editor, save, file_hint, requirements, cases, tool_panes, session_state],
        api_name=False,
        show_progress="hidden",
    )
    files.change(
        fn=bind(select_file),
        inputs=[files, session_state],
        outputs=[
            editor,
            save,
            file_hint,
            tool_panes,
            code_pane,
            widget_pane,
            tool_tests_pane,
            widget_tests_pane,
            reviewed,
            session_state,
        ],
        api_name=False,
        show_progress="hidden",
    )
    save.click(
        fn=bind(backend.save_review),
        inputs=[
            files,
            editor,
            code_pane,
            widget_pane,
            tool_tests_pane,
            widget_tests_pane,
            identity,
            session_state,
        ],
        outputs=outputs,
        api_name=False,
        **operation,
    )

    def poll_application(token: str | None, request: Any):
        """Update owned lifecycle and repair visibility without progress flicker."""
        message, content, owned = backend.poll(token, request)
        state = backend.review_state(owned, request)
        available = state["repair_available"]
        return (
            gr.skip() if message is None else message,
            gr.skip() if content is None else content,
            gr.Button(visible=available, interactive=available),
            gr.Button(
                visible=state.get("tool_revision_pending", False), interactive=not state["busy"]
            ),
            owned,
        )

    gr.Timer(value=1.0).tick(
        fn=bind(poll_application),
        inputs=[session_state],
        outputs=[status, frame, repair, review_tools, session_state],
        api_name=False,
        show_progress="hidden",
    )

    return {"status": status, "outputs": outputs}


def build_applications_frontend(
    gr: Any, backend: Any, bind: Any, session_state: Any, progress: Any = None
) -> None:
    """Compose full-width workspace and a separate right-hand installed-app catalog."""
    with gr.Row(elem_id="applications-workspace"):
        with gr.Column(scale=4, min_width=420):
            workspace = _build_application_workspace(gr, backend, bind, session_state, progress)
        with gr.Column(scale=1, min_width=240, elem_id="installed-apps-panel"):
            build_apps_catalog(gr, backend, bind, session_state, workspace, progress)
