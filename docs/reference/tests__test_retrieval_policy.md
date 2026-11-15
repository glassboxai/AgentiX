# Reference for tests/test_retrieval_policy.py

Characterize retrieval policy boundaries independently of production constants.

Literal expectations intentionally pin the approved contract. Do not derive them
from the implementation's constants: that would hide accidental policy changes.

Source fingerprint: 251d8b0e6b4f002e197c5ac1fa4ce8b013d2a726b498aa41e8998d552c82b6b7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_keyword_limits_and_generation_contract

Keep the twenty-term, hundred-character contract in validation and generation.

Kind: callable. Declared return: None. Source line: 19.

### test_keyword_limits_and_generation_contract.CapturedClient

Capture generation payload data without contacting Ollama.

Kind: class. Declared return: Not declared / class. Source line: 28.

### test_keyword_limits_and_generation_contract.CapturedClient.post

Return a valid keyword response and retain the request contract.

Kind: callable. Declared return: dict. Source line: 33.

### test_bm25_scores_preserve_approved_formula

Pin term saturation and length normalization with unequal document lengths.

Kind: callable. Declared return: None. Source line: 47.

### test_query_bytes_and_default_result_limit

Preserve five default results and the 32 KiB UTF-8 query boundary.

Kind: callable. Declared return: None. Source line: 58.

### test_descriptor_text_character_boundary

Keep per-field character limits distinct from query byte limits.

Kind: callable. Declared return: None. Source line: 69.

### test_transport_byte_limits_and_overflow_probe

Preserve exact HTTP byte boundaries and detect oversized response bodies.

Kind: callable. Declared return: None. Source line: 77.

### test_transport_byte_limits_and_overflow_probe.Response

Expose a deterministic bounded response stream.

Kind: class. Declared return: Not declared / class. Source line: 83.

### test_transport_byte_limits_and_overflow_probe.Response.__enter__

Return the inert response object.

Kind: callable. Declared return: 'Response'. Source line: 86.

### test_transport_byte_limits_and_overflow_probe.Response.__exit__

Release no external resources.

Kind: callable. Declared return: None. Source line: 90.

### test_transport_byte_limits_and_overflow_probe.Response.read

Record the requested overflow-probe size and return synthetic bytes.

Kind: callable. Declared return: bytes. Source line: 93.

### test_transport_byte_limits_and_overflow_probe.Opener

Accept transport requests without network access.

Kind: class. Declared return: Not declared / class. Source line: 98.

### test_transport_byte_limits_and_overflow_probe.Opener.open

Record serialized request size and return the inert response.

Kind: callable. Declared return: Response. Source line: 101.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Request | Imported dependency for Request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | descriptor | Imported dependency for descriptor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | retriever | Imported dependency for retriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | OllamaClient | Imported dependency for OllamaClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | OllamaKeywords | Imported dependency for OllamaKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | validate_keywords | Imported dependency for validate keywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | bm25 | Imported dependency for bm25 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| test_keyword_limits_and_generation_contract | terms | Local binding for terms in test_keyword_limits_and_generation_contract; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 21 |
| test_keyword_limits_and_generation_contract.comprehension_21 | index | Comprehension item for index in test_keyword_limits_and_generation_contract.comprehension_21; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 21 |
| test_keyword_limits_and_generation_contract | invalid | Loop item for invalid in test_keyword_limits_and_generation_contract; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 24 |
| test_keyword_limits_and_generation_contract.CapturedClient | payload | Typed binding for payload in test_keyword_limits_and_generation_contract.CapturedClient; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 31 |
| test_keyword_limits_and_generation_contract.CapturedClient.post | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| test_keyword_limits_and_generation_contract.CapturedClient.post | route | Parameter for route in test_keyword_limits_and_generation_contract.CapturedClient.post; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 33 |
| test_keyword_limits_and_generation_contract.CapturedClient.post | payload | Parameter for payload in test_keyword_limits_and_generation_contract.CapturedClient.post; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 33 |
| test_keyword_limits_and_generation_contract.CapturedClient.post | self.payload | Attribute for payload in test_keyword_limits_and_generation_contract.CapturedClient.post; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_keyword_limits_and_generation_contract | client | Local binding for client in test_keyword_limits_and_generation_contract; use the enclosing contract and type below. | Return type of CapturedClient; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_bm25_scores_preserve_approved_formula | scores | Local binding for scores in test_bm25_scores_preserve_approved_formula; use the enclosing contract and type below. | Return type of bm25; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_query_bytes_and_default_result_limit | tmp_path | Parameter for tmp path in test_query_bytes_and_default_result_limit; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 58 |
| test_query_bytes_and_default_result_limit | service | Local binding for service in test_query_bytes_and_default_result_limit; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_query_bytes_and_default_result_limit | index | Loop item for index in test_query_bytes_and_default_result_limit; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 61 |
| test_descriptor_text_character_boundary | tmp_path | Parameter for tmp path in test_descriptor_text_character_boundary; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 69 |
| test_descriptor_text_character_boundary | service | Local binding for service in test_descriptor_text_character_boundary; use the enclosing contract and type below. | Return type of retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_transport_byte_limits_and_overflow_probe | monkeypatch | Parameter for monkeypatch in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 77 |
| test_transport_byte_limits_and_overflow_probe | requests | Typed binding for requests in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | list[int] | Enclosing invocation or class/instance lifetime | 79 |
| test_transport_byte_limits_and_overflow_probe | reads | Typed binding for reads in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | list[int] | Enclosing invocation or class/instance lifetime | 80 |
| test_transport_byte_limits_and_overflow_probe | response_body | Local binding for response body in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81, 115 |
| test_transport_byte_limits_and_overflow_probe.Response.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_transport_byte_limits_and_overflow_probe.Response.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 90 |
| test_transport_byte_limits_and_overflow_probe.Response.__exit__ | args | Parameter for args in test_transport_byte_limits_and_overflow_probe.Response.__exit__; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 90 |
| test_transport_byte_limits_and_overflow_probe.Response.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_transport_byte_limits_and_overflow_probe.Response.read | size | Parameter for size in test_transport_byte_limits_and_overflow_probe.Response.read; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 93 |
| test_transport_byte_limits_and_overflow_probe.Opener.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_transport_byte_limits_and_overflow_probe.Opener.open | request | Parameter for request in test_transport_byte_limits_and_overflow_probe.Opener.open; use the enclosing contract and type below. | Request | Enclosing invocation or class/instance lifetime | 101 |
| test_transport_byte_limits_and_overflow_probe.Opener.open | timeout | Parameter for timeout in test_transport_byte_limits_and_overflow_probe.Opener.open; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 101 |
| test_transport_byte_limits_and_overflow_probe | client | Local binding for client in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | Return type of OllamaClient; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_transport_byte_limits_and_overflow_probe | overhead | Local binding for overhead in test_transport_byte_limits_and_overflow_probe; use the enclosing contract and type below. | Return type of len; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
