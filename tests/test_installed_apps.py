"""Persistent application catalog tests use reviewed maintained fixtures only."""

import json

import pytest
from schema3_package import widget_source
from test_application_supervisor import candidate
from test_widget_reuse import Protector

from agentix.application.app_workflow import ApplicationSupervisor


def library(tmp_path):
    """Inject authenticated fixture protection instead of claiming Windows execution."""
    from agentix.storage.installed_apps import InstalledApps

    return InstalledApps(tmp_path / "installed", tmp_path / "records", protector=Protector())


def verified(tmp_path):
    """Publish a trusted fixture verification boundary, not a model-supplied claim."""
    item = candidate(tmp_path / "draft")
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    item.review_text = json.dumps(
        {
            "original_request": "Count words and vowels",
            "approved_catalog_dependencies": {},
            "proposed_tests_and_notes": {"widgets": {}},
            "independent_acceptance": [],
        }
    )
    return item


def test_only_verified_apps_can_be_installed_and_loaded_after_restart(tmp_path):
    """A durable catalog must neither list drafts nor depend on their old session."""
    item = verified(tmp_path)
    service = library(tmp_path)
    item.verified = False
    with pytest.raises(ValueError):
        service.publish(item)
    item.verified = True
    record = service.publish(item)
    assert record.name and record.id
    fresh = library(tmp_path)
    assert [app.id for app in fresh.list()] == [record.id]
    loaded = fresh.get(record.id)
    assert loaded.digest == item.digest and loaded.package != item.package
    assert (loaded.package / "config.json").is_file()


def test_source_tampering_invalidates_catalog_approval(tmp_path):
    """A JSON manifest or old receipt cannot approve changed executable bytes."""
    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    (app.package / "app.py").write_text("changed", encoding="utf-8")
    with pytest.raises(ValueError):
        service.get(app.id)
    assert service.list() == []


def test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code(tmp_path):
    """Presentation config is bounded data and separate from executable identity."""
    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    layout = {
        "version": 1,
        "positions": {
            "application_count_words_in_text_input": {"x": 10, "y": 20, "width": 300, "height": 100}
        },
    }
    service.save_layout(app.id, layout)
    assert library(tmp_path).get(app.id).digest == app.digest
    assert service.read_layout(app.id) == layout
    with pytest.raises(ValueError):
        service.save_layout(
            app.id,
            {
                "version": 1,
                "positions": {"../../outside": {"x": 0, "y": 0, "width": 1, "height": 1}},
            },
        )
    with pytest.raises(ValueError):
        service.get("../outside")


def test_manager_application_decision_uses_only_a_catalog_id_and_typed_text():
    """Reject path/function injection instead of treating an app request as tool creation."""
    from agentix.decisions import RunApplicationDecision, parse_manager_response

    identity = "a" * 32
    result = parse_manager_response(
        json.dumps(
            {"action": "RUN_APPLICATION", "app_id": identity, "arguments": {"text": "Hello World!"}}
        )
    )
    assert isinstance(result, RunApplicationDecision)
    assert result.app_id == identity and result.arguments == {"text": "Hello World!"}
    for app_id, arguments in [
        ("../app", {"text": "x"}),
        (identity, {"text": False}),
        (identity, {"text": "x", "function": "exec"}),
    ]:
        with pytest.raises(ValueError):
            parse_manager_response(
                json.dumps({"action": "RUN_APPLICATION", "app_id": app_id, "arguments": arguments})
            )


def published_with_tools(tmp_path):
    """Construct a verified catalog fixture with exact installed tool dependency hashes."""
    from test_application_catalog import installed, registry

    from agentix.application.app_workflow import ApplicationPipeline

    root = tmp_path / "tools"
    root.mkdir()
    fixture = installed(root)
    tools = registry(fixture).resolve()

    def factory(folder):
        """Supply trusted widget/workflow fixtures without model inference."""

        def client(role, content):
            """Return reviewed test data, never execute its source on the host."""
            if role == "General Widget Designer":
                module = content["requirements"]["approved_tool_contract"]["module"]
                return {
                    "widget_code": widget_source(module),
                    "tests_code": "",
                    "notes": "fixture",
                }
            catalog = content["requirements"]["approved_catalog"]
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [{"id": name, "tool": name} for name in sorted(catalog)],
                "connection_code": (
                    '"""Connect approved catalog calls."""\n'
                    "def run(payload: dict, call) -> None:\n"
                    '    """Call every approved tool with the shared text input."""\n'
                    + "".join(
                        f'    call("{name}", text=payload["text"])\n' for name in sorted(catalog)
                    )
                ),
                "notes": "fixture",
            }

        return client

    item = ApplicationPipeline(tmp_path / "drafts", factory).generate(
        "Count words and vowels", tools=tools
    )
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    service = library(tmp_path)
    return service, service.publish(item), fixture


