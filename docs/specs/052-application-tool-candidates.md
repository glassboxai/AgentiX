# RAG-010: GUI application candidate selection

The description-edit and read-only presentation behavior below is superseded by [RAG-011](053-candidate-checkboxes.md).

Status: implemented; verification is recorded in reports/RAG_010_GUI_CANDIDATES.md.
The user approved startup loading, candidate preview, repeated limit searches,
explicit candidate acceptance, current approval checks and safe logging.

## Observable requirements

| ID | Requirement | Acceptance |
| --- | --- | --- |
| RAG-010-01 | Load/synchronize the installed GUI catalog when the application opens | Bootstrap initializes the injected retrieval service once before constructing the view |
| RAG-010-02 | Keep the GUI available after index/model failure | Safe startup status; a later Generate application action retries without model pulls |
| RAG-010-03 | Generate application first searches the exact description without generation | Candidate search audit exists while generation audit remains empty |
| RAG-010-04 | Place candidate list and integer limit spinner below Delete selected application | Real DOM geometry, unique panel ID, readable names/descriptions, initial 5 and bounds 1..100 |
| RAG-010-05 | Repeat search when the user changes limit | Actual up/down keyboard spinner events forward 5, 4 and 5 and refresh the list |
| RAG-010-06 | Accept candidates and generate uses exactly the displayed server-owned scope | One-use revision plus query/limit/owner checks; generation receives only accepted dependencies |
| RAG-010-07 | Preserve current tool approval and exact-byte checks | Changed, unavailable or unapproved tools block acceptance; application review/native gates remain separate |
| RAG-010-08 | Prevent stale and cross-session publication/acceptance | Description edits, superseded failures, owner close, foreign tokens and replay tests |
| RAG-010-09 | Record the complete new flow without request/source bodies | Startup, invalidation, search/rejection, limit/count/rank, acceptance, generation scope, timings and safe error types |

## Composition and ownership

Production get_default_ui constructs one GuiToolRetrieval and initializes it from
runtime.catalog before view construction. The default factory uses local
nomic-embed-text:latest and qwen3:14b through the already approved adapters and
source-bound data/tool_registry. No agent model or Ollama service is restarted.
ChromaDB 1.5.9 is now a direct GUI runtime dependency, already present in the
managed environment and existing hashed runtime lock; no installer Apply is part
of this block.

The GUI service serializes index operations inside its process. Startup clients
are temporary; each application session retains its own retriever/providers in a
RetrieverHandle. Selection, revisions and accepted dependency scope live in that
owner's ApplicationState. The standalone index writer must not run concurrently
from another process; cross-process coordination remains outside this block.

Startup readiness describes index synchronization, not guaranteed model health.
An unchanged index can load without inference. Missing dependencies, unreadable
catalogs or failed embedding calls yield a safe unavailable message. A user search
retries; errors never substitute the full catalog or start generation automatically.

## UI and data flow

Generate application clears the previous preview and calls ToolRetriever.search
through the GUI service with the description unchanged and the current limit.
Search does not require an application name; acceptance applies the existing name
and uniqueness validation before generation. The panel shows every returned
candidate in order with name, bounded first-line description, score and current
eligibility. Unavailable entries stay visible and block acceptance; no invisible
subset is substituted.

The spinner is an integer Number with shared retrieval policy bounds and step one.
Every user change queues another search. Query value changes invalidate the preview
without generating per-keystroke model calls. The value-change event covers paste
and complete replacements, not just key handlers. Gradio queues serialize candidate
searches, while server revisions discard obsolete successes and failures. Controls
are disabled during active work or pending application review.

Candidate text is escaped before HTML rendering. Component-local CSS gives names,
descriptions and eligibility separate readable blocks inside Gradio's isolated HTML
content. A Column supplies one unique panel ID, avoiding Group's duplicate DOM ID
behavior in the installed Gradio version.

Accept candidates and generate submits the application name, current query/limit
and a revision ID. It never submits authoritative tool objects or editable tool IDs.
The server verifies ownership and exact preview identity, consumes it once, then
resolves current approved source bytes. A stale, empty, changed or ineligible scope
requires a new explicit search. Failed approval storage is logged safely and shown
in the persistent message dialog without exposing provider exception bodies.

## Existing generation and security contracts

SelectedToolRegistry wraps the existing approval registry and supplies only accepted
tools to the existing pipeline. It preserves adapter role keys for legacy callers
and checks SHA-256 of current approved code against candidate source fingerprints.
Its dependency recheck compares current selected ApprovedTool snapshots; unrelated
catalog additions cannot expand the set. Repairs of newly generated proposals keep
this accepted scope and original query. Changed selected source/grants require a
new selection instead of silently broadening the dependency set.

The candidate button authorizes generation only. Source/test review, independent
acceptance cases, application approval and native isolation are unchanged. Existing
saved-application and trusted non-UI backend entrypoints retain their prior contracts;
the GUI Generate callback no longer binds directly to immediate generation.

Closing an owner invalidates outstanding search revisions. Errors, logs and outputs
remain owner-bound. The new code never imports or executes generated tool Python,
changes approval flags, adopts grants, downloads models or scans generated_tools.

## Verification boundaries

Default tests replace provider/generation boundaries and use independent temporary
fixtures. Explicit frameworks checks construct real Gradio components and invoke
registered callbacks without a model/server. Playwright drives real controls on
separate owned loopback servers with explicit retrieval/generation doubles. These
checks establish the new interaction and dependency scope; they do not establish
real application-model quality or native execution isolation.

Legacy browser fixtures use an explicit retrieval double for their historical
function aliases; this does not extend production canonical-catalog discovery.
No live GUI is restarted. The source change takes effect on the next normal launch.

Publishing reviewed tool revisions also invalidates a candidate-bound proposal. The prior draft stays on disk, but its active server candidate is cleared and generation requires a fresh search/acceptance. The legacy revision path remains unchanged for proposals without a candidate scope; it cannot broaden a candidate-bound generation to unrelated installed tools.
