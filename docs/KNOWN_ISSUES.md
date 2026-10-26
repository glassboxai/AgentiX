# V3 supervised GUI validation — 2026-10-23

See reports/V3_LIVE_GUI_REVIEW.md for the complete real qwen3-coder:30b run.
V3-LIVE-001 specification arithmetic/contract errors and V3-LIVE-002 invalid acceptance
JSON were corrected through manual GUI review. V3-LIVE-003 records reviewer additions
to incomplete boundary/type tests. Eight provisional tests, sixteen host-compared cases
and three targeted mutation probes passed their respective expected outcomes.
These are corrections to temporary generated artifacts, not production fixes.

V3-LIVE-004 remains open: the injected ExecutionBackend protocol omits evaluate although
acceptance requires it. Concrete WindowsSandbox worked in this run. Proposed next block:
complete the protocol and add an injected-provider regression through TDD, after user
validation. The GUI final card also lacks an explicit currency label; improvement only
proposed. No application source was changed during this validation.

# V3 engineering incidents — 2026-10-23

- V3-ERR-001: explicit startup did not force Gradio analytics off when a caller enabled it. The new regression failed before correction; configure_process now sets False. This enforces startup policy and avoids the analytics path involved in the earlier startup failure; it does not prove all framework initialization bugs absent.
- V3-ERR-002: execution composition could not inject one independent backend into every verification path. A failing factory regression reproduced the missing keyword; ExecutionBackend and composition-root injection now share one boundary across execution, provisional tests and acceptance.
- V3-ERR-003: source references could be missing or stale with no regression failure. New reference tests first failed, then passed after static generation; the suite now checks exact source/reference consistency.
- Evidence: reports/v3-red.txt, v3-reference-red.txt, v3-reference-before-generation.txt and v3-offline.txt. No historical baseline hashes were replaced.

# Known issues and regression register

UI-013: the missing project link was reproduced by the header regression before
implementation (`reports/ui013-link-red.txt`). Link order is now tested alongside
computed square corners, checkbox dimensions/colors and Space-key toggling.
The external reference was inspected read-only, without saving configuration.

## UI-012 presentation incidents (2026-10-20)

- UI012-ERR-001 (corrected): the CSS send glyph contributed to the accessible
  name, preventing exact-name browser actions. Empty CSS alternative text makes
  it decorative while retaining Send query. The initial five browser failures
  and final five passes are retained.
- UI012-ERR-002 (corrected): inherited light chat bubbles conflicted with light
  text. Screenshot review found this after functional checks passed. An explicit
  contrast regression failed at about 1.07:1. Dark bubble fills/theme variables
  correct it; final desktop/mobile tests enforce at least 4.5:1 for result text.
- UI012-ERR-003 (corrected): two-place formatting hid finer observed rates.
  A 0.12345 regression failed before correction. Only already two-place amounts
  receive padded formatting; finer rates remain unchanged. Currency formatting
  requires explicit euro information in the original query.
- UI012-ERR-004 (engineering edit corrected): an intermediate default-codepage
  edit corrupted Unicode presentation characters. The currency assertion caught
  it. Restored UTF-8 and reverified; subsequent edits explicitly specify UTF-8.

Restricted framework initialization timed out; all five checks passed outside
that restriction using the same source. No model/server is started by these
checks. See `reports/UI012_PRESENTATION.md` for root causes and raw evidence.

## Domain-only supervised review (2026-10-20)

LIVE-USER-ERR-001/002/003/004 concern temporary model proposals: an incorrect
specification example, boolean/unused-tier code defects, an overconstrained error
message test and malformed acceptance data. Each was reviewed and corrected;
the original and approved evidence is retained. The corrected eleven-test suite
fails against the original code and passes against the approved code; sixteen
host acceptance comparisons pass. See `reports/USER_PROMPT_LIVE30B.md` for causes,
corrections, regressions, operational interruptions and remaining limitations.
These are supervised artifact corrections, not new production implementation
changes or proof of autonomous model correctness.

UI-VALIDATION-001 (presentation corrected): the validation summary exposed an
internal contract SHA-256 without helping user review. Removed only that line
from the GUI renderer; evaluator and ledger retain the digest. The presentation
regression failed in `reports/validation-summary-red.txt` before correction.


## Communication block incidents (2026-10-19)

Current status: the full approved block completed one real English supervised
creation/review/acceptance/execution run with qwen3-coder:30b. Seven reviewed tests
and sixteen host comparisons passed; actual call 250 returned 4250. Manual model
artifact corrections were necessary. See `reports/COMMUNICATION_LIVE30B.md` for
earlier failed attempts, red/green evidence, source hashes and remaining limits.

- DOC-EDIT-002 (documentation tooling corrected before completion): moving the
  current changelog/register sections temporarily joined their headings to the
  first content line. Final readback caught this; restored blank-line separators
  and checked both headers. No runtime behavior changed or runtime test applies.

- LIVE-SPEC-003 / LIVE-TEST-002 (temporary review corrections verified): the final
  specification's 150/250 examples were arithmetically wrong, and QA expected 1212
  for 101 kWh. Corrected to 2100/4250 and 1218 before approval, preserving originals.
  Independent acceptance cases for 101/150/250 passed. Native negative evidence
  executes the original wrong test against correct code (one failure), then the
  approved suite (seven passes). Bool counterexamples fail twice on original code
  and pass twice on corrected code. See `reports/live-workflow30b-counterexamples.json`.

