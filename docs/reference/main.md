# Reference for main.py

Legacy CLI and workflow entrypoints backed by explicit package services.

Source fingerprint: 7f6adc2d30fdb440a8a593f3bb6830f06391b47b68cd39c17c000d50d8622308

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### __getattr__

Retain legacy agent/factory access without eager framework initialization.

Kind: callable. Declared return: Any. Source line: 11.

### get_installed_tools_catalog

Inspect the configured catalog on demand, without constructing agents.

Kind: callable. Declared return: str. Source line: 28.

### build_tool_pipeline

Start the original creation pipeline through the lazy default runtime.

Kind: callable. Declared return: Any. Source line: 33.

### run_system

Process one query using the existing manager decision semantics.

Kind: callable. Declared return: str. Source line: 40.

### main

Start the interactive command-line loop.

Kind: callable. Declared return: None. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SECURITY_GUARDRAILS | Imported dependency for SECURITY GUARDRAILS in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| __getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 11 |
| __getattr__ | get_default_runtime | Imported dependency for get default runtime in __getattr__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 22 |
| build_tool_pipeline | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 33 |
| build_tool_pipeline | user_requirement | Parameter for user requirement in build_tool_pipeline; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| build_tool_pipeline | get_default_runtime | Imported dependency for get default runtime in build_tool_pipeline; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 35 |
| run_system | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 40 |
| run_system | get_default_runtime | Imported dependency for get default runtime in run_system; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| main | run_cli | Imported dependency for run cli in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
