# REUSE-002 / UI-REVIEW-002

Date: 2026-10-25. Status: investigation and approved layout correction in progress.

## Problem and acceptance

The previous delivery verified consecutive queries through real Playwright and Ollama but retained approvals only in the session ledger. Reload/restart loses them, so an already reviewed tool requires acceptance again. The user reports this is unacceptable; durable cross-session authorization scope is being clarified before implementing persistent trust.

The user explicitly requests that Authorization & Review Required, including code/tests and approval/rejection buttons, appear below Tool validation in the right column, not in the model-settings sidebar. There must be one review editor and one pair of decision buttons. Closing the sidebar must not hide a pending review. Public callbacks retain owner/request identity validation and manual acceptance requirements.

## Verification

Capture a failing Playwright layout assertion before changing the view. Exercise first review, actual calls with new inputs and absence of repeated review in the same session. Extend browser coverage to reload/new session and process restart after durable authorization is approved and specified. Use temporary trusted fixtures first and a supervised real qwen3-coder:30b GUI run separately. No existing generated_tools artifacts or live process restarts are authorized by these tests.


## Approved durable authorization

The user explicitly approved persistence across reload, other sessions and process restart. Only successful host-accepted calls publish protected records outside tool storage, under user-local application data. Windows DPAPI user protection with explicit machine-bound entropy seals records; tests inject an authenticated fixture protector. Records bind canonical storage root, tool identifier, exact code/test hashes, reviewed functions/contract and a maintained security-policy fingerprint. No source bodies are persisted in this store. Unreadable, changed, relocated, modified-policy or tampered records fail closed and require review; observed drift revokes the durable record. Session closure does not revoke the user's durable approval. Sensitive/unclassified calls retain per-call manual permission and unchanged native isolation. Existing historic tools without a protected record require one initial review; reports and child unittest success cannot migrate trust.

Use atomic unique-temp replacement per record; do not promise transactional coordination with artifacts or immediate cross-process cancellation. DPAPI protects user data, not against malicious software running as the same user. Machine binding uses the Windows MachineGuid as optional entropy. Store errors deny durable reuse and emit fixed diagnostics; current valid execution may still return its observed result if saving approval fails.

Playwright must cover initial review, same-session new inputs, page reload, a second browser context, server restart with retained temporary storage, and changed-source reapproval. A real qwen3-coder:30b run will additionally exercise the creation and reload/reuse path. Never inspect old project artifacts to bootstrap approval.
