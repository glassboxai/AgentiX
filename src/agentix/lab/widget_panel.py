"""Owner-scoped lifecycle of approved native widgets embedded in an application view.

Only server-owned review configuration supplies package paths and identities. Browser
callbacks select no files or capabilities. Native Gradio stays on a different origin;
its iframe may be embedded only by the explicit parent Lab origin.
"""

import atexit
import html
import json
import logging
import re
import socket
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generic, Protocol, TypeVar

from agentix.lab.widget_artifacts import ApprovedWidget, approve_package
from agentix.lab.widget_bridge import WidgetBridge
from agentix.lab.widget_identity import TOOL_NAME
from agentix.lab.widget_session import WidgetSession

Capability = TypeVar("Capability")

logger = logging.getLogger(__name__)


class Preview(Protocol):
    """Opaque owned native worker and listener; no generated module references."""

    url: str

    @property
    def alive(self) -> bool:
        """Whether the owned worker can still answer requests."""
        ...

    def close(self) -> None:
        """Stop only the owned listener/job and release temporary resources."""
        ...


def iframe_html(url: str) -> str:
    """Render only a supervisor-created loopback address inside a restricted iframe."""
    match = re.fullmatch(r"http://127\.0\.0\.1:([0-9]{4,5})/", url)
    if match is None or not 1024 <= int(match[1]) <= 65535:
        raise ValueError("Invalid widget iframe URL")
    return f'<iframe title="{TOOL_NAME}" src="{html.escape(url, quote=True)}" sandbox="allow-scripts allow-same-origin" referrerpolicy="no-referrer" class="agentix-application-frame"></iframe>'


def reviewed_widget() -> ApprovedWidget:
    """Load the explicitly activated host-owned review; never trust child test reports."""
    configuration = Path(__file__).resolve().parents[3] / "infra" / "widget-review.json"
    record = json.loads(configuration.read_text(encoding="utf-8-sig"))
    if (
        set(record) != {"package", "reviewedDigest", "verifiedDigest"}
        or record["verifiedDigest"] != record["reviewedDigest"]
        or not isinstance(record["package"], str)
    ):
        raise ValueError("Widget package has not been independently verified")
    package = Path(record["package"])
    if (
        not package.is_absolute()
        or package.drive.startswith("\\\\")
        or any(part.lower() == "generated_tools" for part in package.parts)
    ):
        raise ValueError("Invalid experimental widget package")
    return approve_package(package, record["reviewedDigest"])


class NativePreview(Generic[Capability]):
    """One finite native ASGI worker behind an explicitly bound private origin."""

    def __init__(self, approved: Capability, parent_origin: str | None, *, port: int = 0) -> None:
        """Start only reviewed bytes; clean up all partial native/listener failures."""
        import uvicorn

        self.approved = approved
        self.paused = False
        self.stop = threading.Event()
        self.listener = socket.socket()
        try:
            self.listener.bind(("127.0.0.1", port))
        except BaseException:
            self.listener.close()
            raise
        self.listener.listen(128)
        self.port = self.listener.getsockname()[1]
        self.url = f"http://127.0.0.1:{self.port}/"
        self.session = self._create_session(approved)
        try:
            self.session.__enter__()
            self.bridge = WidgetBridge(self.session, self.port, parent_origin=parent_origin)
            self.server = uvicorn.Server(
                uvicorn.Config(
                    self.bridge,
                    host="127.0.0.1",
                    port=self.port,
                    lifespan="off",
                    log_level="warning",
                    timeout_graceful_shutdown=2,
                )
            )
            self.thread = threading.Thread(target=self._serve, daemon=True)
            self.thread.start()
            self.monitor = threading.Thread(target=self._monitor, daemon=True)
            self.monitor.start()
            deadline = time.monotonic() + 10
            while self.thread.is_alive() and time.monotonic() < deadline:
                if self.server.started:
                    self.session.timings["listener_ready"] = (
                        time.monotonic() - self.session.start_time
                    )
                    return
                time.sleep(0.02)
            raise RuntimeError("Widget listener did not start")
        except BaseException:
            self.close()
            raise

    def _create_session(self, approved: Capability) -> WidgetSession:
        """Create the legacy gateway widget session; specialized applications use their snapshot."""
        if not isinstance(approved, ApprovedWidget):
            raise ValueError("Reviewed widget required")
        return WidgetSession(approved, lifetime=300)

    @property
    def alive(self) -> bool:
        """Report real worker/channel state rather than the existence of an old URL."""
        return (
            not self.stop.is_set()
            and self.thread.is_alive()
            and (
                self.paused
                or (self.session.native_thread.is_alive() and not self.session.cancel.is_set())
            )
        )

    def _serve(self) -> None:
        """Own listener lifecycle; worker cleanup runs even after HTTP errors."""
        try:
            self.server.run(sockets=[self.listener])
        finally:
            self.stop.set()
            self.session.close()
            self.listener.close()

    def _monitor(self) -> None:
        """Expire this listener when its isolated worker ends; no unrelated process work."""
        while not self.stop.wait(0.2):
            if not self.paused and (
                not self.session.native_thread.is_alive() or self.session.cancel.is_set()
            ):
                break
        self.server.should_exit = True

    def close(self) -> None:
        """Cancel the owned job and wait a bounded interval for owned cleanup."""
        self.stop.set()
        self.session.cancel.set()
        if hasattr(self, "server"):
            self.server.should_exit = True
        if hasattr(self, "thread") and self.thread.ident is not None:
            self.thread.join(40)
            if self.thread.is_alive():
                raise RuntimeError("Widget cleanup is still in progress")
        else:
            self.session.close()
            self.listener.close()


