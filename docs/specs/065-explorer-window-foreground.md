# V7-065: the catalog folder window is raised above the browser

Approved scope: after `View in explorer` completes, the Explorer window that shows
the installed Tools or Applications folder must appear above the AgentiX window.
No change to the reveal roots, ownership checks, approvals, `app_policy()`,
`generated_tools` content, live processes or V7-064.

## Requirement

`os.startfile` delegates to the shell, and Windows does not grant the foreground to
a process that does not already own it. The folder window was therefore created
behind the browser, so the owner had to find it manually. The owner confirmed the
window opens and asked only for it to be brought to the front.

Observable acceptance:

- Pressing `View in explorer` in Tools leaves the tools folder window above the
  AgentiX window, with keyboard focus on it.
- Pressing `View in explorer` in Applications does the same for the applications
  folder.
- The window is not left permanently always-on-top.
- A refused foreground change never turns a completed open into a failed action:
  the success message stays and the refusal is logged.
- A foreign session, an unknown catalog, a missing folder or a linked folder is
  still refused before either the opener or the focus helper runs.
- Non-Windows hosts and hosts without a matching window are a no-op.

## Contract

`src/agentix/controllers/explorer_window.py` is new and uses only `ctypes` from the
standard library, matching the existing precedent in `sandbox/windows_process.py`
and `security/credentials.py`. No shell, no `subprocess`, no new dependency and no
directory enumeration.

- `snapshot()` returns the visible `CabinetWClass` handles. Only the window class
  and visibility are inspected; no title, path or document is read.
- `window_title(hwnd)` returns a bounded caption and never raises for a stale
  handle.
- `raise_window(hwnd)` restores the window, raises it with
  `SetWindowPos(HWND_TOPMOST)` immediately followed by `HWND_NOTOPMOST`, attaches
  the input queues with `AttachThreadInput`, then calls `BringWindowToTop`,
  `SetForegroundWindow` and `SetFocus`, and always detaches. It returns whether the
  window reached the top of the z-order; keyboard focus stays best effort because
  Windows may refuse it to a background process.
- `ExplorerWindowFocus.raise_for(before, folder_name)` polls the injected
  enumeration until a handle absent from `before` appears, bounded by an injected
  clock, an injected sleep and an attempt cap derived from `timeout / interval`.
  It prefers a caption match among the new handles. When Explorer reuses an
  already open folder, no new handle appears and it falls back to a caption match
  only, accepting the exact name or the localized `name - suffix` form. A sibling
  such as `tools_archive` never matches `tools`. A refused native raise is
  reported as `OSError`.
- `focus_opened_window(folder_name, before)` applies the default policy.

`CatalogMaintenanceBackend.__init__` accepts `window_snapshot` and `focus_window`,
defaulting to the module functions, so tests never touch a real window.
`reveal` captures the snapshot before the opener, opens the validated folder, then
calls the focus helper with the resolved folder name. `OSError` and `ValueError`
from the focus helper are logged as `catalog_folder_focus_failed` and the success
message is unchanged.

## Acceptance and regression

- `tests/test_explorer_window.py` covers the fresh handle, the localized title
  fallback, the `tools_archive` prefix rejection, the bounded poll with injected
  clock and sleep, the refused native raise and the non-Windows no-op.
- `tests/test_maintenance_owners.py::test_reveal_raises_the_opened_folder_above_the_browser`
  asserts both catalogs focus the resolved folder name with the pre-open handles.
- `tests/test_maintenance_owners.py::test_reveal_keeps_success_when_focus_is_refused`
  asserts the open still succeeds and the helper was called.
- `tests/test_maintenance_owners.py::test_reveal_never_focuses_a_foreign_session`
  asserts neither the opener nor the focus helper runs for another owner.
- `tests/test_maintenance_owners.py::test_reveal_opens_when_the_window_snapshot_fails`
  asserts a failed native enumeration still opens the folder with an empty snapshot.
- The existing reveal, missing-root and aliased-root regressions are unchanged.

## Verification

Executed on 2026-11-12 with the managed v5 interpreter
(`D:/AI/Agentix-data/v7/environments/7d6df7e204a38b63/Scripts/python.exe`):

- First red run: 8 failed, 5 passed. The new module did not exist and `reveal`
  never called a focus helper.
- Second run exposed two test defects, not product defects: an injected clock that
  never advanced made the poll loop unbounded, and the fixture's applications root
  is named `installed`, not `applications`. The tests now advance the clock and use
  the resolved name; `raise_for` also gained an attempt cap so a non-advancing
  clock cannot spin.
- `tests/test_explorer_window.py` and `tests/test_maintenance_owners.py`: 14 passed.
- Focused offline set (`test_catalog_maintenance`, `test_applications_backend`,
  `test_ui_stylesheet`, `test_reference_freshness`): 48 passed.
- Ruff lint and format: clean on the four changed Python files.
- Native acceptance against a disposable loopback server on port 7899 with a
  temporary `AGENTIX_HOME`, invoking the real reveal endpoints exactly as the
  buttons do: both reported `success=True`, `GetForegroundWindow()` equalled the
  folder window, that window was first in `EnumWindows` z-order, and the captions
  were `tools - Explorador de archivos` and `applications - Explorador de
  archivos`. The first pass exercised the fresh-handle path; the second pass
  exercised the reuse path with `new_handles=0`. The disposable server was stopped
  afterwards; the live 7878 process was not restarted and keeps the previous code
  until the owner relaunches it.

`explorer_window.py` is not part of `app_policy()`, so the policy digest and the
installed approvals are unchanged.
