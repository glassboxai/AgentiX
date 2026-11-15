"""V7-047: authenticated relocation uses authored fixtures, never user artifacts."""

import json
import shutil
from pathlib import Path
from types import SimpleNamespace

import pytest
from test_application_crews import approved_tool
from test_general_application_pipeline import WIDGET
from test_widget_reuse import Protector

from agentix.security.approval_store import ApprovalStore, policy_fingerprint
from agentix.storage.widget_store import WidgetStore


def migration_fixture(tmp_path: Path):
    """Build source grants and copied bytes under independent temporary roots."""
    from agentix.storage.catalog_migration import CatalogMigration

    source, target = tmp_path / "old", tmp_path / "new"
    tools = source / "data/tools"
    tool = approved_tool()
    folder = tools / tool.tool_name
    folder.mkdir(parents=True)
    (folder / "calculator_code.py").write_bytes(tool.code)
    (folder / "calculator_tests.py").write_bytes(tool.tests)
    grant = ApprovalStore(
        source / "data/approvals/tools", tools, protector=Protector(), policy=policy_fingerprint()
    )
    contract = {
        "version": 1,
        "cases": [
            dict(case, id="sum", purpose="Known sum") for case in tool.reviewed_contract["cases"]
        ],
    }
    grant.save(
        "calculator",
        tool.code,
        tool.tests,
        tool.contract_digest,
        frozenset({"calculator"}),
        contract,
    )
    widgets = WidgetStore(
        SimpleNamespace(TOOLS_ROOT_DIR=str(tools)),
        source / "data/approvals/widgets",
        protector=Protector(),
    )
    # Publication is a fixture setup double for previous human/native acceptance.
    from agentix.security.paths import resolve_artifact_path

    widgets.security.validate_and_resolve_path = lambda name, file: resolve_artifact_path(
        str(tools), name, file
    )
    widgets.publish(tool, {"widget_code": WIDGET, "tests_code": "# reviewed", "notes": "fixture"})
    shutil.copytree(source, target)
    service = CatalogMigration(source, tools, target, protector=Protector())
    return service, source, target, tool


def test_readonly_plan_and_reviewed_relocation(tmp_path: Path) -> None:
    """A reviewed exact plan makes both grants reusable without changing source."""
    service, source, target, tool = migration_fixture(tmp_path)
    before = {p: p.read_bytes() for p in source.rglob("*") if p.is_file()}
    plan = service.plan()
    assert [(i["kind"], i["status"]) for i in plan["items"]] == [
        ("tools", "ready"),
        ("widgets", "ready"),
    ]
    assert not (target / "migrations").exists()
    with pytest.raises(ValueError, match="review"):
        service.apply("wrong")
    report = service.apply(plan["review_digest"])
    assert all(i["status"] == "migrated" for i in report["items"])
    fresh = ApprovalStore(
        target / "data/approvals/tools",
        target / "data/tools",
        protector=Protector(),
        policy=policy_fingerprint(),
    )
    assert fresh.load("calculator", tool.code, tool.tests) is not None
    assert all(p.read_bytes() == value for p, value in before.items())
    assert all(i["status"] == "preserved" for i in service.plan()["items"])


@pytest.mark.parametrize("change", ["code", "tests", "widget", "css", "unsigned", "policy"])
def test_changed_or_unauthenticated_bytes_never_migrate(tmp_path: Path, change: str) -> None:
    """Corruption and policy drift stay blocked; no target grant is minted."""
    service, source, target, _ = migration_fixture(tmp_path)
    if change == "unsigned":
        path = next((source / "data/approvals/tools").rglob("*.approval"))
        path.write_bytes(b"unsigned")
    elif change == "policy":
        path = next((source / "data/approvals/tools").rglob("*.approval"))
        record = json.loads(Protector().unseal(path.read_bytes()))
        record["policy"] = "old-policy"
        path.write_bytes(Protector().seal(json.dumps(record).encode()))
    else:
        suffix = {
            "code": "_code.py",
            "tests": "_tests.py",
            "widget": "_widget.py",
            "css": "_widget.css",
        }[change]
        (target / "data/tools/calculator" / ("calculator" + suffix)).write_bytes(b"changed")
    plan = service.plan()
    assert any(i["status"] == "blocked" for i in plan["items"])
    report = service.apply(plan["review_digest"])
    assert any(i["status"] == "blocked" for i in report["items"])


def test_stale_review_and_destination_conflict_are_preserved(tmp_path: Path) -> None:
    """No operation overwrites a new destination grant or uses a stale review."""
    service, _, target, _ = migration_fixture(tmp_path)
    plan = service.plan()
    (target / "data/tools/calculator/calculator_tests.py").write_bytes(b"new review")
    with pytest.raises(ValueError, match="review"):
        service.apply(plan["review_digest"])
    assert not (target / "migrations").exists()


