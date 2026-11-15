"""Installed Apps Catalog controls; discovery/execution remain owner-bound backend work."""

from typing import Any

STARTUP_TIMER_SECONDS = 1.0  # One-shot page-load catalog population.
CATALOG_OUTPUT_COUNT = 3
STARTUP_OUTPUT_COUNT = 4
NO_SELECTION = "Select a verified saved application."


def require_selected_app(selected: str) -> None:
    """Reject catalog actions before any backend call when nothing is selected."""
    if not selected:
        raise ValueError("Please, select an installed application.")


def catalog_view(backend: Any, gr: Any, selected: str, token: str | None, request: Any) -> tuple:
    """Rebuild dropdown choices and description from one protected listing.

    Both outputs come from the same read so a successful re-approval or
    re-verification drops the stale label and its guidance in one refresh.
    """
    choices, owned = backend.catalog_entries(token, request)
    ids = {identity for _, identity in choices}
    value = selected if selected in ids else None
    description = backend.describe_app(value, token, request) if value else NO_SELECTION
    return gr.Dropdown(choices=choices, value=value), description, owned


def build_apps_catalog(
    gr: Any,
    backend: Any,
    bind: Any,
    session_state: Any,
    workspace: dict,
    progress: Any,
    maintenance: Any = None,
) -> None:
    """Render one right-side durable catalog with explicit load/play actions."""
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    dialog = workspace.get("dialog")
    if dialog is None:
        from agentix.ui.message_dialog import MessageDialog

        dialog = MessageDialog(gr)
    with gr.Row():
        gr.Markdown("### Installed Apps Catalog")
        if maintenance is not None:
            reveal_apps = gr.Button("View in explorer", elem_id="apps-reveal", scale=0, size="sm")
    choice = gr.Dropdown(choices=[], label="Installed applications", elem_id="installed-apps")
    description = gr.Markdown(
        "Select a verified saved application.", elem_id="installed-app-description"
    )
    refresh = gr.Button("Refresh apps", elem_id="installed-apps-refresh")
    with gr.Row():
        load = gr.Button("Load selected app", elem_id="installed-apps-load")
        play = gr.Button("Play selected app", elem_id="installed-apps-play")
        reverify = gr.Button("Re-verify selected app", elem_id="installed-apps-reverify")

    if maintenance is not None:
        from agentix.ui.catalog_actions import build_delete_controls

        build_delete_controls(
            gr,
            maintenance,
            bind,
            "application",
            choice,
            session_state,
            workspace["status"],
            dialog=dialog,
        )

        def reveal_apps_folder(token: str | None, request: Any):
            """Open this owner's installed applications folder; no browser path is accepted."""
            maintenance.reveal("application", token, request)

        reveal_apps.click(
            fn=bind(dialog.guard_result(reveal_apps_folder, 0)),
            inputs=[session_state],
            outputs=[*dialog.outputs()],
            api_name=False,
            show_progress="hidden",
        )

    from agentix.ui.application_candidates import build_candidate_panel

    build_candidate_panel(gr, backend, bind, session_state, workspace, progress)

    def refresh_apps(selected: str, token: str | None, request: Any):
        """Preserve selection while refreshing protected metadata and its description."""
        return catalog_view(backend, gr, selected, token, request)

    def describe_app(selected: str, token: str | None, request: Any):
        """Show escaped metadata only for an exact catalog selection."""
        return backend.describe_app(selected, token, request) if selected else NO_SELECTION

    refresh.click(
        fn=bind(dialog.guard_result(refresh_apps, CATALOG_OUTPUT_COUNT)),
        inputs=[choice, session_state],
        outputs=[choice, description, session_state, *dialog.outputs()],
        api_name=False,
        **operation,
    )
    workspace["status"].change(
        fn=bind(dialog.guard_result(refresh_apps, CATALOG_OUTPUT_COUNT)),
        inputs=[choice, session_state],
        outputs=[choice, description, session_state, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )
    choice.change(
        fn=bind(dialog.guard_result(describe_app, 1)),
        inputs=[choice, session_state],
        outputs=[description, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )

    def load_selected(selected: str, token: str | None, request: Any):
        """Require an explicit catalog selection before streaming the load."""
        require_selected_app(selected)
        yield from backend.load_app(selected, token, request)

    def play_selected(selected: str, token: str | None, request: Any):
        """Require an explicit catalog selection before streaming the launch."""
        require_selected_app(selected)
        yield from backend.open_app(selected, token, request)

    def reverify_selected(selected: str, token: str | None, request: Any):
        """Require an explicit catalog selection before repeating independent gates."""
        require_selected_app(selected)
        yield from backend.reverify_app(selected, token, request)

    load.click(
        fn=bind(dialog.wrap_stream_final(load_selected, 6)),
        inputs=[choice, session_state],
        outputs=workspace["outputs"] + dialog.outputs(),
        api_name=False,
        **operation,
    )
    play.click(
        fn=bind(dialog.wrap_stream_final(play_selected, 6)),
        inputs=[choice, session_state],
        outputs=workspace["outputs"] + dialog.outputs(),
        api_name=False,
        **operation,
    )
    reverify.click(
        fn=bind(dialog.wrap_stream_final(reverify_selected, 6)),
        inputs=[choice, session_state],
        outputs=workspace["outputs"] + dialog.outputs(),
        api_name=False,
        **operation,
    )
    startup = gr.Timer(value=STARTUP_TIMER_SECONDS)

    def initial_catalog(selected: str, token: str | None, request: Any):
        """Populate once on page load, without continuous artifact polling."""
        update, description_text, owned = refresh_apps(selected, token, request)
        return update, description_text, owned, gr.Timer(active=False)

    startup.tick(
        fn=bind(dialog.guard_result(initial_catalog, STARTUP_OUTPUT_COUNT)),
        inputs=[choice, session_state],
        outputs=[choice, description, session_state, startup, *dialog.outputs()],
        api_name=False,
        show_progress="hidden",
    )
