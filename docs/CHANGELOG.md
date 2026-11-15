# Current change log

## 2026-11-13 — V7-075 Mermaid rendering in the read-only Code Help transcript
The Applications `Code help` transcript is now a Markdown component, so a fenced
Mermaid diagram returned by the model renders as an inline SVG instead of literal
text. `mermaid_render.js` scopes a `MutationObserver` to
`#chathelper-transcript`, handles both Gradio's `<div class="mermaid">` and a
`pre > code.language-mermaid` block, and draws each diagram with
`mermaid.render` under `securityLevel: 'strict'` plus a bounded retry for
Mermaid's load-time render queue; unparseable blocks keep their source and are
excluded from retries. `branding.mermaid_script()` wraps the pinned Mermaid
11.12.2 bundle in an IIFE so Gradio's `eval` scope still publishes
`globalThis.mermaid`, with the vendored bytes and their SHA-256 unchanged, so no
CDN or network fetch is introduced and the launch-time `js` option stays
self-contained. No tool, widget, declarative case, AppContainer boundary or
policy digest changes. See
[specification](specs/075-code-help-mermaid-rendering.md).

`tests/test_v5_review_browser.py::test_review_resize_and_context_help` now carries
a strict `xfail` (owner decision D): V7-068 moved `#application-candidates-accept`
into the closed `#applications-sidebar` and the test never opens it, so the click
waits for a hidden element. The flow passes with the toggle clicked; the repair
changes the geometry asserted later in the same test and awaits its own block.
`xfail_strict = true` turns an unexpected pass into a failure.

## 2026-11-13 — V7-074 browser evidence for the composite accordion
The cancellation browser test now slows the application-owned
`count_words_in_text_code.py` instead of the maintained `operation.py`, closing
defect V7-074-D1 where strict capture rejected the fixture with
`RuntimeSourceChanged` before Chromium started; `allow_runtime_drift` was rejected as
a correction because it replaces the member and deletes the delay. A new
`tests/test_composite_data_browser.py` renders the real Applications tab and keeps the
visible input contract, the hidden stale table and the bounded `JSONDecodeError`
diagnostic. Only test modules change, so no approval, grant or policy digest moves.
See [specification](specs/074-composite-browser-evidence.md).

## 2026-11-13 — V7-073 composite data-operation input contract and diagnostics
The `Use the application as a composite tool` accordion now states the loaded
application's closed JSON input contract, with one row per declared key and one
example payload, and refreshes it through `Show input schema` or on every run.
Catalog applications render one `Named results` table with `Result`, `Type` and
`Value` instead of the fixed `Words`/`Vowels` fields, which legacy applications keep.
A rejected payload now names its bounded reason, closing defect V7-073-D1 where
`hola gola` produced only `Data operation failed (JSONDecodeError).` without the
required keys or the JSON position; the message never repeats the typed payload.
`describe_data_inputs` and `named_result_rows` bound model-authored descriptions and
observed values, and `ApplicationsBackend.data_contract` reads only the verified
snapshot. No tool, widget, declarative case, AppContainer boundary or policy digest
changes. See
[specification](specs/073-composite-data-input-contract.md).

## 2026-11-12 — V7-067 separate web tab, Edit affordances and code-help identity
A Generated Application heading now offers `View as web`, which opens the same
validated loopback page in a new tab. Edit mode keeps the widget name clear of its
move handle, restores the default surface of the outer box, shows a visibility
checkbox with a visible checked state and adds a compact `Tools` colour legend built
from the same mapping as the move handles. The isolated page titles itself with the owner's application
name from a host-staged `application_display.json`, never from a query parameter or
an evaluated script, because the bridge Content Security Policy forbids
`unsafe-eval`. Code Help now names the file it answers about, closing defect
V7-067-D1 where the pane identity had been stored instead of the file. Two further
defects found in the delivered Edit mode are closed: V7-067-D2, where the visibility
checkbox toggled without any visible state because the forced dark fill hid the dark
checkmark, and V7-067-D3, where Gradio's full-width child rule stretched the colour
legend across the viewport. The legend is now a compact `Tools` box pinned below the
layout notice. The template participates in `app_policy()`, so previously installed
applications require re-approval. See
[specification](specs/067-generated-application-web-and-edit-affordances.md).

