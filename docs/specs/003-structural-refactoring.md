# REF-003: Behavior-preserving package refactoring

Status: approved by the user on 2026-10-19 and implemented. Verification is in `../reports/REFACTOR.md`.

## Scope

Move application responsibilities into `src/agentix/`, retaining root compatibility entrypoints. Preserve the five fixed defects, tool-result strings, prompts, task/context ordering, manager fallback, CLI exit aliases, approval semantics, UI labels/events and launch settings. Do not access project `generated_tools/` content. All artifact tests use independent temporary fixtures.

## Components and acceptance criteria

| ID | Responsibility | Acceptance |
| --- | --- | --- |
| STR-01 | Pure settings and explicit bootstrap | Importing application modules does not create directories, LLMs, agents, UI, alter stdout/environment or patch Rich; startup does so explicitly |
| STR-02 | Paths, approvals and persistence | Separate modules retain all path/approval/edit regression assertions; storage receives its approval/path dependency explicitly |
| STR-03 | Catalog and execution | AST catalog, in-process executor and subprocess test runner have separate responsibilities; trusted component lifecycle tests still pass |
| STR-04 | Orchestration and CrewAI | Orchestrator receives factories, agent set and catalog; agent/tool registration happens only at startup and preserves original prompt/tool assignments |
| STR-05 | UI and controllers | Instance controller receives workflow/catalog/security/update dependencies; view construction is explicit; existing state scope remains unchanged |
| STR-06 | Entry compatibility | `python app.py` launches the same UI, `python main.py` launches the same CLI; legacy configuration/security/tool imports remain available, with lazy construction for runtime objects |
| STR-07 | Quality and traceability | English module/class/method contracts, annotations, rationale comments, useful logs, before/after evidence, current architecture and change log |

## Test-first sequence

Run the existing 131 cases before moving code. Add failing tests for pure imports, settings, explicit UI/runtime construction and compatibility routing before implementing new contracts. Adapt fixture wiring to inject dependencies; preserve existing behavioral assertions except import-time initialization assertions intentionally replaced by STR-01 tests. Run the suite after each extraction group. Do not claim live model or browser verification from mocked tests.

## Deferred changes

Session isolation, correlated approvals, manager schema/fallback changes, execution sandboxing, output/log retention policy, atomic writes and installer implementation are outside this block. Existing security limitations remain explicit. Startup timing changes are intentional: imports are inert and first explicit startup/legacy runtime-object access constructs dependencies.
