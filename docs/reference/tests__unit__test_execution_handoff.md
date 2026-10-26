# Reference for tests/unit/test_execution_handoff.py

Host execution receipts prevent manager completion prose from becoming evidence.

Source fingerprint: 2b196f9839bc0da4afeb15bd261d9d512906122595d13f3af36b079fac92c054

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### authorize_fixture

Install independently authored trusted code; bypass only the human fixture UI.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_creation_final_answer_requires_actual_current_execution

Verify creation final answer requires actual current execution.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_creation_final_answer_requires_actual_current_execution.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_creation_final_answer_requires_actual_current_execution.crew.kickoff

Provide kickoff for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_execution_context_is_defensive_and_receipt_is_call_bound

Verify execution context is defensive and receipt is call bound.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_stale_or_failed_call_cannot_supply_final_evidence

Verify stale or failed call cannot supply final evidence.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_reuse_cannot_replace_observed_result_with_model_prose

Verify reuse cannot replace observed result with model prose.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_reuse_cannot_replace_observed_result_with_model_prose.kickoff

Provide kickoff for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### test_edit_during_child_execution_revokes_result

Verify edit during child execution revokes result.

Kind: callable. Declared return: Not declared / class. Source line: 129.

### test_edit_during_child_execution_revokes_result.replace

Provide replace for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 135.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| authorize_fixture | system | Parameter for system in authorize_fixture; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| authorize_fixture | folder | Local binding for folder in authorize_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 11 |
| authorize_fixture | ledger | Local binding for ledger in authorize_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 15 |
| authorize_fixture | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| authorize_fixture | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| authorize_fixture | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 25 |
| test_creation_final_answer_requires_actual_current_execution | system | Parameter for system in test_creation_final_answer_requires_actual_current_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_creation_final_answer_requires_actual_current_execution | monkeypatch | Parameter for monkeypatch in test_creation_final_answer_requires_actual_current_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_creation_final_answer_requires_actual_current_execution | execute | Parameter for execute in test_creation_final_answer_requires_actual_current_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_creation_final_answer_requires_actual_current_execution | stages | Local binding for stages in test_creation_final_answer_requires_actual_current_execution; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 46 |
| test_creation_final_answer_requires_actual_current_execution.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_creation_final_answer_requires_actual_current_execution | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_execution_context_is_defensive_and_receipt_is_call_bound | system | Parameter for system in test_execution_context_is_defensive_and_receipt_is_call_bound; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_execution_context_is_defensive_and_receipt_is_call_bound | ledger | Local binding for ledger in test_execution_context_is_defensive_and_receipt_is_call_bound; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_execution_context_is_defensive_and_receipt_is_call_bound | context | Local binding for context in test_execution_context_is_defensive_and_receipt_is_call_bound; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_execution_context_is_defensive_and_receipt_is_call_bound | args | Local binding for args in test_execution_context_is_defensive_and_receipt_is_call_bound; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 82 |
| test_execution_context_is_defensive_and_receipt_is_call_bound | receipt | Local binding for receipt in test_execution_context_is_defensive_and_receipt_is_call_bound; use the enclosing contract and type below. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_stale_or_failed_call_cannot_supply_final_evidence | system | Parameter for system in test_stale_or_failed_call_cannot_supply_final_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_stale_or_failed_call_cannot_supply_final_evidence | invalidate | Parameter for invalidate in test_stale_or_failed_call_cannot_supply_final_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_stale_or_failed_call_cannot_supply_final_evidence | ledger | Local binding for ledger in test_stale_or_failed_call_cannot_supply_final_evidence; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_stale_or_failed_call_cannot_supply_final_evidence | system.security.operation_id | Attribute for system.security.operation id in test_stale_or_failed_call_cannot_supply_final_evidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 102 |
| test_stale_or_failed_call_cannot_supply_final_evidence | stream | Managed resource for stream in test_stale_or_failed_call_cannot_supply_final_evidence; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 104 |
| test_reuse_cannot_replace_observed_result_with_model_prose | system | Parameter for system in test_reuse_cannot_replace_observed_result_with_model_prose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_reuse_cannot_replace_observed_result_with_model_prose | monkeypatch | Parameter for monkeypatch in test_reuse_cannot_replace_observed_result_with_model_prose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_reuse_cannot_replace_observed_result_with_model_prose | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_edit_during_child_execution_revokes_result | system | Parameter for system in test_edit_during_child_execution_revokes_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_edit_during_child_execution_revokes_result | monkeypatch | Parameter for monkeypatch in test_edit_during_child_execution_revokes_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_edit_during_child_execution_revokes_result | ledger | Local binding for ledger in test_edit_during_child_execution_revokes_result; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_edit_during_child_execution_revokes_result | backend | Injected framework/execution provider; callers determine the required protocol. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_edit_during_child_execution_revokes_result | original | Local binding for original in test_edit_during_child_execution_revokes_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_edit_during_child_execution_revokes_result.replace | args | Parameter for args in test_edit_during_child_execution_revokes_result.replace; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_edit_during_child_execution_revokes_result.replace | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_edit_during_child_execution_revokes_result.replace | observed | Returned observation checked against the reviewed host-side expectation. | Return type of original; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
