# ADR-0002: Explicit composition and inert imports

Date: 2026-10-19. Status: accepted under REF-003.

## Decision

Place application code under `src/agentix/`. Pure settings, path policy, approval coordinator, persistence, catalog, tool operations, test runner and executor are independent of framework initialization. The orchestrator receives agents, factories and a catalog callable. The UI controller receives workflow/catalog/security/update dependencies; the view owns only widgets and event bindings.

`bootstrap.py` is the composition root. Explicit startup configures the existing logging/telemetry hooks, creates storage, constructs the LLM and agent set, builds the view and installs capture during launch. Imports do not create storage, mutate environment/stdout, patch Rich or import CrewAI/Gradio. Root compatibility modules add the checkout's `src` path through `_agentix_path.py`; that import-path adjustment is intentional and does not initialize the application.

## Compatibility choices

Keep original model/provider settings, role prompts, task order/context, fallback parsing, textual results, approval protocol, CLI behavior, labels/events and launch parameters. Lazily expose legacy model/tools/agent/UI attributes when explicitly accessed. SecurityManager remains a class facade over separated components so existing approval toggles and callbacks share the same coordinator. Explicit custom runtimes can receive their own coordinator/root, without claiming browser-session isolation.

Keep the actual execution model unchanged: tools run in-process and generated tests use the existing 30-second subprocess. Do not introduce stronger safety claims. Preserve pre-write validation fixes and independent ExecutionState histories. Retain one legacy default runtime/UI.

## Consequences and validation

Dependencies can be replaced at construction rather than by replacing imported modules. Offline tests require only the development runner; opt-in adapter tests exercise real tool schemas and Gradio bindings without model/server execution. Runtime objects are initialized later than before, an intentional startup-timing change covered by STR-01. Installed-package/installer design remains deferred; supported checkout launch commands remain the root scripts.

Logging uses package module names and adds composition/catalog diagnostics. Full log redaction, bounded capture and rotation remain subsequent policy work. General static type-checker certification, coverage percentages and OS isolation are not implied by type annotations or lint checks.
