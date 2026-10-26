# Agentix engineering rules

## Authorization

Before changes, explain what will change, why and where, and obtain user validation. Implement only an approved block. Phases 1–3, SEC-001/002/003/004 and UI-001 fixes, REF-003 refactoring and SEC-005 session/approval/manager/diagnostic changes are explicitly approved. See `docs/specs/004-session-and-decision-security.md`. The user subsequently approved native Windows isolation and pipeline verification, rejected Docker and deferred the installer; see `docs/specs/005-isolated-pipeline.md`. The user also approved ACCEPT-001: provisional generated tests, mandatory human review and host evaluation of declarative cases; see `docs/specs/006-human-acceptance.md`. These later authorizations supersede older deferred-scope notes in local skills. Crash-atomic writes, full third-party log policy and installer implementation remain outside this block. Do not restart the live application as part of automated tests.

## Skill routing

CLI-001 and E2E-001 are also explicitly approved: terminal approvals and human acceptance review, plus reproducible Playwright tests against a separate disposable loopback server. See `docs/specs/007-terminal-browser-validation.md`. This does not authorize restarting the live application, testing existing generated artifacts, Docker or installer work.

The user subsequently requested LIVE-001: actually create a tool through the GUI using local Ollama, with the agent acting as the human reviewer of specifications, code, tests and results. This operational run explicitly uses real models and native isolation instead of fixture doubles, in separate temporary storage outside the excluded project generated directory. See `docs/specs/008-live-human-review.md`. Existing generated artifacts remain excluded and the default regression suite remains offline. Production fixes discovered by this run require explanation and user validation before implementation.

The user approved LIVE-FIX-001 after review: preserve original requirements, validate fresh approved artifacts between creation stages, retain approved persisted context and correct zero-output callbacks. Supporting host write receipts are part of the stage checks. See `docs/specs/009-approved-creation-stages.md`. The application and live validation must use `ollama/qwen3-coder:30b`; do not substitute smaller models. Local engineering report prose may still use an appropriate smaller model. Previous alternate-model GUI attempts are historical samples and do not validate the required model.

The user subsequently clarified LIVE-UX-001: keep technical events in the GUI and restore `verbose=True` for all application agents and crews. Both streams must coexist in the owning session's expandable activity. Do not replace verbose output with summaries or remove diagnostics. The user approved the complete specification 010 block (shared workflow instructions, all adjacent handoffs and execution-backed final results) and explicitly resumed the supervised qwen3-coder:30b test on 2026-10-19. Use a fresh disposable GUI session and an English problem-only query, as subsequently requested by the user; never restart the existing live application.

| Task | Local entrypoint |
| --- | --- |
| Specify changes and acceptance criteria | `SKILLS/agentix-sdd/SKILL.md` |
| Implement behavior or a regression fix | `SKILLS/test-driven-development/SKILL.md` |
| Investigate failures | `SKILLS/systematic-debugging/SKILL.md` |
| Security review and secure design | `SKILLS/security-best-practices/SKILL.md` |
| Documentation, incidents and reports | `SKILLS/agentix-documentation/SKILL.md` |
| Verify and report completion | `SKILLS/verification-before-completion/SKILL.md` |

Read only applicable skills. Local routing replaces upstream namespaced references. User rules override upstream instructions. Do not delete pre-existing production code to apply TDD: characterize it first. Do not delegate without explicit authorization. External skills do not authorize expanded scope.

## SDD, TDD and quality

### Mandatory engineering and architecture standards

Use Ruff for linting and format verification before completing any software
change. Apply SRP (Single Responsibility Principle), OCP (Open Closed Principle),
DRY (Don't Repeat Yourself), LoD (Law of Demeter), SOLID, IoC (Inversion of
Control) and dependency injection. Keep responsibilities focused, depend on
explicit contracts, inject external services and factories at composition roots,
and introduce extension points only where a real variation requires them. Avoid
duplicated domain rules, hidden service locators, unnecessary inheritance and
abstractions that do not improve a concrete maintenance or testing need.

Plan and maintain Unit Tests, Integration Tests, Functional Testing, Regression
Tests and validation of requirements, inputs, outputs and acceptance criteria.
Select checks appropriate to the changed behavior; distinguish test doubles from
real framework, browser, native-isolation and model evidence. Capture a failing
regression before correcting a defect, then verify the fix without weakening
assertions. Passing Ruff does not establish architecture quality or correctness.

