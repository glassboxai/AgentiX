# V3 real GUI validation — 2026-10-23

Completed a supervised qwen3-coder:30b warehouse-pricing workflow through a separate GUI.
Reviewed/corrected specifications, tests and acceptance; approved unmodified generated
implementation. Eight provisional tests and sixteen host cases passed; final execution
returned 47.0 for 27 boxes. Three isolated mutation probes detected their deliberate
defects. Report and evidence: reports/V3_LIVE_GUI_REVIEW.md. No production Python changes;
the incomplete backend evaluate protocol and currency presentation remain follow-ups.

# AgentiX v3 — 2026-10-23

Added explicit engineering rules, a curated v3 checkout, package version 3.0.0, shared injected execution protocol, explicit Gradio analytics policy, English test documentation and AST source references with a freshness regression. See reports/V3_ENGINEERING.md and specs/014-v3-engineering-quality.md. Original historical entries follow.

# Change log

## 2026-10-23 — Four week project proposal

- Added an English planning proposal in Markdown and visually reviewed Word
  format, with all activities and milestones pending, staffing assumptions,
  sixteen planned days, four reserve days and observable acceptance gates.
- Specified proposed Widget Designer, Assembler and Supervisor responsibilities,
  strict contracts, Playwright evidence and a Day 3 execution-boundary decision.
  This is a proposal, not implementation authorization or a claim of completion.
- Reused maintained project evidence for planning without inspecting existing
  generated artifacts. No application code, runtime or test configuration changed.

## 2026-10-20 — UI-013 reference typography and square controls

- Added The Glass Box AI Project link below the final header description.
- Matched the inspected local reference's typography and removed rounded corners
  throughout panels, controls and messages. Retained the compact accessible send button.
- Matched 20px square checkbox styling in unchecked/checked/focus/disabled states,
  preserving native semantics, approval defaults and forced-color support.
- Added link order regression and computed-style/keyboard browser assertions.
  See `reports/UI013_REFERENCE_CONTROLS.md` for verification and provenance.

## 2026-10-20 — UI-012 AgentiX presentation

- Added the supplied local logo/favicon, AgentiX identity, approved description,
  dark/cyan reference palette and local Inter font stack.
- Removed decorative interface emoji/chat toolbar icons; added a compact
  accessible send control. Preserved verbose output and technical diagnostics.
- Added bounded, escaped result fields/tables with collapsed execution details;
  preserved the agent/CLI result record and finer-grained observed rates.
- Added validation summaries, bounded case scrolling, individual evidence
  disclosures, folded test context and per-tool catalog disclosures.
- Verified 316 offline, five real-framework and five disposable browser checks,
  including desktop/mobile contrast. Ruff passes for 78 active Python files.
  See `reports/UI012_PRESENTATION.md` for evidence and limitations.

## 2026-10-20 — USER-PROMPT-001 domain-only supervised validation

- Submitted an English household electricity query to qwen3-coder:30b without
  programming instructions. Reviewed and corrected temporary specifications,
  code, tests and acceptance data manually in a separate loopback GUI.
- Recorded eleven provisional tests and sixteen independent host comparisons
  passing, plus original-code failing reproductions. Retained original proposals
  and review corrections. Final isolated execution for 350 kWh returned EUR 67.50
  and the correct three-tier breakdown; see `reports/USER_PROMPT_LIVE30B.md`.
- Reverified the UI digest-summary change: 307 offline tests passed, 17 opt-in
  cases deselected, Ruff lint/format passed for 75 active Python files.

## 2026-10-19 — UI-VALIDATION-001 concise validation summary

- Removed the contract digest from the user-facing GUI summary while retaining
  evaluator/ledger evidence and verbose diagnostics. State, cases and comparisons
  remain visible. Captured the failing presentation regression before correction.


## 2026-10-19 — Specification 010 communication and supervised 30B validation

