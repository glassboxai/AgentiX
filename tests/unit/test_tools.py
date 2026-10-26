"""Exercise actual artifact functions; replace only service and process boundaries."""

import subprocess
from types import SimpleNamespace
from unittest.mock import Mock

import pytest


def write_tool(system, code, name="adder"):
    """Install a trusted test fixture into temporary tool storage."""
    directory = system.root / name
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{name}_code.py").write_text(code, encoding="utf-8")


def observe_fixture(system, name="adder"):
    """Simulate the OS boundary observation for trusted call-focused fixtures."""
    (system.root / name / f"{name}_tests.py").write_text("import unittest", encoding="utf-8")
    ledger = system.custom_tools.verification
    code, tests = ledger.snapshot(name)
    assert ledger.record(
        name,
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    assert ledger.authorize(name, code, tests, "trusted-fixture-contract", frozenset({"add"}))


@pytest.mark.parametrize("wrapper", ["{}", "```python\n{}\n```", "```\n{}\n```"])
def test_compile_strips_markdown_and_saves(system, wrapper):
    """Verify compile strips markdown and saves."""
    system.security.auto_approve = True
    code = "def add(a, b):\n    return a + b"
    assert system.custom_tools.compile_and_save_code_tool("adder", wrapper.format(code)).startswith(
        "Success:"
    )
    assert (system.root / "adder" / "adder_code.py").read_text() == code


def test_invalid_syntax_logs_incident_without_saving_code(system):
    """Verify invalid syntax logs incident without saving code."""
    system.security.auto_approve = True
    result = system.custom_tools.compile_and_save_code_tool("bad", "def broken(:")
    assert result.startswith("COMPILATION_ERROR:")
    assert not (system.root / "bad" / "bad_code.py").exists()
    assert "SyntaxError" in (system.root / "bad" / "bad_code_incidences.md").read_text()


def test_compilation_does_not_execute_code(system):
    """Verify compilation does not execute code."""
    system.security.auto_approve = True
    assert system.custom_tools.compile_and_save_code_tool(
        "safe", "raise RuntimeError('must not run')"
    ).startswith("Success:")


def test_save_specifications(system):
    """Verify save specifications."""
    system.security.auto_approve = True
    system.custom_tools.save_specifications_tool("adder", "# Specification")
    assert (system.root / "adder" / "adder_specifications.md").read_text() == "# Specification"


@pytest.mark.parametrize(
    "function,suffix",
    [
        ("log_specifications_incidence_tool", "specifications"),
        ("log_coder_incidence_tool", "code"),
        ("log_tester_incidence_tool", "tests"),
    ],
)
def test_incidence_logging_appends(system, function, suffix):
    """Verify incidence logging appends."""
    system.security.auto_approve = True
    log = getattr(system.custom_tools, function)
    log("adder", "first failure")
    log("adder", "second failure")
    content = (system.root / "adder" / f"adder_{suffix}_incidences.md").read_text()
    assert "first failure" in content and "second failure" in content
    assert content.count("### Incidence Details:") == 2


def test_read_existing_artifact(system):
    """Verify read existing artifact."""
    write_tool(system, "# café")
    assert system.custom_tools.read_artifact_tool("adder", "adder_code.py") == "# café"


def test_read_missing_artifact(system):
    """Verify read missing artifact."""
    assert "does not exist" in system.custom_tools.read_artifact_tool("adder", "missing")


def test_read_traversal_returns_error(system):
    """Verify read traversal returns error."""
    assert system.custom_tools.read_artifact_tool("adder", "../../outside").startswith(
        "Error reading file:"
    )


@pytest.mark.parametrize(
    "kwargs,result", [("{}", 3), ('{"a": 5, "b": 7}', 12), ("", 3), ("''", 3), ('""', 3)]
)
def test_execute_function_arguments(system, kwargs, result):
    """Verify execute function arguments."""
    write_tool(system, "def add(a=1, b=2):\n    return a + b")
    observe_fixture(system)
    assert (
        system.custom_tools.execute_generated_tool_tool("adder", "add", kwargs)
        == f"Tool Execution Result: {result}"
    )


def test_execute_missing_file(system):
    """Verify execute missing file."""
    assert "TOOL_NOT_VERIFIED" in system.custom_tools.execute_generated_tool_tool("missing", "add")


def test_execute_unknown_function_is_rejected(system):
    """Verify execute unknown function is rejected."""
    write_tool(system, "def add(): return 1\ndef _private(): return 2")
    observe_fixture(system)
    result = system.custom_tools.execute_generated_tool_tool("adder", "missing")
    assert result.startswith("TOOL_NOT_VERIFIED:")


def test_execute_invalid_json(system):
    """Verify execute invalid json."""
    write_tool(system, "def add(): return 1")
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", "{bad").startswith(
        "Error parsing kwargs_json:"
    )


@pytest.mark.parametrize(
    "code,kwargs",
    [
        ('def add(): raise ValueError("bad value")', "{}"),
        ("def add(a): return a", "{}"),
    ],
)
def test_execute_errors_are_reported(system, code, kwargs):
    """Verify execute errors are reported."""
    write_tool(system, code)
    observe_fixture(system)
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", kwargs).startswith(
        "Execution Error:"
    )


