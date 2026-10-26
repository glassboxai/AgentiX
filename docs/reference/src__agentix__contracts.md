# Reference for src/agentix/contracts.py

Structural contracts shared by storage, execution and interface adapters.

Source fingerprint: 098082df3d918e6ead0d8ecd21f74eb53d580e256186f3cc579b37db2cc3f054

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SecurityBoundary

Required authorization/path API; it does not promise OS isolation.

Kind: class. Declared return: Not declared / class. Source line: 9.

### SecurityBoundary.record_saved_artifact

Bind a host-observed approved save to its original operation identity.

Kind: callable. Declared return: None. Source line: 17.

### SecurityBoundary.get_artifact_receipt

Read the current operation's immutable save receipt and byte digest.

Kind: callable. Declared return: tuple[str, str] | None. Source line: 23.

### SecurityBoundary.validate_and_resolve_path

Return a confined path or raise SecurityViolationError.

Kind: callable. Declared return: str. Source line: 27.

### SecurityBoundary.request_user_permission

Return approval and final edited text, denying on timeout.

Kind: callable. Declared return: tuple[bool, str]. Source line: 31.

### SecurityBoundary.is_closed

Return whether the owner has been cancelled or unloaded.

Kind: callable. Declared return: bool. Source line: 43.

### SecurityBoundary.safe_write_file

Persist approved content or return the existing textual error result.

Kind: callable. Declared return: str. Source line: 47.

### SecurityBoundary.get_pending_request

Return an independent snapshot of the pending request.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 51.

### SecurityBoundary.resolve_pending_request

Accept a matching, unexpired, single-use owner/request decision.

Kind: callable. Declared return: bool. Source line: 55.

### SecurityBoundary.cancel_pending

Close the owner and deny pending/future writes.

Kind: callable. Declared return: None. Source line: 66.

### ExecutionBackend

Injected process boundary shared by execution, tests and acceptance.

Structural compatibility is not proof of isolation. Callers must still
check isolation flags, process outcomes and current operation evidence.

Kind: class. Declared return: Not declared / class. Source line: 71.

### ExecutionBackend.execute

Run approved bytes inside a bounded child and return an observation.

Code and optional tests are exact staged source bytes; tool_name names
their module, function_name selects the public callable (empty in test
mode), and kwargs contains bounded JSON data. The returned process
outcome includes an untrusted child report, not a semantic guarantee.
Implementations may raise RuntimeError if provisioning is unavailable;
callers must deny execution rather than introduce a host fallback.

Kind: callable. Declared return: 'SandboxResult'. Source line: 78.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | TYPE_CHECKING | Imported dependency for TYPE CHECKING in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SandboxResult | Imported dependency for SandboxResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| SecurityBoundary | auto_approve | Typed binding for auto approve in SecurityBoundary; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 12 |
| SecurityBoundary | owner_id | Session owner identity used to prevent cross-session authorization. | str | Enclosing invocation or class/instance lifetime | 13 |
| SecurityBoundary | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str | Enclosing invocation or class/instance lifetime | 14 |
| SecurityBoundary | activity_capture | Typed binding for activity capture in SecurityBoundary; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 15 |
| SecurityBoundary.record_saved_artifact | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| SecurityBoundary.record_saved_artifact | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 18 |
| SecurityBoundary.record_saved_artifact | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 18 |
| SecurityBoundary.record_saved_artifact | owner_id | Session owner identity used to prevent cross-session authorization. | str | Enclosing invocation or class/instance lifetime | 18 |
| SecurityBoundary.record_saved_artifact | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | str | Enclosing invocation or class/instance lifetime | 18 |
| SecurityBoundary.get_artifact_receipt | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| SecurityBoundary.get_artifact_receipt | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 23 |
| SecurityBoundary.validate_and_resolve_path | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| SecurityBoundary.validate_and_resolve_path | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 27 |
| SecurityBoundary.validate_and_resolve_path | filename | Parameter for filename in SecurityBoundary.validate_and_resolve_path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| SecurityBoundary.request_user_permission | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| SecurityBoundary.request_user_permission | filepath | Parameter for filepath in SecurityBoundary.request_user_permission; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| SecurityBoundary.request_user_permission | action | Parameter for action in SecurityBoundary.request_user_permission; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| SecurityBoundary.request_user_permission | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 35 |
| SecurityBoundary.request_user_permission | require_manual | Parameter for require manual in SecurityBoundary.request_user_permission; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 37 |
| SecurityBoundary.request_user_permission | review_context | Parameter for review context in SecurityBoundary.request_user_permission; use the enclosing contract and type below. | dict[str, Any] &#124; None | Enclosing invocation or class/instance lifetime | 38 |
| SecurityBoundary.is_closed | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| SecurityBoundary.safe_write_file | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| SecurityBoundary.safe_write_file | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 47 |
| SecurityBoundary.safe_write_file | filename | Parameter for filename in SecurityBoundary.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 47 |
| SecurityBoundary.safe_write_file | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 47 |
| SecurityBoundary.safe_write_file | mode | Parameter for mode in SecurityBoundary.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 47 |
| SecurityBoundary.get_pending_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| SecurityBoundary.resolve_pending_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| SecurityBoundary.resolve_pending_request | decision | Parameter for decision in SecurityBoundary.resolve_pending_request; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 57 |
| SecurityBoundary.resolve_pending_request | edited_content | Parameter for edited content in SecurityBoundary.resolve_pending_request; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 58 |
| SecurityBoundary.resolve_pending_request | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str &#124; None | Enclosing invocation or class/instance lifetime | 60 |
| SecurityBoundary.resolve_pending_request | owner_id | Session owner identity used to prevent cross-session authorization. | str &#124; None | Enclosing invocation or class/instance lifetime | 61 |
| SecurityBoundary.cancel_pending | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| ExecutionBackend.execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| ExecutionBackend.execute | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 80 |
| ExecutionBackend.execute | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes &#124; None | Enclosing invocation or class/instance lifetime | 81 |
| ExecutionBackend.execute | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 82 |
| ExecutionBackend.execute | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 83 |
| ExecutionBackend.execute | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 84 |
