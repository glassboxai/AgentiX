# V7-056: stale installed-application re-approval

## Observed defect

After an installed application was published, a maintained host source changed.
On the next launch `InstalledApps.get()` raised `Application approval is stale`,
`InstalledApps.list()` dropped the record, and the catalog showed only the
remaining application. Each refresh emitted one `event=installed_app_rejected`
warning without any application identity, twice per refresh because
`refresh_apps` is bound to both `refresh.click` and `workspace["status"].change`.

Cause: `app_policy()` binds 24 maintained sources plus `infra/runtime.lock.txt`
into the protected record, and `get()` compares that fingerprint on every read.
The package bytes were unchanged (`application_digest` matched the sealed
digest); only the host fingerprint moved. The record was therefore
indistinguishable from a tampered one and was hidden instead of being offered
for re-approval.

## Second defect: dependency drift blocked both actions

Reported after the first delivery: `Re-verify selected app` returned
`Re-verification failed (ValueError)` and `Load selected app` returned
`Application load failed (ValueError)` for the same record.

Cause: `check_dependencies()` compares five fields, including
`contract_digest`. The two tools `calculator` and `count_vowels` had been
re-approved after the application was installed, so their protected approval
digest moved (`dede4676…` → `06751dd7…`, `5be5ad69…` → `aa664fa4…`) while their
code and test bytes stayed identical. The record was therefore stale for two
independent reasons, and the dependency check ran before any re-approval path
existed, so both actions aborted with an opaque `ValueError`.

Solution: `rebind_dependencies()` re-derives only the digest fields when the
role, `tool_name` and `function` are unchanged. A renamed tool or a changed
function identity still requires a new review. `load_app` uses the rebinding to
open the record for re-approval and reports which binding moved; `reverify_app`
refuses with an actionable message instead of a bare failure, because a moved
contract needs human review. The rebound digests are stored on publication, so
the resealed record matches the tools it was verified against.

## Third defect: stale guidance stayed visible after success

Reported after the second delivery: after a successful re-approval or
re-verification the panel still showed `Re-approval required: Application
approval is stale` and `Use Load selected app to review it again, or Re-verify
selected app to repeat the independent gates on the installed bytes`.

Cause: the description markdown was bound only to `choice.change`. The approve
and re-verify streams repaint the status and the dropdown through
`workspace["status"].change`, but that binding returned only the dropdown and
the session token, so the description kept its previous value.

Solution: `catalog_view()` builds the dropdown update and the description from
one protected listing, and both `refresh.click` and `workspace["status"].change`
now write the description. `describe_app` also degrades to an actionable
message when the dependency check fails instead of raising inside a refresh.

## Fourth defect: maintained-runtime drift reported as changed source

Reported after the third delivery: `Re-verify selected app` returned
`Re-verification failed (ValueError)` and `Load selected app` returned
`Application load failed (ValueError)` for `MultiplyAll2`, while the catalog
labelled both records `source_changed`.

Cause: `general_package.capture()` compares every `CODE_SHARED` member with the
current maintained template. `templates/code/application_context.py` changed one
docstring word after the packages were published, so the installed copy no
longer matched. `installed_apps._validated()` wrapped every `ValueError` from
`application_digest()` into `CHANGED_SOURCE`, so host drift and tampered
application bytes produced the same status and the same log detail. The stored
digest still matched the installed bytes, so nothing in the application itself
had changed.

Solution: `capture()` raises the typed `RuntimeSourceChanged(ValueError)` for a
moved maintained runtime member. `_source_digest()` maps it to the distinct
`CHANGED_RUNTIME` reason and `runtime_changed` status, and is used by
`_validated()`, `_reseal()` and `_reseal_candidate()`. The exception remains a
`ValueError`, so every bounded rejection path keeps its previous behaviour.

## Fifth defect: the frozen record discriminator looked like a stale version

