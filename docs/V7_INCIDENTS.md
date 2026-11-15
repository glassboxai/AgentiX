# AgentiX v7 incident register

This register preserves V5 incident identifiers alongside V7 defects. Entries concern maintained sources or trusted temporary fixtures; an identifier's version prefix records its historical origin rather than the current document version.

| ID | Trigger / cause | Correction / evidence |
| --- | --- | --- |
| V7-ERR-005 | After V7-060 changed `storage/maintenance.py`, every installed application showed `(re-approval required)` again, because `app_policy()` hashed that removal service together with the execution boundary. The service never runs in the AppContainer child and only `controllers/catalog.py` imports it, so its edits invalidated approvals without affecting what executes. | `storage/maintenance.py` is removed from the `app_policy()` tuple and the docstring states the digest binds execution and runtime, not catalog services. Twenty-three files stay hashed, including every execution member; `get()` still refuses a stale policy and removal keeps its lock, lease, dependency and digest gates. `usage.py`, `catalog_lock.py`, `layout_contracts.py` and `application_editor.js` stay hashed because they participate in host validation. Regressions in `tests/test_installed_apps.py`. See [specification](specs/061-catalog-services-outside-policy.md). |
| V7-ERR-004 | `Delete selected application` returned `Application approval is stale` for every installed application after V7-059 changed `domain/application_code.py`, because `CatalogMaintenance._prepare` resolved the record through `InstalledApps.get()` and that call enforces the current host policy. Removal never executes the package, so the execution gate blocked an unrelated operation. | The application branch now uses `load_stale()`, which still verifies identity, exact source digest and review digest; usage-lease and dependency checks are unchanged and `confirm()` recomputes everything under the catalog lock. `get()` still refuses a stale policy, so stale applications remain unlaunchable. Regressions in `tests/test_catalog_maintenance.py`. See [specification](specs/060-stale-policy-removal.md). |
| V7-ERR-003 | The plan task emitted a public input schema with `minimum: 0` for `repeat_count`, derived from the approved `repeat_word_tool` contract ("Must be a non-negative integer"). `validate_input_shape` accepted only `type`, `description`, `enum` and `items`, so `validate_catalog` raised a generic `ValueError` and the controller reported only its type name; `SuperRepeater` failed three times after 84 to 89 seconds in `application_plan` without reaching widgets. | The plan prompt now lists the closed keys and forbids numeric bounds and other JSON Schema keywords; `ApplicationContractError` names the input and the sorted rejected keys without carrying the value; the controller propagates that closed text only. Regressions in `tests/test_code_application.py`, `tests/test_application_crews.py` and `tests/test_applications_backend.py`. See [specification](specs/059-closed-input-schema-diagnostics.md). |
| V7-ERR-002 | A fresh session accepted application candidates with no saved profile selected. `ensure_generation_identity()` raised an untyped `ValueError`, `_generate()` replaced it with the changed-digest text and `_safe_stream()` yielded it without logging, so the accept stream stopped silently while Tools kept working. | The precondition now raises the closed code `profile_not_selected`, each identity rejection shows its own message and logs `application_generate_rejected` with a bounded reason, and `demo.load` auto-selects the only saved profile for editing. The changed-digest refusal and the explicit reset are unchanged; no record, credential or digest was rewritten. Regressions in `tests/test_applications_backend.py` and `tests/unit/test_saved_model_profiles.py`. |
| V7-ERR-001 | `test_application_verbose_and_events_belong_to_the_owning_session` supplied `model_configuration=None`, so the production local-Ollama profile gate rejected the trusted fake before its session-routing assertions. | The fixture now supplies a local Ollama profile, stable trusted digest and no-op identity check. The focused test passes without a provider request; production gating is unchanged. |
| V5-ERR-001 | Relocation conversion applied the storage prefix twice; imports resolved to artifacts.catalog. | Corrected explicit imports and preserved same-module aliases. Four new identity regressions passed; initial failure retained in architecture-first. |
| V5-ERR-002 | Source encoding/newline transformations changed maintained template bytes. | Recompute the maintained template manifest after formatting; exact-byte checks retained. No generated approval was copied. |
| V5-ERR-003 | Some transformation helpers used Windows default decoding and corrupted Unicode punctuation. | Identified three affected files, backed them up and repaired only those files with explicit UTF-8 and compilation. A broad heuristic repair was rejected by automatic approval review and was not executed. |
| V5-ERR-004 | Packaged-host virtualization changes realpath without a reparse point. | Check reparse attributes separately, resolve physical root and pass AGENTIX_HOME from the managed launcher. Five new location regressions. |
| V5-ERR-005 | First named-app implementation omitted the protected folder field and reused a loop variable for the display name. | Separate filename variable and protected folder/name metadata. Eight new name regressions plus inherited catalog checks passed. |
| V5-ERR-006 | New CSS members were passed to Python compile. | Compile only .py members; validate CSS through its own scoped grammar before manifest acceptance. |
| V5-ERR-007 | Gradio field overflow clipped input/output edit grips. | Real native Playwright reproduced hidden overflow, then passed with visible controls, in-box grips and transparent borderless residual wrappers. |
| V5-ERR-008 | Group repeated the helper's DOM ID. | Use a Column with one ID. Real Playwright retained the strict unique-element assertion and passed after correction. |
| V5-ERR-009 | IaC Apply overlapped maintained source edits, making its source-bound plan stale. | Apply rejected as designed; stop source editing and generate a fresh plan. No bypass or relaxed source check. Final provisioning result recorded separately. |
| V5-ERR-010 | Legacy IaC doubles overrode LOCALAPPDATA while production now uses a stable root; an archive test observed a real cached path. | Inject the module's filesystem root inside the PowerShell fixture; keep real integrity/error assertions. Fifty targeted legacy contracts passed afterward. |

## Additional historical V5 verification findings

- V5-ERR-011: new CSS and cleanup dependencies were initially omitted from policy
  fingerprints. Three red regressions modified maintained temporary boundary
  files and demonstrated unchanged policy hashes. Include those modules and the
  location boundary; all three regressions now invalidate the approval binding.
- V5-ERR-012: an independently authored hard-link fixture demonstrated a widget
  CSS publication overwriting another temporary file. Resolve all three members
  before writes and reject aliases, non-files and multiple hard links. The exact
  red exploit is retained; companion/reuse regressions passed after correction.
- V5-ERR-013: the first environment fixture left an empty unowned v5 environment
  directory. Apply refused adoption. Verify the exact physical v5 path and its
  emptiness, remove it with rmdir only and provision using a fresh plan. No v4
  environment was copied, deleted or activated as the deployed v5 runtime.
- PowerShell 5's AST help-content interpretation rejected an inherited function
  comment in the static verifier. The established PowerShell 7 verifier passed
  all six files; this does not claim cross-version verifier compatibility.

## Remaining limitations

- Legacy unregistered AppContainer residues are preserved; v5 cannot establish that
  an old profile is inactive merely because AC/Temp is empty.
- Cleanup can be delayed by Windows locks or nonempty content; diagnostics and
  ownership records are retained instead of deleting unknown files.
- Application generation now uses approved canonical catalog contracts and a maintained
  compositor. Arbitrary third-party runtimes and dynamic LLM call trees are not implemented.
- Chat advice may be incorrect and prompt defenses are not an OS security boundary.
- Source/topic migration preserves compatibility aliases; it is not removal of
  every historical import path. The lab transport remains explicitly maintained.
  Superseded: the alias layer was retired intentionally, so legacy import paths
  are no longer supported; the lab transport statement still holds.
- Initial characterization used v4's interpreter as a read-only test runner, not
  the deployed v5 environment. Final evidence must identify its actual interpreter.

## V5-038 findings and corrections

- V5-ERR-014: concatenating member names and contents made different removal
  snapshots ambiguous. A red collision fixture reproduced it. Versioned,
  length-framed names, kinds, sizes and bytes now bind exact package content.
- V5-ERR-015: lock release errors could skip closing the lock handle. The failing
  release regression now passes with handle cleanup in a nested finally block.
- V5-ERR-016: copying a protected installed-app record into another library could
  authorize it there because its payload omitted the root. A cross-root replay
  regression failed before adding and checking the protected canonical root.
- V5-ERR-017: the first repair browser fixture called an API that does not exist.
  Correct the trusted fixture to compile_and_save_code_tool; preserve production
  behavior. The deletion scenario had already passed in that same run.
- V5-ERR-018: the native repair browser submitted another query after acceptance
  became verified but before sample execution finished. Keep the result assertion
  and wait for the full operation to finish; the real native/browser run now passes.
  Repair completion also uses the ordinary host-observed result envelope rather
  than displaying the internal approval digest to the user.
- V5-ERR-019: the repair acceptance prompt proposed an exception field inconsistent
  with the maintained schema. It now requests expect.type. The native browser
  regression checks invalid string and boolean cases alongside normal/zero/negative
  values. This validates protocol handling with a synthetic model, not the model's
  ability to propose correct cases unaided.
