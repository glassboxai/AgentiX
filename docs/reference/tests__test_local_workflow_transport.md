# Reference for tests/test_local_workflow_transport.py

V5-ERR-041-03: preserve source presence across the actual local-model boundary.

Source fingerprint: 5f3aad4f55da6252cce5dcc8e627484919495793753725fb92c22bb15efa1397

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_local_http_client_round_trip_keeps_graph_and_timeout

Exercise real serialization and parsing with only HTTP replaced by a fixture.

Kind: callable. Declared return: None. Source line: 15.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Response

Return one bounded completed Ollama response without network activity.

Kind: class. Declared return: Not declared / class. Source line: 36.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__enter__

Open the authored response.

Kind: callable. Declared return: 'Response'. Source line: 39.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__exit__

Propagate failures without suppressing them.

Kind: callable. Declared return: bool. Source line: 43.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Response.read

Return reviewed fixture data within the caller's byte boundary.

Kind: callable. Declared return: bytes. Source line: 47.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Opener

Capture timeout and request schema; never call a model.

Kind: class. Declared return: Not declared / class. Source line: 57.

### test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open

Record the transport options and return the inert response.

Kind: callable. Declared return: Response. Source line: 60.

### test_timeout_is_bounded_before_any_operation

No unlimited, coerced or oversized deadline may reach the HTTP boundary.

Kind: callable. Declared return: None. Source line: 75.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | jsonschema | Imported dependency for jsonschema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | SCHEMAS | Imported dependency for SCHEMAS in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | workflow | Imported dependency for workflow in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | LocalModelClient | Imported dependency for LocalModelClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | CatalogAssembler | Imported dependency for CatalogAssembler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | tmp_path | Parameter for tmp path in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 16 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | monkeypatch | Parameter for monkeypatch in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 16 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | timeout | Parameter for timeout in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 16 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | proposal | Local binding for proposal in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 19 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.comprehension_21 | node | Comprehension item for node in test_local_http_client_round_trip_keeps_graph_and_timeout.comprehension_21; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 21 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | seen | Local binding for seen in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 34 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__exit__ | args | Parameter for args in test_local_http_client_round_trip_keeps_graph_and_timeout.Response.__exit__; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 43 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Response.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Response.read | size | Parameter for size in test_local_http_client_round_trip_keeps_graph_and_timeout.Response.read; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 47 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open | request | Parameter for request in test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 60 |
| test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open | timeout | Parameter for timeout in test_local_http_client_round_trip_keeps_graph_and_timeout.Opener.open; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 60 |
| test_local_http_client_round_trip_keeps_graph_and_timeout | client | Local binding for client in test_local_http_client_round_trip_keeps_graph_and_timeout; use the enclosing contract and type below. | Return type of LocalModelClient; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_timeout_is_bounded_before_any_operation | tmp_path | Parameter for tmp path in test_timeout_is_bounded_before_any_operation; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 75 |
| test_timeout_is_bounded_before_any_operation | timeout | Parameter for timeout in test_timeout_is_bounded_before_any_operation; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 75 |
