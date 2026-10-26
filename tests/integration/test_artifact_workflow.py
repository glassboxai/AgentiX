"""Integrate storage, compilation, unittest protocol and execution gating.

Only trusted fixture code is executed. CrewAI and widgets remain substituted;
The native OS observation is doubled. This is not a native isolation, live LLM
or browser end-to-end test; those security checks are explicitly opt-in.
"""

from trusted_sandbox import approve_next_review


def test_complete_trusted_tool_lifecycle(system):
    """Verify complete trusted tool lifecycle."""
    system.security.auto_approve = True
    tools = system.custom_tools
    assert tools.save_specifications_tool("adder", "Add two integers.").startswith("Success:")
    assert tools.compile_and_save_code_tool(
        "adder", 'def add(a, b):\n    """Add two numbers."""\n    return a + b'
    ).startswith("Success:")
    test_code = """import unittest
from adder_code import add

class AdditionTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, 3), 1)
"""
    result = tools.run_and_save_tests_tool("adder", test_code)
    assert result.startswith("TESTS_PROVISIONAL_PASSED:"), result
    assert "Ran 2 tests" in result
    assert not tools.verification.is_verified("adder")
    thread, errors = approve_next_review(system.security)
    assert tools.submit_acceptance_cases_tool(
        "adder",
        '{"version":1,"cases":[{"id":"sum","purpose":"Add integers","function":"add","kwargs":{"a":2,"b":3},"expect":{"kind":"value","value":5}}]}',
    ).startswith("ACCEPTANCE_VERIFIED:")
    thread.join(10)
    assert not errors
    assert "add(a, b)" in system.main.get_installed_tools_catalog()
    assert (
        tools.execute_generated_tool_tool("adder", "add", '{"a": 2, "b": 3}')
        == "Tool Execution Result: 5"
    )


def test_real_failing_generated_test_creates_incident(system):
    """Verify real failing generated test creates incident."""
    system.security.auto_approve = True
    system.custom_tools.compile_and_save_code_tool("broken", "def broken(): return 0")
    code = "import unittest\nclass Failure(unittest.TestCase):\n    def test_failure(self):\n        self.assertEqual(1, 2)"
    result = system.custom_tools.run_and_save_tests_tool("broken", code)
    assert result.startswith("TESTS_FAILED:")
    assert "AssertionError" in (system.root / "broken" / "broken_tests_incidences.md").read_text()
