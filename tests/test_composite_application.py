"""LAB-005 contracts and package trust tests with maintained, offline fixtures."""

import json
import shutil

import pytest


def api():
    """Import the maintained host validator, never an application module."""
    from agentix.lab import application_artifacts

    return application_artifacts


def copied(tmp_path):
    """Copy only the generated schema-3 package, not any catalog."""
    from schema3_package import package

    target = tmp_path / "application with spaces"
    shutil.copytree(package(tmp_path), target, ignore=shutil.ignore_patterns("__pycache__"))
    return target


def test_review_captures_bytes_and_rejects_changes(tmp_path):
    """Catch review bypass and rereading changed code after snapshot approval."""
    folder = copied(tmp_path)
    digest = api().application_digest(folder)
    approved = api().approve_application(folder, digest)
    original = dict(approved.files)["application_logic.py"]
    (folder / "application_logic.py").write_bytes(b"raise RuntimeError('changed')")
    assert dict(approved.files)["application_logic.py"] == original
    with pytest.raises(ValueError):
        api().approve_application(folder, digest)


@pytest.mark.parametrize(
    "mutation", ["extra", "missing", "lock", "permission", "cycle", "unknown", "port"]
)
def test_unreviewable_packages_are_rejected(tmp_path, mutation):
    """Catch unexpected executables, missing closure, elevated scope and invalid DAGs."""
    folder = copied(tmp_path)
    path = folder / "application.json"
    manifest = json.loads(path.read_text())
    if mutation == "extra":
        (folder / "surprise.py").write_text("raise RuntimeError()")
    elif mutation == "missing":
        (folder / "application_logic.py").unlink()
    elif mutation == "lock":
        manifest["runtime_lock_sha256"] = "0" * 64
    elif mutation == "permission":
        manifest["permissions"] = ["network"]
    elif mutation == "cycle":
        manifest["files"]["application_logic.py"] = "1" * 64
    elif mutation == "unknown":
        manifest["files"]["unknown.py"] = "2" * 64
    elif mutation == "port":
        manifest["files"]["application_logic.py"] = "0" * 64
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        api().application_digest(folder)


def test_symlink_package_member_is_rejected(tmp_path):
    """Catch approved-file aliasing outside the selected package."""
    folder = copied(tmp_path)
    member = folder / "application_logic.py"
    original = tmp_path / "outside.py"
    member.rename(original)
    try:
        member.symlink_to(original)
    except OSError:
        pytest.skip("Symlink creation unavailable for this Windows user")
    with pytest.raises(ValueError):
        api().application_digest(folder)


def test_strict_return_contract_rejects_bool_negative_and_extra_fields():
    """Catch coercion or accepting invalid structured child results as success."""
    from agentix.lab.application_artifacts import validate_result

    manifest = {
        "schema_version": 3,
        "widgets": [{"id": "count_words_in_text", "tool": "count_words_in_text"}],
        "tools": {"count_words_in_text": {"returns": {"type": "integer"}}},
    }
    assert validate_result({"count_words_in_text": 0}, manifest) == {"count_words_in_text": 0}
    for value in (
        {"count_words_in_text": True},
        {"count_words_in_text": 2, "extra": 0},
        "2,3",
    ):
        with pytest.raises(ValueError):
            validate_result(value, manifest)


def test_parent_rejects_application_tool_rpc_without_dispatch(tmp_path):
    """Direct-call applications cannot request legacy host tool capabilities."""
    from agentix.lab.application_session import ApplicationSession

    folder = copied(tmp_path)
    approved = api().approve_application(folder, api().application_digest(folder))
    session = ApplicationSession(approved)
    try:
        with pytest.raises(ValueError):
            session._invoke_tool({"type": "tool"})
        assert session.cancel.is_set()
        assert not session.tool_receipts
    finally:
        session.close()


def test_application_cannot_exceed_manifest_lifetime(tmp_path):
    """A host caller cannot silently exceed the application's declared 300-second limit."""
    from agentix.lab.application_session import ApplicationSession

    folder = copied(tmp_path)
    approved = api().approve_application(folder, api().application_digest(folder))
    with pytest.raises(ValueError):
        session = ApplicationSession(approved, lifetime=301)
        session.close()