## 2026-11-12 — V7-064 actionable catalog dependency diagnostics
`Re-verify selected app` and `Load selected app` now name the missing tool approval
and the recovery step instead of only the exception type, and a missing application
dependency names the tool with its maintained skip reason. A refused shell open
reaches the maintained modal instead of a raw framework error. Approval behaviour,
durable-record revocation, `policy_fingerprint()` and `app_policy()` are unchanged,
so no installed approval is invalidated. See
[specification](specs/064-catalog-dependency-diagnostics.md).

## 2026-11-12 — V7-065 the catalog folder window is raised above the browser
`View in explorer` now leaves the Explorer window of the installed Tools or
Applications folder above AgentiX with keyboard focus, instead of behind the
browser. The window is not left always-on-top, a refused foreground change is
logged without failing the completed open, and ownership, root validation and
linked-folder refusal are unchanged. Only `ctypes` from the standard library is
used. `explorer_window.py` is outside `app_policy()`, so approvals and the policy
digest do not move. See
[specification](specs/065-explorer-window-foreground.md).

## 2026-11-11 — V7-063 catalog explorer buttons and per-tool handle colors
`View in explorer` opens the installed Tools or Applications folder from a
server-resolved root bound to the owning session; a foreign session, an unknown
catalog, a missing folder or a linked folder is refused and the browser never
supplies a path. In Edit, move handles are tinted per tool group so related
widgets are recognizable; the tint is re-randomized on each Edit entry, applied
only to the handle and never persisted. `layout_contracts.py`,
`application/app_controls.py` and `ui/assets/application_editor.js` participate
in `app_policy()`, so installed applications require re-approval under the new
boundary digest `859d7f910c68615c...`. See
[specification](specs/063-catalog-explorer-and-tool-colors.md).

## 2026-11-11 — V7-062 widget visibility outside Edit
Edit mode now renders a 16 px checkbox over every editable canvas control.
Checked keeps the control visible after leaving Edit; unchecked hides it with
`display: none`, so Gradio callbacks, entered values and the Status indicator
keep working. Visibility is stored as the optional `hidden` list of the same
version-1 layout record and validated against the shared control allowlist, so
toolbar and foreign IDs stay rejected and older `config.json` files remain valid.
`layout_contracts.py` and `ui/assets/application_editor.js` participate in
`app_policy()`, so the policy moved to `fb943707bfc10e53...` and installed
applications require re-approval. See
[specification](specs/062-widget-visibility.md).

