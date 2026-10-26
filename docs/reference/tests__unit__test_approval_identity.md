# Reference for tests/unit/test_approval_identity.py

Exercise real handshakes with deterministic thread synchronization.

Source fingerprint: cd801ff8abdfee2e89f318c18c81d7247c011a14f39c3768ad1c47f15173987f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### pending_request

Publish a real worker request and return a deterministic cleanup handle.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_wrong_or_missing_identity_does_not_authorize

Verify wrong or missing identity does not authorize.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_duplicate_response_cannot_change_first_decision

Verify duplicate response cannot change first decision.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_expired_response_is_denied

Verify expired response is denied.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_second_request_cannot_overwrite_pending_request

Verify second request cannot overwrite pending request.

Kind: callable. Declared return: Not declared / class. Source line: 89.

### test_owners_have_independent_auto_approval_settings

Verify owners have independent auto approval settings.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### test_owner_factory_does_not_inherit_parent_activity_or_operation

Verify owner factory does not inherit parent activity or operation.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_previous_request_id_cannot_approve_same_filepath_again

Verify previous request id cannot approve same filepath again.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_two_pending_owners_cannot_resolve_each_others_work

Verify two pending owners cannot resolve each others work.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### test_closing_owner_denies_pending_and_future_operations

Verify closing owner denies pending and future operations.

Kind: callable. Declared return: Not declared / class. Source line: 174.

### test_invalid_decision_types_do_not_authorize

Verify invalid decision types do not authorize.

