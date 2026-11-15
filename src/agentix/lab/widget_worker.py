"""Native ASGI child entrypoint; imported generated widget code never enters the host.

Only framed JSON uses inherited private pipes. Standard output remains bounded diagnostic
text. This worker opens no network listener. Legacy widget calls use the host gateway;
reviewed application mode imports and calls its tools directly inside this boundary.
"""

import asyncio
import base64
import importlib.util
import json
import os
import struct
import sys
import threading
import time
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
os.environ.update(
    PATH=str(ROOT / "runtime"),
    GRADIO_ANALYTICS_ENABLED="False",
    HF_HUB_OFFLINE="1",
    HF_HOME=str(ROOT / "scratch"),
    GRADIO_TEMP_DIR=str(ROOT / "scratch"),
    USERPROFILE=str(ROOT / "scratch"),
    HOME=str(ROOT / "scratch"),
    TEMP=str(ROOT / "scratch"),
    TMP=str(ROOT / "scratch"),
    OTEL_SDK_DISABLED="true",
)
sys.path[:0] = [str(ROOT), str(ROOT / "runtime" / "site-packages")]

import msvcrt  # noqa: E402

from ipc_protocol import decode_frame, encode_frame  # noqa: E402
from widget_identity import TESTS_FILENAME, WIDGET_FILENAME  # noqa: E402

READER = msvcrt.open_osfhandle(int(sys.argv[1]), os.O_RDONLY | os.O_BINARY)
WRITER = msvcrt.open_osfhandle(int(sys.argv[2]), os.O_WRONLY | os.O_BINARY)
WRITE_LOCK = threading.Lock()
TOOLS = {}


def emit(message: dict) -> None:
    """Serialize complete framed writes; concurrent responses cannot interleave."""
    wire = encode_frame(message)
    with WRITE_LOCK:
        while wire:
            count = os.write(WRITER, wire)
            wire = wire[count:]


def exact(size: int) -> bytes:
    """Read exactly a bounded frame segment, treating closed parent IPC as shutdown."""
    data = bytearray()
    while len(data) < size:
        part = os.read(READER, size - len(data))
        if not part:
            raise EOFError
        data.extend(part)
    return bytes(data)


def read_message() -> dict:
    """Reject oversized lengths before allocating payload memory."""
    size = struct.unpack("<I", exact(4))[0]
    if size > 262144:
        raise ValueError("Frame limit")
    return decode_frame(exact(size))


class Context:
    """Minimal instance-specific capability; Python tool implementations stay outside."""

    def __init__(self, instance: str) -> None:
        """Bind the reviewed tool to one widget identity and API namespace."""
        self.instance = instance
        self.api_name = "vowels_" + instance

    def elem_id(self, control: str) -> str:
        """Permit only reviewed component roles, namespaced per instance."""
        if control not in ("input", "output", "execute"):
            raise ValueError("Unknown component role")
        return f"widget_{self.instance}_{control}"

    def invoke(self, text: str) -> int:
        """Request the approved vowel tool, with finite wait and no direct import."""
        identity = uuid4().hex
        event, result = threading.Event(), {}
        TOOLS[identity] = (event, result)
        try:
            emit({"type": "tool", "id": identity, "instance": self.instance, "text": text})
            if not event.wait(30) or "value" not in result:
                raise RuntimeError("Approved tool gateway failed")
            return result["value"]
        finally:
            TOOLS.pop(identity, None)


