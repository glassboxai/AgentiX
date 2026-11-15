# Reference for tests/unit/test_acceptance_ui.py

Show human-review context without treating generated source as markup.

Source fingerprint: c8857b3bd81a736deccfea4fa1ab759e84f170005e0750fc6adc987a867e4692

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _acceptance_pending

Install one bounded acceptance review owned by the test session.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_valid_acceptance_proposal_enables_approval

Enable the review control only after the existing contract parser accepts it.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_invalid_acceptance_proposal_disables_approval

Prevent an invalid acceptance proposal from reaching the generic approval error.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_pending_or_replaced_acceptance_request_disables_approval

Keep approval disabled until the current pending request has been validated.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_pending_acceptance_validation_disables_approval

Do not enable approval before the evaluator reports the review-ready stage.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_missing_acceptance_validation_disables_approval

Do not treat a proposal as validated when no evaluator is available.

Kind: callable. Declared return: Not declared / class. Source line: 73.

### test_editing_a_valid_acceptance_proposal_disables_approval_immediately

Revalidate the edited text instead of retaining the prior valid button state.

Kind: callable. Declared return: Not declared / class. Source line: 83.

### test_review_panel_shows_python_tests_and_provisional_summary

Verify review panel shows python tests and provisional summary.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_validation_status_uses_owned_evaluator_and_escapes_values

Verify validation status uses owned evaluator and escapes values.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_final_status_shows_expected_and_observed_data

Verify final status shows expected and observed data.

Kind: callable. Declared return: Not declared / class. Source line: 132.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | VALID_CONTRACT | Module binding for VALID CONTRACT in module; use the enclosing contract and type below. | str | Module/process lifetime | 5 |
| _acceptance_pending | system | Parameter for system in _acceptance_pending; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| _acceptance_pending | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_valid_acceptance_proposal_enables_approval | system | Parameter for system in test_valid_acceptance_proposal_enables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_valid_acceptance_proposal_enables_approval | monkeypatch | Parameter for monkeypatch in test_valid_acceptance_proposal_enables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_valid_acceptance_proposal_enables_approval | system.app.validation | Attribute for system.app.validation in test_valid_acceptance_proposal_enables_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_valid_acceptance_proposal_enables_approval | button | Local binding for button in test_valid_acceptance_proposal_enables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_valid_acceptance_proposal_enables_approval | message | Local binding for message in test_valid_acceptance_proposal_enables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_invalid_acceptance_proposal_disables_approval | system | Parameter for system in test_invalid_acceptance_proposal_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_invalid_acceptance_proposal_disables_approval | monkeypatch | Parameter for monkeypatch in test_invalid_acceptance_proposal_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_invalid_acceptance_proposal_disables_approval | system.app.validation | Attribute for system.app.validation in test_invalid_acceptance_proposal_disables_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_invalid_acceptance_proposal_disables_approval | button | Local binding for button in test_invalid_acceptance_proposal_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_invalid_acceptance_proposal_disables_approval | message | Local binding for message in test_invalid_acceptance_proposal_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_pending_or_replaced_acceptance_request_disables_approval | system | Parameter for system in test_pending_or_replaced_acceptance_request_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_pending_or_replaced_acceptance_request_disables_approval | monkeypatch | Parameter for monkeypatch in test_pending_or_replaced_acceptance_request_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_pending_or_replaced_acceptance_request_disables_approval | button | Local binding for button in test_pending_or_replaced_acceptance_request_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_pending_or_replaced_acceptance_request_disables_approval | message | Local binding for message in test_pending_or_replaced_acceptance_request_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_pending_acceptance_validation_disables_approval | system | Parameter for system in test_pending_acceptance_validation_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_pending_acceptance_validation_disables_approval | monkeypatch | Parameter for monkeypatch in test_pending_acceptance_validation_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_pending_acceptance_validation_disables_approval | system.app.validation | Attribute for system.app.validation in test_pending_acceptance_validation_disables_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_pending_acceptance_validation_disables_approval | button | Local binding for button in test_pending_acceptance_validation_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_pending_acceptance_validation_disables_approval | message | Local binding for message in test_pending_acceptance_validation_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_missing_acceptance_validation_disables_approval | system | Parameter for system in test_missing_acceptance_validation_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| test_missing_acceptance_validation_disables_approval | monkeypatch | Parameter for monkeypatch in test_missing_acceptance_validation_disables_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| test_missing_acceptance_validation_disables_approval | button | Local binding for button in test_missing_acceptance_validation_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_missing_acceptance_validation_disables_approval | message | Local binding for message in test_missing_acceptance_validation_disables_approval; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | system | Parameter for system in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 83 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | monkeypatch | Parameter for monkeypatch in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 83 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | system.app.validation | Attribute for system.app.validation in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | ready_button | Local binding for ready button in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | _ | Local binding for  in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | edited_button | Local binding for edited button in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_editing_a_valid_acceptance_proposal_disables_approval_immediately | message | Local binding for message in test_editing_a_valid_acceptance_proposal_disables_approval_immediately; use the enclosing contract and type below. | Return type of approval_readiness; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_review_panel_shows_python_tests_and_provisional_summary | system | Parameter for system in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_review_panel_shows_python_tests_and_provisional_summary | monkeypatch | Parameter for monkeypatch in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_review_panel_shows_python_tests_and_provisional_summary | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_review_panel_shows_python_tests_and_provisional_summary | snapshot | Local binding for snapshot in test_review_panel_shows_python_tests_and_provisional_summary; use the enclosing contract and type below. | Return type of poll_with_request; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | system | Parameter for system in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | system.app.validation | Attribute for system.app.validation in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_validation_status_uses_owned_evaluator_and_escapes_values | rendered | Local binding for rendered in test_validation_status_uses_owned_evaluator_and_escapes_values; use the enclosing contract and type below. | Return type of validation_status; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_final_status_shows_expected_and_observed_data | system | Parameter for system in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 132 |
| test_final_status_shows_expected_and_observed_data | system.app.validation | Attribute for system.app.validation in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_final_status_shows_expected_and_observed_data | rendered | Local binding for rendered in test_final_status_shows_expected_and_observed_data; use the enclosing contract and type below. | Return type of validation_status; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
