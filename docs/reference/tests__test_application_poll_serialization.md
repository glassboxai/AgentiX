# Reference for tests/test_application_poll_serialization.py

Serialize application polling with opening/closing the same browser-owned preview.

Source fingerprint: 1d75959e028aaa77d148defded9fc1bd4c4129f9c486273a90a10da184555fc0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock

A stale dead-preview observation must not race a new preview/usage lease.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.resolve

Expose controlled owner state without a browser or filesystem.

Kind: callable. Declared return: Not declared / class. Source line: 24.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | controller | Local binding for controller in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | candidate | Local binding for candidate in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | session | Local binding for session in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | resolved | Local binding for resolved in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | closed | Local binding for closed in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.resolve | token | Parameter for token in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.resolve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.resolve | request | Parameter for request in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.resolve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | backend._resolve | Attribute for backend. resolve in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | backend._close | Attribute for backend. close in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock.lambda_30 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 30 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | thread | Local binding for thread in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | premature | Local binding for premature in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | Return type of wait; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock | controller.state.application_busy | Attribute for controller.state.application busy in test_poll_cannot_close_a_preview_while_an_open_transition_holds_owner_lock; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 36 |