async def main() -> None:
    """Run a headless operation or build the reviewed GUI and multiplex private ASGI traffic."""
    if "--headless" in sys.argv:
        from operation import analyze_text

        value = analyze_text(json.loads((ROOT / "application_input.json").read_bytes()))
        emit({"type": "application_result", "result": value})
        return
    if "--application-tests" in sys.argv:
        import io
        import unittest

        suite = unittest.TestSuite()
        names = json.loads((ROOT / "application_widget_test_plan.json").read_bytes())
        for name in names:
            test_spec = importlib.util.spec_from_file_location(
                name + "_widget_tests", ROOT / (name + "_widget_tests.py")
            )
            module = importlib.util.module_from_spec(test_spec)
            test_spec.loader.exec_module(module)
            suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
        result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
        emit(
            {
                "type": "provisional_tests",
                "run": result.testsRun,
                "failures": len(result.failures),
                "errors": len(result.errors),
                "successful": result.wasSuccessful(),
                "detail": str(result.failures + result.errors)[:8192],
            }
        )
        if not result.wasSuccessful():
            raise RuntimeError("Proposed application widget tests failed")
        return
    import_started = time.monotonic()
    import gradio as gr
    from fastapi import FastAPI

    imported = time.monotonic()
    if "--application" in sys.argv:
        from app import create_application

        demo = create_application()

        def stop_application() -> None:
            """Ask the maintained parent to stop only this owned application job."""
            emit({"type": "supervisor_stop"})

        with demo:
            gr.Button(
                "Reload application",
                elem_id="application_refresh",
                elem_classes=["application-refresh-button"],
                scale=0,
                min_width=32,
            )
            gr.Button(
                "Edit layout",
                elem_id="application_edit",
                elem_classes=["application-edit-button"],
                scale=0,
                min_width=32,
            )
            gr.Button(
                "Close application",
                elem_id="application_stop",
                elem_classes=["application-close-button"],
                scale=0,
                min_width=32,
            ).click(stop_application, inputs=None, outputs=None, queue=False, api_name=False)
        from callback_runtime import supervise_callback

        for block in demo.fns.values():
            if block.fn is not None:
                block.fn = supervise_callback(block.fn, emit)
    else:
        spec = importlib.util.spec_from_file_location("approved_widget", ROOT / WIDGET_FILENAME)
        widget = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(widget)
        tests_path = ROOT / TESTS_FILENAME
        if tests_path.exists():
            import io
            import unittest

            test_spec = importlib.util.spec_from_file_location("reviewed_widget_tests", tests_path)
            test_module = importlib.util.module_from_spec(test_spec)
            test_spec.loader.exec_module(test_module)
            result = unittest.TextTestRunner(stream=io.StringIO()).run(
                unittest.defaultTestLoader.loadTestsFromModule(test_module)
            )
            emit(
                {
                    "type": "provisional_tests",
                    "run": result.testsRun,
                    "errors": len(result.errors),
                    "failures": len(result.failures),
                    "successful": result.wasSuccessful(),
                }
            )
            if not result.wasSuccessful():
                raise RuntimeError("Proposed widget tests failed")
        if "--tests-only" in sys.argv:
            return
        with gr.Blocks(title="AgentiX isolated widget") as demo:
            widget.create_widget(Context("first"))
            widget.create_widget(Context("second"))
    emit(
        {
            "type": "startup_timings",
            "seconds": {
                "gradio_import": imported - import_started,
                "application_build": time.monotonic() - imported,
            },
        }
    )
    from theme_policy import create_theme

    app = gr.mount_gradio_app(
        FastAPI(),
        demo,
        path="/",
        server_name="127.0.0.1",
        show_error=False,
        enable_monitoring=False,
        mcp_server=False,
        ssr_mode=False,
        theme=create_theme(gr),
        css=(ROOT / "application.css").read_text(encoding="utf-8"),
    )
    tasks = {}

    async def handle(message: dict) -> None:
        """Run one ASGI request; stream bounded response events rather than trusting HTML."""
        identity = message["id"]
        delivered = False

        async def receive() -> dict:
            """Deliver one bounded request body; cancellation represents disconnect."""
            nonlocal delivered
            if not delivered:
                delivered = True
                return {
                    "type": "http.request",
                    "body": base64.b64decode(message["body"], validate=True),
                    "more_body": False,
                }
            await asyncio.Future()

        async def send(event: dict) -> None:
            """Normalize only HTTP start/body events into non-executable JSON."""
            if event["type"] == "http.response.start":
                emit(
                    {
                        "type": "start",
                        "id": identity,
                        "status": event["status"],
                        "headers": [
                            [a.decode("latin1"), b.decode("latin1")]
                            for a, b in event.get("headers", [])
                        ],
                    }
                )
            elif event["type"] == "http.response.body":
                data = event.get("body", b"")
                for offset in range(0, len(data), 65536):
                    emit(
                        {
                            "type": "body",
                            "id": identity,
                            "data": base64.b64encode(data[offset : offset + 65536]).decode(),
                            "more": True,
                        }
                    )
                if not event.get("more_body", False):
                    emit({"type": "body", "id": identity, "data": "", "more": False})

        try:
            scope = message["scope"]
            scope["query_string"] = scope["query_string"].encode("ascii")
            scope["headers"] = [
                (a.encode("latin1"), b.encode("latin1")) for a, b in scope["headers"]
            ]
            await app(scope, receive, send)
        except Exception:
            emit({"type": "error", "id": identity})
        finally:
            tasks.pop(identity, None)

    async with app.router.lifespan_context(app):
        emit({"type": "ready"})
        try:
            while True:
                message = await asyncio.to_thread(read_message)
                if message["type"] == "request":
                    tasks[message["id"]] = asyncio.create_task(handle(message))
                elif message["type"] == "cancel":
                    task = tasks.get(message["id"])
                    if task:
                        task.cancel()
                elif message["type"] == "tool_result":
                    pending = TOOLS.get(message["id"])
                    if pending:
                        pending[1].update(message.get("result", {}))
                        pending[0].set()
                elif message["type"] == "stop":
                    break
        except EOFError:
            pass
        finally:
            for task in list(tasks.values()):
                task.cancel()
            if tasks:
                await asyncio.gather(*list(tasks.values()), return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
