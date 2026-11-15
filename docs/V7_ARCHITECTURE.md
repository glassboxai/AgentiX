# AgentiX v7 architecture

V5 requirement identifiers and evidence names remain historical.

## Main execution paths

AgentiX uses a layered modular monolith with ports/adapters and explicit dependency
injection at bootstrap.py. It is not a microservice deployment. Native workers
provide a separate execution security boundary; the host never imports generated
Python. Canonical package paths are the only supported import paths; the retired
compatibility alias layer is not restored.

```text
ui/tools.py                -> controllers/tools.py
                           -> controllers/tool_controller.py
                           -> application/tool_workflow.py
ui/applications.py         -> controllers/applications.py
                           -> application/app_workflow.py
ui/sidebar.py              -> controllers/sidebar.py -> models / storage
ui/chathelper.py           -> controllers/chathelper.py
                           -> application/code_assistance.py -> injected model
```

## Responsibility packages

| Package | Responsibility |
| --- | --- |
| ui | Gradio components, formatting, shared theme and maintained browser behavior |
| controllers | Session/token checks, UI operation dispatch and response coordination |
| application | Tool workflow, application workflow, review, invocation and preview controls |
| domain | Framework-independent contracts and application-name validation |
| agents | Agent roles, workflow policy and bounded application model adapters |
| models | Local/external profile validation and provider clients |
| host_requirements | Static host dependency registry, bounded probes and explicitly confirmed repair commands |
| storage | Artifact IO, installed tool/app catalogs, reusable widgets and profile metadata |
| security | Human authorization, acceptance, content binding, DPAPI, credentials and path checks |
| sandbox | Windows AppContainer lifecycle, jobs and owned empty-residue cleanup |
| widgets | Scoped style validation and independent widget presentation assets |
| lab | Maintained experimental transport, deterministic motor and compositor support |
| infra (repository root) | PowerShell/DSC provisioning and managed launchers |

The legacy lab package is retained as transport/composition support rather than
renamed in the same behavioral increment. Root compatibility modules were retired;
canonical package paths are the supported imports.

## Patterns and constraints

Dependency injection, adapters, repository-style catalogs, explicit composition
roots, strict contracts and dependency-ordered workflow execution are retained.
Each session owns controller/model state. New helper histories live on that
controller and change scope when its selected source/specification changes.

The Tools and Applications tabs each own one right-hand sidebar
(`#tools-sidebar`, `#applications-sidebar`) beside the shared left model sidebar.
All three collapse with the native toggle and resize through
`ui/assets/sidebar_resize.js`, which keeps the geometry in per-panel CSS custom
properties instead of Gradio's single global overlap variable.

Applications use copied reviewed tool dependencies inside one native worker.
Only bounded HTTP/ASGI traffic crosses the maintained IPC bridge. No network
capability expansion or ordinary-subprocess fallback was introduced.

Widget CSS is a first-class package member, validated using a deliberately small
scoped grammar and covered by the executable package digest. Tool-local widget
Python, CSS and proposed tests have separate files; authorization records remain
outside their directories. CSS changes require renewed review.

Code help receives the full current Gradio editor value, specification, filename
and I/O contract, plus the widget-context contract where applicable. It has no
execution or editing capability. Its transcript is Markdown, so a fenced Mermaid
diagram renders as an inline SVG through a locally packaged, digest-pinned bundle
with `securityLevel: 'strict'`; rendering is scoped to the helper and no network
fetch is involved. Source/specifications are untrusted model input;
prompt instructions cannot guarantee immunity from prompt injection. Remote
clients still require the session's explicit consent and protected credentials.

Refer to docs/reference for source-bound module/class/method/binding inventory.
Inventory freshness does not establish semantic correctness.

## V5-038: permanent removal and rejected-tool repair

Implemented permanent deletion with explicit, session-bound, one-use confirmation.
Installed dependencies block tool removal, including apps whose source is no
longer valid. Open application and data-operation leases block app removal across
sessions/processes. The service rechecks exact content under a cross-process lock,
revokes grants, then removes the owned package. No recycle bin or cascade exists.
A filesystem failure can leave a partially removed, unauthorized package; external
filesystem operations are not transactional.

Rejected proposals retain their owner-bound code and tests, including code not yet
written. The repair editor requires explicit Save and restart. Both buffers compile
before writes; shared dependencies cannot be changed. New native unittest results
remain provisional until reviewed declarative cases pass independent comparison.
The normal permission-aware executor establishes reusable authorization. Model
proposals cannot write files or grant approval, and rejection does not auto-retry.