- V5-ERR-020: legacy browser fixtures omitted the new required application name and
  assumed the old config.json nesting. Update fixtures to the new user-visible
  contract. Test servers now pin AGENTIX_HOME to their temporary directory, so new
  synthetic widget approval records cannot enter the managed user's v5 store.

All browser servers are disposable; v4 is not restarted. Raw red and green reports
are retained under docs/reports/v5-038-*. Earlier v3/v4 evidence is historical.

- V5-ERR-021: the manual live smoke waited for networkidle and timed out despite a running Gradio page. Use DOM readiness plus explicit visible Tools/Applications/deletion-control assertions. Playwright then observed HTTP 200 and captured the live screenshot without changing application behavior.


## V5-039 findings (verification recorded in the delivery report)
- V5-ERR-022: the first full compatibility run overlapped source/manifests under active development and used a strict-contract flag on the shared legacy facade. Preserve that red report; synchronize maintained sample hashes and set strict mode only on owner instances. A fresh suite is required before completion.
- V5-ERR-023: initial activity border removal stripped Python indentation and allowed nested Markdown fences to break presentation. Failing indentation/markup regressions now use frame-only removal and escaped pre markup. Raw diagnostics are preserved.
- V5-ERR-024: parameter control IDs could collide across underscore-containing scopes. The failing semantic-ID regression now uses centrally registered parameter roles and globally unique allocation, retaining rejection of unregistered legacy roles.
- V5-ERR-025: real GUI review exposed duplicate authorization Group IDs. Use a Column; the final browser regression must assert uniqueness without selecting an arbitrary first duplicate.
- LIVE-039-01: the real model's calculator specification omitted Annotated metadata. Human review supplied the required interface contract before code generation.
- LIVE-039-02: generated calculator code used NaN equality and failed to validate operation type before set membership. Human review corrected finite checks and invalid operation handling; the corresponding nonfinite/overflow/unhashable-operation regressions are in the reviewed 21-test suite. Twelve host-compared acceptance cases passed and real GUI execution returned 102.0 for 17 multiplied by 6.
- LIVE-039-03: proposed exception cases used kind error/exception/message rather than raises/type. Human review corrected the JSON schema and checked expected arithmetic independently; no parser assertions were weakened.


- V5-ERR-026: owner coordinators are per-session subclasses, not instances. An instance/type check accidentally skipped new strict gates. A failing real-composition regression now verifies strict Annotated checks and router activation on the actual owned coordinator while preserving the separate legacy facade.
- V5-ERR-027: the real manager chose basic_calculator for a vowel-count request and started unrelated verification. Human review rejected it. Production now selects from typed catalog metadata with no callable tools, then exposes only the selected verified API to execution. A live structured retry correctly requested count_english_vowels instead of reviewing arithmetic.
- V5-ERR-028: an unstructured creation route included nonempty invocation arguments. It was rejected before writing or execution. The installed CrewAI client supports response_model; a Pydantic discriminated creation/reuse grammar now requires empty creation arguments without relaxing the host check.
- LIVE-039-04: the proposed vowel specification contradicted itself about rejecting ASCII-external text and returning zero for None. Human review made Unicode acceptance and strict non-string errors explicit, retaining ASCII vowel membership and adding Unicode regression cases.
- LIVE-039-05: the proposed vowel acceptance JSON embedded Python multiplication as a value. It was never evaluated. Human review kept literal finite cases and left the exact 16000/16001 boundary in the reviewed native unittest module.


## V5-039 live findings (finite verification completed)

The real-model run uses a disposable GUI on 7879 and new temporary tool storage.
The user instances on 7877 and 7878 are preserved. These observations are not a
claim that the four-tool application has passed acceptance.

- LIVE-039-06: proposed word-count tests expected five tokens for a six-token
  sentence, and labelled a 32,000-character expression as 16,000 characters.
  The human reviewer corrected the oracle and asserted actual boundary lengths.
- LIVE-039-07: proposed seeded-random acceptance invented a sequence. An independent
  standard-library reference established [6, 3, 7, 1, 2, 9] for seed 7 and six
  inclusive draws from 1 through 10. The tool implementation needed no algorithm
  change; reviewed tests also check unchanged global random state.
- LIVE-039-08: five-minute human-review expiry cancelled a pending random-tool
  review. Expired evidence was not treated as approval. A new operation must obtain
  current explicit review; no timeout bypass or automatic approval was introduced.
- ERR-039-09: conservative reuse classification rejected an unused comprehension
  target named underscore. A regression now permits underscore Store context only;
  underscore reads and private introspection remain denied. Literal boolean
  contracts are distinguished from integers; heterogeneous Literal types fail closed.
- ERR-039-10: text-mode writes changed proposed widget bytes on Windows. Widget,
  tests and CSS now preserve exact UTF-8 bytes. First publication rebinds the
  expected approved widget record after checking its exact source/CSS; subsequent
  unexpected changes still fail closed. Regressions cover both cases.
- ERR-039-11: generic review needed one physical widget-test entry rather than a
  duplicate virtual entry. Saving that editor updates both proposal and file bytes,
  manifest hash and candidate identity, invalidating previous review.
- ERR-039-12: composite-result frontend returned five updates for six outputs.
  A real Gradio callback regression verifies the corrected arity and hides legacy
  word/vowel controls for generic applications. Layout controls now derive from
  the validated graph rather than fixed word/vowel names.

Approval fingerprints include host policy. Revalidation after an engineering
policy change is intentional; it does not demonstrate normal unchanged-tool
reuse. The latter must be checked after the final host policy is frozen.

### ERR-039-13: malformed acceptance stopped before review

A real revalidation proposal contained NaN. The read-only model adapter applied
transport JSON validation before the acceptance service could display the proposal,
so the reviewer saw only a failure. A red regression reproduced this. The adapter
now returns bounded acceptance proposal text to the existing mandatory review
service, which marks invalid JSON and requires valid edited cases before native
evaluation. Tool-routing responses remain strictly parsed; their malformed JSON
still fails before selection/execution. Ten routing regressions pass after the fix.
The acceptance prompt additionally requests at most eight concise finite-JSON cases.
This is not an authorization or JSON-validation bypass.

### ERR-039-14: bounded model timeout during revalidation

The real random-tool proposer exceeded its unchanged 120-second request limit.
Its 15 provisional unittest methods had passed, but no acceptance or execution
was granted from the incomplete response. The proposal prompt now requests at
most four concise cases, allowing the reviewer to add more. A provider failure
returns deliberately invalid explanatory review text, not invented cases. The
acceptance service requires the owner to enter a valid contract and approve it
before evaluation. A regression fails before this change and all eleven routing
checks pass afterwards; no automatic retry is introduced. Current calculator and
counter approvals survive this adapter-only change because host security policy
and approved artifact bytes remain unchanged.

### ERR-039-15: real widget proposals used incompatible Gradio interfaces

The first complete four-tool proposal selected the correct actual catalog tools,
but its widgets treated the injected api_name string as a function. Two counters
returned a Group rather than the required references. Proposed tests used invented
Button.fn, gr.Context and Blocks.test_api interfaces. Random inputs also rounded
and truncated fractions, and random tests checked formatting without invoking a
callback. These original bytes were inspected in the GUI and retained unchanged
as evidence. An explicit negative verification failed, closed its native session
and did not install the application.

The maintained designer now receives a typed context contract (api_name is a
non-callable string; elem_id is callable), explicit return/error/integer/table
constraints and the actual test-framework API vocabulary. No reference widget
implementation is supplied. Tests reproduce the missing contract before correction.
A second real-model GUI generation uses the same plain user request; its outcome
must be recorded separately from the failed first proposal and prepared human edits.

### ERR-039-16: independent browser adapter assumed every scalar used a textbox

The calculator model correctly chose a Radio control. The maintained browser
adapter tried to fill it as text. An independent real-Chromium radio regression
failed before correction and passes after selecting the exact labelled option.
This fixture proves the radio adapter, not the four-widget application by itself.

### ERR-039-17: failed provisional widget-test reports were discarded

The native gate previously raised a generic RuntimeError and lost the bounded
child report. WidgetTestsFailed now carries bounded private diagnostics, while
its public message stays generic. General verification saves the report beside
its candidate on failure. Native exit and timeout observations remain separate
from the untrusted report; an empty/failed child suite still cannot pass. A
failure-session double reproduces the missing diagnostic before the correction.

### ERR-039-18: widget-only edits rewrote approved CRLF tool bytes

On 2026-10-30, a trusted CRLF regression reproduced the grouped editor writing
normalized LF tool source even when the displayed tool code was unchanged. Save
now writes tool implementation bytes only when its displayed content actually
changes. Widget/test edits still invalidate application review. The regression
verifies exact original bytes and absence of pending tool revisions after a
widget-only edit; all seven focused offline application tests pass. No installed
user tool was modified to reproduce or correct this issue.

### ERR-039-19: repeated zero values did not prove fresh GUI execution

The four-widget browser check passed a prior visible zero before the new callback
finished. Gradio's default once-trigger then suppressed a rapid following click.
A real authored Gradio regression reproduced the failure. Verification now waits
for a fresh queue event acknowledgement and its completed status-tracker state
before comparing the output. Gradio uses a hide class rather than removing the
tracker; the first visibility-based correction was rejected by the regression.
The corrected regression verifies five distinct completed events and exact values.
Two browser adapter regressions pass; ten emitted warnings are third-party pandas
queueing deprecations from these fixture calls.

