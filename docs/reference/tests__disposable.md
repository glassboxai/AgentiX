# Reference for tests/disposable.py

Explicit ownership cleanup for disposable browser-test process trees only.

Source fingerprint: d38dba56457885a433d4ad64a611b867ea9356968bf89d5c46fb3c76afc8a045

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### stop_process_tree

Stop the exact Popen-owned test tree; never discover or terminate live apps.

Kind: callable. Declared return: None. Source line: 7.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| stop_process_tree | process | Parameter for process in stop_process_tree; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
