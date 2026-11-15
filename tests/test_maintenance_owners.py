"""Deletion confirmations are bound to one session, target and current contents."""

from types import SimpleNamespace

import pytest
from test_application_catalog import installed
from test_applications_backend import registry
from test_installed_apps import library


def setup(tmp_path):
    """Compose real temporary storage with fake authorization protection only."""
    try:
        from agentix.controllers.catalog import CatalogMaintenanceBackend
    except ImportError:
        pytest.fail("Owner-bound catalog controls are not implemented")
    from agentix.controllers.applications import ApplicationsBackend
    from agentix.storage.maintenance import CatalogMaintenance

    tools = tmp_path / "tools"
    tools.mkdir()
    fixture = installed(tools)
    apps = library(tmp_path)
    apps.root.mkdir(parents=True, exist_ok=True)
    sessions = registry()
    actions = CatalogMaintenanceBackend(
        sessions,
        ApplicationsBackend(sessions, library_factory=lambda: apps),
        service_factory=lambda controller: CatalogMaintenance(
            tools, apps, revoke_tool=fixture.ledger.invalidate, revoke_widget=lambda name: None
        ),
        window_snapshot=lambda: frozenset(),
        focus_window=lambda name, before: None,
    )
    owner = sessions.resolve(None, "alice")

    class Security:
        """Minimal tool-root holder mirroring the maintained security contract."""

        TOOLS_ROOT_DIR = str(tools)

        @classmethod
        def published_tools_root(cls):
            """Return the configured root so a test can point it at a missing folder."""
            return cls.TOOLS_ROOT_DIR

    owner.controller.security = Security
    return actions, owner, tools, apps


def test_reseal_batch_stops_when_changed_tool_tests_fail(tmp_path):
    """A changed tool is re-run, and a failing suite stops the batch."""
    actions, owner, tools, _apps = setup(tmp_path)
    calls = []

    class Store:
        """Accept every intact tool and report the changed one."""

        def reseal(self, name, code, tests):
            """Return the changed reason for the designated tool."""
            calls.append(name)
            return None if name != "count_words_in_text" else "changed"

    class Operations:
        """Report a failing isolated suite without executing generated code."""

        verification = SimpleNamespace(store=Store())

        def verify_existing_tool_tool(self, name):
            """Fail the isolated suite for the changed tool."""
            return "TESTS_FAILED: Isolated tests not verified (nonzero_exit)."

    owner.controller.tool_operations = Operations()
    for name in ("alpha", "beta"):
        folder = tools / name
        folder.mkdir()
        (folder / f"{name}_code.py").write_text(f"def {name}():\n    return 1\n", encoding="utf-8")
        (folder / f"{name}_tests.py").write_text("import unittest\n", encoding="utf-8")
    request = SimpleNamespace(session_hash="alice")

    message, token = actions.reseal_tools(owner.token, request)

    assert calls[-1] == "count_words_in_text"
    assert token == owner.token
    assert "Stopped at count_words_in_text" in message
    assert "isolated tests did not pass" in message


def test_reseal_batch_reruns_missing_tools_and_requires_acceptance(tmp_path):
    """A missing record is re-run, and acceptance review is never granted here."""
    actions, owner, tools, _apps = setup(tmp_path)
    ran = []

    class Store:
        """Report every record as absent without touching storage."""

        def reseal(self, name, code, tests):
            """Return the missing-record reason for every tool."""
            return "missing"

    class Operations:
        """Report a passing isolated suite without executing generated code."""

        verification = SimpleNamespace(store=Store())

        def verify_existing_tool_tool(self, name):
            """Pass the isolated suite and record the call."""
            ran.append(name)
            return "TESTS_PROVISIONAL_PASSED:\nOK\nHuman acceptance review is still required."

    owner.controller.tool_operations = Operations()
    folder = tools / "alpha"
    folder.mkdir()
    (folder / "alpha_code.py").write_text("def alpha():\n    return 1\n", encoding="utf-8")
    (folder / "alpha_tests.py").write_text("import unittest\n", encoding="utf-8")

    message, _token = actions.reseal_tools(owner.token, SimpleNamespace(session_hash="alice"))

    assert "alpha" in ran
    assert "re-ran the isolated tests" in message
    assert "acceptance review" in message
    assert "bytes changed" not in message


def test_reveal_opens_the_owned_catalog_root_without_browser_paths(tmp_path):
    """V7-063: explorer buttons open server-resolved roots for the owning session only."""
    from agentix.controllers.sessions import SessionAccessError

    actions, owner, tools, apps = setup(tmp_path)
    opened = []
    actions.opener = opened.append
    request = SimpleNamespace(session_hash="alice")
    assert "tools" in actions.reveal("tool", owner.token, request).lower()
    assert opened == [tools.resolve()]
    assert "applications" in actions.reveal("application", owner.token, request).lower()
    assert opened[-1] == apps.root
    with pytest.raises(SessionAccessError):
        actions.reveal("tool", owner.token, SimpleNamespace(session_hash="bob"))
    with pytest.raises(ValueError):
        actions.reveal("unknown", owner.token, request)
    assert len(opened) == 2


