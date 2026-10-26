# Reference for tools/live_gui_review.py

Launch the real Agentix GUI with temporary storage for supervised model testing.

This is an opt-in operational harness, not an offline regression or a simulated
workflow. It uses real CrewAI, local Ollama and the native execution boundary.
No approvals are automated. Existing project-generated artifacts are never used.

Source fingerprint: 5f04b7a63f8950f490626b9e19013a8a3444197fdcfa65aa7a5d3c118ce4b1db

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Start a separate loopback UI and record its explicitly temporary storage.

The caller owns process lifetime. Temporary artifacts are retained for review;
this launcher never deletes existing directories or restarts another server.

Kind: callable. Declared return: None. Source line: 16.

### main.create

Compose actual agents/services for each browser, without fixture doubles.

Kind: callable. Declared return: UiController. Source line: 59.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| main | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 27 |
| main | configure_process | Imported dependency for configure process in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| main | create_runtime | Imported dependency for create runtime in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| main | activity_output | Imported dependency for activity output in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| main | Settings | Imported dependency for Settings in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
| main | launch_options | Imported dependency for launch options in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| main | UiController | Imported dependency for UiController in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 34 |
| main | SessionRegistry | Imported dependency for SessionRegistry in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 35 |
| main | build_view | Imported dependency for build view in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 36 |
| main | gr | Imported dependency for gr in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 39 |
| main | artifacts | Local binding for artifacts in main; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| main | settings | Immutable startup configuration; constructing it does not start external services. | Return type of Settings; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| main.create | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 59 |
| main.create | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| main.create | runtime.security.approval_timeout | Attribute for runtime.security.approval timeout in main.create; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 62 |
| main.create | controller | Local binding for controller in main.create; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| main.create | controller.state.session_id | Attribute for controller.state.session id in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| main | view | Local binding for view in main; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
