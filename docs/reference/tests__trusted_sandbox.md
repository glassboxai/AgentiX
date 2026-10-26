# Reference for tests/trusted_sandbox.py

OS-boundary double for trusted infrastructure fixtures only, never production.

This deliberately does not provide isolation. Native security is verified by the
separate opt-in suite. The application receives a simulated OS observation here.

Source fingerprint: d22e894922ef4871fdb6dd65c9db2d80e1af8b98c050b7de4a0aa0a4ebab0618

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### approve_next_review

Simulate a human only in infrastructure tests; retain callback errors.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### approve_next_review.respond

Provide respond for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### TrustedFixtureSandbox

Execute only independently authored test fixture bytes with the real protocol.

Kind: class. Declared return: Not declared / class. Source line: 44.

### TrustedFixtureSandbox.execute

Use an isolated temporary input folder, without claiming native coverage.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### TrustedFixtureSandbox.evaluate

Run the trusted fixture through the same observation worker protocol.

Kind: callable. Declared return: Not declared / class. Source line: 84.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | sandbox_worker | Imported dependency for sandbox worker in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SandboxResult | Imported dependency for SandboxResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | decode_report | Imported dependency for decode report in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| approve_next_review | security | Owner-scoped approval and path boundary injected into this service. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| approve_next_review | edited | Parameter for edited in approve_next_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| approve_next_review | errors | Local binding for errors in approve_next_review; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 22 |
| approve_next_review.respond | deadline | Local binding for deadline in approve_next_review.respond; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| approve_next_review.respond | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| approve_next_review | thread | Local binding for thread in approve_next_review; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| TrustedFixtureSandbox.execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | tests | Optional unittest source snapshot; child-authored success remains provisional. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | tool_name | Validated public tool identifier within the configured storage boundary. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | function_name | Public callable selected for the current operation; empty selects test mode. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | observation | Parameter for observation in TrustedFixtureSandbox.execute; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| TrustedFixtureSandbox.execute | folder | Managed resource for folder in TrustedFixtureSandbox.execute; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 49 |
| TrustedFixtureSandbox.execute | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| TrustedFixtureSandbox.execute | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| TrustedFixtureSandbox.execute | output | Local binding for output in TrustedFixtureSandbox.execute; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| TrustedFixtureSandbox.execute | report | Local binding for report in TrustedFixtureSandbox.execute; use the enclosing contract and type below. | Return type of decode_report; see its callable contract | Enclosing invocation or class/instance lifetime | 79, 81 |
| TrustedFixtureSandbox.evaluate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| TrustedFixtureSandbox.evaluate | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| TrustedFixtureSandbox.evaluate | tool_name | Validated public tool identifier within the configured storage boundary. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| TrustedFixtureSandbox.evaluate | function_name | Public callable selected for the current operation; empty selects test mode. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| TrustedFixtureSandbox.evaluate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
