# ADR 0008: observed execution and role-ending handoffs

Status: accepted and implemented under user-approved specification 010.

## Context

Approved artifacts and acceptance did not prove the final manager actually invoked
the tool. Live model behavior also demonstrated guessed verification on an empty
catalog, repeated specification writes, invalid case JSON and guessed package reads.
Prompt instructions alone cannot enforce these boundaries.

## Decision

Keep four workflow roles, plus a separate tool-free manager instance for empty
catalog decisions. CrewAI falls back from empty task tools to agent tools; avoid
temporary mutation of the execution manager. All agents/crews remain verbose.
Supply shared English duties through agent system backstories, while assigning
implementation, QA and final execution to their respective roles.

Specification/code saves return directly to host receipt gates. QA uses a terminal
acceptance registration; the reuse manager uses a nonterminal variant to continue
to execution. Final execution is terminal. None of these tool results replace
artifact receipts, strict human acceptance or the native isolation boundary.

Publish defensive acceptance context from the trusted ledger: reviewed contract,
digest and accepted public AST signatures. Do not import generated modules on the
host. Supply the original query so final arguments are derived from the requested
problem rather than copied from an example case. Catalogs expose conventional
artifact filenames without claiming those files all exist.

Only the trusted executor publishes a successful isolated call observation bound
to current owner, operation, exact code/tests, accepted contract, function and JSON
arguments. Recheck after dispatch and before display. Clear previous observations
on new attempts and revoke on acceptance/artifact changes. Render the observed
arguments/result, not unsupported model completion prose. Missing observations
fail closed. Plain conversation remains model text without execution certification.

Bound malformed model case proposals before displaying them for manual correction.
Validate the approved edited JSON with the unchanged strict parser before any case
evaluation. Keep mandatory review, ownership, rejection and size limits intact.

## Consequences and verification

The UI preserves both verbose SDK output and technical events. A finite set of
host comparisons and a process observation cannot prove universal correctness or
malicious-child honesty. Human review is substantive: the real 30B run required
corrections to examples, type validation and a test expectation.

Offline regressions and real framework/native/browser checks are distinct from the
successful supervised model run. Source hashes and prior failures remain preserved
in `../reports/COMMUNICATION_LIVE30B.md` and its raw evidence. Installer, Docker,
crash-atomic storage and comprehensive third-party redaction remain out of scope.
