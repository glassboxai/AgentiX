# Reference for tests/test_persistent_application.py

Regression coverage for persistent previews with finite operations.

Source fingerprint: f752e9c39c73fbe63dced98917059e475bfde06fd8e276e048e5ae55331cf00e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### capability

Explicitly review a generated schema-3 fixture, never existing artifacts.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_persistent_gui_does_not_expire_when_idle

Catch applying the headless duration cap to an idle interactive application.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_callback_timeout_cancels_owned_application

Catch infinite callbacks surviving a persistent GUI's operation budget.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### test_finished_callback_releases_lease

Catch expired completed work stopping an otherwise idle application.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_headless_cannot_select_unlimited_lifetime

Catch removing execution deadlines from reusable data operations.

Kind: callable. Declared return: Not declared / class. Source line: 56.

### test_concurrent_close_waits_for_owned_cleanup

Catch returning from a second close before the first has released resources.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_concurrent_close_waits_for_owned_cleanup.Temporary

Hold the external filesystem cleanup boundary deterministically.

Kind: class. Declared return: Not declared / class. Source line: 68.

### test_concurrent_close_waits_for_owned_cleanup.Temporary.cleanup

Block cleanup until both callers have reached the close protocol.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_concurrent_close_waits_for_owned_cleanup.close_again

Observe completion of the concurrent caller, not just its invocation.

Kind: callable. Declared return: Not declared / class. Source line: 80.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ApplicationSession | Imported dependency for ApplicationSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| capability | tmp_path | Parameter for tmp path in capability; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| capability | package | Imported dependency for package in capability; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 11 |
| capability | folder | Local binding for folder in capability; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_persistent_gui_does_not_expire_when_idle | tmp_path | Parameter for tmp path in test_persistent_gui_does_not_expire_when_idle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_persistent_gui_does_not_expire_when_idle | session | Local binding for session in test_persistent_gui_does_not_expire_when_idle; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_callback_timeout_cancels_owned_application | tmp_path | Parameter for tmp path in test_callback_timeout_cancels_owned_application; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| test_callback_timeout_cancels_owned_application | session | Local binding for session in test_callback_timeout_cancels_owned_application; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_callback_timeout_cancels_owned_application | session.clock | Attribute for session.clock in test_callback_timeout_cancels_owned_application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32, 34 |
| test_finished_callback_releases_lease | tmp_path | Parameter for tmp path in test_finished_callback_releases_lease; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| test_finished_callback_releases_lease | session | Local binding for session in test_finished_callback_releases_lease; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_finished_callback_releases_lease | session.clock | Attribute for session.clock in test_finished_callback_releases_lease; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46, 49 |
| test_headless_cannot_select_unlimited_lifetime | tmp_path | Parameter for tmp path in test_headless_cannot_select_unlimited_lifetime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
| test_concurrent_close_waits_for_owned_cleanup | tmp_path | Parameter for tmp path in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_concurrent_close_waits_for_owned_cleanup | threading | Imported dependency for threading in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 64 |
| test_concurrent_close_waits_for_owned_cleanup | entered | Local binding for entered in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_concurrent_close_waits_for_owned_cleanup | release | Local binding for release in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_concurrent_close_waits_for_owned_cleanup | second_started | Local binding for second started in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_concurrent_close_waits_for_owned_cleanup | second_done | Local binding for second done in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_concurrent_close_waits_for_owned_cleanup.comprehension_66 | _ | Comprehension item for  in test_concurrent_close_waits_for_owned_cleanup.comprehension_66; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 66 |
| test_concurrent_close_waits_for_owned_cleanup.Temporary.cleanup | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_concurrent_close_waits_for_owned_cleanup | session | Local binding for session in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_concurrent_close_waits_for_owned_cleanup | session.temporary | Attribute for session.temporary in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Return type of Temporary; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_concurrent_close_waits_for_owned_cleanup | first | Local binding for first in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_concurrent_close_waits_for_owned_cleanup | second | Local binding for second in test_concurrent_close_waits_for_owned_cleanup; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
