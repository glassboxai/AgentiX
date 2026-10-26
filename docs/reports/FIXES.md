# Verified defect correction report

Historical REF-002 verification snapshot. Implementation has subsequently moved into the package under REF-003 while retaining these regressions. Current architecture and test evidence are in `REFACTOR.md`; limitations/results below describe the time of the original correction.

Date: 2026-10-19. Scope: user-approved SEC-001, SEC-002, SEC-003, SEC-004 and UI-001 corrections. This supersedes the open-status statements in the historical `BASELINE.md` snapshot.

## Outcome and evidence

The full suite passes: **131 tests, zero failures, zero expected failures**. The original five reproducer tests are now ordinary regression tests. Before changing production, all five failed with expected-failure handling disabled (`fixes-before.txt`). Expanded targeted tests then produced 25 failures and 71 passes before implementation (`fixes-expanded-before.txt`). The final full-suite raw results are in `fixes-tests.xml`; current production hashes and metrics are in `fixes-evidence.json`.

An additional filename-alias validation edge case was reproduced separately (`alias-before.txt`) and fixed before the final run. It models resolver output using a temporary file, not an actual Windows link.

## Corrections

| Issue | Root cause | Implemented correction |
| --- | --- | --- |
| SEC-001 | Text prefixes do not establish tool-directory containment | Reject traversal/ambiguous components and require resolved artifact containment inside its tool |
| SEC-002 | A sibling root can share the same string prefix | Validate a single tool component, reject drive/root aliases and require resolved root containment |
| SEC-003 | Caller receives the mutable internal pending dictionary | Return a deep-copy snapshot while holding the coordinator lock |
| SEC-004 | Editor changes happen after initial compilation | Compile final approved Python before opening destination; include combined append text and requested/resolved suffixes; reject invalid edited tests before execution |
| UI-001 | A class-level list is shared between instances | Dataclass fields with an independent history default factory |

Changed production modules: `security_manager.py`, `custom_tools.py` and `app.py`. `config.py` and `main.py` remain unchanged relative to the historical baseline. New contracts, rationale comments and path/validation diagnostics are English. Routine validation logs omit artifact bodies.

## Compatibility and boundaries

Nested relative artifact paths remain supported. Windows device names, drive/UNC/rooted paths, alternate streams, parent traversal and trailing dot/space aliases are rejected. Existing filesystem links are resolved; tool-directory aliases and resolved escapes are rejected. The destination is revalidated after file approval. These rules intentionally tighten previously unsafe inputs.

Approved valid edits, empty content, Markdown persistence, write/append behavior and denial/timeout semantics retain their regression coverage. Invalid final Python preserves an existing file because compilation occurs before opening it for writing. No atomic-replacement guarantee is added for valid writes.

Each ExecutionState instance has independent data; the UI still owns a global instance. These fixes do not implement per-browser isolation, correlated concurrent approvals, OS sandboxing or protection against hostile filesystem races. Syntax validation does not establish execution safety. Existing execution/logging risks remain in `../KNOWN_ISSUES.md`.

The project's `generated_tools/` content was not inspected, tested, documented or modified. All service fixtures live in independent temporary directories. The running application was not restarted, so an already running process retains its loaded code until restarted. No live browser, real agent/LLM execution or installer validation was performed.

## Local report provenance

Local Ollama `qwen3:14b` drafts `ollama-fixes-draft.md` from `fixes-evidence.json`; the raw draft and model provenance are retained separately. Only prose is requested; no local model writes code or tests. This verified report is checked against raw red/green evidence and code, not accepted solely because a model produced it.

Review correction: the draft speculates that excluding generated artifacts could affect application functionality. No such effect was observed or established; this is an engineering-scope exclusion, not a runtime change. That unsupported inference is rejected. The draft's generic “unresolved defects” heading also includes deliberate scope boundaries, which are distinguished above from confirmed open issues.

## Reproduction

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = '1'
.\.autotool\Scripts\python.exe -m pytest --junitxml=docs/reports/fixes-tests.xml
```

The before-fix files are historical evidence; the current regression suite should pass without xfail markers. No unrelated production refactoring or installer implementation is included.