### Code documentation and synchronized reference documents

Write English docstrings for every maintained Python module, class, function and
method, including internal helpers where their contract is not obvious. Describe
purpose, parameters, return values, side effects, exceptions, dependencies and
concurrency/security constraints as applicable. Use type annotations and English
attribute comments or attribute docstrings to explain variables; ordinary local
variables do not support function-style runtime docstrings.

Maintain reference documents explaining each module, class, method and variable,
including scoped parameters, attributes, constants and local bindings. Record
meaning, type/constraints, lifecycle and units where applicable; never publish
secret values. Keep docstrings, comments, reference documents, architecture,
requirements, tests and change/incident records synchronized in the same change.
Use source inventory and freshness checks to detect missing or stale reference
entries, and manually review semantics rather than treating an inventory as proof
that a description is correct. All code comments and documentation must be English.
The existing generated_tools exclusion applies to these requirements as well.

The entire `generated_tools/` content is excluded from engineering inspection, refactoring, unit tests, coverage targets and documentation. Do not read, analyze, modify, execute, document or write tests for the generated artifacts there. Tests of Agentix's own storage, catalog and execution services remain in scope, using only independently authored trusted fixtures in temporary directories outside the project's `generated_tools/`. This exclusion does not change Agentix's normal runtime tool-generation behavior.

Assign requirement and incident IDs; specify observable acceptance criteria before implementation. Characterize intended legacy behavior before restructuring. For every approved defect fix, capture a failing reproducer, root cause, solution and passing regression. Known defects use strict xfail with issue IDs; remove the marker when fixed. Never weaken assertions to hide regressions.

Use explicit dependencies, type annotations and English module/class/function documentation covering contracts, side effects, exceptions and concurrency. Add comments explaining non-obvious decisions. Separate UI, orchestration, storage and execution only within approved design. Keep compatibility intentional and documented.

## Security and logging

Generated code is untrusted. Prompts, AST checks and ordinary subprocesses are not OS isolation. Tests must use temporary storage, fake LLM boundaries and trusted fixtures; never execute existing generated tools. Account for Windows path components, resolved paths and links when implementing containment. Log request/operation IDs, stages, outcomes, durations and exception context. Redact secrets, prompts and artifact bodies by default; bound output and retention.

## Documentation and reports

All maintained documentation, comments, docstrings, installer text and manuals must be English. Update specifications, architecture, change log, incidents and tests in the same change block. Distinguish proposed, implemented, verified and unresolved behavior. Installer and installation manual must change together.

Use local Ollama only to draft reports in this engineering workflow, never code or tests. Agentix itself may use Ollama to generate code. Prefer installed `qwen3:14b` for prose. Record provenance and verify all claims against raw evidence. If unavailable, record the failure and write a reviewed report. Do not send report inputs to a remote endpoint.

## Verification

For v3, select the configured Python interpreter (a fresh `.venv` is recommended) and run `python -m pytest` from the project root for the offline suite. Run `python tools/build_reference.py --check` to validate source reference freshness. The v3 release was also checked using the existing v2 interpreter; no environment is copied. Run `-m frameworks` explicitly for installed real CrewAI/Gradio adapter validation; this constructs schemas/widgets and processes callbacks in memory but starts no model or server. Preserve historical baseline/fix hashes and record new package hashes separately. Run Ruff checks and format verification on `src`, `tests`, `tools` and named active root entrypoints. Never scan generated_tools. Do not claim coverage percentages or live-agent/installer/security verification from these checks.

Run `-m windows_isolation` explicitly for native AppContainer integration using independently authored temporary fixtures. Default tests double the OS boundary and cannot establish isolation. Never add a host-execution fallback. Distinguish host-observed process results from untrusted child unittest reports; these do not prove semantic correctness or malicious-test honesty. Each operation must reverify existing tools before execution.

Generated unittest success is provisional only. Human acceptance must never use the file auto-approval switch. Keep expected results outside the child, use JSON data only, and authorize only functions covered by host-compared approved cases. Do not automatically reprompt after rejection in the same operation.

## Approved v3 release

