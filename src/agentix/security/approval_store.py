"""Protected durable approvals, separate from untrusted tool artifacts.

Records contain hashes and reviewed declarative data, never executable trust
markers supplied by a tool. Each atomic record is bound to root/tool/policy.
Concurrent revocation is observed on the next check, not instant cancellation.
"""

import hashlib
import json
import logging
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Protocol

from agentix.diagnostics import log_event
from agentix.security.data_protection import WindowsDataProtection

logger = logging.getLogger(__name__)


class DataProtector(Protocol):
    """Injected authenticated Windows protection; tests use explicit doubles."""

    def seal(self, data: bytes) -> bytes:
        """Protect bounded serialized authorization bytes or raise."""
        ...

    def unseal(self, data: bytes) -> bytes:
        """Recover authenticated bytes or raise on failure."""
        ...


def policy_fingerprint() -> str:
    """Hash named maintained security sources; never traverse generated storage."""
    root = Path(__file__).resolve().parents[1]
    digest = hashlib.sha256(b"AgentiX-reviewed-approval-v2")
    for name in (
        "security/approval_store.py",
        "security/data_protection.py",
        "security/reuse_policy.py",
        "security/verification.py",
        "execution.py",
        "security/acceptance.py",
        "sandbox/__init__.py",
        "sandbox_worker.py",
        "sandbox/windows_process.py",
        "sandbox/profile_cleanup.py",
        "storage/locations.py",
        "application/tool_repair.py",
        "agents/repair_acceptance.py",
        "security/paths.py",
        "security/__init__.py",
        "storage/tool_publication.py",
        "domain/tool_schema.py",
    ):
        digest.update(name.encode())
        digest.update((root / name).read_bytes())
    return digest.hexdigest()


