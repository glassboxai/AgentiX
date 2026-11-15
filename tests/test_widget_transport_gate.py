"""LAB-002 native transport gate; authored temporary fixture, never generated code."""

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import pytest

from agentix.sandbox import WindowsSandbox


@pytest.mark.windows_isolation
@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="LAB-002-TRANSPORT: current zero-capability AppContainer cannot serve host HTTP",
)
def test_native_widget_server_can_serve_host_browser(tmp_path):
    """A reachable isolated HTTP server is necessary, not sufficient, for Gradio."""

    class Control(BaseHTTPRequestHandler):
        """Demonstrate the host HTTP route works independently of the child."""

        def do_GET(self):
            """Return one bounded response and no user data."""
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"lab002-control")

        def log_message(self, *args):
            """Suppress benign access logs without hiding assertions."""

    control = HTTPServer(("127.0.0.1", 0), Control)
    control.timeout = 3
    control_thread = threading.Thread(target=control.handle_request)
    control_thread.start()
    opener = build_opener(ProxyHandler({}))
    try:
        with opener.open(f"http://127.0.0.1:{control.server_port}/", timeout=2) as response:
            if response.read(128) != b"lab002-control":
                raise RuntimeError("Host control did not return the expected independent payload")
    finally:
        control_thread.join(5)
        control.server_close()
    port = control.server_port
    source = f"""import http.server

def probe():
    requests = []
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            requests.append(True)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"lab002-isolated")
        def log_message(self, *args):
            pass
    try:
        server = http.server.HTTPServer(("127.0.0.1", {port}), Handler)
        server.timeout = 5
        server.handle_request()
        server.server_close()
        return {{"stage": "bound", "http_requests": len(requests)}}
    except OSError as error:
        return {{"stage": "bind_or_serve_denied", "error_type": type(error).__name__, "errno": error.errno, "winerror": getattr(error, "winerror", None)}}
""".encode()
    observation = {}

    def execute():
        """Keep native ownership on one thread and expose result only after joining."""
        try:
            observation["result"] = WindowsSandbox(timeout=15).evaluate(
                source, "widget_probe", "probe", {}
            )
        except Exception as error:
            observation["setup_error"] = type(error).__name__

    thread = threading.Thread(target=execute)
    thread.start()
    reached = False
    connection_errors = {}
    deadline = time.monotonic() + 35
    while thread.is_alive() and time.monotonic() < deadline:
        try:
            with opener.open(f"http://127.0.0.1:{port}/", timeout=0.5) as response:
                reached = response.status == 200 and response.read(128) == b"lab002-isolated"
                if reached:
                    break
        except (URLError, TimeoutError, OSError) as error:
            reason = getattr(error, "reason", error)
            category = type(reason).__name__
            connection_errors[category] = connection_errors.get(category, 0) + 1
            time.sleep(0.1)
    thread.join(30)
    result = observation.get("result")
    evidence = {
        "host_control": True,
        "host_reached_isolated_http": reached,
        "thread_stopped": not thread.is_alive(),
        "setup_error": observation.get("setup_error"),
        "isolated": result.isolated if result else False,
        "exit_code": result.exit_code if result else None,
        "failure": result.failure if result else None,
        "child_observation": result.report if result else None,
        "host_connection_errors": connection_errors,
    }
    (tmp_path / "widget-transport.json").write_text(
        json.dumps(evidence, indent=2), encoding="utf-8"
    )
    print(json.dumps(evidence, indent=2))
    if (
        thread.is_alive()
        or result is None
        or not result.isolated
        or result.failure
        or result.exit_code != 0
    ):
        raise RuntimeError("Probe setup, isolation or cleanup failed; not a transport-gate verdict")
    assert reached, (
        "LAB-002-TRANSPORT: host cannot reach isolated HTTP server; see host/child evidence"
    )
