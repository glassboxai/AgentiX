# Reference for tests/integration/test_windows_approval_protection.py

Opt-in Windows DPAPI integrity and cross-process approval persistence.

Source fingerprint: c740a6ba20a9f0c01d66efb2427843986d93431a04e0cfeed75cf7e0857eb0e7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_dpapi_survives_new_process_and_rejects_altered_blob

The real user/machine protector restores after restart and rejects corruption.

Kind: callable. Declared return: Not declared / class. Source line: 16.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | list | Module/process lifetime | 10 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | tmp_path | Parameter for tmp path in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | WindowsDataProtection | Imported dependency for WindowsDataProtection in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | protector | Local binding for protector in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | Return type of WindowsDataProtection; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | payload | Local binding for payload in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 21 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | protected | Local binding for protected in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | script | Local binding for script in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_dpapi_survives_new_process_and_rejects_altered_blob | corrupt | Loop item for corrupt in test_dpapi_survives_new_process_and_rejects_altered_blob; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 36 |
