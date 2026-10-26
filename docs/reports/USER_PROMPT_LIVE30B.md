# Domain-only request: supervised live review

Date: 2026-10-20. Requirement: USER-PROMPT-001. UI change: UI-VALIDATION-001.

The initial English request describes only household electricity consumption and
progressive prices. It supplies no tool name, function signature, programming
type or testing instructions. The exact request is retained in
`live-user-prompt-query.txt`. The independent arithmetic oracle is EUR 67.50:
100 × 0.12 + 100 × 0.18 + 150 × 0.25 = 12 + 18 + 37.50.

The separate loopback GUI at port 7870 uses `ollama/qwen3-coder:30b`, temporary
storage outside the excluded project directory, native Windows isolation and
manual approvals. The application selected `electricity_bill_calculator` and its
function contract itself. Technical events and agent verbosity remain enabled.
No original user application was restarted.

## Review incidents and regression evidence

- LIVE-USER-ERR-001: the generated specification's example said 67.0 while its
  written breakdown correctly implied 67.50. The reviewer corrected the example
  before approval. The normal-case unittest and full-result acceptance case
  retain the independently calculated 67.50 expectation.
- LIVE-USER-ERR-002: the candidate accepted booleans through `isinstance` and
  conditionally omitted unused tiers, contrary to the approved specification.
  The reviewer required exact numeric input types and all three tier entries,
  clamped unused quantities to zero and replaced misleading fractional range
  labels. The same corrected eleven-test suite reports nine assertion failures
  against the original candidate and zero against the reviewed candidate. These
  are isolated child test reports, not independent semantic proof.
- LIVE-USER-ERR-003: the generated unittest expected the infinity-specific error
  message for negative infinity. The implementation rejects it as negative with
  the required `ValueError`; message precedence was not specified. The reviewer
  initially missed this overconstraint. The GUI blocked progress and recorded
  the failure. The corrected test still requires `ValueError`, without inventing
  a message contract for overlapping invalid categories. Both infinities, NaN,
  negative values, booleans and nonnumeric inputs remain tested. The model's retry
  dropped checks and included incorrect explanatory comments; the reviewer
  replaced it with the corrected eleven-test suite, preserving coverage.
- LIVE-USER-ERR-004: the acceptance proposal was a bare array rather than a
  version-1 object, used unsupported exception fields and represented NaN as a
  string while expecting a numeric validation exception. The UI flagged the
  proposal as invalid and required correction. The reviewer retained the
  original, supplied sixteen schema-validated JSON cases with independently
  tabulated full results, and approved them manually. Nonfinite inputs remain
  Python unittest cases because strict JSON cannot represent them. Case-schema
  and invalid-input regressions already cover the maintained evaluator; this
  incident changes temporary review data, not production parsing rules.

Original, approved, retry and corrected versions are separate evidence files
with the prefix `live-user-prompt-resumed-`. The two counterexample JSON files
retain both the initially overconstrained run and the corrected regression run.
The GUI subsequently reported eleven provisional tests passing. All sixteen
human-approved cases passed host comparisons. The final manager then actually
called `calculate_electricity_bill` with `consumption_kwh=350`; the host-observed
result was `total_cost=67.5`, with usage 100/100/150 kWh, rates 0.12/0.18/0.25
and costs 12.0/18.0/37.5. The maintained final renderer returned this observation,
not unsupported model prose. The observed full result was checked against the
independent approved expectation. `live-user-prompt-resumed-result-dom.txt` and
`live-user-prompt-resumed-result.png` retain the GUI result; the traced server
log retains `final_execution_observed` and the internal contract digest.

The live summary contains sixteen PASS verdicts and no contract-digest line.
`user-prompt-evidence.json` records this operation and 75 current active source
hashes separately from historical baseline/fix hashes. This presentation change
does not modify the ledger, acceptance or sandbox behavior.

## Presentation verification

The validation summary no longer renders the approved-contract digest. Internal
digest state is retained and explicitly asserted by the renderer regression.
The pre-change failure is in `validation-summary-red.txt`. The final offline
run reports 307 passed and 17 deselected (`validation-summary-offline-final.txt`).
Ruff lint and format checks pass for the 75 active Python files. These checks
start no model or server and do not prove live execution or universal security.

## Operational limitations

The previous day's pending operation expired overnight and did not complete.
This run starts a new operation and empty temporary catalog. An initial new
server stalled during imports; after stopping only the matched disposable
process, a traced launch succeeded. Resource pressure was observed, but the
cause of the startup stall is not established. Failed browser navigation before
server readiness was abandoned; no browser security warning was bypassed.

This is supervised completion with reviewer corrections, not evidence that an
unreviewed model output was correct. Finite tests and acceptance examples do not
prove correctness for all inputs. Half-cent rounding policy is unspecified, so
independent acceptance deliberately avoids such ties.

The final answer currently exposes a raw execution record and dictionary rather
than a polished bill explanation. The numbers and breakdown are correct, but
this remains a user-experience limitation for a nontechnical audience. A future
presentation change should preserve the host evidence while rendering currency
and tier descriptions readably; no such additional production change was made
in this block.

## Report provenance

Local `qwen3:14b` was used only for report prose through the loopback Ollama
endpoint. The first restricted attempt failed with socket permission error
WinError 10013; the authorized local retry completed. Its draft was reviewed and
rejected: it substituted dollars for euros, speculated about unrelated uses and
asked what to do rather than producing the requested report. The draft and
review findings are retained in `user-prompt-ollama-draft.md` and its provenance
JSON. This final report was written and checked against raw evidence by the
engineering agent. No engineering code or tests were generated using Ollama.
