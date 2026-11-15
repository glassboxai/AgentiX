# V7-048: reviewed installed application updates

## Approved scope and observable acceptance

Recover Simply app, Another simple application and Application calculator in v7.
Update only the maintained schema-3 app.py in the two schema-3 packages, their
manifest hashes and authenticated reviews/dependency bindings. Preserve generated
logic, widgets, tool code/tests, application independent payload/expected cases,
identities, names and exact stored position bytes. Four-tool workshop is excluded
while random_number_draw is absent. Do not change v6 or restart existing instances.

Activation requires current package validation, authenticated original provenance,
current exact dependency bytes/grants and fresh native/browser host comparisons.
Any mismatch or busy/conflicting installed approval must remain blocked. Preserve
original installed bytes in a per-operation backup before ordinary replacement.

## Incident and implementation

V7-047 intentionally refused old maintained template bytes and stale case-binding
metadata. The operator approved this separate package-update block after receiving
the exact differences. src/agentix/storage/application_update.py composes the
existing migration snapshot reader and current tool validation; it does not alter
policy fingerprints or the execution boundary. tools/update_applications.py is the
explicit local operator command, with no model or file auto-approval switch.

A protected source record must bind the exact old executable identity and review.
Current manifest closure, paths, file sizes, hard links and aliases are checked.
Only a new maintained app.py may replace executable bytes, only for schema 3.
Every other runtime member must already satisfy current validation. Dependency
code, schema and reviewed tool tests must remain identical to current approved
bytes; only the case-contract binding may refresh. Current independent application
cases remain equal as JSON data, never inferred or repaired from observed outputs.

Read-only plans expose candidate and review hashes and bind every observed input
and maintained policy. Apply requires the exact reviewed digest. Complete copies
are staged; ApplicationSupervisor runs native and browser gates on those copies.
No installed writes occur on a failed gate or changed staging snapshot. The target
catalog lock and repeated input checks cover normal concurrent mutations. Existing
current grants are retained, never overwritten. Only already approved matching
widgets skip their old provisional test suites; differing widgets receive the
normal current checks. Provisional test reports are not acceptance evidence.

After verification, original package/review/source-record bytes are backed up.
Only changed maintained files and review metadata are written; the new protected
application approval is created exclusively and last. Ordinary write failures
restore affected installed bytes, including a partially written review. Crash-
atomic multi-file replacement and hostile same-user filesystem races remain
outside this block; invalid/partial grants cannot approve mismatched package bytes.

## Regression and verification

Tests are in tests/test_application_update.py and use only authored temporary
fixtures with explicit protection and verifier doubles. Seven initial tests failed
because the updater was absent; after implementation all passed. An additional
partial-review-write regression failed before tracking attempted writes for
rollback and passed after that correction. Source fixtures simulate an old signed
maintained template without deleting production code or weakening current policy.

Checks cover selective runtime update, exact layout/logic/source preservation,
changed generated code, changed cases/reviews, unauthorized runtime drift, missing
dependencies, stale plans, failed verifier, staging drift, idempotency and partial
write recovery. Actual catalog operations are separate from regression fixtures.
Final offline, Ruff, reference and actual native/browser results follow below.
No report model is used; prose is manually checked against raw evidence.

## Final software checks

The offline suite passed 859 tests, with 88 opt-in tests deselected and 18 existing
CrewAI deprecation warnings. Ruff lint/format passed for all 329 maintained Python
files; exact source-reference freshness passed. References were reviewed for
snapshot lifetime, selective changes, preserved cases and rollback semantics.
These checks use authored fixtures and do not establish real native behavior.

The first real operation retained two failures from native startup and activated
Application calculator only after fresh native/browser comparison. A targeted
follow-up uses the same candidate/review hashes for the other two apps, with safe
host phase diagnostics; neither startup limits nor expected results are changed.
A readiness failure is not relabeled as a passed acceptance case. Operational
results and any unresolved failure are recorded below after those gates finish.
