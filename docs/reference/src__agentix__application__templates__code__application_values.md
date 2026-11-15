# Reference for src/agentix/application/templates/code/application_values.py

Portable strict value validation shared by host contracts and the native code runtime.

Source fingerprint: b2696747d1b37c9f11a489c7f56c9fb83dabf4d10eefb254d07a1e0ac8544bd7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### validate_value

Validate bounded finite JSON scalar/array values without coercion or side effects.

Kind: callable. Declared return: object. Source line: 6.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| validate_value | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 6 |
| validate_value | shape | Parameter for shape in validate_value; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 6 |
| validate_value | kind | Local binding for kind in validate_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 8 |
| validate_value | valid | Local binding for valid in validate_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| validate_value | item | Loop item for item in validate_value; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 23 |
