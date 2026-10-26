# IAC-001 infrastructure integration

Native Windows desired state and operations are documented in ../infra/README.md.
Source references now include PowerShell AST function/variable inventories. Application
Settings adds explicit server_port/open_browser and an absolute tools_root override;
normal construction remains side-effect free. The current source namespace and version
identity remain agentix / 3.0.0. See reports/IAC_IMPLEMENTATION.md for verified outcomes.

# Current version: AgentiX v3

The current English architecture and responsibility map is ARCHITECTURE_QUALITY.md. The complete maintained Python inventory is reference/README.md; regenerate it after source changes and verify --check. The release scope and limitations are reports/V3_ENGINEERING.md. Historical technical notes below remain evidence of earlier stages.

# Agentix technical architecture

UI-013 further aligns the presentation with the inspected local reference:
Inter typography, square corners and 20px square native checkboxes with dark
unchecked fill, cyan checked fill, visible keyboard focus and a forced-colors
fallback. A fixed HTTPS link to The Glass Box AI Project follows the final header
description. No remote resource is loaded by adding this ordinary link. Approval
semantics/defaults, agent behavior and execution evidence are unchanged.

## AgentiX presentation (UI-012, 2026-10-20)

`ui/branding.py` loads only maintained local logo/CSS resources. Shared launch
options apply styling/favicon to normal and disposable launchers without exposing
an arbitrary filesystem root. The header uses the approved AgentiX identity and
three-line description. Inter is resolved locally with Arial/sans-serif fallback;
there is no external font request. Decorative interface emoji are removed.

`ui/presentation.py` provides bounded, escaped, deterministic display functions.
The GUI renders host result records as fields/tables and retains the technical
record in a collapsed disclosure. It does not execute text, invent observations
or replace ledger authorization. Literal decoding has size/node/depth limits;
unknown output falls back to escaped text. Explicit euro context enables monetary
formatting without rounding away finer rates. Existing CLI/agent output remains
unchanged. The catalog's original text is folded only at the UI boundary.

Validation stage/counts remain visible above a bounded list of per-case
disclosures. Expected/observed data, provisional output and Python tests remain
available on demand; mandatory review and editable approval IDs are preserved.
See specification 012 and `reports/UI012_PRESENTATION.md` for verification.

Updated: 2026-10-19 after approved refactoring/security/acceptance work and specification 010 communication changes. This describes the implemented application structure. It documents Agentix's infrastructure, not the contents of the excluded project `generated_tools/` directory. Current communication and supervised 30B results: `reports/COMMUNICATION_LIVE30B.md`.

CLI-001 keeps terminal input on the main thread and runs the shared workflow in a daemon worker. It services directory/file and mandatory acceptance requests through the existing coordinator, preserves request identity during editing and prints independent host verdicts after the model response. EOF/Ctrl+C closes permissions; it cannot forcibly stop model I/O. Review text escapes terminal controls without changing approval content. See `ACCEPTANCE_REVIEW.md`.

E2E-001 uses a separate temporary real Gradio server and Playwright with trusted workflow/execution fixtures, no model and no production storage. It validates browser controls, session separation, acceptance edits/rejection and persisted file edits. It does not certify native isolation or model quality. See `BROWSER_TESTING.md` and ADR 0006.

LIVE-001 subsequently exercised the real model-driven creation workflow with the reviewer operating the GUI. Three sampled attempts did not complete tool creation/execution. The review exposed original-requirement loss at the creation boundary, missing persisted implementation before the tester stage, insufficient proposed invalid-input tests and a no-output Gradio callback warning. LIVE-FIX-001 subsequently corrected original-requirement preservation, stage advancement and the no-output callback. The two deterministic defects are now normal passing regressions; actual model output and manual review evidence are in `reports/LIVE_HITL.md`. Passing deterministic E2E checks must not be described as successful real-model tool creation.

## Purpose and preserved behavior

Agentix uses a local Gradio interface or CLI with CrewAI and Ollama to reuse or create tools. The manager receives a query and AST catalog, either answers through an existing tool or requests the original Architect -> Coder -> Tester pipeline, then attempts final execution. REF-003 established the component structure. SEC-005 now adds owner-bound browser sessions, identified approvals, fail-closed creation decisions and correlated diagnostics. Task/context ordering, valid tool results, approval editing and loopback launch parameters remain.

