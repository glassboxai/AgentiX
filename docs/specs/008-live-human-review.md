# LIVE-001: supervised real-model tool creation through the GUI

Status: supervised validation concluded, NOT PASSED. Three real-model attempts
were reviewed; none produced an executed tool result. See `../reports/LIVE_HITL.md`.

Use a separate loopback GUI with the real application composition, CrewAI agents,
local Ollama and native Windows isolation. No fake workflows or execution doubles.
Use temporary artifact storage outside the excluded project generated directory.
The reviewer must inspect proposed specifications, implementation, unittest source,
provisional test evidence, acceptance cases and final result through the actual
review workflow. No automatic file or acceptance approval is permitted.

The problem is progressive electricity pricing in integer cents: first 100 integer
kWh cost 12 cents each, next 100 cost 18, remaining units cost 25. Inputs must be
nonnegative integers excluding booleans; invalid inputs raise ValueError. Expected
values independently calculated before model generation: 0 -> 0, 1 -> 12,
99 -> 1188, 100 -> 1200, 101 -> 1218, 199 -> 2982, 200 -> 3000,
201 -> 3025, 250 -> 4250, 1000 -> 23000. Include negative, float, boolean,
string and null input checks. The final user problem is the bill for 250 kWh.

Require actual creation, meaningful non-tautological tests, isolated execution,
human-reviewed host comparisons and a final tool invocation returning 4250 cents.
Record every deviation or failure; do not silently repair production code or
claim success from a model's assertion. Reviewer edits must be distinguished from
model-authored output. This is one sampled supervised run, not a reproducible
guarantee of model quality or universal correctness. Preserve English evidence,
review notes, screenshots and source hashes. The existing live app is untouched.
