# CLI-001 and E2E-001 verification report

Date: 2026-10-19. Status: implemented and verified for the boundaries described below.

The terminal now services owner-bound file and acceptance reviews while the shared workflow runs in a daemon worker. Users can approve, reject or edit multiline content before an explicit decision. Empty decisions reject. EOF/Ctrl+C closes permissions, including interruption during editing. Query exit aliases and legacy injected-workflow behavior remain supported. Independent host validation is printed after the model response. Review display escapes terminal control characters without modifying approved bytes. Logs record workflow/review events and identifiers without review bodies.

Reproducible browser tests run real Gradio in a separate temporary loopback server and installed headless Microsoft Edge through Playwright 1.56.0. They verify mandatory acceptance despite file auto-approval, edited expectations compared by maintained host code, visible verdicts, rejection, independent sessions, separate directory/file decisions and persisted file edits. Fresh profiles and temporary trusted fixtures keep these tests independent of the live application and production storage. No model is called by the test suite.

## Verification evidence

| Check | Result | Raw evidence |
| --- | --- | --- |
| Default offline suite | 263 passed | `cli-browser-offline.txt` |
| Real framework adapters | 3 passed | `cli-browser-frameworks.txt` |
| Native Windows isolation | 9 passed | `cli-browser-native.txt` |
| Playwright browser scenarios | 3 passed | `cli-browser-e2e.txt` |
| Ruff check and format verification | Passed; 65 Python files already formatted | `cli-browser-ruff.txt` |

These are 278 distinct passing cases across mutually exclusive test markers. The 12 new offline cases characterize terminal behavior and include a real acceptance-service lifecycle with trusted temporary fixtures. CLI feature failures were captured before implementation in `cli-review-red.txt` and `cli-verdict-red.txt`; the terminal-control regression failed in `cli-control-red.txt`. The first browser run passed two scenarios and failed because the file test omitted directory permission; the corrected harness passed all three scenarios. See `KNOWN_ISSUES.md` for causes, solutions and limits.

`cli-browser-evidence.json` preserves current application source hashes separately from historical evidence. `browser-acceptance.png` shows the disposable test interface after the human-edited expected value 3 matched the host-observed value 3. It is a fixture demonstration, not a live-model response. Temporary test servers were checked for cleanup; no matching server process remained. The live application was not restarted.

## Boundaries and remaining work

The browser workflow and OS boundary are trusted fixture doubles; browser success does not establish native isolation or model quality. The separately passing native tests cover their own independently authored fixtures. Finite approved cases do not prove universal correctness or requirement quality. The CLI cannot forcibly cancel model I/O, and an expired review may remain at an input prompt until the user responds; the coordinator denies late authorization. The simple multiline editor reserves `.end` as its terminator. Model memory admission, inference cancellation/deadlines, model-driven E2E and a clean runtime dependency lock remain open. The installer remains deferred; no Docker dependency was added. Existing project generated artifacts were not read or executed by engineering checks.

## Local report provenance and review

Local Ollama `qwen3:8b` drafted report prose only using the evidence JSON. This smaller resident model was selected because earlier larger-model runtime checks coincided with severe memory pressure. Neither code nor tests were requested from the model. The raw draft and provenance are retained as `cli-browser-ollama-draft.md` and `cli-browser-ollama-draft.provenance.json`.

The draft was reviewed and corrected in this authoritative report. Its “Unresolved Defects” heading incorrectly grouped the three fixed CLI incidents and corrected harness incident; all four are resolved in this block. Its statement that Ruff “formatted 65 files” conflated a read-only format check with formatting changes: final output says 65 files were already formatted. Its statement that tests “do not provide ... fixes” was too broad; the reproduced terminal defects do have passing regressions, while no universal correctness/security claim follows. The raw draft remains explicitly unverified and must not supersede this report.
