"""Exercise real handshakes with deterministic thread synchronization."""

import threading

import pytest

from agentix.approvals import ApprovalCoordinator


def pending_request(boundary, monkeypatch):
    """Publish a real worker request and return a deterministic cleanup handle."""
    ready = threading.Event()
    original = boundary._approval_event.wait
    monkeypatch.setattr(
        boundary._approval_event, "wait", lambda timeout: (ready.set(), original(2))[1]
    )
    result = []
    worker = threading.Thread(
        target=lambda: result.append(boundary.request_user_permission("file", content="original"))
    )
    worker.start()
    assert ready.wait(2)
    return worker, result, boundary.get_pending_request()


@pytest.mark.parametrize(
    "request_id,owner", [(None, "alice"), ("wrong", "alice"), ("correct", "bob")]
)
def test_wrong_or_missing_identity_does_not_authorize(monkeypatch, request_id, owner):
    """Verify wrong or missing identity does not authorize."""
    boundary = ApprovalCoordinator.for_owner("alice")
    worker, result, pending = pending_request(boundary, monkeypatch)
    try:
        supplied = pending["request_id"] if request_id == "correct" else request_id
        assert (
            boundary.resolve_pending_request(True, "bad", request_id=supplied, owner_id=owner)
            is False
        )
        assert not boundary._approval_event.is_set()
        assert (
            boundary.resolve_pending_request(
                True, "approved", request_id=pending["request_id"], owner_id="alice"
            )
            is True
        )
        worker.join(2)
        assert result == [(True, "approved")]
    finally:
        boundary._approval_event.set()
        worker.join(2)


def test_duplicate_response_cannot_change_first_decision(monkeypatch):
    """Verify duplicate response cannot change first decision."""
    boundary = ApprovalCoordinator.for_owner("alice")
    worker, result, pending = pending_request(boundary, monkeypatch)
    try:
        assert boundary.resolve_pending_request(
            True, "first", request_id=pending["request_id"], owner_id="alice"
        )
        assert not boundary.resolve_pending_request(
            False, "second", request_id=pending["request_id"], owner_id="alice"
        )
        worker.join(2)
        assert result == [(True, "first")]
    finally:
        boundary._approval_event.set()
        worker.join(2)


def test_expired_response_is_denied(monkeypatch):
    """Verify expired response is denied."""
    boundary = ApprovalCoordinator.for_owner("alice")
    now = [100.0]
    boundary._clock = staticmethod(lambda: now[0])
    worker, result, pending = pending_request(boundary, monkeypatch)
    try:
        now[0] = 401.0
        assert not boundary.resolve_pending_request(
            True, request_id=pending["request_id"], owner_id="alice"
        )
        worker.join(2)
        assert result == [(False, "original")]
    finally:
        boundary._approval_event.set()
        worker.join(2)


def test_second_request_cannot_overwrite_pending_request(monkeypatch):
    """Verify second request cannot overwrite pending request."""
    boundary = ApprovalCoordinator.for_owner("alice")
    worker, result, pending = pending_request(boundary, monkeypatch)
    try:
        assert boundary.request_user_permission("other", content="second") == (False, "second")
        assert boundary.get_pending_request()["request_id"] == pending["request_id"]
        boundary.resolve_pending_request(False, request_id=pending["request_id"], owner_id="alice")
        worker.join(2)
        assert result == [(False, "original")]
    finally:
        boundary._approval_event.set()
        worker.join(2)


def test_owners_have_independent_auto_approval_settings():
    """Verify owners have independent auto approval settings."""
    first, second = ApprovalCoordinator.for_owner("alice"), ApprovalCoordinator.for_owner("bob")
    first.auto_approve = True
    assert second.auto_approve is False
    assert first._approval_event is not second._approval_event


def test_owner_factory_does_not_inherit_parent_activity_or_operation():
    """Verify owner factory does not inherit parent activity or operation."""
    parent = ApprovalCoordinator.for_owner("legacy")
    parent.activity_capture = object()
    parent.operation_id = "parent-operation"
    child = parent.for_owner("new-owner")
    assert child.activity_capture is None
    assert child.operation_id == ""


def test_previous_request_id_cannot_approve_same_filepath_again(monkeypatch):
    """Verify previous request id cannot approve same filepath again."""
    boundary = ApprovalCoordinator.for_owner("alice")
    first_worker, first_result, first = pending_request(boundary, monkeypatch)
    boundary.resolve_pending_request(True, request_id=first["request_id"], owner_id="alice")
    first_worker.join(2)
    second_worker, second_result, second = pending_request(boundary, monkeypatch)
    try:
        assert second["request_id"] != first["request_id"]
        assert not boundary.resolve_pending_request(
            True, "stale", request_id=first["request_id"], owner_id="alice"
        )
        assert boundary.resolve_pending_request(
            False, request_id=second["request_id"], owner_id="alice"
        )
        second_worker.join(2)
        assert first_result == [(True, "original")]
        assert second_result == [(False, "original")]
    finally:
        boundary._approval_event.set()
        second_worker.join(2)


def test_two_pending_owners_cannot_resolve_each_others_work(monkeypatch):
    """Verify two pending owners cannot resolve each others work."""
    first, second = ApprovalCoordinator.for_owner("alice"), ApprovalCoordinator.for_owner("bob")
    worker_a, result_a, request_a = pending_request(first, monkeypatch)
    worker_b, result_b, request_b = pending_request(second, monkeypatch)
    try:
        assert not first.resolve_pending_request(
            True, request_id=request_b["request_id"], owner_id="alice"
        )
        assert not second.resolve_pending_request(
            True, request_id=request_a["request_id"], owner_id="bob"
        )
        assert first.resolve_pending_request(
            True, "a", request_id=request_a["request_id"], owner_id="alice"
        )
        assert second.resolve_pending_request(
            False, request_id=request_b["request_id"], owner_id="bob"
        )
        worker_a.join(2)
        worker_b.join(2)
        assert result_a == [(True, "a")]
        assert result_b == [(False, "original")]
    finally:
        first._approval_event.set()
        second._approval_event.set()
        worker_a.join(2)
        worker_b.join(2)


def test_closing_owner_denies_pending_and_future_operations(monkeypatch):
    """Verify closing owner denies pending and future operations."""
    boundary = ApprovalCoordinator.for_owner("alice")
    worker, result, pending = pending_request(boundary, monkeypatch)
    boundary.cancel_pending()
    worker.join(2)
    assert result == [(False, "original")]
    boundary.auto_approve = True
    assert boundary.request_user_permission("later", content="new") == (False, "new")


@pytest.mark.parametrize("decision,content", [("yes", "text"), (True, 123)])
def test_invalid_decision_types_do_not_authorize(monkeypatch, decision, content):
    """Verify invalid decision types do not authorize."""
    boundary = ApprovalCoordinator.for_owner("alice")
    worker, result, pending = pending_request(boundary, monkeypatch)
    try:
        assert not boundary.resolve_pending_request(
            decision, content, request_id=pending["request_id"], owner_id="alice"
        )
        boundary.resolve_pending_request(False, request_id=pending["request_id"], owner_id="alice")
        worker.join(2)
        assert result == [(False, "original")]
    finally:
        boundary._approval_event.set()
        worker.join(2)
