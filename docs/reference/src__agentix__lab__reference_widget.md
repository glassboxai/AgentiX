# Reference for src/agentix/lab/reference_widget.py

Maintained reference widget for native feasibility tests, not LLM evidence.

Source fingerprint: 3699449f2f6561b28cec99536c8235e15a008a97e2a27df993565236b93b5f75

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### create_widget

Build one isolated instance and bind only its injected approved tool callback.

Kind: callable. Declared return: Not declared / class. Source line: 6.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | gr | Imported dependency for gr in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| create_widget | context | Parameter for context in create_widget; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| create_widget | text | Local binding for text in create_widget; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| create_widget | output | Local binding for output in create_widget; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| create_widget | button | Local binding for button in create_widget; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
