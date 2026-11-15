"""V7-065: the Explorer window opened for a catalog folder is raised above the browser."""

import pytest


def focus(**overrides):
    """Compose the focus helper over injected native boundaries, never real windows."""
    from agentix.controllers.explorer_window import ExplorerWindowFocus

    options = dict(
        enumerate_windows=lambda: frozenset(),
        window_title=lambda hwnd: "",
        raise_window=lambda hwnd: True,
        clock=lambda: 0.0,
        sleep=lambda seconds: None,
        timeout=2.0,
        interval=0.05,
    )
    options.update(overrides)
    return ExplorerWindowFocus(**options)


def test_focus_prefers_the_window_that_appeared_after_opening():
    """A new CabinetWClass handle wins over an older window with a similar title."""
    raised = []
    helper = focus(
        enumerate_windows=lambda: frozenset({11, 22}),
        window_title=lambda hwnd: {11: "tools", 22: "tools - Explorador de archivos"}[hwnd],
        raise_window=lambda hwnd: raised.append(hwnd) or True,
    )
    assert helper.raise_for(frozenset({11}), "tools") == 22
    assert raised == [22]


def test_focus_falls_back_to_the_localized_title_prefix():
    """Explorer reuses an open folder, so no new handle appears and the title decides."""
    raised = []
    ticks = iter([0.0, 2.1])
    titles = {
        31: "applications - Explorador de archivos",
        32: "tools - Explorador de archivos",
        33: "Documentos",
    }
    helper = focus(
        enumerate_windows=lambda: frozenset(titles),
        window_title=titles.__getitem__,
        raise_window=lambda hwnd: raised.append(hwnd) or True,
        clock=lambda: next(ticks),
    )
    assert helper.raise_for(frozenset(titles), "applications") == 31
    assert raised == [31]


def test_focus_ignores_a_folder_whose_name_only_shares_a_prefix():
    """A sibling folder such as tools_archive must not be raised for tools."""
    raised = []
    ticks = iter([0.0, 2.1])
    titles = {41: "tools_archive - Explorador de archivos"}
    helper = focus(
        enumerate_windows=lambda: frozenset(titles),
        window_title=titles.__getitem__,
        raise_window=lambda hwnd: raised.append(hwnd) or True,
        clock=lambda: next(ticks),
    )
    assert helper.raise_for(frozenset(titles), "tools") is None
    assert raised == []


def test_focus_polls_until_the_timeout_without_sleeping_for_real():
    """A slow shell is awaited with a bounded number of injected clock/sleep calls."""
    ticks = iter([0.0, 0.1, 0.2, 0.3, 0.4])
    sleeps = []
    helper = focus(
        enumerate_windows=lambda: frozenset(),
        clock=lambda: next(ticks),
        sleep=sleeps.append,
        timeout=0.3,
        interval=0.1,
    )
    assert helper.raise_for(frozenset(), "tools") is None
    assert sleeps == [0.1, 0.1]


def test_focus_reports_a_native_raise_failure():
    """A refused SetWindowPos/SetForegroundWindow surfaces as an OSError, not silence."""
    helper = focus(
        enumerate_windows=lambda: frozenset({51}),
        window_title=lambda hwnd: "tools",
        raise_window=lambda hwnd: False,
    )
    with pytest.raises(OSError):
        helper.raise_for(frozenset(), "tools")


def test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows(monkeypatch):
    """Non-Windows hosts enumerate nothing and never call a native function."""
    from agentix.controllers import explorer_window

    monkeypatch.setattr(explorer_window, "SUPPORTED", False)
    assert explorer_window.snapshot() == frozenset()
    assert explorer_window.focus_opened_window("tools", frozenset()) is None