Prompts do not enforce security. Native Windows AppContainer now isolates generated Python, and a host-owned ledger gates execution against current test-service observations. Unittest reports remain untrusted and provisional. Final authorization additionally requires explicit human-reviewed cases and deterministic host comparisons; see the limits below and `KNOWN_ISSUES.md`.

## Package and dependency direction

Application implementation lives in `src/agentix/`. Root scripts provide checkout compatibility and lazy runtime access. `_agentix_path.py` adds the checkout's src directory to the import path; imports otherwise perform no runtime initialization.

| Module | Responsibility and contract |
| --- | --- |
| `settings.py` | Frozen Settings loaded from an explicit environment mapping or the process environment; construction does not create storage |
| `contracts.py` | Structural SecurityBoundary protocol used by services and controllers |
| `paths.py` | Resolved containment and Windows component policy; raises SecurityViolationError |
| `approvals.py` | Owner-specific locks/events, unique expiring request IDs, single-use decisions, defensive snapshots and cancellation |
| `storage.py` | ArtifactStore, approval-aware UTF-8 persistence and final Python syntax validation |
| `security.py` | Compatibility SecurityManager class facade composing path, approval and storage behavior |
| `catalog.py` | ToolCatalog AST inspection and existing Markdown rendering, without executing source |
| `execution.py` | ToolExecutor, JSON/evidence validation and execution of exact verified bytes in an isolated child |
| `testing.py` | TestRunner, approved persistence, isolated unittest observations and incident recording |
| `sandbox.py`, `windows_process.py` | Fresh standard-library runtime, AppContainer provisioning, native handle/job lifecycle and finite resource limits |
| `sandbox_worker.py` | Trusted disposable child entrypoint; reports remain untrusted because generated Python shares the interpreter |
| `verification.py` | Separate provisional observations and host-accepted contract/function bindings; current owner/run/content checks and independent non-executing syntax checks |
| `acceptance.py` | Strict bounded declarative contracts, mandatory human review, host comparisons, per-case verdicts and current validation status |
| `tools.py` | Framework-free ArtifactTools operations composed with executor and runner |
| `adapters/crewai.py` | Explicit tool registration/signatures, owner-context restoration in provider threads, role definitions and AgentSet; verbose agent output enabled alongside technical events |
| `orchestration.py` | Orchestrator with injected agents, factories and catalog callable |
| `ui/state.py` | Independent ExecutionState histories and locked ConsoleThoughtsCapture; construction does not replace stdout |
| `ui/controller.py` | UiController callbacks, worker state, activity rendering and approval editor interaction |
| `ui/view.py` | Session-aware Gradio events, trusted Request injection, server-side token State and browser-snapshot approval ID |
| `ui/sessions.py` | Bounded owner/token registry, expiration, close hooks and owner-checked callbacks |
| `decisions.py` | Bounded exact creation JSON contract and explicit validation errors |
| `diagnostics.py` | Payload-free correlated events, ContextVars and host stdout routing |
| `bootstrap.py` | Explicit process setup and service composition, lazy compatibility runtime/model/tools/UI |
| `cli.py` | Existing interactive input loop, exit aliases and failure recovery |

Services do not import root compatibility modules. Framework imports are local to startup/adapter calls, not service-module import time. Test fixtures pass dependencies directly instead of replacing whole application modules.

## Settings and startup

Settings retain the checkout-relative artifact root, model `ollama/qwen3-coder:30b`, endpoint `http://localhost:11434` and temperature 0.2. OLLAMA_MODEL and OLLAMA_BASE_URL overrides retain their meaning. The src package location does not move user storage.

Explicit production startup applies existing logging/telemetry policy, best-effort CrewAI tracing suppression and an idempotent Rich tracing-panel filter. It creates the configured storage root and constructs services, model, registered tools and agents without running tasks. The UI view is constructed only on request. Stdout capture is installed during UI launch and restored if launch fails or returns.

Importing config, security_manager, custom_tools, main or app does not construct a model/agent, create storage, build widgets, modify environment/stdout or patch Rich. Requesting a lazy runtime attribute is an explicit initialization request. Catalog-only access does not construct agents.

