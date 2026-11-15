"""Rejected-tool repair preserves human acceptance and host-compared execution."""

import json
import threading
import time

import pytest
from test_installed_apps import library
from test_widget_reuse import Protector
from trusted_sandbox import TrustedFixtureSandbox, approve_next_review

from agentix.controllers.tool_controller import UiController
from agentix.security import SecurityManager
from agentix.security.approval_store import ApprovalStore
from agentix.storage.catalog import ToolCatalog
from agentix.tools import ArtifactTools

CODE = '"""Trusted arithmetic fixture."""\ndef double(value):\n    return value * 2\n'
TESTS = "import unittest\nfrom repair_demo_code import double\nclass Tests(unittest.TestCase):\n    def test_normal(self):\n        self.assertEqual(double(2), 4)\n"
CASES = {
    "version": 1,
    "cases": [
        {
            "id": "normal",
            "purpose": "Double a normal value",
            "function": "double",
            "kwargs": {"value": 2},
            "expect": {"kind": "value", "value": 4},
        }
    ],
}


def fixture(tmp_path):
    """Compose the real protocol with an explicitly non-native trusted-fixture double."""
    root = tmp_path / "tools"
    root.mkdir()
    security = SecurityManager.for_owner("repair-owner")
    security.TOOLS_ROOT_DIR = str(root)
    security.operation_id = "new-repair-operation"
    store = ApprovalStore(tmp_path / "grants", root, protector=Protector(), policy="fixture")
    operations = ArtifactTools(security, sandbox=TrustedFixtureSandbox(), approval_store=store)
    return root, security, operations


def repair_service(tmp_path, security, operations):
    """Fail until the explicitly approved repair workflow exists."""
    try:
        from agentix.application.tool_repair import RejectedTool, ToolRepair
    except ImportError:
        pytest.fail("Rejected-tool repair is not implemented")
    return ToolRepair(
        security, operations, library(tmp_path), propose_cases=lambda context: json.dumps(CASES)
    ), RejectedTool("repair_demo", CODE, TESTS, "Double a numeric input")


def test_invalid_tests_leave_both_files_unchanged(tmp_path):
    """Validate every buffer before revocation or the first filesystem write."""
    root, security, operations = fixture(tmp_path)
    service, draft = repair_service(tmp_path, security, operations)
    folder = root / "repair_demo"
    folder.mkdir()
    (folder / "repair_demo_code.py").write_text("original code", encoding="utf-8")
    (folder / "repair_demo_tests.py").write_text("original tests", encoding="utf-8")
    with pytest.raises(ValueError):
        service.save_and_validate(draft, CODE, "def broken(")
    assert (folder / "repair_demo_code.py").read_text(encoding="utf-8") == "original code"
    assert (folder / "repair_demo_tests.py").read_text(encoding="utf-8") == "original tests"


def test_repair_retests_requires_review_and_establishes_reuse(tmp_path):
    """Unit test success cannot skip manual acceptance or the real worker protocol."""
    root, security, operations = fixture(tmp_path)
    service, draft = repair_service(tmp_path, security, operations)
    thread, errors = approve_next_review(security)
    result = service.save_and_validate(draft, CODE, TESTS)
    thread.join(10)
    assert not errors and not thread.is_alive()
    assert "ACCEPTANCE_VERIFIED" in result
    assert operations.verification.prepare_reuse("repair_demo")
    assert (root / "repair_demo/repair_demo_tests.py").read_bytes() == TESTS.encode()


def test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection(tmp_path):
    """Retain the proposed bytes even when rejecting the file prevented its creation."""
    root, security, operations = fixture(tmp_path)
    controller = UiController(
        lambda query: "",
        ToolCatalog(root).render,
        security,
        lambda **values: values,
        tool_operations=operations,
    )
    worker = threading.Thread(
        target=lambda: security.request_user_permission(
            str(root / "repair_demo/repair_demo_code.py"), "write/overwrite file", CODE
        )
    )
    worker.start()
    deadline = time.monotonic() + 3
    while security.get_pending_request() is None and time.monotonic() < deadline:
        time.sleep(0.005)
    pending = security.get_pending_request()
    assert pending
    try:
        assert not controller.on_reject("stale")
        assert getattr(controller, "_rejected_tool", None) is None
        assert controller.on_reject(pending["request_id"])
        draft = controller._rejected_tool
        assert draft.tool_name == "repair_demo" and draft.code == CODE
        assert not (root / "repair_demo/repair_demo_code.py").exists()
    finally:
        security.cancel_pending()
        worker.join(5)
