"""Loopback HTTP bridge serving only native ASGI response events, never widget imports."""

import asyncio
import base64
import re
import threading

from agentix.lab.ipc_protocol import validate_http_request
from agentix.lab.widget_session import WidgetSession


class WidgetBridge:
    """One owner-scoped experimental origin with strict route/header/body limits."""

    def __init__(
        self, session: WidgetSession, port: int, *, parent_origin: str | None = None
    ) -> None:
        """Bind the maintained transport to an explicit loopback origin."""
        if parent_origin is not None and (
            not re.fullmatch(r"http://127\.0\.0\.1:[0-9]{4,5}", parent_origin)
            or not 1024 <= int(parent_origin.rsplit(":", 1)[1]) <= 65535
        ):
            raise ValueError("Only an explicit loopback Lab origin may embed a widget")
        self.frame_ancestors = parent_origin or "'none'"
        self.controls = None
        self.session = session
        self.origin = f"127.0.0.1:{port}"

    async def __call__(self, scope, receive, send) -> None:
        """Forward HTTP bytes over IPC; reject origin spoofing and unsupported routes."""
        if scope["type"] != "http":
            return
        started = False
        iterator = None
        try:
            headers = {
                key.decode("latin1").lower(): value.decode("latin1")
                for key, value in scope.get("headers", [])
            }
            if (
                len(scope.get("headers", [])) > 64
                or any(len(key) + len(value) > 4096 for key, value in headers.items())
                or headers.get("host") != self.origin
            ):
                raise ValueError("Invalid host or headers")
            if scope["method"] == "POST" and headers.get("origin") not in (
                None,
                "http://" + self.origin,
            ):
                raise ValueError("Cross-origin request denied")
            body = bytearray()
            while True:
                event = await receive()
                if event["type"] != "http.request":
                    return
                body.extend(event.get("body", b""))
                if len(body) > 65536:
                    raise ValueError("Request size limit")
                if not event.get("more_body", False):
                    break
            if self.controls and scope["path"].startswith("/_agentix/"):
                status, media, content = await asyncio.to_thread(
                    self.controls.handle, scope["method"], scope["path"], headers, bytes(body)
                )
                await send(
                    {
                        "type": "http.response.start",
                        "status": status,
                        "headers": [
                            (b"content-type", media.encode()),
                            (b"cache-control", b"no-store"),
                            (b"x-content-type-options", b"nosniff"),
                        ],
                    }
                )
                await send({"type": "http.response.body", "body": content})
                return
            if self.controls and self.controls.preview.paused and scope["path"] == "/":
                content = b'<html><head><link rel="stylesheet" href="/_agentix/style.css"></head><body><button id="application_execute">Resume application</button><button id="application_stop">Close application</button><p id="application_paused">Application stopped.</p><script src="/_agentix/editor.js" defer></script></body></html>'
                await send(
                    {
                        "type": "http.response.start",
                        "status": 200,
                        "headers": [
                            (b"content-type", b"text/html"),
                            (b"cache-control", b"no-store"),
                        ],
                    }
                )
                await send({"type": "http.response.body", "body": content})
                return
            validate_http_request(scope["method"], scope["path"], bytes(body))
            query = scope.get("query_string", b"")
            if len(query) > 4096:
                raise ValueError("Query limit")
            safe_headers = [
                [name, headers[name]]
                for name in ("host", "content-type", "accept")
                if name in headers
            ]
            iterator = self.session.events(
                scope["method"], scope["path"], bytes(body), query=query, headers=safe_headers
            )

            def advance():
                """Avoid propagating StopIteration through an asyncio Future."""
                return next(iterator, None)

            while True:
                message = await asyncio.to_thread(advance)
                if message is None:
                    break
                if message["type"] == "start":
                    if (
                        started
                        or type(message["status"]) is not int
                        or not 200 <= message["status"] <= 599
                        or len(message["headers"]) > 64
                    ):
                        raise ValueError("Invalid response start")
                    response_headers = []
                    for name, value in message["headers"]:
                        if (
                            name.lower()
                            in ("content-type", "cache-control", "content-encoding", "vary")
                            and len(value) <= 4096
                            and "\r" not in value
                            and "\n" not in value
                        ):
                            response_headers.append((name.lower().encode(), value.encode("latin1")))
                    response_headers += [
                        (
                            b"content-security-policy",
                            b"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data: blob:; font-src 'self' data:; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors "
                            + self.frame_ancestors.encode(),
                        ),
                        (b"x-content-type-options", b"nosniff"),
                        (b"referrer-policy", b"no-referrer"),
                    ]
                    await send(
                        {
                            "type": "http.response.start",
                            "status": message["status"],
                            "headers": response_headers,
                        }
                    )
                    started = True
                elif message["type"] == "body":
                    if not started or type(message["more"]) is not bool:
                        raise ValueError("Invalid response body")
                    await send(
                        {
                            "type": "http.response.body",
                            "body": base64.b64decode(message["data"], validate=True)
                            + (
                                b'<link rel="stylesheet" href="/_agentix/application.css">'
                                b'<script src="/_agentix/editor.js" defer></script>'
                                if self.controls and scope["path"] == "/" and not message["more"]
                                else b""
                            ),
                            "more_body": message["more"],
                        }
                    )
        except Exception:
            if not started:
                await send(
                    {
                        "type": "http.response.start",
                        "status": 403,
                        "headers": [(b"content-type", b"text/plain")],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": b"Widget request rejected or unavailable",
                    }
                )
            else:
                await send({"type": "http.response.body", "body": b"", "more_body": False})
        finally:
            if iterator is not None:
                await asyncio.to_thread(iterator.close)


def serve_widget(session: WidgetSession, port: int) -> None:
    """Expose only one loopback origin and stop its server when the native worker ends."""
    import uvicorn

    server = uvicorn.Server(
        uvicorn.Config(
            WidgetBridge(session, port),
            host="127.0.0.1",
            port=port,
            log_level="warning",
            lifespan="off",
        )
    )

    def monitor():
        """Close only the owned preview server after native timeout or channel failure."""
        while session.native_thread.is_alive() and not session.cancel.wait(0.2):
            pass
        server.should_exit = True

    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
    server.run()