- LIVE-REVIEW-003 (implemented): the English QA run sent malformed acceptance JSON
  after eight provisional tests passed. The parser rejected it before opening a
  review, so the human could not repair the proposal. The original run stopped
  without acceptance/execution; logs record JSONDecodeError, not its exact content
  or a proven provider cause. Bounded invalid proposal text now reaches mandatory
  manual review with a warning; the approved edited JSON must pass the unchanged
  strict parser before any child evaluation. Oversized proposals still fail before
  review, invalid human edits still revoke, and no model retry is introduced. Two
  repair regressions failed first in `reports/malformed-proposal-red.txt`.
- LIVE-CATALOG-002 (implemented): the reuse manager guessed package filenames after
  provisional verification, read missing files and attempted unauthorized execution.
  The host returned EXECUTION_NOT_VERIFIED. Catalog entries now expose conventional
  explicit artifact filenames; manager instructions require them. The consumer
  regression failed in `reports/catalog-artifacts-red.txt`. Existing files are not
  claimed to exist merely because their conventional names are listed.

- LIVE-CODE-001 (reviewed temporary artifact correction): generated implementations
  in both Spanish and English attempts used isinstance(kwh, int), admitting bool.
  Reviewer replaced that check with exact type validation before approval. The
  English source otherwise needed no code edit. Original and approved text are
  retained as `live-workflow30b-english-code-*.txt`; generated invalid-input tests
  and independently reviewed True/False acceptance cases guard the behavior.
  Original unapproved generated code was not executed on the host.
- LIVE-TEST-001 (reviewed temporary artifact correction): the English QA proposal
  expected 5750 for 300 kWh although its own numeric explanation totals 5500.
  Reviewer corrected the expectation using independent arithmetic and added
  exact-type/boundary checks and the integral float 1.0 case. The independent
  acceptance contract also covers 300 -> 5500. Originals/edits are retained as
  `live-workflow30b-english-tests-*.txt`; this is not an application source defect
  or an autonomous model success. Execution results are recorded in the report.

- REVIEW-ERR-001 (reviewer input corrected; no production parser defect): the
  independent live-review case IDs initially used hyphens, which version 1 rejects.
  Approval therefore failed closed before any acceptance observation or final
  execution. The reviewed source/tests remained temporary. Corrected the case IDs
  to underscores and preflighted all sixteen cases with the actual parse_contract.
  Preserved the invalid reviewed JSON and failed GUI result; added the concrete
  invalid-human-ID case to the coordinator regression (36 acceptance tests pass in
  `reports/review-identifier-regression.txt`). No parser restriction was weakened.
- LIVE-LANGUAGE-001 (user steering): earlier resumed attempts used a Spanish domain
  query with English system policy. The user subsequently requested an English
  query for model reliability. The pending specification operation ended without
  an approved artifact; a new operation uses `live-workflow30b-english-query.txt`.
  This does not establish a measured causal comparison between query languages.

- LIVE-STAGE-003 (implemented): after saving the reviewer-corrected specification,
  the 30B architect requested the original erroneous content again. The reviewer
  rejected that overwrite and stopped the second temporary server; it did not
  complete the pipeline. Evidence: `live-workflow30b-spec-original.md`, approved
  version, second proposal, repeat-save DOM and retry server log. Cause: an extra
  model turn remained after a single-artifact stage's successful service result.
  Mark specification/code saves as CrewAI result_as_answer so control returns
  directly to host receipt gates. Adapter regression failed in
  `reports/stage-completion-red.txt`; real-framework registration is also checked.
- LIVE-SPEC-002 (observed model error): the 30B specification's 250 kWh example
  said 3750 although its stated formula yields 4250. Reviewer changed only that
  example before approving. This is a manual artifact correction, not proof of
  autonomous model correctness; independent literal acceptance values are retained.

- LIVE-CATALOG-001 (implemented): the first supervised 30B attempt ignored the
  empty-catalog instruction and called verification on a guessed nonexistent tool.
  The reviewer rejected the resulting incidence-directory request and stopped the
  disposable server. Evidence: `reports/live-workflow30b-first-finding.*` and its
  server log. Cause: prompt prohibition still exposed verification tools. CrewAI
  falls back from empty Task.tools to Agent.tools. Solution: a separate manager
  instance with no tools for empty-catalog decisions, preserving the execution
  manager's tools without mutable per-task changes. Regression failed first in
  `reports/empty-catalog-red.txt`; the final fresh real run completed successfully.

- LIVE-EXEC-001 (fixed and verified): the final manager returned
  arbitrary prose even without executing, or after an actual call returned a
  different result. Reproducer: `test_execution_handoff.py`, red evidence
  `reports/handoff-red.txt`. Cause: acceptance gated the final task, but no host
  postcondition checked its call. Solution: per-operation content/contract-bound
  execution observations and host-rendered final results; missing calls fail closed.
- LIVE-PROMPT-001 (implemented and observed in supervised validation): shared workflow
  policy now reaches all four agents. Empty catalogs require creation; original
  requirements and approved persisted artifacts reach each role, and the final
  manager receives accepted functions/signatures/cases. The earlier proposed entry
  elsewhere in this register is historical and superseded by specification 010.

Live operational follow-up: see `reports/LIVE_SMOKE.md` for the real browser/CLI checks and ENV-004 below. Historical ACCEPT-001 evidence remains preserved; the latest CLI/browser verification is in `reports/CLI_BROWSER.md`.

