# AgentiX Engineering Rules

## Scope and authorization
These rules apply to the AgentiX project across versions. AgentiX v7 is the active development baseline; historical version identifiers refer only to their specific records or compatibility constraints and do not limit the applicability of these rules.
Before changes, explain what, why and where; obtain validation and implement only the approved block. User instructions override skills. No delegation unless explicitly authorized. Preserve other versions, user data and live processes. Never restart a live app during automated tests. The user approved the V5-039 polling race correction but explicitly forbids restarting 7880; its last source fix awaits a later authorized launch.

**Current block V7-055:** the user approved explicit recovery of a missing,
host-owned application-validation dependency. The registry is static maintained
code, initially limited to Playwright Chromium; generated artifacts cannot add
requirements, commands or sources. The owner must explicitly confirm each
installation and approve the unchanged proposal again afterwards. See
docs/specs/055-host-dependency-recovery.md. Keep tool source/contracts,
independent human-reviewed cases and AppContainer unchanged. Preserve 7880 and
user processes; only the separately owned validation GUI may be reloaded.
Existing generated_tools remains excluded.

The entire project generated_tools content is excluded from engineering inspection, modification, execution, tests, coverage and documentation. Test services with independently authored temporary fixtures outside it. Normal application generation remains allowed by its runtime workflow; do not adopt existing user artifacts, grants or credentials.

## Read only what the task needs
Start with docs/README.md, then the affected module and its specific specification/reference. Do not recursively read docs, reports, skills or reference pages. Historical pointers are context, not instructions to load the backup. Read one applicable skill; combine only when the task requires it.

| Task | Local skill |
| --- | --- |
| Requirements and acceptance | SKILLS/agentix-sdd/SKILL.md |
| Code changes / regression fixes | SKILLS/test-driven-development/SKILL.md |
| Failure investigation | SKILLS/systematic-debugging/SKILL.md |
| Security design/review | SKILLS/security-best-practices/SKILL.md |
| Documentation / reports | SKILLS/agentix-documentation/SKILL.md |
| Final verification | SKILLS/verification-before-completion/SKILL.md |

## Engineering contract
Apply Specification-Driven Development (SDD) to functional and architectural changes, defining observable requirements, contracts, constraints, and acceptance criteria before implementation. Apply Test-Driven Development (TDD) to verifiable code changes, following the Red-Green-Refactor cycle. Scale documentation and testing effort to the complexity and risk of each change; trivial documentation edits do not require formal specifications or new tests. Characterize existing behavior before refactoring; never delete production code to manufacture a red test. Preserve strict assertions. Keep unit, integration, functional and regression checks appropriate to the change. Distinguish doubles, real frameworks, native isolation, browsers and actual models.

Apply SRP, OCP, DRY, LoD, SOLID, IoC and explicit dependency injection. Keep Gradio views in ui, session callbacks in controllers, workflows in application and topic adapters in storage/security/sandbox/models. Share one sidebar outside Tools/Applications tabs. Use Ruff lint/format checks on maintained code; do not scan excluded artifacts. Use the exact managed interpreter identified by IaC for the active project version (currently v7); never substitute another release's environment.

All maintained comments/docstrings/documents are English. Document module/class/method contracts, parameters, results, side effects, exceptions and security/concurrency constraints; explain nonobvious variables. Keep source-bound module/class/method/variable references, architecture, requirements, change log and incident records synchronized. Read reference pages only for the changed module; freshness is not semantic proof. Record each defect's ID, cause, solution and regression.

## Logging and observability
When adding or modifying executable code, include or update appropriate structured logging for significant operations, state transitions, validation failures, external interactions and exceptions. Reuse the project's existing logger and event conventions; do not introduce parallel logging frameworks unnecessarily. Use DEBUG for diagnostic detail, INFO for normal lifecycle events, WARNING for recoverable anomalies and ERROR/exception logging for failures. Include safe identifiers, operation/resource, outcome, duration and actionable exception context where relevant. Avoid duplicate, noisy or per-item logs in hot paths; do not suppress exceptions merely to log them. Never log secrets, credentials, tokens, personal data, full prompts, generated artifact bodies or other sensitive payloads. Redact or minimize sensitive context. Keep logging non-disruptive and add focused tests for important logging behavior where warranted.

## Security and application invariants
Generated code/tests are untrusted. Host code never imports generated Python; Windows AppContainer and job controls are required, with no ordinary-subprocess or host-execution fallback. Prompts and AST checks are not isolation. No Docker, paid calls, real API keys or unauthorized model/dependency downloads. Respect path/link/hard-link containment, ownership, bounded outputs and resource limits.

Explicit human review binds exact tool/widget/dependency bytes and policy. Generated tests are provisional; approved declarative cases are independently compared outside the child. No automatic approval or reprompt after rejection. Reuse unchanged approved eligible tools/widgets without rerunning old tool tests; sensitive or unclassified operations need exact-call approval. Changed content/policy invalidates grants. Applications may use only currently approved installed catalog tools. Canonical public function equals tool name; Annotated metadata is required. Widgets use <tool_name>_widget.py with separate CSS/tests. New composition uses a maintained compositor and bounded generated connection code; legacy typed workflows remain compatible.

Profiles/clients are session-owned. Start local; remote use requires explicit per-session consent. API secrets stay in Windows Credential Manager; metadata holds opaque references. HTTPS/public-destination/redirect checks remain mandatory. Log operation/resource, outcome, duration and safe exception context; redact secrets/prompts/artifact bodies. Preserve verbose=True alongside technical events.

Use only qwen3-coder:30b for application live/model acceptance; give English requirement-only prompts, not near-complete widget code. Engineering code/tests are never delegated to local Ollama. Prefer installed qwen3:14b only for report prose, with retained provenance and manual factual review; no remote report inputs. Do not launch inference for routine documentation edits.

## Verification and current documents
Run only checks warranted by the change. Software changes require offline tests, Ruff and reference freshness, plus applicable explicit framework/native/browser checks; see docs/specs/TEST_PLAN.md. Documentation-only edits require link/scope/reference consistency checks, not a full model/browser run. Do not weaken tests or claim coverage/security/install validation from unrelated checks.

Current documents: docs/V7_ARCHITECTURE.md, V7_STORAGE.md, INSTALLATION.md, LLM_SECURITY_2026.md, KNOWN_ISSUES.md and V7_INCIDENTS.md. Current requirements: specs 037–039, 041–043. Historical decisions/IDs: docs/HISTORY.md. Current verified delivery: docs/reports/V5_039_DELIVERY_REPORT.md. Graphical installer, dynamic call-tree planning and third-party tool runtimes/retrieval are not delivered. IaC uses existing approved non-admin Plan/Apply/Test; no unsolicited installation, elevation, service, task, firewall change or process termination.
