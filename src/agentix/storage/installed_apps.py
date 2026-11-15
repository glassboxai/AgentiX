"""Protected installed-app catalog, immutable executable snapshots and separate layout.

Construction performs no reads. Only the maintained supervisor may publish a
human-approved independently verified candidate. UI inputs contain opaque IDs,
never filesystem paths. Descriptions are untrusted display/model data.
"""

import hashlib
import json
import logging
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agentix.application.code_package import SHARED as CODE_SHARED
from agentix.lab.application_artifacts import _identity, application_digest, approve_application
from agentix.layout_contracts import (
    application_layout_groups,
    application_layout_ids,
    validate_layout,
)
from agentix.security.approval_store import ApprovalStore
from agentix.security.data_protection import WindowsDataProtection
from agentix.storage.locations import data_directory

logger = logging.getLogger(__name__)

PURPOSE = "AgentiX/v5/installed-app/v1"
"""Sealed-record discriminator, not a product version.

The ``v5`` segment is a frozen storage-domain tag: it is written into every
protected application record and rechecked on each read, so renaming it would
invalidate every installed approval. It is intentionally independent of the
AgentiX release number and of the retired ``agentix/v5`` data namespace that
``storage.locations`` rejects.
"""
STALE_APPROVAL = "Application approval is stale"
CHANGED_SOURCE = "Installed application source changed"
CHANGED_RUNTIME = "Installed application maintained runtime changed"
CHANGED_REVIEW = "Application review changed"
STATUS_BY_REASON = {
    STALE_APPROVAL: "approval_stale",
    CHANGED_SOURCE: "source_changed",
    CHANGED_RUNTIME: "runtime_changed",
    CHANGED_REVIEW: "review_changed",
}


@dataclass(frozen=True)
class InstalledApp:
    """Authenticated catalog metadata; executable bytes are rechecked on every get."""

    id: str
    name: str
    description: str
    package: Path
    digest: str
    dependencies: dict
    review: dict


@dataclass(frozen=True)
class CatalogEntry:
    """One catalog row that keeps a rejected record visible with a bounded reason."""

    id: str
    name: str
    status: str
    reason: str
    app: InstalledApp | None = None


def _safe_name(value: Any) -> str:
    """Bound untrusted display text before it reaches a log line or a dropdown."""
    if not isinstance(value, str):
        return ""
    return re.sub(r"[^A-Za-z0-9 _.-]", "", value)[:80]


def app_policy() -> str:
    """Bind the maintained execution boundary and runtime, not catalog services.

    Removal, usage leases and presentation geometry are catalog services: they
    gate mutation and display but never run inside the child, so their edits must
    not invalidate an installed approval.
    """
    root = Path(__file__).resolve().parents[1]
    digest = hashlib.sha256(b"AgentiX-v5-installed-app-v1")
    for name in (
        "storage/installed_apps.py",
        "widgets/styles.py",
        "storage/locations.py",
        "storage/catalog_lock.py",
        "storage/usage.py",
        "sandbox/profile_cleanup.py",
        "application/app_controls.py",
        "layout_contracts.py",
        "lab/widget_bridge.py",
        "lab/application_panel.py",
        "ui/assets/application_editor.js",
        "lab/application_artifacts.py",
        "application/general_package.py",
        "application/general_pipeline.py",
        "application/general_acceptance.py",
        "application/templates/code/app.py",
        "application/templates/code/operation.py",
        "application/templates/code/application_context.py",
        "domain/application_code.py",
        "domain/tool_schema.py",
        "lab/application_session.py",
        "lab/widget_worker.py",
        "sandbox/windows_process.py",
    ):
        digest.update(name.encode())
        digest.update((root / name).read_bytes())
    digest.update((root.parents[1] / "infra/runtime.lock.txt").read_bytes())
    return digest.hexdigest()