SEC-001/002/003/004 and UI-001 were explicitly approved and fixed on 2026-10-19. Their former strict xfails are normal passing regression tests. Historical correction evidence is in `reports/fixes-before.txt`, `reports/fixes-expanded-before.txt` and `reports/fixes-tests.xml`. Current SEC-005 session/approval/decision fixes and remaining open risks are distinguished below; see `reports/HUMAN_ACCEPTANCE.md` for current verification and `reports/SESSION_SECURITY.md` for the SEC-005 snapshot.

| ID | Trigger / root cause | Affected module | Passing regression | Implemented solution |
| --- | --- | --- | --- | --- |
| SEC-001 | Sibling tool prefix accepted as containment | `security_manager.py` | `test_reject_sibling_tool_prefix_escape` | Validate components and require resolved path containment |
| SEC-002 | Sibling root prefix accepted as containment | `security_manager.py` | `test_reject_sibling_root_prefix_escape` | Reject traversal/drive aliases and enforce resolved root boundary |
| SEC-003 | Pending dictionary returned by reference | `security_manager.py` | `test_pending_request_is_defensive_copy`, `test_pending_snapshot_cannot_modify_nested_state` | Deep-copy pending state while holding the coordinator lock |
| SEC-004 | Approved edits bypassed Python compilation | `custom_tools.py`, `security_manager.py` | `test_edited_python_is_validated_before_save`, `test_invalid_edited_tests_are_not_executed`, preservation/append tests | Compile final approved Python before opening destination, including combined append content |
| UI-001 | Class-level mutable history shared across instances | `app.py` | `test_execution_states_have_independent_histories`, `test_new_execution_state_does_not_inherit_other_state_values` | Dataclass instance fields and independent history factory; session isolation remains pending |

## Further investigation

Current implementation locations after REF-003: path policy is `src/agentix/paths.py`, approval snapshots are in `approvals.py`, final content validation is in `storage.py`, and independent state histories are in `ui/state.py`. Root modules are compatibility facades; the original regression names remain in the suite.

SEC-004 follow-up: validation now considers both requested and resolved filename suffixes, so a confined file alias cannot bypass compilation by resolving to a non-Python suffix. `test_python_alias_cannot_bypass_validation_by_resolving_to_text_file` failed before this correction (`reports/alias-before.txt`) and passes afterward. The test models resolver output without requiring Windows symlink privileges; it is not a filesystem-link integration test.

- EXEC-001 (host-execution defect fixed by EXEC-002): production services no longer import generated modules in the UI process or run ordinary host unittest subprocesses. Fresh Windows AppContainer processes with no network capabilities execute staged standard-library Python under limited Job Objects. Setup failures deny execution. Eight opt-in native tests cover private host file access, a live controlled loopback listener, read-only staging, omitted secrets, time/output/memory/process limits and cleanup. This is not VM isolation or an exhaustive escape audit; see `reports/ISOLATED_PIPELINE.md`.
- AUTH-001 (fixed by SEC-005): browser sessions now own separate coordinators/agents/clients/state. Manual decisions require matching owner/request IDs and valid deadlines; live slots cannot be overwritten. Tests cover simultaneous owners, duplicate/expired/missing/previous IDs, cancellation and same-file requests. Gradio process_api tests verify foreign-token rejection and unload. This is workflow isolation, not account authentication.
- FLOW-001 (fixed by SEC-005): strict exact creation JSON replaces the arbitrary fallback. Invalid output raises DecisionValidationError without starting the pipeline. The former fallback characterization was replaced by explicit rejection/no-creation assertions, plus malformed/type/name/duplicate/extra-field tests.
- LOG-001 (partially fixed by SEC-005): routine application events no longer log query/source/model/exception payloads; they carry session/run/request identifiers and error type/line. Activity is context-local and bounded. The user subsequently explicitly approved verbose agents/crews alongside technical events under LIVE-UX-001. This visible SDK output may contain workflow text; fixed-field diagnostics remain payload-free. Arbitrary tool stdout, all third-party logging, persistent rotation and total process resource bounds remain outside this fix.
- FLOW-002 (agent/self-report authorization bypass fixed by ACCEPT-001): generated unittest reports are now provisional and cannot authorize execution. Explicit owner-bound human review of editable declarative cases precedes fresh isolated observations and comparisons in maintained host code. Only functions covered by passing approved cases are authorized for the current owner/operation/content/contract/evaluator version. Counts and child PASS claims cannot override a wrong returned value. Finite approved cases still do not prove all-input correctness or correct requirements; human-reviewed relevance remains essential. CLI-001 subsequently added a dedicated owner-bound acceptance-review client, using the same mandatory manual approval rules. See `ACCEPTANCE_REVIEW.md`.

## EXEC-002 / FLOW-002 implementation incidents