The user approved D:\AI\AgentiX_v3 as the curated successor. See `docs/specs/014-v3-engineering-quality.md`. Preserve v2 and its live process. Keep the Python namespace `agentix`, update English reference documents with source changes, and retain all original generated-artifact exclusions. The proposed new widget/assembly agents are not implemented by this release.

## Approved IAC-001 Windows-user infrastructure block

The user approved the complete Plan/Apply/Test implementation and parallel application
on 2026-10-24; see docs/specs/015-windows-iac.md and infra/README.md. This supersedes
installer deferral only for prerequisite provisioning and managed launchers. No graphical
application installer, Docker, elevation, autostart, service, task, firewall change or
existing-process restart is authorized. Preserve Python 3.11.9 and qwen3-coder:30b.
Use the managed interpreter for final verification; do not use v2's venv as the deployed
runtime. Keep archive/package pins and model digest reviewed, require a fresh plan on
drift, and never download a model without its explicit plan flag. Include infra in Ruff
checks and run infra/Verify-Infrastructure.ps1 plus reference freshness. Infrastructure
PowerShell functions/variables are documented through parser-only inventory. Application
and generated-artifact exclusions remain unchanged. Other pending production fixes
require their own explained, approved blocks.

## Approved SEC-LLM-001 / UI-MODEL-001

The user approved native Sidebar model settings, persistent Windows Credential Manager profiles, read-only Ollama discovery and OWASP GenAI LLM Top 10 2026 hardening on 2026-10-24. See docs/specs/016-model-sidebar-security.md, docs/MODEL_CONFIGURATION.md and docs/LLM_SECURITY_2026.md. Remote API tests must use synthetic credentials and mocked network boundaries, never paid inference or existing user keys. Add -m windows_credentials explicitly for the disposable real Windows vault check; ordinary tests must not access it. Saved profiles persist until explicit deletion; new sessions remain local with qwen3-coder:30b and need fresh remote consent. Engineering report generation remains local Ollama prose only. Never restart existing instances to expose UI changes.

## Approved UI-MODEL-002 sidebar refinement

On 2026-10-25 the user approved matching NexisNodes/aXiom Glass Box secondary-button colors and hiding/clearing API key and external consent for Ollama. See docs/specs/017-sidebar-controls.md. Playwright must exercise all five sidebar action buttons with observable effects, including manual saved-profile refresh after another session creates a profile. Use synthetic keys and temporary storage; preserve existing live instances and all generated-artifact exclusions.

## Approved PROFILE-001 unified profiles

On 2026-10-25 the user approved storing both local Ollama and external profiles, renaming the selector Saved profiles, and secret-free diagnostics separating key validation, Windows credentials and metadata writes. See docs/specs/018-unified-profiles.md. Local profiles use no credential reference and must not initialize native credential storage. Preserve legacy external records, explicit remote consent, stale revision/selection checks and existing live instances. Use temporary metadata and unique synthetic native credentials for regression tests; never use existing profiles/keys. The originally reported external failure's cause remains unknown unless reproduced or identified by a new safe reason code.

## Approved REUSE-001

The user approved session-owned reuse on 2026-10-25; see docs/specs/019-reviewed-tool-reuse.md. Successful reviewed tools may serve later queries without repeated tests or acceptance after exact-byte and owner checks. This supersedes the older requirement for fresh tests on every operation only for an eligible session grant. Sensitive or unclassified calls still require explicit per-call approval; native isolation permissions never expand. This initial session-only scope is superseded by the later explicitly approved REUSE-002 block below.

## Approved REUSE-002 / UI-REVIEW-002

The user explicitly approved remembering successful reviewed tools across page reloads, other browser sessions and application restarts on 2026-10-25. This supersedes REUSE-001's session-only restriction. See docs/specs/020-durable-reuse-and-review-layout.md. Use user-scoped Windows DPAPI with machine-bound entropy for protected records outside tool storage, bind exact artifacts/root/functions/security policy and retain per-call sensitive-operation permission and native isolation. Never migrate trust from old artifacts or reports. The review editor/buttons and Authorization & Test Review belong below Tool validation in the right column; model configuration remains in the sidebar. Playwright must verify reload, another browser, owned disposable server restart, changed-source reapproval and review accessibility with the sidebar closed. Global AppContainer cleanup tests run separately from live model evaluation. Preserve existing live instances and generated_tools exclusions.