def _legacy_digest(package: Path) -> str:
    """Reproduce the pre-V7-076 identity that also hashed scoped stylesheets.

    Records sealed before scoped styles left the application identity still carry
    that value. Comparing against it proves the installed bytes are unchanged, so a
    formula change never reports an untouched application as tampered.
    """
    from agentix.application.general_package import capture

    files = capture(package)
    return hashlib.sha256(
        json.dumps(
            {name: hashlib.sha256(body).hexdigest() for name, body in files}, sort_keys=True
        ).encode()
    ).hexdigest()


def _source_digest(package: Path, *, allow_runtime_drift: bool = False) -> str:
    """Recompute installed bytes, naming maintained-runtime drift apart from tampering.

    ``application_digest`` rejects both a modified application member and a
    maintained runtime member that no longer matches the installed copy. Only the
    first is a changed application source; the second is host drift that a
    re-approval can resolve, so the bounded reason stays distinguishable. With
    ``allow_runtime_drift`` the digest is computed over the installed package with
    the current runtime members, which never equals the sealed digest.
    """
    from agentix.application.general_package import RuntimeSourceChanged

    try:
        return application_digest(package)
    except RuntimeSourceChanged as error:
        if not allow_runtime_drift:
            raise ValueError(CHANGED_RUNTIME) from error
        from agentix.application.general_package import capture_with_current_runtime

        return _identity(capture_with_current_runtime(package))
    except ValueError as error:
        raise ValueError(CHANGED_SOURCE) from error


