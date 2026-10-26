"""Show human-review context without treating generated source as markup."""

from types import SimpleNamespace


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
