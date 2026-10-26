# Readable activity, shared workflow policy and agent handoffs

Status: full block approved, implemented and verified on 2026-10-19. The final
English supervised qwen3-coder:30b operation completed with seven reviewed tests,
sixteen host-compared acceptance cases and an actual 250 -> 4250 call. Manual
artifact corrections were necessary. Evidence: `../reports/COMMUNICATION_LIVE30B.md`;
earlier verbosity-only evidence remains in `../reports/VERBOSE_ACTIVITY.md`.

The user paused the real 30B test because the activity panel exposed opaque
diagnostic identifiers instead of the original useful agent information. The
original reference uses verbose CrewAI agents/crews and captures their stdout.
The adapter had disabled verbosity while log_event wrote technical event names
to the UI capture. The user clarified that technical events may remain visible
but original verbose messages must also be preserved. Verbosity is now enabled
for all four agents and every application Crew, with owned stdout routing for
both the main server and supervised test launcher.

Approved and implemented changes:

1. Approved verbosity sub-block: restore original CrewAI verbose role/task/tool
   result/final-answer output alongside technical events in per-session activity.
   Preserve the expandable display and final activity history. Keep operation IDs
   and debugging events visible as requested. Do not introduce shared capture or
   leak another session's content. Reassemble Rich write fragments into bounded
   logical lines and retain Unicode in the GUI even when the host console cannot
   encode it. Keep actual review content available in its approval panel.
2. Put the workflow policy in maintained agent instructions, so a user describes
   the problem without asking for English specifications, code, tests, acceptance,
   actual execution and truthful results each time. Share core policy while
   assigning appropriate responsibilities and tools to each role. An empty catalog
   requires creation, rather than verification of a guessed nonexistent tool.
3. Verify handoffs with real consumer-boundary tests: manager to architect retains
   the original query; coder receives the persisted approved specification; tester
   receives the same requirement plus approved specification/code; final manager
   receives the accepted function/arguments and actual execution evidence. A role
   cannot advance on unsupported completion prose or unapproved artifacts.

Expected locations: `src/agentix/adapters/crewai.py`, maintained prompt definitions,
`src/agentix/diagnostics.py`, `src/agentix/ui/state.py`,
`src/agentix/ui/controller.py`, `src/agentix/orchestration.py`, associated tests and
English documentation. Inspect original reference files read-only. Keep the
required application model `ollama/qwen3-coder:30b`, storage exclusion, approval
boundaries and native isolation. After approval, test-first implementation precedes
a new supervised GUI run using a problem-only user query.

## Approved observable acceptance criteria

- LIVE-PROMPT-001: all four constructed agents receive shared English workflow
  instructions, with role-specific duties. Normal values, exact tier boundaries,
  invalid types, human review and real execution are application obligations.
  An empty catalog must not invite verification of an invented existing tool.
- LIVE-HANDOFF-001: original requirements and persisted reviewed specifications
  and code reach their consuming stages (existing receipt regressions retained).
  The final manager receives accepted public function signatures, human-reviewed
  declarative cases and their contract digest from the host acceptance ledger.
  No source is imported on the host to construct this context.
- LIVE-EXEC-001: creation cannot finish successfully on manager prose alone.
  The executor records only successful isolated calls bound to current owner,
  operation, code/tests, accepted contract, function and arguments. Failed calls,
  revoked acceptance, source edits and operation changes invalidate observations.
  Final tool answers use the host-observed call result rather than model claims.
  Reuse with acceptance or execution activity has the same final evidence gate.
  Plain conversational responses without tool activity remain model responses,
  not evidence of a tool execution.
- LIVE-REVIEW-002: after offline/framework/native/browser verification, run a new
  disposable GUI session using ollama/qwen3-coder:30b and an English problem-only query
  (the user subsequently clarified the query language).
  Review actual specifications/code/tests/cases, compare independent literal
  expectations and inspect the final observed call. Record manual edits and
  distinguish successful validation from incomplete or rejected runs.

Expected additional modules: verification.py, execution.py and acceptance.py.
No installer, Docker, live-server restart or project generated artifact inspection.

## Host handoff refinements observed during approved live validation

- Empty-catalog decisions use a separate manager instance without tools. CrewAI's
  empty task-tool list falls back to agent tools, so a task-only override cannot
  enforce this restriction. The regular manager retains verification/execution.
- Specification/code save tools and final execution return their service result
  directly to the host (`result_as_answer`). QA's acceptance tool also terminates
  its stage; the reuse manager has a separate nonterminal acceptance registration
  because it must still execute. Host receipt/acceptance/execution gates remain
  mandatory; terminal results do not turn model prose into evidence.
- Reviewer-authored acceptance data must pass `parse_contract` before submission.
  A live review with invalid hyphenated IDs was rejected without authorization.
  Preserve that failure rather than weakening validation or recording success.
- Bounded malformed model proposals may be manually corrected in the review panel.
  Human-approved JSON must still pass the unchanged strict schema before evaluation;
  oversized input never reaches review. Catalog context supplies canonical artifact
  filenames to avoid guessed package reads during reuse.
