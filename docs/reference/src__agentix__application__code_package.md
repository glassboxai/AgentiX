# Reference for src/agentix/application/code_package.py

Version-3 package contracts for native generated connection code, without graphs.

Source fingerprint: 851f6eac53346e0c8c28c2bf72edd8cfa81bbf4bb404cb089dc478d5fa0e0c15

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### runtime_template

Select exact maintained native runtime bytes; no generated imports occur here.

Every version-3 member resolves inside this package so the connection-code
runtime no longer depends on legacy template paths or the lab package.

Kind: callable. Declared return: Path. Source line: 20.

### validate_manifest

Validate presentation/input contracts and exact dependency closure without edges.

Kind: callable. Declared return: set[str]. Source line: 31.

### validate_payload

Require every public application input, without numeric or string coercion.

Kind: callable. Declared return: dict. Source line: 88.

### validate_results

Validate every observed tool output against its exact approved return type.

Kind: callable. Declared return: dict. Source line: 97.

### validate_acceptance

Require host-held reviewed cases; never infer expected values from child code.

Kind: callable. Declared return: dict. Source line: 108.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | validate_value | Imported dependency for validate value in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ApplicationCode | Imported dependency for ApplicationCode in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | LOCK_PATH | Imported dependency for LOCK PATH in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SHARED | Module binding for SHARED in module; use the enclosing contract and type below. | set | Module/process lifetime | 11 |
| runtime_template | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 20 |
| validate_manifest | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 31 |
| validate_manifest | tools | Local binding for tools in validate_manifest; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| validate_manifest.comprehension_61 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 61 |
| validate_manifest.comprehension_72 | widget | Comprehension item for widget in validate_manifest.comprehension_72; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 72 |
| validate_manifest | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| validate_manifest.comprehension_77 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 79 |
| validate_manifest.comprehension_77 | suffix | Comprehension item for suffix in validate_manifest.comprehension_77; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| validate_payload | payload | Parameter for payload in validate_payload; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 88 |
| validate_payload | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 88 |
| validate_payload | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 92 |
| validate_payload | shape | Loop item for shape in validate_payload; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 92 |
| validate_results | results | Parameter for results in validate_results; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 97 |
| validate_results | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 97 |
| validate_results.comprehension_99 | widget | Comprehension item for widget in validate_results.comprehension_99; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 100 |
| validate_results | widget | Loop item for widget in validate_results; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 103 |
| validate_acceptance | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict | Enclosing invocation or class/instance lifetime | 108 |
| validate_acceptance | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 108 |
| validate_acceptance | error | Caught exception for error in validate_acceptance; use the enclosing contract and type below. | (ValueError, KeyError, TypeError) | Current exception handler; Python clears this binding afterward | 115 |