The already generated and GUI-edited proposal is retained. A fresh maintained
supervisor process requires a new explicit terminal approval of its exact digest,
rechecks durable tool grants and reruns all native/browser gates. This is not a
new model generation, a model replay, an automatic approval or a host-execution
fallback. The user-visible 7879 process is preserved; corrected GUI code runs on
7880. Verification provenance distinguishes original GUI generation/review from
this explicit operational recovery.

### ERR-039-20: table assertion read Gradio's hidden sizing table

Fresh synchronization exposed another checker defect: the six-number table was
visible, but the CSS selector read one aria-hidden measurement cell. A real Gradio
fixture confirmed that actual values are role=gridcell elements in a virtual grid.
The retained independent expected sequence is unchanged. The regression includes
six values, 100 virtualized rows and an empty result; its correction and final
native/browser outcome must be recorded after execution.

The ERR-039-20 correction now checks the accessible grid's exact row/column count
and every expected value, scrolling the real virtual viewport for long tables.
All three real-browser adapter regressions pass, including six numbers, 100 rows
and zero rows. Expectations were not reduced to the first visible cell or count.
Seventeen warnings in this fixture batch originate in Gradio/pandas queueing and
compatibility code; they are not suppressed or interpreted as security evidence.

### V5-ERR-039-21: rapid Close/Play overlaps lifecycle polling (source fixed; live reload deferred)

A real rapid GUI close/reopen produced a Windows lease unlink PermissionError.
Native processes still closed and a new preview started, but polling may observe a
dead preview outside the controller lock while Open changes that same candidate
and lease. A deterministic two-thread regression failed before correction. The approved
solution runs the polling lifecycle check under the same owner controller lock as
opening/closing. The regression is now a normal passing test. The running 7880
instance retains its prior code because the user expressly declined a restart.
The ordinary four-tool execution, independent browser checks and saved geometry
passed; this issue concerns a rapid overlapping lifecycle transition.

On 2026-10-30 the user approved V5-ERR-039-21 correction but explicitly selected
"Correct without restarting 7880". Lifecycle polling now acquires the owner's
controller lock before observing/closing a preview. The strict xfail is removed
and the deterministic regression passes. This source correction is not loaded
in the already-running 7880 process; it will apply at the next authorized launch.
An initial verification command used a nonexistent singular backend test filename
and ran no tests; the correct plural backend test file was then selected. That
mistaken command is not counted as verification evidence.


### V5-ERR-041-01: workflow sources cannot express a requested composition

Trigger: the user requested an application chaining four approved tools and
observed missing output-to-input connections. Existing generated artifacts were
not inspected, so the exact live graph is not asserted here. Static investigation
found that bindings supported only separate manual ports and complete prior
results. There was no named shared source, fixed parameter or explicit array item.
Type/cycle validation also did not establish request semantics. Acceptance selected
the first compatible case greedily, missing valid combinations requiring earlier
choices to change.

Approved correction: extend the general data-only binding contract, validate types
and exclusive sources, resolve one canonical shared input and typed constants,
check array selection at runtime, and backtrack over independently reviewed cases
with a hard search bound. Explain requested dataflow in the assembler instructions
without naming particular tools. Review binds the graph and expected values;
human semantic review remains necessary. Preserve exact legacy runtime hashes.

Red evidence: the initial focused run had two failures (unsupported binding fields
and missing canonical shared payload), with ten invalid-binding cases passing.
After graph/payload correction those passed. Two new coherent-acceptance tests
then failed because the selection service was absent; both passed after its
implementation. Fixtures use unrelated measurement/sample/product functions and
repeated tools, not existing catalog artifacts. Verification is recorded in
reports/V5_041_WORKFLOW_BINDINGS.md. No inference or live restart is included.

During verification another open chat restored application_graph.py; the user
confirmed that chat was closed. The approved contract was reapplied, and affected
checks were repeated. This transient overlap is not a product defect.


### V5-ERR-041-02: integral float table presentation rejected

The new disposable native-browser graph returned the independently expected sample
[3.0], but Gradio displayed its cell as 3. The browser comparator required the text
3.0 and failed. The shared numeric-display comparator now accepts an omitted zero
fraction while anchoring the entire value, rejecting prefixes such as 30 and
nonmatching values such as 3.1. This also prevents the previous unanchored scalar
float regex from matching a numeric prefix. Expected data and cases are unchanged;
there is no rounding tolerance. The native-browser failure and two focused red
regressions preceded correction. Passing results are in the V5-041 record.


### V5-ERR-041-03: actual model transport adds absent binding fields

The supervised live run on the separate 7882 GUI timed out after 120 seconds
before producing a candidate. Investigation also reproduced a separate transport
defect: LocalModelClient serializes the validated response with model_dump, which
added input=null, value=null and index=null to bindings. Those added fields change
source presence and fail the second validation even for a correct model proposal.
Injected-client tests had skipped that boundary. The original provider schema
also permitted source mixtures which the host validator would reject.

Nine failing regressions captured model-dump round-trip corruption, permissive
provider grammar and the missing bounded timeout injection. The user approved
correction and a 600-second validation-only wait. Binding now serializes only
explicit fields and publishes five disjoint provider object shapes. LocalModelClient
accepts an injected 1â€“600 second wait with the unchanged 120-second default.
get_default_ui accepts an explicit application-client factory at its composition
root; the separately owned validation launcher uses 600 seconds. Thirty-five
focused transport/agent/binding checks pass. This does not itself establish live
model semantic correctness. No automatic retry or 7880 restart occurred.


Two subsequent supervised proposals returned within the transport limit but
invented a numeric placeholder for text and indexed scalar results. Both were
rejected before code execution. A problem-only clarification did not correct the
model. The approved provider-grammar correction was therefore completed with
catalog-derived tool/port variants and typed node prefixes. A shared compatibility
predicate now drives both grammar and host edge checks. Two additional failing
regressions preceded implementation; 46 focused checks pass, including an unrelated
string pipeline. No special handling for the user's four tool names was added.


### V5-ERR-042-01: application coordination duplicates framework responsibilities

The user identified that application creation used a direct Ollama transport and
increasingly complex provider-specific graph grammar while CrewAI already supplies
sequential task coordination and context. The user approved V5-042 to simplify
that boundary. Existing binding behavior and exact package bytes were characterized
by the graph/pipeline/reuse suite before refactoring.

Three initial coordination regressions failed before the adapter existed. The
new CrewAI adapter uses a plan/connect crew and a missing-widget crew with explicit
context and Pydantic outputs. Host validation and native execution stay separate.
The prefix generator was removed; its type-rejection cases now exercise the
unchanged authoritative host contract with readable IDs. Missing structured output
and failed kickoff stop without retry/approval; capacity is released for a new
explicit operation. A two-session regression preserves verbose and technical
activity ownership. Real CrewAI schema/context construction passed with only
kickoff inference replaced by authored outputs; this is not live-model evidence.

Fast tests use model/OS doubles. The user's AppContainer concern is addressed by
running expensive real native checks at closure, never by executing generated code
on the host. Final checks and real application outcome are recorded separately.


### V5-ERR-042-02: input placeholders survive CrewAI review; GUI hides the cause

Two user attempts on the CrewAI validation GUI returned a count_english_vowels
call named input_text and then supplied its integer result to the text parameters
of both counters. Host type validation correctly rejected both before package
creation or AppContainer execution. The GUI exposed only ValueError, preventing
the user from distinguishing invalid connections from isolation/transport errors.

The approved simple-call coordination contract now uses ApplicationSteps: each
argument explicitly names an input, a fixed value or a prior result. It translates
once to the existing persisted manifest. The integrator checks a call list rather
than recreating graph input nodes. ApplicationPlanError carries only validated
identifiers and static contract types to the GUI; arbitrary exception bodies remain
hidden. Six new failing regressions preceded correction. Forty-one focused tests
and actual CrewAI task/context construction with inference replaced pass.

A separate read-only runtime catalog check found four approved random value cases
but none covering one draw from 1 through 3. This is an independent acceptance-data
gap which must not be hidden by weakening expectations or changing approved tools.


### V5-ERR-043-01: simplified creation still depended on custom graphs

The Simply app experiment removed the random tool but still translated model call
lists to the custom graph. Scalar count results incorrectly indexed as arrays
failed before packaging, so that experiment did not isolate the requested graph-free
architecture. The user approved persisting generated Python connection code instead.

A version-3 package now stores run(payload, call), public input contracts and a
presentation-only widget inventory. It contains no workflow/order/bindings. Host
syntax checks never import it; the maintained native adapter validates and records
approved tool calls. The existing review editor supports code edits and independent
application cases, with exact-byte approval and revocation. Tool source/contracts
are unchanged. Legacy graph packages retain their own compatibility route.

