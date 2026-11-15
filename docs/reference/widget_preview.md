# Reference for widget_preview.py

Preview an explicitly reviewed package through native Gradio and a maintained bridge.

Source fingerprint: eaf77a1ae2d41abf630b83bfa2add6993f0db4fad118376051ae11f911b8f92d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Require a review digest; never approve a package merely because it exists.

Kind: callable. Declared return: None. Source line: 14.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | configure_process | Imported dependency for configure process in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | approve_package | Imported dependency for approve package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | serve_widget | Imported dependency for serve widget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | WidgetSession | Imported dependency for WidgetSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | run_provisional_tests | Imported dependency for run provisional tests in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| main | approved | Local binding for approved in main; use the enclosing contract and type below. | Return type of approve_package; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| main | provisional | Local binding for provisional in main; use the enclosing contract and type below. | Return type of run_provisional_tests; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| main | session | Managed resource for session in main; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 28 |
| main.lambda_40 | item | Callback parameter for item in main.lambda_40; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 40 |
