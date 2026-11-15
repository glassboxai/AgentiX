# Reference for src/agentix/domain/application_names.py

Human application names and safe deterministic Windows directory names.

Source fingerprint: 405bf18ad07c9a9d07b35d589a1e044fed06fa352d7f06531dee84bc7125cab4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### application_folder

Validate a display name and derive a non-device ASCII folder name.

Paths, trailing punctuation, empty names and Windows devices are rejected.
The catalog reserves the derived folder without overwriting prior packages.

Kind: callable. Declared return: str. Source line: 20.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | unicodedata | Imported dependency for unicodedata in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | MAX_APPLICATION_NAME_LENGTH | Module binding for MAX APPLICATION NAME LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 7 |
| module | RESERVED_DEVICE_NAMES | Module binding for RESERVED DEVICE NAMES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 8 |
| comprehension_14 | i | Comprehension item for i in comprehension_14; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 14 |
| comprehension_15 | i | Comprehension item for i in comprehension_15; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 15 |
| application_folder | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 20 |
| application_folder.comprehension_32 | c | Comprehension item for c in application_folder.comprehension_32; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| application_folder | ascii_name | Local binding for ascii name in application_folder; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| application_folder | folder | Local binding for folder in application_folder; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
