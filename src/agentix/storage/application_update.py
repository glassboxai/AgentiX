"""V7-048: stage exact authenticated applications for reviewed runtime updates.

Only the schema-3 maintained app.py may change executable bytes. Generated logic,
widgets, dependency code/tests, independent cases and geometry remain unchanged.
Current native/browser gates precede any installed write. No model is constructed.
"""

import copy
import json
import logging
import os
import re
import tempfile
import time
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from agentix.application.general_package import validate_manifest
from agentix.lab.application_artifacts import _identity, application_digest
from agentix.layout_contracts import application_layout_ids, validate_layout
from agentix.storage.catalog_lock import CatalogLock, reject_alias
from agentix.storage.catalog_migration import CatalogMigration, fingerprint
from agentix.storage.installed_apps import PURPOSE, InstalledApps, app_policy
from agentix.storage.usage import app_in_use

logger = logging.getLogger(__name__)


@dataclass
class Update:
    """Immutable-by-contract staged bytes and original proof for one review lifetime."""

    item: dict
    record: dict
    source_record: bytes
    original: dict[str, bytes]
    updated: dict[str, bytes]
    review_path: Path
    old_review: bytes
    new_review: bytes
    approval_path: Path


class ApplicationUpdates:
    """Compose the catalog's authenticated snapshot reader with package staging.

    A single operator owns this instance. CatalogMigration owns bounded input
    capture/freshness and current tool-grant validation; this service owns only
    application transformations and installation. Source remains read-only.
    """

    def __init__(self, migration: CatalogMigration) -> None:
        """Inject an explicit migration snapshot; construction performs no writes."""
        self.migration = migration
        self.prepared: list[Update] = []
        self.widget_approvals: set[str] = set()

    def _prepare(self, path: Path, item: dict) -> Update | None:
        """Authenticate old bytes and prepare the only permitted runtime/metadata edits."""
        m = self.migration
        record, source_record = m._decode(path)
        identity, folder = record["id"], record["folder"]
        if (
            not re.fullmatch(r"[0-9a-f]{32}", identity)
            or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,99}", folder)
            or record.get("purpose") != PURPOSE
            or record.get("root") != os.path.normcase(str(m.source / "data/applications"))
            or m._path(m.source, "applications", m.source / "data/applications", "app_" + identity)
            != path
        ):
            raise ValueError("Original protected application identity is invalid")
        item["name"] = folder
        approval = m._path(
            m.target, "applications", m.target / "data/applications", "app_" + identity
        )
        existing = m._read(approval, optional=True, limit=262144)
        if existing is not None:
            library = InstalledApps(
                m.target / "data/applications",
                m.target / "data/approvals/applications",
                protector=m.protector,
            )
            current = library.get(identity)
            if self._dependencies(current.dependencies) != current.dependencies:
                raise ValueError(
                    "Existing v7 approval has changed dependencies; retained unchanged"
                )
            item.update(status="preserved", reason="Valid v7 application approval retained")
            return None
        review_path = m.target / "data/reviews" / identity / "review.json"
        old_review = m._read(review_path)
        if fingerprint(old_review) != record["review"]:
            raise ValueError("Original independent review changed")
        review = json.loads(old_review)
        package = m.target / "data/applications" / folder
        reject_alias(package)
        manifest_raw = m._read(package / "application.json", limit=65536)
        manifest = json.loads(manifest_raw)
        expected = validate_manifest(manifest) | {"application.json"}
        if {p.name for p in package.iterdir()} - {"__pycache__", "config.json"} != expected:
            raise ValueError("Unexpected application members")
        original = {name: m._read(package / name, limit=65536) for name in sorted(expected)}
        if _identity(tuple(original.items())) != record["digest"]:
            raise ValueError("Original reviewed executable package changed")
        if review["manifest"] != manifest:
            raise ValueError("Original review manifest differs from installed package")
        for name, expected_hash in manifest["files"].items():
            if fingerprint(original[name]) != expected_hash:
                raise ValueError("Original manifest binding changed")
        layout = m._read(package / "config.json", optional=True, limit=65536)
        if layout is not None:
            validate_layout(json.loads(layout), allowed=application_layout_ids(manifest))
            original["config.json"] = layout
        dependencies = self._dependencies(record["dependencies"])
        for name in dependencies:
            tool = m.effective[name]
            if (
                original[name + "_code.py"] != tool.code
                or manifest["tools"][name] != tool.schema
                or review["approved_tool_tests"][name].encode("utf-8") != tool.tests
            ):
                raise ValueError(
                    "Embedded application dependency differs from current approved bytes"
                )
        updated = dict(original)
        changed = []
        if manifest["schema_version"] == 3:
            from agentix.application.code_package import runtime_template

            current_template = runtime_template("app.py").read_bytes()
            if updated["app.py"] != current_template:
                updated["app.py"] = current_template
                manifest = copy.deepcopy(manifest)
                manifest["files"]["app.py"] = fingerprint(current_template)
                updated["application.json"] = json.dumps(manifest, indent=2).encode()
                changed.append("app.py")
        # Validate every maintained runtime member against current policy in a
        # disposable directory; the live package is never repaired to pass a test.
        with tempfile.TemporaryDirectory(prefix="agentix-app-update-check-") as temporary:
            staged = Path(temporary)
            self._stage(staged, updated)
            digest = application_digest(staged)
        new_review = copy.deepcopy(review)
        new_review["manifest"] = manifest
        new_review["source_files"] = {
            name: body.decode("utf-8")
            for name, body in updated.items()
            if name not in {"application.json", "config.json"}
        }
        new_review["approved_catalog_dependencies"] = dependencies
        new_review["tool_acceptance_contracts"] = {
            name: m.effective[name].reviewed_contract for name in dependencies
        }
        for name in dependencies:
            matches = all(
                m._read(m.tools / name / (name + suffix), limit=65536) == updated[name + suffix]
                for suffix in ("_widget.py", "_widget.css", "_widget_tests.py")
            )
            new_review["widget_reuse"][name] = (
                "approved widget reused"
                if matches and name in self.widget_approvals
                else "Reviewed application widget requires current checks"
            )
        if new_review["independent_acceptance"] != review["independent_acceptance"]:
            raise ValueError("Independent acceptance must never change during migration")
        new_raw = json.dumps(new_review, ensure_ascii=True, indent=2).encode()
        if len(new_raw) > 1048576:
            raise ValueError("Updated review exceeds limit")
        new_record = dict(
            record,
            root=os.path.normcase(str(m.target / "data/applications")),
            digest=digest,
            review=fingerprint(new_raw),
            policy=app_policy(),
            dependencies=dependencies,
        )
        item.update(
            changed_runtime_files=changed,
            updated_digest=digest,
            updated_review_sha256=fingerprint(new_raw),
        )
        return Update(
            item,
            new_record,
            source_record,
            original,
            updated,
            review_path,
            old_review,
            new_raw,
            approval,
        )

    def _dependencies(self, previous: dict) -> dict:
        """Refresh case bindings only when current approved dependency bytes match exactly."""
        m = self.migration
        current = copy.deepcopy(previous)
        for name, dependency in current.items():
            tool = m.effective.get(name)
            if tool is None or any(
                dependency.get(key) != value
                for key, value in {
                    "code_sha256": fingerprint(tool.code),
                    "tests_sha256": fingerprint(tool.tests),
                    "function": tool.function,
                }.items()
            ):
                raise ValueError("Missing or changed approved application dependency")
            # Never rely on a source-only grant that has not reached the v7 root.
            grant = m._read(m._path(m.target, "tools", m.tools, name), limit=262144)
            m._grant(grant, m.tools, name, tool.code, tool.tests)
            dependency["contract_digest"] = tool.contract_digest
        return current

    @staticmethod
    def _stage(folder: Path, files: dict[str, bytes]) -> None:
        """Write closed server-selected filename bytes to a fresh owned staging directory."""
        for name, body in files.items():
            (folder / name).write_bytes(body)

    def plan(self, names: list[str]) -> dict:
        """Return exact candidate identities without changing installed bytes or grants."""
        if not names or len(names) > 16 or len(names) != len(set(names)):
            raise ValueError("Select one to sixteen distinct application folders")
        m = self.migration
        catalog_plan = m.plan()
        self.widget_approvals = {
            item["name"]
            for item in catalog_plan["items"]
            if item["kind"] == "widgets" and item["status"] == "preserved"
        }
        self.prepared = []
        items = []
        found = set()
        for path in m._records("applications", m.source / "data/applications"):
            record, _ = m._decode(path)
            name = record.get("folder")
            if name not in names:
                continue
            if name in found:
                raise ValueError("Ambiguous source application identity")
            found.add(name)
            item = {"name": name, "status": "ready", "reason": ""}
            try:
                update = self._prepare(path, item)
                if update is not None:
                    self.prepared.append(update)
            except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
                item.update(status="blocked", reason=str(error)[:250])
            items.append(item)
        for name in sorted(set(names) - found):
            items.append(
                {"name": name, "status": "blocked", "reason": "No protected source application"}
            )
        binding = {
            "items": items,
            "inputs": {
                str(p): fingerprint(b) if b is not None else None
                for p, b in sorted(m.inputs.items())
            },
            "policies": m.policies,
        }
        return {
            "items": items,
            "review_digest": fingerprint(json.dumps(binding, sort_keys=True).encode()),
        }

    def apply(
        self,
        names: list[str],
        reviewed_digest: str,
        *,
        verifier: Callable[[Path, dict, Path], bool],
    ) -> dict:
        """Verify staged candidates, then install selective edits with backups and rollback.

        A current destination grant is never overwritten. Installed files may be
        updated only by this explicitly reviewed operation. Failure before commit
        changes no live bytes; ordinary commit errors restore backed-up bytes.
        Crash-atomic multi-file replacement is outside this operation's contract.
        """
        m = self.migration
        with CatalogLock(m.target / "data"):
            plan = self.plan(names)
            if reviewed_digest != plan["review_digest"]:
                raise ValueError("Exact package update review is required; plan is stale")
            operation = m.target / "migrations" / ("applications-" + uuid4().hex)
            reject_alias(operation)
            operation.mkdir(parents=True)
            for update in self.prepared:
                started = time.monotonic()
                item = update.item
                package = m.target / "data/applications" / update.record["folder"]
                evidence = operation / update.record["id"]
                evidence.mkdir()
                staged = evidence / "application"
                staged.mkdir()
                try:
                    m._fresh()
                    if app_in_use(m.target / "data", update.record["id"]):
                        raise ValueError("Application is in use; close its own preview first")
                    self._stage(staged, update.updated)
                    review = json.loads(update.new_review)
                    (evidence / "review.json").write_bytes(update.new_review)
                    if verifier(staged, review, evidence) is not True:
                        raise ValueError("Independent native/browser verification failed")
                    if application_digest(staged) != update.record["digest"]:
                        raise ValueError("Staged application changed during verification")
                    m._fresh()
                    if {p.name for p in package.iterdir()} - {"__pycache__"} != set(
                        update.original
                    ):
                        raise ValueError("Installed application members changed during review")
                    backup = evidence / "backup"
                    backup.mkdir()
                    self._stage(backup, update.original)
                    (backup / "review.json").write_bytes(update.old_review)
                    (backup / "source.approval").write_bytes(update.source_record)
                    self._commit(update, package)
                    item.update(
                        status="updated",
                        reason="Fresh native/browser gates passed; original bytes backed up",
                    )
                except Exception as error:
                    item.update(
                        status="blocked",
                        reason=str(error)[:250]
                        if isinstance(error, (OSError, ValueError))
                        else type(error).__name__,
                    )
                finally:
                    item["duration_seconds"] = round(time.monotonic() - started, 3)
                    logger.info(
                        "operation=%s stage=application_update outcome=%s duration_seconds=%.3f",
                        operation.name,
                        item["status"],
                        item["duration_seconds"],
                    )
            plan.update(operation_id=operation.name, evidence=str(operation))
            (operation / "receipt.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
            return plan

    def _commit(self, update: Update, package: Path) -> None:
        """Install changed maintained bytes/review and create the protected grant last."""
        m = self.migration
        changes = {
            package / name: body
            for name, body in update.updated.items()
            if body != update.original[name]
        }
        changes[update.review_path] = update.new_review
        originals = {path: m.inputs[path] for path in changes}
        sealed = m.protector.seal(json.dumps(update.record, sort_keys=True).encode())
        if len(sealed) > 262144:
            raise ValueError("Updated application approval exceeds limit")
        update.approval_path.parent.mkdir(parents=True, exist_ok=True)
        reject_alias(update.approval_path)
        written = []
        try:
            for path, body in changes.items():
                written.append(path)
                path.write_bytes(body)
            with update.approval_path.open("xb") as stream:
                stream.write(sealed)
        except Exception:
            for path in reversed(written):
                path.write_bytes(originals[path])
            raise
        m.inputs.update(changes)
        m.inputs[update.approval_path] = sealed
