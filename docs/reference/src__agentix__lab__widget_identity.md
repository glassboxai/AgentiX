# Reference for src/agentix/lab/widget_identity.py

Canonical external tool identity and co-located widget artifact filenames.

The pilot exposes count_vowels_in_text while retaining count_vowels as the reviewed
implementation callable. The single definition is shared by host and native worker.

Source fingerprint: 77afcfd30d49cd2fd23997fe51297202f266f5e7aec24d19c105104ae4db635a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | TOOL_NAME | Module binding for TOOL NAME in module; use the enclosing contract and type below. | str | Module/process lifetime | 7 |
| module | FUNCTION_NAME | Module binding for FUNCTION NAME in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | WIDGET_FILENAME | Module binding for WIDGET FILENAME in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 9 |
| module | TOOL_FILENAME | Module binding for TOOL FILENAME in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 10 |
| module | TESTS_FILENAME | Module binding for TESTS FILENAME in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 11 |
| module | CONTRACT | Module binding for CONTRACT in module; use the enclosing contract and type below. | dict | Module/process lifetime | 12 |
