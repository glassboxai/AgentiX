# Reference for src/agentix/sandbox_worker.py

Disposable child entrypoint; never imported to execute artifacts in the host.

All output is untrusted. Parent validates framing, schema and OS status. Tests
share this interpreter and can tamper with unittest; reports are not attestations.

Source fingerprint: d6ce9f20338db5d6a61552073836f4d2cd50ba1b451b472604f6e1ee2c89964f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Read a bounded parent-authored request and emit one JSON report on stdout.

Kind: callable. Declared return: None. Source line: 15.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | contextlib | Imported dependency for contextlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | unittest | Imported dependency for unittest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| main | folder | Local binding for folder in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 17 |
| main | request | Local binding for request in main; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| main | suite | Local binding for suite in main; use the enclosing contract and type below. | Return type of discover; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| main | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| main | report | Local binding for report in main; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 27, 47, 54, 56 |
| main | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| main | spec | Local binding for spec in main; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| main | module | Local binding for module in main; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| main | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| main | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| main | exc | Caught exception for exc in main; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 46 |
