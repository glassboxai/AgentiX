# Reference for tests/test_applications_backend.py

Owner and cross-tab coordination regressions for Applications backend.

Source fingerprint: 4dee97c9ad28cce5885da158775c9c827b139457b0bf6bccb9b877bec93dfdcc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### registry

Supply an inert controller; model/native work is never needed for ownership tests.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### test_foreign_token_is_rejected_before_model_or_storage

Catch application generation using another browser's Tools session.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_active_tools_operation_blocks_application_generation

Catch concurrent model work bypassing the shared controller state.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_repair_requires_a_failed_reviewed_candidate

Catch automatic/unbounded repair without an independent failure report.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_explicit_rejection_revokes_repair_eligibility

Catch proposing another model repair after the human has rejected the operation.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_rejection_revokes_verified_data_execution

Rejecting a verified proposal must revoke its native data-execution grant.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_data_operation_reports_the_json_contract_without_echoing_input

V7-073: a schema-3 payload rejection names the JSON error, never the typed text.

Kind: callable. Declared return: Not declared / class. Source line: 105.

### test_data_contract_names_declared_inputs_and_an_example_payload

V7-073: the owner sees the closed input schema before typing a payload.

Kind: callable. Declared return: Not declared / class. Source line: 139.

### test_repair_control_is_unavailable_until_owned_verification_failure

The UI must not advertise repair before its server-side eligibility exists.

Kind: callable. Declared return: Not declared / class. Source line: 162.

### test_unsaved_editor_changes_block_approval

A checkbox cannot approve older bytes while different source is displayed.

Kind: callable. Declared return: Not declared / class. Source line: 171.

### test_missing_registered_host_requirement_keeps_review_pending

A missing host prerequisite must not approve, execute or close reviewed bytes.

Kind: callable. Declared return: Not declared / class. Source line: 188.

### test_missing_registered_host_requirement_keeps_review_pending.Requirements

Offer only the fixed browser requirement through the injected host boundary.

Kind: class. Declared return: Not declared / class. Source line: 195.

### test_missing_registered_host_requirement_keeps_review_pending.Requirements.missing

Return an inert maintained requirement instead of running an installer.

Kind: callable. Declared return: Not declared / class. Source line: 198.

### test_missing_registered_host_requirement_keeps_review_pending.Supervisor

Fail if approval crosses the host prerequisite boundary.

Kind: class. Declared return: Not declared / class. Source line: 205.

### test_missing_registered_host_requirement_keeps_review_pending.Supervisor.approve

Record an unexpected approval attempt.

Kind: callable. Declared return: Not declared / class. Source line: 208.

### test_explicit_host_dependency_install_requires_pending_owner_consent

Only the owning pending review can invoke the fixed registered installer.

Kind: callable. Declared return: Not declared / class. Source line: 232.

### test_explicit_host_dependency_install_requires_pending_owner_consent.Requirements

Record the one injected installer identity without exposing command choice.

Kind: class. Declared return: Not declared / class. Source line: 239.

### test_explicit_host_dependency_install_requires_pending_owner_consent.Requirements.install

Record an explicit installation request and return its reviewed metadata.

Kind: callable. Declared return: Not declared / class. Source line: 242.

### test_generation_only_exposes_safe_catalog_dependency_diagnostics

An arbitrary model/parser ValueError must not be mistaken for a safe diagnostic.

Kind: callable. Declared return: Not declared / class. Source line: 263.

### test_generation_only_exposes_safe_catalog_dependency_diagnostics.fail

Simulate a parser error whose untrusted body mentions catalog.

Kind: callable. Declared return: Not declared / class. Source line: 269.

### test_generation_names_an_unsupported_public_input_key

V7-059: a closed contract rejection reaches the owner with its bounded reason.

Kind: callable. Declared return: Not declared / class. Source line: 287.

### test_generation_names_an_unsupported_public_input_key.fail

Simulate a model proposal whose input schema carries a numeric bound.

Kind: callable. Declared return: Not declared / class. Source line: 295.

### test_generation_passes_the_active_session_llm_to_the_pipeline

Applications use the already configured session client, not a new default.