- Approved full communication block and resumed supervised 30B validation.
- Added shared role-appropriate workflow obligations; corrected class-oriented
  architect guidance and tester's unconditional iterate-until-pass instruction.
- Added defensive acceptance context with reviewed cases and AST signatures.
- Bound final tool responses to actual successful isolated execution observations;
  discard unsupported model final prose. Preserve verbose messages/technical events.
- Added failing regressions before implementation; verification/live results are
  recorded separately in the communication report.


- Completed a supervised English qwen3-coder:30b creation/review/acceptance/execution operation: seven reviewed provisional tests, sixteen host comparisons, observed kwh=250 -> 4250. Corrected model examples/code/tests manually and preserved original failures.
- Verified 307 offline, five framework, nine native and three deterministic browser cases; Ruff checks/format pass for 75 files. Added canonical catalog filenames and bounded malformed-proposal manual correction without relaxing approved-data validation.
- Current report, incidents, ADR 0008, installation status, specification and 35 source hashes are synchronized. Local qwen3:14b drafted report prose only; unsupported draft inferences were rejected.

## 2026-10-19 — LIVE-UX-001 verbose output with technical events

- Restored `verbose=True` for all four agents and every application Crew, as explicitly requested. Technical events remain visible alongside the original SDK messages. Kept per-session routing and bounded activity rather than replacing verbose information with summaries.
- Shared the stdout-routing startup context between the main UI and real-model supervised launcher, with restoration after exit/failure. Fixed legacy Windows console encoding errors without losing Unicode GUI messages, and reassembled Rich fragments into bounded logical lines.
- Added ten offline regressions and real CrewAI event-renderer/concurrent-controller verification. Documented both observed output failures, their red/green evidence and updated stream-tail semantics. The actual 30B functional run remains paused; shared workflow prompts and additional handoff work remain proposed.

## 2026-10-19 — LIVE-FIX-001 approved creation-stage corrections

- Preserved the original user request alongside manager context. Split creation into separately checked architect/coder/tester crews using actual approved persisted specification/code. Added bounded owner/operation-bound save receipts and final source/specification rechecks. Missing/stale/modified artifacts stop advancement and revoke acceptance where necessary.
- Corrected zero-output Gradio approve/reject bindings. Converted the two resolved strict xfails into normal regressions; added ten creation-stage cases. Documented two implementation races with failing reproducers and passing fixes.
- Verified 274 offline, four framework, nine native and three browser cases, with Ruff checks passing. Required qwen3-coder:30b in live validation and launcher documentation. The real 30B run was paused by the user before approvals; no functional success or model failure is claimed. Proposed activity/system-policy/handoff improvements remain pending validation under specification 010.

## 2026-10-19 — LIVE-001 supervised real-model GUI validation

- Added an opt-in launcher for the actual application composition with local models, native isolation, manual approvals and separate temporary storage. Recorded a predetermined progressive-tariff problem and independent oracle; deterministic browser fixtures remain separate.
- Reviewed and corrected model-proposed specifications through the GUI, preserving originals and edited versions. Real sampled failures and progress are recorded in `reports/LIVE_HITL.md`; no production source was changed to hide failures.
- Added strict expected-failure regressions for original-requirement loss at the pipeline boundary and Gradio's no-output approval callback mismatch. Their failures were reproduced explicitly before any proposed correction. Production fixes require a later approved block.

## 2026-10-19 — CLI-001 terminal review and E2E-001 browser regressions

- Added owner-bound terminal approve/reject/edit dialogs, separate explicit approval after multiline editing, EOF/Ctrl+C denial, and host validation output. Preserved `main.py`, query exit aliases and injected-workflow compatibility. Added correlated workflow/review events and escaped terminal control characters in review text without altering approved bytes.
- Added optional pinned Playwright dependency, separate browser marker and disposable real Gradio server with temporary trusted fixtures. Browser scenarios exercise acceptance editing/host verdicts, rejection, session separation and actual edited file persistence. No model, live application restart, existing generated artifact access, Docker or installer is involved.
- Added specification 007, ADR 0006, terminal/browser instructions and incident/regression evidence. Historical reports remain snapshots; see `reports/CLI_BROWSER.md` for current results and limits.

