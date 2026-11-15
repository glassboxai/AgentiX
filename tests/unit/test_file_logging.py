"""Process logging must also persist to a bounded file under the data directory.

Every handler these tests install is flushed, closed and detached again, and no
handler may outlive the test that created it. Handlers owned by pytest or other
libraries are preserved. All destinations are pytest temporary directories.
"""

import logging
from pathlib import Path

from conftest import agentix_file_handlers, release_agentix_file_handlers

from agentix.bootstrap import configure_process
from agentix.storage.locations import data_directory


def test_configure_process_installs_single_rotating_file_handler(tmp_path, monkeypatch):
    """A bounded agentix.log appears once under data/logs and receives events."""
    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path))
    root = logging.getLogger()
    baseline = agentix_file_handlers()
    for handler in baseline:
        root.removeHandler(handler)
    try:
        configure_process()
        configure_process()
        handlers = agentix_file_handlers()
        assert len(handlers) == 1
        handler = handlers[0]
        assert Path(handler.baseFilename).resolve().is_relative_to(tmp_path.resolve())
        assert getattr(handler, "maxBytes", 0) > 0
        assert getattr(handler, "backupCount", 0) >= 1
        logging.getLogger("agentix.test_file_logging").info("event=file_logging_probe")
        for item in root.handlers:
            item.flush()
        log_path = data_directory() / "logs" / "agentix.log"
        assert log_path.is_file()
        assert "file_logging_probe" in log_path.read_text(encoding="utf-8")
    finally:
        release_agentix_file_handlers(
            [item for item in agentix_file_handlers() if item not in baseline]
        )
        for handler in baseline:
            if handler not in root.handlers:
                root.addHandler(handler)


def test_release_closes_only_the_handlers_it_owns(tmp_path, monkeypatch):
    """Cleanup detaches and closes owned handlers without touching foreign ones."""
    monkeypatch.setenv("AGENTIX_HOME", str(tmp_path))
    root = logging.getLogger()
    detached = agentix_file_handlers()
    for handler in detached:
        root.removeHandler(handler)
    foreign = logging.StreamHandler()
    root.addHandler(foreign)
    try:
        configure_process()
        owned = agentix_file_handlers()
        assert len(owned) == 1
        released = release_agentix_file_handlers(owned)
        assert released == owned
        assert owned[0] not in root.handlers
        assert owned[0]._closed is True
        assert owned[0].stream is None
        assert foreign in root.handlers
        assert foreign._closed is False
        assert release_agentix_file_handlers(owned) == []
    finally:
        root.removeHandler(foreign)
        release_agentix_file_handlers(agentix_file_handlers())
        for handler in detached:
            if handler not in root.handlers and not handler._closed:
                root.addHandler(handler)


def test_installed_handler_keeps_its_first_destination_when_home_changes(tmp_path, monkeypatch):
    """A later AGENTIX_HOME never re-points an already installed handler."""
    first = tmp_path / "first"
    second = tmp_path / "second"
    monkeypatch.setenv("AGENTIX_HOME", str(first))
    detached = agentix_file_handlers()
    for handler in detached:
        logging.getLogger().removeHandler(handler)
    installed: list[logging.Handler] = []
    try:
        configure_process()
        installed = agentix_file_handlers()
        assert len(installed) == 1
        original = Path(installed[0].baseFilename).resolve()
        monkeypatch.setenv("AGENTIX_HOME", str(second))
        configure_process()
        assert agentix_file_handlers() == installed
        assert Path(installed[0].baseFilename).resolve() == original
        assert original.is_relative_to(first.resolve())
        assert not (second / "data" / "logs" / "agentix.log").exists()
    finally:
        release_agentix_file_handlers(installed)
        for handler in detached:
            if handler not in logging.getLogger().handlers and not handler._closed:
                logging.getLogger().addHandler(handler)


def test_session_storage_stays_inside_the_pytest_temporary_root(tmp_path_factory):
    """The session fixture resolves storage under the pytest temporary root."""
    authorized = Path(tmp_path_factory.getbasetemp()).resolve()
    resolved = data_directory().resolve()
    assert resolved.is_relative_to(authorized)
    assert ("agentix", "v5") not in [
        (left.casefold(), right.casefold())
        for left, right in zip(resolved.parts, resolved.parts[1:])
    ]