def test_library_load_does_not_generate_or_execute_code(tmp_path):
    """Loading a verified app restores a draft snapshot without model/test calls."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: service)
    rows = list(backend.load_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    assert rows[-1][0] == (
        "Loaded "
        + app.name
        + ". Review the restored code here; press Play selected app to start it in the "
        "sandbox, or Run data operation to call it without opening its interface. "
        "Previous tests are not repeated."
    )
    _, state = backend._resolve(owner.token, SimpleNamespace(session_hash="alice"))
    assert state.candidate.verified and state.candidate.catalog_id == app.id
    assert state.candidate.package != app.package
    assert not owner.controller.state.application_review_pending


def test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required(tmp_path):
    """Discovery retains a protected app while loading still enforces tool approvals."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    fixture.ledger._reuse.clear()
    backend = ApplicationsBackend(sessions, library_factory=lambda: service)
    request = SimpleNamespace(session_hash="alice")

    choices, _ = backend.catalog_entries(owner.token, request)
    assert choices == [(app.name, app.id)]
    rows = list(backend.load_app(app.id, owner.token, request))
    assert "Application load failed" in rows[-1][0]


def test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies(tmp_path):
    """A manager-selected app calls the injected native boundary without model/test work."""
    from test_application_catalog import registry

    from agentix.application.app_invocation import AppInvocation

    service, app, fixture = published_with_tools(tmp_path)
    calls = []

    def native(snapshot, payload):
        """Record only the trusted boundary contract, not child semantic proof."""
        calls.append((snapshot.digest, payload))
        return {"count_words_in_text": 2, "count_vowels_in_text": 3}

    invocation = AppInvocation(service, registry(fixture), native=native)
    assert invocation.catalog()[0]["id"] == app.id
    assert invocation.candidates() == [
        {"id": app.id, "name": app.name, "description": app.description}
    ]
    assert invocation.execute(app.id, {"text": "Hello World!"}) == {
        "count_words_in_text": 2,
        "count_vowels_in_text": 3,
    }
    assert calls == [(app.digest, {"text": "Hello World!"})]
    fixture.ledger._reuse.pop("count_words_in_text")
    assert invocation.catalog() == []
    assert invocation.candidates() == []
    with pytest.raises(ValueError):
        invocation.execute(app.id, {"text": "Hello World!"})
    assert len(calls) == 1


def test_invocation_rejects_tool_changes_during_native_execution(tmp_path):
    """A result is not accepted after a dependency changes while the child runs."""
    from test_application_catalog import registry

    from agentix.application.app_invocation import AppInvocation

    service, app, fixture = published_with_tools(tmp_path)

    def native(snapshot, payload):
        """Simulate an external edit during an otherwise successful computation."""
        fixture.ledger._reuse.pop("count_words_in_text")
        return {"count_words_in_text": 2, "count_vowels_in_text": 3}

    with pytest.raises(ValueError):
        AppInvocation(service, registry(fixture), native=native).execute(
            app.id, {"text": "Hello World!"}
        )


def test_publishing_reviewed_revision_preserves_valid_presentation_config(tmp_path):
    """A code revision may require new approval without discarding the user's layout."""
    item = verified(tmp_path)
    layout = {
        "version": 1,
        "positions": {"application_input_text": {"x": 20, "y": 30, "width": 400, "height": 90}},
    }
    (item.package / "config.json").write_text(json.dumps(layout), encoding="utf-8")
    service = library(tmp_path)
    app = service.publish(item)
    assert service.read_layout(app.id) == layout


def test_name_availability_reflects_existing_install_folder(tmp_path):
    """Publication reserves the display-name folder; availability must report it."""
    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    assert not service.name_available(app.name)
    assert service.name_available("Another application")