## Compatibility entrypoints

`python app.py` retains queued Gradio launch on `127.0.0.1:7860`, the same theme and browser-opening request. `python main.py` retains the interactive CLI. Existing SecurityManager/exception exports remain available; tools, agent objects, local_llm, callbacks and Blocks are lazily available through compatibility modules. A running process needs a restart to load changed source; automated tests do not restart it.

## Paths, approvals and persistence

Path policy rejects traversal, drive/UNC/rooted paths, invalid Windows components, reserved devices, alternate streams and trailing dot/space aliases. Resolved paths must remain inside the root and intended tool; tool-directory aliases are rejected. Relative nested artifact paths remain supported. Revalidation after approval detects changed destinations but cannot eliminate hostile filesystem races.

The browser receives an independently owned coordinator, provider client, role set and controller. Directory/file approvals remain separate, with a 300-second default timeout. Each request has a server-generated ID, owner and monotonic deadline. Resolution requires both identifiers and accepts one valid decision; wrong/missing/expired/duplicate responses cannot change it. A live slot cannot be overwritten. Unload/close denies unresolved and new requests. Edited text, including empty text, and defensive snapshots remain supported. The legacy CLI facade retains a separate legacy coordinator.

ArtifactStore validates final approved Python before opening the destination. Append validates existing plus approved text. Both requested and resolved suffixes are considered so confined aliases cannot bypass compilation. Invalid edits preserve existing files. Compile checks syntax without execution; valid writes retain non-atomic persistence semantics.

## Tool operations and orchestration

ArtifactTools composes storage services, WindowsSandbox and one VerificationLedger per runtime. TestRunner saves final approved test edits and stages exact code/test bytes in a disposable runtime. ToolExecutor validates JSON arguments and public function names before execution, requires matching ledger evidence, and passes the verified byte snapshot to an isolated child. It never imports generated code in the host. Missing isolation, empty/all-skipped/expected-failure suites, child failures and changed artifacts deny execution. Failures record an incident. Failure details are bounded child output, not trusted instructions.

The new `Verify Existing Tool` manager action re-runs stored tests without changing code/tests. Evidence is in memory, bounded to one tool and tied to owner, operation and SHA-256 of length-framed code/test bytes. A new query, failed attempt, restart, source edit or test edit invalidates prior trust. The final manager stage requires current human acceptance independently of the creation crew's text. Generated unittest success alone never authorizes execution. The new `Submit Acceptance Cases for Human Review` tool proposes bounded JSON cases (purpose, function, inputs and exact/approximate/error expectations). The owner sees the generated Python tests and provisional output, can edit case data and approve or reject. File auto-approval cannot approve this request. IDs, deadlines, cancellation and owner checks remain mandatory. Rejection/expiry prevents automatic reprompting during the same operation. Direct plaintext manager answers remain model output, not certified execution evidence.

WindowsSandbox copies only CPython executable/DLLs/standard library, a trusted worker and explicit inputs. It excludes site-packages and never copies the project. A unique AppContainer SID receives read/execute access to staging, with no network capabilities or inherited host secrets. A suspended child's token is checked and its Job Object configured before resuming. Only selected standard handles inherit. Default job bounds are 512 MiB memory, eight processes, 30 seconds wall time and 256 KiB combined output. A pipe reader drains output while enforcing its bound. Closing/terminating the job also terminates surviving descendants; temporary staging and the AppContainer profile are removed. Provisioning/copy time is outside the child deadline. No Docker, VM, administrator setup or host-execution fallback is used.

This initial runtime supports standard-library functions and unittest. Third-party packages are unavailable. Windows resources already accessible to AppContainers and the profile's private writable storage remain governed by OS policy. There is no disk quota, VM kernel boundary or security certification. Tests cover a private host file, controlled loopback listener, read-only staging, environment secrets, timeout, memory, process count, bounded output and normal cleanup; they cannot establish absence of all escape techniques.