## 2026-10-19 — ACCEPT-001 human-reviewed acceptance

- Made generated unittest success explicitly provisional. It cannot authorize functions or the final manager stage. Added strict declarative acceptance cases proposed by the application and edited/approved by the user.
- Added mandatory manual acceptance reviews with owner/request IDs, expiration and cancellation. File auto-approval cannot approve acceptance. Rejection/expiry prevents automatic reprompting in the same operation.
- Added deterministic host comparisons of typed JSON returns, numeric tolerances and expected function exceptions. Each approved case gets a fresh isolated process receiving only implementation/function/inputs. Expected values, contract and unittest source remain outside that child.
- Added final authorization bindings for owner/operation/source/tests/approved contract/evaluator version/covered functions. Added atomic pre-dispatch rechecks and permanent revocation when content changes are observed. Updated agent tools/prompts and creation/reuse gates.
- Added escaped session-owned UI displays for generated Python tests, provisional results, editable acceptance cases, current stage and per-case expected/observed outcomes. Added English review instructions, specification, architecture, ADR and incident records.
- Resolved ACCEPT-ERR-001 through ACCEPT-ERR-005 and ACCEPT-UI-001 with failing-before/passing-after regressions. Added forged-unittest and malformed-data regressions plus real Gradio edited approval and native typed observation tests. Adjusted legacy assertions only for the approved provisional/final behavior change.
- Verification: 251 offline tests, nine real Windows isolation tests and three real-framework tests pass (263 distinct cases). Ruff check/format pass for 62 Python files. Evidence includes 34 active application source hashes; see `reports/HUMAN_ACCEPTANCE.md`.
- Local Ollama was used only for a report draft, reviewed against raw evidence. No existing project generated content was accessed, no live application restarted, and no installer or Docker dependency added. Finite reviewed cases do not prove universal correctness; runtime-only approvals and the lack of a dedicated CLI review adapter are explicit limits.

## 2026-10-19 — EXEC-002 native isolation and FLOW-002 outcome gating

- Replaced production in-process imports and host unittest execution with disposable Windows AppContainer processes. Explicitly selected pipe handles, minimal environment, read-only staged inputs, fresh CPython standard library and Job Objects enforce process/memory/time/output bounds. No Docker or host-execution fallback; installer deferred by the user.
- Added owner/operation/content-bound in-memory observations, non-executing syntax checks and fail-closed execution/final-manager gates. Added manager `Verify Existing Tool` for current-query reuse. Reject zero, skipped, expected-failure, failed, stale, changed and missing outcomes. Artifact byte snapshots, not mutable paths, enter the child.
- Added regressions for manager prose bypass, operation/owner/content changes, late results, invalid current source and malformed reports. Default infrastructure tests explicitly double OS observations; separate native tests establish the actual Windows controls. Replaced legacy expectations only where this approved behavior intentionally changed.
- Fixed and documented EXEC-ERR-001 and FLOW-ERR-001 through FLOW-ERR-004. Strengthened the network fixture to distinguish an unavailable service from OS blocking. Updated architecture, approval scope, specifications, ADR, installation status and issue register in English.
- Verification: 212 default tests, eight native Windows tests and two real-framework tests pass; Ruff check and formatting pass for 58 active Python files. Raw evidence and 33 application source hashes are in `reports/isolation-evidence.json`. See `reports/ISOLATED_PIPELINE.md` for exact limits and report provenance.
- Child unittest reports remain forgeable by generated code in the same interpreter; semantic correctness and malicious-report attestation are explicitly not certified. No project artifact content was accessed, no live app restarted and no installer created.

## 2026-10-19 — SEC-005 session, approval and decision security

