# Reference for src/agentix/ui/callback_compat.py

Intentional legacy combined callback facade; new shell uses separate backends.

Source fingerprint: 9a9639ca2c2f57cb2bc70934ab816051f23cfd4ee97290402d84d8c9bf732a24

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SessionCallbacks

Preserve prior imports while keeping sidebar implementations in their own module.

Kind: class. Declared return: Not declared / class. Source line: 7.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SidebarBackend | Imported dependency for SidebarBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | ToolsBackend | Imported dependency for ToolsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| SessionCallbacks | configure_model | Local binding for configure model in SessionCallbacks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 10 |
| SessionCallbacks | model_menu | Local binding for model menu in SessionCallbacks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 11 |
| SessionCallbacks | refresh_models | Local binding for refresh models in SessionCallbacks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 12 |
