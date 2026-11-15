# Reference for tests/unit/test_import_boundaries.py

Test the new inert-import contract before moving legacy initialization.

Source fingerprint: 2f4dc8421a5be42e45199bce217ca5e8cc28ccd3648dc7ce8c5dc2b0aa1ad155

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_legacy_imports_do_not_initialize_application

Compatibility imports must not need installed UI/LLM packages or storage.

Kind: callable. Declared return: Not declared / class. Source line: 9.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_legacy_imports_do_not_initialize_application | tmp_path | Parameter for tmp path in test_legacy_imports_do_not_initialize_application; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| test_legacy_imports_do_not_initialize_application | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_legacy_imports_do_not_initialize_application | script | Local binding for script in test_legacy_imports_do_not_initialize_application; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 12 |
| test_legacy_imports_do_not_initialize_application | environment | Local binding for environment in test_legacy_imports_do_not_initialize_application; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_legacy_imports_do_not_initialize_application | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
