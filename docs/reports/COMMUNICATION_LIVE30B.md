# Agent communication and supervised qwen3-coder:30b validation

Date: 2026-10-19. Scope: approved specification 010 and supervised LIVE-001.

## Outcome

The final English problem-only query completed the real creation pipeline with
manual review, local **ollama/qwen3-coder:30b** and native Windows isolation.
The host displayed the actual call to `tiered_energy_bill(kwh=250)` and result
**4250 cents**. Seven reviewed unittest methods passed provisionally; all sixteen
human-approved declarative cases passed independent host comparison. This is a
supervised success, not autonomous model correctness or an all-input guarantee.

The test-owned GUI remains open at `http://127.0.0.1:7868/`, PID 19380, external
temporary storage recorded in `live-workflow30b-reviewed-manifest.json`. No existing
user server was restarted. No project generated artifact content was inspected.

## Implemented communication contract

- Shared English system duties reach each role through CrewAI backstories; real
  framework tests verify the constructed system prompts. Users need describe only
  the domain problem. All agents and crews remain verbose with technical events.
- Empty-catalog decisions use a manager instance with no tools. The execution
  manager retains verification, review, artifact reading and execution tools.
- Original requirements reach the architect; fresh approved persisted specification
  reaches the coder; that specification and exact approved code reach QA. Receipt
  gates and final source checks prevent unsupported claims from advancing stages.
- Single-artifact stage saves and final execution return directly to host gates.
  QA acceptance ends QA; reuse-manager acceptance remains nonterminal.
- Final manager context includes host-reviewed cases, digest and authorized AST
  function signatures. Only an actual current successful isolated call supplies the
  final tool response. An invented or missing result returns EXECUTION_NOT_VERIFIED.
- Conventional artifact filenames reach the manager through its catalog. Bounded
  malformed case proposals can be corrected manually, but approved edited JSON
  must pass the unchanged strict parser before any host evaluation.

## Human review in the successful operation

Operation: `d9cad6c5ec9e43b88c27839f75b72eda`. English query:
`live-workflow30b-english-query.txt`. It contains business rules and the requested
250 kWh calculation, without engineering workflow instructions.

| Artifact | Reviewer action |
| --- | --- |
| Specification | Corrected example 150 kWh from 1950 to 2100 and 250 from 3750 to 4250; tariff/type requirements already correct |
| Implementation | Replaced isinstance input check with exact int validation to reject bool; removed optional demonstration main block |
| Unittest suite | Corrected 101 kWh expectation from 1212 to 1218; required exact return type; added independent literal cases including 150/250/300 and larger consumption |
| Acceptance | Expanded seven valid generated cases to sixteen independently checked normal/boundary/invalid cases, including both booleans and None |
| Final call | Verified function, kwargs `{"kwh":250}` and host-observed result `4250` |

Original and approved artifacts are preserved as `live-workflow30b-reviewed-*`.
The three actual persisted temporary artifacts match their approved review text;
exact persisted byte hashes are in `communication-evidence.json`. Contract SHA-256:
`2d23e91c702108e4a09574eb08eb9fdc65702729f9369adceae1143530ed976a`.

`live-workflow30b-reviewed-final-dom.txt` records all sixteen PASS verdicts and the
final observed call. `live-workflow30b-reviewed-result.png` shows the result in the
GUI; the full-page capture retains case details. The server log records real
provisioning, acceptance, final function execution and completion.

## Negative evidence and earlier attempts

Maintained-code regressions failed before implementation in `handoff-red.txt`,
`workflow-policy-red.txt`, `empty-catalog-red.txt`, `stage-completion-red.txt`,
`stage-handoff-red.txt`, `malformed-proposal-red.txt` and `catalog-artifacts-red.txt`.
The initial handoff red run reproduces fabricated prose replacing an actual result.

Additional explicit native counterexamples in `live-workflow30b-counterexamples.json`
use the preserved temporary reviewed proposals, never host imports: the original
implementation fails both reviewer-authored bool tests; the corrected version
passes both. Original generated tests fail once against the correct implementation
(wrong 101 kWh expectation); all seven approved tests pass. These live artifact
corrections were found by review, not falsely described as test-first generation.

Earlier attempts were not successful: empty-catalog guessed verification was
rejected; a repeated erroneous specification overwrite was rejected; reviewer
hyphenated case IDs were rejected by the strict parser; a Spanish pending operation
ended without approved specification before the user requested English; a later
English QA run sent malformed JSON and stopped; a reuse attempt guessed package
files and tried unapproved execution, which the host blocked. Their manifests,
logs, originals, DOM snapshots and screenshots remain in the report directory.
Do not merge these attempts into an uninterrupted successful run.

## Fresh engineering verification

| Check | Outcome | Evidence |
| --- | --- | --- |
| Offline pytest | 307 passed; 17 opt-in cases deselected | handoff-offline.txt |
| Real CrewAI/Gradio adapters, no models/server | 5 passed | handoff-frameworks.txt |
| Native AppContainer, independently authored temporary fixtures | 9 passed | handoff-native.txt |
| Disposable deterministic Playwright browser tests | 3 passed | handoff-browser.txt |
| Ruff lint/format, explicit active targets | Passed, 75 Python files | handoff-ruff.txt |

Thirty-five application/root-entrypoint hashes are recorded separately from older
baseline/fix snapshots. No coverage percentage, clean installation or universal
security guarantee is inferred. Browser fixtures do not establish model quality;
the separate supervised run supplies the real-model evidence.

## Remaining limits and provenance

The successful live run covers creation and final execution. No successful post-fix
real-model reuse run is claimed. Malformed-proposal recovery is tested offline;
the successful final model proposal was valid JSON. Ollama metadata reports the
required coder model with context length 4096; no causal language/context comparison
is established. Generated unittest reports remain provisional and finite cases do
not prove semantic correctness for all inputs or honesty of malicious child code.

Local qwen3:14b produced the prose-only `communication-ollama-draft.md` from reviewed
evidence over loopback. Its observations/limitations were checked against raw
results. The draft incorrectly classified historical failures as unresolved
production defects, including unsupported language-specific defects; that inference
was rejected. Provenance records the review. This authoritative report distinguishes
implemented fixes, model/reviewer mistakes, successful evidence and remaining limits.
The engineering workflow used Ollama for report prose only, never maintained
application code/tests. Agentix itself used qwen3-coder:30b to propose temporary
tool code/tests; human review and host comparisons made acceptance decisions.
