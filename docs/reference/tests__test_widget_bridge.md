# Reference for tests/test_widget_bridge.py

LAB-003 framing and bridge policies reject data before native dispatch.

Source fingerprint: 4c54d5224aea77da245bbf5912d51479aebb8a96601c66873473d485839d39a8

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_frames_preserve_json_and_reject_duplicates_or_executable_values

Catch ambiguous messages, coercion and unbounded cross-process data.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_bridge_admits_only_supported_http_routes

Catch accidental rejection of required Gradio startup and event routes.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_bridge_denies_files_uploads_and_unknown_methods

Catch host filesystem/proxy features leaking through the HTTP bridge.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### test_bridge_checks_origin_and_streams_bounded_response

Exercise the real ASGI bridge, observing HTTP rejection and streamed payload.

Kind: callable. Declared return: Not declared / class. Source line: 45.

### test_bridge_checks_origin_and_streams_bounded_response.Session

Deterministic IPC boundary double; the maintained HTTP policy remains real.

Kind: class. Declared return: Not declared / class. Source line: 54.

### test_bridge_checks_origin_and_streams_bounded_response.Session.events

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_bridge_checks_origin_and_streams_bounded_response.exercise

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### test_preview_rejects_unbounded_lifetime

A caller cannot turn the isolated preview into an unbounded background job.

Kind: callable. Declared return: Not declared / class. Source line: 87.

### test_invalid_tool_input_reports_error_without_killing_preview

Validation failure is recoverable and must not cancel the whole native UI.

Kind: callable. Declared return: Not declared / class. Source line: 95.

### test_unapproved_widget_bytes_never_start_a_native_process

Callers must present the reviewed capability, not arbitrary source bytes.

Kind: callable. Declared return: Not declared / class. Source line: 113.

### test_partial_staging_failure_removes_private_runtime

A failed dependency stage must not leak its owned temporary directory.

Kind: callable. Declared return: Not declared / class. Source line: 121.

### test_partial_staging_failure_removes_private_runtime.fail

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 125.

### test_bridge_frame_policy_allows_only_explicit_lab_origin

Embedding must never turn into an unrestricted frame-ancestors wildcard.

Kind: callable. Declared return: Not declared / class. Source line: 135.

### test_bridge_frame_policy_allows_only_explicit_lab_origin.Session

Replace only the external IPC events with a literal response.

Kind: class. Declared return: Not declared / class. Source line: 144.

### test_bridge_frame_policy_allows_only_explicit_lab_origin.Session.events

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 147.