Initial regression: five failures (missing code contract and graph-only packaging).
New regressions cover graph-free closure, source edits, pending independent cases,
strict input/output contracts, runtime tampering, dependent native calls and repeated
browser runs. Closure: offline 827, real frameworks 13, native positive/rejection fixtures and
repeated browser checks passed. Real qwen3-coder:30b Simply app passed native and
browser acceptance and was installed; a visible run produced 3, 2, 9 and 6. See
[verification](reports/V5_043_GENERATED_CONNECTION_CODE.md) for transient Windows
preparation failures, isolated repeats and the untested random-app limitation.


## V6-044: schema-3 widget layout

Fixed shared editable-ID discovery for connection-code widgets; Status and widget
controls now use the same existing editor handlers and bounded storage contract.
See [cause, acceptance and verification](specs/044-widget-layout.md).


## V6-045: independent acceptance proposals

Schema-3 drafts now propose bounded reviewed catalog cases through inert source
matching, retain unresolved expectations and open an editable JSON review. Invalid
cases produce persistent guidance before verification. Explicit review and native
comparison remain required. See [design, incident and verification](specs/045-proposed-acceptance-cases.md).


## V7-046: public input layout

Schema-3 public inputs are created inside the editable canvas and their declared
IDs join the shared layout allowlist. Existing callbacks, editor events, geometry
bounds and approval invalidation remain in force. See [scope, cause and checks](specs/046-public-input-layout.md).


## V7-047: reviewed catalog migration

Explicit catalog relocation authenticates prior grants, preserves current v7
approvals and requires fresh gates for changed case bindings and applications.
Stale packages remain blocked, without silent runtime edits or grant overwrites.
See [scope, design and evidence](specs/047-catalog-migration.md).


## V7-048: installed application update

The explicitly reviewed updater stages maintained-template and dependency-review
changes while preserving generated logic, independent application cases and layout.
Fresh native/browser gates precede backed-up installation; current grants and v6
remain untouched. See [scope and evidence](specs/048-installed-application-update.md).


## V7-049: actionable docstring contract and current Ollama pin

Tool creation runs failed with `CONTRACT_ERROR: Tool module requires an English
docstring` because the coder submitted code starting with imports and neither the
coder prompt nor the error stated that the module docstring must be the very first
statement. Cause, not a contract relaxation: the message and prompt were
unactionable, so the agent could not self-correct. The error now states the exact
placement and the coder prompt makes it explicit; a strict regression in
`tests/test_v5_tool_contracts.py` matches `module.*first statement`.

The managed IaC launchers also drifted: generated scripts still referenced the
old `D:\AI\AgentiX_v5` tree, and the reviewed Ollama pin `0.40.11` no longer
matched the installed and running `0.40.13`, so `LaunchGui` refused to start.
The reviewed pin was explicitly advanced to `0.40.13` in
`infra/windows.local.json`, `infra/Agentix.Iac.psm1` and
`docs/V5_INSTALLATION.md`, the adoption regression in `tests/unit/test_iac.py`
was updated to reject the old pin, and the launchers were regenerated through a
fresh Plan/Apply cycle. No process was restarted and no version was
auto-adopted.

## V7-ERR-050: Ollama upgrade prevents launch

Exact provisioning version equality was reused at launch. Upgrading Ollama produced
drift; changing the profile then hit the hard-coded allowed pin. V7-050 adds separate
API-based launch readiness while retaining strict provisioning, model integrity and
other prerequisite checks. See [requirements and evidence](specs/050-ollama-launch-compatibility.md).

## RAG-ERR-001: Chroma distance metadata compatibility
During RAG-001 development, copying legacy hnsw:space metadata into Collection.modify raised ValueError. The regression first failed during upsert. Configure cosine through Chroma's collection configuration instead; metadata then holds only schema/model/dimension. Persistence/reopen regressions pass.

## RAG-ERR-002: Placeholder stage timings
The real-model evaluation exposed zero placeholder durations for persistence, snapshot and ranking. A captured-log regression failed before correction. Start a monotonic timer for each stage and pass it to the completion event; the regression verifies measured positive durations. No query or artifact payloads are added to logs.

## RAG-ERR-003: Unnamed and duplicated retrieval policies
Review identified hard-coded bounds and ranking parameters in the initial RAG delivery. Keyword limits were duplicated across validation, JSON schema and prompt; BM25 encoded derived factors separately. RAG-008 introduces typed, documented policy constants and derives the factors. Existing behavior was characterized with independent boundary and score expectations before refactoring; those tests pass afterwards. This is a maintainability correction, with no claimed runtime defect or artificial failing test.

## RAG-ERR-004: Mutable catalog root could prune bound metadata
A regression redirected the injected ToolCatalog.root after binding. Membership checks then used a different root and incorrectly omitted the original entries. Reject root changes before scanning; the failing regression now passes and verifies that the original entry remains unchanged after restoring the root.

## RAG-ERR-005: Catalog reconciliation duration was not measured
The new reconciliation completion event initially used a zero placeholder duration. A stage-duration regression failed first. Measure reconciliation from its own monotonic start and pass the elapsed duration to diagnostics; the regression now passes.

## RAG-ERR-006: Selected dependencies changed legacy role keys
The first selection wrapper keyed dependencies by tool name and lost legacy adapter roles. A role-preservation regression failed. Keep the original registry keys while selecting by tool identity and exact source hash; subset and generation-boundary tests pass.

## RAG-ERR-007: Obsolete retrieval errors overwrote newer input
Successful obsolete searches were discarded, but old provider failures still surfaced after an edit. The failed-response revision test reproduced it. Check the current revision in both success and failure paths; superseded responses produce no UI update.

## RAG-ERR-008: Gradio Group duplicated the candidate panel ID
Actual Playwright DOM lookup found two elements with the new Group ID. Use a uniquely identified Column with the same visual boundary. The strict unique selector and below-delete geometry pass.

## RAG-ERR-009: Textbox input did not cover complete value replacements
The installed Gradio frontend dispatches input from its key handler, while change follows bound value updates. A complete replacement in the browser left old candidates enabled. Bind invalidation to query.change; edits/pastes now clear the preview without automatic inference.

## RAG-ERR-010: Candidate descriptions collapsed into names
Visual QA and DOM geometry showed inline name/description text. Global CSS did not style the isolated HTML content sufficiently. Load a maintained component-local CSS asset via css_template and explicitly lay out the blocks; the unchanged geometry assertion passes.

## RAG-ERR-011: Approval storage failure escaped candidate acceptance
A PermissionError crossed the callback without a maintained modal/error event. A failing regression captured it. Log only the safe exception type and return a bounded acceptance-unavailable ValueError; no generation starts and the sensitive body stays out of logs.

## RAG-ERR-012: Closed application owner retained an in-flight search revision
A simulated close during inference still returned a ready preview. Invalidate the revision during owner/candidate cleanup; the late-result test now returns no preview and cannot publish a new accepted scope.

## RAG-ERR-013: Revised-tool review reused the full registry
The legacy review completion path resolved all installed tools even for a candidate-scoped proposal; a regression with an unrelated tool failed at a manifest-role lookup. After successful tool revision publication, invalidate the candidate-bound proposal and require a new search/acceptance, preserving its draft evidence. The legacy non-candidate path remains intact.

## RAG-ERR-014: Ignored invalidation was logged as applied
An edit during generation correctly retained the original server context but logged candidate_invalidated unconditionally. A captured-log regression failed. Track whether invalidation actually occurred and emit candidate_invalidation_ignored for the busy/review case; the regression passes without changing generation context.

## RAG-ERR-015: candidate preview refreshed during description editing

Cause: the Textbox change callback cleared and invalidated the panel for every value change. User approved removing that callback while retaining exact-description validation on acceptance. Browser regression covers stable preview, rejected stale-description acceptance, checkbox reset, empty-selection gating and explicit generation consent.

RAG-011 verification initially found that the composition-test Gradio double lacked CheckboxGroup; its supported component inventory now includes the real control without changing existing assertions. A concurrent browser-test edit also made its generated reference stale; references were rebuilt before the final frozen-source suite.

## V7-ERR-054: invalid acceptance proposal reached generic approval failure

The review panel enabled Approve before the current acceptance JSON was checked,
so malformed function identifiers or cleared cases reached the backend and
returned a generic failure after approval. Reuse the maintained contract parser
in the UI readiness callback, bind it to edits and the current poll snapshot, and
keep backend validation unchanged. Focused tests cover valid, invalid, pending,
replaced and edited proposals.

## V7-ERR-062: the load status did not say when to press Play

`Load selected app` answered `Use Play or Run data operation; previous tests are
not repeated.`, which named neither the button nor the moment, so the owner could
not tell why the application was not displayed.

The status now reads `Review the restored code here; press Play selected app to
start it in the sandbox, or Run data operation to call it without opening its
interface. Previous tests are not repeated.` Loading still starts nothing, and
the load regression asserts the exact sentence.

## V7-ERR-061: saving acceptance cases dropped the installed identity

`ApplicationReview.save()` cleared `catalog_id` when acceptance cases were saved,
so `_publish()` no longer recognised an installed record and tried to create a
second install folder, failing with `An application with this name already
exists` after the independent gates had already passed.

