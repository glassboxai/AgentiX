# Reference for tests/unit/test_creation_stage_gates.py

LIVE-FLOW-002: advance only on fresh approved artifacts, never model prose.

Source fingerprint: d5faecfb7834f30af6a34444cb037b18644e1e366cd2771337d3e053e3650c23

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### install_backend

Replace only model execution; use real storage/approval/receipt boundaries.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### install_backend.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### install_backend.crew.kickoff

Provide kickoff for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### save

Provide save for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_missing_specification_stops_before_coder

Verify missing specification stops before coder.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_missing_code_stops_before_tester

Verify missing code stops before tester.

Kind: callable. Declared return: Not declared / class. Source line: 43.

### test_contract_rejection_is_reported_without_starting_tester

Expose the host contract rejection instead of masking it as a missing receipt.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_creation_prompts_require_the_public_function_docstring

The contract rejects a missing function docstring, so both roles must demand it.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_existing_or_unapproved_artifact_cannot_complete_stage

Verify existing or unapproved artifact cannot complete stage.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_stage_context_uses_saved_edits_instead_of_model_claim

Verify stage context uses saved edits instead of model claim.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_changed_saved_bytes_cannot_complete_stage

Verify changed saved bytes cannot complete stage.

Kind: callable. Declared return: Not declared / class. Source line: 132.

### test_changed_saved_bytes_cannot_complete_stage.tamper

Provide tamper for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 135.

### test_receipt_cannot_adopt_an_intervening_unapproved_write

A concurrent replacement between save and observation must fail closed.

Kind: callable. Declared return: Not declared / class. Source line: 149.

### test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open

Provide intervening open for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 157.

### test_current_owner_operation_and_fresh_save_are_required

Verify current owner operation and fresh save are required.

Kind: callable. Declared return: Not declared / class. Source line: 172.

### test_gated_pipeline_completes_with_real_acceptance_services

Verify gated pipeline completes with real acceptance services.

Kind: callable. Declared return: Not declared / class. Source line: 189.

### test_gated_pipeline_completes_with_real_acceptance_services.tester

