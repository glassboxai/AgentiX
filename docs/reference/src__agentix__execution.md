# Reference for src/agentix/execution.py

Validate calls before importing code exclusively inside an OS-isolated child.

Source fingerprint: a6e5745cd14d49db3c69fb66a5e643080f100bdbaa5b2175e0deef84a6536a41

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolExecutor

Enforce evidence and JSON boundaries independently of agent instructions.

Kind: class. Declared return: Not declared / class. Source line: 15.

### ToolExecutor.__init__

Bind a per-runtime ledger and injectable isolated process backend.

Kind: callable. Declared return: None. Source line: 18.

### ToolExecutor.execute_generated_tool_tool

Validate input and evidence, then pass exact verified bytes to a child.

Kind: callable. Declared return: str. Source line: 27.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | computation_only | Imported dependency for computation only in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 12 |
| ToolExecutor.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| ToolExecutor.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 20 |
| ToolExecutor.__init__ | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend | Enclosing invocation or class/instance lifetime | 21 |
| ToolExecutor.__init__ | verification | Content-bound ledger used to authorize only the current approved operation. | VerificationLedger | Enclosing invocation or class/instance lifetime | 22 |
| ToolExecutor.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| ToolExecutor.__init__ | self.sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| ToolExecutor.__init__ | self.verification | Content-bound ledger used to authorize only the current approved operation. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| ToolExecutor.execute_generated_tool_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| ToolExecutor.execute_generated_tool_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 28 |
| ToolExecutor.execute_generated_tool_tool | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 28 |
| ToolExecutor.execute_generated_tool_tool | kwargs_json | Untrusted JSON argument text to validate before execution. | str | Enclosing invocation or class/instance lifetime | 28 |
| ToolExecutor.execute_generated_tool_tool | clean | Local binding for clean in ToolExecutor.execute_generated_tool_tool; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| ToolExecutor.execute_generated_tool_tool | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| ToolExecutor.execute_generated_tool_tool | exc | Caught exception for exc in ToolExecutor.execute_generated_tool_tool; use the enclosing contract and type below. | (ValueError, RecursionError) | Current exception handler; Python clears this binding afterward | 41, 88 |
| ToolExecutor.execute_generated_tool_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ToolExecutor.execute_generated_tool_tool | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ToolExecutor.execute_generated_tool_tool | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| ToolExecutor.execute_generated_tool_tool | approved | Local binding for approved in ToolExecutor.execute_generated_tool_tool; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| ToolExecutor.execute_generated_tool_tool | _ | Local binding for  in ToolExecutor.execute_generated_tool_tool; use the enclosing contract and type below. | Return type of request_user_permission; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| ToolExecutor.execute_generated_tool_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
