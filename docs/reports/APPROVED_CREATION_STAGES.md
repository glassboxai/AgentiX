# LIVE-FIX-001 implementation verification and paused 30B validation

Date: 2026-10-19. The approved stage/receipt/callback corrections are implemented.
Real-model validation is PAUSED at the user's request, not passed or failed.

Original requirements now reach creation alongside the manager summary. Separate
architect, coder and tester crews use persisted approved context. Each save must
produce a fresh owner/operation-bound receipt matching actual approved bytes.
Empty, oversized, stale, missing or changed artifacts block advancement. Final
creation rechecks specification/code and requires current human acceptance.
No-output approve/reject callbacks discard their internal booleans.

## Tests and incidents

Six initial stage gate cases failed before implementation (`stage-gates-red.txt`).
The suite now includes ten stage cases, including a successful acceptance-service
lifecycle with trusted temporary fixtures. The two earlier strict xfails were
converted to ordinary regressions after the approved fixes.

- LIVE-FIX-ERR-001: receipt creation could initially adopt an intervening write
  between storage and observation. The reproducer failed in
  `stage-receipt-race-red.txt`. Compare observed persisted bytes with the approved
  candidate, including platform newline conversion, before issuing a receipt.
- LIVE-FIX-ERR-002: final acceptance initially did not recheck the approved source
  after the testing stage. A substituted source could pass a selected case and
  complete creation. `stage-final-source-red.txt` records the failure. Recheck
  specification/code and revoke ledger evidence on mismatch.

Final offline suite: 274 passed. Real framework adapters: four passed. Native
Windows isolation: nine passed. Deterministic Playwright browser suite: three
passed. These are 290 passing cases. Ruff check and format verification pass for
69 active Python files. Raw evidence is in `approved-stage-offline.txt`,
`approved-stage-frameworks.txt`, `approved-stage-native.txt`,
`approved-stage-browser.txt` and `approved-stage-ruff.txt`. Native/browser suites
preceded the final orchestration-only recheck; offline/framework checks ran after
that final source change. They exercise their specific boundaries, not model
quality. Receipt writes remain non-atomic; no crash-atomic storage is claimed.

## Required-model validation

The user confirmed that Agentix must use qwen3-coder:30b. The launcher default and
current instructions now match it; earlier smaller-model samples are historical,
not validation of the required model. No replacement model was used in this run.
The temporary real instance used `ollama/qwen3-coder:30b`, native isolation,
manual approvals and external temporary storage. The manifest and server log are
`live-coder30b-manifest.json` and `live-coder30b-server.log`.

The user paused execution before any approval. The manager had attempted existing
tool verification against empty temporary storage, which failed and requested
directory creation for an incidence record. No directory/file approval was given,
no implementation/test was created and no generated code ran. Do not label this
interrupted sample a model failure or a completed functional validation. The
temporary process was stopped after verifying its recorded PID and command line.
The user's original live process and existing generated artifacts were untouched.

The user identified the unreadable technical event stream as a presentation
regression and requested shared system workflow instructions plus agent-handoff
checks. Source comparison confirms original verbose output was replaced by
technical capture. Proposed remediation and validation are in specification 010;
that additional implementation awaits user validation. A new real 30B run should
use a problem-only query after that correction, not embedded engineering workflow
instructions supplied by the user.

No additional report-generation inference was requested after the user paused
execution. This reviewed record uses source comparison and raw verification
evidence directly; local model report drafting is deferred with the paused run.
