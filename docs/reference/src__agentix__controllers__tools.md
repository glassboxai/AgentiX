# Reference for src/agentix/controllers/tools.py

Tools tab backend and shared session/model callbacks, independent of Gradio.

Source fingerprint: 1ddecf0a3fed1de969efbb64b0335ac31669e1b65977266dc61e26fc0ec69ebe

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolsBackend

Framework-independent browser callbacks; every operation rechecks ownership.

Kind: class. Declared return: Not declared / class. Source line: 10.

### ToolsBackend.submit

Submit to this browser's controller and update its server State token.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 13.

### ToolsBackend.poll

Return a coherent editor/request-ID snapshot for this browser only.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 24.

### ToolsBackend.approve

Approve only the displayed request through the verified owner controller.

Kind: callable. Declared return: bool. Source line: 29.

### ToolsBackend.reject

Reject only the displayed request through the verified owner controller.

Kind: callable. Declared return: bool. Source line: 34.

### ToolsBackend.toggle

Update this owner's setting and return its server State token.

Kind: callable. Declared return: str. Source line: 39.

### ToolsBackend.validation_status

Read this owner's trusted validation state, never another session's.

Kind: callable. Declared return: str. Source line: 45.

### ToolsBackend.approval_readiness

Return the current proposal's UI-only approval readiness for its owner.

Kind: callable. Declared return: tuple[Any, str]. Source line: 49.

### ToolsBackend.unload

Cancel this framework owner's pending work when its browser unloads.

Kind: callable. Declared return: None. Source line: 55.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | annotations | Imported dependency for annotations in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SessionOwnerAccess | Imported dependency for SessionOwnerAccess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| ToolsBackend.submit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 13 |
| ToolsBackend.submit | message | Parameter for message in ToolsBackend.submit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 13 |
| ToolsBackend.submit | token | Parameter for token in ToolsBackend.submit; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 13 |
| ToolsBackend.submit | request | Parameter for request in ToolsBackend.submit; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 13 |
| ToolsBackend.submit | session | Local binding for session in ToolsBackend.submit; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| ToolsBackend.poll | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| ToolsBackend.poll | token | Parameter for token in ToolsBackend.poll; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 24 |
| ToolsBackend.poll | request | Parameter for request in ToolsBackend.poll; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 24 |
| ToolsBackend.poll | session | Local binding for session in ToolsBackend.poll; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| ToolsBackend.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| ToolsBackend.approve | text | Parameter for text in ToolsBackend.approve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 29 |
| ToolsBackend.approve | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 29 |
| ToolsBackend.approve | token | Parameter for token in ToolsBackend.approve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 29 |
| ToolsBackend.approve | request | Parameter for request in ToolsBackend.approve; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 29 |
| ToolsBackend.approve | session | Local binding for session in ToolsBackend.approve; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| ToolsBackend.reject | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| ToolsBackend.reject | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 34 |
| ToolsBackend.reject | token | Parameter for token in ToolsBackend.reject; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 34 |
| ToolsBackend.reject | request | Parameter for request in ToolsBackend.reject; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| ToolsBackend.reject | session | Local binding for session in ToolsBackend.reject; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| ToolsBackend.toggle | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| ToolsBackend.toggle | enabled | Parameter for enabled in ToolsBackend.toggle; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 39 |
| ToolsBackend.toggle | token | Parameter for token in ToolsBackend.toggle; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 39 |
| ToolsBackend.toggle | request | Parameter for request in ToolsBackend.toggle; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 39 |
| ToolsBackend.toggle | session | Local binding for session in ToolsBackend.toggle; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| ToolsBackend.validation_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| ToolsBackend.validation_status | token | Parameter for token in ToolsBackend.validation_status; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 45 |
| ToolsBackend.validation_status | request | Parameter for request in ToolsBackend.validation_status; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 45 |
| ToolsBackend.approval_readiness | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| ToolsBackend.approval_readiness | text | Parameter for text in ToolsBackend.approval_readiness; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 50 |
| ToolsBackend.approval_readiness | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str | Enclosing invocation or class/instance lifetime | 50 |
| ToolsBackend.approval_readiness | token | Parameter for token in ToolsBackend.approval_readiness; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 50 |
| ToolsBackend.approval_readiness | request | Parameter for request in ToolsBackend.approval_readiness; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 50 |
| ToolsBackend.unload | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ToolsBackend.unload | request | Parameter for request in ToolsBackend.unload; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 55 |
