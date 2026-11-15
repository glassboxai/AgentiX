# Reference for tests/unit/test_sandbox_protocol.py

Validate bounded process reports without executing generated project artifacts.

Source fingerprint: 65bc1161122c1a92f9584a39988387a36a937e5a83d2b3a934a75e1eb5d6146a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_plain_text_cannot_become_a_test_report

Verify plain text cannot become a test report.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_runtime_is_never_started_on_unsupported_platform

Verify runtime is never started on unsupported platform.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_duplicate_observation_values_are_rejected

Verify duplicate observation values are rejected.

Kind: callable. Declared return: Not declared / class. Source line: 24.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_plain_text_cannot_become_a_test_report | output | Parameter for output in test_plain_text_cannot_become_a_test_report; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_plain_text_cannot_become_a_test_report | decode_report | Imported dependency for decode report in test_plain_text_cannot_become_a_test_report; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_runtime_is_never_started_on_unsupported_platform | monkeypatch | Parameter for monkeypatch in test_runtime_is_never_started_on_unsupported_platform; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_runtime_is_never_started_on_unsupported_platform | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 17 |
| test_duplicate_observation_values_are_rejected | decode_report | Imported dependency for decode report in test_duplicate_observation_values_are_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 26 |
