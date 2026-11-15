# Reference for app.py

Legacy Gradio launch entrypoint; import alone never builds or starts a UI.

Source fingerprint: 7b2fe4a3b0277a0944044a0c1a718701290690c30b059fea639a68810a945e94

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### __getattr__

Lazily expose legacy callbacks and controller state for existing callers.

Kind: callable. Declared return: Any. Source line: 20.

### main

Launch the compatible loopback UI using explicit startup composition.

Kind: callable. Declared return: None. Source line: 30.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ANSI_ESCAPE | Imported dependency for ANSI ESCAPE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ExecutionState | Imported dependency for ExecutionState in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | format_thoughts_markdown | Imported dependency for format thoughts markdown in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | _CALLBACKS | Module binding for CALLBACKS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 9 |
| __getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 20 |
| __getattr__ | get_default_ui | Imported dependency for get default ui in __getattr__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 23 |
| __getattr__ | controller | Local binding for controller in __getattr__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| main | run_ui | Imported dependency for run ui in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
