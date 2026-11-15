# Reference for src/agentix/domain/application_code.py

Bounded generated connection-code contracts; host validation never executes source.

Source fingerprint: 3d87aa6c51825e0607d80dd02ca642565dcd3ea2eebfc303c90dd4f6952cff75

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ApplicationContractError

Name a rejected public-input key without carrying model or user payload.

The message is built only from the input identity and the closed key list, so
it is safe for the owner-facing status line and the payload-free event log.

Kind: class. Declared return: Not declared / class. Source line: 27.

### unsupported_input_keys

Return the sorted keys a public input schema may not declare.

Kind: callable. Declared return: list[str]. Source line: 35.

### WidgetInstance

Describe a presentation instance and its approved tool, without connectivity.

Kind: class. Declared return: Not declared / class. Source line: 42.

### ApplicationCode

Hold generated Python, public input schemas and the finite widget inventory.

Kind: class. Declared return: Not declared / class. Source line: 50.

### ApplicationCode.validate_catalog

Reject unknown dependencies, invalid input shapes and unsafe source structure.

This is a syntax/contract filter, not isolation or a semantic proof. The
returned source stays inert until exact-byte review and native execution.

Kind: callable. Declared return: dict. Source line: 59.

### validate_input_shape

Accept only scalar/array JSON shapes supported by strict tool validation.

Kind: callable. Declared return: None. Source line: 82.

### validate_connection_source

Compile but never import bounded source; reject module-level work and entry drift.

Kind: callable. Declared return: None. Source line: 115.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ConfigDict | Imported dependency for ConfigDict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Field | Imported dependency for Field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | validate_source | Imported dependency for validate source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | validate_value | Imported dependency for validate value in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | IDENTIFIER | Module binding for IDENTIFIER in module; use the enclosing contract and type below. | str | Module/process lifetime | 11 |
| module | MAX_APPLICATION_INPUTS | Module binding for MAX APPLICATION INPUTS in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| module | MAX_APPLICATION_WIDGETS | Module binding for MAX APPLICATION WIDGETS in module; use the enclosing contract and type below. | int | Module/process lifetime | 14 |
| module | MAX_CONNECTION_CODE_LENGTH | Module binding for MAX CONNECTION CODE LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 15 |
| module | MAX_NOTES_LENGTH | Module binding for MAX NOTES LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 16 |
| module | MAX_INPUT_DESCRIPTION_LENGTH | Module binding for MAX INPUT DESCRIPTION LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 18 |
| module | MAX_ENUM_VALUES | Module binding for MAX ENUM VALUES in module; use the enclosing contract and type below. | int | Module/process lifetime | 19 |
| module | ENTRY_FUNCTION_NAME | Module binding for ENTRY FUNCTION NAME in module; use the enclosing contract and type below. | str | Module/process lifetime | 21 |
| module | ENTRY_ARGUMENTS | Module binding for ENTRY ARGUMENTS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 22 |
| module | INPUT_SHAPE_KEYS | Module binding for INPUT SHAPE KEYS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 24 |
| unsupported_input_keys | shape | Parameter for shape in unsupported_input_keys; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 35 |
| unsupported_input_keys.comprehension_39 | key | Comprehension item for key in unsupported_input_keys.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| WidgetInstance | model_config | Local binding for model config in WidgetInstance; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| WidgetInstance | id | Typed binding for id in WidgetInstance; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 46 |
| WidgetInstance | tool | Typed binding for tool in WidgetInstance; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 47 |
| ApplicationCode | model_config | Local binding for model config in ApplicationCode; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| ApplicationCode | inputs | Typed binding for inputs in ApplicationCode; use the enclosing contract and type below. | dict[str, dict[str, Any]] | Enclosing invocation or class/instance lifetime | 54 |
| ApplicationCode | widgets | Typed binding for widgets in ApplicationCode; use the enclosing contract and type below. | list[WidgetInstance] | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationCode | connection_code | Typed binding for connection code in ApplicationCode; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| ApplicationCode | notes | Typed binding for notes in ApplicationCode; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 57 |
| ApplicationCode.validate_catalog | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| ApplicationCode.validate_catalog | schemas | Parameter for schemas in ApplicationCode.validate_catalog; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 59 |
| ApplicationCode.validate_catalog | re | Imported dependency for re in ApplicationCode.validate_catalog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 65 |
| ApplicationCode.validate_catalog.comprehension_67 | widget | Comprehension item for widget in ApplicationCode.validate_catalog.comprehension_67; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 67, 68 |
| ApplicationCode.validate_catalog | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 71 |
| ApplicationCode.validate_catalog | shape | Loop item for shape in ApplicationCode.validate_catalog; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 71 |
| ApplicationCode.validate_catalog | error | Caught exception for error in ApplicationCode.validate_catalog; use the enclosing contract and type below. | ApplicationContractError | Current exception handler; Python clears this binding afterward | 76 |
| validate_input_shape | shape | Parameter for shape in validate_input_shape; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 82 |
| validate_input_shape | rejected | Local binding for rejected in validate_input_shape; use the enclosing contract and type below. | Return type of unsupported_input_keys; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| validate_input_shape | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 111 |
| validate_input_shape.comprehension_112 | key | Comprehension item for key in validate_input_shape.comprehension_112; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 112 |
| validate_input_shape.comprehension_112 | item | Comprehension item for item in validate_input_shape.comprehension_112; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 112 |
| validate_connection_source | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 115 |
| validate_connection_source | tree | Local binding for tree in validate_connection_source; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| validate_connection_source | statement | Loop item for statement in validate_connection_source; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 119 |
| validate_connection_source | entry | Local binding for entry in validate_connection_source; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| validate_connection_source.comprehension_137 | statement | Comprehension item for statement in validate_connection_source.comprehension_137; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| validate_connection_source.comprehension_143 | argument | Comprehension item for argument in validate_connection_source.comprehension_143; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 143 |
