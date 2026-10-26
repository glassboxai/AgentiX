# Reference for _agentix_path.py

Allow legacy checkout entrypoints to locate the src-layout package.

Installed applications resolve agentix normally; a checkout needs only its local
src directory added to Python's module path, without runtime initialization.

Source fingerprint: 91fe3463ed3d14d74ee19294c8db9f3df027701227223e37d64a33a188349499

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | source_directory | Module binding for source directory in module; use the enclosing contract and type below. | Return type of str; see its callable contract | Module/process lifetime | 10 |
