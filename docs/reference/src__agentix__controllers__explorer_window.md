# Reference for src/agentix/controllers/explorer_window.py

Raise the Explorer window opened for one catalog folder above the browser.

``os.startfile`` delegates to the shell, and Windows does not grant the
foreground to a process that does not already own it, so the folder window is
created behind the browser. This module locates that exact window and raises it
without leaving it permanently topmost.

Only ``ctypes`` from the standard library is used: no shell, no ``subprocess``,
no new dependency and no directory enumeration. Every native failure is reported
as ``OSError`` so callers can log it and keep the already completed open.

Source fingerprint: 064ec11f145921a885b857bf919dd0486060247d9e641d83fa6847eec572ffbf

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _native

Build the Win32 boundary once, declaring every signature explicitly.

Lazy construction keeps importing this module safe on a non-Windows host and
avoids loading ``ctypes.wintypes`` where it does not exist.

Kind: callable. Declared return: Any. Source line: 31.

### snapshot

Return visible Explorer folder windows before a folder is opened.

Only the window class is inspected; no title, path or document is read, and
nothing is created. A non-Windows host returns an empty set.

Kind: callable. Declared return: frozenset[int]. Source line: 85.

### snapshot.collect

Record one visible folder window and keep enumerating.

Kind: callable. Declared return: bool. Source line: 96.

### window_title

Return the bounded caption of one window; never raises for a stale handle.

Kind: callable. Declared return: str. Source line: 106.

### raise_window

Restore, raise and focus one window without leaving it always-on-top.

Returns:
    True when the window reached the top of the z-order. Keyboard focus is
    best effort because Windows may refuse it to a background process.

Kind: callable. Declared return: bool. Source line: 116.

### _class_name

Read the bounded window class name used to recognize a folder window.

Kind: callable. Declared return: str. Source line: 150.

### _matches

Accept the exact folder name or Explorer's localized ``name - suffix`` caption.

Kind: callable. Declared return: bool. Source line: 157.

### ExplorerWindowFocus

Select and raise the folder window that belongs to one completed open.

Native access, the clock and the sleep are injected so tests never touch a
real window and never wait. Selection prefers a handle that did not exist
before the open, because Explorer may also reuse an already open folder.

Kind: class. Declared return: Not declared / class. Source line: 168.

### ExplorerWindowFocus.__init__

Bind the native boundary and the bounded polling policy.

Kind: callable. Declared return: None. Source line: 176.

### ExplorerWindowFocus.snapshot

Return the current folder-window handles through the injected boundary.

Kind: callable. Declared return: frozenset[int]. Source line: 194.

### ExplorerWindowFocus.raise_for

Raise the window opened for ``folder_name``; return its handle or None.

Args:
    before: Handles observed before the folder was opened.
    folder_name: Base name of the already validated catalog folder.

Returns:
    The raised handle, or None when no matching window appeared.

Raises:
    OSError: The window was found but the native raise was refused.

Kind: callable. Declared return: int | None. Source line: 198.

### ExplorerWindowFocus._preferred

Prefer a caption match; fall back to any new handle only for a fresh window.

Kind: callable. Declared return: int | None. Source line: 235.

### focus_opened_window

Raise the Explorer window opened for ``folder_name`` using the default policy.

