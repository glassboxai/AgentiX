"""Confirmed permanent package removal; no generated source is imported or executed."""

import hashlib
import logging
import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from agentix.storage.catalog_lock import CatalogLock, reject_alias

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Removal:
    """Server-only exact target/content binding; never serialized as a browser path."""

    kind: str
    identity: str
    package: Path
    digest: str
    metadata: str


def package_digest(root: Path) -> str:
    """Bound and hash one explicit owned tree; reject aliases before reading members."""
    reject_alias(root)
    if not root.is_dir():
        raise ValueError("Package is unavailable")
    digest = hashlib.sha256(b"AgentiX-removal-snapshot-v1")
    pending, total, count = [root], 0, 0
    for directory in pending:
        for member in sorted(directory.iterdir()):
            reject_alias(member)
            count += 1
            if count > 512:
                raise ValueError("Package member limit exceeded")
            name = member.relative_to(root).as_posix()
            encoded_name = name.encode()
            digest.update(len(encoded_name).to_bytes(4, "big"))
            digest.update(encoded_name)
            if member.is_dir():
                pending.append(member)
                digest.update(b"D")
            elif member.is_file() and member.stat().st_nlink == 1:
                before = member.stat()
                size = before.st_size
                digest.update(b"F" + size.to_bytes(8, "big"))
                total += size
                if size > 32 * 1024 * 1024 or total > 64 * 1024 * 1024:
                    raise ValueError("Package size exceeds safe removal limit")
                observed = 0
                with member.open("rb") as stream:
                    for block in iter(lambda: stream.read(131072), b""):
                        observed += len(block)
                        if observed > size:
                            raise ValueError("Package changed during inspection")
                        digest.update(block)
                after = member.stat()
                if observed != size or (before.st_mtime_ns, size) != (
                    after.st_mtime_ns,
                    after.st_size,
                ):
                    raise ValueError("Package changed during inspection")
            else:
                raise ValueError("Package member aliases are forbidden")
    return digest.hexdigest()


def remove_tree(root: Path, *, code_last: str = "") -> None:
    """Remove an already checked exact tree, keeping the catalog entry until last.

    Repeat alias checks before each unlink. Never follow links or widen to parent
    directories. OS errors propagate; authorization is already revoked on failure.
    """
    reject_alias(root)
    for member in sorted(root.iterdir(), key=lambda path: path.name == code_last):
        reject_alias(member)
        if member.is_dir():
            remove_tree(member)
        else:
            member.unlink()
    root.rmdir()


class CatalogMaintenance:
    """Inject catalogs and strict revocation services; no mutation during construction."""

    def __init__(self, tools: Path, apps, *, revoke_tool: Callable, revoke_widget: Callable):
        """Bind trusted roots, never browser-selected directories or executable callbacks."""
        self.tools, self.apps = tools.resolve(), apps
        self.revoke_tool, self.revoke_widget = revoke_tool, revoke_widget

    def _prepare(self, kind: str, identity: str) -> Removal:
        """Check current dependencies/usage and capture the exact package state.

        Application removal binds identity, exact installed bytes and the review
        digest through ``load_stale`` instead of ``get``: a policy binding that no
        longer matches the current host policy blocks execution, not deletion, and
        the usage/dependency checks below remain the safety conditions for removal.
        """
        if kind == "tool":
            if not isinstance(identity, str) or not re.fullmatch(
                r"[A-Za-z][A-Za-z0-9_]{0,127}", identity
            ):
                raise ValueError("Select an installed tool")
            dependents = self.apps.dependency_references(identity)
            if dependents:
                raise ValueError(
                    "Tool has installed application/composite dependencies: "
                    + ", ".join(dependents)[:1000]
                )
            package = self.tools / identity
            if not (package / (identity + "_code.py")).is_file():
                raise ValueError("Select an installed tool")
            metadata = "tool"
        elif kind == "application":
            app = self.apps.load_stale(identity)
            if self.apps.in_use(identity):
                raise ValueError("Close the open application or wait for its data operation")
            if self.apps.dependency_references(identity, kind="application"):
                raise ValueError("Application has installed composite dependencies")
            package = app.package
            metadata = hashlib.sha256(self.apps._record(identity).read_bytes()).hexdigest()
        else:
            raise ValueError("Unknown catalog action")
        return Removal(kind, identity, package, package_digest(package), metadata)

    def prepare_tool(self, identity: str) -> Removal:
        """Prepare a read-only, exact-content tool deletion confirmation."""
        with CatalogLock(self.apps.root.parent):
            return self._prepare("tool", identity)

    def prepare_app(self, identity: str) -> Removal:
        """Prepare only after application usage and dependency checks succeed."""
        with CatalogLock(self.apps.root.parent):
            return self._prepare("application", identity)

    def confirm(self, removal: Removal) -> None:
        """Recheck under the cross-process lock, revoke, then permanently remove."""
        with CatalogLock(self.apps.root.parent):
            current = self._prepare(removal.kind, removal.identity)
            if current != removal:
                raise ValueError("Package changed; request a new confirmation")
            if removal.kind == "tool":
                self.revoke_tool(removal.identity)
                self.revoke_widget(removal.identity)
            else:
                self.apps._record(removal.identity).unlink()
            try:
                remove_tree(
                    removal.package,
                    code_last=removal.identity + "_code.py" if removal.kind == "tool" else "",
                )
                if removal.kind == "application":
                    review = self.apps.root.parent / "reviews" / removal.identity
                    if review.exists():
                        package_digest(review)
                        remove_tree(review)
            except OSError:
                logger.error("event=catalog_removal_failed kind=%s", removal.kind)
                raise ValueError(
                    "Removal failed after authorization was revoked; diagnostics retained"
                ) from None
            logger.info("event=catalog_removed kind=%s", removal.kind)
