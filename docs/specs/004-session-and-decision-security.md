# SEC-005: Session, approval and manager-decision boundaries

Status: explicitly approved and implemented on 2026-10-19. Verification and red/green evidence are in `../reports/SESSION_SECURITY.md`.

## Requirements

| ID | Contract | Acceptance |
| --- | --- | --- |
| SES-01 | Browser sessions own controller, state, activity, agents and approval settings | Two session owners cannot read/approve each other's pending work or share history/configuration |
| SES-02 | Server-owned session registry | Opaque server token bound to Gradio session hash; mismatched/stale tokens rejected; idle inactive sessions expire; capacity bounded; close cancels pending approval |
| AUTH-02 | Every manual decision names owner and request | Reject missing, wrong, expired, duplicate and previous request IDs; never overwrite a live pending request |
| FLOW-02 | Strict creation-decision contract | Require exact action and fields, safe snake_case identifier, nonblank bounded purpose; reject malformed/ambiguous/duplicate-key JSON; remove arbitrary fallback; no creation after error |
| LOG-02 | Correlated application events without payloads | Session/run/request identifiers and error type, not full queries/code/model output; session-local activity capture with no process-wide redirect per worker |
| UI-02 | Race-safe controller updates | One active workflow per session; late/busy messages cannot redirect the active answer; editor loads once per approval ID |

## Compatibility and explicit changes

Direct text answers and full raw/fenced creation JSON remain supported. Invalid names are rejected rather than silently normalized; prose-wrapped creation JSON and extra/duplicate fields are rejected. Manual resolution now requires explicit request and owner identifiers. Valid edited text, rejection, timeout and pre-write Python validation remain. Default CLI/legacy facades remain available; the browser uses per-session runtimes rather than shared agents.

Approval owner means the owning server-side workflow session, not a verified human identity. Gradio session hashes route sessions but do not implement account authentication. Shared artifact storage/catalog remains intentional. Session tokens are held in Gradio server-side State and checked against the framework request. Public diagnostic IDs are independent UUIDs, not those access tokens. Approval IDs travel with the browser editor snapshot in a hidden non-stateful textbox; mutable server State could relabel a queued stale click. Do not infer hostile-client authentication or filesystem isolation from this change.

Session expiry applies to inactive sessions; active workers remain until completion or explicit close. A delivered framework unload event cancels unresolved approvals and denies new writes; server-State cleanup and registry expiry provide fallback cleanup. Lost unload notifications are not guaranteed immediate. Previously authorized/executing operations are not forcibly interrupted or rolled back. Output from unrelated/background threads without session context is never copied into another session's activity. Provider verbosity is disabled so application diagnostics do not rely on printing prompts/code.

## Deferred

OS-enforced execution isolation, validation of actual pipeline testing outcomes, crash-atomic writes, complete third-party log redaction/file rotation, installation and real-model quality are separate blocks. Project generated_tools contents remain excluded. All artifacts used by tests are independently authored temporary fixtures.

## Implemented defaults and diagnostics

Registry capacity is 128 sessions; inactive entries expire after 1800 seconds when the registry next processes a callback. Active workers are retained until completion or explicit close. Registry access is serialized; first callbacks with no token reuse an existing owner session rather than creating duplicates. Both provider client and role objects belong to the session. Ollama model weights may remain shared inside the local service.

Activity retains at most 256 records of 4096 characters. A single host stdout router uses ContextVars; workers never globally redirect stdout. Tool wrappers explicitly restore context from their bound security owner for provider thread pools. Unscoped background output is not copied into any session buffer. Application diagnostic events contain fixed event names, session/run/request IDs, error type and optional line number, not query/source/output/exception bodies. Provider/agent verbosity is disabled. This is not blanket sanitization of all third-party or arbitrary tool output.

Creation JSON requires exactly action, tool_name and purpose. Names are 1–64 ASCII snake_case characters beginning with a letter and excluding Windows devices. Purpose must be nonblank text of at most 4000 characters. Whole responses are bounded to 100000 characters. Duplicate/extra fields, prose-wrapped JSON, unsupported actions, malformed JSON and empty sanitized answers fail closed. Direct valid textual answers remain supported; no automatic retry is added.
