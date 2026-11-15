# ADR 0007: host-gated creation with approved artifact receipts

Status: accepted for LIVE-FIX-001.

One Crew containing all creation tasks cannot let the host verify persistence
between architect and coder or coder and tester. Model completion prose is not
evidence that a save tool ran. Creation now uses one sequential Crew per stage,
and later task descriptions contain the original query plus actual approved file
content. No previous agent's completion summary substitutes for approved context.

Storage records in-memory owner/operation/write-ID/hash receipts for reviewed
overwrite saves. Random write IDs distinguish an unchanged fresh save from a
stale existing file. Receipt creation compares observed persisted bytes with the
approved candidate, including platform newline translation. Host stage checks
require a fresh receipt, nonempty bounded UTF-8 content and matching bytes. Python
compilation checks syntax without importing generated code. Final acceptance
rechecks approved code and specification and revokes evidence after a mismatch.

This does not introduce crash-atomic storage, filesystem authentication, universal
correctness or model-output attestation. Receipts never replace native isolated
tests, manual acceptance or the execution ledger. File auto-approval remains a
user setting; acceptance always requires explicit manual review.

The user's required model is qwen3-coder:30b. The live harness and documented
launch commands default to it. Alternate-model failures remain historical
observations and cannot establish the required model's functionality.
