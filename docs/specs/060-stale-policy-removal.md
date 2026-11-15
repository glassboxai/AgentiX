# V7-060: permanent application removal ignores a stale policy binding

## Observed defect

Selecting the installed application `SuperRepeater` and pressing
`Delete selected application` returned `Application approval is stale` instead of
deleting it. The owner wanted the package removed, not executed, so a policy
mismatch should not have blocked the operation.

The log recorded `installed_app_rejected app_id=3d47a874c1274fb8a0c98b4267d85981
name=SuperRepeater status=approval_stale detail=Application approval is stale`
on every catalog refresh, and the same status for `MultiplyAll2`,
`VowelsExceptA` and `MultiplyVowelsAndWords`.

## Cause

`CatalogMaintenance._prepare` resolved the application through
`InstalledApps.get()`, which passes `require_policy=True`. That comparison
rejects a record whose sealed `policy` differs from the current `app_policy()`.

`app_policy()` hashes maintained sources, including
`domain/application_code.py`, which V7-059 edited. Every installed record was
sealed under the previous policy, so all four applications became
`approval_stale` at once. Verified against the live library with the managed
interpreter:

```
current policy: 6964ca4eed93be97
MultiplyAll2            approval_stale  record policy: dd2d82646652a47b  match: False
SuperRepeater           approval_stale  record policy: dd2d82646652a47b  match: False
VowelsExceptA           approval_stale  record policy: dd2d82646652a47b  match: False
MultiplyVowelsAndWords  approval_stale  record policy: dd2d82646652a47b  match: False
```

The policy binding exists to authorize execution. Removal needs a different set
of conditions: authenticated identity, exact installed bytes, an unchanged
review, no open usage lease and no dependent composite application. `get()`
enforced the execution condition on an operation that never executes anything.

## Solution

`src/agentix/storage/maintenance.py`: the application branch of `_prepare` now
resolves the record through `InstalledApps.load_stale()`, which still verifies
identity, the exact source digest and the review digest, and omits only the
policy comparison. The usage-lease and dependency checks are unchanged, and
`confirm()` recomputes the whole removal under the cross-process catalog lock, so
a stale confirmation still cannot delete changed content.

The execution gate is untouched: `get()` still refuses a stale policy, so a
stale application cannot be launched, and `reverify_app` remains the only path
that reseals a policy binding.

## Evidence

- `tests/test_catalog_maintenance.py`: an application whose policy no longer
  matches is prepared and permanently removed, including its review directory,
  while `get()` still rejects it; an application whose source changed after
  installation is still refused with `Installed application source changed`.
- `tests/test_maintenance_owners.py`, `tests/test_installed_apps.py` and
  `tests/test_catalog_maintenance.py`: 45 passed.
- Offline suite: `1018 passed, 83 deselected` in 671.63s.
- Ruff lint and format pass on the two touched files and
  `tools/build_reference.py --check` reports no issues.

No live model run, browser check or process restart was performed. The owner
confirmed separately that `Re-verify selected app` followed by deletion already
worked before this change; that path is unchanged.
