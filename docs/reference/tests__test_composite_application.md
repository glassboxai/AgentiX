# Reference for tests/test_composite_application.py

LAB-005 contracts and package trust tests with maintained, offline fixtures.

Source fingerprint: 36a0d381961e5e77edbb24d972da196098c2ad54f243a0a6d61dffe371bbcc28

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### api

Import the maintained host validator, never an application module.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### copied

Copy only the generated schema-3 package, not any catalog.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### test_review_captures_bytes_and_rejects_changes

Catch review bypass and rereading changed code after snapshot approval.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_unreviewable_packages_are_rejected

Catch unexpected executables, missing closure, elevated scope and invalid DAGs.

Kind: callable. Declared return: Not declared / class. Source line: 40.

### test_symlink_package_member_is_rejected

Catch approved-file aliasing outside the selected package.

Kind: callable. Declared return: Not declared / class. Source line: 64.

### test_strict_return_contract_rejects_bool_negative_and_extra_fields

Catch coercion or accepting invalid structured child results as success.

Kind: callable. Declared return: Not declared / class. Source line: 78.

### test_parent_rejects_application_tool_rpc_without_dispatch

Direct-call applications cannot request legacy host tool capabilities.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### test_application_cannot_exceed_manifest_lifetime

A host caller cannot silently exceed the application's declared 300-second limit.

Kind: callable. Declared return: Not declared / class. Source line: 113.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| api | application_artifacts | Imported dependency for application artifacts in api; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 11 |
| copied | tmp_path | Parameter for tmp path in copied; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| copied | package | Imported dependency for package in copied; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| copied | target | Local binding for target in copied; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_review_captures_bytes_and_rejects_changes | tmp_path | Parameter for tmp path in test_review_captures_bytes_and_rejects_changes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_review_captures_bytes_and_rejects_changes | folder | Local binding for folder in test_review_captures_bytes_and_rejects_changes; use the enclosing contract and type below. | Return type of copied; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_review_captures_bytes_and_rejects_changes | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_review_captures_bytes_and_rejects_changes | approved | Local binding for approved in test_review_captures_bytes_and_rejects_changes; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_review_captures_bytes_and_rejects_changes | original | Local binding for original in test_review_captures_bytes_and_rejects_changes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_unreviewable_packages_are_rejected | tmp_path | Parameter for tmp path in test_unreviewable_packages_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| test_unreviewable_packages_are_rejected | mutation | Parameter for mutation in test_unreviewable_packages_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| test_unreviewable_packages_are_rejected | folder | Local binding for folder in test_unreviewable_packages_are_rejected; use the enclosing contract and type below. | Return type of copied; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_unreviewable_packages_are_rejected | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_unreviewable_packages_are_rejected | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_symlink_package_member_is_rejected | tmp_path | Parameter for tmp path in test_symlink_package_member_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 64 |
| test_symlink_package_member_is_rejected | folder | Local binding for folder in test_symlink_package_member_is_rejected; use the enclosing contract and type below. | Return type of copied; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_symlink_package_member_is_rejected | member | Local binding for member in test_symlink_package_member_is_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_symlink_package_member_is_rejected | original | Local binding for original in test_symlink_package_member_is_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_strict_return_contract_rejects_bool_negative_and_extra_fields | validate_result | Imported dependency for validate result in test_strict_return_contract_rejects_bool_negative_and_extra_fields; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 80 |
| test_strict_return_contract_rejects_bool_negative_and_extra_fields | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 82 |
| test_strict_return_contract_rejects_bool_negative_and_extra_fields | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 88 |
| test_parent_rejects_application_tool_rpc_without_dispatch | tmp_path | Parameter for tmp path in test_parent_rejects_application_tool_rpc_without_dispatch; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_parent_rejects_application_tool_rpc_without_dispatch | ApplicationSession | Imported dependency for ApplicationSession in test_parent_rejects_application_tool_rpc_without_dispatch; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 99 |
| test_parent_rejects_application_tool_rpc_without_dispatch | folder | Local binding for folder in test_parent_rejects_application_tool_rpc_without_dispatch; use the enclosing contract and type below. | Return type of copied; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_parent_rejects_application_tool_rpc_without_dispatch | approved | Local binding for approved in test_parent_rejects_application_tool_rpc_without_dispatch; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_parent_rejects_application_tool_rpc_without_dispatch | session | Local binding for session in test_parent_rejects_application_tool_rpc_without_dispatch; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_application_cannot_exceed_manifest_lifetime | tmp_path | Parameter for tmp path in test_application_cannot_exceed_manifest_lifetime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 113 |
| test_application_cannot_exceed_manifest_lifetime | ApplicationSession | Imported dependency for ApplicationSession in test_application_cannot_exceed_manifest_lifetime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 115 |
| test_application_cannot_exceed_manifest_lifetime | folder | Local binding for folder in test_application_cannot_exceed_manifest_lifetime; use the enclosing contract and type below. | Return type of copied; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_application_cannot_exceed_manifest_lifetime | approved | Local binding for approved in test_application_cannot_exceed_manifest_lifetime; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_application_cannot_exceed_manifest_lifetime | session | Local binding for session in test_application_cannot_exceed_manifest_lifetime; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
