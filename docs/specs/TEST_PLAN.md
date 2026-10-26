# Baseline test and requirement mapping

Current ACCEPT-001 verification: `../reports/HUMAN_ACCEPTANCE.md`. Declarative schema/host comparisons, mandatory manual review, edits/rejection/expiry/cancellation, forged unit reports, covered functions, operation/content races, revocation, restore attacks and safe logs are in `test_human_acceptance.py`. Escaped review/result panels are in `test_acceptance_ui.py`. Real Gradio request preprocessing and edited acceptance are in `test_gradio_acceptance.py`. Native typed observations and the human-reviewed lifecycle extend `test_windows_isolation.py`. Earlier counts and evidence below are historical phase snapshots.

Current EXEC-002/FLOW-002 verification is in `../reports/ISOLATED_PIPELINE.md`: 212 default tests, eight opt-in native Windows tests and two opt-in actual-framework tests. `test_pipeline_verification.py` covers evidence lifetime, identity/content races, syntax, failed/excluded suites and manager gating. `test_sandbox_protocol.py` covers malformed frames and unsupported hosts. `test_windows_isolation.py` verifies real process/file/network/resource/environment boundaries with temporary fixtures. The default OS double is in `tests/trusted_sandbox.py`; it is not an isolation implementation. Earlier counts below are historical phase snapshots.

Current SEC-005 evidence is in `../reports/SESSION_SECURITY.md`. New suites cover strict decisions/payload-free diagnostics (`test_decision_security.py`), identified approval races (`test_approval_identity.py`), bounded/owner-checked registry and activity (`test_sessions.py`), production runtime/client independence (`test_ui_runtime_isolation.py`), parallel browser callbacks and provider tool threads (`test_session_workflows.py`), plus real Gradio State/request/editor/unload preprocessing (`test_gradio_session_routing.py`). Approved behavior changes replace the prior fallback/name-normalization/manual-response assertions; other regressions remain active.

Status: the 131-case corrected baseline is retained through REF-003. Current tests use explicit service composition rather than module replacement. Additional tests cover inert imports, composition, CLI, compatibility and real framework adapters; see `../reports/REFACTOR.md` for current counts. No known-defect xfail markers remain.

The project's `generated_tools/` content is excluded from tests, discovery, coverage, inspection and documentation. Component fixtures are independently authored and created outside that directory in temporary storage; no tests target existing generated tool implementations.

| Area | Test module | Behaviors / associated requirements |
| --- | --- | --- |
| Approval and storage | `tests/unit/test_security.py` | UTF-8 write/append, edits including empty text, directory/file denial, timeout cleanup, real thread handshake, write errors, valid and escaping paths; REF-01/02/05, SEC-001/002/003 |
| Tool operations | `tests/unit/test_tools.py` | Fence removal, syntax validation without execution, specifications/incidents, reads, dynamic arguments/errors, unittest outcomes/timeouts/spawn errors and rejection; REF-01/02/05, SEC-004 |
| Catalog and orchestration | `tests/unit/test_orchestration.py` | AST inspection without execution, visibility/order/errors, manager response formats, legacy fallback, task context order and failure propagation; REF-01/02, FLOW-001 characterization |
| UI controller | `tests/unit/test_app.py` | Stream mirroring/ANSI cleanup, busy/empty queries, worker success/failure, activity/final rendering, editor preservation and callbacks; REF-01/02, UI-001 |
| Configuration | `tests/unit/test_config.py` | Defaults, environment overrides and expected initialization boundary without live services; REF-01 |
| Component lifecycle | `tests/integration/test_artifact_workflow.py` | Real persistence → compilation → trusted subprocess tests → AST catalog → execution; real failing fixture records an incident; REF-01/02 |
| Reporting helpers | `tests/integration/test_evidence_collection.py` | Missing/present distribution metadata, local-only endpoints, redirect refusal, completed prose output/provenance; REF-06/08, ENV-001 |

REF-003 implements English module/class/function documentation, annotations and component diagnostics; further logging/security policy is deferred. REF-07 is verified through provenance/license review and structural validators. REF-09 has no installer test because no installer is implemented. REF-10 is reviewed against implementation and documentation together.

New modules: `test_import_boundaries.py` checks root/package imports in a clean subprocess with filesystem-creation guards; `test_composition.py` checks settings, dependency wiring and view events; `test_cli.py` checks exit aliases and error recovery; `test_compatibility.py` checks lazy exports, exception identity and stdout restoration. The opt-in `test_framework_adapters.py` checks actual CrewAI schemas and Gradio bindings, with no model/server startup. The original configuration test now verifies the same values through explicit settings and LLM construction; the old import-side-effect assertion was intentionally superseded by STR-01.

## Interpretation

The baseline's 105 collected cases include parametrized cases, reporting helpers and five strict xfails; they are not 105 independent end-to-end scenarios. A test count is not a coverage metric. No mutation testing or statement/branch coverage measurement has been performed. Separate framework compatibility, multi-client concurrency, Windows link/reparse behavior and OS isolation tests are required during later approved blocks.

When moving production symbols into a package, preserve behavioral assertions while changing import/dependency setup deliberately. Keep legacy fallback tests only until an approved specification changes that behavior. Remove each expected-failure marker only when its underlying defect is fixed and verified.
