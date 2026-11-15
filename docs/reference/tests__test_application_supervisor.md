# Reference for tests/test_application_supervisor.py

Fail-closed supervisor regressions using explicit native/browser doubles.

Source fingerprint: b4060c53b6fc61d9685a3712ec4a1767be8a12876c05abef6d00211d3f1de944

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### candidate

Build a reviewed schema-3 fixture in independently owned storage.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_approval_binds_displayed_identity_and_bytes

Catch stale-click approval and post-review dependency changes.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_independent_native_mismatch_never_starts_gui

Catch treating a validly shaped wrong result as functional acceptance.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_independent_native_mismatch_never_starts_gui.forbidden

Fail if a rejected result reaches a boundary that must remain unused.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_failed_browser_closes_owned_preview_and_keeps_evidence

Catch leaking a worker or retaining a verified grant after GUI failure.

Kind: callable. Declared return: Not declared / class. Source line: 49.

### test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview

Represent only the owned native-preview boundary for cleanup assertions.

Kind: class. Declared return: Not declared / class. Source line: 53.

### test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview.close

Record that the owned preview was closed after verification failure.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_failed_browser_closes_owned_preview_and_keeps_evidence.browser

Write a controlled failed acceptance receipt and propagate the mismatch.

Kind: callable. Declared return: Not declared / class. Source line: 65.

### test_failed_verification_never_publishes_widget_approval

A human checkbox alone must not create a persistent reusable widget.

Kind: callable. Declared return: Not declared / class. Source line: 86.

### test_failed_verification_never_publishes_widget_approval.Preview

Represent owned preview cleanup at the explicit boundary double.

Kind: class. Declared return: Not declared / class. Source line: 92.

### test_failed_verification_never_publishes_widget_approval.Preview.close

Dispose the inert fixture after the controlled browser failure.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### test_failed_verification_never_publishes_widget_approval.fail

Simulate a failed independent result comparison.

Kind: callable. Declared return: Not declared / class. Source line: 101.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| candidate | tmp_path | Parameter for tmp path in candidate; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| candidate | build | Imported dependency for build in candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_approval_binds_displayed_identity_and_bytes | tmp_path | Parameter for tmp path in test_approval_binds_displayed_identity_and_bytes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_approval_binds_displayed_identity_and_bytes | item | Local binding for item in test_approval_binds_displayed_identity_and_bytes; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_approval_binds_displayed_identity_and_bytes | supervisor | Local binding for supervisor in test_approval_binds_displayed_identity_and_bytes; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_independent_native_mismatch_never_starts_gui | tmp_path | Parameter for tmp path in test_independent_native_mismatch_never_starts_gui; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_independent_native_mismatch_never_starts_gui | item | Local binding for item in test_independent_native_mismatch_never_starts_gui; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_independent_native_mismatch_never_starts_gui.forbidden | args | Parameter for args in test_independent_native_mismatch_never_starts_gui.forbidden; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_independent_native_mismatch_never_starts_gui.forbidden | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_independent_native_mismatch_never_starts_gui | supervisor | Local binding for supervisor in test_independent_native_mismatch_never_starts_gui; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence | tmp_path | Parameter for tmp path in test_failed_browser_closes_owned_preview_and_keeps_evidence; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence | item | Local binding for item in test_failed_browser_closes_owned_preview_and_keeps_evidence; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview | closed | Local binding for closed in test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 56 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview | url | Local binding for url in test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 57 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview.close | self.closed | Attribute for closed in test_failed_browser_closes_owned_preview_and_keeps_evidence.Preview.close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 61 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence | preview | Local binding for preview in test_failed_browser_closes_owned_preview_and_keeps_evidence; use the enclosing contract and type below. | Return type of Preview; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence.browser | args | Parameter for args in test_failed_browser_closes_owned_preview_and_keeps_evidence.browser; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence | supervisor | Local binding for supervisor in test_failed_browser_closes_owned_preview_and_keeps_evidence; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_failed_browser_closes_owned_preview_and_keeps_evidence | report | Local binding for report in test_failed_browser_closes_owned_preview_and_keeps_evidence; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_failed_verification_never_publishes_widget_approval | tmp_path | Parameter for tmp path in test_failed_verification_never_publishes_widget_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_failed_verification_never_publishes_widget_approval | item | Local binding for item in test_failed_verification_never_publishes_widget_approval; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_failed_verification_never_publishes_widget_approval | published | Local binding for published in test_failed_verification_never_publishes_widget_approval; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 89 |
| test_failed_verification_never_publishes_widget_approval | item.widget_commit | Attribute for item.widget commit in test_failed_verification_never_publishes_widget_approval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_failed_verification_never_publishes_widget_approval.lambda_90 | item | Callback parameter for item in test_failed_verification_never_publishes_widget_approval.lambda_90; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 90 |
| test_failed_verification_never_publishes_widget_approval.Preview | url | Local binding for url in test_failed_verification_never_publishes_widget_approval.Preview; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 95 |
| test_failed_verification_never_publishes_widget_approval.Preview.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_failed_verification_never_publishes_widget_approval.fail | args | Parameter for args in test_failed_verification_never_publishes_widget_approval.fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_failed_verification_never_publishes_widget_approval | supervisor | Local binding for supervisor in test_failed_verification_never_publishes_widget_approval; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
