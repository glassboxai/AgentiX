# Reference for tests/conftest.py

Exercise real package services with explicit offline dependency wiring.

Only framework/LLM constructors and Gradio update payloads are substituted.
Artifact operations, storage, approval coordination, catalog and execution are
real; fixtures never access the project artifact directory.

Source fingerprint: 6332e638da62e47cb22be1319b760872822e12d7bd192ebcf2a0b72cb7be9519

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### agentix_file_handlers

Return the AgentiX rotating file handlers attached to ``logger``.

``logger`` defaults to the root logger. The returned list is a snapshot, so
callers may detach handlers while iterating it. Nothing is flushed, closed
or removed here; the caller owns that decision.

Kind: callable. Declared return: list[logging.Handler]. Source line: 30.

### release_agentix_file_handlers

Flush, close and detach owned handlers exactly once.

Handlers in ``keep`` stay attached and open, so a session can preserve
handlers that existed before it started. Each released handler is detached
before it is flushed, so no record can reach it afterwards, an object listed
twice is closed once, and an already closed handler is only detached again.
Returns the handlers this call closed, so a repeated call returns ``[]``.

Kind: callable. Declared return: list[logging.Handler]. Source line: 41.

### isolated_user_storage

Keep every test away from real v5 and v7 user storage.

Production now requires both variables, so tests must supply them. Explicit
per-test overrides still win because monkeypatch applies afterwards. The
resolved data root is validated against the pytest temporary root before any
test runs, and every AgentiX file handler created during the session is
flushed, closed and detached at teardown. Handlers that already existed are
preserved. Raises ``RuntimeError`` when a destination escapes the temporary
root, after the escaping handlers have been closed.

Kind: callable. Declared return: Not declared / class. Source line: 74.

### system

Compose isolated services; constructor wiring replaces import patching.

Kind: callable. Declared return: Not declared / class. Source line: 115.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | TrustedFixtureSandbox | Imported dependency for TrustedFixtureSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | security_module | Imported dependency for security module in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | build_agents | Imported dependency for build agents in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | Orchestrator | Imported dependency for Orchestrator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ExecutionState | Imported dependency for ExecutionState in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | format_thoughts_markdown | Imported dependency for format thoughts markdown in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| agentix_file_handlers | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | logging.Logger &#124; None | Enclosing invocation or class/instance lifetime | 30 |
| agentix_file_handlers | target | Local binding for target in agentix_file_handlers; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| agentix_file_handlers.comprehension_38 | handler | Comprehension item for handler in agentix_file_handlers.comprehension_38; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| release_agentix_file_handlers | handlers | Parameter for handlers in release_agentix_file_handlers; use the enclosing contract and type below. | list[logging.Handler] | Enclosing invocation or class/instance lifetime | 42 |
| release_agentix_file_handlers | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | logging.Logger &#124; None | Enclosing invocation or class/instance lifetime | 43 |
| release_agentix_file_handlers | keep | Parameter for keep in release_agentix_file_handlers; use the enclosing contract and type below. | tuple[logging.Handler, ...] &#124; list[logging.Handler] | Enclosing invocation or class/instance lifetime | 45 |
| release_agentix_file_handlers | target | Local binding for target in release_agentix_file_handlers; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 55 |
| release_agentix_file_handlers | retained | Local binding for retained in release_agentix_file_handlers; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 56 |
| release_agentix_file_handlers.comprehension_56 | handler | Comprehension item for handler in release_agentix_file_handlers.comprehension_56; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 56 |
| release_agentix_file_handlers | released | Typed binding for released in release_agentix_file_handlers; use the enclosing contract and type below. | list[logging.Handler] | Enclosing invocation or class/instance lifetime | 57 |
| release_agentix_file_handlers | seen | Typed binding for seen in release_agentix_file_handlers; use the enclosing contract and type below. | set[int] | Enclosing invocation or class/instance lifetime | 58 |
| release_agentix_file_handlers | handler | Loop item for handler in release_agentix_file_handlers; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 59 |
| release_agentix_file_handlers | identity | Explicit owner identity used by a session factory or fixture. | Return type of id; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| isolated_user_storage | tmp_path_factory | Parameter for tmp path factory in isolated_user_storage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| isolated_user_storage | root | Explicit root directory against which named paths are resolved. | Return type of mktemp; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| isolated_user_storage | authorized | Local binding for authorized in isolated_user_storage; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| isolated_user_storage | previous | Local binding for previous in isolated_user_storage; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 87 |
| isolated_user_storage.comprehension_87 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 87 |
| isolated_user_storage | resolved | Local binding for resolved in isolated_user_storage; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| isolated_user_storage | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| isolated_user_storage | preexisting | Local binding for preexisting in isolated_user_storage; use the enclosing contract and type below. | Return type of agentix_file_handlers; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| isolated_user_storage | escaped | Local binding for escaped in isolated_user_storage; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 98 |
| isolated_user_storage.comprehension_98 | handler | Comprehension item for handler in isolated_user_storage.comprehension_98; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 100 |
| isolated_user_storage.comprehension_98.comprehension_101 | item | Comprehension item for item in isolated_user_storage.comprehension_98.comprehension_101; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 101 |
| isolated_user_storage | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 105 |
| isolated_user_storage | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 105 |
| system | tmp_path | Parameter for tmp path in system; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| system | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| system | security | Owner-scoped approval and path boundary injected into this service. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| system | operations | Local binding for operations in system; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| system | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| system.comprehension_133 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 135 |
| system | registered | Local binding for registered in system; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| system.lambda_139 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 139 |
| system.lambda_139.lambda_139 | fn | Callback parameter for fn in system.lambda_139.lambda_139; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 139 |
| system | agents | Local binding for agents in system; use the enclosing contract and type below. | Return type of build_agents; see its callable contract | Enclosing invocation or class/instance lifetime | 140 |
| system | catalog | Local binding for catalog in system; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| system | orchestrator | Local binding for orchestrator in system; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| system | controller | Local binding for controller in system; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
