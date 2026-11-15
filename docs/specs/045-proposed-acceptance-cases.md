# V6-045: proposed independent acceptance cases

Status: implemented and verified with offline, real-framework and disposable-browser checks. User approved this block
on 2026-10-30. No live restart, inference or generated_tools inspection is included.

## Observable acceptance

- CASE-01: schema-3 creation proposes inputs/results from previously reviewed
  catalog value cases where direct connection references can be matched exactly.
- CASE-02: missing/incompatible cases and unsupported Python remain explicit
  pending fields; no generated source or tool is executed to predict expectations.
- CASE-03: the review opens with editable application_acceptance.json selected;
  an always-visible notice explains missing data and the save/review steps.
- CASE-04: invalid cases block before native/browser verification and give an
  actionable persistent status. Saving revokes approval and clears human review.
- CASE-05: exact-byte review, independent native comparison and schema-2 behavior
  remain in force. Structurally valid suggestions never constitute human approval.

## Design and boundaries

code_cases.propose_cases reads inert AST only during proposal creation. It matches
straight-line assignments and call(widget_id, **named_arguments) to reviewed kwargs;
only reviewed expected JSON values may flow to subsequent variable references.
Constants, payload keys and list indexing are supported; helpers, arithmetic,
branching, loops and other syntax are unresolved. This is a conservative proposal
matcher, not execution or a runtime graph interpreter. It never calls eval/exec,
imports generated source or invokes tools. The original Python runtime is unchanged.

Candidate input domains contain up to 32 type-valid reviewed argument values per
public input. At most 4096 payload candidates are visited; bounded or incomplete
search can leave a valid application needing manual cases. Best partial matches
are retained. This mechanism does not infer correctness from the original request:
humans must check that the suggestions test the requested behavior. Expectations
are never copied from child/model output. No LLM fallback is added.

Result fields: widgets maps widget identities to reviewed value cases; payload
contains candidate public inputs; expected maps matched widget IDs to reviewed
results; pending lists unresolved payload/expected paths; provenance identifies
reviewed catalog origins. Proposal pending/provenance metadata is historical;
current validity is always recomputed from saved cases and exact manifest types.
No case values are included in status/error text. Bounds/constants are per proposal.

The existing editor/save/ownership paths are reused. Saving invalid JSON or invalid
case types is rejected. Valid edits revoke identity/snapshot/approval. The checkbox
still gates the supervisor; backend prevalidation also protects direct callback use.
The Approve button may be clicked to explain invalid cases, but native/browser
verification cannot start until they are valid. The separate saved JSON display
is informational; the selected JSON source editor is interactive.

## Incident and evidence

Cause: schema-3 generation explicitly installed empty dictionaries instead of the
schema-2 reviewed-case selector. That selector requires graph bindings, so it
cannot be copied unchanged. The controller collapsed acceptance ValueError into
an unrelated stale-review message. The review initially selected app.py and kept
its JSON cases display read-only. V6-045 adds the bounded matcher, preselects the
virtual acceptance file, expands review and supplies persistent safe guidance.

Red evidence: three new proposer tests failed on missing code_cases; the controller
regression then reproduced the generic stale-review message (after correcting the
fixture to double the supervisor rather than pass an incomplete candidate).
Focused checks: 41 passed, 3 deselected. Real frameworks: 13 passed, 907 deselected;
no model/server was started by that check. Browser/offline closure follows below.
This record is manually authored and checked against raw tool output; routine
engineering documentation does not trigger Ollama inference.


Final closure (2026-10-30): offline 834 passed, 87 deselected (18 dependency
deprecation warnings); real frameworks 13 passed, 907 deselected (12 warnings);
real Gradio/Chromium review test 1 passed, 4 deselected. Ruff lint and format
passed for 316 maintained files; source references passed exact freshness checks.

Browser preparation initially failed because the older text fixture uses legacy
tool identities/contracts; the canonical calculator fixture then encountered the
real widget store's requirement for an installed fixture folder. The final
review-only harness explicitly injects canonical ApprovedTool metadata and doubles
widget storage through a pipeline proxy. No production checks were weakened.
The passing browser test covers partial suggestions, visible editable JSON,
missing-case notice, blocked approval, explicit save and cleared review checkbox.
It does not run native verification or establish live/model/isolation correctness.
No need to rerun native isolation: its implementation and runtime boundary were
unchanged. Port 7882 remains running its previously loaded source; applying this
block there requires a separately authorized restart. Existing drafts are not
silently regenerated; their missing cases remain editable.