New implementation: storage/catalog_lock.py, usage.py and maintenance.py;
application/tool_repair.py; agents/repair_acceptance.py; controllers/catalog.py
and tool_repair.py; ui/catalog_actions.py and tool_repair.py.
Research-only dependency and retrieval recommendations are in
proposals/V5_Dependencies_and_Tool_Retrieval_Study.md. No new dependency runtime,
embedding model or retrieval index is installed by this increment.

## V5-039: catalog-driven native applications

Production discovers canonical approved APIs from Installed Tools Catalog. The
legacy two-counter resolver is retained only for explicit compatibility fixtures.
The application model first proposes bounded connection code and public inputs
from real catalog contracts, then generates a widget for each selected tool that
lacks a reusable approved widget. No reference widget implementation is included
in the prompt.

The canonical public function equals tool_name. Public inputs and return require
Annotated with English metadata; AST extraction does not evaluate annotations.
Scalar JSON types and bounded homogeneous lists are supported. The manager catalog
receives this metadata, not only parameter names. Existing legacy artifacts are
not silently renamed or re-approved. They need an explicitly reviewed migration
before participating in the canonical application contract.

## PUB-001: tool publication boundary

Tool creation and repair write unapproved specification, code and tests only to
owner/operation-bound drafts. After current human acceptance, the host copies
exact bounded bytes into a previously absent public tool directory. Failed or
rejected drafts remain outside the catalog. The policy fingerprint includes this
publication boundary, so prior durable grants require fresh review.

A version-3 package contains the exact selected <tool>_code.py, <tool>_widget.py,
<tool>_widget.css and <tool>_widget_tests.py, alongside maintained app.py,
operation.py, application_context.py, element_ids.py and application_values.py,
plus the generated application_logic.py. application.json describes the strict
file closure, source-derived contracts, public inputs and the widget inventory;
it carries no workflow, edge list or execution order. The compositor, data
executor and value validator must exactly match maintained templates; updating
child manifest hashes cannot authorize rewritten host glue. Model source never
imports on the host. Native imports remain inside AppContainer.

Widgets expose inputs (parameter/component map), output, button and render (raw
result to component value). The model chooses the actual Gradio components and
callback implementation. Context assigns readable unique IDs, including custom
parameter roles, while structural Groups receive no IDs. Duplicate aliases across
scopes are resolved centrally. CSS is scoped per tool and rebound to each widget
instance within the staged private stylesheet. Outputs use read-only scalar
controls and tables; the final interface does not display a raw result JSON.

A right-click on a widget control opens the style window (V7-076), which edits
border radius, border width, border color, background color, font family and font
size in the base scoped block of `<tool>_widget.css`. Scoped stylesheets are
excluded from the application identity: their closed grammar is the gate, so a
style edit keeps the approval valid while capture still verifies the declared
member hash.
After a style-only save, the served `application.css` uses four extra widget
attribute selectors to outrank Gradio's prefixed embedded startup copy on a
reloaded or separate web page. The running preview uses inline important
declarations and applies caption font rules only to caption text, even when a
Gradio label wraps a value input.

Only newly proposed widget unittest modules run in a separate native process.
Previously approved tool unittest suites are not copied or rerun by composition.
Widget test success is provisional: the host separately compares approved tool
cases through a native data call and actual browser interactions, including repeated
combined execution and ID uniqueness. Expected values stay outside the child.
A composed application needs compatible reviewed value cases; otherwise verification
fails explicitly rather than inventing expected results. Finite cases do not prove
universal correctness. General package testing currently supports scalar widget
inputs and scalar/list results, not arbitrary Python classes or third-party tool
runtimes. Unsupported contracts are rejected before execution.

Activity formatting removes decorative pipe frames while preserving internal
operators, indentation, verbose messages and raw captured diagnostics. Escaped pre
markup prevents nested generated Markdown from breaking the activity panel. Dark,
thin scrollbars follow the parent application's palette.

## Actual four-tool reuse evidence

The disposable GUI on 7879 created/reviewed a calculator, an English vowel counter,
a whitespace word counter and a seeded random draw. After final security-policy
revalidation, Playwright issued new ordinary user queries. Calculator subtraction
91 - 17 returned 74.0; Building reliable tools returned 9 vowels and 3 words;
eight draws from -4 through 4 using seed 11 returned [3, 4, 3, 3, 4, -1, -2, 4].
Each comparison used a maintained independent expectation, with explicit assertions
that no approval_requested or generated_tests_provisional_passed event occurred.
The calculator check included a page reload after a disposable-server restart.
See v5-039-reuse-*.json in docs/reports. This establishes these finite reuse cases;
it does not establish arbitrary tool semantics. The four-widget application subsequently passed the separate native/browser gates; see reports/V5_039_DELIVERY_REPORT.md for recovery provenance and limits.