def test_application_record_requires_native_browser_verdict(tmp_path: Path) -> None:
    """A protected prior review alone never marks an app verified for v7."""
    from test_code_application import make_code_candidate

    from agentix.application.app_workflow import ApplicationSupervisor
    from agentix.storage.installed_apps import InstalledApps

    service, source, target, _ = migration_fixture(tmp_path)
    item = make_code_candidate(tmp_path / "authored")
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True  # Setup double only; migration must obtain a fresh verdict.
    library = InstalledApps(
        source / "data/applications", source / "data/approvals/applications", protector=Protector()
    )
    library.publish(item)
    shutil.copytree(source / "data/applications", target / "data/applications")
    shutil.copytree(source / "data/reviews", target / "data/reviews")
    shutil.copytree(source / "data/approvals/applications", target / "data/approvals/applications")
    plan = service.plan()
    assert next(i for i in plan["items"] if i["kind"] == "applications")["status"] == "ready"
    report = service.apply(plan["review_digest"])
    result = next(i for i in report["items"] if i["kind"] == "applications")
    assert result["status"] == "blocked"
    assert "verification is required" in result["reason"]
    assert (
        InstalledApps(
            target / "data/applications",
            target / "data/approvals/applications",
            protector=Protector(),
        ).list()
        == []
    )

    calls = []

    def verified(package, review, evidence):
        """Stand in for the explicit native/browser boundary, never model execution."""
        assert review["independent_acceptance"]["expected"] == {"first": 5, "second": 8}
        calls.append(package)
        return True

    service.verifier = verified
    report = service.apply(service.plan()["review_digest"])
    assert len(calls) == 1
    assert next(i for i in report["items"] if i["kind"] == "applications")["status"] == "migrated"
    assert (
        len(
            InstalledApps(
                target / "data/applications",
                target / "data/approvals/applications",
                protector=Protector(),
            ).list()
        )
        == 1
    )


def test_changed_reviewed_cases_require_widget_revalidation(tmp_path: Path) -> None:
    """Current tool approval survives; an older widget binding needs fresh gates."""
    service, _, target, tool = migration_fixture(tmp_path)
    grant = ApprovalStore(
        target / "data/approvals/tools",
        target / "data/tools",
        protector=Protector(),
        policy=policy_fingerprint(),
    )
    contract = {
        "version": 1,
        "cases": [
            dict(case, id="sum", purpose="Known sum") for case in tool.reviewed_contract["cases"]
        ],
    }
    grant.save("calculator", tool.code, tool.tests, "b" * 64, frozenset({"calculator"}), contract)
    plan = service.plan()
    assert plan["items"][0]["status"] == "preserved"
    assert plan["items"][1]["reverify_widget"] is True
    report = service.apply(plan["review_digest"])
    assert report["items"][1]["status"] == "blocked"
    calls = []

    def verify(current, proposal, css, evidence):
        """Record the exact current contract behind a native/browser test double."""
        calls.append(current.contract_digest)
        return True

    service.widget_verifier = verify
    report = service.apply(service.plan()["review_digest"])
    assert calls == ["b" * 64]
    assert report["items"][1]["status"] == "migrated"
    assert grant.load("calculator", tool.code, tool.tests)["digest"] == "b" * 64


def test_verifier_drift_cannot_mint_widget_grant(tmp_path: Path) -> None:
    """A successful child claim cannot conceal bytes changed during native checks."""
    service, source, target, _ = migration_fixture(tmp_path)
    path = next((source / "data/approvals/widgets").rglob("*.approval"))
    record = json.loads(Protector().unseal(path.read_bytes()))
    record["binding"]["contract"] = "previous-review"
    path.write_bytes(Protector().seal(json.dumps(record).encode()))

    def drift(*args):
        """Simulate an untrusted concurrent edit after a nominal verification result."""
        (target / "data/tools/calculator/calculator_widget.py").write_bytes(b"changed")
        return True

    service.widget_verifier = drift
    report = service.apply(service.plan()["review_digest"])
    assert report["items"][1]["status"] == "blocked"
    assert "stale" in report["items"][1]["reason"]
    assert service.plan()["items"][1]["status"] == "blocked"


def test_conflicting_widget_approval_is_never_overwritten(tmp_path: Path) -> None:
    """Preserve destination records even when their contents cannot be authenticated."""
    service, _, target, _ = migration_fixture(tmp_path)
    path = service._path(target, "widgets", target / "data/tools", "calculator")
    path.parent.mkdir(parents=True)
    path.write_bytes(b"retained-conflict")
    plan = service.plan()
    assert plan["items"][1]["status"] == "blocked"
    service.apply(plan["review_digest"])
    assert path.read_bytes() == b"retained-conflict"


