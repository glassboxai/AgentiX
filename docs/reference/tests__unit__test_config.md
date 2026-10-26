# Reference for tests/unit/test_config.py

Verify preserved configuration values through explicit, inert settings.

Source fingerprint: 2e659bb5104f4d3dffec39723769e1e2e7d826b8d453203ec9e036b75275047b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_configuration_defaults_and_overrides

Retain model/provider values while deferring construction until requested.

Kind: callable. Declared return: Not declared / class. Source line: 15.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ModuleType | Imported dependency for ModuleType in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | create_llm | Imported dependency for create llm in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| test_configuration_defaults_and_overrides | monkeypatch | Parameter for monkeypatch in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_configuration_defaults_and_overrides | model | Parameter for model in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_configuration_defaults_and_overrides | url | Parameter for url in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_configuration_defaults_and_overrides | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_configuration_defaults_and_overrides | values | Local binding for values in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 18 |
| test_configuration_defaults_and_overrides | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_configuration_defaults_and_overrides | crew | Local binding for crew in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | Return type of ModuleType; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_configuration_defaults_and_overrides | crew.LLM | Attribute for crew.LLM in test_configuration_defaults_and_overrides; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