## V5-041 workflow binding contract (removed)

The bounded declarative graph, its binding resolver and its reviewed-case search
were removed together with the schema-2 route. No graph module, binding file, node
definition or workflow definition remains in the maintained tree, and no package
validator accepts `binding_version`. Schema-3 connection code under V5-043 is the
only application composition contract. The removal record is in V7_INCIDENTS.md.


The actual model transport preserves binding-field presence through the domain
serializer. Its provider grammar has five exclusive shapes, matching host source
rules. Validation launchers can inject a LocalModelClient factory through
get_default_ui; timeout remains 120 seconds by default and is explicitly bounded
to 600 seconds. This keeps runtime configuration at the composition root and
avoids process-global timeout patches or changes to another GUI instance.



## V5-043 generated connection code

The default catalog creation path uses CrewAI sequential tasks to generate and
review ApplicationCode: public input schemas, a presentation-only widget inventory,
Python connection source and notes. A second crew generates only missing widgets,
with explicit context from the completed code task. Approved unchanged widgets and
tool bytes are reused. Agents have no execution tools or approval authority; both
verbose output and technical events remain owner scoped. The local client remains
pinned to qwen3-coder:30b with bounded waits and no automatic retry/fallback.

Version-3 packages contain application_logic.py with run(payload, call). Ordinary
Python variables connect real results to later calls. No workflow, order, bindings
file, graph conversion or graph interpreter is used on this route. The inventory
only maps widget instances to approved tools. The maintained native operation
adapter bounds calls to one per declared instance, validates public inputs, tool
arguments and results, and records observed arguments for read-only widget controls.
A portable maintained value validator is shared with host contracts and hash-bound
in the package. Generated code is never imported on the host; AppContainer remains
mandatory. Generated code has no model dependency when reopening or executing.

ApplicationReview exposes connection code and a virtual application_acceptance.json
in the existing file editor. Cases may start with reviewed catalog proposals, live
outside the child package and must be independently completed/reviewed before approval. Saving code or cases
revokes the previous grant. Native execution and repeated browser callbacks compare
against host-held expected values. New widget tests are provisional and run only
natively; approved old tool tests are not rerun. Opening verified installed apps
checks exact current dependencies without regenerating code or repeating old tests.

Only version-3 packages are accepted; version-1/2 manifests and their binding
validators are rejected explicitly. See specification 043 for acceptance criteria
and the current verification report for measured evidence; framework doubles do
not prove model quality or native isolation.


Schema-3 layout control IDs are derived from manifest widgets through ElementIds;
the editor and layout storage share this exact allowlist. Structural groups remain
unidentified; editing targets individual controls. Toolbar IDs remain excluded.
See [V6-044](specs/044-widget-layout.md).


## V6-045: independent acceptance proposals

Schema-3 drafts now propose bounded reviewed catalog cases through inert source
matching, retain unresolved expectations and open an editable JSON review. Invalid
cases produce persistent guidance before verification. Explicit review and native
comparison remain required. See [design, incident and verification](specs/045-proposed-acceptance-cases.md).

## V7-054: acceptance approval readiness

The Tools review button is presentation-only and begins disabled. It is enabled
only for the current `pending_review` acceptance proposal after the maintained
contract parser accepts the edited text. Text edits and replacement requests
recompute that display state; the existing owner-bound backend validation and
human-approval boundary still decide authorization. See [requirements and
evidence](specs/054-acceptance-approval-readiness.md).


## V7-055: explicit host dependency recovery

The Applications backend checks the static host registry before approval can
cross into native/browser verification. A missing registered component leaves
the reviewed candidate pending and exposes its maintained explanation only to
that owner. The user must click the explicit install control; the controller
then invokes the injected, immutable requirement command and rechecks its
postcondition. Successful repair does not replay approval, execute generated
content or change Tools/apps: the user must select **Approve and verify** again.
Generated artifacts, model output and browser values cannot define requirements,
commands, package sources or installer arguments. The initial registry contains
only Playwright Chromium; arbitrary third-party provisioning remains unsupported.
See [V7-055](specs/055-host-dependency-recovery.md).

## V7-046: public input layout

Schema-3 public inputs are created inside the editable canvas and their declared
IDs join the shared layout allowlist. Existing callbacks, editor events, geometry
bounds and approval invalidation remain in force. See [scope, cause and checks](specs/046-public-input-layout.md).

