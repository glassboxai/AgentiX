# Reference for tests/test_activity_indicator.py

Central activity state is owner-scoped and yields to human review.

Source fingerprint: 2299c6bb0bca18b5107bf65202a6fd5ab985999790fb655422308daff37d7eb5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_background_execution_is_visible_and_pending_review_is_not_blocked

Fast query-submit callbacks must not hide the actual background workload.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_foreign_owner_cannot_poll_another_sessions_processing_state

Activity information must use the same ownership checks as business state.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_application_activity_describes_the_actual_phase

A data run must never be presented as model generation or verification.

Kind: callable. Declared return: Not declared / class. Source line: 52.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | registry | Imported dependency for registry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | ActivityBackend | Imported dependency for ActivityBackend in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 11 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | sessions | Local binding for sessions in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner | Local binding for owner in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner.controller.security | Attribute for owner.controller.security in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | request | Local binding for request in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | service | Local binding for service in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Return type of ActivityBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner.controller.state.is_running | Attribute for owner.controller.state.is running in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 18, 22 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner.controller.security.get_pending_request | Attribute for owner.controller.security.get pending request in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20, 23 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner.controller.state.application_busy | Attribute for owner.controller.state.application busy in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 24, 27 |
| test_background_execution_is_visible_and_pending_review_is_not_blocked | owner.controller.state.application_phase | Attribute for owner.controller.state.application phase in test_background_execution_is_visible_and_pending_review_is_not_blocked; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 25 |
| test_foreign_owner_cannot_poll_another_sessions_processing_state | ActivityBackend | Imported dependency for ActivityBackend in test_foreign_owner_cannot_poll_another_sessions_processing_state; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| test_foreign_owner_cannot_poll_another_sessions_processing_state | SessionAccessError | Imported dependency for SessionAccessError in test_foreign_owner_cannot_poll_another_sessions_processing_state; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 34 |
| test_foreign_owner_cannot_poll_another_sessions_processing_state | sessions | Local binding for sessions in test_foreign_owner_cannot_poll_another_sessions_processing_state; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_foreign_owner_cannot_poll_another_sessions_processing_state | owner | Local binding for owner in test_foreign_owner_cannot_poll_another_sessions_processing_state; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_application_activity_describes_the_actual_phase | phase | Parameter for phase in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_application_activity_describes_the_actual_phase | label | Parameter for label in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| test_application_activity_describes_the_actual_phase | ActivityBackend | Imported dependency for ActivityBackend in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| test_application_activity_describes_the_actual_phase | sessions | Local binding for sessions in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_application_activity_describes_the_actual_phase | owner | Local binding for owner in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_application_activity_describes_the_actual_phase | owner.controller.state.application_busy | Attribute for owner.controller.state.application busy in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 58 |
| test_application_activity_describes_the_actual_phase | owner.controller.state.application_phase | Attribute for owner.controller.state.application phase in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_application_activity_describes_the_actual_phase | owner.controller.security | Attribute for owner.controller.security in test_application_activity_describes_the_actual_phase; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
