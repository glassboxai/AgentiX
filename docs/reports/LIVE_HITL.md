# LIVE-001 supervised real-model GUI validation

Status: supervised validation concluded — NOT PASSED. Date: 2026-10-19.

The test uses a separate real Gradio GUI at loopback port 7861, real CrewAI agents,
local `ollama/qwen3:8b`, native AppContainer execution and a new temporary artifact
directory. No workflow, model or execution fixture is injected. File auto-approval
is disabled. The existing application and its generated artifact directory are
outside this test. The launch manifest and exact query are retained separately.

## Independent oracle established before generation

For progressive bands of 100 units at 12 cents, 100 more at 18 cents and remaining
units at 25 cents, the independent expected totals are:

| kWh | Cents |
| --- | --- |
| 0 | 0 |
| 1 | 12 |
| 99 | 1188 |
| 100 | 1200 |
| 101 | 1218 |
| 199 | 2982 |
| 200 | 3000 |
| 201 | 3025 |
| 250 | 4250 |
| 1000 | 23000 |

Negative integers, floats, boolean values, strings and null must raise ValueError.
The final business result for 250 kWh is 4250 cents, or EUR 42.50. These expectations
are reviewer-authored from the requirement, not taken from generated tests.

## Review observations

1. The manager requested actual creation of `tiered_energy_bill` and started the
   Architect -> Coder -> Tester pipeline. The reviewer approved only the specific
   temporary tool directory.
2. LIVE-SPEC-001: the first architect specification incorrectly declared `kwh: float`
   and assumed nonnegative inputs without the required validation or boolean
   exclusion. The reviewer preserved `live-hitl-spec-original.md`, replaced it with
   the explicit integer/error contract in the GUI, then approved that edited
   specification. `live-hitl-spec-approved.md` and the review screenshot retain the
   intervention. This is a human correction, not autonomous model success.
3. LIVE-UI-001: Gradio logged that the approve callback returned a boolean while
   declaring zero output components. The decision was accepted; the extra value
   was ignored. This warning remains a production follow-up, not silently fixed.

## First two sampled outcomes

- qwen3:8b ran from 14:23:42 to 14:29:44 Europe/Berlin (362 seconds), saved only
  specifications and ended with `PIPELINE_NOT_VERIFIED`. No code, unittest file,
  provisional success, acceptance or final tool invocation was produced. The
  temporary file inventory confirms this. Code/test quality cannot be certified
  when those artifacts do not exist.
- qwen2.5:7b failed during the manager stage with `Invalid response from LLM call -
  None or empty.` No creation-stage review was reached. The exact integration
  root cause is not established by this single sample.

The completed test servers for these attempts were stopped by their recorded
manifest PIDs, after verifying their command lines referred to this launcher.
The original live application was not stopped or restarted.

## Third attempt: qwen3:14b

The model again requested real tool creation. Its architect specification changed
the argument to `kwh_usage` and used `isinstance(input, int)` without excluding
booleans. The reviewer preserved the original proposal and approved the corrected
`kwh`/ValueError contract in the GUI. This was another manual intervention.

The tester subsequently proposed a meaningful unittest class importing the actual
intended function, with correct arithmetic checks for 0, 1, 50, 99, 100, 101, 150,
199, 200, 201 and 250, plus string, fractional-float, null and negative checks.
Review found missing bool cases, integral float rejection and exact return-type
assertions. More fundamentally, no code-save approval had occurred. An inventory
of the temporary directory confirmed only the specification existed: the pipeline
advanced to the tester without a persisted/reviewed implementation.

The reviewer preserved the proposed tests as evidence and rejected their write
request through the GUI. The application then displayed `Automatic checks failed`
and did not grant acceptance. No generated Python was executed on the host. A
successful code review, unittest execution, independent acceptance verdict and
final 4250-cent tool result remain unachieved. The test is not passed.

After rejection, the tester attempted acceptance submission, which the host denied
with a ValueError and `Acceptance failed`. The reviewer captured that state and
stopped only this temporary server by its verified manifest PID while its worker
was still running. This third outcome is a terminated supervised review, not a
natural completed pipeline. No additional model or source workaround was used to
manufacture a passing result. All three temporary inventories contain only the
approved specification or no files; no implementation or tests were persisted.

## Deterministic findings and verification

`test_creation_pipeline_retains_original_user_contract` reproduces that only the
manager summary reaches creation, dropping the immutable original request.
`test_approval_callback_respects_real_gradio_output_contract` reproduces the
no-output callback returning False. Both failed with xfail disabled; raw red logs
are retained. Both remain strict xfails, not corrected production defects.

The existing regression `test_creation_claim_without_service_evidence_blocks_final_manager`
protects the observed fail-closed final boundary. Production source is unchanged.
Offline checks: 263 passed and one known xfail. Real framework checks: three passed
and one known xfail. Ruff check and format verification pass for 68 active Python
files. These counts are regression results, not successful live-model validation.

Proposed follow-up, requiring user validation: preserve the original query and
approved artifacts at creation-stage boundaries, verify real artifact existence
before advancing, improve stage-specific failure reporting, and discard internal
decision booleans in zero-output Gradio adapters. Model compatibility and bounded
inference also need investigation; simply selecting a larger model is not a fix.

The machine-readable outcomes and unchanged application hashes are in
`live-hitl-evidence.json`. The native boundary was configured but not reached by
these live attempts; native-isolation correctness is not established by them.
The original application's generated content was never inspected or executed.

## Local report provenance

Local `qwen3:8b` drafted prose from `live-hitl-evidence.json` only after the test
servers were stopped. No code or tests were requested from Ollama by engineering;
tool generation above was performed by Agentix itself, as requested by the user.
The draft and provider provenance are retained as `live-hitl-ollama-draft.md` and
`live-hitl-ollama-draft.provenance.json`. This reviewed report is authoritative.
The draft's wording about the third worker continuing after shutdown is imprecise:
the worker was active when the process was stopped, not a surviving background
worker. Its broad wording about regressions should be read as the stated passing
checks and two deliberately unresolved strict xfails, not newly fixed defects.
