# Reference for tests/unit/test_reviewed_reuse.py

REUSE-001: exact reviewed tools may serve later queries in the same session.

Source fingerprint: 588c7d2e0ce098a83dbe6b03585fd5ca1656a2712b59f8003902fbb0d0eab157

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### successful_tool

Establish review and actual execution using independently authored code.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_second_query_reuses_without_tests_review_or_reading_code

A real service call with new inputs must yield a fresh observed result.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### test_second_query_reuses_without_tests_review_or_reading_code.forbidden

Fail on any repeated review, artifact read or unittest execution.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_second_query_reuses_without_tests_review_or_reading_code.kickoff

Replace only LLM choice; exercise real preparation and execution.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_review_without_successful_call_does_not_grant_reuse

A review alone must not establish later-operation authorization.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### test_reuse_rejects_drift_owner_and_revocation

Observed edits and owner/lifecycle changes cannot revive earlier trust.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_successful_tool_does_not_authorize_unreviewed_function

Reusable grants retain the approved public-function boundary.

Kind: callable. Declared return: Not declared / class. Source line: 72.

### test_sensitive_call_needs_manual_permission_even_after_review

File-capable code cannot inherit silent execution from acceptance.

Kind: callable. Declared return: Not declared / class. Source line: 82.

### test_sensitive_call_needs_manual_permission_even_after_review.deny

Capture server-owned exact-call details and deny the sensitive action.

Kind: callable. Declared return: Not declared / class. Source line: 101.

### test_computation_classifier_is_conservative

Only explicit computation constructs avoid the per-call permission gate.

Kind: callable. Declared return: Not declared / class. Source line: 135.

### test_sensitive_approval_is_per_call_and_rechecks_waiting_state

An approved dialog neither changes arguments nor overrides concurrent drift.

Kind: callable. Declared return: Not declared / class. Source line: 143.

### test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve

Approve only the captured call, simulating a mutation during the wait.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### test_new_ledger_cannot_import_session_grant_from_same_artifacts

Disk artifacts and another session's success never establish reuse trust.

Kind: callable. Declared return: Not declared / class. Source line: 183.

### test_status_polling_does_not_destroy_unchanged_later_query_grant

Read-only UI status may expire a receipt without losing session approval.

