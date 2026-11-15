# V7-063: catalog explorer buttons and per-tool handle colors

Approved scope: two read-only "View in explorer" buttons that open the installed
Tools and Applications folders, plus a per-tool color on the move handle inside a
generated application's Edit mode. No generated widget source, approval hash,
executable path, live process or `generated_tools` content changes.

## Requirement

The owner needs to reach the installed catalogs from the GUI without copying
paths, and needs to recognize which widgets belong to the same tool while
rearranging a composed application.

Observable acceptance:

- Tools shows `View in explorer` next to `Installed Tools Catalog`; pressing it
  opens the installed tools folder.
- Applications shows `View in explorer` next to `Installed Apps Catalog`; pressing
  it opens the installed applications folder.
- The browser never supplies a path; a foreign session, an unknown catalog, a
  missing folder or a linked folder is reported instead of opened.
- In Edit, every move handle of one tool shares one color; different tools differ;
  Status and each public input keep their own color.
- The color appears only on the move handle, is re-randomized on each Edit entry
  and is not persisted; leaving Edit restores the base handle color.

## Contract

`src/agentix/security/__init__.py` adds `published_tools_root()`. It returns the
published catalog root, never `TOOLS_ROOT_DIR`, because that attribute points at
the isolated draft directory while a tool proposal is active.

`src/agentix/controllers/catalog.py` adds
`CatalogMaintenanceBackend.reveal(kind, token, request)`. It resolves ownership
through `SessionOwnerAccess`, derives the root from server state
(`published_tools_root()` or `library_factory().root`), rejects a symbolic link,
a missing directory and a reparse point, and then calls an injected opener that
defaults to `os.startfile`. No shell, no `subprocess`, no browser path and no
directory creation. The opener is injectable so tests never launch Explorer.

`src/agentix/ui/tools.py` and `src/agentix/ui/apps_catalog.py` render the buttons
only when a maintenance backend exists and wire them through
`dialog.guard_result(handler, 0)`, so a rejected request opens the existing modal
instead of surfacing a native exception.

`src/agentix/layout_contracts.py` adds `application_layout_groups(manifest)`,
which maps each movable control to its tool using the same `ElementIds` registry
that already derives the allowlist. Status and each public input are their own
groups; legacy schema-2 manifests return an empty mapping. The function is
presentation data and never widens `application_layout_ids`.

`src/agentix/storage/installed_apps.py` exposes `layout_groups(identity)` over the
reviewed manifest, and `src/agentix/application/app_controls.py` adds the
additive `groups` field to the authorized `GET /_agentix/layout` payload.

`src/agentix/ui/assets/application_editor.js` assigns one random hue per group on
each Edit entry and sets `--application-handle-color` on the move handle only.
`src/agentix/ui/assets/style.css` consumes that variable with the previous
`#162630` fallback, so leaving Edit needs no extra rule.

## Acceptance and regression

- `tests/test_maintenance_owners.py::test_reveal_opens_the_owned_catalog_root_without_browser_paths`
  covers both catalogs, the injected opener, a foreign session and an unknown kind.
- `tests/test_maintenance_owners.py::test_reveal_refuses_a_missing_or_aliased_directory`
  covers a missing root and asserts the opener is never called.
- `tests/test_code_application.py::test_v7_063_layout_groups_bind_widget_controls_to_their_tool`
  covers same-tool grouping, distinct tools, separate Status/input groups and the
  legacy empty mapping, and asserts the group keys equal the movable allowlist.
- `tests/test_code_application.py::test_v7_063_editor_colors_only_the_move_handle_per_tool`
  drives the real editor script with inert DOM controls: same tool equal, other
  tool different, Status distinct, and the base color restored after Edit.

## Verification

Executed on 2026-11-11 with the managed v5 interpreter
(`D:/AI/Agentix-data/v7/environments/7d6df7e204a38b63/Scripts/python.exe`):

- `tests/test_maintenance_owners.py`: 4 passed. The first run failed because the
  fixture never created the applications root, which the contract deliberately
  refuses to open; the fixture now creates that folder instead of relaxing the
  check.
- `tests/test_code_application.py`: 13 passed, 10 deselected. The first run
  exposed a wrong assumption in the regression: widget scopes derive from the
  widget id, not the tool name. The assertions now use the real
  `application_<widget>_<role>` identifiers.
- Browser (`-m browser`, installed Microsoft Edge): 4 passed, 19 deselected,
  including the new per-tool handle color check and the existing V6-044 and
  V7-062 editor regressions.
- Focused offline set (`test_application_controls`, `test_installed_apps`,
  `test_application_update`, `test_catalog_maintenance`,
  `test_applications_backend`, `test_ui_stylesheet`): 80 passed.
- Ruff lint and format: clean on the nine changed Python files.
- `tools/build_reference.py` then `--check`: no issues;
  `tests/unit/test_reference_freshness.py`: 3 passed.
- Full offline suite: 1024 passed, 85 deselected, 0 failed (577.74 s).

`layout_contracts.py`, `application/app_controls.py` and
`ui/assets/application_editor.js` participate in `app_policy()`, so the policy
digest moved to
`859d7f910c68615cb0cfd6196d9b7768161e62a5f7d73c40a94f95cca9892232` and installed
applications require re-approval. No live process was restarted and nothing was
deployed to the GUI.