Kind: callable. Declared return: Not declared / class. Source line: 186.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ApprovalCoordinator | Imported dependency for ApprovalCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| pending_request | boundary | Parameter for boundary in pending_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| pending_request | monkeypatch | Parameter for monkeypatch in pending_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| pending_request | ready | Local binding for ready in pending_request; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| pending_request | original | Local binding for original in pending_request; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| pending_request.lambda_15 | timeout | Callback parameter for timeout in pending_request.lambda_15; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 15 |
| pending_request | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 17 |
| pending_request | worker | Local binding for worker in pending_request; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_wrong_or_missing_identity_does_not_authorize | monkeypatch | Parameter for monkeypatch in test_wrong_or_missing_identity_does_not_authorize; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_wrong_or_missing_identity_does_not_authorize | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_wrong_or_missing_identity_does_not_authorize | owner | Parameter for owner in test_wrong_or_missing_identity_does_not_authorize; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_wrong_or_missing_identity_does_not_authorize | boundary | Local binding for boundary in test_wrong_or_missing_identity_does_not_authorize; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_wrong_or_missing_identity_does_not_authorize | worker | Local binding for worker in test_wrong_or_missing_identity_does_not_authorize; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_wrong_or_missing_identity_does_not_authorize | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_wrong_or_missing_identity_does_not_authorize | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_wrong_or_missing_identity_does_not_authorize | supplied | Local binding for supplied in test_wrong_or_missing_identity_does_not_authorize; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_duplicate_response_cannot_change_first_decision | monkeypatch | Parameter for monkeypatch in test_duplicate_response_cannot_change_first_decision; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_duplicate_response_cannot_change_first_decision | boundary | Local binding for boundary in test_duplicate_response_cannot_change_first_decision; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_duplicate_response_cannot_change_first_decision | worker | Local binding for worker in test_duplicate_response_cannot_change_first_decision; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_duplicate_response_cannot_change_first_decision | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_duplicate_response_cannot_change_first_decision | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_expired_response_is_denied | monkeypatch | Parameter for monkeypatch in test_expired_response_is_denied; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_expired_response_is_denied | boundary | Local binding for boundary in test_expired_response_is_denied; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_expired_response_is_denied | now | Local binding for now in test_expired_response_is_denied; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 74 |
| test_expired_response_is_denied | boundary._clock | Attribute for boundary. clock in test_expired_response_is_denied; use the enclosing contract and type below. | Return type of staticmethod; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_expired_response_is_denied | worker | Local binding for worker in test_expired_response_is_denied; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_expired_response_is_denied | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_expired_response_is_denied | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_second_request_cannot_overwrite_pending_request | monkeypatch | Parameter for monkeypatch in test_second_request_cannot_overwrite_pending_request; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 89 |
| test_second_request_cannot_overwrite_pending_request | boundary | Local binding for boundary in test_second_request_cannot_overwrite_pending_request; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_second_request_cannot_overwrite_pending_request | worker | Local binding for worker in test_second_request_cannot_overwrite_pending_request; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_second_request_cannot_overwrite_pending_request | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_second_request_cannot_overwrite_pending_request | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_owners_have_independent_auto_approval_settings | first | Local binding for first in test_owners_have_independent_auto_approval_settings; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 106 |
| test_owners_have_independent_auto_approval_settings | second | Local binding for second in test_owners_have_independent_auto_approval_settings; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 106 |
| test_owners_have_independent_auto_approval_settings | first.auto_approve | Attribute for first.auto approve in test_owners_have_independent_auto_approval_settings; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 107 |
| test_owner_factory_does_not_inherit_parent_activity_or_operation | parent | Local binding for parent in test_owner_factory_does_not_inherit_parent_activity_or_operation; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_owner_factory_does_not_inherit_parent_activity_or_operation | parent.activity_capture | Attribute for parent.activity capture in test_owner_factory_does_not_inherit_parent_activity_or_operation; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_owner_factory_does_not_inherit_parent_activity_or_operation | parent.operation_id | Attribute for parent.operation id in test_owner_factory_does_not_inherit_parent_activity_or_operation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 116 |
| test_owner_factory_does_not_inherit_parent_activity_or_operation | child | Local binding for child in test_owner_factory_does_not_inherit_parent_activity_or_operation; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_previous_request_id_cannot_approve_same_filepath_again | monkeypatch | Parameter for monkeypatch in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| test_previous_request_id_cannot_approve_same_filepath_again | boundary | Local binding for boundary in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_previous_request_id_cannot_approve_same_filepath_again | first_worker | Local binding for first worker in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_previous_request_id_cannot_approve_same_filepath_again | first_result | Local binding for first result in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_previous_request_id_cannot_approve_same_filepath_again | first | Local binding for first in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_previous_request_id_cannot_approve_same_filepath_again | second_worker | Local binding for second worker in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_previous_request_id_cannot_approve_same_filepath_again | second_result | Local binding for second result in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_previous_request_id_cannot_approve_same_filepath_again | second | Local binding for second in test_previous_request_id_cannot_approve_same_filepath_again; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_two_pending_owners_cannot_resolve_each_others_work | monkeypatch | Parameter for monkeypatch in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_two_pending_owners_cannot_resolve_each_others_work | first | Local binding for first in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 147 |
| test_two_pending_owners_cannot_resolve_each_others_work | second | Local binding for second in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 147 |
| test_two_pending_owners_cannot_resolve_each_others_work | worker_a | Local binding for worker a in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_two_pending_owners_cannot_resolve_each_others_work | result_a | Local binding for result a in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_two_pending_owners_cannot_resolve_each_others_work | request_a | Local binding for request a in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_two_pending_owners_cannot_resolve_each_others_work | worker_b | Local binding for worker b in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_two_pending_owners_cannot_resolve_each_others_work | result_b | Local binding for result b in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_two_pending_owners_cannot_resolve_each_others_work | request_b | Local binding for request b in test_two_pending_owners_cannot_resolve_each_others_work; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_closing_owner_denies_pending_and_future_operations | monkeypatch | Parameter for monkeypatch in test_closing_owner_denies_pending_and_future_operations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 174 |
| test_closing_owner_denies_pending_and_future_operations | boundary | Local binding for boundary in test_closing_owner_denies_pending_and_future_operations; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_closing_owner_denies_pending_and_future_operations | worker | Local binding for worker in test_closing_owner_denies_pending_and_future_operations; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_closing_owner_denies_pending_and_future_operations | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_closing_owner_denies_pending_and_future_operations | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_closing_owner_denies_pending_and_future_operations | boundary.auto_approve | Attribute for boundary.auto approve in test_closing_owner_denies_pending_and_future_operations; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 181 |
| test_invalid_decision_types_do_not_authorize | monkeypatch | Parameter for monkeypatch in test_invalid_decision_types_do_not_authorize; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_invalid_decision_types_do_not_authorize | decision | Parameter for decision in test_invalid_decision_types_do_not_authorize; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_invalid_decision_types_do_not_authorize | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 186 |
| test_invalid_decision_types_do_not_authorize | boundary | Local binding for boundary in test_invalid_decision_types_do_not_authorize; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| test_invalid_decision_types_do_not_authorize | worker | Local binding for worker in test_invalid_decision_types_do_not_authorize; use the enclosing contract and type below. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_invalid_decision_types_do_not_authorize | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_invalid_decision_types_do_not_authorize | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
