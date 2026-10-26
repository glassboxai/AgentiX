# Verified structural refactoring report

Historical REF-003 snapshot. SEC-005 subsequently changes session ownership, approval IDs, manager validation and diagnostics; current results are in `SESSION_SECURITY.md`.

Date: 2026-10-19. Scope: approved REF-003, behavior-preserving restructuring before further functional/security changes.

## Outcome

Implementation now lives in `src/agentix/`, with separate settings, contracts, path policy, approvals, storage, catalog, execution, test runner, artifact operations, CrewAI adapter, orchestrator, UI state/controller/view, bootstrap and CLI. Root `app.py`, `main.py`, `config.py`, `custom_tools.py` and `security_manager.py` remain compatibility entrypoints. `_agentix_path.py` locates src when running a checkout; no installer or installed-package workflow is introduced.

Service dependencies are passed explicitly. Importing root/package modules does not create storage/models/agents/widgets, change environment/stdout, patch Rich or load CrewAI/Gradio. The checkout import-path adjustment is intentional. Explicit startup applies the prior process policy and constructs the runtime. Stdout is restored on launch failure or return.

Prompts, role/tool assignments, manager parsing/fallback, pipeline task/context ordering, textual results, approval/edit/timeout behavior, independent state histories, corrected path/content checks, CLI exit/recovery behavior and UI bindings/launch settings retain regression coverage. Logger names now identify package components and additional composition/catalog diagnostics are available. Initialization timing intentionally changes from import to explicit startup.

## Verification

| Check | Verified result | Evidence |
| --- | --- | --- |
| Before extraction | 131 passed | `refactor-before.xml` |
| New import contract before implementation | Failed because legacy import created storage | `refactor-imports-red.txt` |
| New composition contracts before implementation | Three failures because package/components did not exist | `refactor-composition-red.txt` |
| Current offline suite | 149 passed; the opt-in framework test is intentionally deselected | `refactor-tests.xml` |
| Real framework adapter suite | One passed; offline cases deselected | `refactor-frameworks.xml` |
| Ruff lint | All checks passed | `refactor-lint.txt` |
| Ruff format | 41 active Python files already formatted | `refactor-format.txt` |
| Source contract inventory | 26 active application files, 17 classes, 74 functions/methods; no missing module/class/function docstrings or checked annotations | `refactor-contract-inventory.json` |

Together, the two suites execute all **150 current tests**, with no failures or expected failures. The original 131-case behavior suite was adapted to constructor wiring rather than removed. Configuration defaults/overrides remain asserted; its former eager-import effects were deliberately replaced by STR-01 startup/import tests. Additional tests cover CLI, lazy compatibility exports, explicit composition, real schema/widget registration and stdout restoration.

The contract inventory is a structural check, not proof that every explanation is semantically complete or that static typing is sound. Ruff checks formatting, imports and selected Python rules; no general static type checker, mutation testing or coverage percentage was run.

## Defect encountered during refactoring

REF-ERR-001: unused-import cleanup removed the intended SecurityViolationError re-export from `agentix.security`, causing compatibility import failures. Declaring the explicit public API via `__all__` preserves the export. A dedicated exception-identity regression failed before correction (`refactor-export-red.txt`) and now passes. Existing path-security regressions also passed after the correction. See the incident register for cause/solution details.

The real-framework check timed out in the restricted environment, then passed outside it in about seven seconds using the same code. It starts no model/server and reads no project artifact content. It remains opt-in so the offline suite does not require runtime dependencies or unrestricted framework initialization.

## Documentation and provenance

Updated architecture, REF-003, ADR-0002, engineering rules, local SDD authorization scope, test plan, installation status, change log and incident locations. Historical baseline/fix evidence remains preserved and labeled as snapshots. Current source hashes include all 26 active application files in `refactor-evidence.json`; skill hashes are updated in `SKILLS/provenance.json`.

Ollama `qwen3:14b` drafted `ollama-refactor-draft.md` from the reviewed evidence JSON using the loopback-only report helper. Raw draft/provenance are retained. The local model generated no code or tests.

Review corrections: the draft's statement that the project does not include generated content is rejected; that directory is excluded from engineering work, not absent. Its suggestion that no unresolved defects are mentioned is not an application assessment: the existing execution, authorization and logging concerns remain in the issue register. General adjectives about comprehensiveness are not used as verification claims in this report.

## Limits and next work

The project's `generated_tools/` content was not inspected, modified, tested or documented in this phase. Artifact fixtures are independently authored in temporary storage. No live model answer, browser interaction, server launch, installed-package installation or OS isolation was verified.

Session isolation, correlated approvals, manager schema/fallback changes, OS-enforced execution isolation, atomic valid writes, log redaction/retention and the Windows installer remain deferred. Structural refactoring does not resolve them implicitly. The running application was not restarted; an existing process continues using its previously loaded implementation until restarted.

## Reproduction

From the checkout root, with the existing development environment:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = '1'
.\.autotool\Scripts\python.exe -m pytest
.\.autotool\Scripts\python.exe -m pytest -m frameworks
.\.autotool\Scripts\python.exe -m ruff check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
.\.autotool\Scripts\python.exe -m ruff format --check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
```

The framework command requires installed compatible CrewAI/Gradio dependencies and may need execution outside a restrictive sandbox. Other commands do not require a running Ollama service or browser. Package installation and installer acceptance are separate future deliverables.
