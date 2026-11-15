"""Native catalog lock handles must close even when unlock reports an OS error."""

import msvcrt

import pytest

from agentix.storage.catalog_lock import CatalogLock


def test_unlock_failure_closes_handle(tmp_path, monkeypatch):
    """Catch file handles surviving failed catalog cleanup and blocking later actions."""
    guard = CatalogLock(tmp_path / "data")
    guard.__enter__()
    original = msvcrt.locking

    def fail_unlock(handle, mode, count):
        """Inject only the release failure; acquisition used the real Windows lock."""
        if mode == msvcrt.LK_UNLCK:
            raise OSError("fixture unlock failure")
        return original(handle, mode, count)

    monkeypatch.setattr(msvcrt, "locking", fail_unlock)
    with pytest.raises(OSError):
        guard.__exit__()
    try:
        assert guard.stream.closed
    finally:
        guard.stream.close()