`save()` now rotates only `identity` and keeps `catalog_id`, so a re-approval
reseals the existing record while a new application keeps its empty binding.

## V7-ERR-060: approval rejected the refreshed candidate digest

`load_app` kept the installed digest as `candidate.digest` while the draft held
the refreshed runtime bytes, so `ApplicationSupervisor.approve()` and
`_publish()` re-captured strictly and rejected it. The refreshed snapshot was
also inconsistent: replacing a `CODE_SHARED` member left that member's manifest
hash stale.

`capture_with_current_runtime()` now rewrites the replaced members' manifest
hashes, `Candidate.runtime_refresh` carries the decision, `load_app` stores the
refreshed digest, and both approval sites pass `allow_runtime_drift` only for
that candidate. `_reseal_candidate()` verifies the installed package against the
refreshed digest, writes the replaced runtime members and manifest, then reseals
the new digest with the current policy.

## V7-ERR-059: layout read re-validated the drifted runtime

`load_app` restored the draft and then called `library.read_layout()`, which
re-validates through `_validated(require_policy=False)` without the runtime-drift
allowance, so the refresh succeeded and the next call rejected the same package.

`read_layout()` and `layout_controls()` now accept `allow_runtime_drift`, and
`load_app` passes it only for the refreshed path. The strict default is
unchanged for every other caller.

## V7-ERR-058: runtime drift blocked the review panel entirely

`load_app` resolved the record with `load_stale()`, which recomputes the digest
with `capture()` and rejected a drifted maintained runtime member before any
draft, snapshot or review panel existed. The owner saw the loading status and
then `Application load failed (ValueError).` with nothing to review.

`capture_with_current_runtime()` replaces only drifted `CODE_SHARED` members,
`load_for_runtime_refresh()` accepts that drift only for `CHANGED_RUNTIME`, and
`approve_application(..., allow_runtime_drift=True)` returns the refreshed
snapshot with its own digest. The candidate stays unapproved and unverified
until an explicit approval repeats the independent gates, and the refreshed
snapshot never matches the sealed digest, so it cannot be resealed.

## V7-ERR-057: frozen record discriminator duplicated as a literal

`PURPOSE` reads `AgentiX/v5/installed-app/v1` in a v7 product, and
`application_update` and `catalog_migration` repeated that literal instead of
importing it. The value is a sealed-record discriminator rechecked on every
read, so renaming it would invalidate every installed approval; the `v5`
segment is frozen and unrelated to the retired `agentix/v5` data namespace.

The constant now documents that contract and both modules import it. No record,
digest or policy fingerprint changes.

## V7-ERR-056: maintained-runtime drift reported as changed application source

A maintained runtime member (`templates/code/application_context.py`) changed one
docstring word after two applications were published. `capture()` rejected the
installed copy, and `installed_apps` collapsed every digest failure into
`CHANGED_SOURCE`, so both actions failed with an opaque `ValueError` and the
catalog reported `source_changed` for unchanged application bytes.

`RuntimeSourceChanged(ValueError)` now names that drift, `_source_digest()` maps
it to `CHANGED_RUNTIME` and the `runtime_changed` status, and the three digest
call sites share it. The regression asserts the distinct status, the bounded
reason and the stale-load refusal. Re-publishing or resealing the two installed
records remains a separate human decision.

## V7-ERR-055: absent Playwright browser closed an otherwise reviewed proposal

The acceptance browser could be absent when the GUI was launched outside the
normal IaC convergence path. Playwright then failed after the user had clicked
approval, and the generic application failure closed the proposal even though
the failure was a host prerequisite rather than generated application behavior.

V7-055 adds a static host-owned requirement registry and pre-approval probe.
Only the owning pending review can show and explicitly invoke the initial
Playwright Chromium repair. The command is fixed to the active isolated Python,
inherits no package/proxy configuration, is post-verified and requires a new
approval click. Tests cover the missing gate, owner-bound install, rejected
unknown identifier, failed postcondition and scrubbed installer environment.

## V7-ERR-063: inline code rendered white on a light chip

Cause: the maintained palette set prose text to near-white but never defined
Gradio's `--code-background-fill` or `--panel-border-color`, so the installed
6.30.0 stylesheet kept the light defaults for `.md :not(pre) > code`. The
pending tool write confirmation (`File:`/`Action:`) and the installed-application
description (`Stored package:`) therefore showed white text on a white chip.

The stylesheet now defines both variables for the dark palette and an explicit
inline/pre rule inside `.gradio-container .prose`. `tests/test_ui_stylesheet.py`
asserts the variables and the rule; the real GUI reports computed colour
`rgb(241, 243, 245)` on background `rgb(16, 20, 27)` for the stored-package chip.

## V7-ERR-064: a blocked candidate acceptance failed silently

Cause: `refresh_controls` always rendered `Accept N selected tools and generate`
and only toggled `interactive`. When the checked subset contained a candidate
without a current reusable approval, `selected_expected` raised, the button
stayed disabled and the browser dispatched no click at all: no status change and
no dialog. A durable approval is required for applications, so a tool usable in
the Tools tab through its session grant can still be ineligible here.

`candidate_controls` now returns a short reason with the existing readiness flag
and `refresh_controls` appends it to the label, keeping the count and the
disabled state required by RAG-011-05. Unit and framework regressions assert the
ineligible, empty, unsearched and ready cases; the disposable browser run shows
`Accept 2 selected tools and generate - approve the selected tools in Tools
first` with zero dispatched clicks, and the eligible run keeps the plain label.

Generated artifacts cannot supply requirements or installation commands.

## V7-ERR-065: collapsed widget groups drew three horizontal rules

Cause: Gradio 6.30 renders `gr.Group` as `div.gr-group` with its own border and
`--block-background-fill`, not as the `.block` element the canvas palette
overrode. Once the editor positioned every control absolutely, each widget group
kept only its 2 px border and fill in normal flow, so three widgets produced
three light horizontal rules above the moved controls. The V5-037 wrapper rule
covered `.form` and `.styler` only.

`style.css` now adds `.application-layout-active .gr-group` to that rule, so the
collapsed wrapper keeps no border, shadow or background while a saved layout is
active. `tests/test_ui_stylesheet.py` asserts the selector and declarations;
`tests/test_v5_native_editor_browser.py` asserts on the real framework that every
canvas group reports `borderTopWidth: 0px` and a transparent background. The
regression failed before the rule and passed after it; a disposable loopback
fixture with the maintained stylesheet showed no thin full-width element left.

## V7-ERR-066: the Tools status timer failed on every tick

Cause: `MessageDialog.guard_history` documents that `size` counts only the
handler's own outputs and that the dialog pair is appended here. The error branch
honoured that contract, but the success branch returned the handler row
untouched. `src/agentix/ui/tools.py` declares nine outputs for the poll event
(`POLL_OUTPUT_COUNT = 7` plus `dialog.outputs()`), while `ToolsBackend.poll`
returns exactly seven, so Gradio 6.30 raised
`ValueError: A function (poll) didn't return enough output values (needed: 9,
returned: 7)` on every tick of the one-second `gr.Timer`. The failure repeated
indefinitely because the timer re-dispatched the same event each second. No test
covered the success branch: `tests/unit/test_message_dialog.py` exercised
`wrap_stream`, `wrap_stream_final`, `wrap_result` and `guard_result` only.

`guard_history` now returns `(*row, *self.skip())` on success, so the dialog stays
closed and the declared output count is reached. The backend, the poll contract
and the error branch are unchanged. The new regression asserts nine outputs with
the history intact on success and nine outputs with the history emptied at index
zero plus the visible modal on `ValueError`; it failed with `assert 7 == 9` before
the fix and passed after it. A read-only probe against the real framework
validated both rows through `Blocks.validate_outputs` with nine components and
nine values.

## V7-ERR-067: the Tools tab executed an application instead of its tool

Cause: `Orchestrator._run_system` ran the installed-application selector before
the exact-contract `ToolRouter`, and `_select_application` returned
`AppInvocation.observed_answer(...)` as the answer. `parse_application_selection`
then assumed every application input contract was a two-level
`node -> {parameter: value}` map. The three schema-3 applications installed in
`D:\AI\Agentix-data\v7` declare flat inputs (`{"text": {...}}`) and require a flat
payload (`code_package.validate_payload` compares `set(payload) == set(inputs)`),
so `arguments = {"text": "Hola caracola"}` made `parameters` a string and raised
`DecisionValidationError("Unknown application parameter")`. The exception aborted
the whole workflow, so `count_english_vowels` was never evaluated. The earlier
"multiply 2 by 80" query had appeared to work only because the application catalog
was still empty in that session (`workflow_started` without
`application_selection_started` in `runtime-data/7884-stdout.log`), which skipped
the selector entirely.