- EXEC-ERR-001 (fixed): the initial minimal child environment omitted LOCALAPPDATA. Windows CreateProcessW returned error 203 while resolving the AppContainer profile, inside and outside the restricted development environment. Preserve that path in the explicit minimal environment, without inheriting credentials/proxies or changing ACL restrictions. `test_native_python_isolated_execution_and_unittest` failed in `reports/isolation-native-first.txt` and `isolation-native-unrestricted.txt`, then passed. Reference: Microsoft's AppContainer launch documentation.
- FLOW-ERR-001 (fixed): a new CLI query initially retained the legacy coordinator's operation ID, allowing previous-query evidence. `test_previous_query_evidence_cannot_authorize_a_new_query` failed in `reports/isolation-edge-red.txt`. Bind the orchestrator's operation ID to its ledger security boundary at query entry.
- FLOW-ERR-002 (fixed): unittest considers expected failures successful. The first worker accepted expected-failure-only suites. The reproducer in `reports/isolation-edge-red.txt` failed before making worker success require no expected failures. Empty and skipped suites are also rejected.
- FLOW-ERR-003 (fixed): an in-flight test result could be labelled with an operation ID changed while it ran. `reports/isolation-run-race-red.txt` records the failing test. Capture owner/operation before execution and reject publication if either changed, in addition to content checks.
- FLOW-ERR-004 (fixed): unrelated passing tests could grant evidence to syntactically invalid current source. `reports/isolation-source-red.txt` records the failing regression. Compile exact source/test snapshots independently without executing them before accepting evidence; syntax failure denies it.
- VERIFY-001 (test corrected): the first network fixture accepted any OSError, so it could mistake an unavailable service for isolation. A strengthened fixture uses a live listener, first establishes a successful parent connection, and accepts child PermissionError or TimeoutError only. Windows filtering silently drops this connection on the tested machine; a timeout does not require permission to connect. Diagnostic evidence is in `reports/isolation-network-diagnostic.txt`. This was a verification correction, not a demonstrated network escape.
- TOOL-001 recurrence: a patch combining delete/add of the same module was rejected before changes. Replaced it with a single explicit file write; no production defect or regression applies. A later documentation context mismatch was also rejected and corrected using verified source text.

## SEC-005 edge cases and their regressions

- AUTH-002 (fixed): a mutable server-only approval ID could relabel a queued stale editor click. A real-Gradio reproducer failed in `reports/security-request-transport-red.txt`. Approval IDs now travel in a hidden non-stateful textbox with the editor snapshot and are revalidated server-side. The real adapter/routing tests protect this contract.
- SES-002 (fixed): the first session factory reused the legacy mutable provider client. `test_default_view_creates_independent_runtime_clients` failed before correction (`security-runtime-client-red.txt`). Each browser now creates its own client and role set; Ollama may share model weights internally.
- LOG-002 (fixed): using a browser capability as the diagnostic ID exposed that token to logs. `test_diagnostic_session_id_is_not_the_browser_capability_token` failed before introducing independent UUIDs. Application events log diagnostic IDs only.
- LOG-003 (fixed): provider tool threads need not inherit ContextVars. A real-thread reproducer failed (`security-thread-context-red.txt`); bound tool wrappers now restore owner/run/activity from their own security boundary. `test_tool_adapter_restores_owner_context_in_provider_threads` verifies correlation without payload leakage.
- SES-003 (fixed): child owner classes could inherit a parent's activity capture/run metadata. The reproducer `test_owner_factory_does_not_inherit_parent_activity_or_operation` failed (`security-owner-metadata-red.txt`) before explicit resets in for_owner().
- SES-004 (fixed): browser unload initially had no callback and only cleanup/expiry fallbacks. The real process_api unload test failed (`security-unload-red.txt`) before connecting a Request-injected unload handler. Delivered unload events now close that framework owner and cancel unresolved approvals; lost notifications still require fallback cleanup.
- AUTH-003 (fixed): nonboolean decisions or nontext edited content could be accepted. Type-rejection tests failed in `security-edge-red.txt` before strict checks. Valid empty edited text remains supported.
- UI-002 (fixed): a busy message could become the target of the original workflow's final result. The controller tracks its active assistant-message index; `test_busy_submission_cannot_steal_active_answer` verifies the corrected behavior.

Additional red/green evidence: `security-contracts-red.txt` records 22 initial contract failures; `security-log-red.txt` records exception-body leaks before safe event logging; `security-diagnostic-edge-red.txt` records capability-ID, degenerate-manager-response and CLI-log failures. Final current verification is in `reports/SESSION_SECURITY.md`.

## Tooling incidents

REF-ERR-001 (resolved): automatic unused-import cleanup removed the public SecurityViolationError re-export from the new package facade, breaking legacy imports. Root cause: the re-export had no explicit public API declaration. Solution: preserve the import and declare `__all__` in `agentix.security`. Regression `test_security_exception_is_exported_from_legacy_and_package_facades` failed before the fix (`reports/refactor-export-red.txt`) and now passes; existing path tests also protect exception compatibility.

ENV-003 (verification limitation, worked around): real CrewAI/Gradio adapter validation timed out after 90 seconds inside the restricted execution environment. The same test passed outside that environment in approximately seven seconds, without a model/server or project artifact access. Keep it opt-in with marker `frameworks`; the default offline suite remains independent of runtime packages. This is not an application behavior fix; the same adapter test is the reproducible verification.

ENV-001: bulk version inspection failed when `litellm` distribution metadata was missing. Solution: collect distributions independently and record missing metadata rather than aborting. Reporting-helper regression tests cover present and missing metadata. No runtime fix was required; missing metadata alone does not prove a runtime dependency failure.

TOOL-001: a documentation patch attempted both delete and add operations on one path and was rejected before applying changes. Solution: submit distinct-file additions separately and update the existing document with one write operation. This was a tooling invocation error, not an application defect; no production regression test applies. Verify production hashes after documentation changes.

ENV-002 (resolved): the external skill validator read UTF-8 upstream text using Windows cp1252 and raised UnicodeDecodeError. Solution: run the unchanged validator with Python `-X utf8`. Regression verification: all six skill entrypoints validate successfully under that invocation. This affects an external validation command, not Agentix runtime code; the documented validation command is the reproducible check.

When fixing an issue, record approved solution, changed files, date and failing-before/passing-after regression evidence. Never mark an xfail as fixed.