@pytest.mark.parametrize(
    "returncode,prefix", [(0, "TESTS_PROVISIONAL_PASSED:"), (1, "TESTS_FAILED:")]
)
def test_test_runner_captures_results(system, monkeypatch, returncode, prefix):
    """Verify test runner captures results."""
    system.security.auto_approve = True
    write_tool(system, "def add(): return 3")
    runner = Mock(
        return_value=SimpleNamespace(
            returncode=returncode,
            stdout=(
                'output\nAGENTIX_REPORT:{"kind":"tests","run":1,"failures":0,'
                '"errors":0,"skipped":0,"successful":true}\n'
            ),
            stderr="detail",
        )
    )
    monkeypatch.setattr(system.test_process, "run", runner)
    result = system.custom_tools.run_and_save_tests_tool("adder", "```python\nimport unittest\n```")
    assert result.startswith(prefix)
    assert "output" in result and "detail" in result
    assert runner.call_args.kwargs["timeout"] == 30
    assert runner.call_args.kwargs["cwd"] != str(system.root / "adder")
    assert runner.call_args.args[0][1:4] == ["-I", "-S", "-B"]
    assert (system.root / "adder" / "adder_tests.py").read_text() == "import unittest"
    assert (system.root / "adder" / "adder_tests_incidences.md").exists() == (returncode != 0)


@pytest.mark.parametrize(
    "error,expected",
    [
        (subprocess.TimeoutExpired("test", 30), "timed out"),
        (OSError("cannot spawn"), "cannot spawn"),
    ],
)
def test_runner_failure_records_incident(system, monkeypatch, error, expected):
    """Verify runner failure records incident."""
    system.security.auto_approve = True
    write_tool(system, "def add(): return 3")
    monkeypatch.setattr(system.test_process, "run", Mock(side_effect=error))
    result = system.custom_tools.run_and_save_tests_tool("adder", "import unittest")
    assert result.startswith("TESTS_FAILED:") and "execution denied" in result
    assert "execution denied" in (system.root / "adder" / "adder_tests_incidences.md").read_text()


def test_rejected_test_file_is_never_executed(system, monkeypatch):
    """Verify rejected test file is never executed."""
    monkeypatch.setattr(
        system.security, "safe_write_file", Mock(return_value="Operation aborted: rejected")
    )
    runner = Mock()
    monkeypatch.setattr(system.test_process, "run", runner)
    assert "aborted" in system.custom_tools.run_and_save_tests_tool("adder", "code")
    runner.assert_not_called()


def test_edited_python_is_validated_before_save(system, monkeypatch):
    """Verify edited python is validated before save."""
    (system.root / "adder").mkdir(parents=True)
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, "def invalid(:"))
    )
    system.custom_tools.compile_and_save_code_tool("adder", "def valid(): return 1")
    target = system.root / "adder" / "adder_code.py"
    assert not target.exists(), "Invalid edited Python was persisted"


def test_invalid_edited_tests_are_not_executed(system, monkeypatch):
    """The same final-content validation must protect test-script persistence."""
    (system.root / "adder").mkdir(parents=True)
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, "def invalid(:"))
    )
    runner = Mock()
    monkeypatch.setattr(system.test_process, "run", runner)
    result = system.custom_tools.run_and_save_tests_tool("adder", "import unittest")
    assert result.startswith("Error validating Python:")
    runner.assert_not_called()
    assert not (system.root / "adder" / "adder_tests.py").exists()