- Added a bounded owner/token session registry, per-session controllers, provider clients, agents, histories, activity and auto-approval settings. Added expiry, trusted State cleanup and Request-injected unload cancellation.
- Added generated approval IDs, owner matching, deadlines, single-use response/type validation and occupied-slot protection. The clicked approval ID travels with the browser editor snapshot rather than mutable server State.
- Added a bounded strict manager creation contract; removed arbitrary fallback/name normalization and reject malformed, ambiguous, duplicate/extra-field, unsafe-name or invalid-purpose output without creation.
- Added correlated payload-free application events, separate diagnostic/capability identifiers, context-local stdout routing and explicit provider-tool thread propagation. Disabled provider verbosity and bounded activity retention; full third-party logging and OS isolation remain deferred.
- Locked controller snapshots/acceptance and retained the active assistant-message index across busy submissions. Preserved valid editing, timeout/rejection, pre-write Python validation and root entrypoints; manual resolution now requires IDs.
- Added and ran regression/concurrency/service tests and real Gradio server-side processing tests without launching a model/server or inspecting project artifacts. Updated English architecture, specifications, installation notes, ADR and issue/provenance records. Current evidence is in `reports/SESSION_SECURITY.md`.

## 2026-10-19 — REF-003 structural refactoring

- Extracted implementation into `src/agentix/`: settings, contracts, paths, approvals, storage, catalog, execution, test runner, tool operations, CrewAI adapter, orchestrator, UI state/controller/view, bootstrap and CLI.
- Replaced active root files with compatible lazy entrypoints; moved directory/model/agent/widget creation, process hooks and stdout capture to explicit startup. `_agentix_path.py` locates the src package from a checkout.
- Preserved role/task prompts, manager parsing/fallback, result strings, approval timing/edit behavior, corrected security checks and instance histories, UI bindings and launch options.
- Rewired test fixtures through explicit dependencies while retaining behavioral assertions. Added import/composition/CLI/compatibility tests and separate actual-framework adapter validation.
- Added English contracts, annotations, rationale comments and component diagnostics. Added pinned Ruff development tooling/configuration and formatted active sources, tests and report helpers; excluded generated artifacts and inactive source copies.
- Fixed REF-ERR-001 public exception re-export with a dedicated regression; documented restricted-environment adapter timeout and successful external validation.
- Updated architecture, specifications, installation status and report/provenance records. No existing generated-tool content was inspected or modified, no live application restart occurred and no installer/session/sandbox redesign was included.

## 2026-10-19 — Remove obsolete source copies

- Removed `app_.py`, `app__.py`, `security_manager_.py` and `security_manager__.py` at the user's explicit request because they are obsolete versions.
- Verified that all four paths are absent. Active source files and generated artifacts were not modified. No tests were needed for removing these inactive copies.

## 2026-10-19 — Approved SEC-001/002/003/004 and UI-001 corrections

- Replaced textual-prefix containment with resolved component checks and Windows path/name validation; preserved relative nested artifact paths.
- Returned deep-copy snapshots of pending approvals under the lock.
- Validated final approved Python before opening a destination, including edited test scripts and combined append content; invalid edits preserve existing files.
- Converted ExecutionState to a dataclass with an independent history factory.
- Added English contracts/comments and validation logs; converted five strict xfails to normal regressions and added 26 cases. Full suite: 131 passing tests. An additional red–green regression ensures a requested Python file cannot bypass validation when its resolved destination has a text suffix.
- Retained pre-fix evidence and baseline hashes; current verification is recorded separately. Existing generated artifacts were not inspected or modified. No live application restart, session-isolation redesign or execution sandbox was included.

## 2026-10-19 — Generated-content scope clarification

- Explicitly excluded all project `generated_tools/` content from inspection, refactoring, tests, coverage targets and documentation, per user instruction.
- Updated engineering rules, local skills, specification and test plan; added an explicit pytest recursion exclusion.
- Retained Agentix infrastructure tests using independent temporary fixtures outside the excluded directory. No generated artifact or production module was accessed or modified for this clarification.

