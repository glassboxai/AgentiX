# Reference for tests/unit/test_storage_isolation_policy.py

v7 storage isolation: explicit configuration, no v5 fallback, no v5 namespace.

Every path here is a pytest temporary directory. The tests resolve configuration
only; they never create, publish, approve or migrate persistent artifacts.

Source fingerprint: a6a78e112508afbc7d5f1c228af0782ab6589980ab6cdc6900c43648def0a5b2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_missing_home_fails_with_actionable_error

No legacy profile is substituted when AGENTIX_HOME is absent.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_missing_tools_root_fails_with_actionable_error

The published Tools root is never derived from a default home.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_legacy_v5_roots_are_rejected

Resolved legacy namespaces fail closed before any storage access.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_unrelated_v5_substrings_are_accepted

Only whole legacy path segments are rejected, not incidental substrings.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_configured_v7_paths_resolve_as_established

The IaC variables resolve to the established v7 layout.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_legacy_home_is_rejected_by_settings

A v5 AGENTIX_HOME cannot configure a v7 runtime.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_legacy_tools_root_is_rejected_by_settings

A v5 published Tools root cannot be configured.

Kind: callable. Declared return: Not declared / class. Source line: 87.

### test_runtime_rejects_legacy_roots_from_direct_settings

Direct Settings construction cannot bypass the namespace guard.

Kind: callable. Declared return: Not declared / class. Source line: 99.

### test_default_security_manager_resolves_configured_tools_root

An unconfigured coordinator resolves AGENTIX_TOOLS_ROOT lazily.

Kind: callable. Declared return: Not declared / class. Source line: 117.

### test_default_security_manager_fails_closed_without_configuration

An unconfigured coordinator raises instead of adopting any fallback root.

Kind: callable. Declared return: Not declared / class. Source line: 128.

### test_import_without_configuration_stays_inert

Importing the package must not require deployment configuration.

Kind: callable. Declared return: Not declared / class. Source line: 139.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | require_v7_namespace | Imported dependency for require v7 namespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | user_home | Imported dependency for user home in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| test_missing_tools_root_fails_with_actionable_error | tmp_path | Parameter for tmp path in test_missing_tools_root_fails_with_actionable_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_legacy_v5_roots_are_rejected | legacy | Parameter for legacy in test_legacy_v5_roots_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_unrelated_v5_substrings_are_accepted | allowed | Parameter for allowed in test_unrelated_v5_substrings_are_accepted; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| test_configured_v7_paths_resolve_as_established | tmp_path | Parameter for tmp path in test_configured_v7_paths_resolve_as_established; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_configured_v7_paths_resolve_as_established | home | Local binding for home in test_configured_v7_paths_resolve_as_established; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_configured_v7_paths_resolve_as_established | tools | Local binding for tools in test_configured_v7_paths_resolve_as_established; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_configured_v7_paths_resolve_as_established | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_legacy_home_is_rejected_by_settings | tmp_path | Parameter for tmp path in test_legacy_home_is_rejected_by_settings; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_legacy_tools_root_is_rejected_by_settings | tmp_path | Parameter for tmp path in test_legacy_tools_root_is_rejected_by_settings; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_runtime_rejects_legacy_roots_from_direct_settings | tmp_path | Parameter for tmp path in test_runtime_rejects_legacy_roots_from_direct_settings; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 99 |
| test_runtime_rejects_legacy_roots_from_direct_settings | create_runtime | Imported dependency for create runtime in test_runtime_rejects_legacy_roots_from_direct_settings; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 101 |
| test_runtime_rejects_legacy_roots_from_direct_settings.lambda_111 | operations | Callback parameter for operations in test_runtime_rejects_legacy_roots_from_direct_settings.lambda_111; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 111 |
| test_runtime_rejects_legacy_roots_from_direct_settings.lambda_112 | model | Callback parameter for model in test_runtime_rejects_legacy_roots_from_direct_settings.lambda_112; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 112 |
| test_runtime_rejects_legacy_roots_from_direct_settings.lambda_112 | tools | Callback parameter for tools in test_runtime_rejects_legacy_roots_from_direct_settings.lambda_112; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 112 |
| test_default_security_manager_resolves_configured_tools_root | tmp_path | Parameter for tmp path in test_default_security_manager_resolves_configured_tools_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 117 |
| test_default_security_manager_resolves_configured_tools_root | monkeypatch | Parameter for monkeypatch in test_default_security_manager_resolves_configured_tools_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 117 |
| test_default_security_manager_resolves_configured_tools_root | SecurityManager | Imported dependency for SecurityManager in test_default_security_manager_resolves_configured_tools_root; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 119 |
| test_default_security_manager_resolves_configured_tools_root | tools | Local binding for tools in test_default_security_manager_resolves_configured_tools_root; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_default_security_manager_resolves_configured_tools_root | unconfigured | Local binding for unconfigured in test_default_security_manager_resolves_configured_tools_root; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_default_security_manager_fails_closed_without_configuration | monkeypatch | Parameter for monkeypatch in test_default_security_manager_fails_closed_without_configuration; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 128 |
| test_default_security_manager_fails_closed_without_configuration | SecurityManager | Imported dependency for SecurityManager in test_default_security_manager_fails_closed_without_configuration; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 130 |
| test_default_security_manager_fails_closed_without_configuration | unconfigured | Local binding for unconfigured in test_default_security_manager_fails_closed_without_configuration; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_import_without_configuration_stays_inert | tmp_path | Parameter for tmp path in test_import_without_configuration_stays_inert; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 139 |
| test_import_without_configuration_stays_inert | environment | Local binding for environment in test_import_without_configuration_stays_inert; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 141 |
| test_import_without_configuration_stays_inert.comprehension_141 | key | Comprehension item for key in test_import_without_configuration_stays_inert.comprehension_141; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 143 |
| test_import_without_configuration_stays_inert.comprehension_141 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 143 |
| test_import_without_configuration_stays_inert | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
