# Reference for tests/unit/test_pipeline_verification.py

Reject fabricated manager claims and stale/foreign test evidence.

Source fingerprint: cc7bceb5b412aed52d1ff6042e2b5fec2b6511e98b88e95452d683edb47a0416

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### artifacts

Persist independently authored inputs without executing their source.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### report

Build a literal successful protocol fixture at the OS boundary.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_invalid_observed_results_never_authorize_execution

Verify invalid observed results never authorize execution.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_evidence_requires_isolation_success_and_unchanged_artifacts

Verify evidence requires isolation success and unchanged artifacts.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_evidence_is_operation_bound_and_new_attempt_invalidates_it

Verify evidence is operation bound and new attempt invalidates it.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### test_creation_claim_without_service_evidence_blocks_final_manager

Verify creation claim without service evidence blocks final manager.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_creation_claim_without_service_evidence_blocks_final_manager.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 67.

### test_unverified_source_is_not_imported

Verify unverified source is not imported.

Kind: callable. Declared return: Not declared / class. Source line: 83.

### test_previous_query_evidence_cannot_authorize_a_new_query

Verify previous query evidence cannot authorize a new query.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_missing_successful_field_is_rejected

Verify missing successful field is rejected.

Kind: callable. Declared return: Not declared / class. Source line: 105.

### test_nonpassing_only_suites_do_not_grant_evidence

Verify nonpassing only suites do not grant evidence.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### test_owner_change_invalidates_evidence

Verify owner change invalidates evidence.

Kind: callable. Declared return: Not declared / class. Source line: 130.

### test_inflight_test_result_cannot_be_relabelled_as_a_new_operation

Verify inflight test result cannot be relabelled as a new operation.

Kind: callable. Declared return: Not declared / class. Source line: 140.

### test_inflight_test_result_cannot_be_relabelled_as_a_new_operation.switched

Provide switched for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### test_test_service_failure_revokes_previous_success

Verify test service failure revokes previous success.

Kind: callable. Declared return: Not declared / class. Source line: 155.

### test_test_service_failure_revokes_previous_success.unavailable

Provide unavailable for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 163.

### test_code_change_during_testing_cannot_publish_evidence

Verify code change during testing cannot publish evidence.

Kind: callable. Declared return: Not declared / class. Source line: 172.

### test_code_change_during_testing_cannot_publish_evidence.changed

Provide changed for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 177.

### test_invalid_current_source_never_gains_evidence_from_unrelated_tests

Verify invalid current source never gains evidence from unrelated tests.