### test_bridge_frame_policy_allows_only_explicit_lab_origin.check

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 151.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | decode_frame | Imported dependency for decode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | encode_frame | Imported dependency for encode frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | validate_http_request | Imported dependency for validate http request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_frames_preserve_json_and_reject_duplicates_or_executable_values | message | Local binding for message in test_frames_preserve_json_and_reject_duplicates_or_executable_values; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 10 |
| test_frames_preserve_json_and_reject_duplicates_or_executable_values | wire | Local binding for wire in test_frames_preserve_json_and_reject_duplicates_or_executable_values; use the enclosing contract and type below. | Return type of encode_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_frames_preserve_json_and_reject_duplicates_or_executable_values | raw | Loop item for raw in test_frames_preserve_json_and_reject_duplicates_or_executable_values; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 13 |
| test_bridge_admits_only_supported_http_routes | method | Parameter for method in test_bridge_admits_only_supported_http_routes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_bridge_admits_only_supported_http_routes | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_bridge_denies_files_uploads_and_unknown_methods | method | Parameter for method in test_bridge_denies_files_uploads_and_unknown_methods; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_bridge_denies_files_uploads_and_unknown_methods | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_bridge_checks_origin_and_streams_bounded_response | asyncio | Imported dependency for asyncio in test_bridge_checks_origin_and_streams_bounded_response; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 47 |
| test_bridge_checks_origin_and_streams_bounded_response | base64 | Imported dependency for base64 in test_bridge_checks_origin_and_streams_bounded_response; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 48 |
| test_bridge_checks_origin_and_streams_bounded_response | httpx | Imported dependency for httpx in test_bridge_checks_origin_and_streams_bounded_response; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 50 |
| test_bridge_checks_origin_and_streams_bounded_response | WidgetBridge | Imported dependency for WidgetBridge in test_bridge_checks_origin_and_streams_bounded_response; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| test_bridge_checks_origin_and_streams_bounded_response.Session.events | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_bridge_checks_origin_and_streams_bounded_response.Session.events | args | Parameter for args in test_bridge_checks_origin_and_streams_bounded_response.Session.events; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_bridge_checks_origin_and_streams_bounded_response.Session.events | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_bridge_checks_origin_and_streams_bounded_response.exercise | client | Managed resource for client in test_bridge_checks_origin_and_streams_bounded_response.exercise; use the enclosing contract and type below. | Return type of AsyncClient; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 67 |
| test_bridge_checks_origin_and_streams_bounded_response.exercise | response | Bounded response text to render or validate; it is not executable code. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_preview_rejects_unbounded_lifetime | seconds | Parameter for seconds in test_preview_rejects_unbounded_lifetime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_preview_rejects_unbounded_lifetime | WidgetSession | Imported dependency for WidgetSession in test_preview_rejects_unbounded_lifetime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 89 |
| test_invalid_tool_input_reports_error_without_killing_preview | WidgetSession | Imported dependency for WidgetSession in test_invalid_tool_input_reports_error_without_killing_preview; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 97 |
| test_invalid_tool_input_reports_error_without_killing_preview | session | Local binding for session in test_invalid_tool_input_reports_error_without_killing_preview; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_invalid_tool_input_reports_error_without_killing_preview | messages | Local binding for messages in test_invalid_tool_input_reports_error_without_killing_preview; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 100 |
| test_invalid_tool_input_reports_error_without_killing_preview | session._write | Attribute for session. write in test_invalid_tool_input_reports_error_without_killing_preview; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_unapproved_widget_bytes_never_start_a_native_process | WidgetSession | Imported dependency for WidgetSession in test_unapproved_widget_bytes_never_start_a_native_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 115 |
| test_partial_staging_failure_removes_private_runtime | monkeypatch | Parameter for monkeypatch in test_partial_staging_failure_removes_private_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| test_partial_staging_failure_removes_private_runtime | widget_session | Imported dependency for widget session in test_partial_staging_failure_removes_private_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 123 |
| test_partial_staging_failure_removes_private_runtime.fail | root | Explicit root directory against which named paths are resolved. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| test_partial_staging_failure_removes_private_runtime | session | Local binding for session in test_partial_staging_failure_removes_private_runtime; use the enclosing contract and type below. | Return type of WidgetSession; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin | asyncio | Imported dependency for asyncio in test_bridge_frame_policy_allows_only_explicit_lab_origin; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 137 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin | base64 | Imported dependency for base64 in test_bridge_frame_policy_allows_only_explicit_lab_origin; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 138 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin | httpx | Imported dependency for httpx in test_bridge_frame_policy_allows_only_explicit_lab_origin; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 140 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin | WidgetBridge | Imported dependency for WidgetBridge in test_bridge_frame_policy_allows_only_explicit_lab_origin; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 142 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.Session.events | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 147 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.Session.events | args | Parameter for args in test_bridge_frame_policy_allows_only_explicit_lab_origin.Session.events; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 147 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.Session.events | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 147 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.check | app | Local binding for app in test_bridge_frame_policy_allows_only_explicit_lab_origin.check; use the enclosing contract and type below. | Return type of WidgetBridge; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.check | client | Managed resource for client in test_bridge_frame_policy_allows_only_explicit_lab_origin.check; use the enclosing contract and type below. | Return type of AsyncClient; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 153 |
| test_bridge_frame_policy_allows_only_explicit_lab_origin.check | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 156 |
