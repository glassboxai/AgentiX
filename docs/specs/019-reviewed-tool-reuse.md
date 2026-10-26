# REUSE-001: Session-owned reuse of reviewed tools

Status: implemented and verified. See ../reports/REUSE_019_VALIDATION.md for initial failures, passing regressions and supervised live evidence.

## Observable acceptance

1. A newly created tool still requires specification, implementation, tests and human acceptance. Only a successful isolated call can establish a reusable grant.
2. A second natural-language query in the same session may select a previously successful tool and invoke an approved function with new arguments, without code display, repeated unittest execution or repeated acceptance.
3. Every reuse checks exact code/test bytes and owner, live session, covered function and policy version. Observed drift permanently revokes the grant, including after restoration. Grants are memory-only, bounded to 64 tools, and do not cross sessions or restarts.
4. Only a conservative subset of computation-only Python is eligible for unattended calls. Unknown constructs and file/network/process capabilities require explicit manual confirmation bound to the exact call. Approval never expands AppContainer permissions or enables host execution.
5. Manager instructions use a host preparation operation returning approved signatures and reviewed context, never require reading/displaying implementation during normal reuse. A missing grant follows the existing review path.
6. Results remain bound to a fresh host-observed execution in the current query. A failed/new query cannot reuse an earlier result.
7. Offline adversarial tests, real framework/native integration and a disposable GUI exercise distinguish doubles from live qwen3-coder:30b evidence. Existing generated_tools and live applications remain untouched.

## Design

VerificationLedger retains separate session grants after successful execution. Preparation rebinds accepted evidence to the new operation only after content and owner checks. Capability classification is a conservative UX gate, not proof of purity or an OS security boundary. ToolExecutor owns per-call approval and rechecks integrity/operation after waiting. No persistent trust database or permission escalation is introduced.

## Incident REUSE-ERR-001

Previously the manager explicitly requested fresh tests and acceptance on every query, while ledger identities included operation_id. Therefore successful tools could not be reused unattended. Regressions must demonstrate the second call, absence of testing/review for safe code, sensitive-call denial, owner/drift rejection and fresh result receipts.

## Scope superseded by REUSE-002

The user subsequently rejected the session-only lifetime and explicitly approved durable protected approval across sessions and restarts. See 020-durable-reuse-and-review-layout.md. The original consecutive-query evidence remains historical; it did not verify reload or restart.