class InstalledApps:
    """User-local durable library with authenticated source/dependency bindings."""

    def __init__(self, root: Path, records: Path, *, protector: Any = None) -> None:
        """Inject protected storage; do not adopt or inspect old session drafts."""
        self.root = root.resolve()
        self.records = ApprovalStore(
            records,
            self.root,
            protector=protector if protector is not None else WindowsDataProtection(),
            policy=app_policy(),
        )

    @classmethod
    def for_user(cls) -> "InstalledApps":
        """Compose v4 user storage, independent of v2/v3 and existing tool artifacts."""
        data = data_directory()
        return cls(data / "applications", data / "approvals" / "applications")

    def _directory(self, identity: str) -> Path:
        """Resolve a safe named folder only through its protected opaque-ID record."""
        record = self._record_data(identity)
        if record.get("root") != self.records.root:
            raise ValueError("Application approval belongs to another library")
        folder = record.get("folder", "")
        if not isinstance(folder, str) or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,99}", folder):
            raise ValueError("Invalid application folder")
        directory = self.root / folder
        if directory.is_symlink() or directory.resolve() != directory:
            raise ValueError("Application directory aliases are forbidden")
        return directory

    def _record_data(self, identity: str) -> dict:
        """Read one bounded authenticated record; unsealed metadata is never trusted."""
        with self._record(identity).open("rb") as stream:
            sealed = stream.read(262145)
        if len(sealed) > 262144:
            raise ValueError("Approval exceeds limit")
        raw = self.records.protector.unseal(sealed)
        if len(raw) > 98304:
            raise ValueError("Approval exceeds limit")
        return json.loads(raw)

    def _write_bytes(self, path: Path, data: bytes) -> None:
        """Replace one owned file atomically so a crash never leaves a partial grant."""
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix=".agentix-", dir=path.parent)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)

    def _write_record(self, identity: str, record: dict) -> None:
        """Seal and atomically replace one protected record; no partial approval survives."""
        sealed = self.records.protector.seal(json.dumps(record, sort_keys=True).encode())
        if len(sealed) > 262144:
            raise ValueError("Application approval exceeds limit")
        self._write_bytes(self._record(identity), sealed)

    def _record(self, identity: str) -> Path:
        """Use the existing bounded protected-record naming/containment primitive."""
        if not isinstance(identity, str) or not re.fullmatch(r"[0-9a-f]{32}", identity):
            raise ValueError("Select an installed application")
        return self.records._path("app_" + identity)

    def dependency_references(self, identity: str, *, kind: str = "tool") -> list[str]:
        """Check protected references even when a dependent source is currently invalid."""
        namespace = self.records.directory / self.records.namespace
        from agentix.storage.catalog_lock import reject_alias

        reject_alias(namespace)
        if not namespace.exists():
            return []
        paths = list(namespace.glob("*.approval"))
        if len(paths) > 512:
            raise ValueError("Dependency catalog exceeds its limit")
        result = []
        for path in paths:
            reject_alias(path)
            if path.stat().st_size > 262144:
                raise ValueError("Dependency metadata is invalid")
            raw = self.records.protector.unseal(path.read_bytes())
            if len(raw) > 98304:
                raise ValueError("Dependency metadata is invalid")
            record = json.loads(raw)
            if (
                record.get("purpose") != PURPOSE
                or record.get("root") != self.records.root
                or self._record(record.get("id")) != path
                or not isinstance(record.get("dependencies"), dict)
            ):
                raise ValueError("Dependency metadata is invalid")
            for dependency in record["dependencies"].values():
                if not isinstance(dependency, dict):
                    raise ValueError("Dependency metadata is invalid")
                key = "tool_name" if kind == "tool" else "app_id"
                if dependency.get(key) == identity:
                    result.append(record["name"])
        return result

    def open_lease(self, identity: str):
        """Validate and reserve an installed package before starting any native work."""
        from agentix.storage.catalog_lock import CatalogLock
        from agentix.storage.usage import AppLease

        with CatalogLock(self.root.parent):
            self.get(identity)
            return AppLease(self.root.parent, identity)

    def in_use(self, identity: str) -> bool:
        """Check shared process receipts; callers hold the catalog mutation lock."""
        from agentix.storage.usage import app_in_use

        self._record(identity)
        return app_in_use(self.root.parent, identity)

    def write_style_member(self, identity: str, name: str, css: str) -> str:
        """Rewrite one scoped stylesheet inside an installed package.

        Style members are excluded from the application identity, so this keeps the
        sealed record and its approval valid while the installed bytes change. The
        package is re-verified first, and the member hash in ``application.json`` is
        rebound by the maintained writer. Raises ``ValueError`` for an unknown
        identity, a changed source, an unsafe declaration or an aliased member.
        """
        from agentix.application.style_member import write_style_member

        try:
            app = self._validated(identity, require_policy=False)
        except ValueError as error:
            if str(error) != CHANGED_RUNTIME:
                raise
            app = self._validated(identity, require_policy=False, allow_runtime_drift=True)
        digest = write_style_member(app.package, name, css)
        record = self._record_data(identity)
        if _source_digest(app.package) != record["digest"] and (
            _legacy_digest(app.package) != record["digest"]
        ):
            raise ValueError(CHANGED_SOURCE)
        logger.info(
            "event=installed_app_style_saved app_id=%s member=%s digest=%s",
            identity,
            name,
            digest[:12],
        )
        return digest

    def publish(self, candidate: Any) -> InstalledApp:
        """Serialize publication with removal and bind any already-open preview lease."""
        from agentix.storage.catalog_lock import CatalogLock
        from agentix.storage.usage import AppLease

        with CatalogLock(self.root.parent):
            if candidate.dependency_check is not None:
                candidate.dependency_check()
            app = self._publish(candidate)
            if candidate.preview is not None:
                candidate.library_lease = AppLease(self.root.parent, app.id)
            return app

    def _publish(self, candidate: Any) -> InstalledApp:
        """Copy exact verified bytes; never publish a draft or a child success claim."""
        if not candidate.approved or not candidate.verified or candidate.snapshot is None:
            raise ValueError("Only independently verified reviewed applications can be installed")
        snapshot = approve_application(
            candidate.package,
            candidate.digest,
            allow_runtime_drift=getattr(candidate, "runtime_refresh", False),
        )
        if snapshot != candidate.snapshot:
            raise ValueError("Application changed after verification")
        existing = getattr(candidate, "catalog_id", "") or ""
        if existing:
            return self._reseal_candidate(candidate, snapshot, existing)
        identity = candidate.identity
        from agentix.domain.application_names import application_folder

        name = getattr(candidate, "display_name", "Text analysis")
        folder = application_folder(name)
        directory = self.root / folder
        package = directory
        try:
            package.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            raise ValueError("An application with this name already exists") from None
        for filename, data in snapshot.files:
            (package / filename).write_bytes(data)
        layout_path = candidate.package / "config.json"
        layout = {"version": 1, "positions": {}}
        if layout_path.exists():
            if layout_path.is_symlink() or layout_path.resolve() != layout_path:
                raise ValueError("Layout aliases are forbidden")
            with layout_path.open("rb") as stream:
                raw_layout = stream.read(65537)
            if len(raw_layout) > 65536:
                raise ValueError("Layout exceeds limit")
            layout = validate_layout(
                json.loads(raw_layout),
                allowed=application_layout_ids(
                    json.loads(dict(snapshot.files)["application.json"])
                ),
            )
        (package / "config.json").write_text(json.dumps(layout, indent=2), encoding="utf-8")
        review = json.loads(candidate.review_text)
        review_raw = json.dumps(review, ensure_ascii=True).encode()
        if len(review_raw) > 1048576:
            raise ValueError("Application review exceeds limit")
        review_directory = self.root.parent / "reviews" / identity
        review_directory.mkdir(parents=True, exist_ok=False)
        self._write_bytes(review_directory / "review.json", review_raw)
        description = str(review.get("original_request", "Text analysis"))[:4000]
        record = {
            "purpose": PURPOSE,
            "root": self.records.root,
            "id": identity,
            "name": name,
            "folder": folder,
            "description": description,
            "digest": candidate.digest,
            "review": hashlib.sha256(review_raw).hexdigest(),
            "policy": self.records.policy,
            "dependencies": review.get("approved_catalog_dependencies", {}),
        }
        self._write_record(identity, record)
        logger.info("event=application_installed app_id=%s", identity)
        return self.get(identity)

    def get(self, identity: str) -> InstalledApp:
        """Recheck protected identity, review and exact source before returning metadata."""
        return self._validated(identity, require_policy=True)

    def load_stale(self, identity: str) -> InstalledApp:
        """Return exact installed bytes for re-approval without granting current policy."""
        return self._validated(identity, require_policy=False)

    def load_for_runtime_refresh(self, identity: str) -> InstalledApp:
        """Return an installed record whose only drift is the maintained runtime.

        The returned package still holds the installed bytes; callers must capture
        them with ``capture_with_current_runtime`` and re-run the independent gates.
        Changed application source, a changed review or an invalid identity is
        refused exactly as ``load_stale`` does.
        """
        try:
            return self.load_stale(identity)
        except ValueError as error:
            if str(error) != CHANGED_RUNTIME:
                raise
        app = self._validated(identity, require_policy=False, allow_runtime_drift=True)
        logger.info("event=application_runtime_refresh_loaded app_id=%s", identity)
        return app

    def _validated(
        self, identity: str, *, require_policy: bool, allow_runtime_drift: bool = False
    ) -> InstalledApp:
        """Bind identity, review and source bytes; policy is optional for re-approval."""
        try:
            directory = self._directory(identity)
            record = self._record_data(identity)
            if (
                record.get("purpose") != PURPOSE
                or record.get("root") != self.records.root
                or record.get("id") != identity
            ):
                raise ValueError(STALE_APPROVAL)
            package = directory
            actual = _source_digest(package, allow_runtime_drift=allow_runtime_drift)
            if actual != record["digest"] and not allow_runtime_drift:
                if _legacy_digest(package) != record["digest"]:
                    raise ValueError(CHANGED_SOURCE)
            if require_policy and record.get("policy") != self.records.policy:
                raise ValueError(STALE_APPROVAL)
            review_path = self.root.parent / "reviews" / identity / "review.json"
            if review_path.is_symlink() or review_path.resolve() != review_path:
                raise ValueError("Review aliases are forbidden")
            with review_path.open("rb") as stream:
                review_raw = stream.read(1048577)
            if (
                len(review_raw) > 1048576
                or hashlib.sha256(review_raw).hexdigest() != record["review"]
            ):
                raise ValueError(CHANGED_REVIEW)
            return InstalledApp(
                identity,
                record["name"],
                record["description"],
                package,
                record["digest"],
                record["dependencies"],
                json.loads(review_raw),
            )
        except (OSError, KeyError, TypeError, json.JSONDecodeError) as error:
            raise ValueError("Installed application is unavailable or unapproved") from error

    def reseal(self, identity: str) -> InstalledApp:
        """Rebind one unchanged installed package to the current host policy atomically.

        The caller must already have re-run the independent gates on these exact
        bytes; this method never re-approves changed source or a changed review.
        """
        from agentix.storage.catalog_lock import CatalogLock

        with CatalogLock(self.root.parent):
            return self._reseal(identity)

    def _reseal(self, identity: str) -> InstalledApp:
        """Replace only the policy binding after exact bytes and review were rechecked."""
        record = self._record_data(identity)
        if (
            record.get("purpose") != PURPOSE
            or record.get("root") != self.records.root
            or record.get("id") != identity
        ):
            raise ValueError(STALE_APPROVAL)
        directory = self._directory(identity)
        if _source_digest(directory) != record["digest"]:
            raise ValueError(CHANGED_SOURCE)
        review_path = self.root.parent / "reviews" / identity / "review.json"
        if review_path.is_symlink() or review_path.resolve() != review_path:
            raise ValueError("Review aliases are forbidden")
        with review_path.open("rb") as stream:
            review_raw = stream.read(1048577)
        if len(review_raw) > 1048576 or hashlib.sha256(review_raw).hexdigest() != record["review"]:
            raise ValueError(CHANGED_REVIEW)
        record["policy"] = app_policy()
        self._write_record(identity, record)
        logger.info("event=application_resealed app_id=%s", identity)
        return self.get(identity)

    def _reseal_candidate(self, candidate: Any, snapshot: Any, identity: str) -> InstalledApp:
        """Replace one installed record after the reviewed candidate passed current gates."""
        record = self._record_data(identity)
        if (
            record.get("purpose") != PURPOSE
            or record.get("root") != self.records.root
            or record.get("id") != identity
        ):
            raise ValueError(STALE_APPROVAL)
        directory = self._directory(identity)
        if getattr(candidate, "runtime_refresh", False):
            if _source_digest(directory, allow_runtime_drift=True) != candidate.digest:
                raise ValueError("Installed application changed after review")
            for name, body in snapshot.files:
                if (
                    name in CODE_SHARED | {"application.json"}
                    and (directory / name).read_bytes() != body
                ):
                    self._write_bytes(directory / name, body)
        else:
            if _source_digest(directory) != record["digest"]:
                raise ValueError(CHANGED_SOURCE)
            if record["digest"] != candidate.digest or snapshot.digest != record["digest"]:
                raise ValueError("Installed application changed after review")
        review = json.loads(candidate.review_text)
        review_raw = json.dumps(review, ensure_ascii=True).encode()
        if len(review_raw) > 1048576:
            raise ValueError("Application review exceeds limit")
        self._write_bytes(self.root.parent / "reviews" / identity / "review.json", review_raw)
        record.update(
            description=str(review.get("original_request", record["description"]))[:4000],
            digest=snapshot.digest,
            review=hashlib.sha256(review_raw).hexdigest(),
            policy=app_policy(),
            dependencies=review.get("approved_catalog_dependencies", {}),
        )
        self._write_record(identity, record)
        logger.info("event=application_resealed app_id=%s", identity)
        return self.get(identity)

    def name_available(self, name: str) -> bool:
        """Report whether the display-name install folder is free for publication."""
        from agentix.domain.application_names import application_folder

        return not (self.root / application_folder(name)).exists()

    def entry(self, identity: str) -> CatalogEntry:
        """Return one catalog row, keeping a rejected record visible with its reason."""
        try:
            app = self.get(identity)
        except (OSError, ValueError, KeyError, TypeError) as error:
            status = STATUS_BY_REASON.get(str(error), "unavailable")
            name = ""
            try:
                name = _safe_name(self._record_data(identity).get("name"))
            except (OSError, ValueError, KeyError, TypeError):
                name = ""
            logger.warning(
                "event=installed_app_rejected app_id=%s name=%s status=%s detail=%.160s",
                identity,
                name or "-",
                status,
                error,
            )
            return CatalogEntry(identity, name or identity, status, str(error)[:160])
        return CatalogEntry(app.id, app.name, "valid", "", app)

    def entries(self) -> list[CatalogEntry]:
        """List every managed record with its current status; never import app modules."""
        namespace = self.records.directory / self.records.namespace
        if not namespace.exists():
            return []
        result = []
        for path in sorted(namespace.glob("*.approval")):
            try:
                if path.is_symlink() or path.stat().st_size > 262144:
                    raise ValueError("Invalid application record")
                raw = self.records.protector.unseal(path.read_bytes())
                if len(raw) > 98304:
                    raise ValueError("Invalid application record")
                identity = json.loads(raw).get("id")
                if not isinstance(identity, str):
                    raise ValueError("Invalid application record")
            except (OSError, ValueError, KeyError, TypeError) as error:
                logger.warning(
                    "event=installed_app_rejected app_id=- name=- status=unavailable detail=%.160s",
                    error,
                )
                result.append(CatalogEntry("", "", "unavailable", str(error)[:160]))
                continue
            result.append(self.entry(identity))
        valid = sum(1 for entry in result if entry.status == "valid")
        logger.info(
            "event=installed_apps_listed total=%d valid=%d rejected=%d",
            len(result),
            valid,
            len(result) - valid,
        )
        return result

    def list(self) -> list[InstalledApp]:
        """List only currently authorized apps; rejected records stay visible via entries()."""
        return [entry.app for entry in self.entries() if entry.app is not None]

    def layout_controls(
        self, identity: str, *, allow_runtime_drift: bool = False
    ) -> set[str] | None:
        """Return only the reviewed manifest's movable controls, never browser selectors."""
        app = self._validated(
            identity, require_policy=False, allow_runtime_drift=allow_runtime_drift
        )
        manifest = json.loads((app.package / "application.json").read_bytes())
        return application_layout_ids(manifest)

    def layout_groups(self, identity: str, *, allow_runtime_drift: bool = False) -> dict[str, str]:
        """Return the reviewed tool grouping of movable controls, never browser data."""
        app = self._validated(
            identity, require_policy=False, allow_runtime_drift=allow_runtime_drift
        )
        manifest = json.loads((app.package / "application.json").read_bytes())
        return application_layout_groups(manifest)

    def read_layout(self, identity: str, *, allow_runtime_drift: bool = False) -> dict:
        """Read bounded presentation data; invalid geometry never becomes executable CSS."""
        app = self._validated(
            identity, require_policy=False, allow_runtime_drift=allow_runtime_drift
        )
        try:
            path = app.package / "config.json"
            if path.is_symlink() or path.resolve() != path:
                raise ValueError("Layout aliases are forbidden")
            with path.open("rb") as stream:
                raw = stream.read(65537)
            if len(raw) > 65536:
                raise ValueError("Layout exceeds limit")
            return validate_layout(
                json.loads(raw),
                allowed=self.layout_controls(identity, allow_runtime_drift=allow_runtime_drift),
            )
        except (OSError, ValueError):
            logger.warning("event=invalid_layout_ignored app_id=%s", identity)
            return validate_layout({"version": 1, "positions": {}})

    def save_layout(self, identity: str, value: object) -> None:
        """Persist only safe numeric layout, without changing executable approval."""
        app = self.get(identity)
        layout = validate_layout(value, allowed=self.layout_controls(identity))
        path = app.package / "config.json"
        if path.is_symlink() or path.resolve() != path:
            raise ValueError("Layout aliases are forbidden")
        path.write_text(json.dumps(layout, indent=2), encoding="utf-8")
        logger.info("event=application_layout_saved app_id=%s", identity)
