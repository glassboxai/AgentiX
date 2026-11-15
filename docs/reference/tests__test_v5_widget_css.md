# Reference for tests/test_v5_widget_css.py

Per-widget styles are reviewed local data, never external resource loaders.

Source fingerprint: 7ee5e0078a0f3abb0501ce78f1bd63e15dc5a5bf0d1b6a4da1245d4337de49a1

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### validator

Fail observably until the maintained scoped-style boundary exists.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_scoped_style_is_accepted

A local palette change for this tool remains usable in its own CSS file.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_unsafe_or_foreign_styles_rejected

Reject external transmission and styling unrelated controls or the toolbar.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_closed_descendant_suffixes_are_accepted

The field box and the caption are inner elements, not the widget container.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_arbitrary_descendants_are_rejected

Only the documented inner elements may be styled, never any node.

Kind: callable. Declared return: Not declared / class. Source line: 51.

### test_widget_companions_are_colocated_and_changes_revoke_reuse

CSS/tests are real files, and editing either never inherits an old grant.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_widget_publication_never_overwrites_a_linked_companion

A tool-local hard link must not redirect CSS writes into another file.

Kind: callable. Declared return: Not declared / class. Source line: 90.

### test_style_dimensions_are_bounded

A small CSS file must not create extreme geometry or overlap lifecycle controls.

Kind: callable. Declared return: Not declared / class. Source line: 120.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| validator | validate_widget_css | Imported dependency for validate widget css in validator; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_scoped_style_is_accepted | css | Local binding for css in test_scoped_style_is_accepted; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 17 |
| test_unsafe_or_foreign_styles_rejected | css | Parameter for css in test_unsafe_or_foreign_styles_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_closed_descendant_suffixes_are_accepted | suffix | Parameter for suffix in test_closed_descendant_suffixes_are_accepted; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_closed_descendant_suffixes_are_accepted | css | Local binding for css in test_closed_descendant_suffixes_are_accepted; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_arbitrary_descendants_are_rejected | suffix | Parameter for suffix in test_arbitrary_descendants_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| test_arbitrary_descendants_are_rejected | css | Local binding for css in test_arbitrary_descendants_are_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | tmp_path | Parameter for tmp path in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | installed | Imported dependency for installed in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | registry | Imported dependency for registry in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | store | Imported dependency for store in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | fixture | Local binding for fixture in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | tool | Local binding for tool in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | service | Local binding for service in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | proposal | Local binding for proposal in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 68 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | directory | Local binding for directory in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | css_path | Local binding for css path in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | tests_path | Local binding for tests path in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_widget_companions_are_colocated_and_changes_revoke_reuse | loaded | Local binding for loaded in test_widget_companions_are_colocated_and_changes_revoke_reuse; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_widget_publication_never_overwrites_a_linked_companion | tmp_path | Parameter for tmp path in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 90 |
| test_widget_publication_never_overwrites_a_linked_companion | os | Imported dependency for os in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 92 |
| test_widget_publication_never_overwrites_a_linked_companion | installed | Imported dependency for installed in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_widget_publication_never_overwrites_a_linked_companion | registry | Imported dependency for registry in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_widget_publication_never_overwrites_a_linked_companion | store | Imported dependency for store in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 95 |
| test_widget_publication_never_overwrites_a_linked_companion | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_widget_publication_never_overwrites_a_linked_companion | fixture | Local binding for fixture in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_widget_publication_never_overwrites_a_linked_companion | tool | Local binding for tool in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_widget_publication_never_overwrites_a_linked_companion | outside | Local binding for outside in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_widget_publication_never_overwrites_a_linked_companion | alias | Local binding for alias in test_widget_publication_never_overwrites_a_linked_companion; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_style_dimensions_are_bounded | declaration | Parameter for declaration in test_style_dimensions_are_bounded; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 120 |
| test_style_dimensions_are_bounded | css | Local binding for css in test_style_dimensions_are_bounded; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 122 |
