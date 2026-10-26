# Reference for src/agentix/decisions.py

Bounded fail-closed manager creation decisions, independent of LLM libraries.

Source fingerprint: 2faef8e005e13451b23531a7d0c206f8b15838d2db69c866b1f2717f19f60e35

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### DecisionValidationError

Manager output cannot safely authorize tool creation.

Kind: class. Declared return: Not declared / class. Source line: 9.

### CreateToolDecision

Validated exact creation action, portable name and nonblank purpose.

Kind: class. Declared return: Not declared / class. Source line: 14.

### _unique_fields

Reject duplicate fields instead of silently accepting the last value.

Kind: callable. Declared return: dict[str, Any]. Source line: 21.

### parse_manager_response

Accept ordinary answers or a complete exact creation JSON object.

Creation-like, structured or fenced output must obey the full contract.
Names are never normalized into another identifier. Invalid output raises
an error without exposing the original response in logs or error text.

Kind: callable. Declared return: CreateToolDecision | str. Source line: 31.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| CreateToolDecision | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 17 |
| CreateToolDecision | purpose | Typed binding for purpose in CreateToolDecision; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| _unique_fields | pairs | Parameter for pairs in _unique_fields; use the enclosing contract and type below. | list[tuple[str, Any]] | Enclosing invocation or class/instance lifetime | 21 |
| _unique_fields | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 23 |
| _unique_fields | key | Loop item for key in _unique_fields; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 24 |
| _unique_fields | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 24 |
| parse_manager_response | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 31 |
| parse_manager_response | text | Local binding for text in parse_manager_response; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 38, 49 |
| parse_manager_response | structured | Local binding for structured in parse_manager_response; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| parse_manager_response | answer | Local binding for answer in parse_manager_response; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| parse_manager_response | fenced | Local binding for fenced in parse_manager_response; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| parse_manager_response | data | Local binding for data in parse_manager_response; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| parse_manager_response | exc | Caught exception for exc in parse_manager_response; use the enclosing contract and type below. | (ValueError, RecursionError) | Current exception handler; Python clears this binding afterward | 52 |
| parse_manager_response | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 56 |
| parse_manager_response | purpose | Local binding for purpose in parse_manager_response; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 56 |