ENV-004 (operational workaround verified; durable controls open): the live 30B query coincided with less than 1 GiB free RAM on this approximately 16 GiB system, browser/HTTP timeouts and a stalled CLI startup. The query was cancelled, only the test's application/CLI processes stopped, and its resident 30B model unloaded. A temporary `OLLAMA_MODEL=ollama/qwen3:8b` launch restored responsiveness: the real browser conversation completed and `main.py` startup/`q` exit returned 0. The default source model is unchanged. This is an observed recovery, not an isolated proof that model size is the only cause or an automated performance regression. Model-memory admission checks, inference deadlines/cancellation and model-driven live E2E remain unimplemented. E2E-001 now supplies committed deterministic browser tests with trusted temporary fixtures, without a model; these do not test model memory or inference behavior. Evidence: `reports/live-smoke-evidence.json`, live logs and screenshot.

## ACCEPT-001 implementation incidents and verification

- ACCEPT-ERR-001 (fixed): serialization errors in observation mode were initially reported as expected function exceptions. A NaN return could satisfy an expected ValueError. Catch only exceptions from the function call, and treat JSON serialization failure as failed transport. Regression: `test_transport_serialization_error_is_not_a_function_exception`; red evidence `reports/acceptance-serialization-red.txt`.
- ACCEPT-ERR-002 (fixed): revocation between the initial authorization check and snapshot dispatch could leave the call authorized by a provisional record. Recheck acceptance, covered function and exact bytes together under the ledger lock. Regression: `test_revocation_between_execution_checks_prevents_the_call`; red evidence `reports/acceptance-edge-red.txt`.
- ACCEPT-ERR-003 (fixed): duplicate JSON observation keys were silently collapsed. Strict duplicate-key rejection now applies to child reports as well as contracts. Regression: `test_duplicate_observation_values_are_rejected`; red evidence `reports/acceptance-edge-red.txt`.
- ACCEPT-ERR-004 (fixed): an agent could automatically open another review after rejection by re-running provisional tests. Keep a rejected-operation marker and require a new user query. Regression: `test_human_rejection_cannot_be_automatically_reprompted_in_same_operation`; red evidence `reports/acceptance-rejection-red.txt`.
- ACCEPT-ERR-005 (fixed): an observed source change followed by restoration could revive an old hash-bound approval. Observed mismatch/access failure now revokes the provisional and acceptance records. Regression: `test_observed_source_change_cannot_revive_old_approval_after_restore`; red evidence `reports/acceptance-restore-red.txt`. Unobserved edits restored before any check are the same executed byte snapshot; no filesystem watcher is claimed.
- ACCEPT-UI-001 (fixed): final status initially omitted expected/observed values. The status panel now renders escaped, bounded data alongside host verdicts. Regression: `test_final_status_shows_expected_and_observed_data`; red evidence `reports/acceptance-results-ui-red.txt`.

`reports/acceptance-contracts-red.txt` and `acceptance-ui-red.txt` preserve initial feature failures. `acceptance-wiring-first.txt` records legacy assertions requiring updates for the approved provisional/final distinction. One test-fixture patch initially placed restoration assertions in the following test; it was corrected before verification. Ruff also identified one-line conditionals in new tests; formatting corrected them and final checks passed. These were test/tooling corrections, not production defects.


## CLI-001 and E2E-001 incidents

- CLI-ERR-001 (fixed): synchronous terminal workflows could not service their own blocking approval requests. The new coordinator-backed worker/main-input adapter supports approve, reject and edited review content while preserving owner/request IDs. Seven initial review regressions failed before implementation (`reports/cli-review-red.txt`); tests now cover approval, default rejection, invalid choices, editing and interruption. EOF at the query prompt also previously entered error recovery instead of exiting; it now exits cleanly. Its first pre-fix test attempt was interrupted because the loop did not terminate, rather than reported as a passing check.
- CLI-ERR-002 (fixed): terminal output initially omitted independent host verdict details. `test_cli_shows_independent_host_verdicts` failed before adding the acceptance status output (`reports/cli-verdict-red.txt`). It now exercises actual provisional checks and edited acceptance with trusted temporary fixtures, and checks the host verdict.
- CLI-ERR-003 (fixed): raw review content could emit terminal erase/carriage-return/bidi controls. Escape non-printable controls for review display, preserving the original approval content. `test_review_control_characters_cannot_hide_terminal_content` failed before correction (`reports/cli-control-red.txt`) and now passes.
- E2E-TEST-001 (test harness corrected): the first file-edit browser test expected the file prompt before approving required directory creation. `reports/browser-first-run.txt` records two passing scenarios and that failure. The test now approves directory creation separately, edits the file prompt and asserts persisted temporary bytes. No application approval rule was changed. Windows fixture teardown also stops its own launcher process tree; no live application is stopped.
- ENV-005 (verification environment): process creation and later browser tooling became unresponsive during the prior attempt; no source changes were made in that attempt. On retry, command execution recovered. Restricted package download also failed DNS lookup; the same pinned Playwright install succeeded through the authorized unrestricted package operation. These are environment observations, not application defect fixes.
- DOC-EDIT-001 (tooling only): two multi-file documentation patches included an incorrect heading and were rejected before application. Reissued the edits with verified context. No production change or runtime regression test applies; final documentation reads and source hashes are the verification.

Current verification and limits: `reports/CLI_BROWSER.md`. Model-driven E2E, model admission checks and forced inference cancellation remain outside this change; the installer remains deferred.

## LIVE-001 supervised real-model GUI findings

