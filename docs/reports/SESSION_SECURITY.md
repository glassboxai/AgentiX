# Verified session and decision security report

Date: 2026-10-19. Scope: approved SEC-005. This is an implementation/test report, not a certification that arbitrary generated Python is safe.

## Delivered behavior

- The browser view resolves server-owned tokens against Gradio request owners. Each session owns its controller, history, activity, provider client, role objects and approval settings. Public diagnostic UUIDs differ from access tokens. Shared artifact storage/catalog is unchanged.
- Manual requests have unique IDs, owners and monotonic deadlines. Missing, foreign, expired, duplicate, previous or incorrectly typed decisions cannot authorize work. A live request cannot be overwritten. Valid edited text, including empty text, is preserved; final Python validation remains active.
- Approval clicks submit the ID associated with their editor snapshot. A hidden non-stateful textbox is intentional: mutable server-only State could relabel a stale queued click. Server ownership/ID/deadline checks remain mandatory.
- Manager creation requires complete raw/fenced JSON with exactly the supported action, canonical safe name and nonblank bounded purpose. Malformed/ambiguous/duplicate/extra fields and invalid types/names fail explicitly. The arbitrary fallback and silent name normalization are removed. Valid ordinary textual answers remain supported. There are no automatic retries.
- Application events contain fixed event names, public session/run/request IDs, error type and optional source line, not full query/source/model/exception bodies. Provider verbosity is disabled. Context-local stdout routing and bound tool wrappers preserve activity/diagnostic ownership across worker/provider threads. Activity retains at most 256 records of 4096 characters per session.
- Controller acceptance/snapshots are locked. Busy messages cannot redirect the active workflow's final answer. Editor content refreshes by request identity rather than filepath. Registry capacity is 128; inactive entries expire after 1800 seconds on registry activity. Delivered unload, State cleanup and expiry close the owner and deny unresolved/new requests.

## Evidence

| Check | Result | Raw evidence |
| --- | --- | --- |
| Before this block | 149 offline tests passed | `security-before.xml` |
| Initial new contracts, before implementation | 22 failures | `security-contracts-red.txt` |
| Additional type/buffer boundaries | Three targeted failures before fixes | `security-edge-red.txt` |
| Exception payload logging | Two failures before safe-event fixes | `security-log-red.txt` |
| Diagnostic-ID/degenerate-output/CLI boundaries | Four failures before fixes | `security-diagnostic-edge-red.txt` |
| Editor request transport with real Gradio | Failed with State-only transport, then corrected | `security-request-transport-red.txt` |
| Independent provider clients | Failed before removing shared legacy client | `security-runtime-client-red.txt` |
| Real Gradio unload | Failed before connecting unload | `security-unload-red.txt` |
| Provider-thread diagnostic ownership | Failed before adapter context restoration | `security-thread-context-red.txt` |
| Owner metadata inheritance | Failed before explicit factory resets | `security-owner-metadata-red.txt` |
| Final offline suite | **189 passed** | `security-tests.xml` |
| Final installed-framework suite | **Two passed** | `security-frameworks.xml` |
| Ruff lint and formatting | Pass; 50 active Python files formatted | `security-lint.txt`, `security-format.txt` |
| Structural documentation inventory | 29 application files, 24 classes, 107 functions/methods; no missing checked contracts | `security-contract-inventory.json` |

All **191 selected tests** pass across the two commands, with zero expected failures. The offline command deselects the two installed-framework tests; the framework command executes those two separately. Direct Gradio process_api tests run preprocessing, server State, typed Request injection, independent browser histories, old-ID rejection, foreign-token rejection and unload without launching an HTTP server or model. This is stronger than widget registration alone, but it is not a browser click/network test.

Approved behavior changes intentionally replace the prior malformed-decision fallback, name normalization/prose-wrapped creation acceptance and identity-free manual resolution assertions. Existing path, persistence, valid edit, rejection/timeout and functional service tests remain active. Further tests were added as edge cases were found during implementation; the report does not claim every assertion represents a separately observed chronological red phase.

## Compatibility and migration

Root launch entrypoints and lazy compatibility exports remain. Direct approval callers must pass the pending request_id and owner_id. A no-ID response now returns False. UI callbacks submit the displayed request ID; invalid manager decisions now raise DecisionValidationError rather than creating an unrelated tool. UI labels describe file approval, not a sandbox guarantee.

The default browser view owns sessions; legacy direct Python/CLI access retains its separate legacy facade. Sharing a facade manually between unrelated callers is not session isolation. Previously authorized/executing operations are not transactionally rolled back on close. Arbitrary executing Python is not forcibly stopped. Lost unload notifications require timeout/State/registry cleanup rather than guaranteed immediate cancellation.

## Remaining limitations

Gradio session hashes route workflows; they are not account authentication. Files/catalog remain shared. EXEC-001 remains open: generated code runs in-process and test subprocesses inherit host capabilities. Independent pipeline outcome checks (FLOW-002), OS-enforced execution isolation, crash-atomic valid writes, total process resource limits and installer implementation remain separate work.

Application event payloads and provider verbosity are controlled, but arbitrary tool stdout and all third-party logging are not comprehensively sanitized; persistent rotation is not implemented. Unscoped background output is not attributed to another session. No real model inference, live HTTP/browser test, installed-package verification, coverage percentage, general static type checker or hostile-OS isolation certification is claimed.

No project generated_tools content was inspected, documented, tested or changed. Service fixtures are independently authored temporary artifacts. The running application was not restarted and needs a restart to load this implementation.

## Documentation and report provenance

Architecture, SEC-005 specification, ADR-0003, engineering rules, local SDD routing, incident register, test plan, installation migration notes and change log are synchronized. Historical baseline/refactor/fix reports retain their original evidence. Current source hashes include all active application files in `security-evidence.json`; local skill hashes are updated separately.

Local Ollama qwen3:14b drafted `ollama-security-draft.md` from the evidence JSON; raw draft/provenance are retained. Only prose was requested, never code or tests. This final report is checked against source and raw verification, not accepted solely on model authority.

Review corrections: passing controlled tests does not establish general production stability; the draft's speculation about data loss/inconsistency from lost unload notifications is unsupported. Excluding generated artifacts from engineering work does not itself change application reliability. “No HTTP server/browser/model test” describes test scope, not the absence of those application capabilities. Account authentication, rollback and installer work are deliberate boundaries here, not newly reproduced failures. These unsupported/generalized draft statements are not adopted in this assessment.

## Reproduction

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = '1'
.\.autotool\Scripts\python.exe -m pytest
.\.autotool\Scripts\python.exe -m pytest -m frameworks
.\.autotool\Scripts\python.exe -m ruff check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
.\.autotool\Scripts\python.exe -m ruff format --check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
```

Framework tests require the installed runtime dependencies and may need execution outside a restricted environment. They do not require running Ollama or opening a server/browser.