class ApprovalStore:
    """Own per-tool protected records under a user-local directory outside tools."""

    def __init__(
        self, directory: Path, tools_root: Path, *, protector: DataProtector, policy: str
    ) -> None:
        """Bind canonical location and policy; construction performs no writes."""
        self.directory = Path(directory).resolve()
        self.root = os.path.normcase(str(Path(tools_root).resolve()))
        if self.directory.is_relative_to(Path(self.root)):
            raise ValueError("Approval storage must be outside tool storage")
        self.protector, self.policy = protector, policy
        self.namespace = hashlib.sha256(self.root.encode()).hexdigest()

    def _path(self, tool_name: str) -> Path:
        """Return only an opaque owned filename after validating the public tool ID."""
        if not isinstance(tool_name, str) or not re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_]{0,127}", tool_name
        ):
            raise ValueError("Invalid approval tool name")
        parent = self.directory / self.namespace
        if self.directory.is_symlink() or parent.is_symlink() or parent.resolve() != parent:
            raise ValueError("Approval directory links are not supported")
        path = parent / (hashlib.sha256(tool_name.encode()).hexdigest() + ".approval")
        if path.is_symlink():
            raise ValueError("Approval record links are not supported")
        return path

    def save(
        self,
        tool_name: str,
        code: bytes,
        tests: bytes,
        digest: str,
        functions: frozenset[str],
        contract: dict[str, Any],
    ) -> None:
        """Atomically persist a trusted host's successful reviewed execution grant.

        Caller must already enforce human acceptance and actual successful isolated
        execution. This is not a model-facing API. Errors propagate to the ledger.
        """
        from agentix.security.acceptance import parse_contract

        contract = parse_contract(json.dumps(contract, allow_nan=False))
        record = dict(
            schema=1,
            root=self.root,
            tool=tool_name,
            code=hashlib.sha256(code).hexdigest(),
            tests=hashlib.sha256(tests).hexdigest(),
            policy=self.policy,
            digest=digest,
            functions=sorted(functions),
            contract=contract,
        )
        raw = json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        if len(raw) > 98304:
            raise ValueError("Approval record exceeds limit")
        sealed = self.protector.seal(raw)
        if len(sealed) > 262144:
            raise ValueError("Protected record exceeds limit")
        path = self._path(tool_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix=".approval-", dir=path.parent)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(sealed)
                stream.flush()
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)

    def load(self, tool_name: str, code: bytes, tests: bytes) -> dict[str, Any] | None:
        """Return valid protected metadata only for exact current artifacts/policy.

        Missing records grant nothing. Other failures revoke the owned record and
        return nothing; diagnostic events never include source, cases or secrets.
        """
        try:
            path = self._path(tool_name)
            if not path.exists():
                return None
            with path.open("rb") as stream:
                sealed = stream.read(262145)
            if len(sealed) > 262144:
                raise ValueError("Protected record exceeds limit")
            plain = self.protector.unseal(sealed)
            if len(plain) > 98304:
                raise ValueError("Approval metadata exceeds limit")
            record = json.loads(plain)
            if not isinstance(record, dict) or set(record) != {
                "schema",
                "root",
                "tool",
                "code",
                "tests",
                "policy",
                "digest",
                "functions",
                "contract",
            }:
                raise ValueError("Invalid approval schema")
            if (
                type(record["schema"]) is not int
                or record["schema"] != 1
                or any(
                    record[key] != value
                    for key, value in {
                        "root": self.root,
                        "tool": tool_name,
                        "code": hashlib.sha256(code).hexdigest(),
                        "tests": hashlib.sha256(tests).hexdigest(),
                    }.items()
                )
            ):
                raise ValueError("Approval identity changed")
            if record["policy"] != self.policy:
                # A policy rotation is recoverable: keep the intact record so an
                # explicit reseal can rebind the same reviewed bytes. It still
                # grants nothing until that happens.
                log_event(logger, "durable_approval_policy_stale", level=logging.WARNING)
                return None
            from agentix.security.acceptance import parse_contract

            contract = parse_contract(json.dumps(record["contract"], allow_nan=False))
            functions = record["functions"]
            if (
                not isinstance(functions, list)
                or not 1 <= len(functions) <= 16
                or any(
                    not isinstance(name, str)
                    or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,127}", name)
                    for name in functions
                )
                or set(functions) != {case["function"] for case in contract["cases"]}
                or not isinstance(record["digest"], str)
                or not 1 <= len(record["digest"]) <= 128
            ):
                raise ValueError("Invalid approved function coverage")
            return record
        except (OSError, ValueError, TypeError, KeyError, RecursionError) as exc:
            log_event(logger, "durable_approval_invalid", error=exc, level=logging.WARNING)
            self.revoke(tool_name)
            return None

    def peek(self, tool_name: str, code: bytes, tests: bytes) -> dict[str, Any] | None:
        """Validate a record for read-only presentation without revoking anything.

        Presentation paths must never destroy an owner grant. Unlike `load`, a
        stale policy or an unreadable record returns None and leaves the sealed
        file untouched; only an explicit reseal or revoke may change it.
        """
        try:
            path = self._path(tool_name)
            if not path.exists():
                return None
            with path.open("rb") as stream:
                sealed = stream.read(262145)
            if len(sealed) > 262144:
                return None
            plain = self.protector.unseal(sealed)
            if len(plain) > 98304:
                return None
            record = json.loads(plain)
            if not isinstance(record, dict) or set(record) != {
                "schema",
                "root",
                "tool",
                "code",
                "tests",
                "policy",
                "digest",
                "functions",
                "contract",
            }:
                return None
            if (
                type(record["schema"]) is not int
                or record["schema"] != 1
                or record["root"] != self.root
                or record["tool"] != tool_name
                or record["code"] != hashlib.sha256(code).hexdigest()
                or record["tests"] != hashlib.sha256(tests).hexdigest()
            ):
                return None
            return record
        except (OSError, ValueError, TypeError, KeyError, RecursionError):
            return None

    def reseal(self, tool_name: str, code: bytes, tests: bytes) -> str | None:
        """Rebind an intact record to the current policy without executing the tool.

        Returns None on success, otherwise a bounded reason: `missing` when no
        record exists, `changed` when the sealed code or test digests differ, and
        `invalid` when the record or its reviewed contract cannot be revalidated.
        Only the policy identity may differ. Missing, unreadable or changed records
        stay revoked; no source, cases or secrets are logged.
        """
        from agentix.security.acceptance import parse_contract

        try:
            path = self._path(tool_name)
            if not path.exists():
                return "missing"
            with path.open("rb") as stream:
                sealed = stream.read(262145)
            if len(sealed) > 262144:
                return "invalid"
            plain = self.protector.unseal(sealed)
            if len(plain) > 98304:
                return "invalid"
            record = json.loads(plain)
            if not isinstance(record, dict) or set(record) != {
                "schema",
                "root",
                "tool",
                "code",
                "tests",
                "policy",
                "digest",
                "functions",
                "contract",
            }:
                return "invalid"
            if (
                type(record["schema"]) is not int
                or record["schema"] != 1
                or record["root"] != self.root
                or record["tool"] != tool_name
            ):
                return "invalid"
            if (
                record["code"] != hashlib.sha256(code).hexdigest()
                or record["tests"] != hashlib.sha256(tests).hexdigest()
            ):
                return "changed"
            contract = parse_contract(json.dumps(record["contract"], allow_nan=False))
            functions = record["functions"]
            if (
                not isinstance(functions, list)
                or not 1 <= len(functions) <= 16
                or any(
                    not isinstance(name, str)
                    or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,127}", name)
                    for name in functions
                )
                or set(functions) != {case["function"] for case in contract["cases"]}
                or not isinstance(record["digest"], str)
                or not 1 <= len(record["digest"]) <= 128
            ):
                return "invalid"
            self.save(tool_name, code, tests, record["digest"], frozenset(functions), contract)
            log_event(logger, "durable_approval_resealed")
            return None
        except (OSError, ValueError, TypeError, KeyError, RecursionError) as exc:
            log_event(logger, "durable_approval_reseal_refused", error=exc, level=logging.WARNING)
            return "invalid"

    def revoke(self, tool_name: str) -> None:
        """Remove only this tool's owned record; missing records are already revoked."""
        self._path(tool_name).unlink(missing_ok=True)


def user_approval_store(tools_root: Path) -> ApprovalStore:
    """Compose user-local durable Windows protection lazily, without native calls."""
    from agentix.storage.locations import data_directory

    directory = data_directory() / "approvals" / "tools"
    return ApprovalStore(
        directory, tools_root, protector=WindowsDataProtection(), policy=policy_fingerprint()
    )
