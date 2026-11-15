# Reference for config.py

Legacy configuration constants with lazy model construction.

Importing constants is inert; accessing local_llm explicitly initializes the
existing provider. New code should use Settings and the composition root.

Source fingerprint: 91d39cb731e5b7e2077abb686fb592db2c80b1c09e884dbc56e26973e340dc6c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### __getattr__

Resolve deployment-dependent values only when specifically requested.

Kind: callable. Declared return: Any. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | BASE_DIR | Module binding for BASE DIR in module; use the enclosing contract and type below. | Return type of str; see its callable contract | Module/process lifetime | 13 |
| module | OLLAMA_MODEL | Module binding for OLLAMA MODEL in module; use the enclosing contract and type below. | str | Module/process lifetime | 14 |
| module | OLLAMA_BASE_URL | Module binding for OLLAMA BASE URL in module; use the enclosing contract and type below. | str | Module/process lifetime | 15 |
| __getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 18 |
| __getattr__ | get_default_llm | Imported dependency for get default llm in __getattr__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 21 |
