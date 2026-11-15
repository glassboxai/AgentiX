# V5-043 — Persisted application connection code

Status: approved, implemented and verified. See [verification](../reports/V5_043_GENERATED_CONNECTION_CODE.md) for authored-fixture and real Simply app evidence and limits.

The user selected generated connection code instead of our graph interpreter. Existing tool source, contracts, approvals and execution isolation remain unchanged. Preserve port 7880 and other user processes.

## Observable acceptance

- CODE-01: CrewAI sequential creation tasks produce reviewable Python connection code and a finite widget inventory. The new manifest contains no workflow edges, binding selectors or topological order.
- CODE-02: opening or executing the approved package calls neither agents nor a graph interpreter. Only the native child imports generated application code and approved tool copies.
- CODE-03: tools and approved reusable widgets retain their exact bytes and current dependency checks. Generated connection code is editable during review; edits invalidate application approval.
- CODE-04: explicit host-held application acceptance inputs and expected results are required before approval. Model code/tests do not supply authoritative expectations. Missing cases leave a reviewable draft, not an opaque generation failure.
- CODE-05: input/result contracts, exact-byte approval, AppContainer, bounded calls and browser comparisons remain mandatory. No host execution fallback. Old packages retain their versioned compatibility route.

## Runtime contract

A generated `application_logic.py` exports `run(payload, call)`. Ordinary Python variables connect returned values to later calls. `call(widget_id, **arguments)` executes the selected approved tool in the native worker, records its arguments/result and rejects unknown, duplicate or missing calls. The widget inventory describes presentation/dependencies only; it has no connectivity. Application inputs are explicit JSON schemas. The maintained compositor renders application inputs and approved tool widgets, populating tool argument controls from observed calls.

Independent application cases are reviewed through `application_acceptance.json`, outside the child package. The file is populated conservatively from reviewed catalog cases where possible (see [V6-045](045-proposed-acceptance-cases.md)); unresolved fields require human completion and all values require human review. It is included in the displayed review. Saving invalidates any previous approval. Native and browser checks compare actual results against these host-held expectations. Existing tool unit tests are not rerun.
