"""V7-048: update only reviewed maintained runtimes using independent fixtures."""

import json
import shutil
from pathlib import Path

import pytest
from test_catalog_migration import migration_fixture
from test_code_application import make_code_candidate
from test_widget_reuse import Protector

from agentix.application.app_workflow import ApplicationSupervisor
from agentix.lab.application_artifacts import _identity
from agentix.security.approval_store import ApprovalStore, policy_fingerprint
from agentix.storage.catalog_migration import fingerprint
from agentix.storage.installed_apps import InstalledApps


def update_fixture(tmp_path: Path):
    """Represent a previously authenticated package with an obsolete maintained template."""
    from agentix.storage.application_update import ApplicationUpdates

    migration, source, target, tool = migration_fixture(tmp_path)
    migration.apply(migration.plan()["review_digest"])
    item = make_code_candidate(tmp_path / "authored")
    item.display_name = "Fixture application"
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True  # Past acceptance is a setup double, not the new verdict.
    library = InstalledApps(
        source / "data/applications", source / "data/approvals/applications", protector=Protector()
    )
    installed = library.publish(item)
    package = installed.package
    old = b"# Older reviewed maintained compositor.\n" + (package / "app.py").read_bytes()
    (package / "app.py").write_bytes(old)
    manifest_path = package / "application.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"]["app.py"] = fingerprint(old)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    layout = b'{"version":1,"positions":{"application_input_amount":{"x":12,"y":20,"width":250,"height":80}}}'
    (package / "config.json").write_bytes(layout)
    record_path = library._record(installed.id)
    record = json.loads(Protector().unseal(record_path.read_bytes()))
    record["digest"] = _identity(
        tuple(
            (name, (package / name).read_bytes())
            for name in sorted(set(manifest["files"]) | {"application.json"})
        )
    )
    review_path = source / "data/reviews" / installed.id / "review.json"
    review = json.loads(review_path.read_bytes())
    review["manifest"] = manifest
    review["source_files"]["app.py"] = old.decode()
    review_path.write_text(json.dumps(review), encoding="utf-8")
    record["review"] = fingerprint(review_path.read_bytes())
    record_path.write_bytes(Protector().seal(json.dumps(record).encode()))
    for area in ("applications", "reviews", "approvals/applications"):
        shutil.copytree(source / "data" / area, target / "data" / area)
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
    service = ApplicationUpdates(migration)
    return (
        service,
        migration,
        installed.id,
        target / "data/applications/fixture-application",
        layout,
    )


def test_reviewed_update_preserves_logic_layout_and_source(tmp_path: Path) -> None:
    """Only the maintained app template and bound metadata may change after fresh gates."""
    from agentix.application.code_package import runtime_template

    service, migration, identity, package, layout = update_fixture(tmp_path)
    before = {p: p.read_bytes() for p in migration.source.rglob("*") if p.is_file()}
    logic = (package / "application_logic.py").read_bytes()
    plan = service.plan(["fixture-application"])
    assert plan["items"][0]["status"] == "ready"
    assert plan["items"][0]["changed_runtime_files"] == ["app.py"]
    calls = []

    def verified(staged, review, evidence):
        """Stand in for real native/browser verification of the exact reviewed candidate."""
        assert (staged / "app.py").read_bytes() == runtime_template("app.py").read_bytes()
        assert review["independent_acceptance"]["expected"] == {"first": 5, "second": 8}
        calls.append(staged)
        return True

    report = service.apply(["fixture-application"], plan["review_digest"], verifier=verified)
    assert report["items"][0]["status"] == "updated"
    assert len(calls) == 1
    assert (package / "application_logic.py").read_bytes() == logic
    assert (package / "config.json").read_bytes() == layout
    assert all(p.read_bytes() == data for p, data in before.items())
    library = InstalledApps(
        migration.target / "data/applications",
        migration.target / "data/approvals/applications",
        protector=Protector(),
    )
    assert library.get(identity).dependencies["calculator"]["contract_digest"] == "b" * 64
    assert service.plan(["fixture-application"])["items"][0]["status"] == "preserved"


@pytest.mark.parametrize("changed", ["application_logic.py", "review.json", "operation.py"])
def test_unauthorized_changed_bytes_are_blocked(tmp_path: Path, changed: str) -> None:
    """Runtime refresh cannot legitimize changed generated logic or acceptance data."""
    service, migration, identity, package, _ = update_fixture(tmp_path)
    path = (
        migration.target / "data/reviews" / identity / changed
        if changed == "review.json"
        else package / changed
    )
    path.write_bytes(path.read_bytes() + b"changed")
    assert service.plan(["fixture-application"])["items"][0]["status"] == "blocked"


@pytest.mark.parametrize("verdict", [False, "drift"])
def test_failed_or_changed_verification_keeps_installed_bytes(tmp_path: Path, verdict) -> None:
    """A failed gate or changed staging package must never activate an application."""
    service, migration, identity, package, _ = update_fixture(tmp_path)
    before = {p.name: p.read_bytes() for p in package.iterdir() if p.is_file()}
    plan = service.plan(["fixture-application"])

    def verify(staged, review, evidence):
        """Inject denial or post-verification drift, without executing any fixture source."""
        if verdict == "drift":
            (staged / "application_logic.py").write_bytes(b"changed")
            return True
        return False

    result = service.apply(["fixture-application"], plan["review_digest"], verifier=verify)
    assert result["items"][0]["status"] == "blocked"
    assert {p.name: p.read_bytes() for p in package.iterdir() if p.is_file()} == before
    assert (
        InstalledApps(
            migration.target / "data/applications",
            migration.target / "data/approvals/applications",
            protector=Protector(),
        ).list()
        == []
    )


def test_stale_plan_and_missing_dependency_cannot_activate(tmp_path: Path) -> None:
    """Reject new edits and absent tools rather than rewriting their approval hashes."""
    service, migration, _, package, _ = update_fixture(tmp_path)
    plan = service.plan(["fixture-application"])
    (package / "config.json").write_bytes(b'{"positions":{}}')
    with pytest.raises(ValueError, match="review"):
        service.apply(["fixture-application"], plan["review_digest"], verifier=lambda *args: True)
    (migration.tools / "calculator/calculator_code.py").unlink()
    assert service.plan(["fixture-application"])["items"][0]["status"] == "blocked"


def test_partial_review_write_failure_restores_installed_state(tmp_path: Path, monkeypatch) -> None:
    """Ordinary commit errors restore even the file whose write failed partway."""
    service, migration, identity, package, _ = update_fixture(tmp_path)
    review_path = migration.target / "data/reviews" / identity / "review.json"
    old_review = review_path.read_bytes()
    old_package = {p.name: p.read_bytes() for p in package.iterdir() if p.is_file()}
    plan = service.plan(["fixture-application"])
    original_write = Path.write_bytes
    failed = []

    def interrupted(path, body):
        """Simulate one partial disk write and allow subsequent rollback writes."""
        if path == review_path and not failed:
            failed.append(True)
            original_write(path, body[:10])
            raise OSError("fixture interrupted write")
        return original_write(path, body)

    monkeypatch.setattr(Path, "write_bytes", interrupted)
    result = service.apply(
        ["fixture-application"], plan["review_digest"], verifier=lambda *args: True
    )
    assert result["items"][0]["status"] == "blocked"
    assert review_path.read_bytes() == old_review
    assert {p.name: p.read_bytes() for p in package.iterdir() if p.is_file()} == old_package
