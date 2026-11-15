# Reference for tests/test_element_ids_native.py

Native Gradio duplicate-tool-instance ID test using only a maintained fixture.

Source fingerprint: b9300e959fdc8e0e92c759d22fbcbfee15b8fe327c5fbac4dc7453c5eb04ca06

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_repeated_widgets_have_distinct_native_controls_and_callbacks

Two copies share an allocator, not control IDs or callback namespaces.

Kind: callable. Declared return: Not declared / class. Source line: 22.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | schema3_package | Imported dependency for schema3 package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 9 |
| module | DUPLICATE_CONNECTION | Module binding for DUPLICATE CONNECTION in module; use the enclosing contract and type below. | str | Module/process lifetime | 11 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | tmp_path | Parameter for tmp path in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | application_digest | Imported dependency for application digest in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 24 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | approve_application | Imported dependency for approve application in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 24 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | ApplicationSession | Imported dependency for ApplicationSession in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 25 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | package | Local binding for package in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | manifest_path | Local binding for manifest path in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | logic | Local binding for logic in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | approved | Local binding for approved in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | session | Managed resource for session in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 40 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | config | Local binding for config in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | ids | Local binding for ids in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 42 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks.comprehension_42 | c | Comprehension item for c in test_repeated_widgets_have_distinct_native_controls_and_callbacks.comprehension_42; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | endpoint | Loop item for endpoint in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 46 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | text | Loop item for text in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 46 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | count | Loop item for count in test_repeated_widgets_have_distinct_native_controls_and_callbacks; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 46 |
| test_repeated_widgets_have_distinct_native_controls_and_callbacks | response | Bounded response text to render or validate; it is not executable code. | Return type of request; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
