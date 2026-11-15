# Reference for tests/test_explorer_window.py

V7-065: the Explorer window opened for a catalog folder is raised above the browser.

Source fingerprint: 66cd69b0bd76f365c35720dbf6670f9c99a3d773f35815e76cda66be53a5441f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### focus

Compose the focus helper over injected native boundaries, never real windows.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_focus_prefers_the_window_that_appeared_after_opening

A new CabinetWClass handle wins over an older window with a similar title.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### test_focus_falls_back_to_the_localized_title_prefix

Explorer reuses an open folder, so no new handle appears and the title decides.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_focus_ignores_a_folder_whose_name_only_shares_a_prefix

A sibling folder such as tools_archive must not be raised for tools.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### test_focus_polls_until_the_timeout_without_sleeping_for_real

A slow shell is awaited with a bounded number of injected clock/sleep calls.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_focus_reports_a_native_raise_failure

A refused SetWindowPos/SetForegroundWindow surfaces as an OSError, not silence.

Kind: callable. Declared return: Not declared / class. Source line: 84.

### test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows

Non-Windows hosts enumerate nothing and never call a native function.

Kind: callable. Declared return: Not declared / class. Source line: 95.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| focus | overrides | Parameter for overrides in focus; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| focus | ExplorerWindowFocus | Imported dependency for ExplorerWindowFocus in focus; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 8 |
| focus | options | Local binding for options in focus; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| focus.lambda_12 | hwnd | Callback parameter for hwnd in focus.lambda_12; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 12 |
| focus.lambda_13 | hwnd | Callback parameter for hwnd in focus.lambda_13; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 13 |
| focus.lambda_15 | seconds | Callback parameter for seconds in focus.lambda_15; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 15 |
| test_focus_prefers_the_window_that_appeared_after_opening | raised | Local binding for raised in test_focus_prefers_the_window_that_appeared_after_opening; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 25 |
| test_focus_prefers_the_window_that_appeared_after_opening | helper | Local binding for helper in test_focus_prefers_the_window_that_appeared_after_opening; use the enclosing contract and type below. | Return type of focus; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_focus_prefers_the_window_that_appeared_after_opening.lambda_28 | hwnd | Callback parameter for hwnd in test_focus_prefers_the_window_that_appeared_after_opening.lambda_28; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 28 |
| test_focus_prefers_the_window_that_appeared_after_opening.lambda_29 | hwnd | Callback parameter for hwnd in test_focus_prefers_the_window_that_appeared_after_opening.lambda_29; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 29 |
| test_focus_falls_back_to_the_localized_title_prefix | raised | Local binding for raised in test_focus_falls_back_to_the_localized_title_prefix; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 37 |
| test_focus_falls_back_to_the_localized_title_prefix | ticks | Local binding for ticks in test_focus_falls_back_to_the_localized_title_prefix; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_focus_falls_back_to_the_localized_title_prefix | titles | Local binding for titles in test_focus_falls_back_to_the_localized_title_prefix; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 39 |
| test_focus_falls_back_to_the_localized_title_prefix | helper | Local binding for helper in test_focus_falls_back_to_the_localized_title_prefix; use the enclosing contract and type below. | Return type of focus; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_focus_falls_back_to_the_localized_title_prefix.lambda_47 | hwnd | Callback parameter for hwnd in test_focus_falls_back_to_the_localized_title_prefix.lambda_47; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 47 |
| test_focus_ignores_a_folder_whose_name_only_shares_a_prefix | raised | Local binding for raised in test_focus_ignores_a_folder_whose_name_only_shares_a_prefix; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 56 |
| test_focus_ignores_a_folder_whose_name_only_shares_a_prefix | ticks | Local binding for ticks in test_focus_ignores_a_folder_whose_name_only_shares_a_prefix; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_focus_ignores_a_folder_whose_name_only_shares_a_prefix | titles | Local binding for titles in test_focus_ignores_a_folder_whose_name_only_shares_a_prefix; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 58 |
| test_focus_ignores_a_folder_whose_name_only_shares_a_prefix | helper | Local binding for helper in test_focus_ignores_a_folder_whose_name_only_shares_a_prefix; use the enclosing contract and type below. | Return type of focus; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_focus_ignores_a_folder_whose_name_only_shares_a_prefix.lambda_62 | hwnd | Callback parameter for hwnd in test_focus_ignores_a_folder_whose_name_only_shares_a_prefix.lambda_62; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 62 |
| test_focus_polls_until_the_timeout_without_sleeping_for_real | ticks | Local binding for ticks in test_focus_polls_until_the_timeout_without_sleeping_for_real; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_focus_polls_until_the_timeout_without_sleeping_for_real | sleeps | Local binding for sleeps in test_focus_polls_until_the_timeout_without_sleeping_for_real; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 72 |
| test_focus_polls_until_the_timeout_without_sleeping_for_real | helper | Local binding for helper in test_focus_polls_until_the_timeout_without_sleeping_for_real; use the enclosing contract and type below. | Return type of focus; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_focus_reports_a_native_raise_failure | helper | Local binding for helper in test_focus_reports_a_native_raise_failure; use the enclosing contract and type below. | Return type of focus; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_focus_reports_a_native_raise_failure.lambda_88 | hwnd | Callback parameter for hwnd in test_focus_reports_a_native_raise_failure.lambda_88; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 88 |
| test_focus_reports_a_native_raise_failure.lambda_89 | hwnd | Callback parameter for hwnd in test_focus_reports_a_native_raise_failure.lambda_89; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 89 |
| test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows | monkeypatch | Parameter for monkeypatch in test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows | explorer_window | Imported dependency for explorer window in test_focus_is_a_no_op_when_the_platform_has_no_cabinet_windows; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 97 |
