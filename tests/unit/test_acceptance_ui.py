"""Show human-review context without treating generated source as markup."""

from types import SimpleNamespace

VALID_CONTRACT = """{
  "version": 1,
  "cases": [
    {
      "id": "normal_case",
      "purpose": "Verify the public function result",
      "function": "replace_e_with_a",
      "kwargs": {"text": "hello"},
      "expect": {"kind": "value", "value": "hallo"}
    }
  ]
}"""


def _acceptance_pending(system, request_id="review-1"):
    """Install one bounded acceptance review owned by the test session."""
    return {
        "request_id": request_id,
        "owner_id": system.security.owner_id,
        "filepath": "Acceptance cases",
        "action": "review_acceptance",
        "content": VALID_CONTRACT,
    }


def test_valid_acceptance_proposal_enables_approval(system, monkeypatch):
    """Enable the review control only after the existing contract parser accepts it."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))
    system.app.validation = SimpleNamespace(status=lambda: {"stage": "pending_review"})

    button, message = system.app.approval_readiness(VALID_CONTRACT, "review-1")

    assert button["interactive"] is True
    assert message == "Acceptance cases are valid and ready for review."


def test_invalid_acceptance_proposal_disables_approval(system, monkeypatch):
    """Prevent an invalid acceptance proposal from reaching the generic approval error."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))
    system.app.validation = SimpleNamespace(status=lambda: {"stage": "pending_review"})

    button, message = system.app.approval_readiness("{}", "review-1")

    assert button["interactive"] is False
    assert message == "Correct the acceptance JSON before approving."


def test_pending_or_replaced_acceptance_request_disables_approval(system, monkeypatch):
    """Keep approval disabled until the current pending request has been validated."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))

    button, message = system.app.approval_readiness(VALID_CONTRACT, "stale-review")

    assert button["interactive"] is False
    assert message == "Wait for the current review proposal to load."


def test_pending_acceptance_validation_disables_approval(system, monkeypatch):
    """Do not enable approval before the evaluator reports the review-ready stage."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))
    system.app.validation = SimpleNamespace(status=lambda: {"stage": "provisional_passed"})

    button, message = system.app.approval_readiness(VALID_CONTRACT, "review-1")

    assert button["interactive"] is False
    assert message == "Acceptance validation is pending."


def test_missing_acceptance_validation_disables_approval(system, monkeypatch):
    """Do not treat a proposal as validated when no evaluator is available."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))

    button, message = system.app.approval_readiness(VALID_CONTRACT, "review-1")

    assert button["interactive"] is False
    assert message == "Acceptance validation is pending."


def test_editing_a_valid_acceptance_proposal_disables_approval_immediately(system, monkeypatch):
    """Revalidate the edited text instead of retaining the prior valid button state."""
    monkeypatch.setattr(system.security, "get_pending_request", lambda: _acceptance_pending(system))
    system.app.validation = SimpleNamespace(status=lambda: {"stage": "pending_review"})

    ready_button, _ = system.app.approval_readiness(VALID_CONTRACT, "review-1")
    edited_button, message = system.app.approval_readiness("", "review-1")

    assert ready_button["interactive"] is True
    assert edited_button["interactive"] is False
    assert message == "Correct the acceptance JSON before approving."


def test_review_panel_shows_python_tests_and_provisional_summary(system, monkeypatch):
    """Verify review panel shows python tests and provisional summary."""
    pending = dict(
        request_id="review-1",
        owner_id=system.security.owner_id,
        filepath="Acceptance cases",
        action="review_acceptance",
        content='{"version":1}',
        review_context={"python_tests": "<script>bad()</script>", "summary": "Review inputs"},
    )
    monkeypatch.setattr(system.security, "get_pending_request", lambda: pending)
    snapshot = system.app.poll_with_request()
    assert "Human acceptance review" in snapshot[2]
    assert "Review inputs" in snapshot[2]
    assert "&lt;script&gt;" in snapshot[2] and "<script>" not in snapshot[2]
    assert snapshot[3]["value"] == '{"version":1}'
    assert snapshot[-1] == "review-1"


def test_validation_status_uses_owned_evaluator_and_escapes_values(system):
    """Verify validation status uses owned evaluator and escapes values."""
    system.app.validation = SimpleNamespace(
        status=lambda: {
            "stage": "verified",
            "tool": "adder",
            "contract_digest": "abcd",
            "cases": [{"id": "<unsafe>", "passed": True}],
        }
    )
    rendered = system.app.validation_status()
    assert "Verified against approved cases" in rendered
    assert "abcd" not in rendered and "SHA-256" not in rendered
    assert "&lt;unsafe&gt;" in rendered
    assert system.app.validation.status()["contract_digest"] == "abcd"


def test_final_status_shows_expected_and_observed_data(system):
    """Verify final status shows expected and observed data."""
    system.app.validation = SimpleNamespace(
        status=lambda: {
            "stage": "failed",
            "tool": "adder",
            "cases": [
                {
                    "id": "sum",
                    "passed": False,
                    "expected": {"kind": "value", "value": "<expected>"},
                    "observed": {"kind": "observation", "status": "returned", "value": 99},
                }
            ],
        }
    )
    rendered = system.app.validation_status()
    assert "&lt;expected&gt;" in rendered and "99" in rendered
