# AgentiX v3 supervised real GUI validation

Date: 2026-10-23. Outcome: **PASSED with human corrections**, not autonomous first-pass success.

## Environment and method

The application used real CrewAI agents and local `ollama/qwen3-coder:30b` through
the actual Gradio GUI at http://127.0.0.1:7872/. The existing 7860 instance was not
restarted. The operational harness composed real services and native Windows isolation,
with fresh temporary storage named in v3-live-manifest.json. No model, workflow or OS
boundary was replaced by a fixture. Existing project generated_tools content was not
read, changed or executed. File auto-approval remained unchecked throughout.

The reviewer entered an English problem-only query, inspected every proposed file in
the GUI, edited the specification/tests/acceptance where necessary, and clicked each
approval manually. No hidden API calls supplied approvals or execution results. Evidence
snapshots, original/reviewed artifacts, fingerprints and screenshots are under
[v3-live-evidence](v3-live-evidence/). The raw server log is v3-live-server.txt.

## Business problem and independent oracle

A warehouse prepares the first 10 boxes at EUR 2 each, the next 10 at EUR 1.50 each,
and remaining boxes at EUR 1 each. Rates apply progressively to their portions.
Add EUR 5 shipping once for positive quantities; zero boxes cost zero. Reject negative,
fractional and non-quantity inputs. The requested order contains 27 boxes.

Before submission, v3-live-oracle.json recorded the independent expected result:
10 * 2 + 10 * 1.50 + 7 * 1 + 5 = **EUR 47.00**. Expected values were not inferred
from the generated function. No programming identifier, Python type or tool name was
specified in the user's query. Technical contracts were reviewed at subsequent stages.

## Reviewed pipeline and interventions

| Stage | Observation and reviewer action |
| --- | --- |
| Manager to architect | The complete original requirement and additional manager purpose were visible. The tool name was selected by the application. |
| Specification | The original proposal contradicted its own arithmetic: 20 boxes were labelled 35 instead of 40; 27 were labelled 42 instead of 47; an example comment also said 39.5. None exception behavior conflicted, and boolean rejection was implicit. The reviewer corrected these through the GUI before approval. Original and reviewed snapshots are retained. |
| Architect to programmer | The programmer received the approved, edited specification, including corrected amounts and validation rules. |
| Implementation | The generated function validated integer/non-boolean inputs, rejected negatives, implemented zero/no-shipping and all progressive tiers. It contained no imports, filesystem/network effects or unittest/report manipulation. It was approved **without editing**. |
| Programmer to tester | Approved source and the reviewed specification were handed to the tester. |
| Unit tests | Eight test methods imported and called the generated function using fixed expected values and assertRaises. The reviewer added 9/19 boundaries, a fractional value and exact float checks for zero/27. Eight revised methods passed in native isolation. This result remained provisional. |
| Acceptance proposal | The generated document included Python True, invalid in JSON. The application visibly flagged the proposal and required correction. The reviewer supplied valid JSON and expanded it to 16 cases using the independent oracle. |
| Host acceptance | Nine valid quantities and seven invalid inputs all matched approved expectations. Expected values remained with the host, and each observed case used native isolation. The panel showed 16 passed, zero failed. |
| Tester to manager | Approved function/context, the accepted contract and original query were supplied for final execution. |
| Final answer | The host observed warehouse_box_shipping_calculator.calculate_total_cost with number_of_boxes=27 returning 47.0. The GUI displayed Result 47.0 with optional execution details. It did not merely repeat a model assertion. |

The approved positive quantities were 0, 1, 9, 10, 11, 19, 20, 21 and 27. Invalid cases
were -1, 1.5, 1.0, true, false, text "27" and null. Exact expectations preserved float
outputs in JSON. A separate unit assertion also checked 50 boxes -> 70.0.

## Test sensitivity checks

After the GUI acceptance completed, three independent mutation probes changed copies
of the reviewed source in memory and ran the reviewed tests through WindowsSandbox.
They were supplemental checks outside the GUI, not extra claims about the GUI itself.
The approved tool and its files were not modified.

| Deliberate defect in temporary copy | Observed outcome |
| --- | --- |
| Remove EUR 5 shipping | Native isolated process exited 1; four unittest methods failed. |
| Change the second-tier rate from 1.50 to 1.00 | Native isolated process exited 1; three unittest methods failed. |
| Remove explicit boolean rejection | Native isolated process exited 1; the invalid-types method failed. |

mutation-results.json preserves process exits, isolation flags, full assertion failures
and child reports. These sampled mutations show sensitivity to those specific defects;
they are not a complete mutation score or proof that all possible defects are detected.

## Incidents and outstanding observations

- V3-LIVE-001: incorrect/contradictory specification arithmetic and input contract.
  Corrected in the human-reviewed specification. The revised unittest expectations and
  host cases for 20/27, None and booleans provide the corresponding sampled regressions.
- V3-LIVE-002: invalid JSON boolean in generated acceptance. The existing schema gate
  detected it. Corrected in the GUI; the valid true/false cases subsequently passed.
  No production parser change or new production regression was required.
- V3-LIVE-003: proposed tests omitted the lower neighbours 9/19 and a genuinely
  fractional input. Reviewer additions passed; original and reviewed tests are retained.
- V3-LIVE-004 (open, source-contract observation): ExecutionBackend declares execute
  but omits evaluate, although acceptance calls evaluate and WindowsSandbox implements
  it. The current concrete runtime succeeded. A future injected provider could satisfy
  the incomplete declared protocol yet fail acceptance. A separate approved TDD change
  should add the missing contract and a provider-contract regression. No fix is claimed.
- Presentation observation: the final card says 47.0 without a currency label or a
  business-language explanation. The value is correct; showing EUR 47.00 and a short
  breakdown would improve clarity. No UI change was made in this test block.

A reporting-only evidence script initially used a nonexistent class import; it failed
before report synthesis and was corrected to inspect the source contract. It did not
change or restart the application. Runtime and reviewer errors are kept distinct.

## Evidence limits and provenance

This is one supervised real-model run with necessary reviewer corrections. It does not
establish autonomous correctness, every-input semantics, malicious-child honesty or
production readiness for arbitrary generated tools. Very large quantities and other
business scenarios were not tested. Human review remains material to the successful run.
No financial transaction or real customer information was involved.

All 81 maintained Python file fingerprints still match the v3 release manifest:
source-preservation-check.json. No production code was fixed during validation.
The existing release offline/integration results remain separate historical evidence;
they were not rerun merely to document this operational test.

Local Ollama qwen3:14b was used only to draft report prose from
v3-live-report-input.json. The raw draft and provenance are retained separately and
must not be treated as evidence. This report is engineering-reviewed against the GUI
snapshots, server log, independent oracle and native mutation observations. Engineering
scripts, reviewer test edits and code were not authored by that reporting model.

Report-draft review note: the raw model draft says "No code was edited". This is only true of the generated implementation and maintained production source; reviewer-authored test edits and in-memory mutation copies did occur, as recorded above. The reviewed report takes precedence over that ambiguous draft wording.
