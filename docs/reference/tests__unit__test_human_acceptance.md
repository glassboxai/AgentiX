# Reference for tests/unit/test_human_acceptance.py

Protect the human approval boundary and host-owned acceptance decisions.

Source fingerprint: 086de2a979f80686eebdc346a8dc195844a8d53003cfc473a28cb612ce0e167f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### contract

Return an independently authored declarative case, never an executable test.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### prepare

Create trusted temporary inputs with a real provisional execution.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### review

Resolve a real owner/request-bound pending review from a separate thread.

Kind: callable. Declared return: Not declared / class. Source line: 40.

### test_provisional_tests_cannot_authorize_execution

Verify provisional tests cannot authorize execution.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_human_review_and_host_comparison_control_authorization

Verify human review and host comparison control authorization.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_human_edited_expectation_is_used_instead_of_generated_value

Verify human edited expectation is used instead of generated value.

Kind: callable. Declared return: Not declared / class. Source line: 82.

### test_invalid_human_edits_do_not_grant_authorization

Verify invalid human edits do not grant authorization.

Kind: callable. Declared return: Not declared / class. Source line: 93.

### test_human_can_repair_bounded_invalid_model_case_proposal

Malformed model data must reach review without granting any authorization.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### test_human_can_repair_bounded_invalid_model_case_proposal.approve

Provide approve for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 111.

### test_oversized_invalid_proposal_never_opens_review

Verify oversized invalid proposal never opens review.

Kind: callable. Declared return: Not declared / class. Source line: 125.

### test_oversized_invalid_proposal_never_opens_review.unexpected

Provide unexpected for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 129.

### test_review_cannot_authorize_changed_or_closed_work

Verify review cannot authorize changed or closed work.

Kind: callable. Declared return: Not declared / class. Source line: 141.

### test_review_cannot_authorize_changed_or_closed_work.mutate

Provide mutate for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### test_only_functions_covered_by_approved_cases_can_execute

Verify only functions covered by approved cases can execute.

Kind: callable. Declared return: Not declared / class. Source line: 163.

### test_invalid_contracts_are_rejected_before_review

Verify invalid contracts are rejected before review.

Kind: callable. Declared return: Not declared / class. Source line: 183.

### test_host_comparison_uses_typed_data

Verify host comparison uses typed data.

Kind: callable. Declared return: Not declared / class. Source line: 200.

### test_transport_serialization_error_is_not_a_function_exception

Verify transport serialization error is not a function exception.

Kind: callable. Declared return: Not declared / class. Source line: 210.

### test_expected_values_are_not_sent_to_the_isolated_process

Verify expected values are not sent to the isolated process.

Kind: callable. Declared return: Not declared / class. Source line: 225.

### test_expected_values_are_not_sent_to_the_isolated_process.observe

Provide observe for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 232.

### test_revocation_between_execution_checks_prevents_the_call

Verify revocation between execution checks prevents the call.

Kind: callable. Declared return: Not declared / class. Source line: 245.

### test_revocation_between_execution_checks_prevents_the_call.revoke_after_read

Provide revoke after read for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 256.

### test_forged_unittest_success_cannot_override_a_wrong_acceptance_result

Verify forged unittest success cannot override a wrong acceptance result.

Kind: callable. Declared return: Not declared / class. Source line: 268.

### test_human_rejection_cannot_be_automatically_reprompted_in_same_operation

Verify human rejection cannot be automatically reprompted in same operation.

Kind: callable. Declared return: Not declared / class. Source line: 288.

### test_human_rejection_cannot_be_automatically_reprompted_in_same_operation.no_second_prompt

Provide no second prompt for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 299.

### test_observed_source_change_cannot_revive_old_approval_after_restore

Verify observed source change cannot revive old approval after restore.

Kind: callable. Declared return: Not declared / class. Source line: 310.

### test_invalid_case_data_never_reaches_review

Verify invalid case data never reaches review.

Kind: callable. Declared return: Not declared / class. Source line: 337.

### test_approval_expires_and_cannot_authorize_later

Verify approval expires and cannot authorize later.

