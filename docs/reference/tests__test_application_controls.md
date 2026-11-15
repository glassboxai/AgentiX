# Reference for tests/test_application_controls.py

Owned application presentation routes require origin/token and bounded geometry.

Source fingerprint: 7abbf9bbb9d1ebf7c8ba34b9d3684a0d6033c70aa6d526e0ba93d97871446748

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### controls

Inject a protected temporary app and inert owned lifecycle methods.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_layout_save_requires_exact_origin_and_private_preview_token

A foreign page cannot write an app's presentation through loopback CSRF.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### test_layout_cannot_move_toolbar_or_execute_code

Only known canvas control IDs and numeric rectangles are persisted.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_layout_hidden_controls_roundtrip_and_reject_toolbar

V7-062: persisted visibility uses the same allowlist as geometry.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_owned_stop_restart_and_close_never_accept_a_path

Lifecycle controls act on this preview only and reject user-selected entries.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_duplicate_layout_keys_and_oversize_requests_are_rejected

Ambiguous or unbounded presentation input cannot reach persistent storage.

Kind: callable. Declared return: Not declared / class. Source line: 127.

### test_paused_preview_restarts_only_owned_snapshot

Lifecycle doubles establish ownership and cleanup, not native isolation.

Kind: callable. Declared return: Not declared / class. Source line: 140.

### test_revoked_dependencies_still_allow_owned_stop_and_close

A stale app must remain cancellable; only restart/save require its grant.

Kind: callable. Declared return: Not declared / class. Source line: 167.

### test_revoked_dependencies_still_allow_owned_stop_and_close.revoked

Represent a changed tool approval without modifying user storage.

Kind: callable. Declared return: Not declared / class. Source line: 171.

### test_changed_app_still_exposes_an_owned_close_token

A tampered source disables layout editing but cannot strand the stopped page.

Kind: callable. Declared return: Not declared / class. Source line: 187.

### test_changed_app_still_exposes_an_owned_close_token.unavailable

Simulate a protected source identity mismatch.

Kind: callable. Declared return: Not declared / class. Source line: 191.

### test_application_stylesheet_is_served_per_request_from_the_staging_root

V7-077: a saved widget style reaches reloads instead of the startup copy.