- LIVE-FLOW-001 (fixed in approved LIVE-FIX-001): creation now retains the original user request alongside the manager summary. `test_creation_pipeline_retains_original_user_contract` is a normal passing regression; its original failing evidence is preserved.
- LIVE-UI-001 (fixed in approved LIVE-FIX-001): zero-output approve/reject adapters discard internal decision booleans. `test_approval_callback_respects_real_gradio_output_contract` is a normal passing regression. Coordinator decisions/ownership remain unchanged.
- LIVE-FLOW-002 (fixed in approved LIVE-FIX-001): separate creation stages require fresh approved save receipts and actual bounded persisted context before advancing. Missing/stale/replaced artifacts stop creation. Ten stage regressions cover these boundaries, including actual acceptance services with trusted temporary fixtures. See `reports/APPROVED_CREATION_STAGES.md` for red/green evidence and limits.
- LIVE-FIX-ERR-001 (fixed): initial receipt observation could adopt an intervening write. Compare persisted bytes to the approved candidate before recording a receipt. `test_receipt_cannot_adopt_an_intervening_unapproved_write` failed first (`reports/stage-receipt-race-red.txt`) and now passes.
- LIVE-FIX-ERR-002 (fixed): final stage checks initially did not revalidate approved source after testing. Recheck specification/code and invalidate ledger evidence after mismatch. `test_gated_pipeline_completes_with_real_acceptance_services[True]` failed first (`reports/stage-final-source-red.txt`) and now passes.
- LIVE-SPEC-001 (observed model output, corrected by reviewer in temporary storage only): the first qwen3:8b architect proposal used float and omitted required invalid-input checks. Original and edited English specifications are preserved in `reports/live-hitl-spec-original.md` and `live-hitl-spec-approved.md`. This manual correction is not a production code fix or evidence of autonomous model success.
- LIVE-MODEL-001 (observed integration failure): the first qwen3:8b run saved specifications but no implementation or tests, and ended with PIPELINE_NOT_VERIFIED. The qwen2.5:7b retry failed with an empty-model-response error. The same query, manifests, GUI snapshots and server logs retain reproduction evidence. These samples do not establish a general failure rate or prove a specific provider root cause. Strengthening per-stage artifact checks/diagnostics and evaluating model/tool-call settings require a separate reviewed implementation block.

The user explicitly requested real-model supervised validation, extending the earlier deterministic test scope. See specification 008 and `reports/LIVE_HITL.md` for current outcomes. Existing project generated artifacts remain excluded. The installer remains deferred.


LIVE-UX-001 (fixed, approved verbosity sub-block): restored `verbose=True` for every application agent and Crew while retaining technical events in the same owner-bound activity. Shared startup routing also covers the real supervised launcher. Eight feature regressions failed before correction (`reports/verbose-activity-red.txt`). Real CrewAI event rendering with two concurrent controllers verifies role/task/tool-result/final-answer output without cross-session mixing. The supervised 30B functional run remains paused; shared prompt/handoff changes are not included in this display fix.

VERBOSE-ERR-001 (fixed): a Windows redirected console using cp1252 rejected CrewAI emoji panels before they reached GUI capture. Preserve the Unicode capture and escape only an unencodable host-console copy. `test_unicode_verbose_message_survives_legacy_windows_console` failed before correction (`reports/verbose-unicode-red.txt`); the first real-framework attempt also records the encoding failure (`reports/verbose-framework-first.txt`).

VERBOSE-ERR-002 (fixed): Rich emits panels in many styled write fragments; treating each write as a stripped record broke formatting and evicted useful activity from the visible tail. Capture logical lines, including split ANSI sequences and bounded partial streaming lines. `test_fragmented_verbose_output_preserves_logical_lines_and_ansi` failed before correction (`reports/verbose-fragments-red.txt`); `verbose-framework-second.txt` records the lost diagnostic event before line reconstruction. Low-level tail/retention fixtures now explicitly terminate lines, matching file-like stream semantics. Final real-framework output and offline checks pass.


LIVE-PROMPT-001 (proposed improvement): users should provide only the domain problem; workflow obligations belong in shared role-appropriate agent instructions. Clarify empty-catalog creation and validate all adjacent-agent handoffs. The user confirmed "the next agent" as the communication scope. Implementation awaits validation of specification 010. The qwen3-coder:30b supervised run was paused before approvals, not passed or failed; see `reports/APPROVED_CREATION_STAGES.md`.

## SEC-LLM-001 / UI-MODEL-001 implementation incidents

- MODEL-ERR-001 (corrected): the first native Gradio run rejected a direct Textbox autocomplete keyword. Cause: the installed version accepts InputHTMLAttributes instead. Solution: use html_attributes with autocomplete off and spellcheck false. Reproducer: reports/model-framework-first.txt; the existing real Gradio adapter regressions cover construction.
- MODEL-ERR-002 (compatibility tests updated): adding Sidebar/Dropdown/InputHTMLAttributes and explicit provider work limits invalidated the old UI double and exact constructor assertions. reports/model-offline-first.txt records three failures. The double now covers the actual components and settings assertions retain every legacy option plus the approved limits; no production behavior was weakened.
- MODEL-TOOL-001 (engineering script corrected): a transformation script expected a single-line return, but formatting had expanded it. It stopped before the controller/session migration; subsequent inspection identified the partial application. The repaired transformation uses verified boundaries, and full regression checks follow. This was an editing-tool error, not an application vulnerability.
- Persistent credential/metadata writes cannot be one cross-service transaction; a crash before metadata commit can leave an orphan target. Cleanup errors after commit retain obsolete references for retry. Same-user compromise, provider retention, DNS rebinding races, instant cancellation and universal generated-code correctness are not guaranteed. See LLM_SECURITY_2026.md. Existing V3-LIVE-004 and old Python follow-ups are not resolved by this block.