## V7-064: actionable catalog dependency diagnostics

`Re-verify selected app` and `Load selected app` name the missing tool approval and
the recovery step instead of only the exception type, and a missing application
dependency names the tool with its maintained skip reason. A refused shell open
reaches the maintained modal. Approval behaviour, durable-record revocation and
both policy digests are unchanged. See
[scope, contract and evidence](specs/064-catalog-dependency-diagnostics.md).

## V7-065: catalog folder window above the browser

`View in explorer` raises the Explorer window of the installed Tools or
Applications folder above AgentiX and gives it keyboard focus, without leaving it
always-on-top. A refused foreground change is logged and never fails the completed
open; ownership, root validation and linked-folder refusal are unchanged. See
[scope, contract and evidence](specs/065-explorer-window-foreground.md).

## V7-063: catalog explorer buttons and per-tool handle colors

`View in explorer` opens the installed Tools or Applications folder from a
server-resolved root for the owning session; the browser never supplies a path
and linked or missing folders are refused. In Edit, move handles are tinted per
tool group so related widgets are recognizable; the tint is re-randomized on each
Edit entry, applied only to the handle and never persisted. See
[scope, contract and evidence](specs/063-catalog-explorer-and-tool-colors.md).

## V7-062: widget visibility outside Edit

Each editable canvas control owns a small checkbox that is rendered only while
Edit is active. Checked keeps the control visible after leaving Edit; unchecked
hides it with `display: none`, so Gradio callbacks and the Status indicator keep
working. Visibility is persisted as the optional `hidden` list of the same
version-1 layout record, validated against the shared control allowlist. The
toolbar stays outside that allowlist. See [scope, contract and evidence](specs/062-widget-visibility.md).


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

## V7-056: stale installed-application re-approval

A record whose host policy fingerprint moved stays visible in the Installed
applications catalog as `(re-approval required)` instead of disappearing.
Loading it restores the exact installed bytes and stored review, marks the
candidate unapproved and reuses the existing review, approval and independent
native/browser gates; publication then replaces the protected record atomically
instead of creating a second folder. Re-verification repeats those gates on the
installed bytes and reseals only after they pass. Rejection warnings name the
application by opaque id and bounded name, with one summary event per listing.
See [scope, design and evidence](specs/056-stale-application-reapproval.md).

## V7-050 launch readiness

Infrastructure separates strict provisioning convergence (Test-IacDeployment) from
operational readiness (Test-IacLaunch). The latter reuses planner rules over a copied
observation, relaxing only Ollama version equality while requiring its loopback API
and approved model. Manual GUI/CLI launch emits version warnings without provisioning.
See [V7-050](specs/050-ollama-launch-compatibility.md).

## Independent tool retrieval (RAG-001)
The optional agentix.retrieval package owns a dedicated Chroma index and injected local Ollama providers. It combines cosine candidates with BM25 through reciprocal rank fusion. It is not wired into current agents, catalog scanning or execution approvals. Retrieval metadata never grants execution; future integration must resolve current catalog identities and eligibility. See [retrieval contracts](specs/051-tool-retrieval.md) and [usage](TOOL_RETRIEVAL.md).

RAG-008 centralizes retrieval limits, algorithm parameters, storage version and diagnostic units in the internal retrieval.policy module. Providers, contracts and ranking use these definitions without changing composition or persisted schema.

RAG-009 adds an optional DescriptorSource contract and CatalogToolSource adapter around the current GUI ToolCatalog root. A dedicated source-bound Chroma collection reconciles initial load and every search; no watcher, GUI callback wiring or execution permission is introduced. Source identity prevents cross-catalog pruning, and incomplete scans fail the operation. See specs/051-tool-retrieval.md.

## GUI application candidate selection (RAG-010)
Startup initializes GuiToolRetrieval from the same runtime catalog. One index-access lock coordinates owner-private providers; CandidateState holds per-session preview revisions. The Applications button first searches; the right-side candidate panel adjusts limit and requires explicit acceptance. SelectedToolRegistry constrains the existing pipeline and repair dependency checks to the accepted approved bytes while preserving adapter roles. Application review and native verification remain independent. See specs/052-application-tool-candidates.md.

RAG-011 replaces candidate HTML with a CheckboxGroup. Browser values are untrusted IDs; CandidateSelection validates them against server-owned snapshot eligibility and fingerprints. Description edits leave the preview unchanged, with stale-description rejection at acceptance.


