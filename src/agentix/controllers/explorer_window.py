"""Raise the Explorer window opened for one catalog folder above the browser.

``os.startfile`` delegates to the shell, and Windows does not grant the
foreground to a process that does not already own it, so the folder window is
created behind the browser. This module locates that exact window and raises it
without leaving it permanently topmost.

Only ``ctypes`` from the standard library is used: no shell, no ``subprocess``,
no new dependency and no directory enumeration. Every native failure is reported
as ``OSError`` so callers can log it and keep the already completed open.
"""

import ctypes
import logging
import sys
import time
from types import SimpleNamespace
from typing import Any

logger = logging.getLogger(__name__)

SUPPORTED = sys.platform == "win32"
CABINET_WINDOW_CLASS = "CabinetWClass"
DEFAULT_TIMEOUT_SECONDS = 2.0  # Bounded wait for the shell to create or reuse a window.
POLL_INTERVAL_SECONDS = 0.05  # Poll cadence while the shell window is still appearing.
TITLE_SEPARATOR = " - "  # Explorer appends a localized suffix after the folder name.

_api: Any = None


def _native() -> Any:
    """Build the Win32 boundary once, declaring every signature explicitly.

    Lazy construction keeps importing this module safe on a non-Windows host and
    avoids loading ``ctypes.wintypes`` where it does not exist.
    """
    global _api
    if _api is not None:
        return _api
    from ctypes import wintypes

    user32 = ctypes.WinDLL("user32", use_last_error=True)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    user32.EnumWindows.argtypes = [ctypes.c_void_p, wintypes.LPARAM]
    user32.EnumWindows.restype = wintypes.BOOL
    user32.GetClassNameW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
    user32.GetClassNameW.restype = ctypes.c_int
    user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
    user32.GetWindowTextW.restype = ctypes.c_int
    user32.IsWindowVisible.argtypes = [wintypes.HWND]
    user32.IsWindowVisible.restype = wintypes.BOOL
    user32.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]
    user32.ShowWindow.restype = wintypes.BOOL
    user32.SetWindowPos.argtypes = [
        wintypes.HWND,
        wintypes.HWND,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_uint,
    ]
    user32.SetWindowPos.restype = wintypes.BOOL
    user32.BringWindowToTop.argtypes = [wintypes.HWND]
    user32.BringWindowToTop.restype = wintypes.BOOL
    user32.SetForegroundWindow.argtypes = [wintypes.HWND]
    user32.SetForegroundWindow.restype = wintypes.BOOL
    user32.SetFocus.argtypes = [wintypes.HWND]
    user32.SetFocus.restype = wintypes.HWND
    user32.GetForegroundWindow.restype = wintypes.HWND
    user32.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
    user32.GetWindowThreadProcessId.restype = wintypes.DWORD
    user32.AttachThreadInput.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.BOOL]
    user32.AttachThreadInput.restype = wintypes.BOOL
    kernel32.GetCurrentThreadId.restype = wintypes.DWORD
    _api = SimpleNamespace(
        user32=user32,
        kernel32=kernel32,
        wintypes=wintypes,
        enum_proc=ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM),
    )
    return _api


def snapshot() -> frozenset[int]:
    """Return visible Explorer folder windows before a folder is opened.

    Only the window class is inspected; no title, path or document is read, and
    nothing is created. A non-Windows host returns an empty set.
    """
    if not SUPPORTED:
        return frozenset()
    api = _native()
    found: set[int] = set()

    def collect(hwnd: int, _param: int) -> bool:
        """Record one visible folder window and keep enumerating."""
        if api.user32.IsWindowVisible(hwnd) and _class_name(api, hwnd) == CABINET_WINDOW_CLASS:
            found.add(int(hwnd))
        return True

    api.user32.EnumWindows(api.enum_proc(collect), 0)
    return frozenset(found)


def window_title(hwnd: int) -> str:
    """Return the bounded caption of one window; never raises for a stale handle."""
    if not SUPPORTED:
        return ""
    api = _native()
    buffer = ctypes.create_unicode_buffer(512)
    api.user32.GetWindowTextW(hwnd, buffer, 512)
    return buffer.value


