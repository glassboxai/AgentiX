"""Opt-in native boundary checks using only independently authored fixtures."""

import socket
import sys

import pytest

pytestmark = [
    pytest.mark.windows_isolation,
    pytest.mark.skipif(sys.platform != "win32", reason="Windows AppContainer is required"),
]


def test_native_python_isolated_execution_and_unittest(tmp_path):
    """Verify native python isolated execution and unittest."""
    from agentix.sandbox import WindowsSandbox

    backend = WindowsSandbox()
    code = b"def add(a=1,b=2): return a+b"
    result = backend.execute(code, None, "adder", "add", {"a": 4})
    assert result.isolated and result.exit_code == 0
    assert result.report == {"kind": "call", "result": "6"}
    tests = b"import unittest\nfrom adder_code import add\nclass Checks(unittest.TestCase):\n def test_sum(self): self.assertEqual(add(),3)\n"
    result = backend.execute(code, tests, "adder", "", {})
    assert result.isolated and result.exit_code == 0
    assert result.report["run"] == 1 and result.report["successful"] is True


def test_native_denies_host_write_read_and_network(tmp_path):
    """Verify native denies host write read and network."""
    from agentix.sandbox import WindowsSandbox

    secret = tmp_path / "host-secret.txt"
    secret.write_text("private", encoding="utf-8")
    target = tmp_path / "host-write.txt"
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen()
    port = listener.getsockname()[1]
    with socket.create_connection(("127.0.0.1", port), timeout=1):
        connection, _ = listener.accept()
        connection.close()
    code = f"""from pathlib import Path
import socket
def restricted():
    denied = []
    for operation in (lambda: Path({str(secret)!r}).read_text(),
                      lambda: Path({str(target)!r}).write_text('bad'),
                      lambda: socket.create_connection(('127.0.0.1', {port}), timeout=1)):
        try:
            operation()
            denied.append(False)
        except PermissionError:
            denied.append(True)
        except TimeoutError:
            # WFP may silently drop an AppContainer loopback connection.
            # The parent control above establishes that this listener is live.
            denied.append(True)
        except OSError as error:
            denied.append((type(error).__name__, error.errno, getattr(error, 'winerror', None)))
    return denied
""".encode()
    try:
        result = WindowsSandbox().execute(code, None, "restricted", "restricted", {})
    finally:
        listener.close()
    assert result.isolated and result.report["result"] == "[True, True, True]"
    assert not target.exists()


def test_native_terminates_endless_execution():
    """Verify native terminates endless execution."""
    from agentix.sandbox import WindowsSandbox

    result = WindowsSandbox(timeout=1).execute(
        b"def loop():\n while True: pass", None, "loop", "loop", {}
    )
    assert result.isolated and result.exit_code != 0
    assert result.failure == "timeout"


def test_native_bounds_output():
    """Verify native bounds output."""
    from agentix.sandbox import WindowsSandbox

    result = WindowsSandbox(max_output=4096).execute(
        b"def flood():\n while True: print('x'*1000, flush=True)", None, "flood", "flood", {}
    )
    assert result.isolated and result.exit_code != 0
    assert result.failure == "output_limit" and len(result.output.encode()) <= 4096


def test_native_staging_is_read_only_and_environment_omits_secrets(monkeypatch):
    """Verify native staging is read only and environment omits secrets."""
    from agentix.sandbox import WindowsSandbox

    monkeypatch.setenv("AGENTIX_TEST_SECRET", "never-inherit-this-value")
    code = b"""import os
from pathlib import Path
def inspect_boundary():
    try:
        Path(__file__).write_text('changed')
        readonly = False
    except PermissionError:
        readonly = True
    return (readonly, os.environ.get('AGENTIX_TEST_SECRET'))
"""
    result = WindowsSandbox().execute(code, None, "boundary", "inspect_boundary", {})
    assert result.isolated and result.report["result"] == "(True, None)"


def test_native_limits_memory_without_stalling_host():
    """Verify native limits memory without stalling host."""
    from agentix.sandbox import WindowsSandbox

    code = b"""def allocate():
    data = bytearray(256*1024*1024)
    return len(data)
"""
    result = WindowsSandbox(memory=64 * 1024 * 1024).execute(code, None, "memory", "allocate", {})
    assert result.isolated and result.exit_code != 0


