# REF-001: Controlled refactoring

Status: phases 1–3, REF-002 defect fixes and REF-003 behavior-preserving structural refactoring are approved and implemented. SEC-005 session/approval/decision/diagnostic changes are also approved and implemented. Remaining execution-isolation/outcome/installation work awaits validation.

## Scope and requirements

User clarification: all content within the project's `generated_tools/` is out of scope. Do not inspect, refactor, document or write unit tests for that generated code. Exclude it from test discovery and coverage targets. Agentix service tests may use independent temporary fixtures outside that directory; they test the application infrastructure, not existing generated tools. Normal Agentix runtime behavior remains unchanged.

Preserve the local Gradio/CLI workflow, Ollama use, existing-tool reuse and Architect → Coder → Tester creation sequence. Preserve human approval and editing, AST cataloging and artifact naming unless a specific change is approved. Existing generated artifacts and alternative source copies are user data; do not delete, migrate or execute them during baseline work.

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| REF-01 | Tests precede refactoring | Baseline tests against unchanged production hashes |
| REF-02 | SDD/TDD | Approved contract, failing reproducer, minimal fix, passing regression |
| REF-03 | English module/class/function documentation | Review changed production contracts during phase 4 |
| REF-04 | Diagnostic logs | Bounded/redacted operation IDs, outcomes, durations and exception context, tested in phase 5 |
| REF-05 | Explicit security boundaries | Path, approval, edited-code and execution threat tests; limitations documented |
| REF-06 | Change/error traceability | Requirement/incident IDs link code, tests, documentation and verification |
| REF-07 | Local skills | Pinned origins, licenses, checksums and AGENTS.md routing |
| REF-08 | Ollama for engineering reports only | Local-only prose helper, provenance and human-reviewed evidence; no generated code/tests |
| REF-09 | Windows 11 per-user installer | Fresh environment, dependency lock, launcher, checks and clean-install validation in phase 6 |
| REF-10 | Synchronized artifacts | Code changes update tests, relevant specs, incidents and manuals |

## Baseline strategy

Import complete production modules with doubles for CrewAI constructors, tool decorators, LLM configuration and Gradio widgets. Exercise actual business functions, temporary filesystem, compilation and AST inspection. Component integration uses real subprocess unittest and dynamic execution of trusted fixtures. Test real configuration separately with import side effects intercepted.

No live browser, real decorator schema, LLM quality, multi-client isolation or installer guarantee follows from these tests. No percentage coverage claim is made. The baseline used strict xfails for the five defects; REF-002 fixes converted them to normal regressions. New confirmed defects should use strict xfails only while unresolved. Passing characterization does not certify security.

## Architecture — implemented through REF-003

`src/agentix/` now separates startup configuration, contracts/state, approvals, storage, execution, catalog, CrewAI adapter, orchestration and Gradio controller/view. Root entrypoints remain compatible and dependency construction is explicit. See `003-structural-refactoring.md` and the current technical architecture.

Approve security behavior changes explicitly: resolved path containment, request identity, defensive state snapshots, final edited-content validation, bounded output and execution policy. A subprocess provides crash/time boundaries but does not confine arbitrary Python. Choose OS-enforced isolation in a dedicated approved threat-model decision.

## Proposed installation contract — not implemented

Windows 11, per-user, no administrator rights. Create a fresh supported Python environment, install locked dependencies, validate Ollama/model availability and provide a launcher and diagnostics. Preserve generated artifacts on upgrade/uninstall. Do not distribute the copied `.autotool` environment or silently download large models. Document network prerequisites. Exact packaging and implementation await phase 6 approval.

## Approved-phase completion gate

Provide governance, skills, English current architecture/specifications, test command and raw results, incident reproducers, reviewed report with local-model provenance when possible, and a production-hash comparison. Then present a concrete production change proposal for approval.
