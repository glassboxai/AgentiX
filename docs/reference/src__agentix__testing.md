# Reference for src/agentix/testing.py

Approved test persistence and OS-observed, content-bound unittest outcomes.

Source fingerprint: 371e498f471afdc511203dc7bccf0ae7021fdbfa2958465f3136457267662e12

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### TestRunner

Publish evidence only from an isolated process and current approved bytes.

Kind: class. Declared return: Not declared / class. Source line: 13.

### TestRunner.__init__

Connect storage, an isolated backend and a per-runtime evidence ledger.

Kind: callable. Declared return: None. Source line: 16.

### TestRunner.run_and_save_tests_tool

Persist final approved edits, isolate execution and reject empty/skipped suites.

Kind: callable. Declared return: str. Source line: 27.

### TestRunner.verify_existing_tool

Re-run existing approved bytes without changing files or trusting old reports.

Kind: callable. Declared return: str. Source line: 42.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 10 |
| TestRunner.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| TestRunner.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 18 |
| TestRunner.__init__ | record_incidence | Parameter for record incidence in TestRunner.__init__; use the enclosing contract and type below. | Callable[..., str] | Enclosing invocation or class/instance lifetime | 19 |
| TestRunner.__init__ | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend | Enclosing invocation or class/instance lifetime | 20 |
| TestRunner.__init__ | verification | Content-bound ledger used to authorize only the current approved operation. | VerificationLedger | Enclosing invocation or class/instance lifetime | 21 |
| TestRunner.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | tuple | Enclosing invocation or class/instance lifetime | 24 |
| TestRunner.__init__ | self.record_incidence | Attribute for record incidence in TestRunner.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 24 |
| TestRunner.__init__ | self.sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| TestRunner.__init__ | self.verification | Content-bound ledger used to authorize only the current approved operation. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| TestRunner.run_and_save_tests_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| TestRunner.run_and_save_tests_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 27 |
| TestRunner.run_and_save_tests_tool | test_code | Proposed unittest source requiring approval and isolated execution. | str | Enclosing invocation or class/instance lifetime | 27 |
| TestRunner.run_and_save_tests_tool | clean | Local binding for clean in TestRunner.run_and_save_tests_tool; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 30, 32, 34, 36 |
| TestRunner.run_and_save_tests_tool | saved | Local binding for saved in TestRunner.run_and_save_tests_tool; use the enclosing contract and type below. | Return type of safe_write_file; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| TestRunner.verify_existing_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| TestRunner.verify_existing_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 42 |
| TestRunner.verify_existing_tool | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 46 |
| TestRunner.verify_existing_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| TestRunner.verify_existing_tool | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| TestRunner.verify_existing_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| TestRunner.verify_existing_tool | details | Local binding for details in TestRunner.verify_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63, 66 |
| TestRunner.verify_existing_tool | exc | Caught exception for exc in TestRunner.verify_existing_tool; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 64 |
