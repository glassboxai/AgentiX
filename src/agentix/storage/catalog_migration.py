"""Reviewed, bounded relocation of authenticated catalog grants, without model calls.

Source storage is read-only. Unchanged same-policy tools/widgets may retain their
reviewed grants at an explicitly approved destination. Applications additionally
require current package validation and an injected native/browser verifier.
"""

import hashlib
import json
import logging
import os
import re
import tempfile
import time
from collections.abc import Callable
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

from agentix.domain.tool_schema import extract_tool_schema
from agentix.lab.application_artifacts import application_digest
from agentix.security.approval_store import ApprovalStore, DataProtector, policy_fingerprint
from agentix.storage.application_catalog import ApprovedTool
from agentix.storage.catalog_lock import CatalogLock, reject_alias
from agentix.storage.installed_apps import PURPOSE, app_policy
from agentix.storage.widget_store import WidgetStore, widget_policy
from agentix.widgets.styles import validate_widget_css

logger = logging.getLogger(__name__)


def fingerprint(value: bytes) -> str:
    """Return a SHA-256 content identity; this never establishes authorization."""
    return hashlib.sha256(value).hexdigest()


class CatalogMigration:
    """Own a single explicit source/destination plan; never overwrite target grants.

    Not thread-safe: use one instance per operator. CatalogLock serializes apply
    with normal destination mutations. Filesystem checks do not defeat a hostile
    same-user process; rechecks detect ordinary concurrent edits before writes.
    """

    def __init__(
        self,
        source_home: Path,
        source_tools: Path,
        target_home: Path,
        *,
        protector: DataProtector,
        application_verifier: Callable[[Path, dict, Path], bool] | None = None,
        widget_verifier: Callable[[ApprovedTool, dict, str, Path], bool] | None = None,
    ) -> None:
        """Inject roots, authenticated protection and optional real app verification.

        Construction rejects aliases, nested/shared roots and excluded artifacts;
        it creates no files and never imports generated code.
        """
        for root in (source_home, source_tools, target_home):
            reject_alias(root)
            if not root.is_absolute() or any(p.lower() == "generated_tools" for p in root.parts):
                raise ValueError("Migration requires absolute, non-excluded roots")
        self.source = source_home.resolve()
        self.source_tools = source_tools.resolve()
        self.target = target_home.resolve()
        if self.source.is_relative_to(self.target) or self.target.is_relative_to(self.source):
            raise ValueError("Migration roots must be separate")
        self.tools = self.target / "data/tools"
        if self.source_tools.is_relative_to(self.target) or self.target.is_relative_to(
            self.source_tools
        ):
            raise ValueError("Source tools must be separate from destination")
        self.protector, self.verifier = protector, application_verifier
        self.widget_verifier = widget_verifier
        self.inputs: dict[Path, bytes | None] = {}
        self.pending: list[tuple[dict, Path, dict, bytes]] = []
        self.effective: dict[str, ApprovedTool] = {}
        self.policies: tuple[str, str, str] = ("", "", "")

    def _read(self, path: Path, *, optional: bool = False, limit: int = 1048576) -> bytes | None:
        """Capture bounded nonlinked file bytes for later freshness verification."""
        reject_alias(path)
        if not path.exists() and optional:
            self.inputs[path] = None
            return None
        if not path.is_file() or path.stat().st_nlink != 1 or path.stat().st_size > limit:
            raise ValueError("Missing, linked or oversized migration input")
        with path.open("rb") as stream:
            data = stream.read(limit + 1)
        if len(data) > limit:
            raise ValueError("Migration input exceeds limit")
        self.inputs[path] = data
        return data

    def _path(self, home: Path, kind: str, root: Path, name: str) -> Path:
        """Use the existing bounded approval namespace and name contract."""
        return ApprovalStore(
            home / "data/approvals" / kind, root, protector=self.protector, policy="path-only"
        )._path(name)

    def _records(self, kind: str, root: Path) -> list[Path]:
        """Enumerate at most 512 records in the explicit authenticated source namespace."""
        parent = self._path(self.source, kind, root, "probe").parent
        reject_alias(parent)
        paths = sorted(parent.glob("*.approval"))
        if len(paths) > 512:
            raise ValueError("Migration record limit exceeded")
        return paths

    def _decode(self, path: Path) -> tuple[dict, bytes]:
        """Unseal bounded metadata; never trust a tool-supplied JSON approval."""
        raw = self._read(path, limit=262144)
        plain = self.protector.unseal(raw)
        if len(plain) > 196608:
            raise ValueError("Unsealed metadata exceeds limit")
        value = json.loads(plain)
        if not isinstance(value, dict):
            raise ValueError("Invalid approval object")
        return value, raw

    def _grant(self, raw: bytes, root: Path, name: str, code: bytes, tests: bytes) -> dict:
        """Reuse the production validator in disposable metadata storage.

        Its revocation-on-error behavior can touch only the temporary record;
        source and destination approvals are never passed to that mutating loader.
        """
        with tempfile.TemporaryDirectory(prefix="agentix-migration-check-") as temporary:
            store = ApprovalStore(
                Path(temporary), root, protector=self.protector, policy=policy_fingerprint()
            )
            path = store._path(name)
            path.parent.mkdir(parents=True)
            path.write_bytes(raw)
            record = store.load(name, code, tests)
        if record is None:
            raise ValueError("Tool bytes, policy or reviewed coverage do not match")
        return record

    def _tool(self, path: Path, item: dict) -> tuple[Path, dict, bytes] | None:
        """Validate unchanged source grants or preserve valid newer destination grants."""
        old, raw = self._decode(path)
        name = old["tool"]
        if self._path(self.source, "tools", self.source_tools, name) != path:
            raise ValueError("Source tool identity does not match its record")
        item["name"] = name
        code = self._read(self.tools / name / (name + "_code.py"), optional=True, limit=65536)
        if code is None:
            item.update(status="skipped", reason="Tool absent at destination; not resurrected")
            return None
        tests = self._read(self.tools / name / (name + "_tests.py"), limit=65536)
        destination = self._path(self.target, "tools", self.tools, name)
        current = self._read(destination, optional=True, limit=262144)
        record = self._grant(
            raw if current is None else current,
            self.source_tools if current is None else self.tools,
            name,
            code,
            tests,
        )
        schema = extract_tool_schema(name, code.decode("utf-8"))
        self.effective[name] = ApprovedTool(
            name, name, name, code, tests, record["digest"], record["contract"], schema
        )
        if current is not None:
            item.update(status="preserved", reason="Valid destination grant retained")
            return None
        record["root"] = os.path.normcase(str(self.tools))
        return destination, record, raw

    def _widget(self, path: Path, item: dict) -> tuple[Path, dict, bytes] | None:
        """Require identical widget bytes, tool review, CSS, tests and widget policy."""
        record, raw = self._decode(path)
        if set(record) != {"binding", "widget", "proposal", "css", "tests"}:
            raise ValueError("Invalid protected widget record")
        name = record["binding"]["tool"]
        if self._path(self.source, "widgets", self.source_tools, name) != path:
            raise ValueError("Source widget identity does not match its record")
        item["name"] = name
        tool = self.effective.get(name)
        if tool is None:
            raise ValueError("No compatible approved destination tool")
        service = WidgetStore(
            SimpleNamespace(TOOLS_ROOT_DIR=str(self.tools)),
            self.target / "data/approvals/widgets",
            protector=self.protector,
        )
        binding = service._binding(tool)
        old_binding = dict(binding, root=os.path.normcase(str(self.source_tools)))
        if {k: v for k, v in record["binding"].items() if k != "contract"} != {
            k: v for k, v in old_binding.items() if k != "contract"
        }:
            raise ValueError("Widget tool contract or policy differs from its prior review")
        item["reverify_widget"] = record["binding"]["contract"] != binding["contract"]
        proposal = record["proposal"]
        service._validate(tool, proposal)
        for suffix, key, proposal_key in (
            ("_widget.py", "widget", "widget_code"),
            ("_widget_tests.py", "tests", "tests_code"),
            ("_widget.css", "css", None),
        ):
            body = self._read(self.tools / name / (name + suffix), limit=65536)
            if fingerprint(body) != record[key] or (
                proposal_key and body != proposal[proposal_key].encode("utf-8")
            ):
                raise ValueError("Widget bytes differ from their protected review")
            if key == "css":
                validate_widget_css(body.decode("utf-8"), name)
        record["binding"] = binding
        destination = self._path(self.target, "widgets", self.tools, name)
        existing = self._read(destination, optional=True, limit=262144)
        if existing is not None:
            if json.loads(self.protector.unseal(existing)) != record:
                raise ValueError("Destination widget approval conflict; retained unchanged")
            item.update(status="preserved", reason="Identical destination widget approval retained")
            return None
        return destination, record, raw

    def _application(self, path: Path, item: dict) -> tuple[Path, dict, bytes] | None:
        """Bind original review and current package; stale templates remain blocked."""
        record, raw = self._decode(path)
        identity, folder = record["id"], record["folder"]
        if not re.fullmatch(r"[0-9a-f]{32}", identity) or not re.fullmatch(
            r"[a-z0-9][a-z0-9_-]{0,99}", folder
        ):
            raise ValueError("Invalid application identity")
        item["name"] = folder
        old_root, new_root = self.source / "data/applications", self.target / "data/applications"
        if (
            record.get("purpose") != PURPOSE
            or record.get("root") != os.path.normcase(str(old_root))
            or self._path(self.source, "applications", old_root, "app_" + identity) != path
        ):
            raise ValueError("Application protected identity does not match")
        review = self._read(self.target / "data/reviews" / identity / "review.json")
        if fingerprint(review) != record["review"]:
            raise ValueError("Application review changed")
        package = new_root / folder
        reject_alias(package)
        for member in sorted(package.iterdir()):
            if member.name != "__pycache__":
                self._read(member, limit=65536)
        if application_digest(package) != record["digest"]:
            raise ValueError("Application package changed after review")
        for name, dependency in record["dependencies"].items():
            tool = self.effective.get(name)
            if tool is None or any(
                dependency[key] != expected
                for key, expected in {
                    "code_sha256": fingerprint(tool.code),
                    "tests_sha256": fingerprint(tool.tests),
                    "contract_digest": tool.contract_digest,
                    "function": tool.function,
                }.items()
            ):
                raise ValueError("Application dependency differs from approved destination tool")
        destination = self._path(self.target, "applications", new_root, "app_" + identity)
        record.update(root=os.path.normcase(str(new_root)), policy=app_policy())
        existing = self._read(destination, optional=True, limit=262144)
        if existing is not None:
            if json.loads(self.protector.unseal(existing)) != record:
                raise ValueError("Destination application approval conflict; retained unchanged")
            item.update(
                status="preserved", reason="Current destination application approval retained"
            )
            return None
        return destination, record, raw

    def plan(self) -> dict:
        """Return safe statuses and a digest binding all observed inputs, without target writes."""
        self.inputs, self.pending, self.effective = {}, [], {}
        self.policies = (policy_fingerprint(), widget_policy(), app_policy())
        items = []
        for kind, root, check in (
            ("tools", self.source_tools, self._tool),
            ("widgets", self.source_tools, self._widget),
            ("applications", self.source / "data/applications", self._application),
        ):
            for path in self._records(kind, root):
                item = {"kind": kind, "name": path.stem, "status": "ready", "reason": ""}
                try:
                    pending = check(path, item)
                    if pending is not None:
                        self.pending.append((item, *pending))
                except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
                    item.update(status="blocked", reason=str(error)[:250])
                items.append(item)
        binding = {
            "items": items,
            "inputs": {
                str(p): fingerprint(b) if b is not None else None
                for p, b in sorted(self.inputs.items())
            },
            "policies": self.policies,
        }
        return {
            "items": items,
            "review_digest": fingerprint(json.dumps(binding, sort_keys=True).encode()),
        }

    def _fresh(self) -> None:
        """Reject input drift and newly introduced aliases immediately before publication."""
        if self.policies != (policy_fingerprint(), widget_policy(), app_policy()):
            raise ValueError("Migration review is stale; maintained policy changed")
        snapshot = dict(self.inputs)
        try:
            for path, expected in snapshot.items():
                actual = self._read(path, optional=expected is None)
                if actual != expected:
                    raise ValueError("Migration review is stale; inputs changed")
        finally:
            self.inputs = snapshot

    def apply(self, reviewed_digest: str) -> dict:
        """Apply one exact reviewed plan with backups; applications require fresh real gates.

        Existing grants are never overwritten. Errors leave original grants intact;
        per-entry outcomes and backups allow an operator to inspect partial progress.
        This is not a crash-atomic multi-file transaction.
        """
        with CatalogLock(self.target / "data"):
            plan = self.plan()
            if reviewed_digest != plan["review_digest"]:
                raise ValueError("Exact migration review digest required; review is stale")
            operation = self.target / "migrations" / uuid4().hex
            reject_alias(operation)
            operation.mkdir(parents=True, exist_ok=False)
            for item, destination, record, raw in self.pending:
                started = time.monotonic()
                try:
                    self._fresh()
                    if item.get("reverify_widget"):
                        if self.widget_verifier is None:
                            raise ValueError(
                                "Changed tool cases require fresh native/browser widget verification"
                            )
                        tool = self.effective[item["name"]]
                        css = self.inputs[
                            self.tools / tool.tool_name / (tool.tool_name + "_widget.css")
                        ].decode("utf-8")
                        evidence = operation / ("widget-" + tool.tool_name)
                        evidence.mkdir()
                        if (
                            self.widget_verifier(tool, record["proposal"], css, evidence)
                            is not True
                        ):
                            raise ValueError("Independent widget verification failed")
                        self._fresh()
                    if item["kind"] == "applications":
                        if self.verifier is None:
                            raise ValueError(
                                "Current native/browser application verification is required"
                            )
                        package = self.target / "data/applications" / record["folder"]
                        review = json.loads(
                            self.inputs[self.target / "data/reviews" / record["id"] / "review.json"]
                        )
                        evidence = operation / record["id"]
                        evidence.mkdir()
                        if self.verifier(package, review, evidence) is not True:
                            raise ValueError("Independent application verification failed")
                        self._fresh()
                        if application_digest(package) != record["digest"]:
                            raise ValueError("Application changed during verification")
                    backup = operation / (item["kind"] + "-" + destination.name)
                    backup.write_bytes(raw)
                    sealed = self.protector.seal(json.dumps(record, sort_keys=True).encode())
                    if len(sealed) > 262144:
                        raise ValueError("Migrated record exceeds limit")
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    reject_alias(destination)
                    with destination.open("xb") as stream:
                        stream.write(sealed)
                    self.inputs[destination] = sealed
                    item.update(
                        status="migrated", reason="Authenticated relocation; source unchanged"
                    )
                except Exception as error:
                    # Native/browser failures are per-entry denials, never approval evidence.
                    reason = (
                        str(error)[:250]
                        if isinstance(error, (OSError, ValueError))
                        else type(error).__name__
                    )
                    item.update(status="blocked", reason=reason)
                finally:
                    item["duration_seconds"] = round(time.monotonic() - started, 3)
                    logger.info(
                        "operation=%s stage=catalog_migration kind=%s outcome=%s duration_seconds=%.3f",
                        operation.name,
                        item["kind"],
                        item["status"],
                        item["duration_seconds"],
                    )
            plan["operation_id"] = operation.name
            plan["evidence"] = str(operation)
            (operation / "receipt.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
            return plan
