# Reference for src/agentix/lab/widget_runtime.py

Stage only installed pinned Gradio distributions into a private native runtime.

No project tool directory or user data is enumerated. Files must resolve inside the
selected environment's site-packages; .pth files are copied as data, never processed.

Source fingerprint: 401e17cfe3e65643e8ecdecc4646a2e37944fda2e5a05bbef0b6a5a7ae657ef5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### stage_runtime

Copy CPython and the Gradio dependency closure after exact lock-version checks.

Kind: callable. Declared return: None. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | metadata | Imported dependency for metadata in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Requirement | Imported dependency for Requirement in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | canonicalize_name | Imported dependency for canonicalize name in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| stage_runtime | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 19 |
| stage_runtime | lock | Local binding for lock in stage_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| stage_runtime | pins | Local binding for pins in stage_runtime; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 23 |
| stage_runtime.comprehension_23 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 25 |
| stage_runtime.comprehension_23 | version | Comprehension item for version in stage_runtime.comprehension_23; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 25 |
| stage_runtime | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | tuple | Enclosing invocation or class/instance lifetime | 29 |
| stage_runtime | visited | Local binding for visited in stage_runtime; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 29 |
| stage_runtime | site | Local binding for site in stage_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| stage_runtime | boundary | Local binding for boundary in stage_runtime; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| stage_runtime | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of canonicalize_name; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| stage_runtime | distribution | Local binding for distribution in stage_runtime; use the enclosing contract and type below. | Return type of distribution; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| stage_runtime | item | Loop item for item in stage_runtime; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 41 |
| stage_runtime | source | Explicit source document or source-code text; never imported for reference generation. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| stage_runtime | destination | Local binding for destination in stage_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| stage_runtime | raw | Loop item for raw in stage_runtime; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 54 |
| stage_runtime | requirement | Local binding for requirement in stage_runtime; use the enclosing contract and type below. | Return type of Requirement; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
