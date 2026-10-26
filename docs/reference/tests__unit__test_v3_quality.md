# Reference for tests/unit/test_v3_quality.py

V3-001 regressions for explicit policy, release identity and backend injection.

Source fingerprint: ca400c0ebbb55b4ce862c8d4bc90c7daa7b0a865f67f690aefe12078d05a75b3

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_explicit_startup_disables_gradio_analytics

Apply the same no-analytics policy to normal startup and test launchers.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_composition_injects_one_execution_boundary_into_all_services

Use a caller-provided boundary instead of constructing an implicit backend.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### test_release_identity_is_v3

Identify the curated release while retaining its public import package.

Kind: callable. Declared return: Not declared / class. Source line: 44.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| test_explicit_startup_disables_gradio_analytics | monkeypatch | Parameter for monkeypatch in test_explicit_startup_disables_gradio_analytics; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_explicit_startup_disables_gradio_analytics | configure_process | Imported dependency for configure process in test_explicit_startup_disables_gradio_analytics; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_composition_injects_one_execution_boundary_into_all_services | tmp_path | Parameter for tmp path in test_composition_injects_one_execution_boundary_into_all_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_composition_injects_one_execution_boundary_into_all_services | create_runtime | Imported dependency for create runtime in test_composition_injects_one_execution_boundary_into_all_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_composition_injects_one_execution_boundary_into_all_services | Settings | Imported dependency for Settings in test_composition_injects_one_execution_boundary_into_all_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_composition_injects_one_execution_boundary_into_all_services | agents | Local binding for agents in test_composition_injects_one_execution_boundary_into_all_services; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_composition_injects_one_execution_boundary_into_all_services | boundary | Local binding for boundary in test_composition_injects_one_execution_boundary_into_all_services; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_composition_injects_one_execution_boundary_into_all_services | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_composition_injects_one_execution_boundary_into_all_services.lambda_32 | operations | Callback parameter for operations in test_composition_injects_one_execution_boundary_into_all_services.lambda_32; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 32 |
| test_composition_injects_one_execution_boundary_into_all_services.lambda_33 | model | Callback parameter for model in test_composition_injects_one_execution_boundary_into_all_services.lambda_33; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 33 |
| test_composition_injects_one_execution_boundary_into_all_services.lambda_33 | tools | Callback parameter for tools in test_composition_injects_one_execution_boundary_into_all_services.lambda_33; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 33 |
| test_release_identity_is_v3 | __version__ | Imported dependency for version in test_release_identity_is_v3; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
