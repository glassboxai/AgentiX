# V7-061: catalog services outside the installed-application policy

## Observed defect

After V7-060 changed `storage/maintenance.py`, every installed application was
listed as `(re-approval required)` on the next launch. The owner had already
re-verified the four applications once after V7-059, so a second full
re-verification was required for a change that never touches execution.

## Cause

`app_policy()` (`src/agentix/storage/installed_apps.py`) hashed 24 maintained
sources, including `storage/maintenance.py`. Every approval record stores the
policy digest captured when it was sealed, and `_validated` compares it on each
authorized read, so any edit to a hashed file invalidates all installed records
at once.

`storage/maintenance.py` is the confirmed permanent-removal service. Its own
docstring states that no generated source is imported or executed, and the only
module importing it is `controllers/catalog.py`, the deletion route. It is not
staged into the AppContainer child: `code_package.SHARED` holds `app.py`,
`operation.py`, `application_context.py`, `element_ids.py` and
`application_values.py`, and `widget_session` copies `widget_worker.py`,
`ipc_protocol.py`, `widget_identity.py` and `callback_runtime.py`. Hashing it
bound the approval to a service that cannot influence what runs.

## Solution

`src/agentix/storage/installed_apps.py`: `storage/maintenance.py` is removed from
the `app_policy()` tuple, and the docstring now states that the digest binds the
execution boundary and runtime rather than catalog services. Twenty-three files
remain hashed, including every execution member: `sandbox/windows_process.py`,
`lab/widget_worker.py`, `lab/application_session.py`,
`application/templates/code/*`, `domain/application_code.py`,
`domain/tool_schema.py`, `application/general_package.py`,
`application/general_acceptance.py`, `lab/application_artifacts.py` and
`storage/installed_apps.py`.

The execution gate is unchanged: `get()` still refuses a stale policy, so a stale
application cannot be launched, and `reverify_app` remains the only path that
reseals a binding. Removal keeps its own independent gates: the cross-process
catalog lock, the usage lease, composite dependency references, the exact package
digest, the review digest and a full recomputation in `confirm()`.

`storage/usage.py`, `storage/catalog_lock.py`, `layout_contracts.py` and
`ui/assets/application_editor.js` stay hashed. They do not run in the child, but
they participate in host validation: `catalog_lock.reject_alias` validates the
package closure in `general_package.py`, `usage.py` backs the removal lease,
`layout_contracts.py` validates persisted geometry and `application_editor.js` is
served to the browser by `app_controls.py`. Excluding them would weaken real
checks, so each would need its own justified block.

## Consequence

Removing an entry changes the digest once more. The policy moved from
`adb73a462251f741…` to `e22809c743f4bb45…`, so the installed applications require
one final re-verification. After that, removal fixes no longer invalidate
launches.

## Evidence

- `tests/test_installed_apps.py`: modifying `storage/maintenance.py` in a copied
  tree leaves `app_policy()` unchanged, while modifying
  `domain/application_code.py` changes it.
- `tests/test_installed_apps.py`, `tests/test_catalog_maintenance.py`,
  `tests/test_v5_policy_bindings.py` and `tests/test_module_closure.py`:
  51 passed. The closure test still sees 23 hashed paths against its minimum of 20.
- Ruff lint and format pass on the two touched files; the offline suite and
  `tools/build_reference.py --check` were run for this block.

No live model run, browser check or process restart was performed.
