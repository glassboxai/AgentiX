"""Supervisor-owned isolated widget session and framed, multiplexed ASGI transport.

Only the fixed maintained worker and approved bytes are staged. The HTTP bridge never
imports the widget. Child network capabilities remain zero. Legacy tool calls get a
second native boundary; application subclasses stage a reviewed direct-call package. Close cancels the complete widget job and closes all channel handles.
"""

import base64
import json
import logging
import queue
import shutil
import struct
import subprocess
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from agentix.lab.contracts import Text
from agentix.lab.ipc_protocol import decode_frame, encode_frame, validate_http_request
from agentix.lab.widget_artifacts import ApprovedWidget, validate_widget
from agentix.lab.widget_identity import FUNCTION_NAME, TESTS_FILENAME, WIDGET_FILENAME
from agentix.lab.widget_runtime import stage_runtime
from agentix.sandbox import WindowsSandbox
from agentix.sandbox.windows_process import NativeWindows

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class HttpResult:
    """Host-observed HTTP response, never an execution authorization."""

    status: int
    headers: list
    body: bytes


class WidgetSession:
    """One finite native worker with private inherited pipes and bounded dispatch."""

    def __init__(
        self,
        approved: ApprovedWidget | None = None,
        *,
        tests_only: bool = False,
        lifetime: int | None = 120,
    ) -> None:
        """Select maintained reference or explicitly reviewed widget bytes; perform no native IO."""
        if lifetime is not None and (type(lifetime) is not int or not 1 <= lifetime <= 600):
            raise ValueError("Widget lifetime must be 1 to 600 seconds")
        self.lifetime = lifetime
        self.session_id = uuid4().hex
        self.approved = approved
        self.tests_only = tests_only
        if approved is not None and not isinstance(approved, ApprovedWidget):
            raise ValueError("Explicit reviewed widget capability required")
        self.responses: dict[str, queue.Queue] = {}
        self.write_lock = threading.Lock()
        self.state_lock = threading.Lock()
        self.cancel = threading.Event()
        self.ready = threading.Event()
        self.closed = False
        self.close_lock = threading.Lock()
        self.diagnostics = {}
        self.timings: dict[str, float] = {}
        self.diagnostics["host_timings"] = self.timings
        self.tool_receipts = []
        self.tool_slots = threading.BoundedSemaphore(2)
        self.tool_calls = 0
        self.pool = ThreadPoolExecutor(max_workers=2)
        self.temporary = None

    def __enter__(self) -> "WidgetSession":
        """Close partial native staging on every startup exception."""
        try:
            return self._start()
        except BaseException as error:
            elapsed = time.monotonic() - getattr(self, "start_time", time.monotonic())
            self.timings["startup_failed_after"] = max(0.0, elapsed)
            self.diagnostics["startup_failure"] = type(error).__name__
            logger.error(
                "session=%s event=widget_startup_failed error_type=%s duration=%.3f",
                self.session_id,
                type(error).__name__,
                elapsed,
            )
            self.close()
            raise

    def _start(self) -> "WidgetSession":
        """Stage pinned dependencies, create private handles and await native readiness."""
        import pywintypes
        import win32api
        import win32con
        import win32pipe

        self.temporary = tempfile.TemporaryDirectory(prefix="agentix-widget-")
        self.root = Path(self.temporary.name)
        runtime = self.root / "runtime"
        runtime.mkdir()
        started = time.monotonic()
        self.start_time = started
        logger.info("session=%s event=widget_staging_started", self.session_id)
        stage_runtime(runtime)
        self.timings["runtime_staging"] = time.monotonic() - started
        logger.info(
            "session=%s event=widget_staged duration=%.3f",
            self.session_id,
            time.monotonic() - started,
        )
        for name in (
            "widget_worker.py",
            "ipc_protocol.py",
            "widget_identity.py",
            "callback_runtime.py",
        ):
            shutil.copyfile(Path(__file__).with_name(name), self.root / name)
        ui = Path(__file__).resolve().parents[1] / "ui"
        (self.root / "application.css").write_bytes((ui / "assets" / "style.css").read_bytes())
        (self.root / "theme_policy.py").write_bytes((ui / "theme.py").read_bytes())
        self._stage_payload()
        (self.root / "scratch").mkdir()
        attributes = pywintypes.SECURITY_ATTRIBUTES()
        attributes.bInheritHandle = True
        self.child_read, self.host_write = win32pipe.CreatePipe(attributes, 65536)
        self.host_read, self.child_write = win32pipe.CreatePipe(attributes, 65536)
        for handle in (self.host_read, self.host_write):
            win32api.SetHandleInformation(handle, win32con.HANDLE_FLAG_INHERIT, 0)
        self.native_thread = threading.Thread(target=self._run_native, daemon=True)
        self.reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self.native_thread.start()
        self.reader_thread.start()
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            if self.ready.wait(0.1):
                return self
            if not self.native_thread.is_alive():
                self.reader_thread.join(2)
                if self.ready.is_set():
                    return self
                break
        self.close()
        raise RuntimeError(
            "Isolated Gradio did not become ready: "
            + json.dumps(self.diagnostics, default=str)[-5000:]
        )

    def _stage_payload(self) -> None:
        """Stage only the legacy widget capability; subclasses provide reviewed app snapshots."""
        source = (
            self.approved.widget
            if self.approved is not None
            else Path(__file__).with_name("reference_widget.py").read_bytes()
        )
        validate_widget(source)
        (self.root / WIDGET_FILENAME).write_bytes(source)
        if self.tests_only and self.approved is not None and self.approved.tests:
            (self.root / TESTS_FILENAME).write_bytes(self.approved.tests)

    def _worker_arguments(self) -> list[str]:
        """Select maintained worker modes without child-controlled command fragments."""
        return ["--tests-only"] if self.tests_only else []

    def _control_message(self, message: dict) -> bool:
        """Accept bounded child timing diagnostics, never treating them as host evidence."""
        if message.get("type") != "startup_timings":
            return False
        values = message.get("seconds")
        if (
            set(message) != {"type", "seconds"}
            or not isinstance(values, dict)
            or set(values) - {"gradio_import", "application_build"}
            or any(type(v) not in (int, float) or not 0 <= v <= 600 for v in values.values())
        ):
            raise ValueError("Invalid startup timing diagnostics")
        self.diagnostics["child_timings"] = values
        return True

    def _run_native(self) -> None:
        """Own profile/job lifetime and grant only staged runtime plus private scratch."""
        native = NativeWindows()
        native_started = time.monotonic()
        try:
            with native.profile() as (sid, sid_text):
                for path, permission in ((self.root, "RX"), (self.root / "scratch", "M")):
                    result = subprocess.run(
                        [
                            "C:\\Windows\\System32\\icacls.exe",
                            str(path),
                            "/grant",
                            f"*{sid_text}:(OI)(CI){permission}",
                            "/T",
                            "/Q",
                        ],
                        capture_output=True,
                        timeout=30,
                        check=False,
                    )
                    if result.returncode:
                        raise RuntimeError("Cannot grant isolated runtime permissions")
                self.timings["permissions"] = time.monotonic() - native_started
                executable = self.root / "runtime" / "python.exe"
                handles = (int(self.child_read), int(self.child_write))
                command = subprocess.list2cmdline(
                    [
                        str(executable),
                        "-I",
                        "-S",
                        "-B",
                        str(self.root / "widget_worker.py"),
                        *map(str, handles),
                        *self._worker_arguments(),
                    ]
                )
                self.diagnostics["native"] = native.run(
                    str(executable),
                    command,
                    str(self.root),
                    sid,
                    timeout=self.lifetime,
                    memory=1024**3,
                    processes=4,
                    max_output=262144,
                    channel_handles=handles,
                    on_started=self._child_started,
                    cancel_event=self.cancel,
                )
        except Exception as error:
            self.diagnostics["error"] = type(error).__name__
        finally:
            for handle in (self.child_read, self.child_write):
                if int(handle):
                    handle.Close()

    def _child_started(self) -> None:
        """Drop parent copies after inheritance so child death produces pipe EOF."""
        self.timings["process_started"] = time.monotonic() - self.start_time
        self.child_read.Close()
        self.child_write.Close()

    def _write(self, message: dict) -> None:
        """Serialize bounded messages; native cancellation breaks stalled pipe operations."""
        import win32file

        wire = encode_frame(message)
        with self.write_lock:
            win32file.WriteFile(self.host_write, wire)

    def _check_runtime(self) -> None:
        """Allow specialized supervisors to enforce operation budgets during idle polling."""

    def _read_exact(self, size: int) -> bytes:
        """Poll available pipe bytes under a finite worker lifetime without blocking reads."""
        import win32file
        import win32pipe

        data = bytearray()
        while len(data) < size and not self.cancel.is_set():
            self._check_runtime()
            available = win32pipe.PeekNamedPipe(self.host_read, 0)[1]
            if available:
                data.extend(win32file.ReadFile(self.host_read, min(available, size - len(data)))[1])
            elif not self.native_thread.is_alive():
                raise EOFError
            else:
                time.sleep(0.005)
        if len(data) != size:
            raise EOFError
        return bytes(data)

    def _read_loop(self) -> None:
        """Dispatch only known message types; unknown/oversized frames terminate the job."""
        try:
            while not self.cancel.is_set():
                size = struct.unpack("<I", self._read_exact(4))[0]
                if size > 262144:
                    raise ValueError("Frame limit")
                message = decode_frame(self._read_exact(size))
                kind = message.get("type")
                if kind == "ready" and set(message) == {"type"}:
                    logger.info("session=%s event=widget_ready", self.session_id)
                    self.timings["worker_ready"] = time.monotonic() - self.start_time
                    self.ready.set()
                elif self._control_message(message):
                    pass
                elif kind == "provisional_tests":
                    self.diagnostics["provisional_tests"] = message
                    if self.tests_only:
                        self.ready.set()
                elif kind == "tool":
                    self.tool_calls += 1
                    if self.tool_calls > 32 or not self.tool_slots.acquire(blocking=False):
                        raise ValueError("Tool dispatch limit")
                    self.pool.submit(self._invoke_tool, message)
                elif kind in ("start", "body", "error"):
                    with self.state_lock:
                        target = self.responses.get(message.get("id"))
                    if target is None:
                        continue
                    target.put_nowait(message)
                else:
                    raise ValueError("Unknown IPC message")
        except Exception as error:
            if (
                (self.tests_only or getattr(self, "headless", False))
                and (
                    "provisional_tests" in self.diagnostics
                    or "application_result" in self.diagnostics
                )
                and (isinstance(error, EOFError) or getattr(error, "winerror", None) in (109, 232))
            ):
                return
            self.diagnostics["channel"] = type(error).__name__
            logger.info(
                "session=%s event=widget_channel_closed error_type=%s",
                self.session_id,
                type(error).__name__,
            )
            self.cancel.set()

    def _invoke_tool(self, message: dict) -> None:
        """Validate a single reviewed tool capability; never dispatch arbitrary names/paths."""
        from pydantic import TypeAdapter

        result = {}
        try:
            if (
                set(message) != {"type", "id", "instance", "text"}
                or message["instance"] not in ("first", "second")
                or not isinstance(message["id"], str)
                or len(message["id"]) != 32
            ):
                raise ValueError("Invalid tool request")
            try:
                text = TypeAdapter(Text).validate_python(message["text"])
            except (ValueError, TypeError):
                self._write({"type": "tool_result", "id": message["id"], "result": {}})
                return
            code = (
                self.approved.tool
                if self.approved is not None
                else Path(__file__).with_name("fixture_tools.py").read_bytes()
            )
            observation = WindowsSandbox().evaluate(
                code, "widget_vowels", FUNCTION_NAME, {"text": text}
            )
            if (
                observation.isolated
                and observation.exit_code == 0
                and not observation.failure
                and observation.report
                and observation.report.get("status") == "returned"
                and type(observation.report.get("value")) is int
            ):
                result = {"value": observation.report["value"]}
                import hashlib

                with self.state_lock:
                    self.tool_receipts.append(
                        {
                            "instance": message["instance"],
                            "input_sha256": hashlib.sha256(text.encode()).hexdigest(),
                            "value": result["value"],
                            "isolated": True,
                        }
                    )
                    self.tool_receipts = self.tool_receipts[-128:]
                logger.info(
                    "session=%s event=widget_tool_completed instance=%s",
                    self.session_id,
                    message["instance"],
                )
            self._write({"type": "tool_result", "id": message["id"], "result": result})
        except Exception:
            self.cancel.set()
        finally:
            self.tool_slots.release()

    def events(
        self,
        method: str,
        path: str,
        body: bytes = b"",
        *,
        query: bytes = b"",
        headers: list | None = None,
    ):
        """Yield bounded ASGI response messages; cancel disconnected/expired requests."""
        validate_http_request(method, path, body)
        if self.closed or self.cancel.is_set():
            raise RuntimeError("Native widget session unavailable")
        identity = uuid4().hex
        target = queue.Queue(maxsize=64)
        with self.state_lock:
            if len(self.responses) >= 16:
                raise RuntimeError("Too many concurrent widget requests")
            self.responses[identity] = target
        scope = {
            "type": "http",
            "asgi": {"version": "3.0", "spec_version": "2.3"},
            "http_version": "1.1",
            "method": method,
            "scheme": "http",
            "path": path,
            "raw_path": path.encode(),
            "query_string": query.decode("ascii"),
            "root_path": "",
            "headers": headers or [["content-type", "application/json"]],
            "server": ["127.0.0.1", 0],
            "client": ["127.0.0.1", 0],
        }
        # Byte-valued ASGI members are encoded explicitly by the worker, not pickle.
        scope.pop("raw_path")
        try:
            self._write(
                {
                    "type": "request",
                    "id": identity,
                    "scope": scope,
                    "body": base64.b64encode(body).decode(),
                }
            )
            total = 0
            deadline = time.monotonic() + 45
            while time.monotonic() < deadline and not self.cancel.is_set():
                try:
                    message = target.get(timeout=0.1)
                except queue.Empty:
                    continue
                if message["type"] == "error":
                    raise RuntimeError("Isolated HTTP request failed")
                if message["type"] == "body":
                    decoded = base64.b64decode(message["data"], validate=True)
                    total += len(decoded)
                    if total > 32 * 1024**2:
                        raise ValueError("Response limit")
                yield message
                if message["type"] == "body" and not message["more"]:
                    return
            raise RuntimeError("Widget response deadline")
        finally:
            with self.state_lock:
                self.responses.pop(identity, None)
            if not self.cancel.is_set():
                self._write({"type": "cancel", "id": identity})

    def request(self, method: str, path: str, body: bytes = b"") -> HttpResult:
        """Collect one finite response for native tests; the live bridge streams events."""
        status, headers, content = 502, [], bytearray()
        for event in self.events(method, path, body):
            if event["type"] == "start":
                status, headers = event["status"], event["headers"]
            else:
                content.extend(base64.b64decode(event["data"], validate=True))
        return HttpResult(status, headers, bytes(content))

    def close(self) -> None:
        """Cancel the owned native job, join workers and remove only its temporary tree."""
        with self.close_lock:
            if self.closed:
                return
            cleanup_started = time.monotonic()
            self.closed = True
            self.cancel.set()
            if hasattr(self, "native_thread"):
                if self.native_thread.ident is not None:
                    self.native_thread.join(35)
                if self.reader_thread.ident is not None:
                    self.reader_thread.join(5)
            for name in ("child_read", "child_write", "host_read", "host_write"):
                handle = getattr(self, name, None)
                if handle is not None and int(handle):
                    handle.Close()
            self.pool.shutdown(wait=True, cancel_futures=True)
            if self.temporary is not None:
                self.temporary.cleanup()
            self.timings["cleanup"] = time.monotonic() - cleanup_started

    def __exit__(self, *args: object) -> None:
        """Always close native resources, including failed browser validation runs."""
        self.close()


def run_provisional_tests(approved: ApprovedWidget) -> dict:
    """Run proposed tests in a distinct native process; reports remain provisional."""
    if not approved.tests:
        return {"run": 0, "successful": True, "note": "No proposed tests provided"}
    with WidgetSession(approved, tests_only=True) as session:
        session.native_thread.join(10)
        native_result = session.diagnostics.get("native")
        if not native_result or native_result[0] != 0 or native_result[2]:
            raise RuntimeError(
                "Provisional test process did not exit successfully: "
                + str((native_result[0], native_result[2]) if native_result else None)
            )
        report = session.diagnostics.get("provisional_tests", {})
        if report.get("successful") is not True:
            raise RuntimeError("Proposed widget tests failed")
        return report
