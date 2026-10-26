# Reference for config.py

Legacy configuration constants with lazy model construction.

Importing constants is inert; accessing local_llm explicitly initializes the
existing provider. New code should use Settings and the composition root.

Source fingerprint: 936baa272919cddc44de2a8a79c542b1f0e1fae22ee65cb43221d7680ea33cc0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### __getattr__

Resolve the former eager local_llm only when specifically requested.

Kind: callable. Declared return: Any. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | _settings | Module binding for settings in module; use the enclosing contract and type below. | Return type of from_environment; see its callable contract | Module/process lifetime | 12 |
| module | BASE_DIR | Module binding for BASE DIR in module; use the enclosing contract and type below. | Return type of str; see its callable contract | Module/process lifetime | 13 |
| module | TOOLS_ROOT_DIR | Module binding for TOOLS ROOT DIR in module; use the enclosing contract and type below. | Return type of str; see its callable contract | Module/process lifetime | 14 |
| module | OLLAMA_MODEL | Module binding for OLLAMA MODEL in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| module | OLLAMA_BASE_URL | Module binding for OLLAMA BASE URL in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| __getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 19 |
| __getattr__ | get_default_llm | Imported dependency for get default llm in __getattr__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 22 |
