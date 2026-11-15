# Reference for src/agentix/lab/ipc_protocol.py

Bounded JSON framing and explicit HTTP route policy for the native widget bridge.

Source fingerprint: 17f2ebec379cc6bed4f858b0426c805e25915c899dd43bdd54dd69fe18e6a1a8

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _pairs

Reject duplicate JSON names rather than authorizing ambiguous requests.

Kind: callable. Declared return: dict. Source line: 12.

### _constant

Forbid JSON NaN and infinity across the process boundary.

Kind: callable. Declared return: None. Source line: 22.

### decode_frame

Decode one bounded object; no pickle, code or implicit deserialization.

Kind: callable. Declared return: dict. Source line: 27.

### encode_frame

Prefix strict JSON bytes with a little-endian unsigned payload length.

Kind: callable. Declared return: bytes. Source line: 40.

### validate_http_request

Expose required Gradio endpoints, excluding arbitrary file/proxy/upload routes.

Kind: callable. Declared return: None. Source line: 50.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | struct | Imported dependency for struct in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | unquote | Imported dependency for unquote in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | MAX_FRAME | Module binding for MAX FRAME in module; use the enclosing contract and type below. | int | Module/process lifetime | 8 |
| module | MAX_BODY | Module binding for MAX BODY in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| _pairs | pairs | Parameter for pairs in _pairs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 12 |
| _pairs | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 14 |
| _pairs | key | Loop item for key in _pairs; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 15 |
| _pairs | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 15 |
| _constant | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 22 |
| decode_frame | payload | Parameter for payload in decode_frame; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 27 |
| decode_frame | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| decode_frame | error | Caught exception for error in decode_frame; use the enclosing contract and type below. | (RecursionError, UnicodeError) | Current exception handler; Python clears this binding afterward | 33 |
| encode_frame | message | Parameter for message in encode_frame; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 40 |
| encode_frame | payload | Local binding for payload in encode_frame; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| encode_frame | error | Caught exception for error in encode_frame; use the enclosing contract and type below. | (TypeError, RecursionError) | Current exception handler; Python clears this binding afterward | 44 |
| validate_http_request | method | Parameter for method in validate_http_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 50 |
| validate_http_request | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 50 |
| validate_http_request | body | Parameter for body in validate_http_request; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 50 |
| validate_http_request | decoded | Local binding for decoded in validate_http_request; use the enclosing contract and type below. | Return type of unquote; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| validate_http_request | fixed | Local binding for fixed in validate_http_request; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 61 |
| validate_http_request | assets | Local binding for assets in validate_http_request; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| validate_http_request | events | Local binding for events in validate_http_request; use the enclosing contract and type below. | Return type of fullmatch; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
