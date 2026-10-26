# Reference for tests/unit/test_compatibility.py

Validate lazy legacy entrypoints against injected runtime boundaries.

Source fingerprint: 7b9f1ceedb1f78f7103d0a1b8566cfc0a0741cdac977910e4f21421830e339c9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_security_exception_is_exported_from_legacy_and_package_facades

Public exception re-exports must survive unused-import cleanup.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### test_legacy_workflow_calls_share_the_injected_runtime

Verify legacy workflow calls share the injected runtime.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_legacy_app_exports_callbacks_without_starting_server

Verify legacy app exports callbacks without starting server.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_unknown_compatibility_attribute_is_not_a_startup_request

Verify unknown compatibility attribute is not a startup request.

Kind: callable. Declared return: Not declared / class. Source line: 49.

### test_ui_startup_restores_stdout_on_launch_error

Verify ui startup restores stdout on launch error.

Kind: callable. Declared return: Not declared / class. Source line: 56.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | bootstrap | Imported dependency for bootstrap in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| test_security_exception_is_exported_from_legacy_and_package_facades | SecurityViolationError | Imported dependency for SecurityViolationError in test_security_exception_is_exported_from_legacy_and_package_facades; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 14 |
| test_security_exception_is_exported_from_legacy_and_package_facades | PackageError | Imported dependency for PackageError in test_security_exception_is_exported_from_legacy_and_package_facades; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 15 |
| test_security_exception_is_exported_from_legacy_and_package_facades | LegacyError | Imported dependency for LegacyError in test_security_exception_is_exported_from_legacy_and_package_facades; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| test_legacy_workflow_calls_share_the_injected_runtime | monkeypatch | Parameter for monkeypatch in test_legacy_workflow_calls_share_the_injected_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_legacy_workflow_calls_share_the_injected_runtime | entry | Local binding for entry in test_legacy_workflow_calls_share_the_injected_runtime; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_legacy_workflow_calls_share_the_injected_runtime | orchestrator | Local binding for orchestrator in test_legacy_workflow_calls_share_the_injected_runtime; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_legacy_workflow_calls_share_the_injected_runtime | orchestrator.run_system.return_value | Attribute for orchestrator.run system.return value in test_legacy_workflow_calls_share_the_injected_runtime; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| test_legacy_workflow_calls_share_the_injected_runtime | orchestrator.build_tool_pipeline.return_value | Attribute for orchestrator.build tool pipeline.return value in test_legacy_workflow_calls_share_the_injected_runtime; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| test_legacy_app_exports_callbacks_without_starting_server | monkeypatch | Parameter for monkeypatch in test_legacy_app_exports_callbacks_without_starting_server; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_legacy_app_exports_callbacks_without_starting_server | entry | Local binding for entry in test_legacy_app_exports_callbacks_without_starting_server; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_legacy_app_exports_callbacks_without_starting_server | controller | Local binding for controller in test_legacy_app_exports_callbacks_without_starting_server; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 41 |
| test_legacy_app_exports_callbacks_without_starting_server | view | Local binding for view in test_legacy_app_exports_callbacks_without_starting_server; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 41 |
| test_unknown_compatibility_attribute_is_not_a_startup_request | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| test_unknown_compatibility_attribute_is_not_a_startup_request | entry | Local binding for entry in test_unknown_compatibility_attribute_is_not_a_startup_request; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_ui_startup_restores_stdout_on_launch_error | monkeypatch | Parameter for monkeypatch in test_ui_startup_restores_stdout_on_launch_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| test_ui_startup_restores_stdout_on_launch_error | sys | Imported dependency for sys in test_ui_startup_restores_stdout_on_launch_error; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_ui_startup_restores_stdout_on_launch_error | controller | Local binding for controller in test_ui_startup_restores_stdout_on_launch_error; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_ui_startup_restores_stdout_on_launch_error | view_module | Local binding for view module in test_ui_startup_restores_stdout_on_launch_error; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_ui_startup_restores_stdout_on_launch_error | before | Local binding for before in test_ui_startup_restores_stdout_on_launch_error; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
