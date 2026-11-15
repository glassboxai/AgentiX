# Reference for tests/test_module_closure.py

Guard the module closure that keeps application code independent of the Lab UI.

The Lab package mixes presentation with reviewed runtime sources. These checks fail
before a removal step deletes a module that is still imported, copied by path into
the sandbox, or referenced by an installed-application policy digest.

Source fingerprint: 6939ccc1d9fd8f368e2b2180145c29b25656c7e1e63bd4a4939e7f90d30a3f28

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _module_name

Return the dotted import name of a source file inside the package.

Kind: callable. Declared return: str. Source line: 33.

### _imports

Collect absolute module names imported by one source file.

Kind: callable. Declared return: set[str]. Source line: 41.

### test_no_maintained_module_imports_a_removable_lab_module

Catch a removal step that leaves a live importer behind.

Kind: callable. Declared return: Not declared / class. Source line: 60.

### test_sandbox_staging_sources_stay_present

Catch deletion of a module that is copied by path instead of imported.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_staging_sources_are_referenced_by_name

Catch a staging reference removed while its source file still exists.

Kind: callable. Declared return: Not declared / class. Source line: 82.

### test_installed_application_policy_paths_exist

Catch a policy digest path that no longer resolves after a move or removal.

Kind: callable. Declared return: Not declared / class. Source line: 91.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 11 |
| module | PACKAGE | Module binding for PACKAGE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 12 |
| module | REMOVABLE | Module binding for REMOVABLE in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 14 |
| module | COPIED_BY_PATH | Module binding for COPIED BY PATH in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 25 |
| _module_name | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 33 |
| _module_name | parts | Local binding for parts in _module_name; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| _imports | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 41 |
| _imports | tree | Local binding for tree in _imports; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| _imports | found | Typed binding for found in _imports; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 44 |
| _imports | node | Loop item for node in _imports; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 45 |
| _imports.comprehension_47 | alias | Comprehension item for alias in _imports.comprehension_47; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| _imports | base | Local binding for base in _imports; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| _imports | prefix | Local binding for prefix in _imports; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| _imports | module | Local binding for module in _imports; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52, 54 |
| _imports.comprehension_56 | alias | Comprehension item for alias in _imports.comprehension_56; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 56 |
| test_no_maintained_module_imports_a_removable_lab_module | offenders | Local binding for offenders in test_no_maintained_module_imports_a_removable_lab_module; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 62 |
| test_no_maintained_module_imports_a_removable_lab_module | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 63 |
| test_no_maintained_module_imports_a_removable_lab_module | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of _module_name; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_no_maintained_module_imports_a_removable_lab_module | hits | Local binding for hits in test_no_maintained_module_imports_a_removable_lab_module; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_sandbox_staging_sources_stay_present | lab | Local binding for lab in test_sandbox_staging_sources_stay_present; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_sandbox_staging_sources_stay_present | missing | Local binding for missing in test_sandbox_staging_sources_stay_present; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 78 |
| test_sandbox_staging_sources_stay_present.comprehension_78 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 78 |
| test_staging_sources_are_referenced_by_name | sources | Local binding for sources in test_staging_sources_are_referenced_by_name; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| test_staging_sources_are_referenced_by_name.comprehension_84 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 85 |
| test_staging_sources_are_referenced_by_name | unreferenced | Local binding for unreferenced in test_staging_sources_are_referenced_by_name; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 87 |
| test_staging_sources_are_referenced_by_name.comprehension_87 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 87 |
| test_installed_application_policy_paths_exist | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_installed_application_policy_paths_exist | names | Typed binding for names in test_installed_application_policy_paths_exist; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 94, 99 |
| test_installed_application_policy_paths_exist | node | Loop item for node in test_installed_application_policy_paths_exist; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 95 |
| test_installed_application_policy_paths_exist | inner | Loop item for inner in test_installed_application_policy_paths_exist; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 97 |
| test_installed_application_policy_paths_exist.comprehension_99 | element | Comprehension item for element in test_installed_application_policy_paths_exist.comprehension_99; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 101 |
| test_installed_application_policy_paths_exist | missing | Local binding for missing in test_installed_application_policy_paths_exist; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 105 |
| test_installed_application_policy_paths_exist.comprehension_105 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 105 |
