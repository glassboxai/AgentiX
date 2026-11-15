# AgentiX v3 architecture and quality guide

## Scope and dependency direction

The root entrypoints are compatibility facades. `app.py` starts the GUI; `main.py`
starts interactive terminal review. `_agentix_path.py` enables checkout imports.
`config.py`, `custom_tools.py` and `security_manager.py` preserve existing import
contracts. Removing those facades would break existing callers and regression tests.
The package version is 3.0.0; the import namespace remains `agentix`.

Interfaces and immutable configuration sit below application services. Adapters and
UI components depend on those services. `bootstrap.create_runtime` is the composition
root: it selects the execution boundary and injects the same instance into tool
execution, provisional testing and acceptance evaluation. An optional structural
`ExecutionBackend` dependency supports independently authored test doubles. Production
composition defaults to WindowsSandbox; a failed OS boundary never selects host execution.
The protocol describes compatibility, not an isolation guarantee.

## Responsibility and state ownership

| Modules | Responsibility and important state |
| --- | --- |
| settings, paths | Explicit configuration and validated storage/path boundaries. Paths are resolved before containment decisions. |
| contracts | Dependency interfaces and shared type contracts, including ExecutionBackend. |
| bootstrap | Explicit process policy and runtime composition. Startup disables Gradio analytics as well as the existing telemetry policy. Imports remain inert. |
| approvals, security | Owner-bound, identified, expiring human decisions; defensive snapshots and approved writes. Pending state belongs to the session. |
| storage, catalog | Approved artifact persistence and tool discovery. Catalog visibility is not execution permission. |
| verification | Content-bound query receipts and bounded session-only reuse grants. A new operation expires result receipts, while intact successful reviewed tools may be prepared for reuse. |
| testing | Provisional unittest orchestration; a child report alone cannot authorize use. |
| acceptance | Human-reviewed declarative cases and host-side expected/observed comparison. Expected values remain outside the child. |
| execution, sandbox, windows_process, sandbox_worker | Invocation validation, native AppContainer/Job Object provisioning, bounded child execution and JSON result transport. Provisioning failures deny execution. |
| tools | Application tool API joining storage, approvals, testing, acceptance and execution through explicit dependencies. |
| decisions, orchestration, workflow_policy | Manager decisions, preserved requirements and approved stage handoffs; execution-backed final answers. |
| diagnostics | Owner-scoped verbose and technical activity routing, bounded diagnostics and exception context. |
| adapters | CrewAI integration, schema registration and callbacks at the framework boundary. |
| ui | Gradio components, presentation/assets, session state and review callbacks. Rendering does not confer authorization. |
| cli | Interactive terminal approval and acceptance review using the same application services. |
| tools directory | Offline reference generation, report drafting and disposable validation helpers; not generated application tools. |
| tests directory | Independently authored fixtures and unit, integration, functional and regression checks. |

For each individual module, class, method and variable, the [source reference](reference/README.md)
provides the current contract, scope, type annotation when present, lifetime and source
fingerprint. Parameters, imports, constants, local bindings, attributes and comprehension
bindings are inventoried separately. Runtime-dependent types are labelled explicitly;
no type is invented and no assigned value or secret is copied into documentation.
The enclosing callable contract supplies the purpose of algorithm-specific locals.

## Applying design principles

SRP is expressed by the boundaries above: presentation, approval, persistence and
execution have separate ownership. OCP uses narrow dependency protocols where actual
variation is required, rather than adding speculative abstraction. SOLID includes
substitutable provider contracts, small role interfaces and dependencies directed toward
contracts. The injected backend is shared intentionally, so tests cannot silently validate
one executor while production acceptance uses another.

IoC is explicit in bootstrap composition; DI passes services to constructors and the
runtime factory. DRY preserves common validation, workflow instructions and service
behavior used by both GUI and CLI. LoD favors service methods over reaching into adapter
internals; framework schema and callback boundaries remain explicit integration points.
Existing compatibility facades are intentional exceptions to structural simplification.
These are review rules and architectural choices, not properties proven by a linter.

Ruff checks import hygiene and the configured rules; its formatter provides consistent
layout. Type annotations document contracts but are not a substitute for runtime input
validation. JSON size/type checks, resolved path containment, identified approvals,
content-bound evidence and bounded process output remain security responsibilities.

## Testing and documentation contract

Unit tests exercise services with fake model and OS boundaries. Integration tests cover
real framework schemas/callbacks and, separately, native Windows process isolation.
Functional browser tests exercise a disposable loopback GUI with trusted temporary
fixtures. Regression tests retain the historical security, session, approval, handoff,
rendering and compatibility reproductions. Test names describe behavior; new fixes need
a failing reproduction, corrected result and incident entry. Do not weaken assertions.

The default suite is offline. Opt-in tests do not start models or restart an existing
application. Native and browser tests must never execute existing generated artifacts.
No finite suite proves arbitrary generated programs correct or malicious tests honest.
Human acceptance and independent host comparisons remain mandatory.

English docstrings describe module/class/callable contracts. Comments explain non-obvious
security and ownership decisions. Reference documents are generated from ASTs and source
hashes; `--check` detects stale, missing and unexpected entries. The regression suite runs
this check. Regenerate after formatting, then review semantics: inventory consistency
cannot establish that a description is complete or true. Update specifications, this
architecture guide, incidents, change log, installation instructions and tests together
when their behavior changes. Historical evidence stays immutable and is dated separately.

## Packaging and cleanup

