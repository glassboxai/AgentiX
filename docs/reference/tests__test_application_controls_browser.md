# Reference for tests/test_application_controls_browser.py

Actual browser cancellation/restart and native owned-process cleanup.

Source fingerprint: f7622811ace1ddbc3f146855b4fda16e950911e1d9e27cdb316bfb70862c390a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_toolbar_stops_and_restarts_same_reviewed_snapshot

Cancel a slow trusted callback, retain its listener, resume and close its job.

Kind: callable. Declared return: Not declared / class. Source line: 16.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | schema3_package | Imported dependency for schema3 package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ApplicationPreview | Imported dependency for ApplicationPreview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | tmp_path | Parameter for tmp path in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | expect | Imported dependency for expect in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | sync_playwright | Imported dependency for sync playwright in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | check_analysis | Imported dependency for check analysis in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | package | Local binding for package in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | tool | Local binding for tool in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | record | Local binding for record in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot.comprehension_38 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | snapshot | Local binding for snapshot in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | preview | Local binding for preview in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of ApplicationPreview; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | first_session | Local binding for first session in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | driver | Managed resource for driver in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 46 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | browser | Local binding for browser in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_native_toolbar_stops_and_restarts_same_reviewed_snapshot | page | Local binding for page in test_native_toolbar_stops_and_restarts_same_reviewed_snapshot; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
