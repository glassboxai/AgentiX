# V7-064: actionable catalog dependency diagnostics

Approved scope (option A): keep the closed-by-default approval behaviour and the
current revocation of invalid durable records, and fix only the diagnosis and the
documented recovery. No change to `security/approval_store.py`, no change to
`policy_fingerprint()`, no change to `app_policy()`, no change to tool sources,
independent human-reviewed cases, AppContainer or `generated_tools`. V7-066
(option B1) remains a separate, unapproved proposal.

## Requirement

`Re-verify selected app` reported
`Re-verification failed (CatalogDependencyError). The stored application remains
unapproved.` and `Load selected app` reported
`Application load failed (CatalogDependencyError).`, so the owner could not tell
what to do or recover a previously created application.

Observable acceptance:

- Both actions name the missing approval and the recovery step, and never show
  only the exception type.
- A missing application dependency names the tool and its maintained skip reason.
- A refused shell open reaches the maintained modal instead of a raw framework
  error.
- The stored application stays unapproved when a gate fails.
- Ownership, root validation, linked-folder refusal and the reveal success message
  are unchanged.

## Contract

- `src/agentix/application/app_invocation.py`: `check_dependencies` raises
  `CatalogDependencyError` listing every missing role with the registry's
  `_skip_reason` when the registry exposes it, falling back to
  `no current reusable approval`. Reasons never include source, prompts or
  approval internals. `CatalogDependencyError` subclasses `ValueError`, so the
  existing `except (OSError, ValueError)` callers keep their behaviour.
- `src/agentix/controllers/applications.py`: `load_app` and `reverify_app` catch
  `CatalogDependencyError` before the generic handler and yield its text.
  `reverify_app` keeps its `application_reverify_failed` warning and appends
  `The stored application remains unapproved.` so the stored state is explicit.
  The generic handler is unchanged for every other exception type.
- `src/agentix/controllers/catalog.py`: `open_directory` converts an `OSError`
  from `os.startfile` into `ValueError`, and `reveal` converts an `OSError` from
  any injected opener into `ValueError` naming the catalog, so `guard_result`
  opens the modal. The success message is unchanged.

## Acceptance and regression

- `tests/test_installed_apps.py::test_load_app_reports_the_missing_catalog_approval_actionably`
  asserts the load message omits the type name and names the approval recovery.
- `tests/test_installed_apps.py::test_reverify_app_reports_the_missing_catalog_approval_actionably`
  asserts the same for re-verification and keeps `unapproved` visible.
- `tests/test_installed_apps.py::test_check_dependencies_names_the_tool_without_a_reusable_approval`
  asserts the tool name and the maintained skip reason.
- `tests/test_maintenance_owners.py::test_reveal_reports_an_opener_failure_as_a_validation_error`
  asserts a refused open becomes `ValueError`.
- Existing load, re-verify, rebind, reveal, missing-root, aliased-root and
  foreign-session regressions are unchanged.

## Verification

Executed on 2026-11-12 with the managed v5 interpreter
(`D:/AI/Agentix-data/v7/environments/7d6df7e204a38b63/Scripts/python.exe`):

- Red run: the three `test_installed_apps.py` cases failed with
  `assert 'CatalogDependencyError' not in 'Application...dencyError).'` and
  `assert 'CatalogDependencyError' not in 'Re-verifica... unapproved.'`; the
  opener case failed with the raw `OSError: no association`.
- Green run of `test_installed_apps.py`, `test_maintenance_owners.py` and
  `test_explorer_window.py`: 50 passed.
- Full offline suite on the final code: 1038 passed, 85 deselected, 0 failed
  (362 s, exit 0).
- Ruff lint and format: clean on the five changed Python files.
- Real-framework smoke check on a disposable loopback server on port 7898 with a
  temporary `AGENTIX_HOME`: the page returned 200, both `tools-reveal` and
  `apps-reveal` components were registered and 65 dependencies were wired, so the
  changed controllers still compose. The server was stopped afterwards.
- `app_policy()` is `859d7f910c68615c...` and `policy_fingerprint()` is
  `37e3c5b979943c4e...`, both unchanged, so installed approvals and durable tool
  records are not invalidated by this block.

## Recovery for the already lost approvals

The five durable records were deleted on 2026-11-11 21:01:30 by the previous
policy change; this block cannot restore them. Recovery is to execute and approve
each tool in Tools and then re-verify each application. V7-066 (option B1) would
prevent the same loss on a future additive policy change by keeping the record and
letting the policy mismatch invalidate it, and it is not part of this block.