Kind: callable. Declared return: Not declared / class. Source line: 193.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | authorize_fixture | Imported dependency for authorize fixture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| successful_tool | system | Parameter for system in successful_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| successful_tool | ledger | Local binding for ledger in successful_tool; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_second_query_reuses_without_tests_review_or_reading_code | system | Parameter for system in test_second_query_reuses_without_tests_review_or_reading_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_second_query_reuses_without_tests_review_or_reading_code | monkeypatch | Parameter for monkeypatch in test_second_query_reuses_without_tests_review_or_reading_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_second_query_reuses_without_tests_review_or_reading_code.forbidden | args | Parameter for args in test_second_query_reuses_without_tests_review_or_reading_code.forbidden; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_second_query_reuses_without_tests_review_or_reading_code.forbidden | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_second_query_reuses_without_tests_review_or_reading_code.kickoff | prepared | Local binding for prepared in test_second_query_reuses_without_tests_review_or_reading_code.kickoff; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_second_query_reuses_without_tests_review_or_reading_code | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_review_without_successful_call_does_not_grant_reuse | system | Parameter for system in test_review_without_successful_call_does_not_grant_reuse; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| test_review_without_successful_call_does_not_grant_reuse | ledger | Local binding for ledger in test_review_without_successful_call_does_not_grant_reuse; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_review_without_successful_call_does_not_grant_reuse | system.security.operation_id | Attribute for system.security.operation id in test_review_without_successful_call_does_not_grant_reuse; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 48 |
| test_reuse_rejects_drift_owner_and_revocation | system | Parameter for system in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_reuse_rejects_drift_owner_and_revocation | change | Parameter for change in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_reuse_rejects_drift_owner_and_revocation | ledger | Local binding for ledger in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | Return type of successful_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_reuse_rejects_drift_owner_and_revocation | system.security.operation_id | Attribute for system.security.operation id in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| test_reuse_rejects_drift_owner_and_revocation | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_reuse_rejects_drift_owner_and_revocation | original | Local binding for original in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_reuse_rejects_drift_owner_and_revocation | system.security.owner_id | Attribute for system.security.owner id in test_reuse_rejects_drift_owner_and_revocation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 64 |
| test_successful_tool_does_not_authorize_unreviewed_function | system | Parameter for system in test_successful_tool_does_not_authorize_unreviewed_function; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_successful_tool_does_not_authorize_unreviewed_function | ledger | Local binding for ledger in test_successful_tool_does_not_authorize_unreviewed_function; use the enclosing contract and type below. | Return type of successful_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_successful_tool_does_not_authorize_unreviewed_function | system.security.operation_id | Attribute for system.security.operation id in test_successful_tool_does_not_authorize_unreviewed_function; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 75 |
| test_sensitive_call_needs_manual_permission_even_after_review | system | Parameter for system in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_sensitive_call_needs_manual_permission_even_after_review | monkeypatch | Parameter for monkeypatch in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_sensitive_call_needs_manual_permission_even_after_review | folder | Local binding for folder in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 84 |
| test_sensitive_call_needs_manual_permission_even_after_review | ledger | Local binding for ledger in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_sensitive_call_needs_manual_permission_even_after_review | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_sensitive_call_needs_manual_permission_even_after_review | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_sensitive_call_needs_manual_permission_even_after_review | requests | Local binding for requests in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 99 |
| test_sensitive_call_needs_manual_permission_even_after_review.deny | args | Parameter for args in test_sensitive_call_needs_manual_permission_even_after_review.deny; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_sensitive_call_needs_manual_permission_even_after_review.deny | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_sensitive_call_needs_manual_permission_even_after_review | outcome | Local binding for outcome in test_sensitive_call_needs_manual_permission_even_after_review; use the enclosing contract and type below. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_computation_classifier_is_conservative | source | Explicit source document or source-code text; never imported for reference generation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_computation_classifier_is_conservative | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_computation_classifier_is_conservative | computation_only | Imported dependency for computation only in test_computation_classifier_is_conservative; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 137 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | system | Parameter for system in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 143 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | monkeypatch | Parameter for monkeypatch in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 143 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | mutation | Parameter for mutation in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 143 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | ledger | Local binding for ledger in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | seen | Local binding for seen in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 158 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve | args | Parameter for args in test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve | system.security.operation_id | Attribute for system.security.operation id in test_sensitive_approval_is_per_call_and_rechecks_waiting_state.approve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 166 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | first | Local binding for first in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_sensitive_approval_is_per_call_and_rechecks_waiting_state | system.security.operation_id | Attribute for system.security.operation id in test_sensitive_approval_is_per_call_and_rechecks_waiting_state; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 176 |
| test_new_ledger_cannot_import_session_grant_from_same_artifacts | system | Parameter for system in test_new_ledger_cannot_import_session_grant_from_same_artifacts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_new_ledger_cannot_import_session_grant_from_same_artifacts | VerificationLedger | Imported dependency for VerificationLedger in test_new_ledger_cannot_import_session_grant_from_same_artifacts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 185 |
| test_new_ledger_cannot_import_session_grant_from_same_artifacts | other | Local binding for other in test_new_ledger_cannot_import_session_grant_from_same_artifacts; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| test_status_polling_does_not_destroy_unchanged_later_query_grant | system | Parameter for system in test_status_polling_does_not_destroy_unchanged_later_query_grant; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 193 |
| test_status_polling_does_not_destroy_unchanged_later_query_grant | ledger | Local binding for ledger in test_status_polling_does_not_destroy_unchanged_later_query_grant; use the enclosing contract and type below. | Return type of successful_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 195 |
| test_status_polling_does_not_destroy_unchanged_later_query_grant | system.security.operation_id | Attribute for system.security.operation id in test_status_polling_does_not_destroy_unchanged_later_query_grant; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 196 |