Kind: callable. Declared return: Not declared / class. Source line: 361.

### test_case_payloads_are_not_logged

Verify case payloads are not logged.

Kind: callable. Declared return: Not declared / class. Source line: 372.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| contract | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| contract | function | Parameter for function in contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| prepare | system | Parameter for system in prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| prepare | system.security.auto_approve | Attribute for system.security.auto approve in prepare; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 30 |
| prepare | system.security.approval_timeout | Attribute for system.security.approval timeout in prepare; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 31 |
| prepare | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| review | system | Parameter for system in review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| review | decision | Parameter for decision in review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| review | edited | Parameter for edited in review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| review | before | Parameter for before in review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| review | deadline | Local binding for deadline in review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| review | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_provisional_tests_cannot_authorize_execution | system | Parameter for system in test_provisional_tests_cannot_authorize_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| test_human_review_and_host_comparison_control_authorization | system | Parameter for system in test_human_review_and_host_comparison_control_authorization; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_human_review_and_host_comparison_control_authorization | decision | Parameter for decision in test_human_review_and_host_comparison_control_authorization; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_human_review_and_host_comparison_control_authorization | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_human_review_and_host_comparison_control_authorization | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_human_review_and_host_comparison_control_authorization | worker | Local binding for worker in test_human_review_and_host_comparison_control_authorization; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_human_review_and_host_comparison_control_authorization | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_human_edited_expectation_is_used_instead_of_generated_value | system | Parameter for system in test_human_edited_expectation_is_used_instead_of_generated_value; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_human_edited_expectation_is_used_instead_of_generated_value | worker | Local binding for worker in test_human_edited_expectation_is_used_instead_of_generated_value; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_human_edited_expectation_is_used_instead_of_generated_value | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_invalid_human_edits_do_not_grant_authorization | system | Parameter for system in test_invalid_human_edits_do_not_grant_authorization; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_invalid_human_edits_do_not_grant_authorization | edited | Parameter for edited in test_invalid_human_edits_do_not_grant_authorization; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_invalid_human_edits_do_not_grant_authorization | worker | Local binding for worker in test_invalid_human_edits_do_not_grant_authorization; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_human_can_repair_bounded_invalid_model_case_proposal | system | Parameter for system in test_human_can_repair_bounded_invalid_model_case_proposal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_human_can_repair_bounded_invalid_model_case_proposal | monkeypatch | Parameter for monkeypatch in test_human_can_repair_bounded_invalid_model_case_proposal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_human_can_repair_bounded_invalid_model_case_proposal | proposed | Parameter for proposed in test_human_can_repair_bounded_invalid_model_case_proposal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_human_can_repair_bounded_invalid_model_case_proposal | observed | Returned observation checked against the reviewed host-side expectation. | list | Enclosing invocation or class/instance lifetime | 109 |
| test_human_can_repair_bounded_invalid_model_case_proposal.approve | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_human_can_repair_bounded_invalid_model_case_proposal.approve | action | Parameter for action in test_human_can_repair_bounded_invalid_model_case_proposal.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_human_can_repair_bounded_invalid_model_case_proposal.approve | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_human_can_repair_bounded_invalid_model_case_proposal.approve | require_manual | Parameter for require manual in test_human_can_repair_bounded_invalid_model_case_proposal.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_human_can_repair_bounded_invalid_model_case_proposal.approve | review_context | Parameter for review context in test_human_can_repair_bounded_invalid_model_case_proposal.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_human_can_repair_bounded_invalid_model_case_proposal | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_oversized_invalid_proposal_never_opens_review | system | Parameter for system in test_oversized_invalid_proposal_never_opens_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| test_oversized_invalid_proposal_never_opens_review | monkeypatch | Parameter for monkeypatch in test_oversized_invalid_proposal_never_opens_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| test_oversized_invalid_proposal_never_opens_review.unexpected | args | Parameter for args in test_oversized_invalid_proposal_never_opens_review.unexpected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_oversized_invalid_proposal_never_opens_review.unexpected | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_review_cannot_authorize_changed_or_closed_work | system | Parameter for system in test_review_cannot_authorize_changed_or_closed_work; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 141 |
| test_review_cannot_authorize_changed_or_closed_work | change | Parameter for change in test_review_cannot_authorize_changed_or_closed_work; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 141 |
| test_review_cannot_authorize_changed_or_closed_work.mutate | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_review_cannot_authorize_changed_or_closed_work.mutate | system.security.operation_id | Attribute for system.security.operation id in test_review_cannot_authorize_changed_or_closed_work.mutate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 150 |
| test_review_cannot_authorize_changed_or_closed_work | worker | Local binding for worker in test_review_cannot_authorize_changed_or_closed_work; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_only_functions_covered_by_approved_cases_can_execute | system | Parameter for system in test_only_functions_covered_by_approved_cases_can_execute; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 163 |
| test_only_functions_covered_by_approved_cases_can_execute | worker | Local binding for worker in test_only_functions_covered_by_approved_cases_can_execute; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_invalid_contracts_are_rejected_before_review | text | Parameter for text in test_invalid_contracts_are_rejected_before_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_invalid_contracts_are_rejected_before_review | parse_contract | Imported dependency for parse contract in test_invalid_contracts_are_rejected_before_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 185 |
| test_host_comparison_uses_typed_data | actual | Parameter for actual in test_host_comparison_uses_typed_data; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_host_comparison_uses_typed_data | expect | Parameter for expect in test_host_comparison_uses_typed_data; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_host_comparison_uses_typed_data | matched | Parameter for matched in test_host_comparison_uses_typed_data; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_host_comparison_uses_typed_data | matches_expectation | Imported dependency for matches expectation in test_host_comparison_uses_typed_data; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| test_transport_serialization_error_is_not_a_function_exception | system | Parameter for system in test_transport_serialization_error_is_not_a_function_exception; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 210 |
| test_transport_serialization_error_is_not_a_function_exception | proposal | Local binding for proposal in test_transport_serialization_error_is_not_a_function_exception; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_transport_serialization_error_is_not_a_function_exception | worker | Local binding for worker in test_transport_serialization_error_is_not_a_function_exception; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_transport_serialization_error_is_not_a_function_exception | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_expected_values_are_not_sent_to_the_isolated_process | system | Parameter for system in test_expected_values_are_not_sent_to_the_isolated_process; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 225 |
| test_expected_values_are_not_sent_to_the_isolated_process | monkeypatch | Parameter for monkeypatch in test_expected_values_are_not_sent_to_the_isolated_process; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 225 |
| test_expected_values_are_not_sent_to_the_isolated_process | seen | Local binding for seen in test_expected_values_are_not_sent_to_the_isolated_process; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 228 |
| test_expected_values_are_not_sent_to_the_isolated_process | backend | Injected framework/execution provider; callers determine the required protocol. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 229 |
| test_expected_values_are_not_sent_to_the_isolated_process | real | Local binding for real in test_expected_values_are_not_sent_to_the_isolated_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 230 |
| test_expected_values_are_not_sent_to_the_isolated_process.observe | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
| test_expected_values_are_not_sent_to_the_isolated_process.observe | tool | Parameter for tool in test_expected_values_are_not_sent_to_the_isolated_process.observe; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
| test_expected_values_are_not_sent_to_the_isolated_process.observe | function | Parameter for function in test_expected_values_are_not_sent_to_the_isolated_process.observe; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
| test_expected_values_are_not_sent_to_the_isolated_process.observe | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
| test_expected_values_are_not_sent_to_the_isolated_process | worker | Local binding for worker in test_expected_values_are_not_sent_to_the_isolated_process; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| test_revocation_between_execution_checks_prevents_the_call | system | Parameter for system in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 245 |
| test_revocation_between_execution_checks_prevents_the_call | monkeypatch | Parameter for monkeypatch in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 245 |
| test_revocation_between_execution_checks_prevents_the_call | worker | Local binding for worker in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_revocation_between_execution_checks_prevents_the_call | ledger | Local binding for ledger in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 252 |
| test_revocation_between_execution_checks_prevents_the_call | snapshot | Local binding for snapshot in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 253 |
| test_revocation_between_execution_checks_prevents_the_call | calls | Local binding for calls in test_revocation_between_execution_checks_prevents_the_call; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 254 |
| test_revocation_between_execution_checks_prevents_the_call.revoke_after_read | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 256 |
| test_revocation_between_execution_checks_prevents_the_call.revoke_after_read | data | Local binding for data in test_revocation_between_execution_checks_prevents_the_call.revoke_after_read; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| test_forged_unittest_success_cannot_override_a_wrong_acceptance_result | system | Parameter for system in test_forged_unittest_success_cannot_override_a_wrong_acceptance_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 268 |
| test_forged_unittest_success_cannot_override_a_wrong_acceptance_result | forged | Local binding for forged in test_forged_unittest_success_cannot_override_a_wrong_acceptance_result; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 272 |
| test_forged_unittest_success_cannot_override_a_wrong_acceptance_result | worker | Local binding for worker in test_forged_unittest_success_cannot_override_a_wrong_acceptance_result; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 279 |
| test_human_rejection_cannot_be_automatically_reprompted_in_same_operation | system | Parameter for system in test_human_rejection_cannot_be_automatically_reprompted_in_same_operation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 288 |
| test_human_rejection_cannot_be_automatically_reprompted_in_same_operation | monkeypatch | Parameter for monkeypatch in test_human_rejection_cannot_be_automatically_reprompted_in_same_operation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 288 |
| test_human_rejection_cannot_be_automatically_reprompted_in_same_operation | worker | Local binding for worker in test_human_rejection_cannot_be_automatically_reprompted_in_same_operation; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 291 |
| test_human_rejection_cannot_be_automatically_reprompted_in_same_operation.no_second_prompt | args | Parameter for args in test_human_rejection_cannot_be_automatically_reprompted_in_same_operation.no_second_prompt; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 299 |
| test_human_rejection_cannot_be_automatically_reprompted_in_same_operation.no_second_prompt | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 299 |
| test_observed_source_change_cannot_revive_old_approval_after_restore | system | Parameter for system in test_observed_source_change_cannot_revive_old_approval_after_restore; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 310 |
| test_observed_source_change_cannot_revive_old_approval_after_restore | worker | Local binding for worker in test_observed_source_change_cannot_revive_old_approval_after_restore; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 313 |
| test_observed_source_change_cannot_revive_old_approval_after_restore | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 317 |
| test_observed_source_change_cannot_revive_old_approval_after_restore | original | Local binding for original in test_observed_source_change_cannot_revive_old_approval_after_restore; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 318 |
| test_invalid_case_data_never_reaches_review | mutate | Parameter for mutate in test_invalid_case_data_never_reaches_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 337 |
| test_invalid_case_data_never_reaches_review | parse_contract | Imported dependency for parse contract in test_invalid_case_data_never_reaches_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 339 |
| test_invalid_case_data_never_reaches_review | data | Local binding for data in test_invalid_case_data_never_reaches_review; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 341 |
| test_invalid_case_data_never_reaches_review | case | Local binding for case in test_invalid_case_data_never_reaches_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 342 |
| test_invalid_case_data_never_reaches_review.comprehension_356 | i | Comprehension item for i in test_invalid_case_data_never_reaches_review.comprehension_356; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 356 |
| test_approval_expires_and_cannot_authorize_later | system | Parameter for system in test_approval_expires_and_cannot_authorize_later; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 361 |
| test_approval_expires_and_cannot_authorize_later | system.security.approval_timeout | Attribute for system.security.approval timeout in test_approval_expires_and_cannot_authorize_later; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 364 |
| test_case_payloads_are_not_logged | system | Parameter for system in test_case_payloads_are_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 372 |
| test_case_payloads_are_not_logged | caplog | Parameter for caplog in test_case_payloads_are_not_logged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 372 |
| test_case_payloads_are_not_logged | data | Local binding for data in test_case_payloads_are_not_logged; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 375 |
| test_case_payloads_are_not_logged | worker | Local binding for worker in test_case_payloads_are_not_logged; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 378 |