Provide tester for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 195.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| install_backend | system | Parameter for system in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install_backend | monkeypatch | Parameter for monkeypatch in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install_backend | actions | Parameter for actions in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install_backend | seen | Local binding for seen in install_backend; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 11 |
| install_backend | system.security.auto_approve | Attribute for system.security.auto approve in install_backend; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 12 |
| install_backend.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| install_backend.crew.kickoff | task | Local binding for task in install_backend.crew.kickoff; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 19 |
| install_backend.crew.kickoff | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| save | system | Parameter for system in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| save | suffix | Parameter for suffix in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| save | text | Parameter for text in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_missing_specification_stops_before_coder | system | Parameter for system in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_missing_specification_stops_before_coder | monkeypatch | Parameter for monkeypatch in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_missing_specification_stops_before_coder | seen | Local binding for seen in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_missing_specification_stops_before_coder.lambda_37 | task | Callback parameter for task in test_missing_specification_stops_before_coder.lambda_37; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 37 |
| test_missing_specification_stops_before_coder | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_missing_code_stops_before_tester | system | Parameter for system in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| test_missing_code_stops_before_tester | monkeypatch | Parameter for monkeypatch in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| test_missing_code_stops_before_tester | seen | Local binding for seen in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_missing_code_stops_before_tester.lambda_48 | task | Callback parameter for task in test_missing_code_stops_before_tester.lambda_48; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 48 |
| test_missing_code_stops_before_tester | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_contract_rejection_is_reported_without_starting_tester | system | Parameter for system in test_contract_rejection_is_reported_without_starting_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_contract_rejection_is_reported_without_starting_tester | monkeypatch | Parameter for monkeypatch in test_contract_rejection_is_reported_without_starting_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_contract_rejection_is_reported_without_starting_tester | system.security.strict_tool_contract | Attribute for system.security.strict tool contract in test_contract_rejection_is_reported_without_starting_tester; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 57 |
| test_contract_rejection_is_reported_without_starting_tester | seen | Local binding for seen in test_contract_rejection_is_reported_without_starting_tester; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_contract_rejection_is_reported_without_starting_tester.lambda_62 | task | Callback parameter for task in test_contract_rejection_is_reported_without_starting_tester.lambda_62; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 62 |
| test_contract_rejection_is_reported_without_starting_tester.lambda_63 | task | Callback parameter for task in test_contract_rejection_is_reported_without_starting_tester.lambda_63; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 63 |
| test_contract_rejection_is_reported_without_starting_tester | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_creation_prompts_require_the_public_function_docstring | system | Parameter for system in test_creation_prompts_require_the_public_function_docstring; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_creation_prompts_require_the_public_function_docstring | monkeypatch | Parameter for monkeypatch in test_creation_prompts_require_the_public_function_docstring; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_creation_prompts_require_the_public_function_docstring | seen | Local binding for seen in test_creation_prompts_require_the_public_function_docstring; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_creation_prompts_require_the_public_function_docstring.lambda_82 | task | Callback parameter for task in test_creation_prompts_require_the_public_function_docstring.lambda_82; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 82 |
| test_creation_prompts_require_the_public_function_docstring.lambda_83 | task | Callback parameter for task in test_creation_prompts_require_the_public_function_docstring.lambda_83; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 83 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | system | Parameter for system in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | monkeypatch | Parameter for monkeypatch in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | untrusted_file | Parameter for untrusted file in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | folder | Local binding for folder in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | system.security.auto_approve | Attribute for system.security.auto approve in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 103 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | seen | Local binding for seen in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_existing_or_unapproved_artifact_cannot_complete_stage.lambda_105 | task | Callback parameter for task in test_existing_or_unapproved_artifact_cannot_complete_stage.lambda_105; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 105 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | system | Parameter for system in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | monkeypatch | Parameter for monkeypatch in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | original | Local binding for original in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 114 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | seen | Local binding for seen in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_119 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_119; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 119 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_120 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_120; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 120 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_121 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_121; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 121 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.comprehension_126 | description | Comprehension item for description in test_stage_context_uses_saved_edits_instead_of_model_claim.comprehension_126; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 126 |
| test_changed_saved_bytes_cannot_complete_stage | system | Parameter for system in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 132 |
| test_changed_saved_bytes_cannot_complete_stage | monkeypatch | Parameter for monkeypatch in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 132 |
| test_changed_saved_bytes_cannot_complete_stage.tamper | task | Parameter for task in test_changed_saved_bytes_cannot_complete_stage.tamper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_changed_saved_bytes_cannot_complete_stage | seen | Local binding for seen in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | system | Parameter for system in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 149 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | monkeypatch | Parameter for monkeypatch in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 149 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | builtins | Imported dependency for builtins in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 151 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | system.security.auto_approve | Attribute for system.security.auto approve in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 153 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | actual_open | Local binding for actual open in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | replaced | Local binding for replaced in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 155 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | mode | Parameter for mode in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | args | Parameter for args in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 157 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | output | Managed resource for output in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Return type of actual_open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 161 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| test_current_owner_operation_and_fresh_save_are_required | system | Parameter for system in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| test_current_owner_operation_and_fresh_save_are_required | system.security.auto_approve | Attribute for system.security.auto approve in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 174 |
| test_current_owner_operation_and_fresh_save_are_required | system.security.operation_id | Attribute for system.security.operation id in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 175, 179 |
| test_current_owner_operation_and_fresh_save_are_required | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_current_owner_operation_and_fresh_save_are_required | first | Local binding for first in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| test_current_owner_operation_and_fresh_save_are_required | second | Local binding for second in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_gated_pipeline_completes_with_real_acceptance_services | system | Parameter for system in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 189 |
| test_gated_pipeline_completes_with_real_acceptance_services | monkeypatch | Parameter for monkeypatch in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 189 |
| test_gated_pipeline_completes_with_real_acceptance_services | replace_code | Parameter for replace code in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 189 |
| test_gated_pipeline_completes_with_real_acceptance_services | json | Imported dependency for json in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 191 |
| test_gated_pipeline_completes_with_real_acceptance_services | approve_next_review | Imported dependency for approve next review in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 193 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | task | Parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 195 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 201, 207 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | thread | Local binding for thread in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | errors | Local binding for errors in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_gated_pipeline_completes_with_real_acceptance_services | seen | Local binding for seen in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_gated_pipeline_completes_with_real_acceptance_services.lambda_231 | task | Callback parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.lambda_231; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 231 |
| test_gated_pipeline_completes_with_real_acceptance_services.lambda_232 | task | Callback parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.lambda_232; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 232 |
| test_gated_pipeline_completes_with_real_acceptance_services | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 236 |
