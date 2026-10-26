# Reference for src/agentix/storage.py

Approval-aware UTF-8 artifact persistence and final Python validation.

The repository receives its path/approval boundary explicitly. It preserves the
legacy result strings and non-atomic write semantics; compile never executes.

Source fingerprint: e0788e86c853ba114741c6c53fe2eb0b5a8ef548a54ce0516d269b882be5f609

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ArtifactStore

Persist artifacts using an injected path and approval coordinator.

Kind: class. Declared return: Not declared / class. Source line: 19.

### ArtifactStore.__init__

Store the boundary without creating directories or requesting approval.

Kind: callable. Declared return: None. Source line: 22.

### ArtifactStore.write

Write/append UTF-8 content after path and human authorization checks.

For Python artifacts, compile the final approved text without executing
it before opening the destination. Appends validate the combined file.
Rejected/invalid edits leave existing file contents intact. Errors retain
the legacy string-result contract; invalid paths raise SecurityViolationError.
Syntax validation is not a safety guarantee for executable Python.

Kind: callable. Declared return: str. Source line: 26.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | SecurityViolationError | Imported dependency for SecurityViolationError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 16 |
| ArtifactStore.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| ArtifactStore.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 22 |
| ArtifactStore.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| ArtifactStore.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| ArtifactStore.write | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 26 |
| ArtifactStore.write | filename | Parameter for filename in ArtifactStore.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| ArtifactStore.write | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 26 |
| ArtifactStore.write | mode | Parameter for mode in ArtifactStore.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| ArtifactStore.write | target_path | Local binding for target path in ArtifactStore.write; use the enclosing contract and type below. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| ArtifactStore.write | write_identity | Local binding for write identity in ArtifactStore.write; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 37 |
| ArtifactStore.write | target_dir | Local binding for target dir in ArtifactStore.write; use the enclosing contract and type below. | Return type of dirname; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| ArtifactStore.write | approved | Local binding for approved in ArtifactStore.write; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 42, 51 |
| ArtifactStore.write | _ | Local binding for  in ArtifactStore.write; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| ArtifactStore.write | action_name | Local binding for action name in ArtifactStore.write; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| ArtifactStore.write | final_content | Local binding for final content in ArtifactStore.write; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| ArtifactStore.write | candidate | Local binding for candidate in ArtifactStore.write; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65, 68 |
| ArtifactStore.write | existing | Managed resource for existing in ArtifactStore.write; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 67 |
| ArtifactStore.write | exc | Caught exception for exc in ArtifactStore.write; use the enclosing contract and type below. | (SyntaxError, ValueError, TypeError) | Current exception handler; Python clears this binding afterward | 71 |
| ArtifactStore.write | f | Managed resource for f in ArtifactStore.write; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 82 |
| ArtifactStore.write | stream | Managed resource for stream in ArtifactStore.write; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 91 |
| ArtifactStore.write | observed | Returned observation checked against the reviewed host-side expectation. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| ArtifactStore.write | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| ArtifactStore.write | e | Caught exception for e in ArtifactStore.write; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 106 |
