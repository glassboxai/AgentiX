# Reference for tests/unit/test_durable_approvals.py

REUSE-002: protected approvals survive fresh ledgers without trusting artifacts.

Source fingerprint: 79762a6271b14be7407c49f57949a11ad420dc1cbe0025c94f2764df0c2d65b9

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

### test_successful_review_survives_a_new_owner_and_ledger

Another session can use intact approved bytes without tests or review.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_durable_approval_rejects_changed_identity_and_tampering

Changed source, policy, location and unauthenticated records cannot authorize.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_session_close_retains_durable_approval_but_explicit_revoke_removes_it

Closing a browser expires its work, not an approval owned by the Windows user.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_review_without_actual_success_creates_no_durable_record

Manual review alone never persists an executable grant.

Kind: callable. Declared return: Not declared / class. Source line: 111.

### test_durable_sensitive_tool_never_persists_per_call_permission

A fresh runtime must ask again for sensitive actions despite durable review.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### test_durable_sensitive_tool_never_persists_per_call_permission.deny

Deny a separate exact-call permission in the new browser owner.

Kind: callable. Declared return: Not declared / class. Source line: 160.

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
| test_successful_review_survives_a_new_owner_and_ledger | system | Parameter for system in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_successful_review_survives_a_new_owner_and_ledger | tmp_path | Parameter for tmp path in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_successful_review_survives_a_new_owner_and_ledger | VerificationLedger | Imported dependency for VerificationLedger in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 50 |
| test_successful_review_survives_a_new_owner_and_ledger | store | Local binding for store in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_successful_review_survives_a_new_owner_and_ledger | _ | Local binding for  in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh_security | Local binding for fresh security in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh_security.TOOLS_ROOT_DIR | Attribute for fresh security.TOOLS ROOT DIR in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_successful_review_survives_a_new_owner_and_ledger | fresh | Local binding for fresh in test_successful_review_survives_a_new_owner_and_ledger; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_durable_approval_rejects_changed_identity_and_tampering | system | Parameter for system in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_durable_approval_rejects_changed_identity_and_tampering | tmp_path | Parameter for tmp path in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_durable_approval_rejects_changed_identity_and_tampering | mutation | Parameter for mutation in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_durable_approval_rejects_changed_identity_and_tampering | VerificationLedger | Imported dependency for VerificationLedger in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 65 |
| test_durable_approval_rejects_changed_identity_and_tampering | store | Local binding for store in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 67, 73, 77 |
| test_durable_approval_rejects_changed_identity_and_tampering | ledger | Local binding for ledger in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_durable_approval_rejects_changed_identity_and_tampering | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_durable_approval_rejects_changed_identity_and_tampering | original | Local binding for original in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_durable_approval_rejects_changed_identity_and_tampering | ApprovalStore | Imported dependency for ApprovalStore in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 75 |
| test_durable_approval_rejects_changed_identity_and_tampering | records | Local binding for records in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| test_durable_approval_rejects_changed_identity_and_tampering | fresh | Local binding for fresh in test_durable_approval_rejects_changed_identity_and_tampering; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | system | Parameter for system in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | tmp_path | Parameter for tmp path in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | VerificationLedger | Imported dependency for VerificationLedger in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | store | Local binding for store in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | ledger | Local binding for ledger in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | other | Local binding for other in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | other.TOOLS_ROOT_DIR | Attribute for other.TOOLS ROOT DIR in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_session_close_retains_durable_approval_but_explicit_revoke_removes_it | fresh | Local binding for fresh in test_session_close_retains_durable_approval_but_explicit_revoke_removes_it; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_review_without_actual_success_creates_no_durable_record | system | Parameter for system in test_review_without_actual_success_creates_no_durable_record; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_review_without_actual_success_creates_no_durable_record | tmp_path | Parameter for tmp path in test_review_without_actual_success_creates_no_durable_record; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| test_durable_sensitive_tool_never_persists_per_call_permission | system | Parameter for system in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_durable_sensitive_tool_never_persists_per_call_permission | tmp_path | Parameter for tmp path in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_durable_sensitive_tool_never_persists_per_call_permission | monkeypatch | Parameter for monkeypatch in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_durable_sensitive_tool_never_persists_per_call_permission | ArtifactTools | Imported dependency for ArtifactTools in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 120 |
| test_durable_sensitive_tool_never_persists_per_call_permission | store | Local binding for store in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of configure_store; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_durable_sensitive_tool_never_persists_per_call_permission | ledger | Local binding for ledger in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of authorize_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_durable_sensitive_tool_never_persists_per_call_permission | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_durable_sensitive_tool_never_persists_per_call_permission | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_durable_sensitive_tool_never_persists_per_call_permission | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_durable_sensitive_tool_never_persists_per_call_permission | reviewed | Local binding for reviewed in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 135 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh_security | Local binding for fresh security in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 156 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh_security.TOOLS_ROOT_DIR | Attribute for fresh security.TOOLS ROOT DIR in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_durable_sensitive_tool_never_persists_per_call_permission | seen | Local binding for seen in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 158 |
| test_durable_sensitive_tool_never_persists_per_call_permission.deny | args | Parameter for args in test_durable_sensitive_tool_never_persists_per_call_permission.deny; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_durable_sensitive_tool_never_persists_per_call_permission.deny | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_durable_sensitive_tool_never_persists_per_call_permission | fresh | Local binding for fresh in test_durable_sensitive_tool_never_persists_per_call_permission; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
