# Reference for tests/test_application_catalog.py

Approved catalog dependency regressions; use trusted temporary source only.

Source fingerprint: 2061ab8fdf6fdc3ee8526a1bcd1c2314b880d57b691e0210ef67915bc5f50f06

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### installed

Publish explicit host-boundary fixture grants, without model/test execution.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### registry

Resolve the production registry only after the test module can collect.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### test_exact_installed_approved_bytes_are_reused_without_running_tests

Catch substitution of internal examples for installed source or test execution.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected

Both catalog membership and a current owner-bound approval are mandatory.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_recheck_detects_revocation_after_packaging

A package snapshot alone must not retain a revoked installed-tool grant.

Kind: callable. Declared return: Not declared / class. Source line: 85.

### test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied

Reject before inference rather than silently using a fixed example package.

Kind: callable. Declared return: Not declared / class. Source line: 96.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SOURCES | Module binding for SOURCES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 11 |
| installed | tmp_path | Parameter for tmp path in installed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| installed | owner_id | Session owner identity used to prevent cross-session authorization. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| installed | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| installed | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in installed; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| installed | ledger | Local binding for ledger in installed; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| installed | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22 |
| installed | code | Source snapshot passed through approval, syntax checks and isolated staging. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22 |
| installed | folder | Local binding for folder in installed; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 23 |
| installed | function | Local binding for function in installed; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 27 |
| registry | fixture | Parameter for fixture in registry; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| registry | ApprovedToolRegistry | Imported dependency for ApprovedToolRegistry in registry; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| test_exact_installed_approved_bytes_are_reused_without_running_tests | tmp_path | Parameter for tmp path in test_exact_installed_approved_bytes_are_reused_without_running_tests; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_exact_installed_approved_bytes_are_reused_without_running_tests | fixture | Local binding for fixture in test_exact_installed_approved_bytes_are_reused_without_running_tests; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_exact_installed_approved_bytes_are_reused_without_running_tests | tools | Local binding for tools in test_exact_installed_approved_bytes_are_reused_without_running_tests; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected | tmp_path | Parameter for tmp path in test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected | failure | Parameter for failure in test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected | fixture | Local binding for fixture in test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 72 |
| test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected | fixture.catalog | Attribute for fixture.catalog in test_missing_unapproved_drifted_or_foreign_catalog_tool_is_rejected; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_recheck_detects_revocation_after_packaging | tmp_path | Parameter for tmp path in test_recheck_detects_revocation_after_packaging; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| test_recheck_detects_revocation_after_packaging | fixture | Local binding for fixture in test_recheck_detects_revocation_after_packaging; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_recheck_detects_revocation_after_packaging | service | Local binding for service in test_recheck_detects_revocation_after_packaging; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_recheck_detects_revocation_after_packaging | tools | Local binding for tools in test_recheck_detects_revocation_after_packaging; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied | tmp_path | Parameter for tmp path in test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied | ApplicationPipeline | Imported dependency for ApplicationPipeline in test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied | calls | Local binding for calls in test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 100 |
| test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied | pipeline | Local binding for pipeline in test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied; use the enclosing contract and type below. | Return type of ApplicationPipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied.lambda_101 | folder | Callback parameter for folder in test_pipeline_never_uses_internal_tools_when_no_approved_catalog_is_supplied.lambda_101; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 101 |
