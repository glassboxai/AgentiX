# Reference for tests/test_v7_072_application_refresh.py

V7-072: a refresh control reloads the already validated generated application.

Source fingerprint: c57ff5d91b4cb242101b7630b6969b50c7b7d8d7e365418bb46983441df06b51

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_v7_072_worker_registers_a_refresh_toolbar_control

The isolated child owns the control; it adds no callback, route or capability.

Kind: callable. Declared return: None. Source line: 8.

### test_v7_072_refresh_stays_outside_the_movable_layout_allowlist

Toolbar identity must never become persisted geometry or a hidden control.

Kind: callable. Declared return: None. Source line: 17.

### test_v7_072_stylesheet_places_refresh_left_of_play

The maintained sheet keeps one compact toolbar row with the refresh icon.

Kind: callable. Declared return: None. Source line: 40.

### test_v7_072_refresh_reloads_the_page_and_sits_left_of_play

A real Chromium click reloads the document and re-runs the maintained editor.

Kind: callable. Declared return: None. Source line: 53.

### test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.route

Serve inert HTML, count document loads and answer the layout probe.

Kind: callable. Declared return: None. Source line: 87.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_v7_072_worker_registers_a_refresh_toolbar_control | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_v7_072_worker_registers_a_refresh_toolbar_control | block | Local binding for block in test_v7_072_worker_registers_a_refresh_toolbar_control; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_v7_072_refresh_stays_outside_the_movable_layout_allowlist | application_layout_ids | Imported dependency for application layout ids in test_v7_072_refresh_stays_outside_the_movable_layout_allowlist; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_v7_072_refresh_stays_outside_the_movable_layout_allowlist | validate_layout | Imported dependency for validate layout in test_v7_072_refresh_stays_outside_the_movable_layout_allowlist; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_v7_072_refresh_stays_outside_the_movable_layout_allowlist | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 21 |
| test_v7_072_refresh_stays_outside_the_movable_layout_allowlist | allowed | Local binding for allowed in test_v7_072_refresh_stays_outside_the_movable_layout_allowlist; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_v7_072_refresh_stays_outside_the_movable_layout_allowlist | rectangle | Local binding for rectangle in test_v7_072_refresh_stays_outside_the_movable_layout_allowlist; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 29 |
| test_v7_072_stylesheet_places_refresh_left_of_play | stylesheet | Imported dependency for stylesheet in test_v7_072_stylesheet_places_refresh_left_of_play; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| test_v7_072_stylesheet_places_refresh_left_of_play | css | Local binding for css in test_v7_072_stylesheet_places_refresh_left_of_play; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | os | Imported dependency for os in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 55 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | expect | Imported dependency for expect in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 57 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | sync_playwright | Imported dependency for sync playwright in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 57 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | application_layout_ids | Imported dependency for application layout ids in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 59 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 61 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | allowed | Local binding for allowed in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | positions | Local binding for positions in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 68 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.comprehension_68 | index | Comprehension item for index in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.comprehension_68; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 70 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.comprehension_68 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 70 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | html | Local binding for html in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.comprehension_79 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 81 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | documents | Local binding for documents in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 85 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.route | request_route | Parameter for request route in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.route | request | Local binding for request in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | driver | Managed resource for driver in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 105 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | browser | Local binding for browser in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | page | Local binding for page in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | refresh | Local binding for refresh in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_v7_072_refresh_reloads_the_page_and_sits_left_of_play | play_box | Local binding for play box in test_v7_072_refresh_reloads_the_page_and_sits_left_of_play; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
