# Reference for tests/unit/test_durable_approvals.py

REUSE-002: protected approvals survive fresh ledgers without trusting artifacts.

Source fingerprint: d1a6fa89d00a544185c2a32b4f1cc4ad685a99cce4d99ab9216c8999a238d8e6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### TestProtector

Authenticate trusted fixture records; this double is not Windows protection.

Kind: class. Declared return: Not declared / class. Source line: 10.

### TestProtector.seal

Attach a test-only keyed digest so tampering fails observably.

Kind: callable. Declared return: bytes. Source line: 15.

### TestProtector.unseal

Reject altered records rather than silently decoding arbitrary JSON.

Kind: callable. Declared return: bytes. Source line: 19.

### configure_store

Inject temporary protected persistence into the actual ledger.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### publish

Install independently authored code and publish only after actual success.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_reseal_rebinds_unchanged_bytes_to_the_current_policy

A policy-only change must be recoverable without re-running the tool.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked

Resealing never transfers a grant to different source or tests.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_successful_review_survives_a_new_owner_and_ledger

Another session can use intact approved bytes without tests or review.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_durable_approval_rejects_changed_identity_and_tampering

Changed source, policy, location and unauthenticated records cannot authorize.

Kind: callable. Declared return: Not declared / class. Source line: 91.

### test_session_close_retains_durable_approval_but_explicit_revoke_removes_it

Closing a browser expires its work, not an approval owned by the Windows user.

Kind: callable. Declared return: Not declared / class. Source line: 124.

### install_approved_tool

Publish one independently authored tool and persist its durable approval.

Kind: callable. Declared return: Not declared / class. Source line: 139.

### test_rerunning_unchanged_tests_keeps_the_durable_approval

Re-verifying identical bytes must not delete an approval the user already gave.

Kind: callable. Declared return: Not declared / class. Source line: 188.

### test_recording_fresh_evidence_keeps_the_durable_approval

New in-memory evidence for identical bytes must not revoke the stored grant.

Kind: callable. Declared return: Not declared / class. Source line: 200.

### test_review_without_actual_success_creates_no_durable_record

Manual review alone never persists an executable grant.

Kind: callable. Declared return: Not declared / class. Source line: 216.

### test_durable_sensitive_tool_never_persists_per_call_permission

A fresh runtime must ask again for sensitive actions despite durable review.

Kind: callable. Declared return: Not declared / class. Source line: 223.

### test_durable_sensitive_tool_never_persists_per_call_permission.deny

Deny a separate exact-call permission in the new browser owner.

