# LIVE-FIX-001: preserve requirements and gate creation stages

Status: approved corrections implemented and regression-verified; real 30B GUI validation paused by the user. See `../reports/APPROVED_CREATION_STAGES.md`.

The user approved corrections after LIVE-001 and requires `ollama/qwen3-coder:30b`
for the application. Alternate-model attempts are historical observations, not
validation of the required model or a reason to substitute another model.

Preserve the exact original user query alongside the manager summary. Run the
architect, coder and tester in separate sequential crews. Each later task receives
the original query and actual persisted approved artifacts, not completion prose.
Missing, empty, oversized, stale, unapproved or changed artifacts stop advancement
with an explicit stage failure. No automatic retries follow human denial.

Maintained storage records bounded in-memory receipts after approved writes of
specification/code/tests. Each receipt binds owner, operation, random write ID and
actual SHA-256; identical-byte reapproval still creates a new write identity.
Compare observed bytes with the approved content after platform newline handling,
so an intervening write cannot become this owner's approval. Receipts are bounded
to 64 entries, are invalid for closed/foreign operations and do not replace test
or acceptance evidence. Reads are confined and bounded to 1 MiB. Final creation
requires fresh saved tests, unchanged approved source/specification and current
human acceptance. Revoke acceptance if those postconditions fail.

The Gradio no-output approve/reject bindings discard internal boolean results,
preserving coordinator decisions and request ownership. Convert the two resolved
strict xfails to normal regressions only after their reproduced failures pass.

Repeat the progressive electricity-bill GUI problem with the required 30B model,
manual review, native execution and temporary storage. Do not inspect existing
project generated artifacts or restart the user's original live process. Review
real code, tests, acceptance cases and final tool output against the independent
4250-cent oracle; report manual interventions and any failure truthfully.