def test_catalog_removal_service_is_outside_the_execution_policy(tmp_path, monkeypatch):
    """V7-061: fixing removal must not invalidate every installed application."""
    import importlib
    import shutil
    from pathlib import Path

    checkout = Path(__file__).resolve().parents[1]
    shutil.copytree(
        checkout / "src", tmp_path / "src", ignore=shutil.ignore_patterns("__pycache__")
    )
    (tmp_path / "infra").mkdir()
    shutil.copyfile(checkout / "infra/runtime.lock.txt", tmp_path / "infra/runtime.lock.txt")
    target = importlib.import_module("agentix.storage.installed_apps")
    relative = Path(target.__file__).relative_to(checkout)
    monkeypatch.setattr(target, "__file__", str(tmp_path / relative))
    before = target.app_policy()
    removal = tmp_path / "src/agentix/storage/maintenance.py"
    removal.write_bytes(removal.read_bytes() + b"\n# changed removal service\n")
    assert target.app_policy() == before
    boundary = tmp_path / "src/agentix/domain/application_code.py"
    boundary.write_bytes(boundary.read_bytes() + b"\n# changed execution boundary\n")
    assert target.app_policy() != before


def stale_library(tmp_path, monkeypatch):
    """Publish under one policy, then reopen the same storage under a changed policy."""
    service = library(tmp_path)
    app = service.publish(verified(tmp_path / "first"))
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    return library(tmp_path), app


def test_rejected_record_logs_identity_and_one_summary(tmp_path, monkeypatch, caplog):
    """A rejection warning must name the application and not repeat per refresh."""
    import logging

    service, app = stale_library(tmp_path, monkeypatch)
    with caplog.at_level(logging.INFO, logger="agentix.storage.installed_apps"):
        entries = service.entries()
    assert [entry.status for entry in entries] == ["approval_stale"]
    rejected = [
        record for record in caplog.records if "installed_app_rejected" in record.getMessage()
    ]
    assert len(rejected) == 1
    assert "app_id=" + app.id in rejected[0].getMessage()
    assert app.name in rejected[0].getMessage()
    summary = [
        record for record in caplog.records if "installed_apps_listed" in record.getMessage()
    ]
    assert len(summary) == 1
    assert "rejected=1" in summary[0].getMessage()


def test_catalog_keeps_stale_app_visible_without_granting_it(tmp_path, monkeypatch):
    """Discovery retains a stale record while get() still refuses to authorize it."""
    service, app = stale_library(tmp_path, monkeypatch)
    entries = service.entries()
    assert [(entry.id, entry.name, entry.status) for entry in entries] == [
        (app.id, app.name, "approval_stale")
    ]
    assert entries[0].app is None
    assert service.list() == []
    with pytest.raises(ValueError):
        service.get(app.id)


def test_stale_load_returns_exact_installed_bytes_without_policy_grant(tmp_path, monkeypatch):
    """Re-approval needs the installed bytes even when the host policy changed."""
    service, app = stale_library(tmp_path, monkeypatch)
    stale = service.load_stale(app.id)
    assert stale.id == app.id and stale.digest == app.digest
    assert stale.package == app.package
    assert stale.review == app.review


def test_reseal_replaces_only_the_policy_binding_atomically(tmp_path, monkeypatch):
    """Re-sealing must keep package and review bytes and leave no partial record."""
    from agentix.lab.application_artifacts import application_digest

    service, app = stale_library(tmp_path, monkeypatch)
    before = application_digest(app.package)
    resealed = service.reseal(app.id)
    assert resealed.id == app.id and resealed.digest == app.digest
    assert application_digest(app.package) == before
    assert library(tmp_path).get(app.id).digest == app.digest
    assert not list((tmp_path / "records").rglob(".approval-*"))


def test_reseal_refuses_changed_source(tmp_path, monkeypatch):
    """A stale policy never authorizes bytes that changed after installation."""
    service, app = stale_library(tmp_path, monkeypatch)
    (app.package / "app.py").write_text("changed", encoding="utf-8")
    with pytest.raises(ValueError):
        service.reseal(app.id)
    assert [entry.status for entry in service.entries()] == ["source_changed"]


