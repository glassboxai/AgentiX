# Native execution and pipeline verification

Historical EXEC-002/FLOW-002 snapshot. ACCEPT-001 subsequently made unittest outcomes provisional and added mandatory human-reviewed host acceptance. Current behavior/evidence is in `HUMAN_ACCEPTANCE.md`; the dated results below are retained for provenance.

Date: 2026-10-19. Implemented scope: EXEC-002 and the application-owned outcome gate for FLOW-002. Docker is excluded. The installer is deferred. No existing project generated artifact content was inspected, tested, modified or executed. No live application was restarted.

## Implemented behavior

Generated Python no longer runs inside the application process. Both unittest and function calls use a disposable Windows AppContainer with zero network capabilities, a unique profile, explicitly inherited output handles and a minimal environment. A freshly copied CPython standard-library runtime receives only the trusted worker and explicit artifact/request bytes. The child receives read/execute access to staging, not write permission. Site-packages and the project are not copied.

The child starts suspended. Its token must identify an AppContainer, and it must join a limited Job Object before resuming. Defaults are 512 MiB job memory, eight processes, 30 seconds wall-clock execution and 256 KiB combined output. The pipe is drained concurrently and excessive output terminates the job. Timeout, child errors, malformed reports, provisioning failures and cleanup failures cannot grant success. Surviving children are terminated and normal profile/staging cleanup is checked. Provisioning time is additional to execution time. There is no ordinary host fallback.

The manager cannot authorize final creation execution by saying tests passed. A per-runtime ledger requires an isolated successful process and a structured report with nonzero executed tests and no failures, errors, skips or expected failures. It independently compiles exact source/test bytes without executing them, and binds the observation to owner, operation and a length-framed SHA-256 digest. Publication checks current bytes and rejects an operation changed while testing. Execution checks the exact snapshot again before passing bytes to the child. Failed attempts revoke previous evidence.

Existing tools need fresh verification for the current query through the manager's new `Verify Existing Tool` action. Evidence is neither persisted nor carried across application restarts/queries. The initial runtime supports standard-library tools; third-party tool dependencies are unavailable. Approved storage/editing behavior remains, and unchanged legacy imports remain inert.

## Verification evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Pre-change offline characterization | 189 passed | `isolation-before.xml` |
| Final offline infrastructure suite | 212 passed, no failures/errors/skips | `isolation-tests.xml`, `isolation-tests.txt` |
| Real native Windows boundary | 8 passed, no failures/errors/skips | `isolation-native.xml`, `isolation-native.txt` |
| Real CrewAI/Gradio adapters | 2 passed, no failures/errors/skips | `isolation-frameworks.xml`, `isolation-frameworks.txt` |
| Native service recheck after final syntax gate | 1 repeat passed, already included among the eight distinct native cases | `isolation-service-final.txt` |
| Ruff check / formatting | Passed, 58 Python files formatted | `isolation-lint.txt`, `isolation-format.txt` |
| Source snapshot | 33 active application files hashed | `isolation-evidence.json` |

There are 222 distinct passing cases across the three suites. Default tests use an explicitly labelled OS-boundary double and independently authored trusted temporary fixtures; they do not establish real isolation. Native tests are opt-in and run outside the development sandbox to test Windows itself. They cover execution/unittest, private host read/write denial, a controlled live loopback listener with a parent connectivity control, read-only staging, omitted environment secrets, timeout, output/memory/process limits and normal cleanup. Real framework checks use in-memory callbacks, no model or HTTP server.

Failing-before evidence is retained in `isolation-contracts-red.txt`, `isolation-protocol-red.txt`, `isolation-edge-red.txt`, `isolation-run-race-red.txt` and `isolation-source-red.txt`. Initial native error-203 failures are in `isolation-native-first.txt` and `isolation-native-unrestricted.txt`; the subsequent same-fixture run passed. `isolation-wiring-first.txt` captures compatibility assertions requiring changes because host execution and unverified calls were deliberately removed. `isolation-network-diagnostic.txt` captures the strengthened network fixture's timeout observation. Incidents and solutions are detailed in `../KNOWN_ISSUES.md`.

Reproduction from the checkout:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = '1'
.\.autotool\Scripts\python.exe -m pytest
.\.autotool\Scripts\python.exe -m pytest -m windows_isolation
.\.autotool\Scripts\python.exe -m pytest -m frameworks
```

## Explicit remaining limits

Child unittest counts remain untrusted. Generated Python shares that interpreter and can manipulate unittest or forge the report. The host independently owns process status, limits, snapshots and publication/gating, but does not attest malicious-test honesty or semantic correctness. FLOW-002's agent-prose bypass is corrected; stronger independent acceptance/attestation remains open. Human-authored acceptance tests and protected observation infrastructure are needed for that stronger guarantee.

AppContainer shares the Windows kernel. OS resources already accessible to AppContainers remain governed by their existing permissions; the profile has writable private storage. There is no disk quota or exhaustive escape/security certification. The native cases demonstrate the tested restrictions on this machine, not safety against every attack. A host crash between suspended process creation and job assignment can leave a suspended process; generated instructions have not resumed, but this narrow resource-cleanup window is not eliminated. Lost browser unload events also do not immediately cancel an already running job; the finite backend limits still apply.

Persistent log rotation, full third-party log sanitization, crash-atomic writes, third-party sandbox dependencies and the installer remain outside this block. No live LLM pipeline quality, clean-install result, coverage percentage or static type-checker certification is claimed.

## Local report provenance

Local Ollama `qwen3:14b` drafted prose from reviewed evidence only; it wrote no code or tests. The unmodified draft and endpoint/model provenance are retained as `ollama-isolation-draft.md` and `ollama-isolation-draft.provenance.json`.

The draft incorrectly grouped resolved implementation incidents under “Unresolved Defects” and overstated source hashes as an integrity guarantee. Those claims were rejected. The incidents were corrected and tested; hashes identify a source snapshot and do not prove security. This reviewed report is grounded in raw evidence and separates the unresolved attestation limitation from fixed regressions.
