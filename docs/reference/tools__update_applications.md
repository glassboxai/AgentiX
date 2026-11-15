# Reference for tools/update_applications.py

Stage or apply explicitly reviewed application runtime/dependency updates.

Source fingerprint: 57bfd6e20e5881f21606cbb50ca5934869ae34ad07898699a186a8f6b3a401cd

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Plan without installed writes, or apply one exact operator-reviewed plan.

Source/target paths must be explicit. No model calls, app renaming, generated
logic edits, case inference or current-grant overwrites are supported.

Kind: callable. Declared return: int. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | PROJECT | Module binding for PROJECT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 9 |
| module | WindowsDataProtection | Imported dependency for WindowsDataProtection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ApplicationUpdates | Imported dependency for ApplicationUpdates in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | CatalogMigration | Imported dependency for CatalogMigration in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | verify_application | Imported dependency for verify application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| main | migration | Local binding for migration in main; use the enclosing contract and type below. | Return type of CatalogMigration; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| main | service | Local binding for service in main; use the enclosing contract and type below. | Return type of ApplicationUpdates; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| main | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38 |
| main.comprehension_44 | item | Comprehension item for item in main.comprehension_44; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 44 |
