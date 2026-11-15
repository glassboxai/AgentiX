"""Permanent removal uses trusted temporary packages and authenticated metadata doubles."""

from pathlib import Path

import pytest
from test_application_catalog import installed
from test_installed_apps import library, published_with_tools


def service(tmp_path, fixture, apps):
    """Resolve the removal boundary without granting a missing implementation a pass."""
    try:
        from agentix.storage.maintenance import CatalogMaintenance
    except ImportError:
        pytest.fail("Catalog deletion is not implemented")
    return CatalogMaintenance(
        Path(fixture.catalog.root),
        apps,
        revoke_tool=fixture.ledger.invalidate,
        revoke_widget=lambda name: None,
    )


def test_tool_referenced_by_installed_app_is_not_deletable(tmp_path):
    """Installed composite data operations count as dependencies even when GUI is closed."""
    apps, app, fixture = published_with_tools(tmp_path)
    with pytest.raises(ValueError, match="depend"):
        service(tmp_path, fixture, apps).prepare_tool("count_words_in_text")
    assert Path(fixture.catalog.root, "count_words_in_text/count_words_in_text_code.py").exists()


def test_invalid_app_source_does_not_hide_dependency(tmp_path):
    """Do not use the executable-only catalog list to decide deletion safety."""
    apps, app, fixture = published_with_tools(tmp_path)
    (app.package / "app.py").write_text("changed", encoding="utf-8")
    assert apps.list() == []
    with pytest.raises(ValueError, match="depend"):
        service(tmp_path, fixture, apps).prepare_tool("count_words_in_text")


def test_confirmed_unused_tool_is_permanently_removed(tmp_path):
    """Preparation is read-only; explicit commit removes only its exact package."""
    tools = tmp_path / "tools"
    tools.mkdir()
    fixture = installed(tools)
    operations = service(tmp_path, fixture, library(tmp_path))
    snapshot = operations.prepare_tool("count_words_in_text")
    assert (tools / "count_words_in_text").is_dir()
    operations.confirm(snapshot)
    assert not (tools / "count_words_in_text").exists()
    assert (tools / "count_vowels_in_text/count_vowels_in_text_code.py").exists()
    assert "count_words_in_text" not in fixture.ledger._reuse


def test_package_change_invalidates_confirmation(tmp_path):
    """A stale prompt cannot permanently delete changed content."""
    tools = tmp_path / "tools"
    tools.mkdir()
    fixture = installed(tools)
    operations = service(tmp_path, fixture, library(tmp_path))
    snapshot = operations.prepare_tool("count_words_in_text")
    (tools / "count_words_in_text/new.txt").write_text("new", encoding="utf-8")
    with pytest.raises(ValueError, match="changed"):
        operations.confirm(snapshot)
    assert (tools / "count_words_in_text/new.txt").exists()


def test_open_app_lease_blocks_removal_across_library_instances(tmp_path):
    """A second session/process must not delete a package serving an open application."""
    apps, app, fixture = published_with_tools(tmp_path)
    try:
        lease = apps.open_lease(app.id)
    except AttributeError:
        pytest.fail("Cross-session application usage leases are not implemented")
    operations = service(tmp_path, fixture, library(tmp_path))
    try:
        with pytest.raises(ValueError, match="open|use"):
            operations.prepare_app(app.id)
    finally:
        lease.close()
    snapshot = operations.prepare_app(app.id)
    operations.confirm(snapshot)
    assert apps.list() == [] and not app.package.exists()
    assert not (apps.root.parent / "reviews" / app.id).exists()


@pytest.mark.parametrize("identity", ["../other", "", "C:\\outside"])
def test_browser_paths_are_not_tool_identifiers(tmp_path, identity):
    """Never turn a browser parameter into an unrestricted deletion target."""
    tools = tmp_path / "tools"
    tools.mkdir()
    fixture = installed(tools)
    with pytest.raises(ValueError):
        service(tmp_path, fixture, library(tmp_path)).prepare_tool(identity)


def test_renamed_member_cannot_preserve_confirmation_digest(tmp_path):
    """File names/content need unambiguous framing, not raw concatenation."""
    tools = tmp_path / "tools"
    tools.mkdir()
    fixture = installed(tools)
    operations = service(tmp_path, fixture, library(tmp_path))
    folder = tools / "count_words_in_text"
    (folder / "a").write_bytes(b"bc")
    snapshot = operations.prepare_tool("count_words_in_text")
    (folder / "a").unlink()
    (folder / "ab").write_bytes(b"c")
    with pytest.raises(ValueError, match="changed"):
        operations.confirm(snapshot)
    assert folder.exists()


def test_stale_policy_does_not_block_permanent_application_removal(tmp_path, monkeypatch):
    """V7-060: removal needs identity, bytes and usage, not a current policy binding."""
    apps, app, fixture = published_with_tools(tmp_path)
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    stale = library(tmp_path)
    assert stale.list() == []
    with pytest.raises(ValueError, match="stale"):
        stale.get(app.id)
    operations = service(tmp_path, fixture, stale)
    snapshot = operations.prepare_app(app.id)
    operations.confirm(snapshot)
    assert not app.package.exists()
    assert not (apps.root.parent / "reviews" / app.id).exists()
    assert stale.entries() == []


def test_stale_policy_still_refuses_changed_application_source(tmp_path, monkeypatch):
    """A stale policy never authorizes removal of bytes that changed after installation."""
    apps, app, fixture = published_with_tools(tmp_path)
    (app.package / "app.py").write_text("changed", encoding="utf-8")
    monkeypatch.setattr("agentix.storage.installed_apps.app_policy", lambda: "changed-policy")
    operations = service(tmp_path, fixture, library(tmp_path))
    with pytest.raises(ValueError, match="source changed"):
        operations.prepare_app(app.id)
    assert app.package.exists()


def test_copied_app_approval_cannot_authorize_another_library(tmp_path):
    """Protected app records must bind their root, not only a namespace filename."""
    import shutil

    from test_widget_reuse import Protector

    from agentix.storage.installed_apps import InstalledApps

    (tmp_path / "first").mkdir()
    apps, app, fixture = published_with_tools(tmp_path / "first")
    other = InstalledApps(
        tmp_path / "other/apps", tmp_path / "other/records", protector=Protector()
    )
    shutil.copytree(app.package, other.root / app.package.name)
    review = other.root.parent / "reviews" / app.id
    review.mkdir(parents=True)
    shutil.copyfile(apps.root.parent / "reviews" / app.id / "review.json", review / "review.json")
    record = other._record(app.id)
    record.parent.mkdir(parents=True)
    shutil.copyfile(apps._record(app.id), record)
    with pytest.raises(ValueError):
        other.get(app.id)