def test_native_service_lifecycle_uses_verified_current_bytes(tmp_path):
    """Verify native service lifecycle uses verified current bytes."""
    from trusted_sandbox import approve_next_review

    from agentix.security import SecurityManager
    from agentix.tools import ArtifactTools

    security = SecurityManager.for_owner("native-test-owner")
    security.TOOLS_ROOT_DIR = str(tmp_path / "artifacts")
    security.auto_approve = True
    operations = ArtifactTools(security)
    operations.compile_and_save_code_tool("adder", "def add(): return 3")
    tests = "import unittest\nfrom adder_code import add\nclass Checks(unittest.TestCase):\n def test_sum(self): self.assertEqual(add(),3)\n"
    assert operations.run_and_save_tests_tool("adder", tests).startswith(
        "TESTS_PROVISIONAL_PASSED:"
    )
    assert "NOT_VERIFIED" in operations.execute_generated_tool_tool("adder", "add")
    thread, errors = approve_next_review(security)
    assert operations.submit_acceptance_cases_tool(
        "adder",
        '{"version":1,"cases":[{"id":"sum","purpose":"Add numbers","function":"add","kwargs":{},"expect":{"kind":"value","value":3}}]}',
    ).startswith("ACCEPTANCE_VERIFIED:")
    thread.join(10)
    assert not errors
    assert operations.execute_generated_tool_tool("adder", "add") == "Tool Execution Result: 3"
    security.operation_id = "new-operation"
    assert operations.verification.execution_result() is None
    assert operations.verify_existing_tool_tool("adder").startswith("REUSE_READY:")
    assert operations.execute_generated_tool_tool("adder", "add") == "Tool Execution Result: 3"
    assert operations.verification.execution_result()["result"] == "3"
    # Changed bytes revoke the session grant; restoring them cannot revive it.
    path = tmp_path / "artifacts" / "adder" / "adder_code.py"
    original = path.read_bytes()
    path.write_bytes(original + b"\n# changed")
    assert "NOT_VERIFIED" in operations.execute_generated_tool_tool("adder", "add")
    path.write_bytes(original)
    assert not operations.verification.prepare_reuse("adder")


def test_native_limits_child_count_and_cleans_resources():
    """Verify native limits child count and cleans resources."""
    import os
    import tempfile
    from pathlib import Path

    from agentix.sandbox import WindowsSandbox

    packages = Path(os.environ["LOCALAPPDATA"]) / "Packages"
    temporary = Path(tempfile.gettempdir())
    profiles_before = set(packages.glob("Agentix.*"))
    folders_before = set(temporary.glob("agentix-isolated-*"))
    code = b"""import subprocess
import sys
def children():
    created = []
    for attempt in range(10):
        try:
            created.append(subprocess.Popen([sys.executable, '-I', '-S', '-c',
                'import time; time.sleep(20)'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        except OSError:
            return len(created)
    return len(created)
"""
    result = WindowsSandbox(processes=2).execute(code, None, "children", "children", {})
    assert result.isolated and result.report["result"] == "1"
    assert set(packages.glob("Agentix.*")) == profiles_before
    assert set(temporary.glob("agentix-isolated-*")) == folders_before


def test_native_typed_observations_and_function_exceptions():
    """Verify native typed observations and function exceptions."""
    from agentix.sandbox import WindowsSandbox

    code = b"def divide(a,b): return a/b"
    backend = WindowsSandbox()
    returned = backend.evaluate(code, "divider", "divide", {"a": 3, "b": 2})
    assert returned.isolated and returned.exit_code == 0
    assert returned.report == {"kind": "observation", "status": "returned", "value": 1.5}
    raised = backend.evaluate(code, "divider", "divide", {"a": 3, "b": 0})
    assert raised.isolated and raised.exit_code == 0
    assert raised.report == {
        "kind": "observation",
        "status": "raised",
        "exception_type": "ZeroDivisionError",
    }