def test_maintained_runtime_drift_is_reported_apart_from_changed_source(tmp_path, monkeypatch):
    """A moved maintained template must not be reported as tampered application source."""
    from agentix.application import general_package

    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    original = general_package.runtime_template
    changed = tmp_path / "application_context.py"
    changed.write_bytes(original("application_context.py").read_bytes() + b"\n# moved\n")
    monkeypatch.setattr(
        general_package,
        "runtime_template",
        lambda name: changed if name == "application_context.py" else original(name),
    )
    entries = service.entries()
    assert [entry.status for entry in entries] == ["runtime_changed"]
    assert entries[0].reason == "Installed application maintained runtime changed"
    with pytest.raises(ValueError, match="maintained runtime"):
        service.load_stale(app.id)


def test_runtime_refresh_loads_installed_bytes_with_current_runtime(tmp_path, monkeypatch):
    """An explicit refresh keeps application bytes and replaces only runtime members."""
    from agentix.application import general_package
    from agentix.lab.application_artifacts import approve_application

    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    original = general_package.runtime_template
    changed = tmp_path / "application_context.py"
    moved = original("application_context.py").read_bytes() + b"\n# moved\n"
    changed.write_bytes(moved)
    monkeypatch.setattr(
        general_package,
        "runtime_template",
        lambda name: changed if name == "application_context.py" else original(name),
    )
    refreshed = service.load_for_runtime_refresh(app.id)
    assert refreshed.digest == app.digest and refreshed.package == app.package
    assert service.read_layout(app.id, allow_runtime_drift=True)["version"] == 1
    with pytest.raises(ValueError, match="maintained runtime"):
        service.read_layout(app.id)
    snapshot = approve_application(app.package, app.digest, allow_runtime_drift=True)
    files = dict(snapshot.files)
    assert snapshot.digest != app.digest
    assert files["application_context.py"] == moved
    assert files["app.py"] == (app.package / "app.py").read_bytes()
    with pytest.raises(ValueError, match="Maintained compositor source was modified"):
        approve_application(app.package, app.digest)
    (app.package / "app.py").write_text("changed", encoding="utf-8")
    with pytest.raises(ValueError):
        service.load_for_runtime_refresh(app.id)


def test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime(tmp_path, monkeypatch):
    """Re-approval after runtime drift reseals the new digest and installed runtime bytes."""
    from types import SimpleNamespace

    from agentix.application import general_package
    from agentix.lab.application_artifacts import approve_application

    service = library(tmp_path)
    app = service.publish(verified(tmp_path))
    original = general_package.runtime_template
    changed = tmp_path / "application_context.py"
    moved = original("application_context.py").read_bytes() + b"\n# moved\n"
    changed.write_bytes(moved)
    monkeypatch.setattr(
        general_package,
        "runtime_template",
        lambda name: changed if name == "application_context.py" else original(name),
    )
    snapshot = approve_application(app.package, app.digest, allow_runtime_drift=True)
    candidate = SimpleNamespace(
        package=app.package,
        digest=snapshot.digest,
        snapshot=snapshot,
        approved=True,
        verified=True,
        review_text=json.dumps(app.review),
        catalog_id=app.id,
        display_name=app.name,
        dependency_check=None,
        preview=None,
        runtime_refresh=True,
    )
    resealed = service.publish(candidate)
    assert resealed.digest == snapshot.digest
    assert (app.package / "application_context.py").read_bytes() == moved
    assert [entry.status for entry in service.entries()] == ["valid"]


def test_acceptance_save_keeps_installed_catalog_identity(tmp_path):
    """Saving acceptance cases for a re-approval must reseal, not create a second folder."""
    from agentix.application.app_review import ApplicationReview

    service = library(tmp_path)
    item = candidate(tmp_path / "draft")
    ApplicationSupervisor().approve(item, item.identity, True)
    item.verified = True
    app = service.publish(item)
    item.catalog_id = app.id
    item.runtime_refresh = True
    manifest = json.loads(item.review_text)["manifest"]
    acceptance = {
        "payload": {name: "Hello World!" for name in manifest["inputs"]},
        "expected": {widget["id"]: 2 for widget in manifest["widgets"]},
    }
    ApplicationReview().save(
        item, "application_acceptance.json", json.dumps(acceptance), item.identity
    )
    assert item.catalog_id == app.id
    assert item.runtime_refresh is True
    assert item.identity != app.id


