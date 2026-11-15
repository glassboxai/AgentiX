# Reference for tests/test_catalog_maintenance_browser.py

Real GUI deletion and rejected-file repair; model boundary and initial catalog grants are explicit doubles.

Source fingerprint: ad0e2a090b6a2eccb9727d3301cc6490fba02d18f6ee245da81ea52394d39c8a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### server

Own one disposable server and its complete process tree.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### choose

Select a real Gradio option by its user-facing identity.

Kind: callable. Declared return: Not declared / class. Source line: 46.

### replace_code

Edit the actual CodeMirror control, not hidden server data.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_delete_confirmation_dependencies_and_open_app

Exercise dependency blocking, cancellation, cross-session use and permanent removal.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_reject_edit_revalidate_and_reuse_from_user_query

No file approval rejection may force a new tool or silently bypass acceptance.

Kind: callable. Declared return: Not declared / class. Source line: 115.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | contextmanager | Imported dependency for contextmanager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | stop_process_tree | Imported dependency for stop process tree in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| module | CODE | Module binding for CODE in module; use the enclosing contract and type below. | str | Module/process lifetime | 16 |
| module | TESTS | Module binding for TESTS in module; use the enclosing contract and type below. | str | Module/process lifetime | 17 |
| server | tmp_path | Parameter for tmp path in server; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| server | mode | Parameter for mode in server; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| server | port | Local binding for port in server; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| server | logpath | Local binding for logpath in server; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| server | log | Managed resource for log in server; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 25 |
| server | process | Local binding for process in server; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| server | url | Local binding for url in server; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| choose | page | Parameter for page in choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| choose | selector | Parameter for selector in choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| choose | label | Parameter for label in choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| replace_code | page | Parameter for page in replace_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| replace_code | selector | Parameter for selector in replace_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| replace_code | text | Parameter for text in replace_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_delete_confirmation_dependencies_and_open_app | tmp_path | Parameter for tmp path in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_delete_confirmation_dependencies_and_open_app | expect | Imported dependency for expect in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| test_delete_confirmation_dependencies_and_open_app | sync_playwright | Imported dependency for sync playwright in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| test_delete_confirmation_dependencies_and_open_app | url | Managed resource for url in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Return type of server; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 63 |
| test_delete_confirmation_dependencies_and_open_app | driver | Managed resource for driver in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 63 |
| test_delete_confirmation_dependencies_and_open_app | browser | Local binding for browser in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_delete_confirmation_dependencies_and_open_app | first | Local binding for first in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 67 |
| test_delete_confirmation_dependencies_and_open_app | second | Local binding for second in test_delete_confirmation_dependencies_and_open_app; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 67 |
| test_reject_edit_revalidate_and_reuse_from_user_query | tmp_path | Parameter for tmp path in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_reject_edit_revalidate_and_reuse_from_user_query | expect | Imported dependency for expect in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 117 |
| test_reject_edit_revalidate_and_reuse_from_user_query | sync_playwright | Imported dependency for sync playwright in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 117 |
| test_reject_edit_revalidate_and_reuse_from_user_query | url | Managed resource for url in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of server; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 119 |
| test_reject_edit_revalidate_and_reuse_from_user_query | driver | Managed resource for driver in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 119 |
| test_reject_edit_revalidate_and_reuse_from_user_query | browser | Local binding for browser in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_reject_edit_revalidate_and_reuse_from_user_query | page | Local binding for page in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_reject_edit_revalidate_and_reuse_from_user_query | review | Local binding for review in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of get_by_label; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_reject_edit_revalidate_and_reuse_from_user_query | proposed | Local binding for proposed in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| test_reject_edit_revalidate_and_reuse_from_user_query | cases | Local binding for cases in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 144 |
| test_reject_edit_revalidate_and_reuse_from_user_query.comprehension_144 | case | Comprehension item for case in test_reject_edit_revalidate_and_reuse_from_user_query.comprehension_144; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 144 |
| test_reject_edit_revalidate_and_reuse_from_user_query | before | Local binding for before in test_reject_edit_revalidate_and_reuse_from_user_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 159 |
