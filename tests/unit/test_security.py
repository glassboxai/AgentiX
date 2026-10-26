"""Characterize real storage and approval behavior without production writes."""

import threading
from unittest.mock import Mock

import pytest


@pytest.mark.parametrize(
    "tool,filename", [("adder", "code.py"), ("tool_1", "notes.md"), ("test", "é.txt")]
)
def test_resolve_valid_path(system, tool, filename):
    """Verify resolve valid path."""
    assert system.security.validate_and_resolve_path(tool, filename) == str(
        system.root / tool / filename
    )


@pytest.mark.parametrize("tool,filename", [("../outside", "x"), ("tool", "../../outside/x")])
def test_reject_traversal(system, tool, filename):
    """Verify reject traversal."""
    with pytest.raises(system.security_manager.SecurityViolationError):
        system.security.validate_and_resolve_path(tool, filename)


def test_auto_approval_returns_original_content(system):
    """Verify auto approval returns original content."""
    system.security.auto_approve = True
    assert system.security.request_user_permission("file", content="original") == (True, "original")
    assert system.security.get_pending_request() is None


@pytest.mark.parametrize(
    "decision,edited,expected",
    [
        (True, "edited", "edited"),
        (True, "", ""),
        (True, None, "original"),
        (False, None, "original"),
    ],
)
def test_interactive_permission_round_trip(system, monkeypatch, decision, edited, expected):
    """Verify interactive permission round trip."""
    sec = system.security

    def respond(timeout):
        """Provide respond for the enclosing trusted test fixture."""
        assert timeout == 300
        assert sec.get_pending_request()["content"] == "original"
        pending = sec.get_pending_request()
        sec.resolve_pending_request(
            decision, edited, request_id=pending["request_id"], owner_id=sec.owner_id
        )
        return True

    monkeypatch.setattr(sec._approval_event, "wait", respond)
    assert sec.request_user_permission("file", content="original") == (decision, expected)
    assert sec.get_pending_request() is None
    assert sec._edited_content is None


def test_timeout_denies_and_cleans_up(system, monkeypatch):
    """Verify timeout denies and cleans up."""
    monkeypatch.setattr(system.security._approval_event, "wait", lambda timeout: False)
    assert system.security.request_user_permission("file", content="x") == (False, "x")
    assert system.security.get_pending_request() is None


def test_response_without_pending_request_does_nothing(system):
    """Verify response without pending request does nothing."""
    system.security.resolve_pending_request(True, "edited")
    assert not system.security._approval_event.is_set()


def test_real_thread_approval_handshake(system):
    """Verify real thread approval handshake."""
    sec = system.security
    ready = threading.Event()
    original_wait = sec._approval_event.wait
    sec._approval_event.wait = lambda timeout: (ready.set(), original_wait(2))[1]
    result = []
    worker = threading.Thread(
        target=lambda: result.append(sec.request_user_permission("x", content="old"))
    )
    worker.start()
    try:
        assert ready.wait(2), "Worker did not publish its request"
        pending = sec.get_pending_request()
        sec.resolve_pending_request(
            True, "new", request_id=pending["request_id"], owner_id=sec.owner_id
        )
        worker.join(2)
        assert not worker.is_alive()
        assert result == [(True, "new")]
    finally:
        sec._approval_event.set()
        worker.join(2)


def test_write_and_append_utf8(system):
    """Verify write and append utf8."""
    system.security.auto_approve = True
    assert system.security.safe_write_file("tool", "notes.md", "café").startswith("Success:")
    system.security.safe_write_file("tool", "notes.md", "\nsecond", "a")
    assert (system.root / "tool" / "notes.md").read_text(encoding="utf-8") == "café\nsecond"


def test_directory_denial_leaves_no_artifacts(system, monkeypatch):
    """Verify directory denial leaves no artifacts."""
    monkeypatch.setattr(system.security, "request_user_permission", Mock(return_value=(False, "")))
    assert "Directory creation rejected" in system.security.safe_write_file("tool", "x", "data")
    assert not system.root.exists()


def test_file_denial_preserves_existing_content(system, monkeypatch):
    """Verify file denial preserves existing content."""
    directory = system.root / "tool"
    directory.mkdir(parents=True)
    target = directory / "x"
    target.write_text("old")
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(False, "new"))
    )
    assert "authorization denied" in system.security.safe_write_file("tool", "x", "new")
    assert target.read_text() == "old"


def test_edited_content_is_persisted(system, monkeypatch):
    """Verify edited content is persisted."""
    (system.root / "tool").mkdir(parents=True)
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, "approved edit"))
    )
    system.security.safe_write_file("tool", "x", "original")
    assert (system.root / "tool" / "x").read_text() == "approved edit"


