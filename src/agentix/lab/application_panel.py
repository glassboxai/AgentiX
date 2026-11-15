"""Reviewed composite application's native lifecycle and optional Lab iframe controls."""

import json
import logging
import threading
from collections.abc import Iterator
from pathlib import Path

from agentix.lab.application_artifacts import ApprovedApplication, approve_application
from agentix.lab.application_session import ApplicationSession
from agentix.lab.widget_panel import NativePreview, WidgetPanel, iframe_html

logger = logging.getLogger(__name__)
REVIEW_PATH = Path(__file__).resolve().parents[3] / "infra/application-review.json"


def reviewed_application() -> ApprovedApplication:
    """Read host-owned activation only; changes fail before any application import."""
    record = json.loads(REVIEW_PATH.read_text(encoding="utf-8"))
    if (
        set(record) != {"package", "reviewedDigest", "verifiedDigest"}
        or record["reviewedDigest"] != record["verifiedDigest"]
    ):
        raise ValueError("Application has not been independently verified")
    return approve_application(Path(record["package"]), record["reviewedDigest"])


class ApplicationPreview(NativePreview[ApprovedApplication]):
    """One composite worker with direct internal calls and the existing restricted bridge."""

    def __init__(
        self,
        approved: ApprovedApplication,
        parent_origin: str | None,
        *,
        port: int = 0,
        lifetime: int | None = None,
        display_name: str = "",
    ) -> None:
        """Bind explicit unprivileged port, bounded lifetime and display name before startup."""
        if not isinstance(approved, ApprovedApplication):
            raise ValueError("Reviewed application required")
        if type(port) is not int or (port != 0 and not 1024 <= port <= 65535):
            raise ValueError("Invalid application port")
        if lifetime is not None and (type(lifetime) is not int or not 1 <= lifetime <= 300):
            raise ValueError("Application lifetime must be 1 to 300 seconds")
        if type(display_name) is not str or len(display_name) > 120:
            raise ValueError("Invalid application display name")
        self.lifetime = lifetime
        self.display_name = display_name
        super().__init__(approved, parent_origin, port=port)
        self.lifecycle_lock = threading.Lock()
        self.configure_layout(None, None)

    def configure_layout(self, library, identity, check=None) -> None:
        """Attach only maintained routes bound to this protected app and preview."""
        from agentix.application.app_controls import ApplicationControls

        self.bridge.controls = ApplicationControls(
            self,
            library=library,
            identity=identity,
            check=check,
            root=lambda: self.session.root,
        )

    def cancel_execution(self) -> None:
        """Cancel this complete native worker while retaining its private stopped page."""
        with self.lifecycle_lock:
            self.paused = True
            self.session.close()

    def restart_execution(self) -> None:
        """Recreate only the same immutable native snapshot; never execute in the host."""
        with self.lifecycle_lock:
            if not self.paused or self.stop.is_set():
                raise ValueError("Application is not stopped")
            session = self._create_session(self.approved)
            try:
                session.__enter__()
            except BaseException:
                session.close()
                raise
            if self.stop.is_set():
                session.close()
                raise ValueError("Application was closed during restart")
            self.session = self.bridge.session = session
            self.paused = False
            if self.stop.is_set():
                session.cancel.set()

    def request_close(self) -> None:
        """Signal owned shutdown without joining the HTTP thread from its request."""
        self.stop.set()
        self.session.cancel.set()
        self.server.should_exit = True

    def _create_session(self, approved: ApprovedApplication) -> ApplicationSession:
        """Create an application worker; never silently substitute a host process."""
        return ApplicationSession(approved, lifetime=self.lifetime, display_name=self.display_name)


class ApplicationPanel(WidgetPanel[ApprovedApplication]):
    """Reuse owner reservations/cleanup with a separate application capability factory."""

    def __init__(self) -> None:
        """Keep the application independent of the legacy widget panel and its sessions."""
        super().__init__(reviewed_application, ApplicationPreview)

    def status(self, owner: str) -> str:
        """Expose lifecycle only, with no source, review identity or filesystem details."""
        return (
            super()
            .status(owner)
            .replace(
                "Ready. The isolated session lasts up to five minutes; reopen it when it expires.",
                "Ready. Stop application when finished.",
            )
            .replace("widget", "application")
            .replace("count_vowels_in_text", "text analysis")
        )


def open_application(panel: WidgetPanel, owner: str, origin: str) -> Iterator[tuple[str, str]]:
    """Clear the prior frame and publish a reviewed native application after readiness."""
    yield ("Preparing the isolated application. This may take about a minute.", "")
    try:
        preview = panel.open(owner, origin)
        yield (
            panel.status(owner),
            iframe_html(preview.url).replace(
                'title="count_vowels_in_text"', 'title="Text analysis application"'
            ),
        )
    except Exception as error:
        logger.error("event=application_open_failed error_type=%s", type(error).__name__)
        yield ("Application unavailable. Check its reviewed package and local diagnostics.", "")


def build_application_panel(panel: WidgetPanel, origin: str) -> None:
    """Register stable Gradio controls; no server or native process starts during rendering."""
    import gradio as gr

    with gr.Accordion("Composite application: text analysis", open=True):
        gr.Markdown(
            "One isolated application, two directly connected tools. It can also run independently."
        )
        with gr.Row():
            start = gr.Button("Open application", elem_id="lab_application_open")
            stop = gr.Button("Close application", elem_id="lab_application_close")
        status = gr.Textbox(
            label="Application status",
            interactive=False,
            value="Closed. Open application to begin.",
            elem_id="lab_application_status",
        )
        frame = gr.HTML(elem_id="lab_application_frame")
        timer = gr.Timer(2)

        def opened(request: gr.Request):
            """Route the requesting browser to its own application instance."""
            yield from open_application(panel, request.session_hash, origin)

        def closed(request: gr.Request):
            """Cancel only the requesting browser's application and clear its iframe."""
            panel.close(request.session_hash)
            return panel.status(request.session_hash), ""

        def state(request: gr.Request):
            """Update status without replacing the live iframe and its user input."""
            return panel.status(request.session_hash)

        start.click(
            opened, outputs=[status, frame], concurrency_limit=2, concurrency_id="application-open"
        )
        stop.click(
            closed, outputs=[status, frame], concurrency_limit=4, concurrency_id="application-close"
        )
        timer.tick(state, outputs=status, queue=False, show_progress="hidden")
