# Reference for tests/test_v5_app_names.py

Named application folders retain opaque authorization identities.

Source fingerprint: e8dfba762ab2f01d4417848af0d34ada5da3eea62590bc8463432bfae84470c9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_named_folder_and_display_name_survive_reload

Catch catalog entries being stored under an unreadable UUID or losing names.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_invalid_name_never_publishes

Reject traversal, Windows devices and ambiguous names before copying files.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_duplicate_name_preserves_original

Never overwrite a reviewed application when a second name collides.

Kind: callable. Declared return: Not declared / class. Source line: 31.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | library | Imported dependency for library in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | verified | Imported dependency for verified in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| test_named_folder_and_display_name_survive_reload | tmp_path | Parameter for tmp path in test_named_folder_and_display_name_survive_reload; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_named_folder_and_display_name_survive_reload | service | Local binding for service in test_named_folder_and_display_name_survive_reload; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| test_named_folder_and_display_name_survive_reload | item | Local binding for item in test_named_folder_and_display_name_survive_reload; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_named_folder_and_display_name_survive_reload | item.display_name | Attribute for item.display name in test_named_folder_and_display_name_survive_reload; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 11 |
| test_named_folder_and_display_name_survive_reload | app | Local binding for app in test_named_folder_and_display_name_survive_reload; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_named_folder_and_display_name_survive_reload.comprehension_17 | x | Comprehension item for x in test_named_folder_and_display_name_survive_reload.comprehension_17; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 17 |
| test_invalid_name_never_publishes | tmp_path | Parameter for tmp path in test_invalid_name_never_publishes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_invalid_name_never_publishes | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_invalid_name_never_publishes | service | Local binding for service in test_invalid_name_never_publishes; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_invalid_name_never_publishes | item | Local binding for item in test_invalid_name_never_publishes; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_invalid_name_never_publishes | item.display_name | Attribute for item.display name in test_invalid_name_never_publishes; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_duplicate_name_preserves_original | tmp_path | Parameter for tmp path in test_duplicate_name_preserves_original; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_duplicate_name_preserves_original | service | Local binding for service in test_duplicate_name_preserves_original; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_duplicate_name_preserves_original | first | Local binding for first in test_duplicate_name_preserves_original; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_duplicate_name_preserves_original | first.display_name | Attribute for first.display name in test_duplicate_name_preserves_original; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 35 |
| test_duplicate_name_preserves_original | original | Local binding for original in test_duplicate_name_preserves_original; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_duplicate_name_preserves_original | second | Local binding for second in test_duplicate_name_preserves_original; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_duplicate_name_preserves_original | second.display_name | Attribute for second.display name in test_duplicate_name_preserves_original; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 38 |
