# Reference for tests/test_application_agents.py

Offline agent contract tests; only the local-model network is substituted.

Source fingerprint: 798d00b04822b40ad5babb9c06e839a79a3f205737cabeb04265124bb886d6f2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_designer_validates_direct_import_contract_without_executing

Catch running candidate code or accepting a widget with an unknown dependency.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_designer_validates_direct_import_contract_without_executing.client

Return a controlled model-boundary proposal without executing source.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_designer_rejects_unknown_import

Catch allowing arbitrary dependencies through the widget proposal filter.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_dynamic_import_is_rejected_before_native_review

Catch bypassing the approved import surface through a dynamic builtin.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_local_client_supplies_a_strict_response_schema

Catch requesting only valid JSON while accepting wrong workflow/notes types.

Kind: callable. Declared return: Not declared / class. Source line: 56.

### test_local_client_supplies_a_strict_response_schema.Response

Provide a bounded HTTP response fixture without network access.

Kind: class. Declared return: Not declared / class. Source line: 64.

### test_local_client_supplies_a_strict_response_schema.Response.__enter__

Open the inert response fixture for a context-managed request.

Kind: callable. Declared return: Not declared / class. Source line: 67.

### test_local_client_supplies_a_strict_response_schema.Response.__exit__

Leave the response fixture without suppressing errors.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_local_client_supplies_a_strict_response_schema.Response.read

Return a complete fixed response envelope within the requested boundary.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_local_client_supplies_a_strict_response_schema.Opener

Capture the outgoing local request while keeping tests offline.

Kind: class. Declared return: Not declared / class. Source line: 103.

### test_local_client_supplies_a_strict_response_schema.Opener.open

Record the request contract and return the controlled response fixture.

Kind: callable. Declared return: Not declared / class. Source line: 106.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | WidgetDesigner | Imported dependency for WidgetDesigner in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_designer_validates_direct_import_contract_without_executing | candidate | Local binding for candidate in test_designer_validates_direct_import_contract_without_executing; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 10 |
| test_designer_validates_direct_import_contract_without_executing | prompts | Local binding for prompts in test_designer_validates_direct_import_contract_without_executing; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 15 |
| test_designer_validates_direct_import_contract_without_executing.client | role | Parameter for role in test_designer_validates_direct_import_contract_without_executing.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_designer_validates_direct_import_contract_without_executing.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_designer_validates_direct_import_contract_without_executing | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_dynamic_import_is_rejected_before_native_review | validate_source | Imported dependency for validate source in test_dynamic_import_is_rejected_before_native_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| test_local_client_supplies_a_strict_response_schema | tmp_path | Parameter for tmp path in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| test_local_client_supplies_a_strict_response_schema | monkeypatch | Parameter for monkeypatch in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| test_local_client_supplies_a_strict_response_schema | json | Imported dependency for json in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_local_client_supplies_a_strict_response_schema | LocalModelClient | Imported dependency for LocalModelClient in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_local_client_supplies_a_strict_response_schema | sent | Local binding for sent in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 62 |
| test_local_client_supplies_a_strict_response_schema.Response.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| test_local_client_supplies_a_strict_response_schema.Response.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_local_client_supplies_a_strict_response_schema.Response.__exit__ | args | Parameter for args in test_local_client_supplies_a_strict_response_schema.Response.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_local_client_supplies_a_strict_response_schema.Response.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_local_client_supplies_a_strict_response_schema.Response.read | size | Parameter for size in test_local_client_supplies_a_strict_response_schema.Response.read; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_local_client_supplies_a_strict_response_schema.Opener.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_local_client_supplies_a_strict_response_schema.Opener.open | request | Parameter for request in test_local_client_supplies_a_strict_response_schema.Opener.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_local_client_supplies_a_strict_response_schema.Opener.open | timeout | Parameter for timeout in test_local_client_supplies_a_strict_response_schema.Opener.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_local_client_supplies_a_strict_response_schema | schema | Local binding for schema in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 113 |
| test_local_client_supplies_a_strict_response_schema | jsonschema | Imported dependency for jsonschema in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 118 |
| test_local_client_supplies_a_strict_response_schema | valid | Local binding for valid in test_local_client_supplies_a_strict_response_schema; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 120 |