Unittest shares an interpreter with generated code and can be manipulated; its successful report is explicitly provisional. After human review, AcceptanceEvaluator runs each approved case in a fresh isolated process and provides only implementation bytes, function name and input data. It never sends expectations, the contract, unittest source or approval metadata to the child. The child returns typed JSON values or an exception-type observation. Maintained host code validates the schema and independently compares results; a child claim that a case passed is irrelevant. Serialization/process failures cannot count as expected function exceptions. No eval, pickle or generated assertion executes in the host.

Authorization binds the approved canonical contract SHA-256, evaluator version and covered function names to the owner/run/source/test identity. Executing another function is denied. Changes observed during review/evaluation, failed rechecks, cancellation or a new operation invalidate authorization; observed changes cannot resurrect old approval after files are restored. Expected and observed values plus per-case verdicts appear in a separate session-owned status panel, escaped as text. Contracts/receipts are runtime memory only; new queries/restarts require review again.

Finite human-approved cases establish agreement for those observed inputs only. They do not prove all-input correctness, that a malicious implementation followed a particular internal path, or that the approved requirements are right. Reviewers remain responsible for test relevance, expected values and numeric tolerances. Interactive review adapters are available in Gradio and the CLI. CLI-001 runs the shared workflow in a daemon worker while the main terminal thread services owner-bound review snapshots and displays host validation status. See `ACCEPTANCE_REVIEW.md`.

ToolCatalog preserves sorted entries, public top-level synchronous function names, positional parameters and first docstring lines; parse errors are reported per entry. It is called only at runtime or against temporary test fixtures during verification.

The CrewAI adapter preserves public tool signatures and creates role objects on demand for each session. Manager creation requires one full raw/fenced JSON object with exactly action, tool_name and purpose. It rejects malformed/duplicate/extra fields, unsupported actions, unsafe/noncanonical names, blank/nontext purpose and oversized responses. Invalid output raises DecisionValidationError without starting creation; arbitrary fallback and name normalization are removed. Ordinary valid text answers remain accepted. Creation output alone cannot grant evidence or trigger final execution; only provisional observations followed by human-approved host comparisons can authorize final execution.

## UI, diagnostics and remaining limits

UiController owns one session's state, lock, activity and callbacks. One workflow is accepted at a time per owner; its assistant-message index remains stable even if a busy submission adds a wait message. Returned histories are defensive copies. Polling loads editor content once per request ID, including a new request for the same filepath.

SessionRegistry binds an opaque server-State token to the Gradio request session hash. Diagnostic UUIDs are separate from access tokens. Gradio session hashes provide routing, not account authentication. The hidden non-stateful approval textbox carries the ID associated with the displayed editor; the server revalidates owner, ID and expiry. A client cannot approve a foreign session by substituting a token into a different owner's State. Default capacity is 128; inactive entries expire after 1800 seconds on registry activity. Unload, State cleanup and expiry close the owner; lost unload notifications are not guaranteed immediate. Active Python is not forcibly interrupted.

Application logs use fixed events with session/run/request IDs, error type and optional line number. Full queries, source, model output, exception bodies, paths and session access tokens are excluded from those routine events. Agent/Crew verbosity is enabled at the user's explicit request. Both verbose SDK messages and technical events reach the owning session. Context-local routing and tool adapters restore diagnostic ownership without per-worker stdout replacement. Activity reassembles fragmented writes into logical lines, retains 256 completed lines plus one bounded 4096-character partial line, and exposes at most 256 lines. If a legacy Windows console cannot encode a verbose icon, only the mirrored console copy is escaped; the GUI retains Unicode. Main UI startup and the supervised launcher share the same stdout-routing context and restore the original stream on exit. Arbitrary tool prints and third-party logs are not comprehensively sanitized; persistent log rotation remains separate work. Generated child output is bounded by the native backend; arbitrary provider output is still not comprehensively sanitized.

## Verification and maintenance

`reports/HUMAN_ACCEPTANCE.md` contains current evidence. `ISOLATED_PIPELINE.md` is the preceding execution-isolation snapshot. `SESSION_SECURITY.md` and `REFACTOR.md` are historical snapshots for their respective changes. The default suite runs offline with explicit fake framework/model factories; artifact fixtures remain outside the excluded project directory. Separate opt-in tests construct real CrewAI schemas/Gradio widgets and exercise Gradio process_api for two server-side sessions, stale IDs, foreign-token rejection and unload, without a model, HTTP server or existing artifact access. The separate `windows_isolation` marker exercises the actual OS boundary without a model, server or project artifact access; default tests use a clearly labelled OS double. Ruff verifies active source formatting/import/code rules. No coverage percentage, static type-checker certification, live agent quality or installer validation is claimed.

