# Reference for tests/conftest.py

Exercise real package services with explicit offline dependency wiring.

Only framework/LLM constructors and Gradio update payloads are substituted.
Artifact operations, storage, approval coordination, catalog and execution are
real; fixtures never access the project artifact directory.

Source fingerprint: fd9daa7d99a8e57881f14947bb0ab6ef18c69a9de05b7078d8b59cfdc9de211e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### system

Compose isolated services; constructor wiring replaces import patching.

Kind: callable. Declared return: Not declared / class. Source line: 27.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | TrustedFixtureSandbox | Imported dependency for TrustedFixtureSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | security_module | Imported dependency for security module in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | build_agents | Imported dependency for build agents in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | Orchestrator | Imported dependency for Orchestrator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | format_thoughts_markdown | Imported dependency for format thoughts markdown in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | ExecutionState | Imported dependency for ExecutionState in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| system | tmp_path | Parameter for tmp path in system; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| system | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| system | security | Owner-scoped approval and path boundary injected into this service. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| system | operations | Local binding for operations in system; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| system | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| system.comprehension_45 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| system | registered | Local binding for registered in system; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| system.lambda_51 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 51 |
| system.lambda_51.lambda_51 | fn | Callback parameter for fn in system.lambda_51.lambda_51; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 51 |
| system | agents | Local binding for agents in system; use the enclosing contract and type below. | Return type of build_agents; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| system | catalog | Local binding for catalog in system; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| system | orchestrator | Local binding for orchestrator in system; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| system | controller | Local binding for controller in system; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