Kind: callable. Declared return: int | None. Source line: 246.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ctypes | Imported dependency for ctypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 20 |
| module | SUPPORTED | Module binding for SUPPORTED in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 22 |
| module | CABINET_WINDOW_CLASS | Module binding for CABINET WINDOW CLASS in module; use the enclosing contract and type below. | str | Module/process lifetime | 23 |
| module | DEFAULT_TIMEOUT_SECONDS | Module binding for DEFAULT TIMEOUT SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 24 |
| module | POLL_INTERVAL_SECONDS | Module binding for POLL INTERVAL SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 25 |
| module | TITLE_SEPARATOR | Module binding for TITLE SEPARATOR in module; use the enclosing contract and type below. | str | Module/process lifetime | 26 |
| module | _api | Typed binding for api in module; use the enclosing contract and type below. | Any | Module/process lifetime | 28 |
| _native | wintypes | Imported dependency for wintypes in _native; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 40 |
| _native | user32 | Local binding for user32 in _native; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| _native | kernel32 | Local binding for kernel32 in _native; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| _native | user32.EnumWindows.argtypes | Attribute for user32.EnumWindows.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 44 |
| _native | user32.EnumWindows.restype | Attribute for user32.EnumWindows.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| _native | user32.GetClassNameW.argtypes | Attribute for user32.GetClassNameW.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 46 |
| _native | user32.GetClassNameW.restype | Attribute for user32.GetClassNameW.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| _native | user32.GetWindowTextW.argtypes | Attribute for user32.GetWindowTextW.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 48 |
| _native | user32.GetWindowTextW.restype | Attribute for user32.GetWindowTextW.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| _native | user32.IsWindowVisible.argtypes | Attribute for user32.IsWindowVisible.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 50 |
| _native | user32.IsWindowVisible.restype | Attribute for user32.IsWindowVisible.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| _native | user32.ShowWindow.argtypes | Attribute for user32.ShowWindow.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 52 |
| _native | user32.ShowWindow.restype | Attribute for user32.ShowWindow.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| _native | user32.SetWindowPos.argtypes | Attribute for user32.SetWindowPos.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 54 |
| _native | user32.SetWindowPos.restype | Attribute for user32.SetWindowPos.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63 |
| _native | user32.BringWindowToTop.argtypes | Attribute for user32.BringWindowToTop.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 64 |
| _native | user32.BringWindowToTop.restype | Attribute for user32.BringWindowToTop.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| _native | user32.SetForegroundWindow.argtypes | Attribute for user32.SetForegroundWindow.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 66 |
| _native | user32.SetForegroundWindow.restype | Attribute for user32.SetForegroundWindow.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| _native | user32.SetFocus.argtypes | Attribute for user32.SetFocus.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 68 |
| _native | user32.SetFocus.restype | Attribute for user32.SetFocus.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| _native | user32.GetForegroundWindow.restype | Attribute for user32.GetForegroundWindow.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| _native | user32.GetWindowThreadProcessId.argtypes | Attribute for user32.GetWindowThreadProcessId.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 71 |
| _native | user32.GetWindowThreadProcessId.restype | Attribute for user32.GetWindowThreadProcessId.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| _native | user32.AttachThreadInput.argtypes | Attribute for user32.AttachThreadInput.argtypes in _native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 73 |
| _native | user32.AttachThreadInput.restype | Attribute for user32.AttachThreadInput.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| _native | kernel32.GetCurrentThreadId.restype | Attribute for kernel32.GetCurrentThreadId.restype in _native; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| _native | _api | Local binding for api in _native; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| snapshot | api | Local binding for api in snapshot; use the enclosing contract and type below. | Return type of _native; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| snapshot | found | Typed binding for found in snapshot; use the enclosing contract and type below. | set[int] | Enclosing invocation or class/instance lifetime | 94 |
| snapshot.collect | hwnd | Parameter for hwnd in snapshot.collect; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 96 |
| snapshot.collect | _param | Parameter for param in snapshot.collect; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 96 |
| window_title | hwnd | Parameter for hwnd in window_title; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 106 |
| window_title | api | Local binding for api in window_title; use the enclosing contract and type below. | Return type of _native; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| window_title | buffer | Local binding for buffer in window_title; use the enclosing contract and type below. | Return type of create_unicode_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| raise_window | hwnd | Parameter for hwnd in raise_window; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 116 |
| raise_window | api | Local binding for api in raise_window; use the enclosing contract and type below. | Return type of _native; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| raise_window | user32 | Local binding for user32 in raise_window; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 126 |
| raise_window | wintypes | Local binding for wintypes in raise_window; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 126 |
| raise_window | topmost | Local binding for topmost in raise_window; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 127 |
| raise_window | not_topmost | Local binding for not topmost in raise_window; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 127 |
| raise_window | flags | Local binding for flags in raise_window; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
| raise_window | foreground | Local binding for foreground in raise_window; use the enclosing contract and type below. | Return type of GetForegroundWindow; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| raise_window | current | Local binding for current in raise_window; use the enclosing contract and type below. | Return type of GetCurrentThreadId; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| raise_window | other | Local binding for other in raise_window; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 134 |
| raise_window | attached | Local binding for attached in raise_window; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| raise_window | raised | Local binding for raised in raise_window; use the enclosing contract and type below. | Return type of bool; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| _class_name | api | Parameter for api in _class_name; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 150 |
| _class_name | hwnd | Parameter for hwnd in _class_name; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 150 |
| _class_name | buffer | Local binding for buffer in _class_name; use the enclosing contract and type below. | Return type of create_unicode_buffer; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| _matches | title | Parameter for title in _matches; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 157 |
| _matches | folder_name | Parameter for folder name in _matches; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 157 |
| _matches | normalized | Local binding for normalized in _matches; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 159 |
| _matches | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 159 |
| module | _NATIVE_SNAPSHOT | Module binding for NATIVE SNAPSHOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 163 |
| module | _NATIVE_TITLE | Module binding for NATIVE TITLE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 164 |
| module | _NATIVE_RAISE | Module binding for NATIVE RAISE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 165 |
| ExplorerWindowFocus.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 177 |
| ExplorerWindowFocus.__init__ | enumerate_windows | Parameter for enumerate windows in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| ExplorerWindowFocus.__init__ | window_title | Parameter for window title in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 180 |
| ExplorerWindowFocus.__init__ | raise_window | Parameter for raise window in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 181 |
| ExplorerWindowFocus.__init__ | clock | Parameter for clock in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 182 |
| ExplorerWindowFocus.__init__ | sleep | Parameter for sleep in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| ExplorerWindowFocus.__init__ | timeout | Parameter for timeout in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 184 |
| ExplorerWindowFocus.__init__ | interval | Parameter for interval in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 185 |
| ExplorerWindowFocus.__init__ | self.enumerate_windows | Attribute for enumerate windows in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 188 |
| ExplorerWindowFocus.__init__ | self.window_title | Attribute for window title in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 189 |
| ExplorerWindowFocus.__init__ | self.raise_window | Attribute for raise window in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 190 |
| ExplorerWindowFocus.__init__ | self.clock | Attribute for clock in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 191 |
| ExplorerWindowFocus.__init__ | self.sleep | Attribute for sleep in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 191 |
| ExplorerWindowFocus.__init__ | self.timeout | Attribute for timeout in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 192 |
| ExplorerWindowFocus.__init__ | self.interval | Attribute for interval in ExplorerWindowFocus.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 192 |
| ExplorerWindowFocus.snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 194 |
| ExplorerWindowFocus.raise_for | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 198 |
| ExplorerWindowFocus.raise_for | before | Parameter for before in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 198 |
| ExplorerWindowFocus.raise_for | folder_name | Parameter for folder name in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 198 |
| ExplorerWindowFocus.raise_for | known | Local binding for known in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Enclosing invocation or class/instance lifetime | 213 |
| ExplorerWindowFocus.raise_for | deadline | Local binding for deadline in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 214 |
| ExplorerWindowFocus.raise_for | attempts | Local binding for attempts in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 215, 219 |
| ExplorerWindowFocus.raise_for | current | Typed binding for current in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | frozenset[int] | Enclosing invocation or class/instance lifetime | 216, 220 |
| ExplorerWindowFocus.raise_for | target | Local binding for target in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 217, 223, 226 |
| ExplorerWindowFocus.raise_for | fresh | Local binding for fresh in ExplorerWindowFocus.raise_for; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| ExplorerWindowFocus._preferred | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 235 |
| ExplorerWindowFocus._preferred | handles | Parameter for handles in ExplorerWindowFocus._preferred; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 235 |
| ExplorerWindowFocus._preferred | folder_name | Parameter for folder name in ExplorerWindowFocus._preferred; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 235 |
| ExplorerWindowFocus._preferred | allow_any | Parameter for allow any in ExplorerWindowFocus._preferred; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 235 |
| ExplorerWindowFocus._preferred | matches | Local binding for matches in ExplorerWindowFocus._preferred; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 237 |
| ExplorerWindowFocus._preferred.comprehension_237 | hwnd | Comprehension item for hwnd in ExplorerWindowFocus._preferred.comprehension_237; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 237 |
| module | _DEFAULT | Module binding for DEFAULT in module; use the enclosing contract and type below. | Return type of ExplorerWindowFocus; see its callable contract | Module/process lifetime | 243 |
| focus_opened_window | folder_name | Parameter for folder name in focus_opened_window; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 246 |
| focus_opened_window | before | Parameter for before in focus_opened_window; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 246 |