Keep this architecture, REF-003, incident/change records and installation instructions synchronized with implementation changes. Historical baseline/fix reports retain their original evidence and are labeled snapshots.


## Approved creation-stage corrections

Creation now runs one Crew per role with a host check between stages. The original query accompanies the manager purpose; code/test tasks receive actual approved persisted specification/code. Maintained storage issues bounded owner/operation/write-ID/SHA-256 receipts after checking actual bytes against the approved candidate. Stage reads require fresh matching receipts, bounded nonempty UTF-8 and Python syntax validity without import. Acceptance rechecks approved source/specification after testing and revokes evidence if either changed. This is not crash-atomic persistence or universal correctness. See specification 009 and ADR 0007.

The application model is `ollama/qwen3-coder:30b`, as required by the user. The user approved technical events alongside original verbose messages, shared system policy, complete handoffs and a resumed supervised functional run. Specification 010 records this block. Domain queries in the resumed test are English, as subsequently requested. Earlier pause details remain historical evidence in `reports/APPROVED_CREATION_STAGES.md`; current outcomes are recorded separately.


The explicit verbose setting preserves the installed CrewAI renderer's agent, task, tool-result and final-answer messages rather than substituting technical summaries. SDK and activity-tail size limits still apply. Verbose console messages can intentionally contain workflow text; fixed-field diagnostic events remain payload-free. No comprehensive redaction of arbitrary third-party verbose output is claimed. The restored display was verified with real SDK event rendering and two concurrent controllers without invoking a model. See `reports/VERBOSE_ACTIVITY.md` for that display-only verification.

## Shared workflow and observed final results (specification 010)

UI-VALIDATION-001 subsequently removes the contract digest from the user-facing
validation summary. It remains in internal acceptance/ledger evidence. The GUI
continues to show verification state and expected/observed case results; verbose
agent output and diagnostic events are preserved.

USER-PROMPT-001 was exercised through the separate GUI with qwen3-coder:30b on
2026-10-20 using an English domain-only electricity query. After manual review
corrections, eleven provisional tests and sixteen host-compared acceptance cases
passed. Final isolated execution for 350 kWh returned EUR 67.50 with tier costs
EUR 12.00, 18.00 and 37.50. The current final renderer still displays a raw
execution record; a friendlier explanation remains a presentation limitation.
See `reports/USER_PROMPT_LIVE30B.md`; finite reviewed cases do not establish
universal correctness or autonomous generation quality.

`agentix.workflow_policy` supplies English workflow obligations through every
agent's backstory, which CrewAI includes in its system prompt. Architect/coder/QA
responsibilities remain separate; only the manager performs final execution.
Users describe domain requirements without repeating engineering instructions.
An empty catalog requires creation, not verification of an invented tool.
It uses a separate manager instance without tools; the regular manager retains
verification and execution. Conventional filenames are supplied by the catalog.
Specification/code saves, QA acceptance and final execution return directly to
host stage gates. The reuse manager's acceptance registration remains nonterminal
so it can execute afterward. No temporary mutation of shared agent tools is used.

Acceptance proposal text is bounded before display. Invalid generated JSON/schema
data can be manually corrected with an explicit warning; only the approved edited
JSON can pass strict validation and enter host evaluation. Oversized proposals,
invalid human edits and changed artifacts never grant authorization. No automatic
model retry follows a rejected review.

The final manager receives current host-accepted function signatures (AST only),
the reviewed declarative contract and its digest, together with the original
query. Approved cases are examples of finite verification, not execution arguments
to copy blindly. Artifact receipt gates preserve approved stage edits.

