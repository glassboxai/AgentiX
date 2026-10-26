# User-facing validation status

Status: requested by the user on 2026-10-19; summary change implemented and
verified by the offline suite (307 passed) and Ruff. The 2026-10-20 supervised
domain-only GUI run passed eleven reviewed provisional tests and sixteen
host-compared acceptance cases, followed by an actual host-observed execution
returning EUR 67.50 and the complete correct breakdown. See
`../reports/USER_PROMPT_LIVE30B.md` for manual corrections and remaining limits.

UI-VALIDATION-001: remove the approved-contract SHA-256 line from the GUI validation
summary. Keep verification state, case outcomes and expected/observed results.
Retain the digest in evaluator/ledger state and technical evidence; no approval,
comparison, signature, verbose logging or execution behavior changes.

Affected presentation: `src/agentix/ui/controller.py`, with a regression in
`tests/unit/test_acceptance_ui.py`. No live application restart is required for
automated tests. A running process retains its loaded source until relaunched.

USER-PROMPT-001: run a different English domain-only request without tool names,
function signatures or programming types. The application must choose its own
implementation contract and apply the existing creation/review/execution workflow.
Use a fresh disposable loopback instance with qwen3-coder:30b and manual review.
The 350 kWh example has an independent expected total of EUR 67.50: EUR 12.00,
18.00 and 37.50 for the three progressive tiers. Require the requested breakdown
as well as the total; do not count an unsupported model answer as execution proof.
