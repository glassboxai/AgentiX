"""V4 composition root: common sidebar and separately implemented tab frontends."""

import functools
import inspect
from dataclasses import dataclass
from typing import Any

from agentix.controllers.activity import ActivityBackend
from agentix.controllers.applications import ApplicationsBackend
from agentix.controllers.catalog import CatalogMaintenanceBackend
from agentix.controllers.sessions import SessionRegistry
from agentix.controllers.sidebar import SidebarBackend
from agentix.controllers.tool_repair import ToolRepairBackend
from agentix.controllers.tools import ToolsBackend
from agentix.host_requirements import HostRequirements
from agentix.ui.applications import build_applications_frontend
from agentix.ui.branding import header, launch_options
from agentix.ui.sidebar import build_sidebar
from agentix.ui.theme import create_theme
from agentix.ui.tools import build_tools_frontend

SESSION_STATE_TTL_SECONDS = 1800  # Gradio drops an idle session state after this delay.
ACTIVITY_TIMER_SECONDS = 0.5  # Progress refresh cadence for running operations.


@dataclass(frozen=True)
class View:
    """Constructed Gradio Blocks and launch theme; owns no running server."""

    demo: Any
    theme: Any


def build_view(
    sessions: SessionRegistry, gradio_module: Any = None, *, applications_backend: Any = None
) -> View:
    """Compose one session-owned sidebar outside Tools and Applications tabs."""
    if gradio_module is None:
        import gradio as gradio_module
    gr = gradio_module
    callbacks = ToolsBackend(sessions)

    def bind(method: Any, *, discard_result: bool = False) -> Any:
        """Tell Gradio to inject Request instead of treating it as a user input."""

        @functools.wraps(method)
        def callback(*args: Any, **kwargs: Any) -> Any:
            """Dispatch only after the session callback checks token ownership."""
            result = method(*args, **kwargs)
            return None if discard_result else result

        if inspect.isgeneratorfunction(method):

            @functools.wraps(method)
            def streaming_callback(*args: Any, **kwargs: Any):
                """Preserve stage streaming while retaining framework Request injection."""
                yield from method(*args, **kwargs)

            callback = streaming_callback

        callback.__annotations__ = dict(method.__annotations__, request=gr.Request)
        signature = inspect.signature(method)
        callback.__signature__ = signature.replace(
            parameters=[
                parameter.replace(annotation=gr.Request)
                if parameter.name == "request"
                else parameter
                for parameter in signature.parameters.values()
            ]
        )
        owner = getattr(method, "__self__", None)
        if owner is None:
            owner = getattr(getattr(method, "__wrapped__", None), "__self__", None)
        if isinstance(owner, ApplicationsBackend):
            callback.__name__ = "application_" + method.__name__
        return callback

    theme = create_theme(gr)

    applications = (
        applications_backend
        if applications_backend is not None
        else ApplicationsBackend(sessions, host_requirements=HostRequirements())
    )
    maintenance = CatalogMaintenanceBackend(sessions, applications)
    repairs = ToolRepairBackend(sessions, applications)
    with gr.Blocks(title="AgentiX", fill_width=True) as demo:
        session_state = gr.State(
            value=None, time_to_live=SESSION_STATE_TTL_SECONDS, delete_callback=sessions.close_state
        )
        request_state = gr.Textbox(value="", visible=False, interactive=False)
        gr.HTML(header())
        progress = gr.HTML(value="", elem_id="agentix-operation-progress")
        from agentix.ui.message_dialog import MessageDialog

        dialog = MessageDialog(gr)
        gr.Timer(value=ACTIVITY_TIMER_SECONDS).tick(
            fn=bind(dialog.guard_result(ActivityBackend(sessions).activity_status, 1)),
            inputs=[session_state],
            outputs=[progress, *dialog.outputs()],
            api_name=False,
            show_progress="hidden",
        )
        build_sidebar(gr, demo, SidebarBackend(sessions), bind, session_state, progress, dialog)
        with gr.Tabs(elem_id="agentix-tabs"):
            with gr.Tab("Tools", elem_id="tools-tab"):
                build_tools_frontend(
                    gr,
                    callbacks,
                    bind,
                    session_state,
                    request_state,
                    progress,
                    maintenance,
                    repairs,
                    dialog,
                )
            with gr.Tab("Applications", elem_id="applications-tab"):
                build_applications_frontend(
                    gr, applications, bind, session_state, progress, maintenance, dialog
                )
    demo.unload(fn=bind(callbacks.unload))
    demo.unload(fn=bind(applications.unload))
    return View(demo, theme)


def launch(view: View, *, server_port: int = 7860, open_browser: bool = True) -> None:
    """Start the existing queued loopback UI and open the browser."""
    view.demo.queue().launch(
        server_name="127.0.0.1",
        server_port=server_port,
        theme=view.theme,
        inbrowser=open_browser,
        **launch_options(),
    )
