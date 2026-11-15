# Reference for tests/test_persistent_application_native.py

Opt-in native lifetime proof; this deliberately lasts longer than five minutes.

Source fingerprint: a051da9eed664be1fb04f9bba9c7d8ac0e8546b509323c1d407319504b9f0c09

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_persistent_survives_five_minutes_and_closes

Catch an inherited fixed TTL and verify owned process/temp cleanup after close.

Kind: callable. Declared return: Not declared / class. Source line: 14.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ApplicationSession | Imported dependency for ApplicationSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 11 |
| test_native_persistent_survives_five_minutes_and_closes | tmp_path | Parameter for tmp path in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| test_native_persistent_survives_five_minutes_and_closes | package | Imported dependency for package in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| test_native_persistent_survives_five_minutes_and_closes | folder | Local binding for folder in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_native_persistent_survives_five_minutes_and_closes | capability | Local binding for capability in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_native_persistent_survives_five_minutes_and_closes | session | Managed resource for session in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 20 |
| test_native_persistent_survives_five_minutes_and_closes | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_native_persistent_survives_five_minutes_and_closes | started | Local binding for started in test_native_persistent_survives_five_minutes_and_closes; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_native_persistent_survives_five_minutes_and_closes | response | Bounded response text to render or validate; it is not executable code. | Return type of request; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