Kind: callable. Declared return: Not declared / class. Source line: 317.

### test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline

Capture the configured client before the controlled generation failure.

Kind: class. Declared return: Not declared / class. Source line: 332.

### test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.set_model_client

Record the model boundary received from the owning session.

Kind: callable. Declared return: Not declared / class. Source line: 335.

### test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.generate

Stop after the injection boundary without creating an artifact.

Kind: callable. Declared return: Not declared / class. Source line: 339.

### test_generation_blocks_a_changed_tofu_identity_before_the_pipeline

A changed local baseline cannot reach application model orchestration.

Kind: callable. Declared return: Not declared / class. Source line: 354.

### test_generation_blocks_a_changed_tofu_identity_before_the_pipeline.changed_identity

Simulate the fixed local-profile change diagnostic.

Kind: callable. Declared return: str. Source line: 363.

### test_generation_names_the_missing_profile_selection

A missing saved selection reports its own action instead of a changed digest.

Kind: callable. Declared return: Not declared / class. Source line: 380.

### test_generation_names_the_missing_profile_selection.missing_selection

Simulate the closed missing-selection diagnostic.

Kind: callable. Declared return: str. Source line: 391.

### test_poll_does_not_race_with_widget_publication

Only the verifier owns dependency checks while publishing a new widget grant.

Kind: callable. Declared return: Not declared / class. Source line: 413.

### test_poll_does_not_race_with_widget_publication.partial_write

Model the short interval between widget source and protected record writes.

Kind: callable. Declared return: Not declared / class. Source line: 422.

### test_saved_group_clears_dirty_marker_and_can_enter_new_review

Explicit group save must not leave a stale dirty flag blocking approval.

Kind: callable. Declared return: Not declared / class. Source line: 439.

### test_streaming_callbacks_never_suspend_while_holding_owner_lock

Gradio may resume a generator on another thread; lexical locks must release.

