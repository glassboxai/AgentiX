# Reference for tests/test_v5_profile_cleanup.py

Only recorded owned empty AppContainer residues may be removed.

Source fingerprint: 634ec6c235fec90ba32ca4f23a759d988d9d7805e6a1bc951fffd35b55635ba5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### service

Resolve the cleanup implementation without loading Windows native APIs.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_empty_owned_residue_is_removed_after_release

Catch successful native profile deletion still leaving empty AC/Temp trees.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_nonempty_and_unowned_profiles_are_preserved

Never delete user files or another AgentiX version's sandbox.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_active_owner_is_never_recovered

Recovery must preserve another live process's recorded profile.

Kind: callable. Declared return: Not declared / class. Source line: 41.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| service | tmp_path | Parameter for tmp path in service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| service | ProfileCleanup | Imported dependency for ProfileCleanup in service; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_empty_owned_residue_is_removed_after_release | tmp_path | Parameter for tmp path in test_empty_owned_residue_is_removed_after_release; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_empty_owned_residue_is_removed_after_release | cleanup | Local binding for cleanup in test_empty_owned_residue_is_removed_after_release; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_empty_owned_residue_is_removed_after_release | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_empty_owned_residue_is_removed_after_release | folder | Local binding for folder in test_empty_owned_residue_is_removed_after_release; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_nonempty_and_unowned_profiles_are_preserved | tmp_path | Parameter for tmp path in test_nonempty_and_unowned_profiles_are_preserved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_nonempty_and_unowned_profiles_are_preserved | cleanup | Local binding for cleanup in test_nonempty_and_unowned_profiles_are_preserved; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_nonempty_and_unowned_profiles_are_preserved | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_nonempty_and_unowned_profiles_are_preserved | folder | Local binding for folder in test_nonempty_and_unowned_profiles_are_preserved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_active_owner_is_never_recovered | tmp_path | Parameter for tmp path in test_active_owner_is_never_recovered; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_active_owner_is_never_recovered | cleanup | Local binding for cleanup in test_active_owner_is_never_recovered; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_active_owner_is_never_recovered | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_active_owner_is_never_recovered | folder | Local binding for folder in test_active_owner_is_never_recovered; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_active_owner_is_never_recovered.lambda_48 | pid | Callback parameter for pid in test_active_owner_is_never_recovered.lambda_48; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 48 |
| test_active_owner_is_never_recovered.lambda_48 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 48 |
| test_active_owner_is_never_recovered.lambda_50 | pid | Callback parameter for pid in test_active_owner_is_never_recovered.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_active_owner_is_never_recovered.lambda_50 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_active_owner_is_never_recovered.lambda_52 | pid | Callback parameter for pid in test_active_owner_is_never_recovered.lambda_52; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 52 |
| test_active_owner_is_never_recovered.lambda_52 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 52 |
