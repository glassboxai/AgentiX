"""Applications controls; owner-bound review and execution live in the backend."""

import re
from typing import Any

from agentix.ui.application_presentation import named_result_rows
from agentix.ui.apps_catalog import build_apps_catalog
from agentix.ui.result_components import ResultField, build_results, result_values

APPLICATION_POLL_SECONDS = 1.0  # Lifecycle refresh without progress flicker.
QUERY_INPUT_LINES = 3
REQUIREMENTS_INPUT_LINES = 3
SOURCE_EDITOR_LINES = 22
WORKSPACE_COLUMN_SCALE = 1
WORKSPACE_COLUMN_MIN_WIDTH = 420
APPLICATIONS_SIDEBAR_WIDTH_PIXELS = 380
REVIEW_OUTPUT_COUNT = 10
SELECTION_OUTPUT_COUNT = 10
POLL_OUTPUT_COUNT = 7
WIDGET_TOOL_NAME = re.compile(r"[a-z][a-z0-9_]{0,63}")


def widget_source_name(tool: str) -> str:
    """Resolve a double-clicked widget tool to its reviewed widget source filename.

    Only a canonical tool identifier is accepted, so browser text never becomes a path.
    """
    if not isinstance(tool, str) or not WIDGET_TOOL_NAME.fullmatch(tool):
        raise ValueError("Select a widget from the generated application")
    return tool + "_widget.py"


