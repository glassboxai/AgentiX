# Reference for src/agentix/approvals.py

Owner-bound approval requests with explicit, single-use decision identifiers.

Source fingerprint: 28978d24fb741e78f26cc788e692a36ac90c96b8c3b8f02af3a2ec9b4f73343e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ApprovalCoordinator

Coordinate one pending request per owner without overwriting live work.

Runtime owners use for_owner() or an independently configured subclass.
Resolution requires both identifiers; missing/late/cross-owner decisions deny.
This is workflow ownership, not authentication of a human account.

Kind: class. Declared return: Not declared / class. Source line: 15.

### ApprovalCoordinator.for_owner

Create isolated synchronization/configuration for a server-owned identity.

Kind: callable. Declared return: type. Source line: 39.

### ApprovalCoordinator.record_saved_artifact

Record a host-observed approved write, bounded to this owner/operation.

The random receipt distinguishes a fresh approved save of identical bytes
from a stale file. Only maintained storage code calls this after writing.
This is workflow evidence, not a replacement for isolated test execution.

Kind: callable. Declared return: None. Source line: 64.

### ApprovalCoordinator.get_artifact_receipt

Return immutable write identity/digest only for the current live operation.

Kind: callable. Declared return: tuple[str, str] | None. Source line: 86.

### ApprovalCoordinator.request_user_permission

Publish a uniquely identified request; deny on timeout or an occupied slot.

Only the owning waiter cleans its slot. The event is never reused while
another request is pending, preventing cross-request decisions/cleanup.

Kind: callable. Declared return: tuple[bool, str]. Source line: 95.

### ApprovalCoordinator.is_closed

Report owner shutdown without exposing mutable synchronization state.

Kind: callable. Declared return: bool. Source line: 150.

### ApprovalCoordinator.get_pending_request

Return a deep-copy snapshot so readers cannot alter the pending slot.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 156.

### ApprovalCoordinator.resolve_pending_request

Resolve exactly once if owner/request match and the deadline is valid.

False means no authorization was accepted. Expiration wakes the owning
waiter with denial; duplicate responses cannot overwrite its first result.

Kind: callable. Declared return: bool. Source line: 162.

### ApprovalCoordinator.cancel_pending

Deny outstanding work when its session closes, waking the waiter.