Kind: callable. Declared return: Not declared / class. Source line: 471.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | RLock | Imported dependency for RLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | SessionAccessError | Imported dependency for SessionAccessError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| registry | ModelProfile | Imported dependency for ModelProfile in registry; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 14 |
| registry.lambda_17 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 17 |
| test_foreign_token_is_rejected_before_model_or_storage | sessions | Local binding for sessions in test_foreign_token_is_rejected_before_model_or_storage; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_foreign_token_is_rejected_before_model_or_storage | owner | Local binding for owner in test_foreign_token_is_rejected_before_model_or_storage; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_foreign_token_is_rejected_before_model_or_storage | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_active_tools_operation_blocks_application_generation | sessions | Local binding for sessions in test_active_tools_operation_blocks_application_generation; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_active_tools_operation_blocks_application_generation | owner | Local binding for owner in test_active_tools_operation_blocks_application_generation; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_active_tools_operation_blocks_application_generation | owner.controller.state.is_running | Attribute for owner.controller.state.is running in test_active_tools_operation_blocks_application_generation; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 48 |
| test_active_tools_operation_blocks_application_generation | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_active_tools_operation_blocks_application_generation | rows | Local binding for rows in test_active_tools_operation_blocks_application_generation; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_repair_requires_a_failed_reviewed_candidate | sessions | Local binding for sessions in test_repair_requires_a_failed_reviewed_candidate; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_repair_requires_a_failed_reviewed_candidate | owner | Local binding for owner in test_repair_requires_a_failed_reviewed_candidate; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_repair_requires_a_failed_reviewed_candidate | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_repair_requires_a_failed_reviewed_candidate | rows | Local binding for rows in test_repair_requires_a_failed_reviewed_candidate; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_explicit_rejection_revokes_repair_eligibility | sessions | Local binding for sessions in test_explicit_rejection_revokes_repair_eligibility; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_explicit_rejection_revokes_repair_eligibility | owner | Local binding for owner in test_explicit_rejection_revokes_repair_eligibility; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_explicit_rejection_revokes_repair_eligibility | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_explicit_rejection_revokes_repair_eligibility | request | Local binding for request in test_explicit_rejection_revokes_repair_eligibility; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_explicit_rejection_revokes_repair_eligibility | _ | Local binding for  in test_explicit_rejection_revokes_repair_eligibility; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_explicit_rejection_revokes_repair_eligibility | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_explicit_rejection_revokes_repair_eligibility | state.repair_allowed | Attribute for state.repair allowed in test_explicit_rejection_revokes_repair_eligibility; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 75 |
| test_rejection_revokes_verified_data_execution | tmp_path | Parameter for tmp path in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_rejection_revokes_verified_data_execution | candidate | Imported dependency for candidate in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 82 |
| test_rejection_revokes_verified_data_execution | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| test_rejection_revokes_verified_data_execution | calls | Local binding for calls in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 86 |
| test_rejection_revokes_verified_data_execution | supervisor | Local binding for supervisor in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_rejection_revokes_verified_data_execution | sessions | Local binding for sessions in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_rejection_revokes_verified_data_execution | owner | Local binding for owner in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_rejection_revokes_verified_data_execution | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_rejection_revokes_verified_data_execution | request | Local binding for request in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_rejection_revokes_verified_data_execution | _ | Local binding for  in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 92, 97 |
| test_rejection_revokes_verified_data_execution | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_rejection_revokes_verified_data_execution | state.candidate | Attribute for state.candidate in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_rejection_revokes_verified_data_execution | state.candidate.verified | Attribute for state.candidate.verified in test_rejection_revokes_verified_data_execution; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 95 |
| test_rejection_revokes_verified_data_execution | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_data_operation_reports_the_json_contract_without_echoing_input | tmp_path | Parameter for tmp path in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_data_operation_reports_the_json_contract_without_echoing_input | candidate | Imported dependency for candidate in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 107 |
| test_data_operation_reports_the_json_contract_without_echoing_input | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 109 |
| test_data_operation_reports_the_json_contract_without_echoing_input | calls | Local binding for calls in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 111 |
| test_data_operation_reports_the_json_contract_without_echoing_input | supervisor | Local binding for supervisor in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_data_operation_reports_the_json_contract_without_echoing_input.lambda_113 | approved | Callback parameter for approved in test_data_operation_reports_the_json_contract_without_echoing_input.lambda_113; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 113 |
| test_data_operation_reports_the_json_contract_without_echoing_input.lambda_113 | payload | Callback parameter for payload in test_data_operation_reports_the_json_contract_without_echoing_input.lambda_113; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 113 |
| test_data_operation_reports_the_json_contract_without_echoing_input | sessions | Local binding for sessions in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| test_data_operation_reports_the_json_contract_without_echoing_input | owner | Local binding for owner in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_data_operation_reports_the_json_contract_without_echoing_input | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_data_operation_reports_the_json_contract_without_echoing_input | request | Local binding for request in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_data_operation_reports_the_json_contract_without_echoing_input | _ | Local binding for  in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 120, 130, 134 |
| test_data_operation_reports_the_json_contract_without_echoing_input | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_data_operation_reports_the_json_contract_without_echoing_input | state.candidate | Attribute for state.candidate in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_data_operation_reports_the_json_contract_without_echoing_input | state.candidate.verified | Attribute for state.candidate.verified in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 123 |
| test_data_operation_reports_the_json_contract_without_echoing_input | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 125, 130, 134 |
| test_data_operation_reports_the_json_contract_without_echoing_input | message | Local binding for message in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 125, 130 |
| test_data_operation_reports_the_json_contract_without_echoing_input | owned | Local binding for owned in test_data_operation_reports_the_json_contract_without_echoing_input; use the enclosing contract and type below. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_data_contract_names_declared_inputs_and_an_example_payload | tmp_path | Parameter for tmp path in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 139 |
| test_data_contract_names_declared_inputs_and_an_example_payload | candidate | Imported dependency for candidate in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 141 |
| test_data_contract_names_declared_inputs_and_an_example_payload | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 143 |
| test_data_contract_names_declared_inputs_and_an_example_payload | sessions | Local binding for sessions in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| test_data_contract_names_declared_inputs_and_an_example_payload | owner | Local binding for owner in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_data_contract_names_declared_inputs_and_an_example_payload | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| test_data_contract_names_declared_inputs_and_an_example_payload | request | Local binding for request in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_data_contract_names_declared_inputs_and_an_example_payload | _ | Local binding for  in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 149, 157 |
| test_data_contract_names_declared_inputs_and_an_example_payload | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_data_contract_names_declared_inputs_and_an_example_payload | empty | Local binding for empty in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of data_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_data_contract_names_declared_inputs_and_an_example_payload | owned | Local binding for owned in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of data_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_data_contract_names_declared_inputs_and_an_example_payload | state.candidate | Attribute for state.candidate in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| test_data_contract_names_declared_inputs_and_an_example_payload | text | Local binding for text in test_data_contract_names_declared_inputs_and_an_example_payload; use the enclosing contract and type below. | Return type of data_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_repair_control_is_unavailable_until_owned_verification_failure | sessions | Local binding for sessions in test_repair_control_is_unavailable_until_owned_verification_failure; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_repair_control_is_unavailable_until_owned_verification_failure | owner | Local binding for owner in test_repair_control_is_unavailable_until_owned_verification_failure; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_repair_control_is_unavailable_until_owned_verification_failure | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_repair_control_is_unavailable_until_owned_verification_failure | request | Local binding for request in test_repair_control_is_unavailable_until_owned_verification_failure; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| test_unsaved_editor_changes_block_approval | tmp_path | Parameter for tmp path in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 171 |
| test_unsaved_editor_changes_block_approval | candidate | Imported dependency for candidate in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 173 |
| test_unsaved_editor_changes_block_approval | sessions | Local binding for sessions in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_unsaved_editor_changes_block_approval | owner | Local binding for owner in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_unsaved_editor_changes_block_approval | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_unsaved_editor_changes_block_approval | request | Local binding for request in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| test_unsaved_editor_changes_block_approval | _ | Local binding for  in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| test_unsaved_editor_changes_block_approval | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| test_unsaved_editor_changes_block_approval | state.candidate | Attribute for state.candidate in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| test_unsaved_editor_changes_block_approval | owner.controller.state.application_review_pending | Attribute for owner.controller.state.application review pending in test_unsaved_editor_changes_block_approval; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 181 |
| test_unsaved_editor_changes_block_approval | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_missing_registered_host_requirement_keeps_review_pending | tmp_path | Parameter for tmp path in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 188 |
| test_missing_registered_host_requirement_keeps_review_pending | sessions | Local binding for sessions in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_missing_registered_host_requirement_keeps_review_pending | owner | Local binding for owner in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| test_missing_registered_host_requirement_keeps_review_pending | request | Local binding for request in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_missing_registered_host_requirement_keeps_review_pending | approved | Local binding for approved in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 193 |
| test_missing_registered_host_requirement_keeps_review_pending.Requirements.missing | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 198 |
| test_missing_registered_host_requirement_keeps_review_pending.Requirements.missing | identifier | Parameter for identifier in test_missing_registered_host_requirement_keeps_review_pending.Requirements.missing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 198 |
| test_missing_registered_host_requirement_keeps_review_pending.Supervisor.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 208 |
| test_missing_registered_host_requirement_keeps_review_pending.Supervisor.approve | args | Parameter for args in test_missing_registered_host_requirement_keeps_review_pending.Supervisor.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 208 |
| test_missing_registered_host_requirement_keeps_review_pending | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 212 |
| test_missing_registered_host_requirement_keeps_review_pending | _ | Local binding for  in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_missing_registered_host_requirement_keeps_review_pending | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_missing_registered_host_requirement_keeps_review_pending | state.candidate | Attribute for state.candidate in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| test_missing_registered_host_requirement_keeps_review_pending | owner.controller.state.application_review_pending | Attribute for owner.controller.state.application review pending in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 222 |
| test_missing_registered_host_requirement_keeps_review_pending | rows | Local binding for rows in test_missing_registered_host_requirement_keeps_review_pending; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | sessions | Local binding for sessions in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | owner | Local binding for owner in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 235 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | request | Local binding for request in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 236 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | installed | Local binding for installed in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 237 |
| test_explicit_host_dependency_install_requires_pending_owner_consent.Requirements.install | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 242 |
| test_explicit_host_dependency_install_requires_pending_owner_consent.Requirements.install | identifier | Parameter for identifier in test_explicit_host_dependency_install_requires_pending_owner_consent.Requirements.install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 242 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | _ | Local binding for  in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | state.pending_host_requirement | Attribute for state.pending host requirement in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 249 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | state.candidate | Attribute for state.candidate in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | owner.controller.state.application_review_pending | Attribute for owner.controller.state.application review pending in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 251 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | message | Local binding for message in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of install_host_requirement; see its callable contract | Enclosing invocation or class/instance lifetime | 253 |
| test_explicit_host_dependency_install_requires_pending_owner_consent | owned | Local binding for owned in test_explicit_host_dependency_install_requires_pending_owner_consent; use the enclosing contract and type below. | Return type of install_host_requirement; see its callable contract | Enclosing invocation or class/instance lifetime | 253 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics | sessions | Local binding for sessions in test_generation_only_exposes_safe_catalog_dependency_diagnostics; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 265 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics | owner | Local binding for owner in test_generation_only_exposes_safe_catalog_dependency_diagnostics; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 266 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics | owner.controller.security | Attribute for owner.controller.security in test_generation_only_exposes_safe_catalog_dependency_diagnostics; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 267 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics.fail | root | Explicit root directory against which named paths are resolved. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 269 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics.lambda_276 | controller | Callback parameter for controller in test_generation_only_exposes_safe_catalog_dependency_diagnostics.lambda_276; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 276 |
| test_generation_only_exposes_safe_catalog_dependency_diagnostics | rows | Local binding for rows in test_generation_only_exposes_safe_catalog_dependency_diagnostics; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 278 |
| test_generation_names_an_unsupported_public_input_key | ApplicationContractError | Imported dependency for ApplicationContractError in test_generation_names_an_unsupported_public_input_key; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 289 |
| test_generation_names_an_unsupported_public_input_key | sessions | Local binding for sessions in test_generation_names_an_unsupported_public_input_key; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 291 |
| test_generation_names_an_unsupported_public_input_key | owner | Local binding for owner in test_generation_names_an_unsupported_public_input_key; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 292 |
| test_generation_names_an_unsupported_public_input_key | owner.controller.security | Attribute for owner.controller.security in test_generation_names_an_unsupported_public_input_key; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 293 |
| test_generation_names_an_unsupported_public_input_key.fail | root | Explicit root directory against which named paths are resolved. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 295 |
| test_generation_names_an_unsupported_public_input_key | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 302 |
| test_generation_names_an_unsupported_public_input_key.lambda_305 | controller | Callback parameter for controller in test_generation_names_an_unsupported_public_input_key.lambda_305; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 305 |
| test_generation_names_an_unsupported_public_input_key | rows | Local binding for rows in test_generation_names_an_unsupported_public_input_key; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | ModelProfile | Imported dependency for ModelProfile in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 319 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | sessions | Local binding for sessions in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 321 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | owner | Local binding for owner in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 322 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | client | Local binding for client in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 323 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | owner.controller.security | Attribute for owner.controller.security in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 324 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | owner.controller.model_configuration | Attribute for owner.controller.model configuration in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 325 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | received | Local binding for received in test_generation_passes_the_active_session_llm_to_the_pipeline; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 330 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.set_model_client | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 335 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.set_model_client | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 335 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.generate | args | Parameter for args in test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.generate; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.Pipeline.generate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_generation_passes_the_active_session_llm_to_the_pipeline | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 343 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.lambda_345 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 345 |
| test_generation_passes_the_active_session_llm_to_the_pipeline.lambda_346 | controller | Callback parameter for controller in test_generation_passes_the_active_session_llm_to_the_pipeline.lambda_346; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 346 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | ModelProfile | Imported dependency for ModelProfile in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 356 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | ProfileError | Imported dependency for ProfileError in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 357 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | sessions | Local binding for sessions in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 359 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | owner | Local binding for owner in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 360 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | owner.controller.security | Attribute for owner.controller.security in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 361 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | owner.controller.model_configuration | Attribute for owner.controller.model configuration in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 367 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 370 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline.lambda_371 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 371 |
| test_generation_blocks_a_changed_tofu_identity_before_the_pipeline | rows | Local binding for rows in test_generation_blocks_a_changed_tofu_identity_before_the_pipeline; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 373 |
| test_generation_names_the_missing_profile_selection | caplog | Parameter for caplog in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 380 |
| test_generation_names_the_missing_profile_selection | logging | Imported dependency for logging in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 382 |
| test_generation_names_the_missing_profile_selection | ModelProfile | Imported dependency for ModelProfile in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 384 |
| test_generation_names_the_missing_profile_selection | ProfileError | Imported dependency for ProfileError in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 385 |
| test_generation_names_the_missing_profile_selection | sessions | Local binding for sessions in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 387 |
| test_generation_names_the_missing_profile_selection | owner | Local binding for owner in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 388 |
| test_generation_names_the_missing_profile_selection | owner.controller.security | Attribute for owner.controller.security in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 389 |
| test_generation_names_the_missing_profile_selection | owner.controller.model_configuration | Attribute for owner.controller.model configuration in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 395 |
| test_generation_names_the_missing_profile_selection | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 398 |
| test_generation_names_the_missing_profile_selection.lambda_399 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 399 |
| test_generation_names_the_missing_profile_selection | rows | Local binding for rows in test_generation_names_the_missing_profile_selection; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 402 |
| test_poll_does_not_race_with_widget_publication | sessions | Local binding for sessions in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 415 |
| test_poll_does_not_race_with_widget_publication | owner | Local binding for owner in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 416 |
| test_poll_does_not_race_with_widget_publication | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 417 |
| test_poll_does_not_race_with_widget_publication | request | Local binding for request in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 418 |
| test_poll_does_not_race_with_widget_publication | _ | Local binding for  in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 419, 434 |
| test_poll_does_not_race_with_widget_publication | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 419 |
| test_poll_does_not_race_with_widget_publication | owner.controller.state.application_busy | Attribute for owner.controller.state.application busy in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 420 |
| test_poll_does_not_race_with_widget_publication | state.candidate | Attribute for state.candidate in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 426 |
| test_poll_does_not_race_with_widget_publication | message | Local binding for message in test_poll_does_not_race_with_widget_publication; use the enclosing contract and type below. | Return type of poll; see its callable contract | Enclosing invocation or class/instance lifetime | 434 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | tmp_path | Parameter for tmp path in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 439 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | generated | Imported dependency for generated in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 441 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | ApplicationReview | Imported dependency for ApplicationReview in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 443 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | sessions | Local binding for sessions in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 445 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | owner | Local binding for owner in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 446 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 447 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | request | Local binding for request in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | _ | Local binding for  in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 449 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 449 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | state.candidate | Attribute for state.candidate in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of generated; see its callable contract | Enclosing invocation or class/instance lifetime | 450 |
| test_saved_group_clears_dirty_marker_and_can_enter_new_review | panes | Local binding for panes in test_saved_group_clears_dirty_marker_and_can_enter_new_review; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 451 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock | ast | Imported dependency for ast in test_streaming_callbacks_never_suspend_while_holding_owner_lock; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 473 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock | inspect | Imported dependency for inspect in test_streaming_callbacks_never_suspend_while_holding_owner_lock; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 474 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock | module | Imported dependency for module in test_streaming_callbacks_never_suspend_while_holding_owner_lock; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 476 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock | tree | Local binding for tree in test_streaming_callbacks_never_suspend_while_holding_owner_lock; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 478 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock | node | Loop item for node in test_streaming_callbacks_never_suspend_while_holding_owner_lock; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 479 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock.comprehension_480 | item | Comprehension item for item in test_streaming_callbacks_never_suspend_while_holding_owner_lock.comprehension_480; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 481 |
| test_streaming_callbacks_never_suspend_while_holding_owner_lock.comprehension_483 | child | Comprehension item for child in test_streaming_callbacks_never_suspend_while_holding_owner_lock.comprehension_483; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 484 |
