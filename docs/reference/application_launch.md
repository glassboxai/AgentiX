# Reference for application_launch.py

Launch a reviewed composite application independently of any laboratory view.

The maintained supervisor enforces native isolation; app.py is never imported here.
Explicit review bytes are required. Standalone mode denies framing by other pages.

Source fingerprint: c699e782fc3360b5af726d62e65b939cba15b0d4976bdce2e5c33c091a3ded54

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Validate the package and start only its owned loopback listener/native job.

Kind: callable. Declared return: None. Source line: 21.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | _agentix_path | Imported dependency for agentix path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | configure_process | Imported dependency for configure process in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApplicationPreview | Imported dependency for ApplicationPreview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | reviewed_application | Imported dependency for reviewed application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | execute_application | Imported dependency for execute application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| main | approved | Local binding for approved in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| main | preview | Local binding for preview in main; use the enclosing contract and type below. | Return type of ApplicationPreview; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
