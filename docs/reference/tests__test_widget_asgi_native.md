# Reference for tests/test_widget_asgi_native.py

LAB-003 actual Gradio ASGI transported through an isolated native process.

Source fingerprint: 9cbf94a8f5d5d49d03479656c1ccce302ab1fc83b98286dabe1e2b7b0dd8f7df

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_gradio_asgi_root_and_event

Require real pinned Gradio in AppContainer, not a host-rendered substitute.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_provisional_tests_cannot_modify_serving_process

Generated tests must run in a different native worker from the served widget.

Kind: callable. Declared return: Not declared / class. Source line: 25.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_native_gradio_asgi_root_and_event | WidgetSession | Imported dependency for WidgetSession in test_native_gradio_asgi_root_and_event; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_native_gradio_asgi_root_and_event | session | Managed resource for session in test_native_gradio_asgi_root_and_event; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 11 |
| test_native_gradio_asgi_root_and_event | root | Explicit root directory against which named paths are resolved. | Return type of request; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_native_gradio_asgi_root_and_event | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of request; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_native_gradio_asgi_root_and_event | json | Imported dependency for json in test_native_gradio_asgi_root_and_event; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_provisional_tests_cannot_modify_serving_process | tmp_path | Parameter for tmp path in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_provisional_tests_cannot_modify_serving_process | Path | Imported dependency for Path in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_provisional_tests_cannot_modify_serving_process | approve_package | Imported dependency for approve package in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 29 |
| test_provisional_tests_cannot_modify_serving_process | package_digest | Imported dependency for package digest in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 29 |
| test_provisional_tests_cannot_modify_serving_process | WidgetSession | Imported dependency for WidgetSession in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| test_provisional_tests_cannot_modify_serving_process | run_provisional_tests | Imported dependency for run provisional tests in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| test_provisional_tests_cannot_modify_serving_process | approved | Local binding for approved in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Return type of approve_package; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_provisional_tests_cannot_modify_serving_process | session | Managed resource for session in test_provisional_tests_cannot_modify_serving_process; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 48 |
