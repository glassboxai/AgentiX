# Reference for tests/test_v5_architecture.py

Canonical imports are the only supported internal import paths.

The retired compatibility layer is recorded here as a frozen contract so that a
reintroduced ``sys.modules[__name__]`` alias or a legacy import path fails the
offline suite instead of silently returning.

Source fingerprint: b789446d1bbcc4df7b8d1aa78561412ef949653f612da0720cd6c17dcd02800e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### maintained_sources

Yield every maintained module under the source package, skipping bytecode.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_canonical_modules_expose_their_public_symbols

Each responsibility package must be importable and expose its public contract.

Kind: callable. Declared return: Not declared / class. Source line: 79.

### test_no_legacy_sys_modules_alias_assignment_remains

A compatibility alias is an assignment to ``sys.modules[__name__]``.

Kind: callable. Declared return: Not declared / class. Source line: 86.

### test_no_maintained_module_imports_a_retired_legacy_path

Retired paths must not return through a static import in maintained source.

Kind: callable. Declared return: Not declared / class. Source line: 109.

### test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias

The storage package must resolve to its package, never to a legacy alias module.

Kind: callable. Declared return: Not declared / class. Source line: 127.

### test_security_and_storage_import_without_circular_failure

Either import order must finish; a partially initialized module raises ImportError.

Kind: callable. Declared return: Not declared / class. Source line: 144.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| module | SOURCE | Module binding for SOURCE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | RETIRED_LEGACY_MODULES | Module binding for RETIRED LEGACY MODULES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 19 |
| maintained_sources | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 61 |
| test_canonical_modules_expose_their_public_symbols | module | Parameter for module in test_canonical_modules_expose_their_public_symbols; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| test_canonical_modules_expose_their_public_symbols | symbol | Parameter for symbol in test_canonical_modules_expose_their_public_symbols; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| test_canonical_modules_expose_their_public_symbols | imported | Local binding for imported in test_canonical_modules_expose_their_public_symbols; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_no_legacy_sys_modules_alias_assignment_remains | offenders | Local binding for offenders in test_no_legacy_sys_modules_alias_assignment_remains; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 88 |
| test_no_legacy_sys_modules_alias_assignment_remains | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 89 |
| test_no_legacy_sys_modules_alias_assignment_remains | tree | Local binding for tree in test_no_legacy_sys_modules_alias_assignment_remains; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_no_legacy_sys_modules_alias_assignment_remains | node | Loop item for node in test_no_legacy_sys_modules_alias_assignment_remains; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 91 |
| test_no_legacy_sys_modules_alias_assignment_remains | targets | Local binding for targets in test_no_legacy_sys_modules_alias_assignment_remains; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_no_legacy_sys_modules_alias_assignment_remains | target | Loop item for target in test_no_legacy_sys_modules_alias_assignment_remains; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 93 |
| test_no_legacy_sys_modules_alias_assignment_remains | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_no_maintained_module_imports_a_retired_legacy_path | retired | Local binding for retired in test_no_maintained_module_imports_a_retired_legacy_path; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_no_maintained_module_imports_a_retired_legacy_path | offenders | Local binding for offenders in test_no_maintained_module_imports_a_retired_legacy_path; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 112 |
| test_no_maintained_module_imports_a_retired_legacy_path | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 113 |
| test_no_maintained_module_imports_a_retired_legacy_path | tree | Local binding for tree in test_no_maintained_module_imports_a_retired_legacy_path; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_no_maintained_module_imports_a_retired_legacy_path | node | Loop item for node in test_no_maintained_module_imports_a_retired_legacy_path; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 115 |
| test_no_maintained_module_imports_a_retired_legacy_path | names | Local binding for names in test_no_maintained_module_imports_a_retired_legacy_path; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 116, 118, 120 |
| test_no_maintained_module_imports_a_retired_legacy_path.comprehension_118 | alias | Comprehension item for alias in test_no_maintained_module_imports_a_retired_legacy_path.comprehension_118; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 118 |
| test_no_maintained_module_imports_a_retired_legacy_path.comprehension_120 | alias | Comprehension item for alias in test_no_maintained_module_imports_a_retired_legacy_path.comprehension_120; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| test_no_maintained_module_imports_a_retired_legacy_path | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 121 |
| test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias | package | Local binding for package in test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias | artifacts | Local binding for artifacts in test_canonical_storage_package_is_not_shadowed_by_a_compatibility_alias; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_security_and_storage_import_without_circular_failure | order | Parameter for order in test_security_and_storage_import_without_circular_failure; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 144 |
| test_security_and_storage_import_without_circular_failure | script | Local binding for script in test_security_and_storage_import_without_circular_failure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_security_and_storage_import_without_circular_failure.comprehension_148 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 148 |
| test_security_and_storage_import_without_circular_failure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