def _build_application_workspace(
    gr: Any, backend: Any, bind: Any, session_state: Any, progress: Any = None, dialog: Any = None
) -> None:
    """Present approved catalog dependencies, readable review and the framed preview."""
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    gr.Markdown(
        "## Applications\nCreate a reviewed application using approved tools from Installed Tools Catalog. The workflow is planned from approved canonical tool contracts; missing or unapproved tools must be created and approved in Tools first."
    )
    application_name = gr.Textbox(label="Application name", elem_id="applications-name")
    query = gr.Textbox(
        label="Describe the application you need",
        lines=QUERY_INPUT_LINES,
        elem_id="applications-query",
        placeholder="Describe the tools, inputs and results you want in your application.",
    )
    generate = gr.Button("Generate application", elem_id="applications-generate")
    status = gr.Markdown("No application has been generated.", elem_id="applications-status")
    from agentix.controllers.widget_style import WidgetStyleBackend
    from agentix.ui.widget_style_dialog import WidgetStyleDialog

    # The overlay lives at column level so a collapsed review panel cannot hide it.
    WidgetStyleDialog(gr, WidgetStyleBackend(backend), bind, session_state)
    from agentix.ui.message_dialog import MessageDialog

    if dialog is None:
        dialog = MessageDialog(gr)
    identity = gr.Textbox(value="", visible=False, interactive=False)
    # Exact server snapshot is internal transport, never the user's review surface.
    review = gr.Textbox(value="", visible=False, interactive=False, elem_id="applications-review")
    with gr.Accordion(
        "Application source, proposed tests and acceptance review",
        open=False,
        elem_id="applications-review-panel",
    ) as review_panel:
        requirements = gr.Textbox(
            label="Original requirements", interactive=False, lines=REQUIREMENTS_INPUT_LINES
        )
        files = gr.Dropdown(
            choices=[], label="Application files and proposed tests", elem_id="applications-files"
        )
        widget_selection = gr.Textbox(
            value="",
            elem_classes=["agentix-internal-input"],
            elem_id="applications-widget-selection",
        )
        widget_select = gr.Button(
            "Select widget source",
            elem_classes=["agentix-internal-input"],
            elem_id="applications-widget-select",
        )
        file_hint = gr.Markdown(
            "Select a file to inspect its source.", elem_id="applications-file-hint"
        )
        editor = gr.Code(
            label="Selected file",
            language="python",
            lines=SOURCE_EDITOR_LINES,
            interactive=True,
            elem_id="applications-file-editor",
        )
        with gr.Row(visible=False, elem_id="applications-tool-panes") as tool_panes:
            with gr.Column():
                code_pane = gr.Code(
                    label="Tool implementation — pending revision",
                    language="python",
                    lines=SOURCE_EDITOR_LINES,
                    interactive=True,
                    elem_id="applications-tool-code",
                )
            with gr.Column():
                widget_pane = gr.Code(
                    label="Tool widget",
                    language="python",
                    lines=SOURCE_EDITOR_LINES,
                    interactive=True,
                    elem_id="applications-widget-code",
                )
            with gr.Column():
                with gr.Tabs():
                    with gr.Tab("Tool tests"):
                        tool_tests_pane = gr.Code(
                            label="Tool tests — pending revision",
                            language="python",
                            lines=SOURCE_EDITOR_LINES,
                            interactive=True,
                            elem_id="applications-tool-tests",
                        )
                    with gr.Tab("Widget tests"):
                        widget_tests_pane = gr.Code(
                            label="Proposed widget tests",
                            language="python",
                            lines=SOURCE_EDITOR_LINES,
                            interactive=True,
                            elem_id="applications-widget-tests",
                        )
        save = gr.Button(
            "Save reviewed changes", interactive=False, elem_id="applications-save-file"
        )
        gr.Markdown(
            "Saving edited tool code/tests creates a pending revision; normal tool review and validation must succeed before application approval. Unchanged approved tools are reused without rerunning their unittest suites. Widget tests and application connections remain independently checked."
        )
        cases = gr.JSON(
            label="Saved independent acceptance cases", elem_id="applications-acceptance"
        )
    from agentix.ui.chathelper import build_chathelper

    build_chathelper(
        gr,
        backend,
        bind,
        files,
        session_state,
        [code_pane, widget_pane, tool_tests_pane, widget_tests_pane],
    )
    reviewed = gr.Checkbox(
        label="I have reviewed the source, proposed tests and independent acceptance cases",
        value=False,
        elem_id="applications-reviewed",
    )
    acceptance_notice = gr.Markdown(
        "Review and save independent acceptance cases before approval.",
        elem_id="applications-acceptance-notice",
    )
    with gr.Row():
        approve = gr.Button("Approve and verify", elem_id="applications-approve")
        reject = gr.Button("Reject proposal", elem_id="applications-reject")
    host_requirement = gr.Markdown("", visible=False, elem_id="applications-host-requirement")
    install_host_requirement = gr.Button(
        "Install required host dependency",
        visible=False,
        interactive=False,
        elem_id="applications-install-host-dependency",
    )
    frame = gr.HTML(value="", elem_id="applications-frame")
    with gr.Accordion("Use the application as a composite tool", open=False):
        gr.Markdown(
            "A composite tool combines approved tools into one reusable data operation. This runs the reviewed operation without opening its interface; it does not yet publish it as an installed tool."
        )
        data_input = gr.Textbox(
            label="Text for legacy apps; named input values (JSON) for catalog apps",
            elem_id="applications-data-input",
        )
        data_contract = gr.Markdown(
            "Load and verify an application to see its data-operation input schema.",
            elem_id="applications-data-contract",
        )
        with gr.Row():
            run_data = gr.Button("Run data operation", elem_id="applications-data-run")
            show_contract = gr.Button("Show input schema", elem_id="applications-data-schema")
        fields = [
            ResultField("words", "Words", "number"),
            ResultField("vowels", "Vowels", "number"),
        ]
        with gr.Row(elem_id="applications-data-result", visible=False) as legacy_data_result:
            data_outputs = build_results(gr, fields, "applications-data")
        general_data_result = gr.HTML(
            value="", visible=False, elem_id="applications-general-data-result"
        )
        general_data_table = gr.Dataframe(
            label="Named results",
            headers=["Result", "Type", "Value"],
            datatype=["str", "str", "str"],
            interactive=False,
            visible=False,
            elem_id="applications-data-table",
        )
    outputs = [status, review, identity, frame, reviewed, session_state]
    approve.click(
        fn=bind(dialog.wrap_stream_final(backend.approve, 3)),
        inputs=[reviewed, identity, session_state],
        outputs=[status, frame, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )
    reject.click(
        fn=bind(dialog.wrap_result(backend.stop, 3)),
        inputs=[session_state],
        outputs=[status, frame, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )
    install_host_requirement.click(
        fn=bind(dialog.wrap_result(backend.install_host_requirement, 2)),
        inputs=[session_state],
        outputs=[status, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )

    def run_typed_data(text: str, token: str | None, request: Any):
        """Present approved structured data as typed results, without generating a tool."""
        contract, _ = backend.data_contract(token, request)
        value, message, owned = backend.data(text, token, request)
        from agentix.ui.presentation import format_result

        generic = value is not None and set(value) != {"words", "vowels"}
        rendered = (
            format_result("Host-observed execution: application\nResult: " + repr(value))
            if generic
            else ""
        )
        return (
            *result_values(value if not generic else None, fields),
            gr.update(visible=value is not None and not generic),
            gr.update(value=rendered, visible=generic),
            gr.update(
                value=named_result_rows(value) if generic else {"headers": [], "data": []},
                visible=generic,
            ),
            contract,
            message,
            owned,
        )

    run_data.click(
        fn=bind(dialog.wrap_result(run_typed_data, 8, status_index=6)),
        inputs=[data_input, session_state],
        outputs=[
            *data_outputs,
            legacy_data_result,
            general_data_result,
            general_data_table,
            data_contract,
            status,
            session_state,
            *dialog.outputs(),
        ],
        api_name=False,
        **operation,
    )

    def show_data_contract(token: str | None, request: Any):
        """Show the loaded application's declared inputs without executing it."""
        return backend.data_contract(token, request)

    show_contract.click(
        fn=bind(dialog.guard_result(show_data_contract, 2)),
        inputs=[session_state],
        outputs=[data_contract, session_state, *dialog.outputs()],
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
        fn=bind(dialog.wrap_stream(backend.review_tools, 6)),
        inputs=[session_state],
        outputs=outputs + dialog.outputs(),
        api_name=False,
        **operation,
    )
    repair.click(
        fn=bind(dialog.wrap_stream(backend.repair, 6)),
        inputs=[session_state],
        outputs=outputs + dialog.outputs(),
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
            gr.Code(
                value=text,
                language="css"
                if (first or "").endswith(".css")
                else "json"
                if (first or "").endswith(".json")
                else "python",
                interactive=editable,
                visible=True,
            ),
            gr.Button(interactive=editable),
            hint,
            original,
            acceptance,
            gr.Row(visible=False),
            owned,
            hint,
            gr.Accordion(open=True),
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
                gr.Code(
                    value=text,
                    language="css"
                    if name.endswith(".css")
                    else "json"
                    if name.endswith(".json")
                    else "python",
                    interactive=editable,
                    visible=True,
                ),
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

    def select_widget_file(tool: str, token: str | None, request: Any):
        """Open <tool>_widget.py and its three panes for a double-clicked widget."""
        name = widget_source_name(tool)
        return (
            gr.Dropdown(value=name),
            gr.Accordion(open=True),
            *select_file(name, token, request),
        )

    def edited_file(name: str, token: str | None, request: Any):
        """Require explicit save rather than approving an older displayed snapshot."""
        hint = backend.mark_edited(name, token, request)
        return False, hint

    editor.input(
        fn=bind(dialog.guard_result(edited_file, 2)),
        inputs=[files, session_state],
        outputs=[reviewed, file_hint, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )

    def edited_group(name: str, token: str | None, request: Any):
        """A change in any pane clears the old review checkbox."""
        return False, backend.mark_group_edited(name, token, request)

    for pane in (code_pane, widget_pane, tool_tests_pane, widget_tests_pane):
        pane.input(
            fn=bind(dialog.guard_result(edited_group, 2)),
            inputs=[files, session_state],
            outputs=[reviewed, file_hint, *dialog.outputs()],
            api_name=False,
            show_progress="hidden",
        )

    review.change(
        fn=bind(dialog.guard_result(refresh_review, REVIEW_OUTPUT_COUNT)),
        inputs=[session_state],
        outputs=[
            files,
            editor,
            save,
            file_hint,
            requirements,
            cases,
            tool_panes,
            session_state,
            acceptance_notice,
            review_panel,
            *dialog.outputs(),
        ],
        api_name=False,
        show_progress="hidden",
    )
    files.change(
        fn=bind(dialog.guard_result(select_file, SELECTION_OUTPUT_COUNT)),
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
            *dialog.outputs(),
        ],
        api_name=False,
        show_progress="hidden",
    )
    widget_select.click(
        fn=bind(dialog.guard_result(select_widget_file, 12)),
        inputs=[widget_selection, session_state],
        outputs=[
            files,
            review_panel,
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
            *dialog.outputs(),
        ],
        api_name=False,
        show_progress="hidden",
    )
    save.click(
        fn=bind(dialog.wrap_result(backend.save_review, 6)),
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
        outputs=outputs + dialog.outputs(),
        api_name=False,
        **operation,
    )

    def poll_application(token: str | None, request: Any):
        """Update owned lifecycle and repair visibility without progress flicker."""
        message, content, owned = backend.poll(token, request)
        state = backend.review_state(owned, request)
        available = state["repair_available"]
        host_dependency_available = (
            state.get("host_dependency_pending", False) and not state["busy"]
        )
        return (
            gr.skip() if message is None else message,
            gr.skip() if content is None else content,
            gr.Button(visible=available, interactive=available),
            gr.Button(
                visible=state.get("tool_revision_pending", False), interactive=not state["busy"]
            ),
            gr.Markdown(
                value=state.get("host_dependency_message", ""),
                visible=host_dependency_available,
            ),
            gr.Button(visible=host_dependency_available, interactive=host_dependency_available),
            owned,
        )

    gr.Timer(value=APPLICATION_POLL_SECONDS).tick(
        fn=bind(dialog.guard_result(poll_application, POLL_OUTPUT_COUNT)),
        inputs=[session_state],
        outputs=[
            status,
            frame,
            repair,
            review_tools,
            host_requirement,
            install_host_requirement,
            session_state,
            *dialog.outputs(),
        ],
        api_name=False,
        show_progress="hidden",
    )

    return {
        "status": status,
        "outputs": outputs,
        "dialog": dialog,
        "query": query,
        "name": application_name,
        "generate": generate,
    }


def build_applications_frontend(
    gr: Any,
    backend: Any,
    bind: Any,
    session_state: Any,
    progress: Any = None,
    maintenance: Any = None,
    dialog: Any = None,
) -> None:
    """Compose a full-width workspace and one collapsible right sidebar for the catalog."""
    with gr.Row(elem_id="applications-workspace"):
        with gr.Column(scale=WORKSPACE_COLUMN_SCALE, min_width=WORKSPACE_COLUMN_MIN_WIDTH):
            workspace = _build_application_workspace(
                gr, backend, bind, session_state, progress, dialog
            )
    with gr.Sidebar(
        label="Applications panel",
        position="right",
        open=False,
        width=APPLICATIONS_SIDEBAR_WIDTH_PIXELS,
        elem_id="applications-sidebar",
    ):
        build_apps_catalog(
            gr,
            backend,
            bind,
            session_state,
            workspace,
            progress,
            maintenance,
        )
