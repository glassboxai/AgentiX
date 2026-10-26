# Reference for tests/integration/test_verbose_activity_framework.py

Real CrewAI verbose events must reach only their owning GUI conversation.

Source fingerprint: 9e69efee4d8a86a9a28003143de69076604db801f4e048e1a1eee8789d02771a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_real_verbose_messages_and_diagnostics_reach_separate_controllers

Use the SDK event renderer and workers, without a model or HTTP server.

Kind: callable. Declared return: Not declared / class. Source line: 11.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_real_verbose_messages_and_diagnostics_reach_separate_controllers | script | Local binding for script in test_real_verbose_messages_and_diagnostics_reach_separate_controllers; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 13 |
| test_real_verbose_messages_and_diagnostics_reach_separate_controllers | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
