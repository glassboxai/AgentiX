# Reference for tests/test_v5_policy_bindings.py

Approval policy fingerprints must include new presentation and cleanup boundaries.

Source fingerprint: 3560665a91a849d963d5bdba3161e3e0705fb4f8342bbc2dee7290695aa19a62

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_changed_boundary_invalidates_policy_binding

Catch retaining an approval after modifying an imported validation boundary.

Kind: callable. Declared return: Not declared / class. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_changed_boundary_invalidates_policy_binding | tmp_path | Parameter for tmp path in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_changed_boundary_invalidates_policy_binding | monkeypatch | Parameter for monkeypatch in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_changed_boundary_invalidates_policy_binding | module | Parameter for module in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_changed_boundary_invalidates_policy_binding | function | Parameter for function in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_changed_boundary_invalidates_policy_binding | changed | Parameter for changed in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_changed_boundary_invalidates_policy_binding | checkout | Local binding for checkout in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_changed_boundary_invalidates_policy_binding | target | Local binding for target in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_changed_boundary_invalidates_policy_binding | relative | Local binding for relative in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Return type of relative_to; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_changed_boundary_invalidates_policy_binding | before | Local binding for before in test_changed_boundary_invalidates_policy_binding; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_changed_boundary_invalidates_policy_binding | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
