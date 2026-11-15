# Reference for tests/test_widget_panel.py

LAB-004 per-browser preview lifecycle using a boundary double, not native execution.

Source fingerprint: 95aaad2f475a2df50d0b3dca038462f52560a3024a328829ad76c9a8c5562572

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Preview

A finite listener/process boundary double with observable ownership.

Kind: class. Declared return: Not declared / class. Source line: 8.

### Preview.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### Preview.close

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_panel_reuses_only_own_live_preview_and_closes_only_owner

Catch cross-session sharing and accidental sibling shutdown.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_panel_capacity_and_expiry_reopen

Catch unbounded workers and stale dead-preview reuse.

Kind: callable. Declared return: Not declared / class. Source line: 32.

### test_iframe_rejects_nonlocal_or_injected_urls

Only supervisor-created loopback URLs can enter the maintained HTML.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### test_iframe_never_accepts_a_display_name_parameter

The isolated page titles itself from its snapshot; the frame carries only the URL.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_expired_other_owner_does_not_exhaust_capacity

A dead session must not prevent another browser from opening the widget.

Kind: callable. Declared return: Not declared / class. Source line: 60.

### test_close_during_startup_never_publishes_or_leaks_worker

A late startup cannot recreate a widget after its owner clicked Close.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_close_during_startup_never_publishes_or_leaks_worker.start

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 78.

### test_close_during_startup_never_publishes_or_leaks_worker.open_widget

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 87.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | WidgetPanel | Imported dependency for WidgetPanel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | iframe_html | Imported dependency for iframe html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| Preview.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| Preview.__init__ | self.url | Attribute for url in Preview.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 12 |
| Preview.__init__ | self.alive | Attribute for alive in Preview.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 13 |
| Preview.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| Preview.close | self.alive | Attribute for alive in Preview.close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 16 |
| test_panel_reuses_only_own_live_preview_and_closes_only_owner | panel | Local binding for panel in test_panel_reuses_only_own_live_preview_and_closes_only_owner; use the enclosing contract and type below. | Return type of WidgetPanel; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_panel_reuses_only_own_live_preview_and_closes_only_owner.lambda_21 | approved | Callback parameter for approved in test_panel_reuses_only_own_live_preview_and_closes_only_owner.lambda_21; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 21 |
| test_panel_reuses_only_own_live_preview_and_closes_only_owner.lambda_21 | origin | Callback parameter for origin in test_panel_reuses_only_own_live_preview_and_closes_only_owner.lambda_21; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 21 |
| test_panel_reuses_only_own_live_preview_and_closes_only_owner | first | Local binding for first in test_panel_reuses_only_own_live_preview_and_closes_only_owner; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_panel_reuses_only_own_live_preview_and_closes_only_owner | second | Local binding for second in test_panel_reuses_only_own_live_preview_and_closes_only_owner; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_panel_capacity_and_expiry_reopen | panel | Local binding for panel in test_panel_capacity_and_expiry_reopen; use the enclosing contract and type below. | Return type of WidgetPanel; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_panel_capacity_and_expiry_reopen.lambda_34 | approved | Callback parameter for approved in test_panel_capacity_and_expiry_reopen.lambda_34; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 34 |
| test_panel_capacity_and_expiry_reopen.lambda_34 | origin | Callback parameter for origin in test_panel_capacity_and_expiry_reopen.lambda_34; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 34 |
| test_panel_capacity_and_expiry_reopen | first | Local binding for first in test_panel_capacity_and_expiry_reopen; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_iframe_rejects_nonlocal_or_injected_urls | url | Parameter for url in test_iframe_rejects_nonlocal_or_injected_urls; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_expired_other_owner_does_not_exhaust_capacity | panel | Local binding for panel in test_expired_other_owner_does_not_exhaust_capacity; use the enclosing contract and type below. | Return type of WidgetPanel; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_expired_other_owner_does_not_exhaust_capacity.lambda_62 | approved | Callback parameter for approved in test_expired_other_owner_does_not_exhaust_capacity.lambda_62; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 62 |
| test_expired_other_owner_does_not_exhaust_capacity.lambda_62 | origin | Callback parameter for origin in test_expired_other_owner_does_not_exhaust_capacity.lambda_62; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 62 |
| test_expired_other_owner_does_not_exhaust_capacity | first | Local binding for first in test_expired_other_owner_does_not_exhaust_capacity; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_close_during_startup_never_publishes_or_leaks_worker | threading | Imported dependency for threading in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_close_during_startup_never_publishes_or_leaks_worker | entered | Local binding for entered in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 75 |
| test_close_during_startup_never_publishes_or_leaks_worker | release | Local binding for release in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 75 |
| test_close_during_startup_never_publishes_or_leaks_worker | created | Local binding for created in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 76 |
| test_close_during_startup_never_publishes_or_leaks_worker | errors | Local binding for errors in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 76 |
| test_close_during_startup_never_publishes_or_leaks_worker.start | approved | Parameter for approved in test_close_during_startup_never_publishes_or_leaks_worker.start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 78 |
| test_close_during_startup_never_publishes_or_leaks_worker.start | origin | Parameter for origin in test_close_during_startup_never_publishes_or_leaks_worker.start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 78 |
| test_close_during_startup_never_publishes_or_leaks_worker.start | preview | Local binding for preview in test_close_during_startup_never_publishes_or_leaks_worker.start; use the enclosing contract and type below. | Return type of Preview; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_close_during_startup_never_publishes_or_leaks_worker | panel | Local binding for panel in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | Return type of WidgetPanel; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_close_during_startup_never_publishes_or_leaks_worker.open_widget | error | Caught exception for error in test_close_during_startup_never_publishes_or_leaks_worker.open_widget; use the enclosing contract and type below. | RuntimeError | Current exception handler; Python clears this binding afterward | 90 |
| test_close_during_startup_never_publishes_or_leaks_worker | thread | Local binding for thread in test_close_during_startup_never_publishes_or_leaks_worker; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