## 2026-10-19 — Baseline foundation, phases 1–3

- Added REF-001, ADR-0001, engineering rules, English current architecture and installation status/contract.
- Vendored TDD, debugging, verification and security skills at fixed revisions; added local SDD and documentation skills, provenance and licenses.
- Added deterministic unit and trusted component tests, pytest configuration and development dependencies.
- Recorded production hashes, raw JUnit results, defect reproducers and reviewed report evidence; added reporting helpers and their tests.
- Documented SEC-001–004 and UI-001 without applying production fixes.
- Production modules, generated artifacts, alternative source copies and the live application are unchanged. Production refactoring, security fixes and installer implementation await approval.

# SEC-LLM-001 / UI-MODEL-001 — 2026-10-24

Added native hideable Sidebar model settings and moved human review out of the right column. Added explicit per-session provider activation, persistent Windows credentials with nonsecret revisioned profiles, local installed-model discovery and remote sync/async transport guards. Added bounded queries, provider settings, agent work budgets and global workflow capacity. Kept verbose agent/crew output and existing acceptance/isolation gates. Added synthetic offline, browser, framework-transport and disposable native-vault checks. Security assessment and operating manual: LLM_SECURITY_2026.md and MODEL_CONFIGURATION.md. Final evidence is recorded in reports/MODEL_SECURITY_IMPLEMENTATION.md.

# UI-MODEL-002 — 2026-10-25

Matched sidebar secondary-button colors to NexisNodes/aXiom Glass Box. API key and remote consent now hide for Ollama and clear on provider changes; saved-profile outputs preserve conditional visibility. Strengthened Playwright tests to explicitly exercise Refresh models, Save profile, Delete selected profile, Refresh saved profiles and Apply model with observable effects. Added computed-color, local visibility and provider-switch clearing checks. Backend authorization and existing live processes are unchanged. See specs/017-sidebar-controls.md and reports/SIDEBAR_017_VALIDATION.md.

# PROFILE-001 — 2026-10-25

Added local Ollama metadata profiles to Saved profiles without credential dependencies; preserved existing external records and safe provider conversion. Accepted readable Unicode/model-style profile names. Added fixed-code validation/native-vault/metadata diagnostics and retained failed-save reasons through refresh. Added local GUI lifecycle, external failure, native Gradio/store/vault and rollback/limit regressions. The user's original external failure is not claimed fixed by synthetic success; its hidden diagnostic is now actionable. See specs/018-unified-profiles.md and reports/PROFILES_018_VALIDATION.md.

## 2026-10-25 — REUSE-001 reviewed tool reuse

Added bounded session-owned grants after successful reviewed execution, REUSE_READY handoff, conservative unattended-call classification and manual per-call authorization for sensitive/unclassified code. Fresh host execution remains mandatory per answer. Added second-query, drift/restoration, owner/lifecycle, unreviewed-function, dynamic-introspection and approval-wait regressions; native lifecycle expectations now exercise reuse and subsequent drift. See specification 019 and its verification report.

## 2026-10-25 — REUSE-002 durable approvals and UI-REVIEW-002

Persist successful reviewed tool approval across reloads/sessions/restarts using Windows-user DPAPI, explicit machine binding, exact artifact/root/function identity and security-policy fingerprints. Preserve per-call sensitive permission, native isolation and fresh result receipts. Historic tools require a first protected review. Move the sole review panel/editor/buttons below Tool validation in the right column and disclose future-session authorization. Add unit tamper/drift/revocation coverage, real DPAPI cross-process checks, Gradio ancestry validation and Playwright reload/new-browser/server-restart/source-change coverage. See specification 020 and its validation report for raw failures, final results and supervised Ollama evidence.

UI-REVIEW-002 also scopes the dark fill to Gradio's nested review styler; a browser contrast regression protects readability after relocation.