def test_publish_reseals_existing_catalog_identity_without_new_folder(tmp_path, monkeypatch):
    """Re-approving a loaded app replaces its record instead of duplicating storage."""
    service, app = stale_library(tmp_path, monkeypatch)
    item = verified(tmp_path / "again")
    item.catalog_id = app.id
    folders = sorted(path.name for path in service.root.iterdir())
    result = service.publish(item)
    assert result.id == app.id and result.digest == app.digest
    assert sorted(path.name for path in service.root.iterdir()) == folders
    assert library(tmp_path).get(app.id).digest == app.digest


def test_catalog_entries_labels_stale_app_for_reapproval(tmp_path, monkeypatch):
    """The dropdown must show a stale application instead of hiding it."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    choices, _ = backend.catalog_entries(owner.token, SimpleNamespace(session_hash="alice"))
    assert choices == [(app.name + " (re-approval required)", app.id)]
    described = backend.describe_app(app.id, owner.token, SimpleNamespace(session_hash="alice"))
    assert "Re-approval required" in described


def test_load_app_restores_stale_app_for_reapproval(tmp_path, monkeypatch):
    """Loading a stale app must restore reviewable bytes and request approval again."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    request = SimpleNamespace(session_hash="alice")
    rows = list(backend.load_app(app.id, owner.token, request))
    assert "re-approval" in rows[-1][0]
    _, state = backend._resolve(owner.token, request)
    assert state.candidate.catalog_id == app.id
    assert not state.candidate.approved and not state.candidate.verified
    assert owner.controller.state.application_review_pending


def drift_tool_contract(fixture, role="count_words_in_text"):
    """Simulate a re-approved tool whose contract digest moved after installation."""
    tool_name = role.removesuffix("_code")
    owner, code, tests, digest, functions, contract = fixture.ledger._reuse[tool_name]
    fixture.ledger._reuse[tool_name] = (
        owner,
        code,
        tests,
        "drifted-" + digest,
        functions,
        contract,
    )
    return tool_name