Solution: tool routing is now the authoritative first decision. `_run_system`
calls `ToolRouter.select` first and returns `_reuse_selected` on `REUSE_TOOL`;
application inspection happens only after `CREATE_TOOL`, through
`_suggest_application`, which builds no arguments and never reaches
`AppInvocation`. `parse_application_selection` and the `RUN_APPLICATION` prompt
examples were removed; `parse_application_suggestion` accepts only one current
catalog ID or an explicit no-match, and `AppInvocation.candidates()` exposes only
`id`, `name` and `description` for dependency-checked applications. A malformed,
ambiguous or unknown suggestion is logged as `application_suggestion_rejected` and
treated as no suggestion, so creation continues without any execution fallback.
`RunApplicationDecision` still fails closed. The Applications tab keeps its
existing execution path unchanged.

Regression: `tests/unit/test_tools_tab_routing.py` executes a real reviewed
`count_vowels` and `basic_calculator` fixture through `run_system` and asserts the
observed results (`6`, `160`) with `candidates`, `observed_answer` and `execute`
never called; `tests/test_application_routing.py` covers the safe recommendation,
the rejected/ambiguous cases and the preserved creation route;
`tests/test_catalog_routing.py` asserts the router decides before any candidate
read; `tests/test_installed_apps.py` asserts `candidates()` empties when a
dependency loses its grant. All failed before the change and pass after it.

## V7-ERR-070: catalog dependency failures hid their recovery step

Cause: `CatalogToolRegistry.resolve` already raised `CatalogDependencyError` with an
owner-actionable message naming every skipped tool and its reason, and
`CatalogDependencyError` subclasses `ValueError`. Both `load_app` and `reverify_app`
caught it in the generic `except Exception` branch, which formats only
`type(error).__name__`, so the owner saw
`Application load failed (CatalogDependencyError).` and
`Re-verification failed (CatalogDependencyError). The stored application remains
unapproved.` with no recovery step. `check_dependencies` raised a fixed
`Application dependencies require fresh review` that named neither the tool nor the
reason, and `reveal` let an `OSError` from the opener escape past `guard_result`,
which only converts `ValueError`.

Solution: `check_dependencies` now raises `CatalogDependencyError` listing each
missing role with the registry's maintained `_skip_reason`; `load_app` and
`reverify_app` catch `CatalogDependencyError` before the generic handler and yield
its text, keeping the `application_reverify_failed` warning and the explicit
`unapproved` state; `open_directory` and `reveal` convert an opener `OSError` into
`ValueError` so the modal opens. Approval behaviour, durable-record revocation,
`policy_fingerprint()` and `app_policy()` are unchanged, so no installed approval is
invalidated.

Regression: `tests/test_installed_apps.py` adds the load, re-verify and
`check_dependencies` cases; `tests/test_maintenance_owners.py` adds the refused
opener case. The red run failed all four for the reported reason and the focused
green run passed 50 tests. The five durable records deleted on 2026-11-11 are not
restored by this block: recovery is to execute and approve each tool in Tools and
re-verify each application. The running 7878 process keeps the previous code until
the owner relaunches it.

## V7-ERR-069: the catalog folder window opened behind the browser

Cause: `CatalogMaintenanceBackend.reveal` called `os.startfile`, which delegates to
the shell. Windows does not grant the foreground to a process that does not already
own it, so the Explorer window was created behind the AgentiX window. The owner
confirmed the folder did open and asked only for it to be raised. Two details
shaped the correction: Explorer reuses an already open folder, so no new window
handle appears on a second press, and the caption carries a localized suffix
(`applications - Explorador de archivos`), so an exact title comparison fails.

Solution: `src/agentix/controllers/explorer_window.py` snapshots the visible
`CabinetWClass` handles before the open and raises the new handle afterwards, or
the caption match when the folder was reused. It restores the window, applies
`HWND_TOPMOST` and immediately `HWND_NOTOPMOST` so nothing stays always-on-top,
attaches the input queues, then calls `BringWindowToTop`, `SetForegroundWindow` and
`SetFocus`. Only `ctypes` from the standard library is used. `reveal` logs
`catalog_folder_focus_failed` and keeps its success message when the foreground
change is refused. `explorer_window.py` is outside `app_policy()`, so approvals and
the policy digest are unchanged.

Regression: `tests/test_explorer_window.py` covers the fresh handle, the localized
fallback, the `tools_archive` prefix rejection, the bounded poll and the non-Windows
no-op; `tests/test_maintenance_owners.py` adds the focus, refused-focus and
foreign-session cases. The first red run failed 8 of 13 for the missing module and
the missing call. Native acceptance on a disposable port-7899 server left both
folder windows first in z-order with `GetForegroundWindow()` equal to the window.
The running 7878 process keeps the previous code until the owner relaunches it.

## V7-ERR-068: re-running tests deleted a durable tool approval

Cause: `VerificationLedger.invalidate` coupled two different operations — clearing
in-memory evidence and deleting the DPAPI-protected durable record — and it was
called on every test attempt (`TestRunner.run_and_save_tests_tool`,
`TestRunner.verify_existing_tool`), at the start of `record`, and from
`is_provisional` when the current operation identity did not match. Re-running an
unchanged suite, or polling status in a session without a session grant, therefore
removed an approval the Windows user had already granted. Applications require
that durable record (`CatalogToolRegistry` -> `prepare_reuse`), so an approved tool
became "no current reusable approval" while the Tools tab still worked from its
in-memory session grant.

Solution: `VerificationLedger.clear_evidence` now drops only in-memory receipts,
session grants, acceptance and execution state. `invalidate` keeps its explicit
revocation meaning (`_revoke_stored` plus `clear_evidence`) for catalog deletion,
repair, rejection and drift. `record`, `is_provisional` and both `TestRunner` entry
points use `clear_evidence`; a failing test run still revokes. Durable records stay
bound to exact code/tests hashes and the policy fingerprint, so changed bytes still
fail `prepare_reuse` and are revoked there.

Regression: `tests/unit/test_durable_approvals.py` adds
`test_rerunning_unchanged_tests_keeps_the_durable_approval` and
`test_recording_fresh_evidence_keeps_the_durable_approval`; both failed before the
change and pass after it, and the existing changed-bytes, policy, tamper and
explicit-revoke cases still pass. The running 7878 process keeps the previous code
until the owner relaunches it.

## V7-ERR-069: external provider rejected the tool-routing grammar

Cause: `ToolRoute.arguments` was typed `dict[str, JsonValue]`, and Pydantic emits an
empty schema (`{}`) for `JsonValue`. `RoutingModelClient` sends
`RoutingEnvelope.model_json_schema()` as the provider-enforced structured-output
grammar for the `Tool Router` role, so a strict external provider answered HTTP 400
with `output_config.format.schema: Empty schema ({}) that accepts any JSON value is
not supported`. Local Ollama accepted the same document, so the defect only appeared
after activating an external profile. Every Tools request failed closed at
`model_planning_failed` before any tool selection or execution.

Solution: `src/agentix/domain/tool_routing.py` replaces `JsonValue` with the concrete
acyclic aliases `JsonScalar` and `JsonArgument`, bounded to scalars and two nested
list levels. Recursion is deliberately avoided because provider structured output
does not support `$ref` cycles, and the tool-contract vocabulary in
`agentix.domain.tool_schema._shape` is scalars, lists and `Literal` alternatives.
Objects and nulls now fail `ToolRoute` validation instead of reaching
`validate_value`; both paths fail closed without executing a tool.

Regression: `tests/test_catalog_routing.py` adds
`test_routing_grammar_exposes_no_empty_schema_to_external_providers`, which walks the
generated schema and fails on any empty node, and
`test_reuse_arguments_accept_scalars_and_nested_lists_only`. Both failed before the
change and pass after it. Provider acceptance of the new grammar is not established
by these offline checks. The running GUI process keeps the previous code until the
owner relaunches it.

## V7-ERR-070: external provider rejected the open argument map

Cause: the V7-ERR-069 correction replaced the empty `JsonValue` schema with concrete
scalars but kept `ToolRoute.arguments` as `dict[str, JsonArgument]`. A keyed map is
serialized as `"type": "object"` with `additionalProperties: <schema>`, and the
provider structured-output subset requires `additionalProperties: false`. The same
node, `properties/arguments`, was rejected again with `For 'object' type,
'additionalProperties: object' is not supported`. The envelope also carried
`oneOf` plus `discriminator`, which that subset does not guarantee.

Solution: `src/agentix/domain/tool_routing.py` now exposes one flat `ToolRoute`
(`action`, `tool_name`, `purpose`, `arguments`) with no envelope, no union and no
discriminator. `arguments` is a bounded `list[ArgumentPair]` (`max_length` 12,
mirroring `MAX_TOOL_PARAMETERS`) where each pair is a closed object with `name` and
`value`. `ToolRouter.select` converts the pair list into the reviewed keyword mapping
and rejects duplicate names before any contract check. `CreateRoute` keeps rejecting
creation arguments through `extra="forbid"`, and `RoutingModelClient` sends
`ToolRoute` as the response model.

