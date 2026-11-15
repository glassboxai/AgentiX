# Reference for tests/test_v4_application_style_browser.py

Real native browser verification of the shared CSS and accessible corner close.

Source fingerprint: b70cfd9f9483845de0c61e5d98fd2f2458f5f8f5db9bc081433a34fc63abb300

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_application_matches_parent_palette_and_closes

Catch iframe style isolation, inaccessible close or a close that leaks the worker.

Kind: callable. Declared return: Not declared / class. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | schema3_package | Imported dependency for schema3 package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| test_native_application_matches_parent_palette_and_closes | tmp_path | Parameter for tmp path in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_native_application_matches_parent_palette_and_closes | expect | Imported dependency for expect in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_native_application_matches_parent_palette_and_closes | sync_playwright | Imported dependency for sync playwright in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_native_application_matches_parent_palette_and_closes | package | Local binding for package in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_native_application_matches_parent_palette_and_closes | port | Local binding for port in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_native_application_matches_parent_palette_and_closes | logpath | Local binding for logpath in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_native_application_matches_parent_palette_and_closes | log | Managed resource for log in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 25 |
| test_native_application_matches_parent_palette_and_closes | process | Local binding for process in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_native_application_matches_parent_palette_and_closes | url | Local binding for url in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_native_application_matches_parent_palette_and_closes | driver | Managed resource for driver in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 44 |
| test_native_application_matches_parent_palette_and_closes | browser | Local binding for browser in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_native_application_matches_parent_palette_and_closes | page | Local binding for page in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_native_application_matches_parent_palette_and_closes | container | Local binding for container in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_native_application_matches_parent_palette_and_closes | button | Local binding for button in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_native_application_matches_parent_palette_and_closes | bounds | Local binding for bounds in test_native_application_matches_parent_palette_and_closes; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