Kind: callable. Declared return: Not declared / class. Source line: 187.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| artifacts | system | Parameter for system in artifacts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| artifacts | system.security.auto_approve | Attribute for system.security.auto approve in artifacts; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 10 |
| report | changes | Parameter for changes in report; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| report | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_invalid_observed_results_never_authorize_execution | system | Parameter for system in test_invalid_observed_results_never_authorize_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_invalid_observed_results_never_authorize_execution | changes | Parameter for changes in test_invalid_observed_results_never_authorize_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_invalid_observed_results_never_authorize_execution | ledger | Local binding for ledger in test_invalid_observed_results_never_authorize_execution; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_invalid_observed_results_never_authorize_execution | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_invalid_observed_results_never_authorize_execution | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_evidence_requires_isolation_success_and_unchanged_artifacts | system | Parameter for system in test_evidence_requires_isolation_success_and_unchanged_artifacts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_evidence_requires_isolation_success_and_unchanged_artifacts | ledger | Local binding for ledger in test_evidence_requires_isolation_success_and_unchanged_artifacts; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_evidence_requires_isolation_success_and_unchanged_artifacts | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_evidence_requires_isolation_success_and_unchanged_artifacts | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_evidence_is_operation_bound_and_new_attempt_invalidates_it | system | Parameter for system in test_evidence_is_operation_bound_and_new_attempt_invalidates_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_evidence_is_operation_bound_and_new_attempt_invalidates_it | ledger | Local binding for ledger in test_evidence_is_operation_bound_and_new_attempt_invalidates_it; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_evidence_is_operation_bound_and_new_attempt_invalidates_it | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_evidence_is_operation_bound_and_new_attempt_invalidates_it | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_evidence_is_operation_bound_and_new_attempt_invalidates_it | system.security.operation_id | Attribute for system.security.operation id in test_evidence_is_operation_bound_and_new_attempt_invalidates_it; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| test_creation_claim_without_service_evidence_blocks_final_manager | system | Parameter for system in test_creation_claim_without_service_evidence_blocks_final_manager; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_creation_claim_without_service_evidence_blocks_final_manager | monkeypatch | Parameter for monkeypatch in test_creation_claim_without_service_evidence_blocks_final_manager; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_creation_claim_without_service_evidence_blocks_final_manager | calls | Local binding for calls in test_creation_claim_without_service_evidence_blocks_final_manager; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 65 |
| test_creation_claim_without_service_evidence_blocks_final_manager.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| test_unverified_source_is_not_imported | system | Parameter for system in test_unverified_source_is_not_imported; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 83 |
| test_unverified_source_is_not_imported | tmp_path | Parameter for tmp path in test_unverified_source_is_not_imported; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 83 |
| test_unverified_source_is_not_imported | canary | Local binding for canary in test_unverified_source_is_not_imported; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_previous_query_evidence_cannot_authorize_a_new_query | system | Parameter for system in test_previous_query_evidence_cannot_authorize_a_new_query; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_previous_query_evidence_cannot_authorize_a_new_query | monkeypatch | Parameter for monkeypatch in test_previous_query_evidence_cannot_authorize_a_new_query; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_previous_query_evidence_cannot_authorize_a_new_query | ledger | Local binding for ledger in test_previous_query_evidence_cannot_authorize_a_new_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_previous_query_evidence_cannot_authorize_a_new_query | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_previous_query_evidence_cannot_authorize_a_new_query | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_missing_successful_field_is_rejected | system | Parameter for system in test_missing_successful_field_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_missing_successful_field_is_rejected | ledger | Local binding for ledger in test_missing_successful_field_is_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_missing_successful_field_is_rejected | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| test_missing_successful_field_is_rejected | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| test_missing_successful_field_is_rejected | incomplete | Local binding for incomplete in test_missing_successful_field_is_rejected; use the enclosing contract and type below. | Return type of report; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_nonpassing_only_suites_do_not_grant_evidence | system | Parameter for system in test_nonpassing_only_suites_do_not_grant_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_nonpassing_only_suites_do_not_grant_evidence | source | Explicit source document or source-code text; never imported for reference generation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_owner_change_invalidates_evidence | system | Parameter for system in test_owner_change_invalidates_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| test_owner_change_invalidates_evidence | ledger | Local binding for ledger in test_owner_change_invalidates_evidence; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_owner_change_invalidates_evidence | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_owner_change_invalidates_evidence | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_owner_change_invalidates_evidence | system.security.owner_id | Attribute for system.security.owner id in test_owner_change_invalidates_evidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 136 |
| test_inflight_test_result_cannot_be_relabelled_as_a_new_operation | system | Parameter for system in test_inflight_test_result_cannot_be_relabelled_as_a_new_operation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_inflight_test_result_cannot_be_relabelled_as_a_new_operation | monkeypatch | Parameter for monkeypatch in test_inflight_test_result_cannot_be_relabelled_as_a_new_operation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_inflight_test_result_cannot_be_relabelled_as_a_new_operation | SandboxResult | Imported dependency for SandboxResult in test_inflight_test_result_cannot_be_relabelled_as_a_new_operation; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 143 |
| test_inflight_test_result_cannot_be_relabelled_as_a_new_operation.switched | args | Parameter for args in test_inflight_test_result_cannot_be_relabelled_as_a_new_operation.switched; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_inflight_test_result_cannot_be_relabelled_as_a_new_operation.switched | system.security.operation_id | Attribute for system.security.operation id in test_inflight_test_result_cannot_be_relabelled_as_a_new_operation.switched; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 147 |
| test_test_service_failure_revokes_previous_success | system | Parameter for system in test_test_service_failure_revokes_previous_success; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 155 |
| test_test_service_failure_revokes_previous_success | monkeypatch | Parameter for monkeypatch in test_test_service_failure_revokes_previous_success; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 155 |
| test_test_service_failure_revokes_previous_success | ledger | Local binding for ledger in test_test_service_failure_revokes_previous_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_test_service_failure_revokes_previous_success | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 159 |
| test_test_service_failure_revokes_previous_success | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 159 |
| test_test_service_failure_revokes_previous_success | IsolationUnavailable | Imported dependency for IsolationUnavailable in test_test_service_failure_revokes_previous_success; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 161 |
| test_test_service_failure_revokes_previous_success.unavailable | args | Parameter for args in test_test_service_failure_revokes_previous_success.unavailable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 163 |
| test_code_change_during_testing_cannot_publish_evidence | system | Parameter for system in test_code_change_during_testing_cannot_publish_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| test_code_change_during_testing_cannot_publish_evidence | monkeypatch | Parameter for monkeypatch in test_code_change_during_testing_cannot_publish_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| test_code_change_during_testing_cannot_publish_evidence | SandboxResult | Imported dependency for SandboxResult in test_code_change_during_testing_cannot_publish_evidence; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 175 |
| test_code_change_during_testing_cannot_publish_evidence.changed | args | Parameter for args in test_code_change_during_testing_cannot_publish_evidence.changed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 177 |
| test_invalid_current_source_never_gains_evidence_from_unrelated_tests | system | Parameter for system in test_invalid_current_source_never_gains_evidence_from_unrelated_tests; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 187 |
| test_invalid_current_source_never_gains_evidence_from_unrelated_tests | unrelated | Local binding for unrelated in test_invalid_current_source_never_gains_evidence_from_unrelated_tests; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 191 |
