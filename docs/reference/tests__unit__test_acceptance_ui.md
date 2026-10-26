# Reference for tests/unit/test_acceptance_ui.py

Show human-review context without treating generated source as markup.

Source fingerprint: 7337d6626b2f8f021e6007edea563acd55f583ffe94ece91a1b29f9068daca4f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_review_panel_shows_python_tests_and_provisional_summary

Verify review panel shows python tests and provisional summary.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_validation_status_uses_owned_evaluator_and_escapes_values

Verify validation status uses owned evaluator and escapes values.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_final_status_shows_expected_and_observed_data

Verify final status shows expected and observed data.

Kind: callable. Declared return: Not declared / class. Source line: 42.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_review_panel_shows_python_tests_and_provisional_summary | system | Parameter for system in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| test_review_panel_shows_python_tests_and_provisional_summary | monkeypatch | Parameter for monkeypatch in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| test_review_panel_shows_python_tests_and_provisional_summary | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 8 |
| test_review_panel_shows_python_tests_and_provisional_summary | snapshot | Local binding for snapshot in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Return type of poll_with_request; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | system | Parameter for system in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | system.app.validation | Attribute for system.app.validation in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | rendered | Local binding for rendered in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Return type of validation_status; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_final_status_shows_expected_and_observed_data | system | Parameter for system in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_final_status_shows_expected_and_observed_data | system.app.validation | Attribute for system.app.validation in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_final_status_shows_expected_and_observed_data | rendered | Local binding for rendered in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Return type of validation_status; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
