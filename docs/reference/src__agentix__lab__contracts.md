# Reference for src/agentix/lab/contracts.py

Strict immutable port, widget and workflow contracts for reviewed applications.

Only scalar text/count and bounded summary objects cross tool boundaries. Contract
validation runs before execution; arbitrary callables and filesystem paths are absent.

Source fingerprint: a5a81eb57adc40f3cef17d318edc41c56204415d1937c99f5dec1cae4e3f69c2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Contract

Forbid unknown fields and coercion; retain immutable contract identities.

Kind: class. Declared return: Not declared / class. Source line: 17.

### ToolDefinition

Reviewed maintained function and its required/optional typed input ports.

Kind: class. Declared return: Not declared / class. Source line: 23.

### WidgetDefinition

One widget instance; its ID namespaces controls independently of the tool.

Kind: class. Declared return: Not declared / class. Source line: 33.

### WidgetDefinition.elem_id

Return a stable instance/control selector without arbitrary DOM syntax.

Kind: callable. Declared return: str. Source line: 40.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Annotated | Imported dependency for Annotated in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Literal | Imported dependency for Literal in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | ConfigDict | Imported dependency for ConfigDict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Field | Imported dependency for Field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | PortType | Module binding for PortType in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 11 |
| module | Identifier | Module binding for Identifier in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 12 |
| module | Text | Module binding for Text in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 13 |
| module | Count | Module binding for Count in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| Contract | model_config | Local binding for model config in Contract; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| ToolDefinition | id | Typed binding for id in ToolDefinition; use the enclosing contract and type below. | Identifier | Enclosing invocation or class/instance lifetime | 26 |
| ToolDefinition | function | Typed binding for function in ToolDefinition; use the enclosing contract and type below. | Identifier | Enclosing invocation or class/instance lifetime | 27 |
| ToolDefinition | inputs | Typed binding for inputs in ToolDefinition; use the enclosing contract and type below. | dict[str, PortType] | Enclosing invocation or class/instance lifetime | 28 |
| ToolDefinition | optional | Typed binding for optional in ToolDefinition; use the enclosing contract and type below. | tuple[str, ...] | Enclosing invocation or class/instance lifetime | 29 |
| ToolDefinition | output | Typed binding for output in ToolDefinition; use the enclosing contract and type below. | PortType | Enclosing invocation or class/instance lifetime | 30 |
| WidgetDefinition | id | Typed binding for id in WidgetDefinition; use the enclosing contract and type below. | Identifier | Enclosing invocation or class/instance lifetime | 36 |
| WidgetDefinition | tool | Typed binding for tool in WidgetDefinition; use the enclosing contract and type below. | Identifier | Enclosing invocation or class/instance lifetime | 37 |
| WidgetDefinition | label | Typed binding for label in WidgetDefinition; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 38 |
| WidgetDefinition.elem_id | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| WidgetDefinition.elem_id | control | Parameter for control in WidgetDefinition.elem_id; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 40 |
