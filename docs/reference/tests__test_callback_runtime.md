# Reference for tests/test_callback_runtime.py

Callback leases preserve actual callable semantics without native dependencies.

Source fingerprint: 6827de08fe56d3ecdfa2fafed80a1dce1b24939d395e251e4574c80ddff88948

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_sync_error_releases_the_operation_lease

Catch lingering leases after normal exception propagation.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_sync_error_releases_the_operation_lease.broken

Raise a controlled callback error to exercise lease release.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_generator_close_releases_the_operation_lease

Catch either eager iteration or leaked cancelled-generator leases.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_generator_close_releases_the_operation_lease.source

Produce literal fixture values while preserving callable lifecycle semantics.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_async_result_preserves_coroutine_contract

Catch converting async callbacks into unsupported synchronous wrappers.

Kind: callable. Declared return: Not declared / class. Source line: 43.

### test_async_result_preserves_coroutine_contract.source

Produce literal fixture values while preserving callable lifecycle semantics.

Kind: callable. Declared return: Not declared / class. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | asyncio | Imported dependency for asyncio in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | supervise_callback | Imported dependency for supervise callback in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| test_sync_error_releases_the_operation_lease | messages | Local binding for messages in test_sync_error_releases_the_operation_lease; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 13 |
| test_sync_error_releases_the_operation_lease.comprehension_21 | message | Comprehension item for message in test_sync_error_releases_the_operation_lease.comprehension_21; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 21 |
| test_generator_close_releases_the_operation_lease | messages | Local binding for messages in test_generator_close_releases_the_operation_lease; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 27 |
| test_generator_close_releases_the_operation_lease | wrapped | Local binding for wrapped in test_generator_close_releases_the_operation_lease; use the enclosing contract and type below. | Return type of supervise_callback; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_generator_close_releases_the_operation_lease | iterator | Local binding for iterator in test_generator_close_releases_the_operation_lease; use the enclosing contract and type below. | Return type of wrapped; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_async_result_preserves_coroutine_contract | messages | Local binding for messages in test_async_result_preserves_coroutine_contract; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 45 |
| test_async_result_preserves_coroutine_contract | wrapped | Local binding for wrapped in test_async_result_preserves_coroutine_contract; use the enclosing contract and type below. | Return type of supervise_callback; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
