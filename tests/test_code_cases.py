"""V6-045: propose reviewed data without executing generated connection code."""

from dataclasses import replace

from test_application_crews import approved_tool
from test_code_application import proposal


def test_reviewed_cases_fill_a_compatible_dependent_application() -> None:
    """Only approved expected values may flow through connection assignments."""
    from agentix.application.code_cases import propose_cases

    tool = approved_tool()
    contract = {
        "cases": tool.reviewed_contract["cases"]
        + [
            {
                "function": "calculator",
                "kwargs": {"a": 5, "b": 3},
                "expect": {"kind": "value", "value": 8},
            }
        ]
    }
    result = propose_cases(proposal(), {"calculator": replace(tool, reviewed_contract=contract)})
    assert result["payload"] == {"amount": 2}
    assert result["expected"] == {"first": 5, "second": 8}
    assert result["pending"] == []
    assert result["provenance"]["second"] == "Reviewed catalog value case"


def test_partial_cases_report_missing_expectations_without_predicting() -> None:
    """A missing downstream approved case must remain a visible human decision."""
    from agentix.application.code_cases import propose_cases

    result = propose_cases(proposal(), {"calculator": approved_tool()})
    assert result["payload"] == {"amount": 2}
    assert result["expected"] == {"first": 5}
    assert "expected.second" in result["pending"]
    assert "second" not in result["expected"]


def test_unsupported_python_is_never_evaluated() -> None:
    """Calls outside the reviewed declarative subset leave pending data, never run."""
    from agentix.application.code_cases import propose_cases

    value = proposal()
    value["connection_code"] = 'def run(payload, call):\n    raise RuntimeError("must not run")\n'
    result = propose_cases(value, {"calculator": approved_tool()})
    assert result["expected"] == {}
    assert set(result["pending"]) >= {"payload.amount", "expected.first", "expected.second"}


def test_missing_cases_produce_persistent_actionable_status(tmp_path) -> None:
    """V6-045: approval rejection must identify cases, without crossing execution gates."""
    import json
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    sessions = registry()
    owner = sessions.resolve(None, "alice")

    def reject(*args):
        """Simulate the existing supervisor acceptance rejection without native work."""
        raise ValueError("Complete independent application acceptance")

    backend = ApplicationsBackend(sessions, supervisor=SimpleNamespace(approve=reject))
    request = SimpleNamespace(session_hash="alice")
    _, state = backend._resolve(owner.token, request)
    state.candidate = SimpleNamespace(
        preview=None,
        close=lambda: None,
        review_text=json.dumps(
            {
                "manifest": {
                    "schema_version": 3,
                    "inputs": {"amount": {"type": "integer"}},
                    "widgets": [{"id": "first", "tool": "calculator"}],
                    "tools": {"calculator": approved_tool().schema},
                },
                "independent_acceptance": {"payload": {}, "expected": {}},
            }
        ),
    )
    owner.controller.state.application_review_pending = True
    rows = list(backend.approve(True, "fixture", owner.token, request))
    assert "application_acceptance.json" in rows[-1][0]
    assert "payload.amount" in rows[-1][0]
    assert "expected.first" in rows[-1][0]
    assert not owner.controller.state.application_busy
    assert backend.poll(owner.token, request)[0] is None


def test_pipeline_prefills_editor_but_still_requires_human_review(tmp_path) -> None:
    """Generated suggestions stay editable and never replace explicit owner approval."""
    import json

    import pytest
    from test_general_application_pipeline import WIDGET

    from agentix.application.app_review import ApplicationReview
    from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor

    class Coordinator:
        """Return independently authored inert source and presentation fixtures."""

        def plan(self, *args):
            """Return one direct reviewed call with a public input."""
            value = proposal()
            value["widgets"] = value["widgets"][:1]
            value["connection_code"] = (
                '"""Fixture."""\ndef run(payload, call):\n    """Connect."""\n    call("first", a=payload["amount"], b=3)\n'
            )
            return value

        def widgets(self, tools, feedback):
            """Supply trusted widget fixtures without model work."""
            return {
                name: {"widget_code": WIDGET, "tests_code": "# provisional", "notes": "fixture"}
                for name in tools
            }

    item = ApplicationPipeline(tmp_path, coordinator_factory=lambda _: Coordinator()).generate(
        "Add three", tools={"calculator": approved_tool()}
    )
    text, editable, hint = ApplicationReview().read(item, "application_acceptance.json")
    assert editable and "structurally valid" in hint
    assert json.loads(text) == {"payload": {"amount": 2}, "expected": {"first": 5}}
    assert not item.approved
    supervisor = ApplicationSupervisor()
    with pytest.raises(ValueError, match="Review"):
        supervisor.approve(item, item.identity, False)
    supervisor.approve(item, item.identity, True)
    assert item.approved and not item.verified
    old_identity = item.identity
    ApplicationReview().save(item, "application_acceptance.json", text, old_identity)
    assert not item.approved and item.identity != old_identity


def test_incompatible_literals_and_branching_leave_expectations_pending() -> None:
    """Neither a different constant nor unsupported control flow invents a result."""
    from agentix.application.code_cases import propose_cases

    for source in (
        'def run(payload, call):\n    call("first", a=payload["amount"], b=99)\n',
        'def run(payload, call):\n    if payload["amount"]:\n        call("first", a=2, b=3)\n',
    ):
        assembly = proposal() | {"connection_code": source}
        result = propose_cases(assembly, {"calculator": approved_tool()})
        assert result["expected"] == {}
        assert "expected.first" in result["pending"]