def test_write_failure_is_reported(system, monkeypatch):
    """Verify write failure is reported."""
    (system.root / "tool").mkdir(parents=True)
    system.security.auto_approve = True
    monkeypatch.setattr("builtins.open", Mock(side_effect=OSError("disk unavailable")))
    assert "Error writing file: disk unavailable" == system.security.safe_write_file(
        "tool", "x", "data"
    )


def test_reject_sibling_tool_prefix_escape(system):
    """Verify reject sibling tool prefix escape."""
    with pytest.raises(system.security_manager.SecurityViolationError):
        system.security.validate_and_resolve_path("safe", "../safe_evil/x.py")


def test_reject_sibling_root_prefix_escape(system):
    """Verify reject sibling root prefix escape."""
    with pytest.raises(system.security_manager.SecurityViolationError):
        system.security.validate_and_resolve_path("../generated_tools_evil", "x.py")


def test_pending_request_is_defensive_copy(system):
    """Verify pending request is defensive copy."""
    system.security._pending_request = {"filepath": "original"}
    system.security.get_pending_request()["filepath"] = "modified"
    assert system.security.get_pending_request()["filepath"] == "original"


@pytest.mark.parametrize(
    "tool,filename",
    [
        ("", "x.py"),
        (".", "x.py"),
        ("..", "x.py"),
        ("safe/other", "x.py"),
        ("safe\\other", "x.py"),
        ("C:drive", "x.py"),
        ("CON", "x.py"),
        ("safe.", "x.py"),
        ("safe ", "x.py"),
        ("safe", ""),
        ("safe", "../safe/x.py"),
        ("safe", "C:relative.py"),
        ("safe", "/absolute.py"),
        ("safe", "\\absolute.py"),
        ("safe", "x.py:stream"),
        ("safe", "NUL.py"),
        ("safe", "nested/../x.py"),
        ("safe", "nested./x.py"),
    ],
)
def test_reject_ambiguous_or_unsafe_windows_paths(system, tool, filename):
    """Reject Windows aliases, traversal and drive forms before filesystem access."""
    with pytest.raises(system.security_manager.SecurityViolationError):
        system.security.validate_and_resolve_path(tool, filename)


def test_allow_nested_relative_artifact_path(system):
    """Verify allow nested relative artifact path."""
    assert system.security.validate_and_resolve_path("safe", "nested/notes.md") == str(
        system.root / "safe" / "nested" / "notes.md"
    )


def test_pending_snapshot_cannot_modify_nested_state(system):
    """Verify pending snapshot cannot modify nested state."""
    system.security._pending_request = {"metadata": {"stage": "original"}}
    system.security.get_pending_request()["metadata"]["stage"] = "changed"
    assert system.security.get_pending_request()["metadata"]["stage"] == "original"


def test_invalid_python_preserves_existing_file(system, monkeypatch):
    """Compilation must occur before opening/truncating the destination."""
    directory = system.root / "safe"
    directory.mkdir(parents=True)
    target = directory / "code.py"
    target.write_text("VALUE = 1", encoding="utf-8")
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, "def invalid(:"))
    )
    result = system.security.safe_write_file("safe", "code.py", "VALUE = 2")
    assert result.startswith("Error validating Python:")
    assert target.read_text() == "VALUE = 1"


def test_valid_edited_python_is_saved_without_execution(system, monkeypatch):
    """Verify valid edited python is saved without execution."""
    (system.root / "safe").mkdir(parents=True)
    edited = "raise RuntimeError('must not execute during save')"
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, edited))
    )
    assert system.security.safe_write_file("safe", "code.py", "VALUE = 1").startswith("Success:")
    assert (system.root / "safe" / "code.py").read_text() == edited


def test_invalid_python_append_preserves_existing_file(system):
    """Verify invalid python append preserves existing file."""
    system.security.auto_approve = True
    system.security.safe_write_file("safe", "code.py", "VALUE = 1\n")
    result = system.security.safe_write_file("safe", "code.py", "def invalid(:", "a")
    assert result.startswith("Error validating Python:")
    assert (system.root / "safe" / "code.py").read_text() == "VALUE = 1\n"


def test_python_alias_cannot_bypass_validation_by_resolving_to_text_file(system, monkeypatch):
    """A confined link may resolve to another suffix; the requested type still counts."""
    directory = system.root / "safe"
    directory.mkdir(parents=True)
    target = directory / "stored.txt"
    target.write_text("VALUE = 1")
    # Model the path resolver's output without requiring Windows symlink privileges.
    monkeypatch.setattr(
        system.security, "validate_and_resolve_path", Mock(return_value=str(target))
    )
    monkeypatch.setattr(
        system.security, "request_user_permission", Mock(return_value=(True, "def invalid(:"))
    )
    result = system.security.safe_write_file("safe", "code.py", "VALUE = 2")
    assert result.startswith("Error validating Python:")
    assert target.read_text() == "VALUE = 1"
