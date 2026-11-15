# Reference for tests/test_direct_widget_browser.py

Opt-in independent browser acceptance of an operator-reviewed model candidate.

Never imports candidate Python on the host. The operator must supply the digest
from a separate code review; tests cannot grant or persist production approval.

Source fingerprint: 1ebc1ea9f1002bf2425b73daa8f0d5fa84ea5dccf56f33288ca4cdeb0f20daef

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_model_generated_widget_in_real_native_gui

Catch incorrect callbacks, zero handling, stale outputs and ID collisions.

Kind: callable. Declared return: Not declared / class. Source line: 20.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| test_model_generated_widget_in_real_native_gui | tmp_path | Parameter for tmp path in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_model_generated_widget_in_real_native_gui | expect | Imported dependency for expect in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 22 |
| test_model_generated_widget_in_real_native_gui | sync_playwright | Imported dependency for sync playwright in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 22 |
| test_model_generated_widget_in_real_native_gui | package | Local binding for package in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_model_generated_widget_in_real_native_gui | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_model_generated_widget_in_real_native_gui | port | Local binding for port in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_model_generated_widget_in_real_native_gui | logpath | Local binding for logpath in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_model_generated_widget_in_real_native_gui | evidence | Local binding for evidence in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_model_generated_widget_in_real_native_gui | log | Managed resource for log in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 31 |
| test_model_generated_widget_in_real_native_gui | process | Local binding for process in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_model_generated_widget_in_real_native_gui | url | Local binding for url in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_model_generated_widget_in_real_native_gui | driver | Managed resource for driver in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 54 |
| test_model_generated_widget_in_real_native_gui | browser | Local binding for browser in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_model_generated_widget_in_real_native_gui | page | Local binding for page in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_model_generated_widget_in_real_native_gui | text | Loop item for text in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| test_model_generated_widget_in_real_native_gui | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| test_model_generated_widget_in_real_native_gui | ids | Local binding for ids in test_model_generated_widget_in_real_native_gui; use the enclosing contract and type below. | Return type of evaluate_all; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