`PURPOSE` still reads `AgentiX/v5/installed-app/v1` in a v7 product, and two
storage modules repeated that literal instead of importing it. The value is a
sealed-record discriminator, not a release marker: it is written into every
protected application record and rechecked on each read, so renaming it would
invalidate every installed approval. The `v5` segment is therefore frozen and
independent of the retired `agentix/v5` data namespace that
`storage.locations` rejects.

Solution: the constant documents that contract, and `application_update` and
`catalog_migration` import `PURPOSE` instead of duplicating the literal. No
record, digest or policy fingerprint changes.

## Sixth defect: runtime drift blocked the review panel entirely

Reported after the fifth delivery: `Load selected app` showed the loading status
and then `Application load failed (ValueError).` with an empty review panel, so
the owner could not review or re-approve anything.

Cause: `load_app` resolved the record with `load_stale()`, which recomputes the
installed digest with `capture()` and therefore rejects a drifted maintained
runtime member before any draft, snapshot or review panel exists.

Solution: `capture_with_current_runtime()` captures the installed package and
replaces only drifted `CODE_SHARED` members with the current maintained bytes,
keeping every application-owned member at its exact installed bytes and still
checking it against the manifest. `InstalledApps.load_for_runtime_refresh()`
accepts that drift only when the reason is `CHANGED_RUNTIME`; changed source,
changed review and invalid identity are refused as before.
`approve_application(..., allow_runtime_drift=True)` returns the refreshed
snapshot with its own digest, and `load_app` and its `recheck` use both, so the
panel is populated and the candidate stays unapproved and unverified until an
explicit human approval repeats the independent gates. The refreshed snapshot
never equals the sealed digest, so no record can be resealed from it.

## Seventh defect: layout read re-validated the drifted runtime

After the sixth delivery the panel still failed: `Load selected app` returned
`Application load failed (ValueError).` with an empty review panel.

Cause: `load_app` restored the draft and then called `library.read_layout()`,
which re-validates the record through `_validated(require_policy=False)` without
the runtime-drift allowance. The refresh path therefore succeeded and the very
next call rejected the same package.

Solution: `read_layout()` and `layout_controls()` accept
`allow_runtime_drift`, and `load_app` passes it only for the refreshed path.
The strict default is unchanged, so every other caller keeps rejecting drift.

## Eighth defect: approval rejected the refreshed candidate digest

After the seventh delivery the owner could load and review the restored code, but
`Approve and verify` answered `Review and explicitly approve the displayed
candidate. Changed or stale artifacts require a new review.` and stopped.

Cause: `load_app` kept the installed digest as `candidate.digest` while the
draft held the refreshed runtime bytes, so `ApplicationSupervisor.approve()` and
`InstalledApps._publish()` re-captured the draft strictly and rejected it. The
refreshed snapshot was also internally inconsistent: replacing a `CODE_SHARED`
member left the manifest hash of that member stale, so no strict capture could
ever accept the refreshed bytes.

Solution: `capture_with_current_runtime()` rewrites the manifest hashes of the
replaced members, `Candidate.runtime_refresh` carries the explicit refresh
decision, `load_app` stores the refreshed snapshot digest, and both approval
sites pass `allow_runtime_drift` only for that candidate. `_reseal_candidate()`
verifies the installed package still matches the refreshed digest, writes the
replaced runtime members and the updated manifest, then reseals the new digest
with the current policy.

## Ninth defect: saving acceptance cases dropped the installed identity

After the eighth delivery the owner could approve, and the independent gates ran,
but publication failed with `An application with this name already exists`.

Cause: `ApplicationReview.save()` cleared `catalog_id` when the acceptance cases
were saved, so `_publish()` no longer recognised an installed record and tried to
create a second install folder for the same display name. The identity rotation
is still required to force a fresh review, but the catalog binding must survive.

