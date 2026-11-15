# Reference for tests/test_composite_launch.py

LAB-005 standalone validation and GUI integration contract tests.

Source fingerprint: ca289d68621d8becc71b10f0d9627b57710195acf809373890104bb749574c39

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_launcher_rejects_occupied_port_before_staging

Catch expensive native startup and accidental fallback when a requested port is busy.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_application_panel_does_not_leak_error_bodies

Startup errors must not publish application code or exception text in UI/logs.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_application_panel_does_not_leak_error_bodies.Broken

Missing docstring: completion is blocked.

Kind: class. Declared return: Not declared / class. Source line: 33.

### test_application_panel_does_not_leak_error_bodies.Broken.open

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 34.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_launcher_rejects_occupied_port_before_staging | monkeypatch | Parameter for monkeypatch in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_launcher_rejects_occupied_port_before_staging | tmp_path | Parameter for tmp path in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_launcher_rejects_occupied_port_before_staging | package | Imported dependency for package in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_launcher_rejects_occupied_port_before_staging | application_digest | Imported dependency for application digest in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_launcher_rejects_occupied_port_before_staging | approve_application | Imported dependency for approve application in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| test_launcher_rejects_occupied_port_before_staging | ApplicationPreview | Imported dependency for ApplicationPreview in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_launcher_rejects_occupied_port_before_staging | folder | Local binding for folder in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_launcher_rejects_occupied_port_before_staging | approved | Local binding for approved in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| test_launcher_rejects_occupied_port_before_staging | entered | Local binding for entered in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 17 |
| test_launcher_rejects_occupied_port_before_staging.lambda_19 | self | Owning instance; its attributes retain state for the instance lifetime. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 19 |
| test_launcher_rejects_occupied_port_before_staging.lambda_19 | capability | Callback parameter for capability in test_launcher_rejects_occupied_port_before_staging.lambda_19; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 19 |
| test_launcher_rejects_occupied_port_before_staging | listener | Managed resource for listener in test_launcher_rejects_occupied_port_before_staging; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 21 |
| test_application_panel_does_not_leak_error_bodies | caplog | Parameter for caplog in test_application_panel_does_not_leak_error_bodies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_application_panel_does_not_leak_error_bodies | open_application | Imported dependency for open application in test_application_panel_does_not_leak_error_bodies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_application_panel_does_not_leak_error_bodies.Broken.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_application_panel_does_not_leak_error_bodies.Broken.open | owner | Parameter for owner in test_application_panel_does_not_leak_error_bodies.Broken.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_application_panel_does_not_leak_error_bodies.Broken.open | origin | Parameter for origin in test_application_panel_does_not_leak_error_bodies.Broken.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_application_panel_does_not_leak_error_bodies | rows | Local binding for rows in test_application_panel_does_not_leak_error_bodies; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
