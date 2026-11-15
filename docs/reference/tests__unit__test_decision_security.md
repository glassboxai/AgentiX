# Reference for tests/unit/test_decision_security.py

Fail-closed creation decisions must never trigger arbitrary tool creation.

Source fingerprint: ddbd543500d887c80eed0313280e4e0590b76a9f8df0dda26e17449f22de0608

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_invalid_manager_decision_never_starts_creation

Verify invalid manager decision never starts creation.

Kind: callable. Declared return: Not declared / class. Source line: 26.

### test_manager_query_and_decision_payload_are_not_logged

Verify manager query and decision payload are not logged.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_execution_exception_payload_is_not_logged

Verify execution exception payload is not logged.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### test_storage_exception_payload_is_not_logged

Verify storage exception payload is not logged.

Kind: callable. Declared return: Not declared / class. Source line: 72.

### test_degenerate_manager_output_is_rejected_as_a_contract_error

Verify degenerate manager output is rejected as a contract error.

Kind: callable. Declared return: Not declared / class. Source line: 87.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_invalid_manager_decision_never_starts_creation | system | Parameter for system in test_invalid_manager_decision_never_starts_creation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_invalid_manager_decision_never_starts_creation | monkeypatch | Parameter for monkeypatch in test_invalid_manager_decision_never_starts_creation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_invalid_manager_decision_never_starts_creation | response | Bounded response text to render or validate; it is not executable code. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_invalid_manager_decision_never_starts_creation | factory | Local binding for factory in test_invalid_manager_decision_never_starts_creation; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_invalid_manager_decision_never_starts_creation | pipeline | Local binding for pipeline in test_invalid_manager_decision_never_starts_creation; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_manager_query_and_decision_payload_are_not_logged | system | Parameter for system in test_manager_query_and_decision_payload_are_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_manager_query_and_decision_payload_are_not_logged | monkeypatch | Parameter for monkeypatch in test_manager_query_and_decision_payload_are_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_manager_query_and_decision_payload_are_not_logged | caplog | Parameter for caplog in test_manager_query_and_decision_payload_are_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_manager_query_and_decision_payload_are_not_logged | secret | Local binding for secret in test_manager_query_and_decision_payload_are_not_logged; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 40 |
| test_execution_exception_payload_is_not_logged | system | Parameter for system in test_execution_exception_payload_is_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_execution_exception_payload_is_not_logged | caplog | Parameter for caplog in test_execution_exception_payload_is_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_execution_exception_payload_is_not_logged | directory | Local binding for directory in test_execution_exception_payload_is_not_logged; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_execution_exception_payload_is_not_logged | ledger | Local binding for ledger in test_execution_exception_payload_is_not_logged; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_execution_exception_payload_is_not_logged | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_execution_exception_payload_is_not_logged | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_storage_exception_payload_is_not_logged | system | Parameter for system in test_storage_exception_payload_is_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_storage_exception_payload_is_not_logged | monkeypatch | Parameter for monkeypatch in test_storage_exception_payload_is_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_storage_exception_payload_is_not_logged | caplog | Parameter for caplog in test_storage_exception_payload_is_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_storage_exception_payload_is_not_logged | system.security.auto_approve | Attribute for system.security.auto approve in test_storage_exception_payload_is_not_logged; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 75 |
| test_degenerate_manager_output_is_rejected_as_a_contract_error | system | Parameter for system in test_degenerate_manager_output_is_rejected_as_a_contract_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_degenerate_manager_output_is_rejected_as_a_contract_error | monkeypatch | Parameter for monkeypatch in test_degenerate_manager_output_is_rejected_as_a_contract_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_degenerate_manager_output_is_rejected_as_a_contract_error | response | Bounded response text to render or validate; it is not executable code. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