def test_hardlinked_input_is_blocked(tmp_path: Path) -> None:
    """Do not relocate approvals over a Windows hard-link alias."""
    service, _, target, _ = migration_fixture(tmp_path)
    source = target / "data/tools/calculator/calculator_code.py"
    alias = tmp_path / "alias.py"
    alias.hardlink_to(source)
    assert service.plan()["items"][0]["status"] == "blocked"


@pytest.mark.windows_isolation
@pytest.mark.browser
def test_real_widget_migration_checks_reviewed_value(tmp_path: Path, monkeypatch) -> None:
    """Native/browser gates exercise authored widget fixtures without a real model."""
    from tools.migrate_catalog import verify_widget

    service, _, target, tool = migration_fixture(tmp_path)
    monkeypatch.setenv("AGENTIX_HOME", str(target))
    evidence = tmp_path / "native-evidence"
    evidence.mkdir()
    assert verify_widget(
        tool,
        {
            "widget_code": WIDGET,
            "tests_code": "\n".join(
                [
                    '"""Trusted widget interface test."""',
                    "import unittest",
                    "from types import SimpleNamespace",
                    "import gradio as gr",
                    "from calculator_widget import create_widget",
                    "class WidgetTest(unittest.TestCase):",
                    '    """Check maintained widget interface with a fixture context."""',
                    "    def test_references(self):",
                    '        """Return expected component references."""',
                    '        context = SimpleNamespace(elem_id=lambda role: "fixture_"+role, api_name="fixture")',
                    "        with gr.Blocks():",
                    "            refs = create_widget(context)",
                    '        self.assertEqual(set(refs["inputs"]), {"a", "b"})',
                    '        self.assertTrue(callable(refs["render"]))',
                ]
            ),
            "notes": "trusted fixture",
        },
        "",
        evidence,
    )


def test_native_failure_is_reported_without_a_grant(tmp_path: Path) -> None:
    """Native startup/test errors retain a receipt and cannot mint widget approval."""
    service, source, _, _ = migration_fixture(tmp_path)
    path = next((source / "data/approvals/widgets").rglob("*.approval"))
    record = json.loads(Protector().unseal(path.read_bytes()))
    record["binding"]["contract"] = "previous-review"
    path.write_bytes(Protector().seal(json.dumps(record).encode()))

    def failed(*args):
        """Represent a native failure without starting a process in offline tests."""
        raise RuntimeError("fixture native failure")

    service.widget_verifier = failed
    report = service.apply(service.plan()["review_digest"])
    assert report["items"][1]["status"] == "blocked"
    assert (Path(report["evidence"]) / "receipt.json").is_file()
    assert service.plan()["items"][1]["status"] == "ready"


@pytest.mark.parametrize("observed_type, passes", [("ValueError", True), ("TypeError", False)])
def test_exception_cases_are_compared_outside_child(
    tmp_path: Path, observed_type: str, passes: bool
) -> None:
    """Never discard reviewed exception cases or give expected values to the child."""
    from dataclasses import replace

    from tools.migrate_catalog import verify_exception_cases

    case = {
        "function": "calculator",
        "id": "invalid",
        "kwargs": {"a": 1, "b": 0},
        "expect": {"kind": "raises", "type": "ValueError"},
    }
    tool = replace(approved_tool(), reviewed_contract={"cases": [case]})
    calls = []

    def evaluate(code, name, function, kwargs):
        """Observe a native boundary double that receives inputs only."""
        calls.append((name, function, kwargs))
        return SimpleNamespace(
            isolated=True,
            exit_code=0,
            failure="",
            report={"kind": "observation", "status": "raised", "exception_type": observed_type},
        )

    if passes:
        verify_exception_cases(tool, tmp_path, evaluate=evaluate)
        assert (tmp_path / "exception-cases.json").is_file()
    else:
        with pytest.raises(ValueError, match="exception case"):
            verify_exception_cases(tool, tmp_path, evaluate=evaluate)
    assert calls == [("calculator", "calculator", {"a": 1, "b": 0})]


def test_empty_destination_tool_record_does_not_restore_old_grant(tmp_path: Path) -> None:
    """An explicit corrupt destination record must not fall back to source trust."""
    service, _, target, _ = migration_fixture(tmp_path)
    path = service._path(target, "tools", target / "data/tools", "calculator")
    path.parent.mkdir(parents=True)
    path.write_bytes(b"")
    plan = service.plan()
    assert plan["items"][0]["status"] == "blocked"
    assert plan["items"][1]["status"] == "blocked"
    assert path.read_bytes() == b""
