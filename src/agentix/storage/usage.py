"""User-local application usage leases, shared by GUI previews and headless calls."""

import json
import os
from pathlib import Path
from uuid import uuid4

from agentix.storage.catalog_lock import reject_alias


def process_alive(pid: int) -> bool:
    """Preserve leases on access denial or uncertain process identity."""
    if pid == os.getpid():
        return True
    if os.name == "nt":
        from agentix.sandbox.windows_process import NativeWindows

        native = NativeWindows()
        try:
            return native._process_alive(pid)
        finally:
            native.close()
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


class AppLease:
    """Own one process receipt; caller acquires the catalog lock before construction."""

    def __init__(self, root: Path, identity: str) -> None:
        """Create only the validated installed application's private usage receipt."""
        self.directory = root / "usage" / identity
        reject_alias(self.directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / (uuid4().hex + ".json")
        with self.path.open("x", encoding="utf-8") as stream:
            json.dump({"id": identity, "pid": os.getpid()}, stream)

    def close(self) -> None:
        """Release only this lease; a remaining concurrent lease stays effective."""
        reject_alias(self.path)
        self.path.unlink(missing_ok=True)
        try:
            self.directory.rmdir()
        except OSError:
            pass

    def __enter__(self):
        """Retain the lease during one bounded native data operation."""
        return self

    def __exit__(self, *error) -> None:
        """Release on native failure as well as successful completion."""
        self.close()


def app_in_use(root: Path, identity: str, *, probe=process_alive) -> bool:
    """Conservatively inspect only the known application's owned usage directory."""
    directory = root / "usage" / identity
    reject_alias(directory)
    if not directory.exists():
        return False
    entries = list(directory.iterdir())
    if len(entries) > 128:
        raise ValueError("Application usage cannot be established")
    for path in entries:
        reject_alias(path)
        if not path.is_file() or path.stat().st_size > 4096:
            raise ValueError("Application usage cannot be established")
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("id") != identity or type(record.get("pid")) is not int or record["pid"] <= 0:
            raise ValueError("Application usage cannot be established")
        if probe(record["pid"]):
            return True
        path.unlink()
    try:
        directory.rmdir()
    except OSError:
        pass
    return False
