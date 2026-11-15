# Reference for tests/test_v5_review_browser.py

Real Gradio panes and floating chat with an explicit synthetic model boundary.

Source fingerprint: 513a155ea941cd32a837a4ac4a960be2897122b55f1bc95986e5e50c62712e4e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_review_resize_and_context_help

Check actual resizing, full edited context, floating controls and session separation.

Kind: callable. Declared return: Not declared / class. Source line: 26.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 13 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| test_review_resize_and_context_help | tmp_path | Parameter for tmp path in test_review_resize_and_context_help; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_review_resize_and_context_help | expect | Imported dependency for expect in test_review_resize_and_context_help; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_review_resize_and_context_help | sync_playwright | Imported dependency for sync playwright in test_review_resize_and_context_help; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_review_resize_and_context_help | port | Local binding for port in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_review_resize_and_context_help | logpath | Local binding for logpath in test_review_resize_and_context_help; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_review_resize_and_context_help | log | Managed resource for log in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 32 |
| test_review_resize_and_context_help | process | Local binding for process in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_review_resize_and_context_help | url | Local binding for url in test_review_resize_and_context_help; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_review_resize_and_context_help | driver | Managed resource for driver in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 47 |
| test_review_resize_and_context_help | browser | Local binding for browser in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_review_resize_and_context_help | page | Local binding for page in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_review_resize_and_context_help | panes | Local binding for panes in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_review_resize_and_context_help | columns | Local binding for columns in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_review_resize_and_context_help | heights | Local binding for heights in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of evaluate_all; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_review_resize_and_context_help | before | Local binding for before in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_review_resize_and_context_help | split | Local binding for split in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_review_resize_and_context_help | height | Local binding for height in test_review_resize_and_context_help; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_review_resize_and_context_help | editor | Local binding for editor in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_review_resize_and_context_help | popup | Local binding for popup in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_review_resize_and_context_help | messages | Local binding for messages in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| test_review_resize_and_context_help | context | Local binding for context in test_review_resize_and_context_help; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_review_resize_and_context_help | box | Local binding for box in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_review_resize_and_context_help | title | Local binding for title in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_review_resize_and_context_help | current | Local binding for current in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_review_resize_and_context_help | other | Local binding for other in test_review_resize_and_context_help; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_review_resize_and_context_help | stop_process_tree | Imported dependency for stop process tree in test_review_resize_and_context_help; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 143 |
