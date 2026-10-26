# Human-reviewed acceptance and host evaluation

Date: 2026-10-19. Scope: ACCEPT-001. The application generates and initially checks Python tests, then requires explicit human review of declarative acceptance cases before host-evaluated authorization. Installer deferred; Docker excluded. No existing project generated artifact content was inspected, modified, tested or executed, and no live application was restarted.

## Implemented result

Generated unittest success is now `TESTS_PROVISIONAL_PASSED`, never final permission. The new `Submit Acceptance Cases for Human Review` tool accepts bounded version-1 JSON cases. The Gradio review panel displays the Python tests read-only, the provisional result and editable cases. The user reviews each purpose, function, input and expected result, then approves or rejects. Request/owner IDs, expiration, cancellation and stale-click protection apply. The file auto-approval checkbox cannot approve acceptance. Rejection/expiry prevents further automatic review prompts in that operation; a new user query is required.

After approval, AcceptanceEvaluator keeps the expected values outside the child. Each case executes in a fresh AppContainer receiving only implementation bytes, function name and keyword inputs. Typed JSON returns or exception-type observations come back as untrusted data. Maintained host code compares them using exact recursive type-aware comparison, explicit numeric tolerances or an expected exception type. Process, transport and serialization failures cannot satisfy expected function exceptions. There is no host eval, pickle, generated assertion or model-based final verdict.

Only every-case success publishes final authorization. It binds the current owner/operation/source/test bytes, edited canonical contract SHA-256, evaluator version and covered function names. An untested function remains unavailable. Rechecks revoke acceptance; current checks reject changes during review/evaluation and immediately before dispatch. An observed change cannot resurrect old approval after restoration. Contracts and receipts remain runtime memory only, requiring review again for a new query/restart.

The separate session-owned validation panel shows provisional/pending/evaluating/rejected/failed/verified/invalidated status, approved contract digest, per-case verdict and escaped expected/observed data. It does not depend on an agent's conversational claims. User instructions are in `../ACCEPTANCE_REVIEW.md`; design and acceptance criteria are in `../specs/006-human-acceptance.md` and ADR-0005.

## Verification

| Suite/check | Result | Raw evidence |
| --- | --- | --- |
| Offline infrastructure tests | 251 passed, no failures/errors/skips | `acceptance-tests.xml`, `acceptance-tests.txt` |
| Real Windows isolation | 9 passed, no failures/errors/skips | `acceptance-native.xml`, `acceptance-native.txt` |
| Real CrewAI/Gradio adapters | 3 passed, no failures/errors/skips | `acceptance-frameworks.xml`, `acceptance-frameworks.txt` |
| Ruff checks and formatting | Passed; 62 Python files formatted | `acceptance-lint.txt`, `acceptance-format.txt` |
| Application source snapshot | 34 active application files hashed | `acceptance-evidence.json` |

Total: **263 distinct passing cases**. Default tests double the native OS observation and use independently authored temporary fixtures. The real native tests retain host file/network/resource/cleanup checks and additionally exercise mandatory human acceptance plus typed return/exception observations. The real Gradio test uses `process_api` in memory: it displays review context, rejects stale IDs, applies the human-edited expected value, displays final status, isolates another browser and revokes acceptance on unload. It starts no HTTP server, browser or model. No live-agent quality or clean-install verification is claimed.

Security regressions include forged unittest success followed by a wrong acceptance result, auto-approval bypass prevention, human edits/rejection/expiry, cancellation, changed owner/run/source/tests, covered functions, invalid/duplicate/oversized/nonfinite/executable case data, expected-value omission from child inputs, payload-free logs and escaped UI output. Legacy tests use explicit simulated trusted acceptance only when testing call/routing behavior; their old assumptions were not retained as final authorization.

TDD evidence:

- `acceptance-contracts-red.txt`: initial twenty feature failures.
- `acceptance-ui-red.txt`: missing review context/status behavior.
- `acceptance-serialization-red.txt`: serialization error misclassified as expected exception.
- `acceptance-edge-red.txt`: revoked approval dispatch and duplicate observation key regressions.
- `acceptance-rejection-red.txt`: automatic reprompt after rejection.
- `acceptance-restore-red.txt`: old approval revived after source restoration.
- `acceptance-results-ui-red.txt`: missing expected/observed display.
- `acceptance-wiring-first.txt`: intentional compatibility changes from final unittest trust to provisional-only results, plus an incomplete test runtime double corrected to include its real operations dependency.

Causes, fixes and named regressions are recorded in `../KNOWN_ISSUES.md`. One test-source patch briefly placed restoration assertions in a following test and was corrected before running final verification. Ruff's one-line-conditional findings were formatted and final checks passed. These test/tooling corrections introduced no production behavior defect.

## Limits and operational impact

Finite human-approved cases establish agreement for the observed inputs, not correctness for all possible inputs, correct requirements, internal execution provenance or comprehensive security certification. A malicious implementation can fabricate output data, but cannot make a host verdict pass without matching the expectation held outside its acceptance child for that input. Humans must validate test relevance and numeric tolerances. Generated unittest reports remain forgeable but have no final authorizing role.

One to sixteen cases and 64 KiB contracts are supported; values are bounded finite JSON. Custom Python objects and third-party tool packages are not supported by the initial native runtime. A fresh copied runtime for each case adds latency; the 30-second child deadline applies per case, with provisioning time additional. Existing AppContainer shared-kernel, writable private profile, no disk-quota and narrow suspended-process cleanup-window limits remain as documented in the execution-isolation snapshot.

Interactive acceptance is implemented in Gradio. The legacy synchronous CLI has no dedicated review client, so it cannot complete acceptance without an external review callback and does not bypass it. Runtime-only contracts/receipts are not a durable audit database. Persistent log rotation, crash-atomic writes and the installer remain outside this block. Restart an existing application process to load the changed code; automated checks did not restart it.

## Local-model report provenance

Local Ollama `qwen3:14b` generated a prose-only draft from `acceptance-evidence.json`. No code or tests were requested from the local model. The original draft and provenance are retained in `ollama-acceptance-draft.md` and `ollama-acceptance-draft.provenance.json`.

The draft's factual counts, resolved incidents and limitations were checked against raw evidence. Its generic description as a “baseline” was corrected here: this is the implemented ACCEPT-001 change, not a new project baseline. The reviewed report distinguishes infrastructure verification from live LLM behavior and finite-case acceptance from universal correctness.
