"""LIVE-FLOW-002: advance only on fresh approved artifacts, never model prose."""

from types import SimpleNamespace

import pytest


def install_backend(system, monkeypatch, actions):
    """Replace only model execution; use real storage/approval/receipt boundaries."""
    seen = []
    system.security.auto_approve = True

    def crew(**kwargs):
        """Provide crew for the enclosing trusted test fixture."""

        def kickoff():
            """Provide kickoff for the enclosing trusted test fixture."""
            task = kwargs["tasks"][0]
            seen.append(task.description)
            actions[len(seen) - 1](task)
            return "Model completion claim"

        return SimpleNamespace(kickoff=kickoff)

    monkeypatch.setattr(system.main, "Crew", crew)
    return seen


def save(system, suffix, text):
    """Provide save for the enclosing trusted test fixture."""
    assert system.security.safe_write_file("adder", f"adder_{suffix}", text).startswith("Success:")


def test_missing_specification_stops_before_coder(system, monkeypatch):
    """Verify missing specification stops before coder."""
    seen = install_backend(system, monkeypatch, [lambda task: None])
    result = system.main.build_tool_pipeline("adder", "reject booleans")
    assert "PIPELINE_STAGE_FAILED: specification" in result
    assert len(seen) == 1


def test_missing_code_stops_before_tester(system, monkeypatch):
    """Verify missing code stops before tester."""
    seen = install_backend(
        system,
        monkeypatch,
        [lambda task: save(system, "specifications.md", "Approved spec"), lambda task: None],
    )
    result = system.main.build_tool_pipeline("adder", "original requirement")
    assert "PIPELINE_STAGE_FAILED: code" in result
    assert len(seen) == 2


@pytest.mark.parametrize("untrusted_file", [False, True])
def test_existing_or_unapproved_artifact_cannot_complete_stage(system, monkeypatch, untrusted_file):
    """Verify existing or unapproved artifact cannot complete stage."""
    if untrusted_file:
        folder = system.root / "adder"
        folder.mkdir(parents=True)
        (folder / "adder_specifications.md").write_text("unapproved", encoding="utf-8")
    else:
        system.security.auto_approve = True
        save(system, "specifications.md", "approved in an earlier stage")
    seen = install_backend(system, monkeypatch, [lambda task: None])
    assert "PIPELINE_STAGE_FAILED: specification" in system.main.build_tool_pipeline(
        "adder", "query"
    )
    assert len(seen) == 1


def test_stage_context_uses_saved_edits_instead_of_model_claim(system, monkeypatch):
    """Verify stage context uses saved edits instead of model claim."""
    original = "Reject bool and float; require exact integer results."
    seen = install_backend(
        system,
        monkeypatch,
        [
            lambda task: save(system, "specifications.md", "Human edited contract"),
            lambda task: save(system, "code.py", "def adder(kwh): return 3"),
            lambda task: None,
        ],
    )
    result = system.main.build_tool_pipeline("adder", original)
    assert len(seen) == 3
    assert all(original in description for description in seen)
    assert "Human edited contract" in seen[1] and "Human edited contract" in seen[2]
    assert "def adder(kwh): return 3" in seen[2]
    assert "PIPELINE_STAGE_FAILED: acceptance" in result


def test_changed_saved_bytes_cannot_complete_stage(system, monkeypatch):
    """Verify changed saved bytes cannot complete stage."""

    def tamper(task):
        """Provide tamper for the enclosing trusted test fixture."""
        save(system, "specifications.md", "approved")
        (system.root / "adder" / "adder_specifications.md").write_text("replaced", encoding="utf-8")

    seen = install_backend(system, monkeypatch, [tamper])
    assert "PIPELINE_STAGE_FAILED: specification" in system.main.build_tool_pipeline(
        "adder", "query"
    )
    assert len(seen) == 1


def test_receipt_cannot_adopt_an_intervening_unapproved_write(system, monkeypatch):
    """A concurrent replacement between save and observation must fail closed."""
    import builtins

    system.security.auto_approve = True
    actual_open = builtins.open
    replaced = []

    def intervening_open(path, mode="r", *args, **kwargs):
        """Provide intervening open for the enclosing trusted test fixture."""
        if mode == "rb" and str(path).endswith("adder_specifications.md") and not replaced:
            replaced.append(True)
            with actual_open(path, "wb") as output:
                output.write(b"intervening unapproved bytes")
        return actual_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", intervening_open)
    system.security.safe_write_file("adder", "adder_specifications.md", "approved")
    path = system.security.validate_and_resolve_path("adder", "adder_specifications.md")
    assert replaced
    assert system.security.get_artifact_receipt(path) is None


def test_current_owner_operation_and_fresh_save_are_required(system):
    """Verify current owner operation and fresh save are required."""
    system.security.auto_approve = True
    system.security.operation_id = "first"
    save(system, "specifications.md", "approved")
    path = system.security.validate_and_resolve_path("adder", "adder_specifications.md")
    first = system.security.get_artifact_receipt(path)
    system.security.operation_id = "second"
    assert system.security.get_artifact_receipt(path) is None
    save(system, "specifications.md", "approved")
    second = system.security.get_artifact_receipt(path)
    assert first is not None and second is not None and first != second
    system.security.cancel_pending()
    assert system.security.get_artifact_receipt(path) is None


@pytest.mark.parametrize("replace_code", [False, True])
def test_gated_pipeline_completes_with_real_acceptance_services(system, monkeypatch, replace_code):
    """Verify gated pipeline completes with real acceptance services."""
    import json

    from trusted_sandbox import approve_next_review

    def tester(task):
        """Provide tester for the enclosing trusted test fixture."""
        if replace_code:
            (system.root / "adder" / "adder_code.py").write_text(
                "def adder(kwh): return 3", encoding="utf-8"
            )
        result = system.custom_tools.run_and_save_tests_tool(
            "adder",
            "import unittest\nfrom adder_code import adder\nclass Checks(unittest.TestCase):\n def test_sum(self): self.assertEqual(adder(1), 3)\n",
        )
        assert result.startswith("TESTS_PROVISIONAL_PASSED:")
        thread, errors = approve_next_review(system.security)
        result = system.custom_tools.submit_acceptance_cases_tool(
            "adder",
            json.dumps(
                {
                    "version": 1,
                    "cases": [
                        {
                            "id": "sum",
                            "purpose": "Check return",
                            "function": "adder",
                            "kwargs": {"kwh": 1},
                            "expect": {"kind": "value", "value": 3},
                        }
                    ],
                }
            ),
        )
        thread.join(3)
        assert not errors and result.startswith("ACCEPTANCE_VERIFIED:")

    seen = install_backend(
        system,
        monkeypatch,
        [
            lambda task: save(system, "specifications.md", "Approved spec"),
            lambda task: save(system, "code.py", "def adder(kwh): return kwh + 2"),
            tester,
        ],
    )
    result = system.main.build_tool_pipeline("adder", "Add two")
    assert result.startswith(
        "PIPELINE_STAGE_FAILED: acceptance" if replace_code else "ACCEPTANCE_VERIFIED:"
    )
    assert len(seen) == 3
