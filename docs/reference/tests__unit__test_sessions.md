# Reference for tests/unit/test_sessions.py

Session tokens and activity must not cross workflow owners.

Source fingerprint: 31cecd3a9c0ceef8acdbd424e907b9176119f1e2f33219f654cf1c4b4bc4e1ab

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_session_registry_binds_token_to_owner

Verify session registry binds token to owner.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_activity_routing_is_context_local_across_threads

Verify activity routing is context local across threads.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_activity_routing_is_context_local_across_threads.worker

Provide worker for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### test_session_expiry_capacity_and_owner_checked_close

Verify session expiry capacity and owner checked close.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_activity_buffer_is_bounded

Verify activity buffer is bounded.

Kind: callable. Declared return: Not declared / class. Source line: 86.

### test_diagnostic_session_id_is_not_the_browser_capability_token

Verify diagnostic session id is not the browser capability token.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### test_diagnostic_session_id_is_not_the_browser_capability_token.create

Provide create for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 103.

### test_session_lifecycle_events_exclude_browser_capabilities

Record session creation and expiry without leaking browser identity data.

Kind: callable. Declared return: None. Source line: 112.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | io | Imported dependency for io in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| test_session_registry_binds_token_to_owner | SessionAccessError | Imported dependency for SessionAccessError in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_session_registry_binds_token_to_owner | SessionRegistry | Imported dependency for SessionRegistry in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_session_registry_binds_token_to_owner | registry | Local binding for registry in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_session_registry_binds_token_to_owner.lambda_16 | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 16 |
| test_session_registry_binds_token_to_owner | alice | Local binding for alice in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_session_registry_binds_token_to_owner | bob | Local binding for bob in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_activity_routing_is_context_local_across_threads | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_activity_routing_is_context_local_across_threads | ActivityRouter | Imported dependency for ActivityRouter in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
| test_activity_routing_is_context_local_across_threads | operation_scope | Imported dependency for operation scope in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
| test_activity_routing_is_context_local_across_threads | host | Local binding for host in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of StringIO; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_activity_routing_is_context_local_across_threads | router | Local binding for router in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of ActivityRouter; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_activity_routing_is_context_local_across_threads | first | Local binding for first in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| test_activity_routing_is_context_local_across_threads | second | Local binding for second in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| test_activity_routing_is_context_local_across_threads | barrier | Local binding for barrier in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of Barrier; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_activity_routing_is_context_local_across_threads.worker | capture | Parameter for capture in test_activity_routing_is_context_local_across_threads.worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_activity_routing_is_context_local_across_threads.worker | owner | Parameter for owner in test_activity_routing_is_context_local_across_threads.worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_activity_routing_is_context_local_across_threads | workers | Local binding for workers in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 45 |
| test_activity_routing_is_context_local_across_threads | worker | Loop item for worker in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 49, 51 |
| test_session_expiry_capacity_and_owner_checked_close | SessionAccessError | Imported dependency for SessionAccessError in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 59 |
| test_session_expiry_capacity_and_owner_checked_close | SessionRegistry | Imported dependency for SessionRegistry in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 59 |
| test_session_expiry_capacity_and_owner_checked_close | cancelled | Local binding for cancelled in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 61 |
| test_session_expiry_capacity_and_owner_checked_close | now | Local binding for now in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 62 |
| test_session_expiry_capacity_and_owner_checked_close | registry | Local binding for registry in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_session_expiry_capacity_and_owner_checked_close.lambda_64 | token | Callback parameter for token in test_session_expiry_capacity_and_owner_checked_close.lambda_64; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_session_expiry_capacity_and_owner_checked_close | alice | Local binding for alice in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_session_expiry_capacity_and_owner_checked_close | bob | Local binding for bob in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_activity_buffer_is_bounded | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 88 |
| test_activity_buffer_is_bounded | capture | Local binding for capture in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Return type of ConsoleThoughtsCapture; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_activity_buffer_is_bounded | index | Loop item for index in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 91 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | SessionRegistry | Imported dependency for SessionRegistry in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 99 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | identities | Local binding for identities in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 101 |
| test_diagnostic_session_id_is_not_the_browser_capability_token.create | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 103 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | session | Local binding for session in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_session_lifecycle_events_exclude_browser_capabilities | caplog | Parameter for caplog in test_session_lifecycle_events_exclude_browser_capabilities; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 113 |
| test_session_lifecycle_events_exclude_browser_capabilities | SessionRegistry | Imported dependency for SessionRegistry in test_session_lifecycle_events_exclude_browser_capabilities; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 116 |
| test_session_lifecycle_events_exclude_browser_capabilities | now | Local binding for now in test_session_lifecycle_events_exclude_browser_capabilities; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 118 |
| test_session_lifecycle_events_exclude_browser_capabilities | registry | Local binding for registry in test_session_lifecycle_events_exclude_browser_capabilities; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_session_lifecycle_events_exclude_browser_capabilities.lambda_120 | _session_id | Callback parameter for session id in test_session_lifecycle_events_exclude_browser_capabilities.lambda_120; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 120 |
| test_session_lifecycle_events_exclude_browser_capabilities | session | Local binding for session in test_session_lifecycle_events_exclude_browser_capabilities; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