Solution: `save()` rotates only `identity` and keeps `catalog_id`, so a
re-approval reseals the existing record. A new application still starts with an
empty `catalog_id`, so its publication path is unchanged.

## Tenth defect: the load status did not say when to press Play

After the ninth delivery the owner asked what `Play selected app` is for, because
`Load selected app` answered `Use Play or Run data operation; previous tests are
not repeated.` without naming the button or the moment.

Solution: the status now reads `Review the restored code here; press Play selected
app to start it in the sandbox, or Run data operation to call it without opening
its interface. Previous tests are not repeated.` Behaviour is unchanged: loading
still starts nothing. The existing load regression asserts the exact sentence.

## Requirements

1. A record whose policy is stale stays visible in the Installed applications
   dropdown, labelled `(re-approval required)`, with its bounded reason.
2. Loading such a record restores the exact installed bytes and the stored
   review, marks the candidate unapproved and unverified, and requests a new
   explicit human approval. The existing review, approval and independent
   native/browser gates are reused unchanged.
3. Publishing a re-approved candidate replaces the existing protected record
   atomically instead of creating a second install folder.
4. Re-verification without a new code review re-runs the independent gates on
   the installed bytes and reseals only after they pass.
5. Rejection warnings name the application by opaque id and bounded display
   name, and one summary event reports the totals per listing.
6. No partial record may survive a crash: record and review writes use a
   temporary file plus `os.replace`.

## Design

- `InstalledApps.entries()` returns `CatalogEntry(id, name, status, reason, app)`
  for every managed record. `list()` keeps returning only authorized apps and
  is now a projection of `entries()`.
- Statuses: `valid`, `approval_stale`, `source_changed`, `runtime_changed`,
  `review_changed`, `unavailable`. Source bytes are checked before the policy so
  a tampered package is never reported as merely stale. A maintained runtime
  member that moved is reported apart from changed application source.
- `InstalledApps.load_stale()` validates identity, review and source bytes but
  not the policy fingerprint. `read_layout()` and `layout_controls()` use the
  same relaxed read because layout is bounded presentation data.
- `InstalledApps.reseal()` replaces only the policy binding under
  `CatalogLock`; `_reseal_candidate()` additionally rewrites the review and its
  hash after the candidate passed the current gates.
- `ApplicationsBackend.reverify_app()` repeats `supervisor.verify()` on the
  installed bytes and reseals only on success; a failure leaves the record
  stale and unapproved.
- `_write_bytes()`/`_write_record()` replace `path.write_bytes()` for records
  and reviews.

## Security constraints

- Re-sealing never authorizes changed source, a changed review or a different
  dependency closure; each is rechecked before the atomic replace.
- Re-verification is an explicit owner action, not an automatic startup grant,
  and it re-runs the real gates rather than reusing a previous result.
- Log lines carry an opaque id and a sanitized name; prompts, artifact bodies
  and secrets are never logged.

## Evidence

`tests/test_installed_apps.py` covers visibility, status classification, stale
load, atomic reseal, refusal of changed source, publish-time reseal, catalog
labelling, re-verification success/failure, the load-for-re-approval path,
dependency rebinding (load, reverify refusal and reseal with rebound digests),
the description clearing after reseal and re-verification, the shared
`catalog_view` refresh and the `status.change` binding arity. It also covers the
maintained-runtime drift status, its bounded reason and the stale load refusal.
Offline suite, Ruff and reference freshness were run after the change.

The reported failure was reproduced on a disposable copy of the real data
directory with the strict catalog registry: before the fix both actions aborted;
after it, `reverify_app` returns the re-approval guidance, `load_app` restores the
record for review, and approving it reseals the record as `valid` with the
current tool digests. The live 7880 process and the real records were not
modified.

The description refresh was verified in a real Chromium session against a
disposable Gradio app built with the production `build_apps_catalog` wiring: the
stale guidance was visible after selection and disappeared, together with the
`(re-approval required)` label, once the status reported success.
