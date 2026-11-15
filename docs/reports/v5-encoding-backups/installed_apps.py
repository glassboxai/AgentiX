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
from dataclasses import dataclass
from pathlib import Path

from agentix.storage.locations import data_directory
from typing import Any

from agentix.security.approval_store import ApprovalStore
from agentix.security.data_protection import WindowsDataProtection
from agentix.lab.application_artifacts import application_digest, approve_application
from agentix.layout_contracts import validate_layout

logger = logging.getLogger(__name__)


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


def app_policy() -> str:
    """Bind the maintained execution boundary and runtime, not presentation coordinates."""
    root = Path(__file__).resolve().parents[1]
    digest = hashlib.sha256(b"AgentiX-v5-installed-app-v1")
    for name in (
        "storage/installed_apps.py",
        "application/app_controls.py",
        "layout_contracts.py",
        "lab/widget_bridge.py",
        "lab/application_panel.py",
        "ui/assets/application_editor.js",
        "lab/application_artifacts.py",
        "lab/application_session.py",
        "lab/widget_worker.py",
        "sandbox/windows_process.py",
    ):
        digest.update(name.encode())
        digest.update((root / name).read_bytes())
    digest.update((root.parents[1] / "infra/runtime.lock.txt").read_bytes())
    return digest.hexdigest()


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
        record_path = self._record(identity)
        with record_path.open("rb") as stream:
            sealed = stream.read(262145)
        if len(sealed) > 262144:
            raise ValueError("Approval exceeds limit")
        raw = self.records.protector.unseal(sealed)
        if len(raw) > 98304:
            raise ValueError("Approval exceeds limit")
        record = json.loads(raw)
        folder = record.get("folder", "")
        if not isinstance(folder, str) or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,99}", folder):
            raise ValueError("Invalid application folder")
        directory = self.root / folder
        if directory.is_symlink() or directory.resolve() != directory:
            raise ValueError("Application directory aliases are forbidden")
        return directory

    def _record(self, identity: str) -> Path:
        """Use the existing bounded protected-record naming/containment primitive."""
        if not isinstance(identity, str) or not re.fullmatch(r"[0-9a-f]{32}", identity):
            raise ValueError("Select an installed application")
        return self.records._path("app_" + identity)

    def publish(self, candidate: Any) -> InstalledApp:
        """Copy exact verified bytes; never publish a draft or a child success claim."""
        if not candidate.approved or not candidate.verified or candidate.snapshot is None:
            raise ValueError("Only independently verified reviewed applications can be installed")
        snapshot = approve_application(candidate.package, candidate.digest)
        if snapshot != candidate.snapshot:
            raise ValueError("Application changed after verification")
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
        for name, data in snapshot.files:
            (package / name).write_bytes(data)
        layout_path = candidate.package / "config.json"
        layout = {"version": 1, "positions": {}}
        if layout_path.exists():
            if layout_path.is_symlink() or layout_path.resolve() != layout_path:
                raise ValueError("Layout aliases are forbidden")
            with layout_path.open("rb") as stream:
                raw_layout = stream.read(65537)
            if len(raw_layout) > 65536:
                raise ValueError("Layout exceeds limit")
            layout = validate_layout(json.loads(raw_layout))
        (package / "config.json").write_text(json.dumps(layout, indent=2), encoding="utf-8")
        review = json.loads(candidate.review_text)
        review_raw = json.dumps(review, ensure_ascii=True).encode()
        if len(review_raw) > 1048576:
            raise ValueError("Application review exceeds limit")
        review_directory = self.root.parent / "reviews" / identity
        review_directory.mkdir(parents=True, exist_ok=False)
        (review_directory / "review.json").write_bytes(review_raw)
        description = str(review.get("original_request", "Text analysis"))[:4000]
        record = {
            "purpose": "AgentiX/v5/installed-app/v1",
            "id": identity,
            "name": "Text analysis Ãƒâ€šÃ‚Â· " + identity[:8],
            "description": description,
            "digest": candidate.digest,
            "review": hashlib.sha256(review_raw).hexdigest(),
            "policy": self.records.policy,
            "dependencies": review.get("approved_catalog_dependencies", {}),
        }
        sealed = self.records.protector.seal(json.dumps(record, sort_keys=True).encode())
        if len(sealed) > 262144:
            raise ValueError("Application approval exceeds limit")
        path = self._record(identity)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(sealed)
        logger.info("event=application_installed app_id=%s", identity)
        return self.get(identity)

    def get(self, identity: str) -> InstalledApp:
        """Recheck protected identity, review and exact source before returning metadata."""
        directory = self._directory(identity)
        try:
            with self._record(identity).open("rb") as stream:
                sealed = stream.read(262145)
            if len(sealed) > 262144:
                raise ValueError("Approval exceeds limit")
            raw = self.records.protector.unseal(sealed)
            if len(raw) > 98304:
                raise ValueError("Approval exceeds limit")
            record = json.loads(raw)
            if (
                record.get("purpose") != "AgentiX/v5/installed-app/v1"
                or record.get("id") != identity
                or record.get("policy") != self.records.policy
            ):
                raise ValueError("Application approval is stale")
            package = directory
            if application_digest(package) != record["digest"]:
                raise ValueError("Installed application source changed")
            review_path = self.root.parent / "reviews" / identity / "review.json"
            if review_path.is_symlink() or review_path.resolve() != review_path:
                raise ValueError("Review aliases are forbidden")
            with review_path.open("rb") as stream:
                review_raw = stream.read(1048577)
            if (
                len(review_raw) > 1048576
                or hashlib.sha256(review_raw).hexdigest() != record["review"]
            ):
                raise ValueError("Application review changed")
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

    def list(self) -> list[InstalledApp]:
        """List only this managed library; never import app modules or scan tool storage."""
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
                record = json.loads(raw)
                result.append(self.get(record["id"]))
            except (OSError, ValueError, KeyError, TypeError):
                logger.warning("event=installed_app_rejected")
        return result

    def read_layout(self, identity: str) -> dict:
        """Read bounded presentation data; invalid geometry never becomes executable CSS."""
        app = self.get(identity)
        try:
            path = app.package / "config.json"
            if path.is_symlink() or path.resolve() != path:
                raise ValueError("Layout aliases are forbidden")
            with path.open("rb") as stream:
                raw = stream.read(65537)
            if len(raw) > 65536:
                raise ValueError("Layout exceeds limit")
            return validate_layout(json.loads(raw))
        except (OSError, ValueError):
            logger.warning("event=invalid_layout_ignored app_id=%s", identity)
            return validate_layout({"version": 1, "positions": {}})

    def save_layout(self, identity: str, value: object) -> None:
        """Persist only safe numeric layout, without changing executable approval."""
        layout = validate_layout(value)
        app = self.get(identity)
        path = app.package / "config.json"
        if path.is_symlink() or path.resolve() != path:
            raise ValueError("Layout aliases are forbidden")
        path.write_text(json.dumps(layout, indent=2), encoding="utf-8")
        logger.info("event=application_layout_saved app_id=%s", identity)
