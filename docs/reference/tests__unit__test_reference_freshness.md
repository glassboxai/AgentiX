# Reference for tests/unit/test_reference_freshness.py

Verify source reference completeness and synchronization without importing source.

Source fingerprint: b960a9972f32b311788a18b8534ee78e4f79e8c37c8116b7a6152a3074eb53bc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_inventory_documents_parameters_attributes_locals_and_types

Preserve lexical ownership and declared types without publishing values.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_reference_check_detects_source_changes_and_never_reads_excluded_storage

Keep authored temporary generated storage outside reference discovery.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_release_reference_is_current

Fail the offline suite whenever source and maintained reference diverge.

Kind: callable. Declared return: Not declared / class. Source line: 46.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | build_documents | Imported dependency for build documents in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | scan_source | Imported dependency for scan source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_inventory_documents_parameters_attributes_locals_and_types | tmp_path | Parameter for tmp path in test_inventory_documents_parameters_attributes_locals_and_types; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_inventory_documents_parameters_attributes_locals_and_types | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_inventory_documents_parameters_attributes_locals_and_types | inventory | Local binding for inventory in test_inventory_documents_parameters_attributes_locals_and_types; use the enclosing contract and type below. | Return type of scan_source; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_inventory_documents_parameters_attributes_locals_and_types | names | Local binding for names in test_inventory_documents_parameters_attributes_locals_and_types; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 24 |
| test_inventory_documents_parameters_attributes_locals_and_types.comprehension_24 | item | Comprehension item for item in test_inventory_documents_parameters_attributes_locals_and_types.comprehension_24; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| test_reference_check_detects_source_changes_and_never_reads_excluded_storage | tmp_path | Parameter for tmp path in test_reference_check_detects_source_changes_and_never_reads_excluded_storage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_reference_check_detects_source_changes_and_never_reads_excluded_storage | folder | Local binding for folder in test_reference_check_detects_source_changes_and_never_reads_excluded_storage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_reference_check_detects_source_changes_and_never_reads_excluded_storage | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_reference_check_detects_source_changes_and_never_reads_excluded_storage | excluded | Local binding for excluded in test_reference_check_detects_source_changes_and_never_reads_excluded_storage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_release_reference_is_current | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
