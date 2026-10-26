# Reference for tests/integration/test_windows_credentials.py

Opt-in native Windows Credential Manager verification using a disposable key.

Source fingerprint: 291645d71d0704ba6ad5ae7e4ecaf98eb484743ee74d2ea0b808befc391a59cc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_real_windows_credential_roundtrip_and_delete

Write/read/delete one unique test target; never access existing credentials.

Kind: callable. Declared return: Not declared / class. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | list | Module/process lifetime | 12 |
| test_real_windows_credential_roundtrip_and_delete | WindowsCredentialVault | Imported dependency for WindowsCredentialVault in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_real_windows_credential_roundtrip_and_delete | redact | Imported dependency for redact in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_real_windows_credential_roundtrip_and_delete | vault | Local binding for vault in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Return type of WindowsCredentialVault; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_real_windows_credential_roundtrip_and_delete | target | Local binding for target in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_real_windows_credential_roundtrip_and_delete | key | Local binding for key in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_real_windows_credential_roundtrip_and_delete | child | Local binding for child in test_real_windows_credential_roundtrip_and_delete; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