def raise_window(hwnd: int) -> bool:
    """Restore, raise and focus one window without leaving it always-on-top.

    Returns:
        True when the window reached the top of the z-order. Keyboard focus is
        best effort because Windows may refuse it to a background process.
    """
    if not SUPPORTED:
        return False
    api = _native()
    user32, wintypes = api.user32, api.wintypes
    topmost, not_topmost = wintypes.HWND(-1), wintypes.HWND(-2)
    flags = 0x0001 | 0x0002 | 0x0040  # SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW
    user32.ShowWindow(hwnd, 9)  # SW_RESTORE
    user32.SetWindowPos(hwnd, topmost, 0, 0, 0, 0, flags)
    user32.SetWindowPos(hwnd, not_topmost, 0, 0, 0, 0, flags)
    foreground = user32.GetForegroundWindow()
    current = api.kernel32.GetCurrentThreadId()
    other = user32.GetWindowThreadProcessId(foreground, None) if foreground else 0
    attached = (
        bool(user32.AttachThreadInput(current, other, True))
        if other and other != current
        else False
    )
    try:
        raised = bool(user32.BringWindowToTop(hwnd))
        user32.SetForegroundWindow(hwnd)
        user32.SetFocus(hwnd)
    finally:
        if attached:
            user32.AttachThreadInput(current, other, False)
    return raised


def _class_name(api: Any, hwnd: int) -> str:
    """Read the bounded window class name used to recognize a folder window."""
    buffer = ctypes.create_unicode_buffer(64)
    api.user32.GetClassNameW(hwnd, buffer, 64)
    return buffer.value


def _matches(title: str, folder_name: str) -> bool:
    """Accept the exact folder name or Explorer's localized ``name - suffix`` caption."""
    normalized, name = title.casefold(), folder_name.casefold()
    return normalized == name or normalized.startswith(name + TITLE_SEPARATOR)


_NATIVE_SNAPSHOT = snapshot
_NATIVE_TITLE = window_title
_NATIVE_RAISE = raise_window


class ExplorerWindowFocus:
    """Select and raise the folder window that belongs to one completed open.

    Native access, the clock and the sleep are injected so tests never touch a
    real window and never wait. Selection prefers a handle that did not exist
    before the open, because Explorer may also reuse an already open folder.
    """

    def __init__(
        self,
        *,
        enumerate_windows=None,
        window_title=None,
        raise_window=None,
        clock=time.monotonic,
        sleep=time.sleep,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        interval: float = POLL_INTERVAL_SECONDS,
    ) -> None:
        """Bind the native boundary and the bounded polling policy."""
        self.enumerate_windows = enumerate_windows or _NATIVE_SNAPSHOT
        self.window_title = window_title or _NATIVE_TITLE
        self.raise_window = raise_window or _NATIVE_RAISE
        self.clock, self.sleep = clock, sleep
        self.timeout, self.interval = timeout, interval

    def snapshot(self) -> frozenset[int]:
        """Return the current folder-window handles through the injected boundary."""
        return frozenset(self.enumerate_windows())

    def raise_for(self, before, folder_name: str) -> int | None:
        """Raise the window opened for ``folder_name``; return its handle or None.

        Args:
            before: Handles observed before the folder was opened.
            folder_name: Base name of the already validated catalog folder.

        Returns:
            The raised handle, or None when no matching window appeared.

        Raises:
            OSError: The window was found but the native raise was refused.
        """
        if not SUPPORTED:
            return None
        known = frozenset(before or ())
        deadline = self.clock() + self.timeout
        attempts = max(1, int(self.timeout / self.interval) + 2) if self.interval > 0 else 1
        current: frozenset[int] = frozenset()
        target = None
        while attempts > 0:
            attempts -= 1
            current = self.snapshot()
            fresh = sorted(current - known)
            if fresh:
                target = self._preferred(fresh, folder_name, allow_any=True)
                break
            if self.clock() >= deadline or attempts == 0:
                target = self._preferred(sorted(current), folder_name, allow_any=False)
                break
            self.sleep(self.interval)
        if target is None:
            return None
        if not self.raise_window(target):
            raise OSError("The Explorer window could not be raised")
        return target

    def _preferred(self, handles, folder_name: str, *, allow_any: bool) -> int | None:
        """Prefer a caption match; fall back to any new handle only for a fresh window."""
        matches = [hwnd for hwnd in handles if _matches(self.window_title(hwnd), folder_name)]
        if matches:
            return matches[0]
        return handles[0] if allow_any and handles else None


_DEFAULT = ExplorerWindowFocus()


def focus_opened_window(folder_name: str, before) -> int | None:
    """Raise the Explorer window opened for ``folder_name`` using the default policy."""
    return _DEFAULT.raise_for(before, folder_name)
