# V5-042: simplify application coordination with CrewAI

Status: user-approved on 30 October 2026. Implementation in progress.

COORD-01: use CrewAI Process.sequential, explicit Task context and structured
Pydantic outputs for application planning/connection and pending widget generation.
Creation phases may be separate crews because selected tools become known after
planning. Preserve verbose=True on every agent and crew, alongside scoped events.
COORD-02: retire direct Ollama HTTP and catalog-prefix schema synthesis from the
production application route. Keep one ordinary validated plan and existing
persisted bindings/manifest compatibility. No tool-name exceptions or new scheduler.
COORD-03: generate only missing widgets and reuse exact currently approved widget
bytes. Model output never grants approval or runs generated code on the host.
COORD-04: keep host validation, exact-byte human review, independent acceptance,
AppContainer and job controls. Develop with injected model/OS boundaries; reserve
real native checks for block closure and actual generated-code execution. Never
introduce a host-execution fallback or restart the user-owned 7880 GUI.
COORD-05: characterize existing behavior, capture failing coordination regressions,
verify offline then real framework adapters, and finish supervised qwen3-coder:30b
acceptance of A complex task on the separately owned validation instance. Finite
fixtures do not establish arbitrary model correctness. No paid/remote inference.

Affected boundaries: agents/catalog request builders, a CrewAI coordination adapter,
application pipeline/composition and scoped GUI activity. Legacy test-injected
callable clients remain an explicit compatibility adapter, not a production fallback.


COORD-06 / V5-ERR-042-02: the model-facing plan is an ordered list of calls with
arguments sourced explicitly from a named user input, fixed JSON value or prior
result. Convert once to the compatible persisted manifest; no new executor or
provider-prefix schema. Invalid type connections produce a maintained diagnostic
identifying only validated step/parameter names and expected/actual types. Never
expose arbitrary model/parser exception bodies.
