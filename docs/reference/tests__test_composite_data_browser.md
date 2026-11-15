# Reference for tests/test_composite_data_browser.py

Rendered-page regression for the composite data-operation accordion.

The backend is an explicit double: this test proves the maintained Gradio view
renders the contract, the named-result table and the bounded rejection message in
a real browser. Native isolation and the supervisor contract are covered by the
offline and Windows-isolation suites, never by this page check.

Source fingerprint: 510de7e75fe1acdb99f32713730e7817851dd63fc71ccf42e0ae8ae14151ab38

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_composite_accordion_renders_contract_table_and_rejection

Catch a hidden contract, a stale table or a swallowed JSON diagnostic.

Kind: callable. Declared return: Not declared / class. Source line: 19.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| test_composite_accordion_renders_contract_table_and_rejection | tmp_path | Parameter for tmp path in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_composite_accordion_renders_contract_table_and_rejection | monkeypatch | Parameter for monkeypatch in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_composite_accordion_renders_contract_table_and_rejection | expect | Imported dependency for expect in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 21 |
| test_composite_accordion_renders_contract_table_and_rejection | sync_playwright | Imported dependency for sync playwright in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 21 |
| test_composite_accordion_renders_contract_table_and_rejection | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 23 |
| test_composite_accordion_renders_contract_table_and_rejection | sessions | Local binding for sessions in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_26 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 26 |
| test_composite_accordion_renders_contract_table_and_rejection | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_composite_accordion_renders_contract_table_and_rejection | contract | Validated declarative acceptance data bound to current artifact identities. | str | Enclosing invocation or class/instance lifetime | 28 |
| test_composite_accordion_renders_contract_table_and_rejection | backend.data_contract | Attribute for backend.data contract in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_34 | token | Callback parameter for token in test_composite_accordion_renders_contract_table_and_rejection.lambda_34; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 34 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_34 | request | Callback parameter for request in test_composite_accordion_renders_contract_table_and_rejection.lambda_34; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 34 |
| test_composite_accordion_renders_contract_table_and_rejection | backend.data | Attribute for backend.data in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_35 | text | Callback parameter for text in test_composite_accordion_renders_contract_table_and_rejection.lambda_35; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 35 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_35 | token | Callback parameter for token in test_composite_accordion_renders_contract_table_and_rejection.lambda_35; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 35 |
| test_composite_accordion_renders_contract_table_and_rejection.lambda_35 | request | Callback parameter for request in test_composite_accordion_renders_contract_table_and_rejection.lambda_35; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 35 |
| test_composite_accordion_renders_contract_table_and_rejection | demo | Local binding for demo in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_composite_accordion_renders_contract_table_and_rejection | listener | Managed resource for listener in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 42 |
| test_composite_accordion_renders_contract_table_and_rejection | port | Local binding for port in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_composite_accordion_renders_contract_table_and_rejection | driver | Managed resource for driver in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 53 |
| test_composite_accordion_renders_contract_table_and_rejection | browser | Local binding for browser in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_composite_accordion_renders_contract_table_and_rejection | page | Local binding for page in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_composite_accordion_renders_contract_table_and_rejection | contract_view | Local binding for contract view in test_composite_accordion_renders_contract_table_and_rejection; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