def test_reveal_raises_the_opened_folder_above_the_browser(tmp_path):
    """V7-065: focus runs after a valid open, with the resolved folder name and prior handles."""
    actions, owner, tools, apps = setup(tmp_path)
    opened, focused = [], []
    actions.opener = opened.append
    actions.window_snapshot = lambda: frozenset({7})
    actions.focus_window = lambda name, before: focused.append((name, before)) or 8
    request = SimpleNamespace(session_hash="alice")
    assert actions.reveal("tool", owner.token, request) == "Opened the installed tools folder."
    assert actions.reveal("application", owner.token, request) == (
        "Opened the installed applications folder."
    )
    assert opened == [tools.resolve(), apps.root]
    assert focused == [("tools", frozenset({7})), (apps.root.name, frozenset({7}))]


def test_reveal_keeps_success_when_focus_is_refused(tmp_path):
    """A refused foreground change must not turn a completed open into a failed action."""
    actions, owner, tools, apps = setup(tmp_path)
    opened, focused = [], []
    actions.opener = opened.append
    actions.window_snapshot = lambda: frozenset()
    actions.focus_window = lambda name, before: focused.append(name) or (_ for _ in ()).throw(
        OSError("foreground refused")
    )
    request = SimpleNamespace(session_hash="alice")
    assert actions.reveal("tool", owner.token, request) == "Opened the installed tools folder."
    assert opened == [tools.resolve()]
    assert focused == ["tools"]


def test_reveal_opens_when_the_window_snapshot_fails(tmp_path):
    """A failed native enumeration must not block the folder the owner asked to open."""
    actions, owner, tools, apps = setup(tmp_path)
    opened, focused = [], []
    actions.opener = opened.append
    actions.window_snapshot = lambda: (_ for _ in ()).throw(OSError("enumeration failed"))
    actions.focus_window = lambda name, before: focused.append((name, before))
    request = SimpleNamespace(session_hash="alice")
    assert actions.reveal("tool", owner.token, request) == "Opened the installed tools folder."
    assert opened == [tools.resolve()]
    assert focused == [("tools", frozenset())]


def test_reveal_reports_an_opener_failure_as_a_validation_error(tmp_path):
    """V7-064: a refused shell open must reach the modal instead of a raw framework error."""
    actions, owner, tools, apps = setup(tmp_path)
    actions.window_snapshot = lambda: frozenset()
    actions.focus_window = lambda name, before: None

    def opener(path):
        """Refuse the open the way a missing shell association does."""
        raise OSError("no association")

    actions.opener = opener
    with pytest.raises(ValueError) as error:
        actions.reveal("tool", owner.token, SimpleNamespace(session_hash="alice"))
    assert "could not be opened" in str(error.value)


def test_reveal_never_focuses_a_foreign_session(tmp_path):
    """Ownership is checked before either the opener or the focus helper runs."""
    from agentix.controllers.sessions import SessionAccessError

    actions, owner, tools, apps = setup(tmp_path)
    opened, focused = [], []
    actions.opener = opened.append
    actions.window_snapshot = lambda: frozenset()
    actions.focus_window = lambda name, before: focused.append(name)
    with pytest.raises(SessionAccessError):
        actions.reveal("tool", owner.token, SimpleNamespace(session_hash="bob"))
    assert opened == [] and focused == []


def test_reveal_refuses_a_missing_or_aliased_directory(tmp_path):
    """A deleted or linked catalog root is reported instead of opening another folder."""
    actions, owner, tools, apps = setup(tmp_path)
    opened = []
    actions.opener = opened.append
    request = SimpleNamespace(session_hash="alice")
    owner.controller.security.TOOLS_ROOT_DIR = str(tmp_path / "missing")
    with pytest.raises(ValueError):
        actions.reveal("tool", owner.token, request)
    assert opened == []


def test_cancellation_does_not_remove_files(tmp_path):
    """Preparing and cancelling a destructive operation grants no deletion."""
    actions, owner, tools, apps = setup(tmp_path)
    request = SimpleNamespace(session_hash="alice")
    message, confirmation, token = actions.prepare(
        "tool", "count_words_in_text", owner.token, request
    )
    assert confirmation and "permanent" in message.lower()
    actions.cancel(confirmation, token, request)
    assert (tools / "count_words_in_text").exists()
    with pytest.raises(ValueError):
        actions.confirm(confirmation, token, request)


def test_confirmation_cannot_cross_sessions_or_be_replayed(tmp_path):
    """A foreign browser or repeated button request cannot reuse a deletion grant."""
    actions, owner, tools, apps = setup(tmp_path)
    request = SimpleNamespace(session_hash="alice")
    _, confirmation, token = actions.prepare("tool", "count_words_in_text", owner.token, request)
    with pytest.raises(ValueError):
        actions.confirm(confirmation, token, SimpleNamespace(session_hash="bob"))
    assert (tools / "count_words_in_text").exists()
    actions.confirm(confirmation, token, request)
    assert not (tools / "count_words_in_text").exists()
    with pytest.raises(ValueError):
        actions.confirm(confirmation, token, request)
