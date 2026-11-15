"""Host-owned, origin-bound presentation and lifecycle routes for one preview."""

import json
import logging
import secrets
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol

from agentix.storage.installed_apps import InstalledApps

logger = logging.getLogger(__name__)
ASSETS = Path(__file__).resolve().parents[1] / "ui" / "assets"


class PreviewControl(Protocol):
    """Owned listener identity and lifecycle operations; never accepts a host path."""

    port: int
    paused: bool

    def cancel_execution(self) -> None:
        """Stop the owned native worker."""
        ...

    def restart_execution(self) -> None:
        """Start the same reviewed snapshot again."""
        ...

    def request_close(self) -> None:
        """Signal owned listener and worker shutdown."""
        ...


class ApplicationControls:
    """Authorize bounded layout writes without granting file or Python capabilities."""

    def __init__(
        self,
        preview: PreviewControl,
        *,
        library: InstalledApps | None = None,
        identity: str | None = None,
        check: Callable[[], None] | None = None,
        root: Callable[[], Path] | None = None,
    ) -> None:
        """Bind one preview, optional protected identity and its private staging root.

        ``root`` is resolved per request because a restart replaces the staging
        directory; it never exposes a host path to the iframe.
        """
        self.preview = preview
        self.library = library
        self.identity = identity
        self.check = check
        self.root = root
        self.token = secrets.token_urlsafe(32)

    def handle(
        self, method: str, path: str, headers: dict[str, str], body: bytes
    ) -> tuple[int, str, bytes]:
        """Return status, media type and bytes; reject malformed or foreign mutations."""
        started = time.monotonic()
        try:
            if method == "GET" and path in {
                "/_agentix/editor.js",
                "/_agentix/style.css",
                "/_agentix/application.css",
            }:
                if path.endswith("application.css"):
                    # Served per request so a saved widget style reaches a reload and
                    # the separate "View as web" tab, which embed the startup CSS.
                    if self.root is None:
                        raise ValueError("Application stylesheet unavailable")
                    return 200, "text/css", (self.root() / "application.css").read_bytes()
                name = "application_editor.js" if path.endswith(".js") else "style.css"
                media = "text/javascript" if name.endswith(".js") else "text/css"
                return 200, media, (ASSETS / name).read_bytes()
            if method == "GET" and path == "/_agentix/layout":
                editable = bool(self.library and self.identity)
                layout = {"version": 1, "positions": {}}
                controls = None
                groups = {}
                if editable:
                    try:
                        layout = self.library.read_layout(self.identity)
                        controls = self.library.layout_controls(self.identity)
                        groups = self.library.layout_groups(self.identity)
                    except (ValueError, OSError):
                        editable = False
                # Even stale apps retain a token for their own Stop/Close. This
                # fallback grants no layout write, restart or code permission.
                return self._json(
                    {
                        "layout": layout,
                        "token": self.token,
                        "editable": editable,
                        "controls": sorted(controls) if controls is not None else None,
                        "groups": groups,
                    }
                )
            if method != "POST" or len(body) > 65536:
                raise ValueError("Unsupported operation")
            if (
                headers.get("origin") != f"http://127.0.0.1:{self.preview.port}"
                or not secrets.compare_digest(headers.get("x-agentix-token", ""), self.token)
                or headers.get("content-type") != "application/json"
            ):
                raise ValueError("Request authorization failed")

            def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
                """Reject ambiguous JSON object keys before validation."""
                result = {}
                for key, value in pairs:
                    if key in result:
                        raise ValueError("Duplicate JSON key")
                    result[key] = value
                return result

            payload = json.loads(body, object_pairs_hook=unique)
            if self.check and path in {"/_agentix/layout", "/_agentix/restart"}:
                self.check()
            if path == "/_agentix/layout" and self.library and self.identity:
                self.library.save_layout(self.identity, payload)
            elif (
                path in {"/_agentix/cancel", "/_agentix/restart", "/_agentix/close"}
                and payload == {}
            ):
                action = {
                    "/_agentix/cancel": self.preview.cancel_execution,
                    "/_agentix/restart": self.preview.restart_execution,
                    "/_agentix/close": self.preview.request_close,
                }[path]
                action()
            else:
                raise ValueError("Unsupported operation")
            logger.info(
                "event=application_control operation=%s duration=%.3f result=success",
                path,
                time.monotonic() - started,
            )
            return self._json({"ok": True})
        except (ValueError, OSError, TypeError):
            logger.warning(
                "event=application_control operation=%s duration=%.3f result=rejected",
                path,
                time.monotonic() - started,
            )
            return 403, "text/plain", b"Application control rejected"

    @staticmethod
    def _json(value: object) -> tuple[int, str, bytes]:
        """Encode only maintained response data."""
        return 200, "application/json", json.dumps(value).encode()