The executor records successful isolated calls in the owning verification ledger.
Each observation binds current owner/operation, exact implementation/tests, accepted
contract, authorized function, JSON arguments and the bounded child result. Failed
attempts clear earlier observations. Revocation, closed sessions, source changes or
operation changes prevent their use. Final tool responses display observed call
arguments and results instead of trusting the manager's completion prose. A missing
call returns `EXECUTION_NOT_VERIFIED`. Ordinary conversational replies without tool
activity remain model text and are not execution evidence. A process observation
does not establish universal correctness or honesty of malicious child code.


## SEC-LLM-001 / UI-MODEL-001 (2026-10-24)

The native left sidebar contains model settings and Authorization & Test Review. Persistent nonsecret profiles use Windows Credential Manager references; each session still starts with local Ollama and must consent before remote task transfer. See MODEL_CONFIGURATION.md for operation, LLM_SECURITY_2026.md for security boundaries, and the generated source reference for modules, classes, methods and variables. The CLI shares query/work budgets but does not offer this GUI profile editor.

## Sidebar refinement (2026-10-25)

UI-MODEL-002 matches the reference secondary-button palette and hides API key and external-transfer consent for local Ollama. Explicit Playwright clicks verify all five model/profile controls, including discovery of new options, active injected client identity, cross-session persistence, update and deletion. See reports/SIDEBAR_017_VALIDATION.md for evidence and the distinction between real browser/framework/native-vault checks and doubled model services.

## PROFILE-001 (2026-10-25)

Saved profiles includes local Ollama and external providers. Local records contain no active credential reference and do not access the vault. Fixed-code diagnostics identify key format, native credential and metadata failures; Refresh retains the last save error. See MODEL_CONFIGURATION.md, specs/018-unified-profiles.md and reports/PROFILES_018_VALIDATION.md. The new native integration test joins actual Gradio callback routing, temporary profile storage and Windows Credential Manager without real API keys or inference.

## Reviewed reuse policy

`reuse_policy.computation_only(code)` parses exact source without importing it and accepts an explicit AST/call/import vocabulary for unattended computation. Unknown syntax, file/network/process libraries, private introspection and dynamic dispatch require exact-call approval. `VerificationLedger.prepare_reuse(tool_name)` restores current-query acceptance only from this session's successful host-published grant after owner/lifecycle and byte checks. `_reuse` holds at most 64 tuples of owner, code/test bytes, contract digest, approved functions and defensive reviewed context. Drift or revocation removes the grant; temporary query expiry alone does not. `ToolExecutor` owns sensitive-call approval, ignores dialog edits as argument changes, rechecks after waiting, executes exact snapshots under native isolation and records a fresh result. `ArtifactTools.verify_existing_tool_tool` returns REUSE_READY signatures/context for reusable tools, retaining provisional tests and review for first use. The manager follows this distinction and derives new arguments from the new query.

## Persistent approval code contracts

`data_protection.WindowsDataProtection` lazily loads Windows DPAPI and reads MachineGuid as binding entropy. `_Blob` mirrors DATA_BLOB; Python retains input/entropy buffers until the call returns, copies native output, and always frees it with LocalFree. `seal` adds a version/digest envelope; `unseal` checks it after native integrity validation. User protection is used without CRYPTPROTECT_LOCAL_MACHINE and UI prompts are forbidden.

`approval_store.DataProtector` defines injectable seal/unseal byte operations. `ApprovalStore` holds canonical directory/root, a root-hashed namespace, protector and policy fingerprint. `_path` validates the tool name and rejects redirected locations. `save` accepts only trusted host-published successful execution, validates declarative contract data, seals bounded metadata and atomically replaces a unique owned file. `load` validates protected schema, root/tool/code/test/policy identities and reviewed function coverage; invalid records grant nothing. `revoke` removes only the named owned record. `policy_fingerprint` reads a fixed list of maintained security files, never traversing tools; `user_approval_store` composes the Windows-user deployment.

`VerificationLedger.store` is an optional injected approval repository; `_owner` fixes this ledger's browser owner, `_reuse` remains a bounded session cache, and query receipts remain separate. Protected records may restore approval across fresh ledgers, not results or session state. `ArtifactTools` and `create_runtime` accept explicit approval-store injection. Injected fake execution backends do not implicitly enable native persistence. Production uses the native store when no execution double is supplied. The review controller adds an explicit future-session authorization notice when persistence is configured.
