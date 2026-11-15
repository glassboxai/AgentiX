# V7-054: acceptance approval readiness

Status: implemented.

## Requirement

The Tools review panel must disable Approve until the current acceptance proposal
is valid for the existing version-1 contract and the evaluator has reached
`pending_review`. Editing, clearing, replacing or losing the displayed request
must disable it immediately and show bounded corrective guidance.

## Design and boundaries

`UiController.approval_readiness` reuses `security.acceptance.parse_contract`;
it introduces no second schema or acceptance rule. The Gradio text-input event
and the poll continuation update only presentation state. `on_approve`, pending
request ownership and `AcceptanceEvaluator.submit` remain mandatory security
boundaries and revalidate the exact text.

No policy-fingerprint source, acceptance contract, persistent format or generated
artifact is changed.

## Regression evidence

`tests/unit/test_acceptance_ui.py` covers valid, invalid, pending, stale/replaced
and edited/cleared proposals. The focused offline suite passes; framework
validation remains a separate Gradio-adapter check.