Kind: callable. Declared return: None. Source line: 204.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | deepcopy | Imported dependency for deepcopy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 12 |
| ApprovalCoordinator | owner_id | Session owner identity used to prevent cross-session authorization. | str | Enclosing invocation or class/instance lifetime | 23 |
| ApprovalCoordinator | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str | Enclosing invocation or class/instance lifetime | 24 |
| ApprovalCoordinator | activity_capture | Typed binding for activity capture in ApprovalCoordinator; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 25 |
| ApprovalCoordinator | approval_timeout | Local binding for approval timeout in ApprovalCoordinator; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 26 |
| ApprovalCoordinator | auto_approve | Local binding for auto approve in ApprovalCoordinator; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 27 |
| ApprovalCoordinator | _approval_event | Local binding for approval event in ApprovalCoordinator; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| ApprovalCoordinator | _approval_decision | Local binding for approval decision in ApprovalCoordinator; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 29 |
| ApprovalCoordinator | _edited_content | Typed binding for edited content in ApprovalCoordinator; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 30 |
| ApprovalCoordinator | _pending_request | Typed binding for pending request in ApprovalCoordinator; use the enclosing contract and type below. | dict[str, Any] &#124; None | Enclosing invocation or class/instance lifetime | 31 |
| ApprovalCoordinator | _resolved | Local binding for resolved in ApprovalCoordinator; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 32 |
| ApprovalCoordinator | _closed | Local binding for closed in ApprovalCoordinator; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 33 |
| ApprovalCoordinator | _lock | Local binding for lock in ApprovalCoordinator; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| ApprovalCoordinator | _saved_artifacts | Typed binding for saved artifacts in ApprovalCoordinator; use the enclosing contract and type below. | dict[str, tuple[str, str, str, str]] | Enclosing invocation or class/instance lifetime | 35 |
| ApprovalCoordinator | _clock | Local binding for clock in ApprovalCoordinator; use the enclosing contract and type below. | Return type of staticmethod; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| ApprovalCoordinator.for_owner | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| ApprovalCoordinator.for_owner | owner_id | Session owner identity used to prevent cross-session authorization. | str | Enclosing invocation or class/instance lifetime | 39 |
| ApprovalCoordinator.for_owner | timeout | Parameter for timeout in ApprovalCoordinator.for_owner; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 39 |
| ApprovalCoordinator.record_saved_artifact | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| ApprovalCoordinator.record_saved_artifact | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 65 |
| ApprovalCoordinator.record_saved_artifact | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 65 |
| ApprovalCoordinator.record_saved_artifact | owner_id | Session owner identity used to prevent cross-session authorization. | str | Enclosing invocation or class/instance lifetime | 65 |
| ApprovalCoordinator.record_saved_artifact | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str | Enclosing invocation or class/instance lifetime | 65 |
| ApprovalCoordinator.record_saved_artifact | cls._saved_artifacts | Attribute for cls. saved artifacts in ApprovalCoordinator.record_saved_artifact; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 76 |
| ApprovalCoordinator.record_saved_artifact.comprehension_76 | key | Comprehension item for key in ApprovalCoordinator.record_saved_artifact.comprehension_76; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 78 |
| ApprovalCoordinator.record_saved_artifact.comprehension_76 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 78 |
| ApprovalCoordinator.get_artifact_receipt | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| ApprovalCoordinator.get_artifact_receipt | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 86 |
| ApprovalCoordinator.get_artifact_receipt | receipt | Local binding for receipt in ApprovalCoordinator.get_artifact_receipt; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| ApprovalCoordinator.request_user_permission | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| ApprovalCoordinator.request_user_permission | filepath | Parameter for filepath in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 97 |
| ApprovalCoordinator.request_user_permission | action | Parameter for action in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 98 |
| ApprovalCoordinator.request_user_permission | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 99 |
| ApprovalCoordinator.request_user_permission | require_manual | Parameter for require manual in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 101 |
| ApprovalCoordinator.request_user_permission | review_context | Parameter for review context in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | dict[str, Any] &#124; None | Enclosing invocation or class/instance lifetime | 102 |
| ApprovalCoordinator.request_user_permission | cls._approval_decision | Attribute for cls. approval decision in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 120 |
| ApprovalCoordinator.request_user_permission | cls._edited_content | Attribute for cls. edited content in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 121, 141 |
| ApprovalCoordinator.request_user_permission | cls._resolved | Attribute for cls. resolved in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 122 |
| ApprovalCoordinator.request_user_permission | request | Local binding for request in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 123 |
| ApprovalCoordinator.request_user_permission | cls._pending_request | Attribute for cls. pending request in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 133, 140 |
| ApprovalCoordinator.request_user_permission | received | Local binding for received in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | Return type of wait; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| ApprovalCoordinator.request_user_permission | approved | Local binding for approved in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | Return type of bool; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| ApprovalCoordinator.request_user_permission | final | Local binding for final in ApprovalCoordinator.request_user_permission; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 138 |
| ApprovalCoordinator.is_closed | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 150 |
| ApprovalCoordinator.get_pending_request | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 156 |
| ApprovalCoordinator.resolve_pending_request | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 163 |
| ApprovalCoordinator.resolve_pending_request | decision | Parameter for decision in ApprovalCoordinator.resolve_pending_request; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 164 |
| ApprovalCoordinator.resolve_pending_request | edited_content | Parameter for edited content in ApprovalCoordinator.resolve_pending_request; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 165 |
| ApprovalCoordinator.resolve_pending_request | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str &#124; None | Enclosing invocation or class/instance lifetime | 167 |
| ApprovalCoordinator.resolve_pending_request | owner_id | Session owner identity used to prevent cross-session authorization. | str &#124; None | Enclosing invocation or class/instance lifetime | 168 |
| ApprovalCoordinator.resolve_pending_request | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| ApprovalCoordinator.resolve_pending_request | cls._resolved | Attribute for cls. resolved in ApprovalCoordinator.resolve_pending_request; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 191, 196 |
| ApprovalCoordinator.resolve_pending_request | cls._approval_decision | Attribute for cls. approval decision in ApprovalCoordinator.resolve_pending_request; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 192, 197 |
| ApprovalCoordinator.resolve_pending_request | cls._edited_content | Attribute for cls. edited content in ApprovalCoordinator.resolve_pending_request; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 198 |
| ApprovalCoordinator.cancel_pending | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 204 |
| ApprovalCoordinator.cancel_pending | cls._closed | Attribute for cls. closed in ApprovalCoordinator.cancel_pending; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 207 |
| ApprovalCoordinator.cancel_pending | cls._resolved | Attribute for cls. resolved in ApprovalCoordinator.cancel_pending; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 209 |
| ApprovalCoordinator.cancel_pending | cls._approval_decision | Attribute for cls. approval decision in ApprovalCoordinator.cancel_pending; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 210 |
