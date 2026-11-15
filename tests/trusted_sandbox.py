"""OS-boundary double for trusted infrastructure fixtures only, never production.

This deliberately does not provide isolation. Native security is verified by the
separate opt-in suite. The application receives a simulated OS observation here.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

from agentix import sandbox_worker
from agentix.sandbox import SandboxResult, decode_report


def approve_next_review(security, edited=None):
    """Simulate a human only in infrastructure tests; retain callback errors."""
    errors = []

    def respond():
        """Provide respond for the enclosing trusted test fixture."""
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            pending = security.get_pending_request()
            if pending:
                if pending["action"] != "review_acceptance":
                    errors.append("Unexpected review kind")
                security.resolve_pending_request(
                    True, edited, request_id=pending["request_id"], owner_id=pending["owner_id"]
                )
                return
            time.sleep(0.005)
        errors.append("Human review request missing")

    thread = threading.Thread(target=respond, daemon=True)
    thread.start()
    return thread, errors


class TrustedFixtureSandbox:
    """Execute only independently authored test fixture bytes with the real protocol."""

    def execute(self, code, tests, tool_name, function_name, kwargs, *, observation=False):
        """Use an isolated temporary input folder, without claiming native coverage."""
        with tempfile.TemporaryDirectory(prefix="agentix-trusted-fixture-") as folder:
            root = Path(folder)
            shutil.copyfile(sandbox_worker.__file__, root / "worker.py")
            (root / f"{tool_name}_code.py").write_bytes(code)
            if tests is not None:
                (root / f"{tool_name}_tests.py").write_bytes(tests)
            (root / "request.json").write_text(
                json.dumps(
                    dict(
                        kind="tests"
                        if tests is not None
                        else "observation"
                        if observation
                        else "call",
                        tool_name=tool_name,
                        function_name=function_name,
                        kwargs=kwargs,
                    )
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, "-I", "-S", "-B", str(root / "worker.py")],
                cwd=folder,
                capture_output=True,
                text=True,
                timeout=30,
            )
            output = result.stdout + "\n" + result.stderr
            try:
                report = decode_report(output)
            except ValueError:
                report = None
            return SandboxResult(result.returncode, output, report, True)

    def evaluate(self, code, tool_name, function_name, kwargs):
        """Run the trusted fixture through the same observation worker protocol."""
        return self.execute(code, None, tool_name, function_name, kwargs, observation=True)