Kind: callable. Declared return: Not declared / class. Source line: 209.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | library | Imported dependency for library in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | verified | Imported dependency for verified in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| controls | tmp_path | Parameter for tmp path in controls; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| controls | ApplicationControls | Imported dependency for ApplicationControls in controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 12 |
| controls | service | Local binding for service in controls; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| controls | app | Local binding for app in controls; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| controls | actions | Local binding for actions in controls; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 16 |
| controls | preview | Local binding for preview in controls; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| controls | router | Local binding for router in controls; use the enclosing contract and type below. | Return type of ApplicationControls; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_layout_save_requires_exact_origin_and_private_preview_token | tmp_path | Parameter for tmp path in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| test_layout_save_requires_exact_origin_and_private_preview_token | router | Local binding for router in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_layout_save_requires_exact_origin_and_private_preview_token | service | Local binding for service in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_layout_save_requires_exact_origin_and_private_preview_token | app | Local binding for app in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_layout_save_requires_exact_origin_and_private_preview_token | _ | Local binding for  in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 30, 31 |
| test_layout_save_requires_exact_origin_and_private_preview_token | status | Local binding for status in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_layout_save_requires_exact_origin_and_private_preview_token | body | Local binding for body in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_layout_save_requires_exact_origin_and_private_preview_token | token | Local binding for token in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_layout_save_requires_exact_origin_and_private_preview_token | layout | Local binding for layout in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 34 |
| test_layout_save_requires_exact_origin_and_private_preview_token | headers | Loop item for headers in test_layout_save_requires_exact_origin_and_private_preview_token; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 40, 48 |
| test_layout_cannot_move_toolbar_or_execute_code | tmp_path | Parameter for tmp path in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_layout_cannot_move_toolbar_or_execute_code | router | Local binding for router in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_layout_cannot_move_toolbar_or_execute_code | _ | Local binding for  in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_layout_cannot_move_toolbar_or_execute_code | actions | Local binding for actions in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_layout_cannot_move_toolbar_or_execute_code | token | Local binding for token in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_layout_cannot_move_toolbar_or_execute_code | headers | Local binding for headers in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 61 |
| test_layout_cannot_move_toolbar_or_execute_code | payload | Loop item for payload in test_layout_cannot_move_toolbar_or_execute_code; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 66 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | tmp_path | Parameter for tmp path in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | router | Local binding for router in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | service | Local binding for service in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | app | Local binding for app in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | _ | Local binding for  in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | token | Local binding for token in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | headers | Local binding for headers in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 84 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | layout | Local binding for layout in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 89 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | forbidden | Loop item for forbidden in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 103 |
| test_layout_hidden_controls_roundtrip_and_reject_toolbar | payload | Local binding for payload in test_layout_hidden_controls_roundtrip_and_reject_toolbar; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 104 |
| test_owned_stop_restart_and_close_never_accept_a_path | tmp_path | Parameter for tmp path in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_owned_stop_restart_and_close_never_accept_a_path | router | Local binding for router in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_owned_stop_restart_and_close_never_accept_a_path | _ | Local binding for  in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_owned_stop_restart_and_close_never_accept_a_path | actions | Local binding for actions in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_owned_stop_restart_and_close_never_accept_a_path | token | Local binding for token in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_owned_stop_restart_and_close_never_accept_a_path | headers | Local binding for headers in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 116 |
| test_owned_stop_restart_and_close_never_accept_a_path | action | Loop item for action in test_owned_stop_restart_and_close_never_accept_a_path; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 121 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | tmp_path | Parameter for tmp path in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 127 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | router | Local binding for router in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | _ | Local binding for  in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | token | Local binding for token in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | headers | Local binding for headers in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 131 |
| test_duplicate_layout_keys_and_oversize_requests_are_rejected | body | Loop item for body in test_duplicate_layout_keys_and_oversize_requests_are_rejected; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 136 |
| test_paused_preview_restarts_only_owned_snapshot | threading | Imported dependency for threading in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 142 |
| test_paused_preview_restarts_only_owned_snapshot | ApplicationPreview | Imported dependency for ApplicationPreview in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 144 |
| test_paused_preview_restarts_only_owned_snapshot | preview | Local binding for preview in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_paused_preview_restarts_only_owned_snapshot | preview.lifecycle_lock | Attribute for preview.lifecycle lock in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| test_paused_preview_restarts_only_owned_snapshot | preview.stop | Attribute for preview.stop in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_paused_preview_restarts_only_owned_snapshot | preview.paused | Attribute for preview.paused in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 149 |
| test_paused_preview_restarts_only_owned_snapshot | preview.approved | Attribute for preview.approved in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_paused_preview_restarts_only_owned_snapshot | actions | Local binding for actions in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 151 |
| test_paused_preview_restarts_only_owned_snapshot | preview.session | Attribute for preview.session in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| test_paused_preview_restarts_only_owned_snapshot | preview.bridge | Attribute for preview.bridge in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| test_paused_preview_restarts_only_owned_snapshot | new | Local binding for new in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_paused_preview_restarts_only_owned_snapshot | preview._create_session | Attribute for preview. create session in test_paused_preview_restarts_only_owned_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_paused_preview_restarts_only_owned_snapshot.lambda_157 | approved | Callback parameter for approved in test_paused_preview_restarts_only_owned_snapshot.lambda_157; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 157 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | tmp_path | Parameter for tmp path in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | router | Local binding for router in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | _ | Local binding for  in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | actions | Local binding for actions in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | router.check | Attribute for router.check in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | token | Local binding for token in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_revoked_dependencies_still_allow_owned_stop_and_close | headers | Local binding for headers in test_revoked_dependencies_still_allow_owned_stop_and_close; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 177 |
| test_changed_app_still_exposes_an_owned_close_token | tmp_path | Parameter for tmp path in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 187 |
| test_changed_app_still_exposes_an_owned_close_token | monkeypatch | Parameter for monkeypatch in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 187 |
| test_changed_app_still_exposes_an_owned_close_token | router | Local binding for router in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_changed_app_still_exposes_an_owned_close_token | service | Local binding for service in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_changed_app_still_exposes_an_owned_close_token | _ | Local binding for  in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 189, 196 |
| test_changed_app_still_exposes_an_owned_close_token | actions | Local binding for actions in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of controls; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_changed_app_still_exposes_an_owned_close_token.unavailable | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 191 |
| test_changed_app_still_exposes_an_owned_close_token | status | Local binding for status in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_changed_app_still_exposes_an_owned_close_token | body | Local binding for body in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_changed_app_still_exposes_an_owned_close_token | data | Local binding for data in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| test_changed_app_still_exposes_an_owned_close_token | headers | Local binding for headers in test_changed_app_still_exposes_an_owned_close_token; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 200 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | tmp_path | Parameter for tmp path in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 209 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | ApplicationControls | Imported dependency for ApplicationControls in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | staging | Local binding for staging in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 213 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | stylesheet | Local binding for stylesheet in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | preview | Local binding for preview in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | router | Local binding for router in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Return type of ApplicationControls; see its callable contract | Enclosing invocation or class/instance lifetime | 218 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | status | Local binding for status in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | media | Local binding for media in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_application_stylesheet_is_served_per_request_from_the_staging_root | body | Local binding for body in test_application_stylesheet_is_served_per_request_from_the_staging_root; use the enclosing contract and type below. | Return type of handle; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