- MODEL-ERR-003 (fixed): collapsed native sidebar content remained visible to accessibility/visibility inspection after sliding outside the viewport. The failing browser reproducer is reports/model-browser-check.txt. Hidden content now uses visibility hidden and disables pointer interaction, while keeping the native toggle available. Browser checks exercise collapse/reopen and mobile interaction.
- MODEL-ERR-004 (fixed): the combined local/custom dropdown did not retain a manually entered external model in the observed browser flow, preventing profile save. reports/model-browser-diagnosis2.txt reproduces the missing selection. Use a separate explicit External model textbox and keep the local dropdown for installed names. The full browser profile lifecycle now checks save, activation, consent, reload, update and delete.
- MODEL-ERR-005 (fixed): a queued stale profile action could use the session's newer selection instead of the browser-displayed identity. reports/model-profile-identity-red.txt captures the failure. Save/delete now require identical displayed/server selection before accessing the store.
- MODEL-ERR-006 (fixed): legacy model environment overrides could select a remote GUI runtime without GUI consent. reports/model-local-start-red.txt captures the failure. GUI session composition now explicitly uses local qwen3-coder:30b and loopback; CLI compatibility configuration remains explicit and separate.
- MODEL-ERR-007 (fixed): Python 3.11 is_global includes multicast addresses. The two failing IPv4/IPv6 cases are in reports/model-multicast-red.txt. Remote endpoint filtering additionally rejects multicast/reserved addresses before credential-bearing requests.
- MODEL-COMPAT-001 (fixed): ordinary namespace/model identifiers were rejected by the initial validator. reports/model-namespace-red.txt captures the failure. Bounded namespace names are now supported while traversal, empty components and control characters remain denied.
- MODEL-TOOL-002 (corrected): editing helpers without explicit UTF-8 decoding damaged a euro assertion and the CSS send glyph on Windows. Browser failure and visual inspection exposed this; the original Unicode bytes were restored and subsequent helpers explicitly use UTF-8. An initial transport subprocess also lacked the checkout path bootstrap; its fixture now imports _agentix_path. These were engineering-tool/test preparation errors, not provider-inference evidence.

- MODEL-TOOL-003 (corrected): a helper staged under the restricted host's temporary directory was not present under the unrestricted host's different Windows virtualized temporary path. The attempted invocation failed without applying the migration. The helper was recreated explicitly within the same authorized host context, then regression checks verified the resulting source. This is a host/tooling path incident; no production regression test applies.

## IAC-001 implementation incident register

Historical infrastructure evidence is retained without rewriting prior baseline/fix manifests. These corrections preceded the SEC-LLM-001 delivery and are exercised by the existing IAC unit suite.

- IAC-ERR-001 (fixed): scalar/PSObject handling in canonical state normalization treated a scalar as an object with a Name member. Add scalar normalization before member traversal. Evidence: reports/iac-scalar-red.txt; IAC normalization regression.
- IAC-ERR-002 (fixed): the Windows PowerShell DSC host did not autoload required OS modules, so Get-FileHash was unavailable. Import explicit OS-provided modules in the Desktop host. Evidence: reports/iac-dsc-modules-red.txt; no-autoload compatibility regression.
- IAC-ERR-003 (fixed): a failing manual launcher did not restore temporary process environment overrides. Restore them in finally. Evidence: reports/iac-launcher-red.txt; failure-path launcher regression.
- IAC-ERR-004 (fixed): culture-dependent sorting produced different reviewed-plan fingerprints between PowerShell editions. Use ordinal canonical-key sorting. Evidence: reports/iac-cross-edition-red.txt; cross-edition regression.
- IAC-ERR-005 (fixed): Windows PowerShell treated a venv stderr warning as failure despite native exit zero. Use the explicit native process adapter with separate streams and exit-code semantics. Evidence: reports/iac-native-stderr-red.txt; native stderr regression.
- IAC-ERR-006 (fixed): an installer exit zero alone could advance dependent resources without actual convergence. Reobserve each resource and require its postcondition. Evidence: reports/iac-postcondition-red.txt; false-success regression.
- IAC-ERR-007 (fixed): packaged-host Windows path virtualization changed the venv's physical root. Resolve through trusted Python and use a validated per-user/per-home location receipt. Evidence: reports/iac-resolved-root-red.txt and iac-location-receipt-red.txt; physical-root/receipt regressions.
- IAC-ERR-008 (fixed): inherited pip target/configuration variables could redirect an otherwise owned install. Clear all PIP variables during the controlled install and restore them afterward. Evidence: reports/iac-pip-environment-red.txt; installer environment regression.
- IAC-ERR-009 (fixed): restoring an originally absent environment variable as an empty value changed process state on PS7/.NET. Explicitly remove originally unset variables. Evidence: reports/iac-unset-environment-red.txt; absence-restoration regression.
- IAC-ENV-001 (observed, not a code fix): final model API/readiness and local prose-draft checks received connection refused on 127.0.0.1:11434. No server was started or model downloaded. Operator startup remains required before real model use; see reports/IAC_IMPLEMENTATION.md and model-report-draft-attempt.txt.

## UI-MODEL-002 incidents and test coverage correction

