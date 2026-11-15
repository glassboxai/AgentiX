# Reference for tests/test_v5_native_editor_browser.py

Real native Gradio edit handles for text, numeric output and action controls.

Source fingerprint: be78731829c9b4c64a2c26cecc54d827515aad54e90a28b63064712a5f0e6da0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_all_controls_have_unclipped_edit_handles

Catch input/output overflow clipping and visible empty container borders.

Kind: callable. Declared return: Not declared / class. Source line: 10.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | list | Module/process lifetime | 7 |
| test_all_controls_have_unclipped_edit_handles | tmp_path | Parameter for tmp path in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| test_all_controls_have_unclipped_edit_handles | expect | Imported dependency for expect in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_all_controls_have_unclipped_edit_handles | sync_playwright | Imported dependency for sync playwright in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_all_controls_have_unclipped_edit_handles | published_with_tools | Imported dependency for published with tools in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_all_controls_have_unclipped_edit_handles | approve_application | Imported dependency for approve application in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 15 |
| test_all_controls_have_unclipped_edit_handles | ApplicationPreview | Imported dependency for ApplicationPreview in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| test_all_controls_have_unclipped_edit_handles | service | Local binding for service in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_all_controls_have_unclipped_edit_handles | app | Local binding for app in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_all_controls_have_unclipped_edit_handles | fixture | Local binding for fixture in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_all_controls_have_unclipped_edit_handles | preview | Local binding for preview in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of ApplicationPreview; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_all_controls_have_unclipped_edit_handles | session | Local binding for session in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_all_controls_have_unclipped_edit_handles | driver | Managed resource for driver in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 23 |
| test_all_controls_have_unclipped_edit_handles | browser | Local binding for browser in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_all_controls_have_unclipped_edit_handles | page | Local binding for page in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_all_controls_have_unclipped_edit_handles | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 37 |
| test_all_controls_have_unclipped_edit_handles | control | Local binding for control in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_all_controls_have_unclipped_edit_handles | handle | Local binding for handle in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_all_controls_have_unclipped_edit_handles | bounds | Local binding for bounds in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_all_controls_have_unclipped_edit_handles | grip | Local binding for grip in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_all_controls_have_unclipped_edit_handles | groups | Local binding for groups in test_all_controls_have_unclipped_edit_handles; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