Kind: callable. Declared return: Not declared / class. Source line: 265.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hmac | Imported dependency for hmac in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | authorize_fixture | Imported dependency for authorize fixture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| TestProtector | __test__ | Local binding for test in TestProtector; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 13 |
| TestProtector.seal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| TestProtector.seal | data | Parameter for data in TestProtector.seal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 15 |
| TestProtector.unseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| TestProtector.unseal | data | Parameter for data in TestProtector.unseal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 19 |
| configure_store | system | Parameter for system in configure_store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| configure_store | directory | Parameter for directory in configure_store; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 28 |
| configure_store | policy | Parameter for policy in configure_store; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 28 |
| configure_store | ApprovalStore | Imported dependency for ApprovalStore in configure_store; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| configure_store | protector | Local binding for protector in configure_store; use the enclosing contract and type below. | Return type of TestProtector; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| configure_store | store | Local binding for store in configure_store; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| configure_store | system.custom_tools.verification.store | Attribute for system.custom tools.verification.store in configure_store; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| publish | system | Parameter for system in publish; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| publish | tmp_path | Parameter for tmp path in publish; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| publish | store | Local binding for store in publish; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| publish | ledger | Local binding for ledger in publish; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | system | Parameter for system in test_reseal_rebinds_unchanged_bytes_to_the_current_policy; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | tmp_path | Parameter for tmp path in test_reseal_rebinds_unchanged_bytes_to_the_current_policy; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | store | Local binding for store in test_reseal_rebinds_unchanged_bytes_to_the_current_policy; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | _ | Local binding for  in test_reseal_rebinds_unchanged_bytes_to_the_current_policy; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_reseal_rebinds_unchanged_bytes_to_the_current_policy | rotated | Local binding for rotated in test_reseal_rebinds_unchanged_bytes_to_the_current_policy; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | system | Parameter for system in test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | tmp_path | Parameter for tmp path in test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | store | Local binding for store in test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | _ | Local binding for  in test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked | rotated | Local binding for rotated in test_reseal_refuses_changed_bytes_and_keeps_the_record_revoked; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_successful_review_survives_a_new_owner_and_ledger | system | Parameter for system in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_successful_review_survives_a_new_owner_and_ledger | tmp_path | Parameter for tmp path in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_successful_review_survives_a_new_owner_and_ledger | VerificationLedger | Imported dependency for VerificationLedger in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
| test_successful_review_survives_a_new_owner_and_ledger | store | Local binding for store in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_successful_review_survives_a_new_owner_and_ledger | _ | Local binding for  in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh_security | Local binding for fresh security in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh_security.TOOLS_ROOT_DIR | Attribute for fresh security.TOOLS ROOT DIR in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh | Local binding for fresh in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_durable_approval_rejects_changed_identity_and_tampering | system | Parameter for system in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_durable_approval_rejects_changed_identity_and_tampering | tmp_path | Parameter for tmp path in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_durable_approval_rejects_changed_identity_and_tampering | mutation | Parameter for mutation in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_durable_approval_rejects_changed_identity_and_tampering | VerificationLedger | Imported dependency for VerificationLedger in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 93 |
| test_durable_approval_rejects_changed_identity_and_tampering | store | Local binding for store in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 95, 101, 105 |
| test_durable_approval_rejects_changed_identity_and_tampering | ledger | Local binding for ledger in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
| test_durable_approval_rejects_changed_identity_and_tampering | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_durable_approval_rejects_changed_identity_and_tampering | original | Local binding for original in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_durable_approval_rejects_changed_identity_and_tampering | ApprovalStore | Imported dependency for ApprovalStore in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 103 |
| test_durable_approval_rejects_changed_identity_and_tampering | records | Local binding for records in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_durable_approval_rejects_changed_identity_and_tampering | fresh | Local binding for fresh in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | system | Parameter for system in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | tmp_path | Parameter for tmp path in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | VerificationLedger | Imported dependency for VerificationLedger in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 126 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | store | Local binding for store in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | ledger | Local binding for ledger in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | other | Local binding for other in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | other.TOOLS_ROOT_DIR | Attribute for other.TOOLS ROOT DIR in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | fresh | Local binding for fresh in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| install_approved_tool | system | Parameter for system in install_approved_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 139 |
| install_approved_tool | tmp_path | Parameter for tmp path in install_approved_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 139 |
| install_approved_tool | store | Local binding for store in install_approved_tool; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| install_approved_tool | folder | Local binding for folder in install_approved_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 142 |
| install_approved_tool | ledger | Local binding for ledger in install_approved_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 151 |
| install_approved_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| install_approved_tool | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| install_approved_tool | records | Local binding for records in install_approved_tool; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | system | Parameter for system in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 188 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | tmp_path | Parameter for tmp path in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 188 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | VerificationLedger | Imported dependency for VerificationLedger in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 190 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | store | Local binding for store in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | _ | Local binding for  in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | records | Local binding for records in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | fresh_security | Local binding for fresh security in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 195 |
| test_rerunning_unchanged_tests_keeps_the_durable_approval | fresh_security.TOOLS_ROOT_DIR | Attribute for fresh security.TOOLS ROOT DIR in test_rerunning_unchanged_tests_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_recording_fresh_evidence_keeps_the_durable_approval | system | Parameter for system in test_recording_fresh_evidence_keeps_the_durable_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_recording_fresh_evidence_keeps_the_durable_approval | tmp_path | Parameter for tmp path in test_recording_fresh_evidence_keeps_the_durable_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_recording_fresh_evidence_keeps_the_durable_approval | store | Local binding for store in test_recording_fresh_evidence_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_recording_fresh_evidence_keeps_the_durable_approval | ledger | Local binding for ledger in test_recording_fresh_evidence_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_recording_fresh_evidence_keeps_the_durable_approval | records | Local binding for records in test_recording_fresh_evidence_keeps_the_durable_approval; use the enclosing contract and type below. | Return type of install_approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_recording_fresh_evidence_keeps_the_durable_approval | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_recording_fresh_evidence_keeps_the_durable_approval | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_review_without_actual_success_creates_no_durable_record | system | Parameter for system in test_review_without_actual_success_creates_no_durable_record; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 216 |
| test_review_without_actual_success_creates_no_durable_record | tmp_path | Parameter for tmp path in test_review_without_actual_success_creates_no_durable_record; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 216 |
| test_durable_sensitive_tool_never_persists_per_call_permission | system | Parameter for system in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_durable_sensitive_tool_never_persists_per_call_permission | tmp_path | Parameter for tmp path in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_durable_sensitive_tool_never_persists_per_call_permission | monkeypatch | Parameter for monkeypatch in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_durable_sensitive_tool_never_persists_per_call_permission | ArtifactTools | Imported dependency for ArtifactTools in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 225 |
| test_durable_sensitive_tool_never_persists_per_call_permission | store | Local binding for store in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_durable_sensitive_tool_never_persists_per_call_permission | ledger | Local binding for ledger in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| test_durable_sensitive_tool_never_persists_per_call_permission | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 229 |
| test_durable_sensitive_tool_never_persists_per_call_permission | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_durable_sensitive_tool_never_persists_per_call_permission | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_durable_sensitive_tool_never_persists_per_call_permission | reviewed | Local binding for reviewed in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 240 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh_security | Local binding for fresh security in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 261 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh_security.TOOLS_ROOT_DIR | Attribute for fresh security.TOOLS ROOT DIR in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_durable_sensitive_tool_never_persists_per_call_permission | seen | Local binding for seen in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 263 |
| test_durable_sensitive_tool_never_persists_per_call_permission.deny | args | Parameter for args in test_durable_sensitive_tool_never_persists_per_call_permission.deny; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 265 |
| test_durable_sensitive_tool_never_persists_per_call_permission.deny | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 265 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh | Local binding for fresh in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 271 |