@dataclass
class _Slot:
    """Reserved owner capacity, including an in-flight native startup."""

    cancelled: threading.Event = field(default_factory=threading.Event)
    preview: Preview | None = None


class WidgetPanel(Generic[Capability]):
    """Bound native previews per browser owner; callbacks never accept package paths."""

    def __init__(
        self,
        review: Callable[[], Capability] = reviewed_widget,
        start: Callable[[Capability, str], Preview] = NativePreview,
        *,
        capacity: int = 2,
    ) -> None:
        """Inject review authority and process boundary; construct without IO or servers."""
        if type(capacity) is not int or not 1 <= capacity <= 4:
            raise ValueError("Invalid preview capacity")
        self.review, self.start, self.capacity = review, start, capacity
        self.slots: dict[str, _Slot] = {}
        self.lock = threading.Lock()
        atexit.register(self.close_all)

    def open(self, owner: str, parent_origin: str) -> Preview:
        """Reuse only the owner's live snapshot; reap expired owners before reserving capacity."""
        if not owner or len(owner) > 256:
            raise ValueError("Missing browser owner")
        expired, reusable, slot = [], None, None
        with self.lock:
            for identity, previous in list(self.slots.items()):
                if previous.preview is not None and not previous.preview.alive:
                    expired.append(previous.preview)
                    self.slots.pop(identity)
            existing = self.slots.get(owner)
            if existing:
                if existing.preview is None or existing.cancelled.is_set():
                    raise RuntimeError("Widget startup or shutdown is already in progress")
                reusable = existing.preview
            else:
                if len(self.slots) >= self.capacity:
                    raise RuntimeError("Two widget previews are already active; close one first")
                slot = _Slot()
                self.slots[owner] = slot
        preview = None
        try:
            for previous in expired:
                previous.close()
            if reusable is not None:
                return reusable
            approved = self.review()
            if slot.cancelled.is_set():
                raise RuntimeError("Widget opening was cancelled")
            preview = self.start(approved, parent_origin)
            with self.lock:
                if slot.cancelled.is_set():
                    raise RuntimeError("Widget opening was cancelled")
                slot.preview = preview
            logger.info("event=widget_panel_opened")
            return preview
        except BaseException:
            if preview:
                preview.close()
            with self.lock:
                if slot is not None and self.slots.get(owner) is slot:
                    self.slots.pop(owner)
            raise

    def close(self, owner: str) -> None:
        """Cancel only the requesting owner's live or pending preview."""
        with self.lock:
            slot = self.slots.get(owner)
            if slot is None:
                return
            slot.cancelled.set()
            preview = slot.preview
        if preview:
            preview.close()
            with self.lock:
                if self.slots.get(owner) is slot:
                    self.slots.pop(owner)
            logger.info("event=widget_panel_closed")

    def status(self, owner: str) -> str:
        """Return concise UI state without artifacts, hashes, test logs or private paths."""
        with self.lock:
            slot = self.slots.get(owner)
            if slot is None:
                return "Closed. Open widget to use count_vowels_in_text."
            if slot.cancelled.is_set():
                return "Closing widget."
            if slot.preview is None:
                return "Preparing the isolated widget. This may take about a minute."
            if slot.preview.alive:
                return "Ready. The isolated session lasts up to five minutes; reopen it when it expires."
            return "Session expired. Open widget again to continue."

    def close_all(self) -> None:
        """Request cleanup only for previews registered by this manager."""
        with self.lock:
            owners = list(self.slots)
        for owner in owners:
            try:
                self.close(owner)
            except Exception:
                logger.exception("event=widget_panel_cleanup_failed")