def test_load_app_rebinds_changed_tool_contracts_for_reapproval(tmp_path, monkeypatch):
    """A changed tool contract must load for re-approval instead of failing outright."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    drift_tool_contract(fixture)
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    request = SimpleNamespace(session_hash="alice")
    rows = list(backend.load_app(app.id, owner.token, request))
    assert "tool contracts changed" in rows[-1][0]
    _, state = backend._resolve(owner.token, request)
    assert state.candidate.catalog_id == app.id
    assert not state.candidate.approved and not state.candidate.verified


def test_load_app_reports_the_missing_catalog_approval_actionably(tmp_path):
    """V7-064: a catalog without reusable approvals must name the recovery, not the type."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.storage.application_catalog import CatalogToolRegistry
    from agentix.storage.catalog import ToolCatalog

    service, app, fixture = published_with_tools(tmp_path)
    empty = tmp_path / "empty-tools"
    empty.mkdir()
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(
        sessions,
        library_factory=lambda: library(tmp_path),
        registry_factory=lambda controller: CatalogToolRegistry(ToolCatalog(empty), fixture.ledger),
    )
    rows = list(backend.load_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    message = rows[-1][0]
    assert "CatalogDependencyError" not in message
    assert "approve" in message.lower()
    assert "Tools" in message


def test_reverify_app_reports_the_missing_catalog_approval_actionably(tmp_path, monkeypatch):
    """V7-064: re-verification must explain the missing approval instead of the type name."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.storage.application_catalog import CatalogToolRegistry
    from agentix.storage.catalog import ToolCatalog

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    empty = tmp_path / "empty-tools"
    empty.mkdir()
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(
        sessions,
        library_factory=lambda: library(tmp_path),
        registry_factory=lambda controller: CatalogToolRegistry(ToolCatalog(empty), fixture.ledger),
    )
    rows = list(backend.reverify_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    message = rows[-1][0]
    assert "CatalogDependencyError" not in message
    assert "approve" in message.lower()
    assert "unapproved" in message


def test_check_dependencies_names_the_tool_without_a_reusable_approval():
    """V7-064: the dependency failure must name the tool and its maintained skip reason."""
    from types import SimpleNamespace

    from agentix.application.app_invocation import check_dependencies
    from agentix.storage.application_catalog import CatalogDependencyError

    class Registry:
        """Expose the maintained skip reason without an approved tool."""

        def resolve(self):
            """Return no approved tool so the application dependency is missing."""
            return {}

        def _skip_reason(self, name):
            """Return the owner-actionable reason for the missing approval."""
            return "no current reusable approval; execute and approve it in Tools first"

    app = SimpleNamespace(
        dependencies={"calculator": {"tool_name": "calculator", "function": "calculator"}}
    )
    with pytest.raises(CatalogDependencyError) as error:
        check_dependencies(app, Registry())
    assert "calculator" in str(error.value)
    assert "no current reusable approval" in str(error.value)


def test_reverify_refuses_dependency_drift_with_actionable_message(tmp_path, monkeypatch):
    """Dependency drift needs a new human review, not an automatic reseal."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    drift_tool_contract(fixture)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    rows = list(backend.reverify_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    assert "requires re-approval" in rows[-1][0]
    assert [entry.status for entry in library(tmp_path).entries()] == ["approval_stale"]


def test_reapproval_reseals_rebound_tool_dependencies(tmp_path, monkeypatch):
    """Approving a reloaded app must store the current tool digests it was verified against."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    tool_name = drift_tool_contract(fixture)
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render

    class Supervisor:
        """Exercise the production dependency check without native or browser claims."""

        def approve(self, candidate, identity, reviewed):
            """Run the same dependency recheck the production supervisor runs."""
            candidate.dependency_check()
            candidate.approved = True

        def verify(self, candidate, origin):
            """Mark verified without claiming a real gate execution."""
            candidate.verified = True
            return SimpleNamespace(url="http://127.0.0.1:7877/", close=lambda: None)

    backend = ApplicationsBackend(
        sessions, supervisor=Supervisor(), library_factory=lambda: library(tmp_path)
    )
    request = SimpleNamespace(session_hash="alice")
    list(backend.load_app(app.id, owner.token, request))
    rows = list(backend.approve(True, app.id, owner.token, request))
    assert "Verified" in rows[-1][0]
    stored = library(tmp_path).get(app.id)
    assert stored.dependencies["count_words_in_text"]["contract_digest"].startswith("drifted-")
    assert stored.dependencies["count_words_in_text"]["tool_name"] == tool_name


def test_describe_app_drops_stale_guidance_after_reseal(tmp_path, monkeypatch):
    """A successful re-approval must remove the re-approval guidance from the panel."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    request = SimpleNamespace(session_hash="alice")
    assert "Re-approval required" in backend.describe_app(app.id, owner.token, request)
    library(tmp_path).reseal(app.id)
    described = backend.describe_app(app.id, owner.token, request)
    assert "Re-approval required" not in described
    assert "Use Load selected app" not in described
    assert app.name in described


def test_describe_app_drops_stale_guidance_after_reverify(tmp_path, monkeypatch):
    """A successful re-verification must remove the re-approval guidance from the panel."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render

    class Supervisor:
        """Accept the installed bytes without claiming a real gate execution."""

        def verify(self, candidate, origin):
            """Mark the candidate verified for the reseal path."""
            candidate.verified = True
            return SimpleNamespace(url="http://127.0.0.1:7877/", close=lambda: None)

    backend = ApplicationsBackend(
        sessions, supervisor=Supervisor(), library_factory=lambda: library(tmp_path)
    )
    request = SimpleNamespace(session_hash="alice")
    list(backend.reverify_app(app.id, owner.token, request))
    described = backend.describe_app(app.id, owner.token, request)
    assert "Re-approval required" not in described
    assert "Use Load selected app" not in described


def test_catalog_view_refreshes_label_and_description_together(tmp_path, monkeypatch):
    """One refresh must drop both the stale dropdown label and its guidance text."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.ui.apps_catalog import catalog_view

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(sessions, library_factory=lambda: library(tmp_path))
    request = SimpleNamespace(session_hash="alice")

    class Dropdown:
        """Capture the update payload without building a real Gradio component."""

        def __init__(self, **kwargs):
            self.kwargs = kwargs

    gr = SimpleNamespace(Dropdown=Dropdown)
    update, described, owned = catalog_view(backend, gr, app.id, owner.token, request)
    assert update.kwargs["choices"] == [(app.name + " (re-approval required)", app.id)]
    assert update.kwargs["value"] == app.id
    assert "Re-approval required" in described
    assert owned == owner.token

    library(tmp_path).reseal(app.id)
    update, described, _ = catalog_view(backend, gr, app.id, owner.token, request)
    assert update.kwargs["choices"] == [(app.name, app.id)]
    assert update.kwargs["value"] == app.id
    assert "Re-approval required" not in described


def test_catalog_refresh_binding_updates_description_with_choices(tmp_path, monkeypatch):
    """The status refresh must repaint the description so stale guidance disappears."""
    from types import SimpleNamespace

    import agentix.ui.application_candidates as candidates
    from agentix.ui.apps_catalog import build_apps_catalog

    monkeypatch.setattr(candidates, "build_candidate_panel", lambda *args, **kwargs: None)
    bindings = []

    class Component:
        """Record constructor kwargs and absorb event bindings."""

        def __init__(self, *args, **kwargs):
            self.kwargs = kwargs
            self.events = {}
            bindings.append(self)

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def __getattr__(self, name):
            def event(**kwargs):
                self.events[name] = kwargs
                return self

            return event

    class Dialog:
        """Absorb dialog wrapping without building real modal components."""

        def guard_result(self, fn, size):
            return fn

        def wrap_stream_final(self, fn, size):
            return fn

        def outputs(self):
            return []

    gr = SimpleNamespace(
        **{
            name: Component
            for name in (
                "Markdown",
                "Dropdown",
                "Button",
                "Row",
                "Column",
                "Timer",
                "Checkbox",
                "CheckboxGroup",
                "Textbox",
                "Number",
                "HTML",
                "State",
            )
        }
    )
    gr.skip = lambda: None
    gr.update = lambda **kwargs: kwargs
    status = Component()
    workspace = {"status": status, "outputs": [status], "dialog": Dialog()}
    backend = SimpleNamespace(
        catalog_entries=lambda token, request: ([("App (re-approval required)", "id")], token),
        describe_app=lambda selected, token, request: "Re-approval required: stale",
        review_state=lambda owned, request: {"repair_available": False, "busy": False},
    )
    build_apps_catalog(gr, backend, lambda fn: fn, Component(), workspace, None, None)
    outputs = status.events["change"]["outputs"]
    assert len(outputs) == 3
    assert outputs[0].kwargs.get("elem_id") == "installed-apps"
    assert outputs[1].kwargs.get("elem_id") == "installed-app-description"
    refreshed = status.events["change"]["fn"]("id", "token", SimpleNamespace())
    assert refreshed[0].kwargs["choices"] == [("App (re-approval required)", "id")]
    assert refreshed[1] == "Re-approval required: stale"


def test_reverify_reseals_only_after_independent_gates_pass(tmp_path, monkeypatch):
    """D3 re-runs real gates on installed bytes and reseals only on success."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    calls = []

    class Supervisor:
        """Record gate invocation without claiming native or browser execution."""

        def verify(self, candidate, origin):
            """Accept only the exact installed bytes under test."""
            calls.append((candidate.digest, origin))
            candidate.verified = True
            return SimpleNamespace(url="http://127.0.0.1:1", close=lambda: None)

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(
        sessions, supervisor=Supervisor(), library_factory=lambda: library(tmp_path)
    )
    rows = list(backend.reverify_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    assert "Re-verified" in rows[-1][0]
    assert calls and calls[0][0] == app.digest
    assert library(tmp_path).get(app.id).digest == app.digest


def test_reverify_keeps_stale_record_when_gates_fail(tmp_path, monkeypatch):
    """A failed gate must leave the stale record untouched and unapproved."""
    from types import SimpleNamespace

    from test_applications_backend import registry

    from agentix.controllers.applications import ApplicationsBackend

    service, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")

    class Supervisor:
        """Fail the gate without touching storage."""

        def verify(self, candidate, origin):
            """Report an independent acceptance failure."""
            raise ValueError("Independent native application acceptance failed")

    sessions = registry()
    owner = sessions.resolve(None, "alice")
    owner.controller.security = fixture.ledger.security
    owner.controller.validation = SimpleNamespace(ledger=fixture.ledger)
    owner.controller.get_installed_tools_catalog = fixture.catalog.render
    backend = ApplicationsBackend(
        sessions, supervisor=Supervisor(), library_factory=lambda: library(tmp_path)
    )
    rows = list(backend.reverify_app(app.id, owner.token, SimpleNamespace(session_hash="alice")))
    assert "Re-verification failed" in rows[-1][0]
    assert [entry.status for entry in library(tmp_path).entries()] == ["approval_stale"]