Regression: `tests/test_catalog_routing.py` adds
`test_routing_grammar_is_accepted_by_strict_external_providers`, which walks the
generated schema and fails on empty nodes, open or implicitly open objects, object
unions and discriminators, and
`test_router_converts_argument_pairs_and_rejects_duplicate_names`. The lint test
reports `open_object` at `$/properties/arguments` for the previous map shape and no
violation for the current one. Live confirmation: after the owner relaunched the GUI
and applied the external profile, session `b6f277898f26449a8f4f94f6e68a028b` at
11:07:43 logged `tool_routing_validated action=REUSE_TOOL tool=repeat_word_tool`,
followed by `tool_reuse_prepared`, `tool_execution_started`, sandbox `exit_code=0`,
`durable_approval_saved` and `final_execution_observed`. No `model_planning_failed`
occurred after that point. This confirms provider acceptance of the flattened grammar
for one reuse route; it does not establish creation routes or other providers.

## V7-ERR-071: creation route rejected its own serialized argument transport

Cause: `RoutingModelClient` requests `ToolRoute` as the provider-enforced structured
output for the `Tool Router` role, and CrewAI returns `result.model_dump_json()`.
Pydantic serializes defaults, so every `CREATE_TOOL` proposal reached
`ToolRouter.select` carrying `arguments: []`. That branch validated the whole
proposal against `CreateRoute`, whose `extra="forbid"` does not declare `arguments`,
so the transport field was read as an extra field and validation failed with
`Invalid tool routing decision; no selected tool was executed`. The defect was
deterministic for every creation request and independent of model quality or prompt
wording; reuse routes were unaffected because they validate against `ToolRoute`.
The existing routing tests passed because none exercised `CREATE_TOOL` through
`RoutingModelClient`.

Solution: `src/agentix/application/tool_routing.py` now copies the creation
proposal, removes only the `arguments` transport field, validates the remainder with
the unchanged strict `CreateRoute`, and rejects a non-empty transport with
`Creation route contains execution arguments for <tool_name>` before any catalog
check. `CreateRoute` keeps `extra="forbid"`, so creation still cannot declare
arguments, parameters or schema fields, and the later empty-arguments assertion
remains as defence in depth. No execution, approval or catalog rule changed.

Regression: `tests/test_catalog_routing.py` adds
`test_creation_route_accepts_the_serialized_empty_argument_transport`, which feeds
`ToolRoute(...).model_dump_json()` through `RoutingModelClient` and requires a
selected `CREATE_TOOL` with `arguments == {}`, and
`test_creation_route_still_rejects_execution_arguments`, parametrized over pair-list
and mapping transports, which requires the explicit rejection message. All three
cases failed before the change and pass after it; the other fourteen routing tests
still pass. Live confirmation is pending an authorized relaunch: the running 7880
process keeps the previous code.

## V7-ERR-072: Gradio test doubles missed the widget style colour pickers

Cause: V7-076 added `WidgetStyleDialog` (`src/agentix/ui/widget_style_dialog.py`),
which builds two `gr.ColorPicker` controls for border and background colour. The
offline doubles that inject a fake Gradio module into the real frontends were not
updated: `_gradio` in `tests/unit/test_right_sidebars.py` exposes a closed allow-list
of component names, and the `SimpleNamespace` in
`tests/unit/test_composition.py::test_view_binds_controller_and_preserves_launch_options`
enumerates its own. `SimpleNamespace` only carries the attributes it was given, so
building the real dialog raised
`AttributeError: 'types.SimpleNamespace' object has no attribute 'ColorPicker'` at
`widget_style_dialog.py:58`. Three tests failed while the product itself was correct:
Gradio 6.30 provides the component. The allow-lists had silently become stale
assertions about which components the UI uses.

Solution: both doubles now include `"ColorPicker"`, in alphabetical position after
`"Code"` in `_gradio` and beside the other checkbox entries in the composition
double. Only test files changed; no production module, contract, approval rule,
sandbox control or UI layout was touched, so runtime behaviour is unchanged. The
doubles still do not validate real colour parsing or rendering, which remains the
browser evidence owned by V7-076.

Regression: the three previously failing cases now pass
(`test_view_binds_controller_and_preserves_launch_options`,
`test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog`,
`test_both_tabs_keep_one_sidebar_each_and_no_second_column`), and the offline suite
reports `1125 passed, 107 deselected` with no failures, against `1122 passed, 3
failed` before the change. `tools/build_reference.py --check` is clean after
regenerating the two affected test references. Live confirmation is not applicable: no runtime
code changed and the running 7880 process keeps its current behaviour.

## V7-ERR-073: coder stage ended on a repairable contract rejection

Cause: `compile_and_save_code_tool` was registered with `result_as_answer=True`
through `TERMINAL_RESULT_TOOLS`, and CrewAI ends the agent turn on any result of such
a tool, including a rejection (`crew_agent_executor.py`: the `result_as_answer` check
runs after the call and returns `AgentFinish`). A generated `count_word_occurrences`
module omitted the public function docstring, so `extract_tool_schema` rejected it with
`CONTRACT_ERROR: Tool function requires an English docstring as its first statement`
and that string became the coder's final answer. The stage lasted 27 s with a single
tool call although the agent had `max_iter=12` and the rejection text invited a retry.
The prompt contributed: the mandatory preflight covered `Annotated` and the module
docstring but never the function docstring, and the architect was not asked for it, so
the approved specification showed a bare `def count_word_occurrences(...) -> int:`.

Solution: two bounded changes. `src/agentix/application/tool_workflow.py` now requires
the public function docstring as the first statement of the function body in the coder
preflight and asks the architect to state it. `src/agentix/adapters/crewai.py` adds
`REPAIRABLE_RESULT_TOOLS` and wraps that operation so `result_as_answer` is set from
the returned outcome: `CONTRACT_ERROR:` and `COMPILATION_ERROR:` hand the turn back to
the coder, while a persisted save keeps the stage terminal. Raising the rejection was
rejected as a mechanism because CrewAI converts tool exceptions into
`Error executing tool: ...` and still returns `AgentFinish` for a terminal tool.
Signature introspection is preserved, so the provider schema still exposes
`tool_name` and `code`. The host still fails closed when no fresh approved artifact
exists, and no automatic host retry was added.

Regression: `tests/unit/test_stage_completion_adapter.py` adds
`test_contract_rejection_keeps_the_coder_turn_open`, which requires a rejection to
clear terminality and a later save to restore it;
`tests/unit/test_creation_stage_gates.py` adds
`test_creation_prompts_require_the_public_function_docstring`, which requires both
role prompts to demand the docstring. Both failed before the change. The offline suite
reports `1127 passed, 107 deselected` with no failures, against `1125 passed` before
this block. Live confirmation is pending an authorized relaunch: the running 7880
process keeps the previous code.

## V7-ERR-074: candidate message blamed approval for a portability rejection

Cause: `present_candidates` marked every ineligible candidate as
`Approve or refresh in Tools` and emitted one fixed sentence naming missing
reusable approval. Eligibility actually has several causes, and
`CatalogToolRegistry._skip_reason` already computed them, but the registry exposed
only `resolve()`, so presentation could not distinguish them. A published
`count_word_occurrences` tool was fully approved (all six durable records loaded with
the current policy fingerprint) yet ineligible because `computation_only` rejected
`str.isalnum`, which is absent from `_METHODS` in `security/reuse_policy.py`. The
owner was therefore told to approve tools that were already approved, with no cause
shown. The same ineligibility disabled the accept button, which in turn hid the
application-name validation that only ran inside `generate_named`.

Solution: `src/agentix/storage/application_catalog.py` extracts `_scan` and adds
`skip_reasons()`, a bounded read-only mapping of tool name to maintained reason that
never raises, never imports generated source and returns an empty mapping for a
missing, oversized or unreadable root. `present_candidates` consumes it through an
optional attribute, labels rows as `Not portable for applications` or
`Approve or refresh in Tools`, and chooses the message from the actual causes, so a
portability rejection no longer mentions approval. `request_candidates` accepts an
optional `name` and validates it with `application_folder` before any retrieval work,
and the Generate event now forwards the name field, so an empty name opens the
existing modal warning instead of silently searching. No approval, sandbox,
publication or execution rule changed.

Regression: `tests/test_application_candidates.py` adds
`test_ineligible_candidate_names_portability_instead_of_approval`, which requires a
portability message and forbids the approval wording, and
`test_generate_without_name_reports_the_missing_name_before_search`, which requires
the name error and no retrieval call. Both failed before the change. The offline suite
reports `1129 passed, 107 deselected` with no failures, against `1127 passed` before
this block. Live confirmation is pending an authorized relaunch: the running process
keeps the previous code.

## V7-ERR-075: portable vocabulary omitted the alphanumeric predicate

Cause: `_METHODS` in `src/agentix/security/reuse_policy.py` allowed `isdigit`,
`isalpha` and `isspace` but not `isalnum`. A published `count_word_occurrences` tool
used `str.isalnum` for input validation, so `computation_only` returned False and the
tool was excluded from application dependencies even though its approval was current.
The rejection surfaced as the portability row label added by V7-ERR-074, which is why
the cause was visible rather than misattributed to approval.

