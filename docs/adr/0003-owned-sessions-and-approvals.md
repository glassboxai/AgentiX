# ADR-0003: Owned sessions, identified approvals and fail-closed decisions

Date: 2026-10-19. Status: accepted under SEC-005.

## Decision

The browser view uses a server registry and opaque Gradio State token bound to the framework session hash. Each session constructs its own mutable provider client, agents, coordinator and controller. Diagnostic session UUIDs differ from access tokens. Maximum registry size is 128; inactive entries expire after 1800 seconds when another callback accesses the registry. Active workers are not silently evicted. Delivered unload events, State deletion and registry expiry close the owner; arbitrary active Python cannot be interrupted by this mechanism.

Keep the existing class-style SecurityManager facade for compatibility, but create isolated subclasses via for_owner() for browser runtimes. Each manual request has a unique ID, owner and monotonic deadline; the owner slot cannot be overwritten. Resolution is single-use and fail-closed on identity, type or expiry errors. Cancellation denies unresolved and new requests; accepted or executing work is not transactionally rolled back.

Approval IDs must be submitted with the displayed editor snapshot. A Gradio State-only ID can change during preprocessing of a queued click, associating old content with new work. Use a hidden non-stateful textbox for that nonsecret ID and recheck it server-side. The access token remains server-State-only.

Manager creation uses exactly action/tool_name/purpose with bounded values and safe canonical names. Accept complete raw/fenced JSON, reject ambiguous/prose-wrapped/duplicate/extra-field decisions, and remove arbitrary fallback. Ordinary valid text answers remain supported. There are no automatic retries or new tool creations after validation errors.

Application diagnostics emit fixed event names, public session/run/request IDs, error type and optional line, without user/model/source/exception bodies. One host stdout proxy uses explicit ContextVars; tool wrappers restore context from their bound owner when provider pools lose it. Activity retains at most 256 records of 4096 characters. Provider verbosity is disabled. This is not general third-party-output redaction.

## Consequences and limits

Manual resolution callers must supply request and owner IDs. Browser callbacks perform ownership checks for every action. UI/controller APIs return independent snapshots, track the active response and refresh editors by request identity. Files/catalog remain shared as before; browser isolation is not account authentication or filesystem isolation. Other code with the same OS privileges can still compromise the process.

Independent pipeline outcome verification, OS-enforced code isolation, crash-atomic persistence, complete log rotation/redaction and the installer remain later blocks. No project generated artifact was inspected or modified to implement or test these boundaries.
