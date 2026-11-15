# Reference for src/agentix/domain/tool_schema.py

Static canonical tool contracts; source and annotation expressions never execute.

Source fingerprint: 7b776548c44c2537a8545323b3c82c74dbaeb0a99d19de09402d4d8d70cf1833

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _shape

Translate the bounded JSON annotation vocabulary, rejecting unknown Python.

Kind: callable. Declared return: dict. Source line: 16.

### _annotated

Require Annotated with a nonempty English description string or Field metadata.

Kind: callable. Declared return: dict. Source line: 48.

### extract_tool_schema

Return a canonical JSON contract; raise ValueError for unsupported/ambiguous APIs.

Exactly one public top-level function is allowed, named after its package.
Private helpers are permitted. Defaults must be JSON literals; varargs,
positional-only parameters and async entrypoints are deliberately unsupported.

Kind: callable. Declared return: dict. Source line: 76.

### validate_value

Check bounded JSON values without coercing booleans to numeric values.

Kind: callable. Declared return: Any. Source line: 135.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | TOOL_NAME_PATTERN | Module binding for TOOL NAME PATTERN in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | MAX_TOOL_SOURCE_BYTES | Module binding for MAX TOOL SOURCE BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | MAX_PARAMETER_DESCRIPTION_LENGTH | Module binding for MAX PARAMETER DESCRIPTION LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | MAX_TOOL_PARAMETERS | Module binding for MAX TOOL PARAMETERS in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | MAX_TOOL_MEANING_LENGTH | Module binding for MAX TOOL MEANING LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 12 |
| module | MAX_TEXT_VALUE_LENGTH | Module binding for MAX TEXT VALUE LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| _shape | node | Parameter for node in _shape; use the enclosing contract and type below. | ast.expr | Enclosing invocation or class/instance lifetime | 16 |
| _shape | values | Local binding for values in _shape; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| _shape | literals | Local binding for literals in _shape; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 36 |
| _shape.comprehension_36 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 36 |
| _shape.comprehension_37 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| _shape.comprehension_39 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| _annotated | node | Parameter for node in _annotated; use the enclosing contract and type below. | ast.expr &#124; None | Enclosing invocation or class/instance lifetime | 48 |
| _annotated | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| _annotated | description | Local binding for description in _annotated; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 55, 58, 66 |
| _annotated | meta | Loop item for meta in _annotated; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 56 |
| _annotated | kw | Loop item for kw in _annotated; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 64 |
| extract_tool_schema | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 76 |
| extract_tool_schema | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 76 |
| extract_tool_schema | tree | Local binding for tree in extract_tool_schema; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| extract_tool_schema | public | Local binding for public in extract_tool_schema; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 93 |
| extract_tool_schema.comprehension_93 | node | Comprehension item for node in extract_tool_schema.comprehension_93; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 95 |
| extract_tool_schema | fn | Local binding for fn in extract_tool_schema; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| extract_tool_schema | params | Local binding for params in extract_tool_schema; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 104 |
| extract_tool_schema.comprehension_104 | arg | Comprehension item for arg in extract_tool_schema.comprehension_104; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 104 |
| extract_tool_schema | defaults | Local binding for defaults in extract_tool_schema; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 107 |
| extract_tool_schema | pairs | Local binding for pairs in extract_tool_schema; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 108, 113 |
| extract_tool_schema.comprehension_113 | arg | Comprehension item for arg in extract_tool_schema.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 115 |
| extract_tool_schema.comprehension_113 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 115 |
| extract_tool_schema | arg | Loop item for arg in extract_tool_schema; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 118 |
| extract_tool_schema | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 118 |
| extract_tool_schema | literal | Local binding for literal in extract_tool_schema; use the enclosing contract and type below. | Return type of literal_eval; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| extract_tool_schema | description | Local binding for description in extract_tool_schema; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 122 |
| validate_value | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 135 |
| validate_value | shape | Parameter for shape in validate_value; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 135 |
| validate_value | validate_json | Imported dependency for validate json in validate_value; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 137 |
| validate_value | kind | Local binding for kind in validate_value; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 144 |
| validate_value | valid | Local binding for valid in validate_value; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| validate_value | item | Loop item for item in validate_value; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 155 |
