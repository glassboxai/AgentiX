# Reference for tests/unit/test_sessions.py

Session tokens and activity must not cross workflow owners.

Source fingerprint: af9abb71fa7b7c4853b076e1f13ac71cf686d9355296d7160225d13d1738dfa3

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_session_registry_binds_token_to_owner

Verify session registry binds token to owner.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_activity_routing_is_context_local_across_threads

Verify activity routing is context local across threads.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### test_activity_routing_is_context_local_across_threads.worker

Provide worker for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_session_expiry_capacity_and_owner_checked_close

Verify session expiry capacity and owner checked close.

Kind: callable. Declared return: Not declared / class. Source line: 56.

### test_activity_buffer_is_bounded

Verify activity buffer is bounded.

Kind: callable. Declared return: Not declared / class. Source line: 85.

### test_diagnostic_session_id_is_not_the_browser_capability_token

Verify diagnostic session id is not the browser capability token.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_diagnostic_session_id_is_not_the_browser_capability_token.create

Provide create for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 102.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | io | Imported dependency for io in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_session_registry_binds_token_to_owner | SessionAccessError | Imported dependency for SessionAccessError in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_session_registry_binds_token_to_owner | SessionRegistry | Imported dependency for SessionRegistry in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_session_registry_binds_token_to_owner | registry | Local binding for registry in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_session_registry_binds_token_to_owner.lambda_15 | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 15 |
| test_session_registry_binds_token_to_owner | alice | Local binding for alice in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_session_registry_binds_token_to_owner | bob | Local binding for bob in test_session_registry_binds_token_to_owner; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_activity_routing_is_context_local_across_threads | ActivityRouter | Imported dependency for ActivityRouter in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| test_activity_routing_is_context_local_across_threads | operation_scope | Imported dependency for operation scope in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 30 |
| test_activity_routing_is_context_local_across_threads | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_activity_routing_is_context_local_across_threads | host | Local binding for host in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of StringIO; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_activity_routing_is_context_local_across_threads | router | Local binding for router in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of ActivityRouter; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_activity_routing_is_context_local_across_threads | first | Local binding for first in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 35 |
| test_activity_routing_is_context_local_across_threads | second | Local binding for second in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 35 |
| test_activity_routing_is_context_local_across_threads | barrier | Local binding for barrier in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Return type of Barrier; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_activity_routing_is_context_local_across_threads.worker | capture | Parameter for capture in test_activity_routing_is_context_local_across_threads.worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_activity_routing_is_context_local_across_threads.worker | owner | Parameter for owner in test_activity_routing_is_context_local_across_threads.worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_activity_routing_is_context_local_across_threads | workers | Local binding for workers in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 44 |
| test_activity_routing_is_context_local_across_threads | worker | Loop item for worker in test_activity_routing_is_context_local_across_threads; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 48, 50 |
| test_session_expiry_capacity_and_owner_checked_close | SessionAccessError | Imported dependency for SessionAccessError in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_session_expiry_capacity_and_owner_checked_close | SessionRegistry | Imported dependency for SessionRegistry in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_session_expiry_capacity_and_owner_checked_close | cancelled | Local binding for cancelled in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 60 |
| test_session_expiry_capacity_and_owner_checked_close | now | Local binding for now in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 61 |
| test_session_expiry_capacity_and_owner_checked_close | registry | Local binding for registry in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_session_expiry_capacity_and_owner_checked_close.lambda_63 | token | Callback parameter for token in test_session_expiry_capacity_and_owner_checked_close.lambda_63; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 63 |
| test_session_expiry_capacity_and_owner_checked_close | alice | Local binding for alice in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_session_expiry_capacity_and_owner_checked_close | bob | Local binding for bob in test_session_expiry_capacity_and_owner_checked_close; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_activity_buffer_is_bounded | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 87 |
| test_activity_buffer_is_bounded | capture | Local binding for capture in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Return type of ConsoleThoughtsCapture; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_activity_buffer_is_bounded | index | Loop item for index in test_activity_buffer_is_bounded; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 90 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | SessionRegistry | Imported dependency for SessionRegistry in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | identities | Local binding for identities in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 100 |
| test_diagnostic_session_id_is_not_the_browser_capability_token.create | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 102 |
| test_diagnostic_session_id_is_not_the_browser_capability_token | session | Local binding for session in test_diagnostic_session_id_is_not_the_browser_capability_token; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
