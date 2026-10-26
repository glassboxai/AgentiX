# Reference for tests/integration/test_gradio_native_profiles.py

Opt-in real Gradio profile callback with native Windows secret persistence.

Source fingerprint: ad7608e2e023dbde378e51d9a68926e24a6da1dd2183b952597708d9a3a4e372

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_gradio_save_refresh_uses_real_windows_vault_and_temporary_metadata

Cover the production callback/store/vault combination with a disposable key.

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
| test_gradio_save_refresh_uses_real_windows_vault_and_temporary_metadata | script | Local binding for script in test_gradio_save_refresh_uses_real_windows_vault_and_temporary_metadata; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| test_gradio_save_refresh_uses_real_windows_vault_and_temporary_metadata | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
