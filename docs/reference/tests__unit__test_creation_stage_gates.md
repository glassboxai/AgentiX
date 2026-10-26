# Reference for tests/unit/test_creation_stage_gates.py

LIVE-FLOW-002: advance only on fresh approved artifacts, never model prose.

Source fingerprint: eaae3818b52ac071b469e77f51483c407f00c6fc3dc88a325dcae922816fa46a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### install_backend

Replace only model execution; use real storage/approval/receipt boundaries.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### install_backend.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 13.

### install_backend.crew.kickoff

Provide kickoff for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### save

Provide save for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_missing_specification_stops_before_coder

Verify missing specification stops before coder.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_missing_code_stops_before_tester

Verify missing code stops before tester.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_existing_or_unapproved_artifact_cannot_complete_stage

Verify existing or unapproved artifact cannot complete stage.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_stage_context_uses_saved_edits_instead_of_model_claim

Verify stage context uses saved edits instead of model claim.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_changed_saved_bytes_cannot_complete_stage

Verify changed saved bytes cannot complete stage.

Kind: callable. Declared return: Not declared / class. Source line: 91.

### test_changed_saved_bytes_cannot_complete_stage.tamper

Provide tamper for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_receipt_cannot_adopt_an_intervening_unapproved_write

A concurrent replacement between save and observation must fail closed.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open

Provide intervening open for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 114.

### test_current_owner_operation_and_fresh_save_are_required

Verify current owner operation and fresh save are required.

Kind: callable. Declared return: Not declared / class. Source line: 129.

### test_gated_pipeline_completes_with_real_acceptance_services

Verify gated pipeline completes with real acceptance services.

Kind: callable. Declared return: Not declared / class. Source line: 146.

### test_gated_pipeline_completes_with_real_acceptance_services.tester

Provide tester for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 152.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| install_backend | system | Parameter for system in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| install_backend | monkeypatch | Parameter for monkeypatch in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| install_backend | actions | Parameter for actions in install_backend; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| install_backend | seen | Local binding for seen in install_backend; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 10 |
| install_backend | system.security.auto_approve | Attribute for system.security.auto approve in install_backend; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 11 |
| install_backend.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 13 |
| install_backend.crew.kickoff | task | Local binding for task in install_backend.crew.kickoff; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| save | system | Parameter for system in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| save | suffix | Parameter for suffix in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| save | text | Parameter for text in save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_missing_specification_stops_before_coder | system | Parameter for system in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_missing_specification_stops_before_coder | monkeypatch | Parameter for monkeypatch in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_missing_specification_stops_before_coder | seen | Local binding for seen in test_missing_specification_stops_before_coder; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_missing_specification_stops_before_coder.lambda_36 | task | Callback parameter for task in test_missing_specification_stops_before_coder.lambda_36; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 36 |
| test_missing_specification_stops_before_coder | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_missing_code_stops_before_tester | system | Parameter for system in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_missing_code_stops_before_tester | monkeypatch | Parameter for monkeypatch in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_missing_code_stops_before_tester | seen | Local binding for seen in test_missing_code_stops_before_tester; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_missing_code_stops_before_tester.lambda_47 | task | Callback parameter for task in test_missing_code_stops_before_tester.lambda_47; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 47 |
| test_missing_code_stops_before_tester | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | system | Parameter for system in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | monkeypatch | Parameter for monkeypatch in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | untrusted_file | Parameter for untrusted file in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | folder | Local binding for folder in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | system.security.auto_approve | Attribute for system.security.auto approve in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 62 |
| test_existing_or_unapproved_artifact_cannot_complete_stage | seen | Local binding for seen in test_existing_or_unapproved_artifact_cannot_complete_stage; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_existing_or_unapproved_artifact_cannot_complete_stage.lambda_64 | task | Callback parameter for task in test_existing_or_unapproved_artifact_cannot_complete_stage.lambda_64; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | system | Parameter for system in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | monkeypatch | Parameter for monkeypatch in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | original | Local binding for original in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 73 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | seen | Local binding for seen in test_stage_context_uses_saved_edits_instead_of_model_claim; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_78 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_78; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 78 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_79 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_79; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 79 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_80 | task | Callback parameter for task in test_stage_context_uses_saved_edits_instead_of_model_claim.lambda_80; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 80 |
| test_stage_context_uses_saved_edits_instead_of_model_claim | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_stage_context_uses_saved_edits_instead_of_model_claim.comprehension_85 | description | Comprehension item for description in test_stage_context_uses_saved_edits_instead_of_model_claim.comprehension_85; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 85 |
| test_changed_saved_bytes_cannot_complete_stage | system | Parameter for system in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_changed_saved_bytes_cannot_complete_stage | monkeypatch | Parameter for monkeypatch in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_changed_saved_bytes_cannot_complete_stage.tamper | task | Parameter for task in test_changed_saved_bytes_cannot_complete_stage.tamper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_changed_saved_bytes_cannot_complete_stage | seen | Local binding for seen in test_changed_saved_bytes_cannot_complete_stage; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | system | Parameter for system in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | monkeypatch | Parameter for monkeypatch in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | builtins | Imported dependency for builtins in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 108 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | system.security.auto_approve | Attribute for system.security.auto approve in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 110 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | actual_open | Local binding for actual open in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | replaced | Local binding for replaced in test_receipt_cannot_adopt_an_intervening_unapproved_write; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 112 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | mode | Parameter for mode in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | args | Parameter for args in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open | output | Managed resource for output in test_receipt_cannot_adopt_an_intervening_unapproved_write.intervening_open; use the enclosing contract and type below. | Return type of actual_open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 118 |
| test_receipt_cannot_adopt_an_intervening_unapproved_write | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_current_owner_operation_and_fresh_save_are_required | system | Parameter for system in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_current_owner_operation_and_fresh_save_are_required | system.security.auto_approve | Attribute for system.security.auto approve in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 131 |
| test_current_owner_operation_and_fresh_save_are_required | system.security.operation_id | Attribute for system.security.operation id in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 132, 136 |
| test_current_owner_operation_and_fresh_save_are_required | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_current_owner_operation_and_fresh_save_are_required | first | Local binding for first in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_current_owner_operation_and_fresh_save_are_required | second | Local binding for second in test_current_owner_operation_and_fresh_save_are_required; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| test_gated_pipeline_completes_with_real_acceptance_services | system | Parameter for system in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_gated_pipeline_completes_with_real_acceptance_services | monkeypatch | Parameter for monkeypatch in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_gated_pipeline_completes_with_real_acceptance_services | replace_code | Parameter for replace code in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_gated_pipeline_completes_with_real_acceptance_services | json | Imported dependency for json in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 148 |
| test_gated_pipeline_completes_with_real_acceptance_services | approve_next_review | Imported dependency for approve next review in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 150 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | task | Parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 152 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 158, 164 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | thread | Local binding for thread in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_gated_pipeline_completes_with_real_acceptance_services.tester | errors | Local binding for errors in test_gated_pipeline_completes_with_real_acceptance_services.tester; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_gated_pipeline_completes_with_real_acceptance_services | seen | Local binding for seen in test_gated_pipeline_completes_with_real_acceptance_services; use the enclosing contract and type below. | Return type of install_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| test_gated_pipeline_completes_with_real_acceptance_services.lambda_188 | task | Callback parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.lambda_188; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 188 |
| test_gated_pipeline_completes_with_real_acceptance_services.lambda_189 | task | Callback parameter for task in test_gated_pipeline_completes_with_real_acceptance_services.lambda_189; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 189 |
| test_gated_pipeline_completes_with_real_acceptance_services | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
