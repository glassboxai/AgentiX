"""Ownership-tracked empty AppContainer residue cleanup; never delete file contents."""

import json
import logging
import os
import re
import stat
from collections.abc import Callable
from pathlib import Path

logger = logging.getLogger(__name__)


class ProfileCleanup:
    """Track v5 profiles before use and retain failed cleanup for later recovery."""

    def __init__(self, packages: Path, pending: Path) -> None:
        """Inject exact Windows Packages and owned pending-record roots; do no IO."""
        self.packages, self.pending = packages, pending

    @classmethod
    def for_user(cls) -> "ProfileCleanup":
        """Use the Windows profile location and separate v5 cleanup metadata."""
        from agentix.storage.locations import user_home

        return cls(
            Path(os.environ["USERPROFILE"]) / "AppData/Local/Packages", user_home() / "cleanup"
        )

    @staticmethod
    def _safe(path: Path) -> None:
        """Reject reparse points in any existing ancestor before traversal or deletion."""
        for part in (path, *path.parents):
            if (
                part.exists()
                and part.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
            ):
                raise ValueError("Cleanup aliases are forbidden")

    def _record(self, name: str) -> Path:
        """Accept only this release's UUID profile names, never browser paths."""
        if not isinstance(name, str) or not re.fullmatch(r"Agentix\.v5\.[0-9a-f]{32}", name):
            raise ValueError("Unknown cleanup profile owner")
        path = self.pending / (name + ".json")
        self._safe(path)
        return path

    def track(self, name: str) -> None:
        """Record process ownership before executing any child; fail closed on IO errors."""
        record = self._record(name)
        self.pending.mkdir(parents=True, exist_ok=True)
        with record.open("x", encoding="utf-8") as stream:
            json.dump({"name": name, "pid": os.getpid()}, stream)

    def release(self, name: str) -> bool:
        """After native deletion, remove only empty owned directories, then the receipt.

        Nonempty files, linked directories and inaccessible resources are retained.
        The caller must already have closed the job and deleted the native profile.
        """
        record = self._record(name)
        if not record.exists():
            raise ValueError("Profile has no ownership record")
        root = self.packages / name
        try:
            self._safe(root)
            if root.exists():
                directories = [root]
                for current in directories:
                    for child in current.iterdir():
                        self._safe(child)
                        if child.is_dir():
                            directories.append(child)
                        else:
                            logger.warning("event=sandbox_cleanup_pending reason=nonempty")
                            return False
                        if len(directories) > 256:
                            raise ValueError("Cleanup directory limit exceeded")
                for directory in reversed(directories):
                    directory.rmdir()
            record.unlink()
            logger.info("event=sandbox_cleanup_complete profile=%s", name)
            return True
        except (OSError, ValueError):
            logger.warning("event=sandbox_cleanup_pending profile=%s", name)
            return False

    def recover(
        self, is_alive: Callable[[int], bool], delete_profile: Callable[[str], bool]
    ) -> None:
        """Retry recorded dead-owner profiles only; unknown/live owners are preserved."""
        self._safe(self.pending)
        if not self.pending.exists():
            return
        for path in list(self.pending.glob("*.json"))[:256]:
            try:
                self._safe(path)
                if path.stat().st_size > 4096:
                    continue
                record = json.loads(path.read_text(encoding="utf-8"))
                name, pid = record["name"], record["pid"]
                if self._record(name) != path or type(pid) is not int or pid <= 0:
                    continue
                if not is_alive(pid) and delete_profile(name):
                    self.release(name)
            except (OSError, ValueError, KeyError, TypeError):
                logger.warning("event=sandbox_cleanup_recovery_rejected")