## 2026-11-11 — V7-061 catalog services outside the installed-application policy
`app_policy()` hashed `storage/maintenance.py`, so the V7-060 removal fix
invalidated every installed application again. The removal service never runs in
the AppContainer child and only the deletion route imports it, so it is no longer
hashed; twenty-three files remain, including every execution member. `get()`
still refuses a stale policy and removal keeps its lock, lease, dependency and
digest gates. `usage.py`, `catalog_lock.py`, `layout_contracts.py` and
`application_editor.js` stay hashed because they participate in host validation.
The policy moved to `e22809c743f4bb45…`, so one final re-verification is needed.
See [specification](specs/061-catalog-services-outside-policy.md) and
[incident](V7_INCIDENTS.md#v7-err-005).

## 2026-11-11 — V7-060 permanent removal ignores a stale policy binding
`Delete selected application` returned `Application approval is stale` for every
installed application after V7-059 changed a maintained source hashed by
`app_policy()`. `CatalogMaintenance._prepare` resolved the record through
`InstalledApps.get()`, which enforces the execution policy on an operation that
never executes the package. The application branch now uses `load_stale()`, which
still verifies identity, exact source digest and review digest, while the usage
and dependency checks are unchanged and `confirm()` recomputes everything under
the catalog lock. `get()` still refuses a stale policy. See
[specification](specs/060-stale-policy-removal.md) and
[incident](V7_INCIDENTS.md#v7-err-004).

## 2026-11-11 — V7-059 closed public input schema diagnostics
`SuperRepeater` failed with `Application generation failed (ValueError)` because
the plan task emitted `minimum: 0` for `repeat_count`, derived from the approved
`repeat_word_tool` contract, and `validate_input_shape` accepts only `type`,
`description`, `enum` and `items`. The plan prompt now lists the closed keys and
forbids numeric bounds and other JSON Schema keywords, `ApplicationContractError`
names the input and the sorted rejected keys without carrying the value, and the
controller propagates that closed text only. The contract is not relaxed and no
live model run was performed. See
[specification](specs/059-closed-input-schema-diagnostics.md) and
[incident](V7_INCIDENTS.md#v7-err-003).

## 2026-11-11 — V7-ERR-066 guarded poll output count
`MessageDialog.guard_history` appended the dialog pair only on its error branch,
so the Tools status timer returned seven values for nine declared outputs and
Gradio raised `ValueError: A function (poll) didn't return enough output values
(needed: 9, returned: 7)` every second. The success branch now returns
`(*row, *self.skip())`; the backend, the poll contract and the error branch are
unchanged. A unit regression covers both branches and the touched reference pages
were regenerated. See [incident](V7_INCIDENTS.md#v7-err-066-the-tools-status-timer-failed-on-every-tick).

## 2026-11-10 — V7-058 explicit profile selection and truthful generation diagnostics
Accepting application candidates in a fresh session no longer fails silently when
no saved profile was selected. `ensure_generation_identity()` raises the closed
code `profile_not_selected`, `_generate()` shows each identity rejection with its
own message and logs `application_generate_rejected` with a bounded reason, and
`demo.load` auto-selects the only saved profile for editing. The Refresh saved
profiles button keeps the displayed selection, a changed digest still requires
the explicit reset, and no profile record, credential or trusted digest is
rewritten. See [specification](specs/058-profile-selection-diagnostics.md).

## 2026-11-07 — ARCH-015 ui/controllers module filename simplification
Fourteen maintained modules dropped their `_front`, `_frontend` and `_back`
filename suffixes: `controllers/{applications,catalog,chathelper,sidebar,
tool_repair,tools}.py` and `ui/{application_candidates,applications,apps_catalog,
catalog_actions,chathelper,sidebar,tool_repair,tools}.py`. Only module paths and
their imports changed; every public class, function, signature, docstring and
implementation stayed byte-identical, no alias module or `sys.modules` shim was
added, and the retired legacy names remain retired. Storage, security, approvals,
credentials, DPAPI, generated tools and persisted user data were not touched.
Reference pages were regenerated with `tools/build_reference.py`.

## 2026-11-07 — ARCH-014 intentional legacy import alias retirement
The 35 remaining `sys.modules[__name__]` compatibility alias modules were removed
and canonical package paths are now the only supported internal imports. ARCH-01,
the architecture document, the incident limitation and the README state the
retirement; `docs/v5-module-moves.json` records an empty migration set. This is an
intentional compatibility break: legacy paths such as `agentix.ui.tools_backend`
or `agentix.orchestration` no longer import. No canonical implementation, storage,
security, approval, sandbox, model or application behavior changed, and persisted
tools, applications, approvals and user data were not touched. Offline regressions
assert canonical symbol availability, the absence of alias assignments, the
absence of retired import paths and canonical `agentix.storage` package
resolution.

## 2026-11-06 — V7-055 explicit host dependency recovery
Application approval now probes a static host-owned requirement registry before
native/browser verification. A missing Playwright Chromium leaves the reviewed
proposal pending, explains the bounded host change and offers an owner-bound
explicit installation button. The installer uses only the active Python with
isolated Playwright Chromium arguments, scrubs inherited package/proxy settings,
checks its resulting executable and never replays approval. No generated source,
model output or browser value can name a dependency or command. Tools, installed
applications, Ollama and Python packages are unchanged.

## 2026-11-06 — IAC-013 readable DSC completion summary
Apply no longer emits the same DSC machine JSON twice. It retains the captured
result for failure diagnostics and reports concise completion and resource-count
stages instead. The DSC JSON protocol and installation behavior are unchanged.

## 2026-11-06 — DOC-012 stale-plan recovery guidance
The V7 installation guide now explains the reviewed-plan stale or mismatched
case: compare the printed plan with the saved JSON, generate a uniquely named
fresh plan, review it, apply it immediately and confirm Test before launch.

## 2026-11-06 — IAC-012 real-time parent process visibility
The IaC native-process adapter now drains stdout and stderr concurrently and
can forward labeled lines to the invoking PowerShell Information stream while a
child runs, without treating zero-exit stderr as failure. Apply emits concise
reviewed-stage messages. The DSC resource stdout JSON contract remains unchanged;
no child-resource stderr bridge is part of this phase. Focused offline regressions
cover line forwarding, concurrent streams, zero-exit stderr, failures, timeout
and bounded diagnostics.

## 2026-11-06 — IAC-011 managed Playwright Chromium
The Windows IaC environment now resolves the Chromium executable required by
its installed Playwright package. Convergence reuses a compatible binary or
installs Chromium only, using the managed virtual-environment Python; failed
browser installation fails with a clear diagnostic. GUI and CLI launch resolve
the same environment-compatible executable while preserving an existing caller
configuration when it is unavailable. The Playwright pin and runtime lock are
unchanged. Focused offline IaC regressions cover fresh installation, reuse,
failure and launcher detection.

## 2026-11-05 — V7-ERR-001 session-routing fixture profile
The trusted session-routing fixture now provides the locally configured Ollama
profile and stable generation identity required by the production gate. It
continues to use an injected pipeline and never contacts a provider. The fix
restores the test's intended ownership assertions without weakening production
profile validation.

## 2026-11-05 — IAC-010 explicit V7 deployment roots
User-approved clean V7 deployment contract. Schema-2 infrastructure configuration
now binds the managed runtime/state home to `D:\AI\Agentix-data\v7` and generated
artifacts to `D:\AI\AgentiX_v7\generated_tools`; it no longer derives or adopts the
V5 namespace. IaC rejects unsafe path forms and overlapping roots, binds location
receipts to the reviewed home and keeps the browser cache lookup under the user-local
Playwright location. Offline IaC regressions cover path derivation, rejection and
receipt binding. No V5 data was read, moved or deleted; no installer, model, GUI or
live process was started by this source change. A separate reviewed `Plan`/`Apply`
operation remains required to provision the new location.

## 2026-11-02 — Early duplicate application name check
User-approved UX fix after a real incident: verification passed but publication failed with "An application with this name already exists" because a stale, invisible install folder still reserved the name. InstalledApps gained name_available(name) (folder-existence contract, same rule publish enforces) and ApplicationsBackend.generate_named now rejects an occupied name before any model work with "An installed application already uses this name; delete it first or choose a different name". The stale Multiplyvowel leftovers (install folder, approval record, review) were removed with user consent.

## 2026-11-02 — Browser launch evidence and launcher Playwright variable
User-approved diagnostics follow-up. New launch_acceptance_browser helper (application/general_acceptance.py) wraps Chromium launch for both schema-2/3 and legacy browser acceptance: a configured but missing AGENTIX_PLAYWRIGHT_EXECUTABLE fails with a clear actionable ValueError, and any launch failure now writes bounded browser-failure.json evidence (stage "browser_launch") plus a warning event instead of escaping evidence capture. The IaC launcher (infra/Agentix.Iac.psm1) resolves the newest managed chromium_headless_shell under the deployment Local root and exports AGENTIX_PLAYWRIGHT_EXECUTABLE for GUI/CLI launches, restoring the prior value afterward. InstalledApps.list now logs the safe rejection detail (e.g. stale policy) instead of dropping records silently. Offline unit suite and Ruff green; reference pages regenerated. Note: the general_acceptance.py change alters the installed-app policy hash, so previously installed applications require re-approval under the new boundary.

## 2026-11-02 — Persistent file logging and application lifecycle diagnostics
User-requested diagnostics addition. Process logging now also persists to a bounded rotating file at `<AGENTIX_HOME>/data/logs/agentix.log` (5 MiB × 3), installed once by bootstrap.configure_process with the same SecretFilter redaction; root level is normalized to INFO when a host (e.g. pytest) pre-installed handlers left it at WARNING. Added payload-free lifecycle events across the application creation path: generate start/rejected/tools-resolved/model start-finish, approve started/blocked (with the safe maintained reason), verify start/stage/failure, supervisor approval checks (dependency recheck, acceptance validated, approved), schema-2/3 acceptance stages (widget tests, native acceptance, browser acceptance), review group saves, acceptance save success and invalid-acceptance detail (missing field names only, never values), and pending independent-case fields at proposal time. Offline suite and Ruff green; reference pages regenerated.

## 2026-11-02 — Catalog selection pre-checks
User-approved UX fix: Load/Play/Delete selected application with an empty selection now open the modal with "Please, select an installed application." before any backend call, replacing the technical "Application load failed (ValueError)." text. Delete controls (both tools and applications kinds) received the shared dialog and open the modal on validation and safe generic failure messages. Offline suite green (883 passed; known flaky test_iac link test passes isolated); Ruff clean; reference pages regenerated; all three buttons browser-verified on the restarted 7878 instance.

## 2026-11-02 — Modal status follow-up
User-approved presentation change: Approve and verify, Reject proposal, Run data operation and Load/Play selected app now open the modal Ok dialog with their outcome message in addition to the persistent status text. Added MessageDialog.wrap_stream_final (only the stream's final non-empty status opens the modal; intermediate progress rows do not) and an optional status_index on wrap_result. Streaming handlers (approve/repair/review_tools/load_app/open_app) use stream wrappers; guard_result rejects generator handlers with TypeError. Offline suite green (879 passed; the known flaky test_iac link test passes isolated); Ruff clean; reference pages regenerated. The running 7878 instance was restarted and each affected button was browser-verified to open the modal.

## 2026-11-01 — UI dialog coverage fix
User-approved error-dialog correction. The modal MessageDialog now guards every Gradio handler that can raise (sidebar, Tools, Applications and installed-app catalog); validation errors open the persistent Ok dialog instead of Gradio's ephemeral toast. Added MessageDialog.guard_result (error-only, scalar/None-safe), preserved handler signatures through the wrappers with functools.wraps so Gradio keeps injecting Request (their loss caused TypeError toasts), kept bind() ApplicationsBackend callback renaming working through wrappers, and shared one dialog built at shell level. Offline suite green (876 passed); Ruff check/format clean. A user restart of the running 7878 app is required to load the change.

## 2026-10-30 â€” V5-039
Catalog-driven typed applications and semantic tool selection; canonical Annotated function contracts; persistent approved widget reuse; four real GUI-generated tools and model-generated widgets composed by maintained code. Human review corrected model proposals. Fresh native/browser acceptance and installed-app GUI cases passed. Fixed exact-byte review saves and radio/queue/table verification regressions. Dark scrollbars and readable verbose activity preserve raw diagnostics. Polling race fixed on disk; user explicitly declined a restart of 7880. See [delivery evidence](reports/V5_039_DELIVERY_REPORT.md) and [incidents](V7_INCIDENTS.md).

## 2026-10-29 â€” V5-038
Permanent confirmed catalog deletion with dependency and active-use blocking; edit rejected tool code/tests and explicitly restart review/validation. Libraries and retrieval remain research only.

## 2026-10-29 â€” V5-037
Independent v5 checkout, topic packages, frontend/controller/application separation, named application folders, owned sandbox cleanup, per-widget CSS, adjustable review panes and read-only contextual code assistance.

## Earlier releases
See [historical decisions and incident digest](HISTORY.md). Detailed original logs are in the external documentation backup. Earlier test counts are not current evidence.

## 2026-10-30 â€” DOC-040
User-approved documentation-only cleanup. Reduced AGENTS and six local skills, removed irrelevant framework guides and redundant report documents/logs/screenshots, consolidated inherited documentation and added selective-reading guidance. Preserved code, tests, configuration, data/fixture files, licenses, generated reference pages and final verification evidence. No application restart. See [cleanup audit](reports/DOC_040_CLEANUP.md).


## 2026-10-30 â€” V5-041
User-approved general workflow bindings: shared external inputs, typed JSON
constants, explicit array-item selection and repeated-tool fan-out. Acceptance
selects coherent independent cases with bounded backtracking. Reviewed legacy
runtime bytes remain supported. See [specification](specs/041-general-workflow-bindings.md)
and [verification](reports/V5_041_WORKFLOW_BINDINGS.md). Source-only for the live
7880 process; no restart or real-model creation is part of this block.


### V5-041 live transport follow-up
V5-ERR-041-03 preserves absent binding fields across the actual model boundary,
aligns provider grammar with source exclusivity, and adds bounded per-client HTTP
wait injection. The normal default is unchanged; only the owned validation GUI
uses the explicitly approved 600 seconds. Live outcome is recorded separately.


## 2026-10-30 â€” V5-042
User-approved CrewAI application coordination with sequential tasks, explicit
context and structured output. Generate only pending widgets, preserve approved
reuse and owning-session verbose/events. Retire prefix grammar and direct HTTP
from production application creation. Host validation, reviewed bytes and native
execution remain required. See [specification](specs/042-crewai-application-coordination.md).


## 2026-10-30 â€” V5-043
The user approved generated application connection code instead of the custom graph.
CrewAI now emits reviewable Python plus input/presentation metadata. Version-3
packages reopen and execute in the native worker without agents or graph machinery.
Existing tools/contracts remain unchanged and approved widgets are reused. The
existing review editor exposes code and independent host-held acceptance cases;
missing cases block approval, not draft creation. Legacy packages remain supported.
See [specification](specs/043-generated-application-code.md).

V5-043 closure: offline 827 passed, real frameworks 13 passed, native dependent-call
and failure fixtures passed, and repeated native browser checks passed. Simply app
was generated with qwen3-coder:30b, reviewed, independently verified, installed and
visibly executed with Hello world => 3 vowels, 2 words, 9 and 6. Only the owned
7882 GUI was reloaded; 7880 stayed intact. See [verification](reports/V5_043_GENERATED_CONNECTION_CODE.md).


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

## 2026-11-03 — V7-050 Ollama launch compatibility

Approved separation of existing loopback Ollama API readiness from exact managed
provisioning. Manual launch warns on server version drift; missing API/model and
other prerequisite failures still block. Restored the provisioning profile pin to
0.40.13. No live application restart or installer/provisioning action was performed.
See [V7-050](specs/050-ollama-launch-compatibility.md).

## 2026-11-03 — RAG-001 independent retrieval
Added a standalone Chroma/Ollama hybrid retriever, bounded keyword generation, correlated diagnostics and static real-tool retrieval fixtures. No agent integration or execution grants. See specs/051-tool-retrieval.md.

RAG-001 verification: 934 offline tests passed; explicit Ollama retrieval evaluation returned all four expected top hits. Ruff and reference freshness passed. See reports/RAG_001_DELIVERY.md.

## 2026-11-03 — RAG-008 named retrieval policies
Replaced retrieval magic numbers with typed, documented constants; shared keyword bounds across contracts and generation, and derived BM25 factors from named parameters. Preserved ranking, numeric limits and stored schema. Added five independent characterization tests.

RAG-008 verification: 939 offline tests passed; Ruff and reference freshness passed. See reports/RAG_008_REFACTOR.md.

## 2026-11-03 — RAG-009 catalog-backed retrieval
Added initial catalog loading and incremental reconciliation before every search. New/modified tools are embedded, unchanged vectors reused, deleted/rejected entries removed. Added source-bound reopen checks, safe bounded AST scanning, a standalone sync command and regression tests. No GUI restart or tool execution.

RAG-009 verification: 953 offline tests passed; Ruff and reference freshness passed. Real catalog load indexed all four tools; reopening reused all four vectors and a real metadata query returned the expected top candidate. See reports/RAG_009_CATALOG_SYNC.md.

## 2026-11-03 — RAG-010 GUI candidate acceptance
Added startup catalog loading, a candidate panel below application deletion, integer limit searches and one-use owner-bound acceptance before generation. The pipeline and repairs receive only accepted eligible tools. Added safe flow diagnostics, startup/retry and stale-response controls, current-source checks and browser regressions. Runtime Chroma pin matches the existing lock; no installer or live restart.

## RAG-011: stable candidate previews and checkboxes

Description edits no longer clear the preview. Each result is checked by default; only the validated checked subset reaches generation. Empty selections disable acceptance. See specs/053-candidate-checkboxes.md.

## 2026-11-12 — V7-069 left sidebar overlap

Expanding the shared model sidebar left an 80 px strip before the work area because
the resizer wrote the shared `.sidebar-parent` overlap for every panel and the Tools
width won. Only the left panel now owns that variable, using Gradio's own
`width - parent.left + 30` formula. Measured 30 px in Chromium with the Tools panel
open. See [V7-069](specs/068-tab-right-sidebars.md#defect-v7-069).

## 2026-11-12 — V7-070 sidebar inset and fixed left panel

The shared model sidebar is no longer resizable: it keeps Gradio's fixed 390 px width
and only owns its own overlap padding, so the 80 px strip stays at the native 30 px
gutter. Both right panels gained a small content inset (`22px 22px 22px 40px`) so they
no longer sit flush against the workspace edge. Verified in Chromium: gap 30 px, no
handle on the left panel, Tools content inset 40 px. See
[V7-070](specs/068-tab-right-sidebars.md#defect-v7-070).

## 2026-11-12 — V7-071 right sidebar gap

The V7-070 inset only padded the panel content; the panel itself stayed at `right: 0`
and touched the workspace. Both right panels now open at a 12 px gap
(`--agentix-sidebar-gap`) and the workspace reserves `width + gap * 2`, so content
stops 12 px before the panel border and the resizer fills the gap. Measured in
Chromium: 12 px on both sides of the panel edge, previously 0 px. See
[V7-071](specs/068-tab-right-sidebars.md#defect-v7-071).
