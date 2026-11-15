# Reference for src/agentix/decisions.py

Bounded fail-closed routing and creation decisions, independent of LLM libraries.

Source fingerprint: 459b07ad52012b49c9bd06ed5bb602e3d45eeea381934a21ec50c46dc9a7085d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### DecisionValidationError

Model output cannot safely authorize a routing or creation decision.

Kind: class. Declared return: Not declared / class. Source line: 9.

### CreateToolDecision

Validated exact creation action, portable name and nonblank purpose.

Kind: class. Declared return: Not declared / class. Source line: 14.

### RunApplicationDecision

A catalog-only opaque application ID and the supported typed data input.

Kind: class. Declared return: Not declared / class. Source line: 22.

### ApplicationSuggestion

A catalog-only recommendation that never authorizes application execution.

Kind: class. Declared return: Not declared / class. Source line: 30.

### _unique_fields

Reject duplicate fields instead of silently accepting the last value.

Kind: callable. Declared return: dict[str, Any]. Source line: 36.

### parse_manager_response

Accept ordinary answers or exact creation/application JSON contracts.

Creation-like, structured or fenced output must obey the full contract.
Names are never normalized into another identifier. Invalid output raises
an error without exposing the original response in logs or error text.

Kind: callable. Declared return: CreateToolDecision | RunApplicationDecision | str. Source line: 46.

### parse_application_suggestion

Parse a tool-free recommendation; only one exact catalog ID may be suggested.

The decision carries no arguments, so it cannot reach an execution path.
Prose, unknown IDs, duplicate keys, extra fields, several candidates and the
legacy ``RUN_APPLICATION`` shape all fail closed instead of degrading into an
execution or an implicit fallback.

Kind: callable. Declared return: ApplicationSuggestion | None. Source line: 101.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| CreateToolDecision | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 17 |
| CreateToolDecision | purpose | Typed binding for purpose in CreateToolDecision; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| RunApplicationDecision | app_id | Typed binding for app id in RunApplicationDecision; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 25 |
| RunApplicationDecision | arguments | Typed binding for arguments in RunApplicationDecision; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 26 |
| ApplicationSuggestion | app_id | Typed binding for app id in ApplicationSuggestion; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| _unique_fields | pairs | Parameter for pairs in _unique_fields; use the enclosing contract and type below. | list[tuple[str, Any]] | Enclosing invocation or class/instance lifetime | 36 |
| _unique_fields | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 38 |
| _unique_fields | key | Loop item for key in _unique_fields; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| _unique_fields | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| parse_manager_response | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 46 |
| parse_manager_response | text | Local binding for text in parse_manager_response; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 53, 64 |
| parse_manager_response | structured | Local binding for structured in parse_manager_response; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| parse_manager_response | answer | Local binding for answer in parse_manager_response; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| parse_manager_response | fenced | Local binding for fenced in parse_manager_response; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| parse_manager_response | data | Local binding for data in parse_manager_response; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| parse_manager_response | exc | Caught exception for exc in parse_manager_response; use the enclosing contract and type below. | (ValueError, RecursionError) | Current exception handler; Python clears this binding afterward | 67 |
| parse_manager_response | arguments | Local binding for arguments in parse_manager_response; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| parse_manager_response | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 87 |
| parse_manager_response | purpose | Local binding for purpose in parse_manager_response; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 87 |
| parse_application_suggestion | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 102 |
| parse_application_suggestion | catalog_ids | Parameter for catalog ids in parse_application_suggestion; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 102 |
| parse_application_suggestion | text | Local binding for text in parse_application_suggestion; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 113, 116 |
| parse_application_suggestion | fenced | Local binding for fenced in parse_application_suggestion; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| parse_application_suggestion | data | Local binding for data in parse_application_suggestion; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| parse_application_suggestion | error | Caught exception for error in parse_application_suggestion; use the enclosing contract and type below. | (ValueError, RecursionError) | Current exception handler; Python clears this binding afterward | 119 |
| parse_application_suggestion | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 127 |
