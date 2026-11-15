# V7-047: reviewed catalog relocation

## Approved requirement and acceptance

Relocate unchanged tools/widgets and independently reviewed applications into v7
without models, regeneration, edits to v6, grant overwrites or live restarts.
Retain current v7 approvals and explicit removals. Authenticate original records,
recheck exact bytes, reject Windows aliases/hard links, bound reads and record
backups and per-entry outcomes. Applications become visible only after current
package/dependency validation and fresh native/browser host comparisons. Unusable
entries remain blocked with a specific reason, never an updated hash alone.

## Incident and design

V7-COPY-001 copied files but left root-bound approval namespaces at the old path.
WidgetStore correctly rejected conventional widget files without destination
metadata. The GUI reported a generic ValueError after planning MasSimple.

The migration service reads explicit authenticated source records. Tools use the
existing approval validator in disposable metadata storage, so its revoke-on-error
behavior cannot mutate either real catalog. Valid destination tool grants win.
Unchanged widgets require matching code, CSS, tests, tool bytes and policy. A
changed reviewed-case digest additionally requires every current approved value
case to pass native/browser checks. Reviewed exception cases are additionally
compared with exact exception types on the host through WindowsSandbox. Child
inputs never include expected results. Typed browser controls exercise value
cases; an invalid Python input type is not silently forced through a text widget.
No model, generated host import, host execution fallback or file auto-approval
switch is used. Existing protected human cases remain the acceptance authority;
expected values are neither inferred from code nor sent to the child.

The read-only plan digest binds observed files, missing destination records and
maintained policies. Apply requires that exact digest, acquires the destination
catalog lock, saves original authenticated records and rechecks before exclusive
new-record writes. An injected verifier supports offline tests; the CLI composes
only the actual ApplicationSupervisor native/browser boundary. Verification does
not replace explicit review: apply is an operator action on an exact reviewed
migration plan and previously authenticated human-reviewed cases.

The service never rewrites application runtime templates, generated logic, cases,
existing grants, names or layouts. Stale maintained template bytes, missing tools
and changed dependency contracts are migration blockers. Updating such packages
requires a separate exact-artifact review; migration cannot silently repair them.
The operation is not a crash-atomic multi-file transaction. Partial progress is
recorded per entry; a retry starts with a newly reviewed plan. An operational
verification rejection never triggers model repair or automatic retry.

## Files and verification

Implementation: src/agentix/storage/catalog_migration.py. Operator command:
tools/migrate_catalog.py. Tests: tests/test_catalog_migration.py, using independent
temporary fixtures. No source in generated_tools is inspected or executed.

Use the managed interpreter with the three explicit absolute path arguments
--source-home, --source-tools and --target-home. With no --review-digest the command
prints a read-only plan. After review, supply its exact --review-digest to apply.
Set AGENTIX_PLAYWRIGHT_EXECUTABLE to an installed compatible Chromium browser.
Exit status 2 means blocked entries remain; individual successful entries are
retained with backups and a receipt under the destination migrations directory.

Initial red: nine tests failed because the approved migration service was absent.
After implementation thirteen offline tests passed, covering integrity, policy
drift, authenticated records, stale review, changed case digests, verifier-time
edits, conflicts, hard links, source immutability and application gating. The first
native fixture correctly rejected its zero-test placeholder; the fixture now
contains an independently authored interface test. Final raw results follow.

All report prose is manually authored from evidence; no model drafted this note.

## Final software checks (2026-10-30)

The final offline run passed 851 tests (88 opt-in tests deselected), with 18
existing CrewAI deprecation warnings. Ruff lint and format verification passed
for all 326 maintained Python files; exact source-reference freshness passed.
One real native/browser fixture passed with an authored widget and an executed
provisional interface test; provisional success was followed by independent native
and browser value comparison. This fixture does not establish model quality.

Additional adversarial red/green regressions cover exceptions from the verifier,
precise native exception types and empty conflicting destination records. A failed
first freshness run was caused by editing a test during that run, then resolved
by regeneration and the final full offline run. No assertion was weakened.

The real relocation uses protected existing human-reviewed tool cases. The first
operation moved the vowel widget and explicitly blocked the two widgets whose
cases included exceptions, rather than discarding those cases. A new explicit
plan then retained that grant and checked the remaining widgets, including exact
native exception observations. Operational receipts remain under runtime-data,
separate from regression fixtures and historical baseline/fix hashes.

## Operational result and unresolved applications

All three present destination tools retained their newer valid grants. Their three
widgets now load as approved through the actual WidgetStore with Windows DPAPI.
Across the widgets, all twelve currently reviewed cases passed: nine value cases
were compared through native application execution and actual browser callbacks;
three exception cases were compared natively against their exact reviewed types.
Provisional widget unittests remained supplemental, not the acceptance oracle.
No model inference or live restart was performed. SHA-256 inventory checks against
the copy receipt confirm unchanged source tools, applications, grants and reviews.

The first receipt is runtime-data/migrations/6a831168d2954f919ac3465cfdc1dadf/receipt.json.
The final receipt is runtime-data/migrations/66439dfb3ba14ff791b826d6931574d7/receipt.json.
Detailed final loader/source checks are in runtime-data/migration-verification-047.json.

The application review is complete, but activation is not: Simply app and Another
simple application still contain the older maintained schema-3 app.py; all three
present tools also have newer reviewed-case digests. Application calculator has
only the dependency-review mismatch. Four-tool workshop additionally requires the
removed random_number_draw tool, which was not resurrected. Exact field/hash
comparisons are retained in runtime-data/application-review-047.json.

No existing application package, manifest, review or application approval was
rewritten by this block. A separate approved package-update block is required to
replace the two old maintained app.py templates, synchronize manifests/reviews and
current dependency bindings for the three eligible apps, preserve generated logic,
expected cases and layouts, and pass new native/browser gates before activation.
Four-tool workshop remains blocked while its required tool is absent.

### New implementation hashes

These hashes identify maintained migration implementation/test bytes, not old
baseline/fix identities or newly approved application packages.

- src/agentix/storage/catalog_migration.py: 0af39f16301ef5b5d84170cc5e24f66e3c585a048e8ec201f20987505658b6b0
- tools/migrate_catalog.py: 13381bf6ff0ad43f15beb9f35fca813564a36e863cd625e7cbf302e00ac493fb
- tests/test_catalog_migration.py: 268252831b1cec68f54a878aafe05a545d34a9e0ce1fee29e593b6dcae36e4d5
