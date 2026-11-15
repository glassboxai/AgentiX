# Reference for tests/test_v5_locations.py

Storage location regressions must not adopt packaged-host v4 or legacy v5 data.

Source fingerprint: 707524a536f394e60a057d858c8ca1dc3a60be0b67fe416c950c5c3cd4448a5f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_missing_home_never_falls_back_to_the_v5_profile

A missing AGENTIX_HOME must fail instead of resolving the retired v5 root.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_explicit_home_and_tools_root_control_storage

Both configured roots govern storage without creating files.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_missing_tools_root_is_rejected

The published Tools root is never derived from a default home.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_relative_or_empty_home_rejected

Never resolve a user data root relative to the current checkout.

Kind: callable. Declared return: Not declared / class. Source line: 34.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_missing_home_never_falls_back_to_the_v5_profile | tmp_path | Parameter for tmp path in test_missing_home_never_falls_back_to_the_v5_profile; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_missing_home_never_falls_back_to_the_v5_profile | values | Local binding for values in test_missing_home_never_falls_back_to_the_v5_profile; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 10 |
| test_explicit_home_and_tools_root_control_storage | tmp_path | Parameter for tmp path in test_explicit_home_and_tools_root_control_storage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_explicit_home_and_tools_root_control_storage | tools | Local binding for tools in test_explicit_home_and_tools_root_control_storage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_explicit_home_and_tools_root_control_storage | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_missing_tools_root_is_rejected | tmp_path | Parameter for tmp path in test_missing_tools_root_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_relative_or_empty_home_rejected | bad | Parameter for bad in test_relative_or_empty_home_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_relative_or_empty_home_rejected | tmp_path | Parameter for tmp path in test_relative_or_empty_home_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