The curated copy excludes the old unreferenced custom_tools_.py alternate, bytecode,
cache directories, root run logs, document rendering intermediates and the machine-bound
.autotool environment. Existing generated_tools content was neither enumerated nor copied.
Historical reports and final proposal documents remain evidence, not disposable runtime
files. The copy manifest records exclusions and original hashes. New package hashes are
recorded separately; they must not overwrite historical baseline/fix hashes.

Direct dependency pins describe the observed runtime, not a fully resolved transitive lock.
No clean-machine install or installer verification is implied by using the existing local
interpreter. Third-party log policy and crash-atomic persistence remain deferred. The new
widget/assembly agents require their own approved specifications and TDD blocks.

## IAC-001 desired-state boundary

Infrastructure is maintained separately under infra. The typed application Settings
accepts explicit port/browser/storage overrides; the view stays loopback-only. Legacy
entrypoints keep their defaults. A PowerShell entrypoint loads validated data and a
pure planner; the planner binds the checkout, configuration, source and observed state.
The native DSC command resource delegates to the convergence service with injected
Observe/Set boundaries. Querying state, invoking native processes, checking signatures,
planning and applying resources are separate functions. The resource allowlist is
intentionally closed to arbitrary commands or plugins; extension requires review.

IoC is expressed through DSC get/test/set and provider injection in convergence/tests.
Shared runtime/service logic remains in Python, rather than being duplicated in shell
launchers. The independent venv and deterministic launchers are desired-state resources,
not installed application services. Hashes enforce download/install identity; package
version observations detect declared dependency drift and do not attest every installed
file. Physical-root resolution accounts for Windows packaged-host virtualization without
relaxing reparse-point containment. See ../infra/README.md for lifecycle, ownership,
parameters, units, failure behavior and recovery. The protocol/currency follow-ups from
V3-LIVE-004 remain outside this infrastructure block.

## SEC-LLM-001 model configuration boundary

The application remains a modular monolith with GUI/CLI adapters and an explicit bootstrap composition root. ModelProfile is immutable validated configuration; SessionModelConfiguration owns provider activation for one controller. SavedProfiles owns user-local metadata, revision checks and serialized persistence. WindowsCredentialVault is the native secret-storage adapter; runtime/vault/catalog/resolver factories are explicit dependencies. Providers are created through the existing CrewAI LLM boundary, with a sync/async request interceptor for remote destinations. Profile metadata and credential references are separate from generated artifacts and acceptance data. No new provider framework or microservice is introduced.

The Gradio native Sidebar hosts settings and the single authorization/review panel. Server callbacks recheck ownership; the controller serializes settings changes against work and review. Applying a model composes fresh services and verification state. Profiles are Windows-user scoped; consent, selected model and mutable clients are session scoped. Credentials are never dependencies of the generated-worker execution contract.

Model choices and work limits are explained in MODEL_CONFIGURATION.md; the OWASP mapping and residual threats are in LLM_SECURITY_2026.md. IoC does not imply an external model has been functionally validated; framework transport tests are distinct from paid inference.

## UI-MODEL-002 presentation refinement

Provider-specific secret/consent visibility is a view responsibility. It is updated on initial rendering, provider selection and saved-profile outputs; backend owner and consent checks are unchanged. Scoped sidebar CSS reuses the NexisNodes/aXiom Glass Box palette without changing primary/destructive button semantics. Browser fixtures make refresh and runtime replacement observable rather than relying solely on status text; no new domain service or dependency is introduced.

## PROFILE-001 unified persistence and diagnostics

SavedProfiles now stores Ollama records with an empty credential_ref alongside legacy external records. Provider conversion uses the existing version/owned-reference/retired-cleanup mechanism. DeferredCredentialVault is a lazy adapter: local metadata operations do not construct native credential services. ProfileError owns a closed catalog of public messages/codes and an optional validated numeric Windows status; raw vendor messages never become browser output. The controller retains only the safe last-save diagnostic through refresh and preserves valid catalog choices when an action fails.

The boundary is verified with offline failure injection, real browser local/remote workflows and an additional in-memory real Gradio callback connected to temporary metadata and a real unique Windows credential. A passing doubled-vault browser scenario alone is no longer presented as proof of the native GUI/store/vault combination. The actual user's historical external failure remains unclassified until a safe diagnostic is observed.

## REUSE-001 session reuse

Successful host-accepted execution publishes a bounded, memory-only grant owned by VerificationLedger. Preparation checks exact implementation/test bytes and owner/lifecycle before rebinding acceptance to a new operation. Fresh execution receipts remain operation-bound. A conservative AST vocabulary gates unattended calls; unsupported constructs require manual exact-call permission. AppContainer permissions remain unchanged. No unprotected metadata field or model message can establish a grant. This initial session-only scope is superseded by the protected durable approval design below.

## Durable approvals and review layout (REUSE-002)

ApprovalStore is an injected persistence port at the runtime composition root. Production uses WindowsDataProtection; ordinary tests use an authenticated fixture double, browser/native opt-in tests use actual DPAPI with temporary storage. Successful host-accepted calls publish bounded sealed records containing source/test hashes, root/tool identity, reviewed functions/contract and a fingerprint of named maintained security modules. No generated code or disk marker supplies its own authorization. VerificationLedger restores approval into a fresh query while keeping execution receipts owner/query-bound. Closing a browser expires its session state but retains the Windows user's durable approval. Changes, policy drift, corruption and explicit revocation deny reuse. No native permissions are expanded.

The left Sidebar contains model configuration. The sole Authorization & Test Review accordion, editor and decision buttons appear in the right column immediately below Tool validation. Callback ownership and displayed-request checks remain unchanged. Real Gradio ancestry and Playwright geometry/visibility checks verify the layout.
