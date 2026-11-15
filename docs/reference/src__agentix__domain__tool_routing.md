# Reference for src/agentix/domain/tool_routing.py

Strict data-only tool routing and acceptance proposal contracts.

Source fingerprint: 08935e35797771ebad379c944779a2f8a5f671c8443b0718bb574cc2552cb32c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ArgumentPair

One named tool argument as a closed object instead of an open key map.

Kind: class. Declared return: Not declared / class. Source line: 20.

### ToolRoute

A selection is data, never authority to call or approve the selected tool.

Kind: class. Declared return: Not declared / class. Source line: 28.

### CreateRoute

Creation proposes a capability, never arguments or executable API metadata.

Kind: class. Declared return: Not declared / class. Source line: 38.

### ReuseRoute

Reuse arguments are checked against the exact selected tool schema.

Kind: class. Declared return: Not declared / class. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Literal | Imported dependency for Literal in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ConfigDict | Imported dependency for ConfigDict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Field | Imported dependency for Field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | IDENTIFIER_PATTERN | Module binding for IDENTIFIER PATTERN in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | MAX_PURPOSE_LENGTH | Module binding for MAX PURPOSE LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | MAX_ARGUMENTS | Module binding for MAX ARGUMENTS in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | JsonScalar | Module binding for JsonScalar in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| module | JsonArgument | Module binding for JsonArgument in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| ArgumentPair | model_config | Local binding for model config in ArgumentPair; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| ArgumentPair | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 24 |
| ArgumentPair | value | Value at the current validation/rendering boundary; apply the enclosing contract. | JsonArgument | Enclosing invocation or class/instance lifetime | 25 |
| ToolRoute | model_config | Local binding for model config in ToolRoute; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| ToolRoute | action | Typed binding for action in ToolRoute; use the enclosing contract and type below. | Literal['CREATE_TOOL', 'REUSE_TOOL'] | Enclosing invocation or class/instance lifetime | 32 |
| ToolRoute | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 33 |
| ToolRoute | purpose | Typed binding for purpose in ToolRoute; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| ToolRoute | arguments | Typed binding for arguments in ToolRoute; use the enclosing contract and type below. | list[ArgumentPair] | Enclosing invocation or class/instance lifetime | 35 |
| CreateRoute | model_config | Local binding for model config in CreateRoute; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| CreateRoute | action | Typed binding for action in CreateRoute; use the enclosing contract and type below. | Literal['CREATE_TOOL'] | Enclosing invocation or class/instance lifetime | 42 |
| CreateRoute | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 43 |
| CreateRoute | purpose | Typed binding for purpose in CreateRoute; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| ReuseRoute | action | Typed binding for action in ReuseRoute; use the enclosing contract and type below. | Literal['REUSE_TOOL'] | Enclosing invocation or class/instance lifetime | 50 |
