# Reference for tests/test_startup_timings.py

Timing diagnostics preserve failures without logging source/prompt bodies.

Source fingerprint: f038d1d0e996e0993a57621e17d46fba6815550d850c7e542f7bccf26f3c41f4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_failed_staging_keeps_safe_duration_and_cleans_owned_tree

Catch missing startup failure diagnostics and leaked partial private runtimes.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_failed_staging_keeps_safe_duration_and_cleans_owned_tree.failed

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### test_invalid_child_timings_cannot_enter_diagnostics

Diagnostic channel rejects arbitrary fields, coercion and nonfinite durations.

Kind: callable. Declared return: Not declared / class. Source line: 34.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | WidgetSession | Imported dependency for WidgetSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_failed_staging_keeps_safe_duration_and_cleans_owned_tree | monkeypatch | Parameter for monkeypatch in test_failed_staging_keeps_safe_duration_and_cleans_owned_tree; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_failed_staging_keeps_safe_duration_and_cleans_owned_tree | module | Imported dependency for module in test_failed_staging_keeps_safe_duration_and_cleans_owned_tree; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_failed_staging_keeps_safe_duration_and_cleans_owned_tree.failed | root | Explicit root directory against which named paths are resolved. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| test_failed_staging_keeps_safe_duration_and_cleans_owned_tree | session | Local binding for session in test_failed_staging_keeps_safe_duration_and_cleans_owned_tree; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| test_invalid_child_timings_cannot_enter_diagnostics | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_invalid_child_timings_cannot_enter_diagnostics | session | Local binding for session in test_invalid_child_timings_cannot_enter_diagnostics; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
