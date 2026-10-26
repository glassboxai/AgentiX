"""REUSE-002: protected approvals survive fresh ledgers without trusting artifacts."""

import hmac
from pathlib import Path

import pytest
from test_execution_handoff import authorize_fixture


class TestProtector:
    """Authenticate trusted fixture records; this double is not Windows protection."""

    __test__ = False

    def seal(self, data: bytes) -> bytes:
        """Attach a test-only keyed digest so tampering fails observably."""
        return hmac.digest(b"independent-fixture-key", data, "sha256") + data

    def unseal(self, data: bytes) -> bytes:
        """Reject altered records rather than silently decoding arbitrary JSON."""
        if not hmac.compare_digest(
            data[:32], hmac.digest(b"independent-fixture-key", data[32:], "sha256")
        ):
            raise ValueError("Invalid fixture seal")
        return data[32:]


def configure_store(system, directory: Path, *, policy: str = "fixture-policy"):
    """Inject temporary protected persistence into the actual ledger."""
    from agentix.approval_store import ApprovalStore

    protector = TestProtector()
    store = ApprovalStore(directory, system.root, protector=protector, policy=policy)
    system.custom_tools.verification.store = store
    return store


def publish(system, tmp_path):
    """Install independently authored code and publish only after actual success."""
    store = configure_store(system, tmp_path / "approvals")
    ledger = authorize_fixture(system)
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":10}').endswith(
        "12"
    )
    return store, ledger


def test_successful_review_survives_a_new_owner_and_ledger(system, tmp_path):
    """Another session can use intact approved bytes without tests or review."""
    from agentix.verification import VerificationLedger

    store, _ = publish(system, tmp_path)
    fresh_security = system.security.for_owner("new-browser-owner")
    fresh_security.TOOLS_ROOT_DIR = str(system.root)
    fresh = VerificationLedger(fresh_security, store=store)
    assert fresh.prepare_reuse("adder")
    assert fresh.is_verified("adder", "add")
    assert fresh.execution_result() is None
    assert not fresh.is_verified("adder", "other")


@pytest.mark.parametrize("mutation", ["code", "tests", "policy", "root", "tamper", "plaintext"])
def test_durable_approval_rejects_changed_identity_and_tampering(system, tmp_path, mutation):
    """Changed source, policy, location and unauthenticated records cannot authorize."""
    from agentix.verification import VerificationLedger

    store, ledger = publish(system, tmp_path)
    if mutation in ("code", "tests"):
        path = system.root / "adder" / f"adder_{mutation}.py"
        original = path.read_bytes()
        path.write_bytes(original + b"\n# changed")
    elif mutation == "policy":
        store = configure_store(system, tmp_path / "approvals", policy="new-policy")
    elif mutation == "root":
        from agentix.approval_store import ApprovalStore

        store = ApprovalStore(
            tmp_path / "approvals",
            tmp_path / "different-root",
            protector=TestProtector(),
            policy="fixture-policy",
        )
    else:
        records = list((tmp_path / "approvals").rglob("*.approval"))
        assert len(records) == 1
        records[0].write_bytes(
            b'{"approved":true}' if mutation == "plaintext" else records[0].read_bytes()[:-1] + b"x"
        )
    fresh = VerificationLedger(system.security, store=store)
    assert not fresh.prepare_reuse("adder")
    if mutation in ("code", "tests"):
        path.write_bytes(original)
        assert not ledger.prepare_reuse("adder")


def test_session_close_retains_durable_approval_but_explicit_revoke_removes_it(system, tmp_path):
    """Closing a browser expires its work, not an approval owned by the Windows user."""
    from agentix.verification import VerificationLedger

    store, ledger = publish(system, tmp_path)
    system.security.cancel_pending()
    assert not ledger.prepare_reuse("adder")
    other = system.security.for_owner("next-owner")
    other.TOOLS_ROOT_DIR = str(system.root)
    fresh = VerificationLedger(other, store=store)
    assert fresh.prepare_reuse("adder")
    fresh.revoke_acceptance("adder")
    assert not VerificationLedger(other, store=store).prepare_reuse("adder")


def test_review_without_actual_success_creates_no_durable_record(system, tmp_path):
    """Manual review alone never persists an executable grant."""
    configure_store(system, tmp_path / "approvals")
    authorize_fixture(system)
    assert not list((tmp_path / "approvals").rglob("*.approval"))


def test_durable_sensitive_tool_never_persists_per_call_permission(system, tmp_path, monkeypatch):
    """A fresh runtime must ask again for sensitive actions despite durable review."""
    from agentix.tools import ArtifactTools

    store = configure_store(system, tmp_path / "approvals")
    ledger = authorize_fixture(system)
    path = system.root / "adder" / "adder_code.py"
    path.write_text("def add(a,b=2):\n    if a < 0: open('output.txt','w')\n    return a+b")
    code, tests = ledger.snapshot("adder")
    assert ledger.record(
        "adder",
        code,
        tests,
        dict(kind="tests", run=1, failures=0, errors=0, skipped=0, successful=True),
        isolated=True,
        exit_code=0,
    )
    reviewed = {
        "version": 1,
        "cases": [
            {
                "id": "sum_case",
                "purpose": "Add two",
                "function": "add",
                "kwargs": {"a": 10},
                "expect": {"kind": "value", "value": 12},
            }
        ],
    }
    assert ledger.authorize(
        "adder", code, tests, "reviewed", frozenset({"add"}), reviewed_contract=reviewed
    )
    monkeypatch.setattr(
        system.security, "request_user_permission", lambda *args, **kwargs: (True, "")
    )
    assert system.custom_tools.execute_generated_tool_tool("adder", "add", '{"a":10}').endswith(
        "12"
    )
    fresh_security = system.security.for_owner("new-sensitive-owner")
    fresh_security.TOOLS_ROOT_DIR = str(system.root)
    seen = []

    def deny(*args, **kwargs):
        """Deny a separate exact-call permission in the new browser owner."""
        seen.append((args, kwargs))
        return False, ""

    monkeypatch.setattr(fresh_security, "request_user_permission", deny)
    fresh = ArtifactTools(
        fresh_security, sandbox=system.custom_tools.executor.sandbox, approval_store=store
    )
    assert fresh.verify_existing_tool_tool("adder").startswith("REUSE_READY:")
    assert fresh.execute_generated_tool_tool("adder", "add", '{"a":40}').startswith(
        "EXECUTION_DENIED:"
    )
    assert len(seen) == 1 and seen[0][1]["require_manual"] is True
    assert fresh.verification.execution_result() is None
