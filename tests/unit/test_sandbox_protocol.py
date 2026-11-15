"""Validate bounded process reports without executing generated project artifacts."""

import pytest


@pytest.mark.parametrize("output", ["TESTS_PASSED", "{}", '{"kind":"tests"}', "[]"])
def test_plain_text_cannot_become_a_test_report(output):
    """Verify plain text cannot become a test report."""
    from agentix.sandbox import decode_report

    with pytest.raises(ValueError):
        decode_report(output)


def test_runtime_is_never_started_on_unsupported_platform(monkeypatch):
    """Verify runtime is never started on unsupported platform."""
    from agentix import sandbox

    monkeypatch.setattr(sandbox.sys, "platform", "linux")
    with pytest.raises(sandbox.IsolationUnavailable):
        sandbox.WindowsSandbox().execute(b"raise RuntimeError()", None, "safe", "call", {})


def test_duplicate_observation_values_are_rejected():
    """Verify duplicate observation values are rejected."""
    from agentix.sandbox import decode_report

    with pytest.raises(ValueError):
        decode_report(
            'AGENTIX_REPORT:{"kind":"observation","status":"returned","value":1,"value":3}'
        )