- UI-017-001 (fixed): API key and remote-transfer consent were constructed visibly and provider/profile updates did not conditionally hide them for local Ollama. Two real-browser assertions failed before correction in reports/sidebar-017-red.txt. Initial visibility and provider/saved-profile outputs now hide local-only-unused inputs, clear values on provider changes and reveal an empty password/unchecked consent for external providers. Browser tests cover both directions and profile load.
- UI-017-002 (fixed): secondary sidebar buttons inherited Gradio's light fill because the reference Glass Box secondary tokens had not been applied to the sidebar. The user-observed screenshot and initial local/style regression identify the mismatch. Scoped CSS now uses rgba(255,255,255,.035), #f1f3f5 and rgba(255,255,255,.10), with hover/focus states. Browser computed-style assertions verify all five buttons and screenshots preserve the result.
- UI-017-TEST-001 (coverage corrected): the original profile lifecycle test relied on automatic page-load refresh instead of clicking Refresh saved profiles; some action checks also relied on status text. The revised test opens the second browser before creation, explicitly refreshes and selects the new profile, then verifies update/delete and JSON removal. Model discovery exposes a new option only after a manual refresh; applying a model changes the configured injected-client identity observed through an actual query. These fixtures do not establish real model inference or provider authentication.

## PROFILE-001 incidents

- PROFILE-ERR-001 (fixed): Save profile rejected Ollama by design despite the visible local profile editor. The store allowed external providers only and required a credential. Red evidence: reports/profiles-018-red.txt. Local metadata now supports create/update/select/apply/delete with an empty credential_ref; native vault initialization is lazy. Tests also cover provider conversion and readable Unicode/model-style names.
- PROFILE-ERR-002 (fixed): the external save wrapper collapsed credential-write and metadata-write failures into the same generic ValueError. The controller then replaced the message on Refresh and cleared choices. Red evidence: reports/profiles-018-red.txt and profiles-018-refresh-red.txt. Fixed-code ProfileError diagnostics now separate key/native/metadata phases, retain safe reasons through refresh and preserve valid choices. Raw error bodies remain private.
- PROFILE-ERR-003 (prevented with explicit validation): UTF-16 credentials could exceed the Windows 2560-byte blob limit while passing the generic ASCII format limit. The native adapter now returns key_storage_limit before writing; existing encoding/credentials remain unchanged. The synthetic oversized-input test confirms the native call is not made. This is not established as the cause of the user's reported failure.
- PROFILE-EXT-001 (original cause unresolved): the running GUI recorded an external failure inside the former save wrapper at line 238. Payload-free logs did not retain its underlying cause. A valid synthetic profile saved/read/deleted successfully with the real Windows vault in temporary storage, and a new real Gradio/store/vault test passes. No user's key or existing profile was inspected. Retry in the updated application can provide a safe fixed code; do not infer the original cause from unrelated passing fixtures.
- PROFILE-TEST-001 (coverage improved): browser profile workflows previously doubled the vault and tested the native vault separately. Added a real Gradio callback-to-store-to-Windows-vault test using unique synthetic credentials with finally cleanup. This supplies integrated evidence without paid calls or existing data.
- PROFILE-TOOL-001 (implementation correction): a text replacement initially missed the multiline generic raise, and a nested exception binding could hide the original error on cleanup failure. Focused tests exposed the missing classified codes; the corrected handler preserves the original exception and tests cover simultaneous cleanup failure. No intermediate implementation was deployed to the live GUI. Formatting also corrected semicolon-packed test statements before final Ruff verification.

## REUSE-ERR-001 — resolved and verified

The original operation-bound ledger and manager prompt forced tests and acceptance on every query. Session-owned, exact-byte grants now retain successful human-reviewed function authorization separately from fresh execution receipts. A direct second-call regression initially also exposed premature grant revocation before preparation; preparation now precedes verification and UI status polling does not revoke unchanged grants solely because the operation changed. A typing.get_type_hints adversarial test exposed an unsafe unattended classification; calls through typing are excluded. The classifier is deliberately conservative and may ask permission for harmless unsupported libraries. Same-session reuse only; no persistent trust, universal-correctness claim or capability escalation.

## NATIVE-TEST-019 — validation scheduling limitation

The native cleanup test measures global Agentix profile sets and therefore conflicts with concurrent independent live evaluators. A combined run had 27 passes and one cleanup failure while the supervised model workflow was creating profiles. After stopping only the owned disposable server, all nine native checks passed unchanged. Keep these resource-counting checks separate from live agent validation. No isolation assertion was relaxed.

## REUSE-ERR-004 / UI-REVIEW-020

The first reuse delivery was intentionally memory-only; page reload, model runtime replacement or restart discarded approval and triggered human review again. Playwright had proved consecutive queries but omitted those lifecycle transitions. The user rejected that limitation and approved protected durable authorization. ApprovalStore and WindowsDataProtection now persist successful reviewed grants outside tools; exact identity/policy checks deny stale or modified records. New Playwright coverage exercises reload, another browser, owned-server restart and source-change reapproval. The review panel was moved below Tool validation; a failing pre-change browser assertion and actual Gradio ancestry check cover its placement. Historic approvals cannot be recovered from child reports and require a first protected review.

An old AST-source test and sidebar browser assertion encoded the superseded layout; they were replaced/updated with actual component ancestry, uniqueness, geometry and visibility assertions. A real-framework fixture supplied an empty security namespace without owner_id; the fixture now supplies the required explicit owner rather than weakening the production ownership contract. Initial failures remain in reuse-020 report logs.

## UI-CONTRAST-020 — relocated review readability

Visual QA found 1.1407:1 contrast in the moved review group. The browser DOM diagnostic identified an opaque light Gradio `.styler` inside the correctly dark outer group. Scope the existing dark palette to the inner styler and verify at least 4.5:1 in Playwright. Raw red/diagnostic logs and final screenshots remain in reuse-020 evidence.