Solution: `isalnum` joins the explicit pure-predicate vocabulary beside the other
character tests. No other method, module, node or call form was added, and the
conservative classifier still rejects private attributes, dynamic calls, unknown
imports and non-computation constructs. Because `security/reuse_policy.py` is sealed
into `policy_fingerprint`, this change invalidates every existing durable approval by
design: the fingerprint moved from `37e3c5b979943c4e` to `f3711d1cb65fd3f0` and each
record now reports `durable_approval_invalid`. Owners must execute and approve the six
installed tools once more in Tools before generating applications. That cost was
stated and accepted before the change; excluding the policy file from the fingerprint
was rejected because it would keep approvals valid under a widened security surface.

Regression: `tests/unit/test_reviewed_reuse.py` adds the `isalnum` case to
`test_computation_classifier_is_conservative` and
`test_alphanumeric_predicate_is_portable_but_private_introspection_is_not`, which also
requires `x.__dict__` to stay rejected. Both failed before the change. The offline
suite reports `1131 passed, 107 deselected` with no failures, against `1129 passed`
before this block. Verified against the real catalog: `computation_only` now returns
True for the published tool and `skip_reasons()` reports only the approval cause,
which is accurate and actionable.

## V7-ERR-076: policy rotation destroyed recoverable approvals

Cause: `ApprovalStore.load` compared the sealed `policy` field inside the same
identity check as root, tool, code and test digests, and any mismatch revoked the
record. A policy-only rotation therefore deleted intact grants whose reviewed bytes
had not changed, forcing a full re-run and re-approval of every installed tool. The
owner had to repeat tests, acceptance review and execution for six tools after
V7-ERR-075, although only the policy fingerprint had moved.

Solution: `load` now checks root, tool, code and test digests first and treats a
policy mismatch as `durable_approval_policy_stale`, returning no grant while keeping
the record. `ApprovalStore.reseal` revalidates the sealed schema, identity, approved
functions and reviewed contract, then rewrites the same grant under the current
policy; changed bytes, a missing record or an invalid contract return False and stay
revoked. `CatalogMaintenanceBackend.reseal_tools` iterates the installed catalog,
reseals intact records and stops at the first refusal, reporting the tool that needs
the full Tools flow. `src/agentix/ui/tools.py` adds the
`Autovalidate all tools (reseal unchanged, run changed)` button above the installed
tool selector, wired through the existing dialog guard. No tool is executed by the
batch, no grant is created for unreviewed content, and sensitive per-call approval is
untouched.

Regression: `tests/unit/test_durable_approvals.py` adds
`test_reseal_rebinds_unchanged_bytes_to_the_current_policy` and
`test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked`;
`tests/test_maintenance_owners.py` adds
`test_reseal_batch_stops_at_the_first_changed_tool`. All three failed before the
change. The offline suite reports `1133 passed, 1 failed`; the single failure is
`tests/unit/test_iac.py::test_managed_file_links_are_rejected`, which imports no
`agentix` module and only exercises a PowerShell junction. It passes in isolation,
passes 5 of 5 consecutive repetitions, and its whole module reports `58 passed`, so it
is an environment-sensitive flake under full-suite load rather than a regression of
this block. Live confirmation is pending an authorized relaunch: the running process
keeps the previous code.

## V7-ERR-077: read-only diagnostics revoked approvals and the batch misreported it

Cause: two defects compounded. First, `ApprovalStore.load` revoked the sealed record
whenever the policy fingerprint differed, so any read path destroyed the grant. An
engineering diagnostic that called `CatalogToolRegistry.skip_reasons()` against the
real store at 18:48:43 therefore deleted all six owner approvals that had been saved
between 18:07 and 18:20; the approvals directory mtime and six
`durable_approval_invalid` events match that call. Second, `reseal` returned a bare
boolean and `reseal_tools` mapped every refusal to one sentence, so the owner was told
`calculator` had changed bytes when in fact no record existed. The owner had not
touched the tool.

Solution: `ApprovalStore.peek` validates a record for presentation and never revokes,
and `CatalogToolRegistry._skip_reason` uses it so opening the catalog cannot destroy a
grant. `reseal` now returns `None` on success or a bounded reason (`missing`,
`changed`, `invalid`), and `reseal_tools` reports the matching owner action, so a
revoked record is never described as changed bytes. Revocation on genuine content or
identity drift is unchanged, and no grant is created for unreviewed content.

Regression: `tests/unit/test_durable_approvals.py` asserts `peek` keeps a stale record
and that `reseal` returns `changed` and `missing` distinctly;
`tests/test_maintenance_owners.py` adds
`test_reseal_batch_reports_a_missing_record_as_missing`, which forbids the word
`changed` for an absent record. The three earlier reseal cases still pass.

Limitation: the six records deleted at 18:48:43 cannot be recovered, because the store
keeps no backup and the deletion was a real unlink. The owner must run and approve
those tools once more; after that, future policy rotations are recoverable through the
button without re-execution.

## V7-ERR-078: the autovalidate button promised a run it never performed

Cause: the button label read `Autovalidate all tools (reseal unchanged, run changed)`,
but `CatalogMaintenanceBackend.reseal_tools` only resealed intact records and stopped
at the first refusal. With every record deleted by V7-ERR-077, the batch therefore
reported `Resealed 0 tool(s). Stopped at calculator: no approval record exists` and did
nothing else, so the owner still had to run each tool by hand. The label described a
behaviour that was never implemented; the message was accurate but the button was
useless in exactly the case it was built for.

Solution: `reseal_tools` now completes the second half. An intact record is still
resealed without execution. A `missing` or `changed` record is re-verified through
`verify_existing_tool_tool`, which runs the stored tests inside the native isolation
boundary and never imports generated code on the host. The batch stops at the first
failing suite and names the tool; a passing suite is reported as re-run with the
acceptance review still pending. `invalid` records stop immediately because their
reviewed contract cannot be revalidated. Acceptance review remains mandatory and is
never granted by the batch, so no grant is created for unreviewed content.

Regression: `tests/test_maintenance_owners.py` replaces the earlier batch cases with
`test_reseal_batch_stops_when_changed_tool_tests_fail` and
`test_reseal_batch_reruns_missing_tools_and_requires_acceptance`, which require the
isolated re-run, the stop on failure, and the pending acceptance review.
`tests/unit/test_durable_approvals.py` keeps the `missing`/`changed` reason contract.
The offline suite reports `1135 passed, 107 deselected` with no failures, against
`1133 passed, 1 failed` before this block. Verified end to end against a temporary
store with a rotated policy: the batch resealed the intact tool, re-ran the two tools
without records, and left the resealed record loadable.

## V7-ERR-079: durable approvals were skipped during candidate discovery

Cause: `CatalogToolRegistry._skip_reason` combined its read-only `ApprovalStore.peek`
check and `VerificationLedger.prepare_reuse` with `and`. A valid sealed record made
`peek` non-None, so Python short-circuited before `prepare_reuse`. A fresh ledger
therefore lacked the in-memory acceptance and provisional identity required by
`acceptance_context`, even though the protected grant matched current bytes and
policy. Candidate resolution excluded the tool and the GUI reported that approval
was missing. `prepare_reuse` itself already restored both identities correctly.

Solution: `_skip_reason` now rejects an absent or mismatched read-only peek and
always prepares reuse when the peek is valid. The existing ledger still loads and
validates exact source/test bytes, policy, reviewed functions and contract; it does
not execute tool tests or create approval. `AcceptanceService.submit` and its
manual exact-byte review requirement are unchanged.

Regression: `test_durable_approvals_populate_fresh_catalog_and_candidate_context`
in `tests/test_application_catalog_skip_reasons.py` builds six independently
authored tools and sealed approvals under temporary storage. Before the change,
five of six were excluded with `no current acceptance context`; afterwards,
`acceptance_context` returns reviewed contract and functions, `resolve` includes
all six, and `present_candidates` marks five displayed candidates ready with the
expected generation prompt. Existing durable-approval tests continue to reject
changed code, tests and policy. The live GUI and its existing process have not been
reloaded; live candidate behavior remains to be verified on a later authorized
launch.

## V7-ERR-080: successive widget saves reverted earlier web styles

Cause: `ApplicationSession.restage_styles` rebuilt the served `application.css`
from the immutable approved application files on every save. A second widget save
therefore replaced the first widget's new CSS with its original bytes. The framed
preview still held the first style as inline declarations, while a separate "View
as web" page used the reverted served sheet. On the owner's running application,
the Result widget had inline border radius 5 px, width 1 px and cyan border, but
the served stylesheet contained only its original text-colour declaration.

Solution: `restage_styles` now retains the latest CSS bytes for every widget in the
application session and rebuilds the served sheet from that copy. The existing
`ApplicationReview.save` path still writes each `<tool>_widget.css` in the draft
package and rebinds its manifest hash; loaded installed applications also use the
existing installed-package write path. No approval or executable-code rule changed.

Regression: `test_restage_styles_preserves_successive_widget_saves` failed before
the fix because the first widget's 22 px radius disappeared after saving a second
widget and passes afterwards. `test_review_style_save_keeps_the_candidate_approved`
verifies that both individual CSS files contain their respective saved bytes. The
browser snapshot cascade test passes with an independent temporary fixture. The
running 7878 and 60126 processes were preserved, so live confirmation awaits a
later authorized launch.


