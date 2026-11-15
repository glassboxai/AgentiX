# Reference for src/agentix/lab/callback_runtime.py

Maintained callback lease instrumentation executed only in the native worker.

Leases let the host stop blocked reviewed callbacks. Child-originated messages
are not a proof that arbitrary malicious code reports its execution honestly.

Source fingerprint: 967c0256256d80271345af3724888e9a93526993a6cd63516a720ff73083d955

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### supervise_callback

Preserve sync/async/generator behavior while reporting a finite execution lease.

Kind: callable. Declared return: Callable. Source line: 13.

### supervise_callback.begin

Allocate an operation identity without including input or output data.

Kind: callable. Declared return: str. Source line: 16.

### supervise_callback.async_generator

Keep the lease through the complete async generator lifecycle.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### supervise_callback.coroutine

Await the callback under the host-observed lease.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### supervise_callback.generator

Release the lease even when iteration is cancelled or fails.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### supervise_callback.callback

Report bounded normal/error callback completion without artifact content.

Kind: callable. Declared return: Not declared / class. Source line: 61.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| supervise_callback | function | Parameter for function in supervise_callback; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 13 |
| supervise_callback | emit | Parameter for emit in supervise_callback; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 13 |
| supervise_callback.begin | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| supervise_callback.async_generator | args | Parameter for args in supervise_callback.async_generator; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| supervise_callback.async_generator | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| supervise_callback.async_generator | identity | Explicit owner identity used by a session factory or fixture. | Return type of begin; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| supervise_callback.async_generator | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 29 |
| supervise_callback.coroutine | args | Parameter for args in supervise_callback.coroutine; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| supervise_callback.coroutine | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| supervise_callback.coroutine | identity | Explicit owner identity used by a session factory or fixture. | Return type of begin; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| supervise_callback.generator | args | Parameter for args in supervise_callback.generator; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| supervise_callback.generator | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| supervise_callback.generator | identity | Explicit owner identity used by a session factory or fixture. | Return type of begin; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| supervise_callback.callback | args | Parameter for args in supervise_callback.callback; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| supervise_callback.callback | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| supervise_callback.callback | identity | Explicit owner identity used by a session factory or fixture. | Return type of begin; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
