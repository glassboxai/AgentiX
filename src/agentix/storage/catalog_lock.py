"""Cross-process catalog mutation lock; never an execution-isolation mechanism."""

import os
import stat
import threading
import time
from pathlib import Path

_THREAD_LOCK = threading.RLock()


def reject_alias(path: Path) -> None:
    """Reject existing reparse ancestors before catalog mutation or traversal."""
    for part in (path, *path.parents):
        if part.is_symlink() or (
            part.exists() and part.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
        ):
            raise ValueError("Catalog path aliases are forbidden")


class CatalogLock:
    """Serialize publication, usage acquisition and removal under one managed root."""

    def __init__(self, root: Path, timeout: float = 3.0) -> None:
        """Remember the bounded acquisition deadline; construction performs no IO."""
        self.root, self.timeout, self.stream = root, timeout, None

    def __enter__(self):
        """Acquire a byte-range lock; report busy rather than waiting indefinitely."""
        if not _THREAD_LOCK.acquire(timeout=self.timeout):
            raise ValueError("Catalog is busy; retry later")
        try:
            reject_alias(self.root)
            self.root.mkdir(parents=True, exist_ok=True)
            path = self.root / "catalog.lock"
            reject_alias(path)
            if path.exists() and path.stat().st_nlink != 1:
                raise ValueError("Catalog lock aliases are forbidden")
            self.stream = path.open("a+b")
            self.stream.seek(0, 2)
            if self.stream.tell() == 0:
                self.stream.write(b"0")
                self.stream.flush()
            deadline = time.monotonic() + self.timeout
            while True:
                self.stream.seek(0)
                try:
                    if os.name == "nt":
                        import msvcrt

                        msvcrt.locking(self.stream.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl

                        fcntl.flock(self.stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    return self
                except OSError:
                    if time.monotonic() >= deadline:
                        raise ValueError("Catalog is busy; retry later") from None
                    time.sleep(0.05)
        except BaseException:
            if self.stream is not None:
                self.stream.close()
            _THREAD_LOCK.release()
            raise

    def __exit__(self, *error) -> None:
        """Close the handle even if the OS reports an unlock error."""
        try:
            if self.stream is not None:
                try:
                    self.stream.seek(0)
                    if os.name == "nt":
                        import msvcrt

                        msvcrt.locking(self.stream.fileno(), msvcrt.LK_UNLCK, 1)
                    else:
                        import fcntl

                        fcntl.flock(self.stream, fcntl.LOCK_UN)
                finally:
                    self.stream.close()
        finally:
            _THREAD_LOCK.release()
