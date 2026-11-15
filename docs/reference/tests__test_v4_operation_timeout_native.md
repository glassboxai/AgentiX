# Reference for tests/test_v4_operation_timeout_native.py

Real native callback watchdog and cleanup evidence, without model inference.

Source fingerprint: d36c8fbb202050dfb9987d0cec838a5df7a8042b47afd8d94f35eb71caeea4ff

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_blocked_callback_stops_the_owned_persistent_job

A GUI with no idle TTL still terminates a callback exceeding 45 seconds.

Kind: callable. Declared return: Not declared / class. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | schema3_package | Imported dependency for schema3 package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ApprovedApplication | Imported dependency for ApprovedApplication in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | ApplicationSession | Imported dependency for ApplicationSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| test_blocked_callback_stops_the_owned_persistent_job | tmp_path | Parameter for tmp path in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_blocked_callback_stops_the_owned_persistent_job | package | Local binding for package in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_blocked_callback_stops_the_owned_persistent_job | capability | Local binding for capability in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_blocked_callback_stops_the_owned_persistent_job | probe | Local binding for probe in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 23 |
| test_blocked_callback_stops_the_owned_persistent_job | files | Local binding for files in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Return type of tuple; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_blocked_callback_stops_the_owned_persistent_job.comprehension_39 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| test_blocked_callback_stops_the_owned_persistent_job.comprehension_39 | body | Comprehension item for body in test_blocked_callback_stops_the_owned_persistent_job.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| test_blocked_callback_stops_the_owned_persistent_job | observed | Returned observation checked against the reviewed host-side expectation. | Return type of ApprovedApplication; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_blocked_callback_stops_the_owned_persistent_job | session | Managed resource for session in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 41 |
| test_blocked_callback_stops_the_owned_persistent_job | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_blocked_callback_stops_the_owned_persistent_job | started | Local binding for started in test_blocked_callback_stops_the_owned_persistent_job; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
