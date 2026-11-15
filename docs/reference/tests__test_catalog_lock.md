# Reference for tests/test_catalog_lock.py

Native catalog lock handles must close even when unlock reports an OS error.

Source fingerprint: 3d53de913725addb72e3903afe3224d9960213c1b239f5783bc264dfecefa79b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_unlock_failure_closes_handle

Catch file handles surviving failed catalog cleanup and blocking later actions.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_unlock_failure_closes_handle.fail_unlock

Inject only the release failure; acquisition used the real Windows lock.

Kind: callable. Declared return: Not declared / class. Source line: 16.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | msvcrt | Imported dependency for msvcrt in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | CatalogLock | Imported dependency for CatalogLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_unlock_failure_closes_handle | tmp_path | Parameter for tmp path in test_unlock_failure_closes_handle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| test_unlock_failure_closes_handle | monkeypatch | Parameter for monkeypatch in test_unlock_failure_closes_handle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| test_unlock_failure_closes_handle | guard | Local binding for guard in test_unlock_failure_closes_handle; use the enclosing contract and type below. | Return type of CatalogLock; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_unlock_failure_closes_handle | original | Local binding for original in test_unlock_failure_closes_handle; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_unlock_failure_closes_handle.fail_unlock | handle | Parameter for handle in test_unlock_failure_closes_handle.fail_unlock; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_unlock_failure_closes_handle.fail_unlock | mode | Parameter for mode in test_unlock_failure_closes_handle.fail_unlock; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_unlock_failure_closes_handle.fail_unlock | count | Parameter for count in test_unlock_failure_closes_handle.fail_unlock; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
