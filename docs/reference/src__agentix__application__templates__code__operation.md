# Reference for src/agentix/application/templates/code/operation.py

Maintained native call recorder for reviewed generated connection code; no graph.

Source fingerprint: 33236ca5f1dfcdc988e2f60d87fe8171d2fa573b67047c9ad2551a835f59a66b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### execute

Execute generated Python once; bound approved calls and capture widget arguments.

This module is imported exclusively in the native worker. No agents, graph
interpretation or host RPC are used. Errors publish no partial outputs.

Kind: callable. Declared return: tuple[dict, dict]. Source line: 14.

### execute.call

Invoke one approved widget's tool once, recording actual arguments and result.

Kind: callable. Declared return: object. Source line: 27.

### analyze_text

Return complete observed results for the maintained native data entrypoint.

Kind: callable. Declared return: dict. Source line: 49.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | deepcopy | Imported dependency for deepcopy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | run | Imported dependency for run in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | validate_value | Imported dependency for validate value in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | MANIFEST | Module binding for MANIFEST in module; use the enclosing contract and type below. | Return type of loads; see its callable contract | Module/process lifetime | 11 |
| execute | payload | Parameter for payload in execute; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 14 |
| execute | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22 |
| execute | shape | Loop item for shape in execute; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22 |
| execute | widgets | Local binding for widgets in execute; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 24 |
| execute.comprehension_24 | widget | Comprehension item for widget in execute.comprehension_24; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| execute | results | Local binding for results in execute; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| execute | arguments | Local binding for arguments in execute; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 25 |
| execute.call | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 27 |
| execute.call | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | object | Enclosing invocation or class/instance lifetime | 27 |
| execute.call | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| execute.call | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 36 |
| execute.call | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 36 |
| execute.call | function | Local binding for function in execute.call; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| analyze_text | payload | Parameter for payload in analyze_text; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 49 |
