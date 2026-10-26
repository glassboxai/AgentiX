# ACCEPT-001: provisional tests, human review and external acceptance evaluation

Status: implemented and verified, 2026-10-19. Installer deferred; Docker excluded. Evidence: `../reports/HUMAN_ACCEPTANCE.md`; user instructions: `../ACCEPTANCE_REVIEW.md`.

## Requirements and observable acceptance criteria

- ACCEPT-01: generated unittest execution remains isolated and provisional. Its report never authorizes execution, even when forged or successful. Display provisional status and require a current successful observation before proposing acceptance cases.
- ACCEPT-02: the application generates cases through a CrewAI tool accepting bounded strict JSON data. Each case includes an ID, purpose, public function, keyword inputs and an expected JSON value, approximate numeric value or exception type. No executable assertions, eval, pickle, imports or model comparisons occur in the host evaluator.
- ACCEPT-03: show the generated Python tests, provisional summary and editable acceptance JSON in the owner's review panel. Approval is explicit, expiring and single-use, with existing browser-snapshot request/owner checks. File auto-approval must never approve acceptance. Invalid edited cases, rejection, expiry, cancellation or owner/operation/content changes deny authorization.
- ACCEPT-04: after human approval, evaluate each case in a fresh isolated process, providing only function/inputs and implementation bytes. Never send expected values or the acceptance document into the child. Validate typed returned data or exception observations; compare in maintained host code. Process failure, ambiguity, invalid output or any failed case denies the tool.
- ACCEPT-05: only host-evaluated approved cases can authorize their covered function names. Bind authorization to owner, operation, exact code/test bytes, acceptance contract digest and evaluator version. Changes or rechecks revoke it. The creation pipeline requires final acceptance, not provisional unittest output.
- ACCEPT-06: show separate provisional, pending human review, approved/evaluating, rejected/failed and verified-against-approved-cases states. Editing a contract changes its digest. Audit events contain IDs/status/counts, not source, arguments or expected values. Explain that finite approved cases do not prove all-input correctness or actual internal execution provenance.
- ACCEPT-07: default tests remain offline with trusted temporary fixtures and an explicit OS double; separate native/framework tests verify the real boundaries. Never inspect or run the project's generated artifact contents or restart the live application.

## JSON contract version 1

Top level: `{"version":1,"cases":[...]}`. One to sixteen cases, unique IDs. A case has exactly `id`, `purpose`, `function`, `kwargs`, `expect`. JSON values must be finite, bounded and free of duplicate object keys. Expectations:

- `{"kind":"value","value":5}`: recursive, type-aware exact JSON comparison (booleans and numbers are distinct).
- `{"kind":"approx","value":0.3,"abs_tol":1e-9,"rel_tol":1e-9}`: finite numeric comparison with explicit nonnegative tolerances.
- `{"kind":"raises","type":"ValueError"}`: exact reported exception type, not exception text.

Contracts and approval receipts are runtime memory only and not silently persisted as artifact writes. They must be proposed/reviewed again after restart or a new operation. Existing file approvals remain independent. The UI displays the exact approved contract digest and per-case verdicts after evaluation.

## Affected components

Add acceptance schema/evaluator service, typed observation protocol, ledger acceptance bindings, mandatory manual approval metadata and session-scoped review status. Wire tools, agents, orchestration and UI while keeping legacy callback signatures. Update tests, architecture, incidents, change log and report evidence in English.
