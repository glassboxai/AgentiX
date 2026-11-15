# Reference for tests/unit/test_portable_modules.py

Owner-extensible portable module list regressions; no generated content is read.

Source fingerprint: 082a9da0ecbf53f12daf4cb475a582769ac134818d9dc113fc15d2f15794881a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_default_list_fails_closed_without_config

A missing config keeps the maintained default, including re.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### test_valid_config_replaces_default_but_always_keeps_typing

The owner list takes full control; typing remains forced for Annotated contracts.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_corrupt_config_falls_back_to_default

Unreadable or malformed JSON never widens or empties the effective list.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_invalid_entries_fall_back_to_default

Non-identifier or uppercase module names reject the whole file.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### test_unapproved_imports_names_each_unlisted_module

Diagnostics surface the exact rejected imports for the owner message.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_computation_only_accepts_owner_extended_list

The real count_words_in_text source passes once re is owner-approved.

Kind: callable. Declared return: Not declared / class. Source line: 61.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | allowed_modules | Imported dependency for allowed modules in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | computation_only | Imported dependency for computation only in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | unapproved_imports | Imported dependency for unapproved imports in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | REGEX_TOOL | Module binding for REGEX TOOL in module; use the enclosing contract and type below. | bytes | Module/process lifetime | 11 |
| test_default_list_fails_closed_without_config | tmp_path | Parameter for tmp path in test_default_list_fails_closed_without_config; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| test_default_list_fails_closed_without_config | modules | Local binding for modules in test_default_list_fails_closed_without_config; use the enclosing contract and type below. | Return type of allowed_modules; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_valid_config_replaces_default_but_always_keeps_typing | tmp_path | Parameter for tmp path in test_valid_config_replaces_default_but_always_keeps_typing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_valid_config_replaces_default_but_always_keeps_typing | config | Local binding for config in test_valid_config_replaces_default_but_always_keeps_typing; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_valid_config_replaces_default_but_always_keeps_typing | modules | Local binding for modules in test_valid_config_replaces_default_but_always_keeps_typing; use the enclosing contract and type below. | Return type of allowed_modules; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_corrupt_config_falls_back_to_default | tmp_path | Parameter for tmp path in test_corrupt_config_falls_back_to_default; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_corrupt_config_falls_back_to_default | config | Local binding for config in test_corrupt_config_falls_back_to_default; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_invalid_entries_fall_back_to_default | tmp_path | Parameter for tmp path in test_invalid_entries_fall_back_to_default; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| test_invalid_entries_fall_back_to_default | config | Local binding for config in test_invalid_entries_fall_back_to_default; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_unapproved_imports_names_each_unlisted_module | tmp_path | Parameter for tmp path in test_unapproved_imports_names_each_unlisted_module; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_unapproved_imports_names_each_unlisted_module | modules | Local binding for modules in test_unapproved_imports_names_each_unlisted_module; use the enclosing contract and type below. | Return type of allowed_modules; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_computation_only_accepts_owner_extended_list | tmp_path | Parameter for tmp path in test_computation_only_accepts_owner_extended_list; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
