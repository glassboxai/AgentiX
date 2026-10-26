# Reference for tests/unit/test_app.py

Exercise UI controllers and stream capture independently of browser widgets.

Source fingerprint: d3961ec51ec08c130011f5ad8a9a8ba90a3b6ae56790581d6b6c5c061a193261

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_capture_mirrors_output_and_removes_ansi

Verify capture mirrors output and removes ansi.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_capture_tail_and_clear

Verify capture tail and clear.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_capture_delegates_stream_operations

Verify capture delegates stream operations.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_thoughts_display

Verify thoughts display.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_empty_thoughts_display

Verify empty thoughts display.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_empty_query_does_not_start_worker

Verify empty query does not start worker.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_busy_query_does_not_start_another_worker

Verify busy query does not start another worker.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### test_worker_success

Verify worker success.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_worker_error_clears_running_flag

Verify worker error clears running flag.

Kind: callable. Declared return: Not declared / class. Source line: 95.

### test_poll_loads_pending_content_once

Verify poll loads pending content once.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_poll_resets_after_request_finishes

Verify poll resets after request finishes.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### test_poll_renders_final_result

Verify poll renders final result.

Kind: callable. Declared return: Not declared / class. Source line: 135.

### test_poll_running_displays_activity

Verify poll running displays activity.

Kind: callable. Declared return: Not declared / class. Source line: 147.

### test_approval_and_rejection_callbacks

Verify approval and rejection callbacks.

Kind: callable. Declared return: Not declared / class. Source line: 154.

### test_auto_approval_toggle

Verify auto approval toggle.

Kind: callable. Declared return: Not declared / class. Source line: 167.

### test_execution_states_have_independent_histories

Verify execution states have independent histories.

Kind: callable. Declared return: Not declared / class. Source line: 173.

### test_new_execution_state_does_not_inherit_other_state_values

Verify new execution state does not inherit other state values.

Kind: callable. Declared return: Not declared / class. Source line: 179.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | io | Imported dependency for io in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_capture_mirrors_output_and_removes_ansi | system | Parameter for system in test_capture_mirrors_output_and_removes_ansi; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| test_capture_mirrors_output_and_removes_ansi | stream | Local binding for stream in test_capture_mirrors_output_and_removes_ansi; use the enclosing contract and type below. | Return type of StringIO; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_capture_mirrors_output_and_removes_ansi | capture | Local binding for capture in test_capture_mirrors_output_and_removes_ansi; use the enclosing contract and type below. | Return type of capture_type; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_capture_tail_and_clear | system | Parameter for system in test_capture_tail_and_clear; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_capture_tail_and_clear | capture | Local binding for capture in test_capture_tail_and_clear; use the enclosing contract and type below. | Return type of capture_type; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_capture_tail_and_clear | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 22 |
| test_capture_delegates_stream_operations | system | Parameter for system in test_capture_delegates_stream_operations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_capture_delegates_stream_operations | stream | Local binding for stream in test_capture_delegates_stream_operations; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_capture_delegates_stream_operations | stream.isatty.return_value | Attribute for stream.isatty.return value in test_capture_delegates_stream_operations; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 32 |
| test_capture_delegates_stream_operations | capture | Local binding for capture in test_capture_delegates_stream_operations; use the enclosing contract and type below. | Return type of capture_type; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_thoughts_display | system | Parameter for system in test_thoughts_display; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_thoughts_display | is_open | Parameter for is open in test_thoughts_display; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_thoughts_display | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_empty_thoughts_display | system | Parameter for system in test_empty_thoughts_display; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_empty_query_does_not_start_worker | system | Parameter for system in test_empty_query_does_not_start_worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_empty_query_does_not_start_worker | monkeypatch | Parameter for monkeypatch in test_empty_query_does_not_start_worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_empty_query_does_not_start_worker | worker | Local binding for worker in test_empty_query_does_not_start_worker; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_busy_query_does_not_start_another_worker | system | Parameter for system in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| test_busy_query_does_not_start_another_worker | monkeypatch | Parameter for monkeypatch in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| test_busy_query_does_not_start_another_worker | system.app.state.is_running | Attribute for system.app.state.is running in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 63 |
| test_busy_query_does_not_start_another_worker | worker | Local binding for worker in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_busy_query_does_not_start_another_worker | _ | Local binding for  in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | Return type of process_user_query; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_busy_query_does_not_start_another_worker | history | Local binding for history in test_busy_query_does_not_start_another_worker; use the enclosing contract and type below. | Return type of process_user_query; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_worker_success | system | Parameter for system in test_worker_success; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_worker_success | monkeypatch | Parameter for monkeypatch in test_worker_success; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_worker_success | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_worker_success | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_worker_success.lambda_87 | target | Callback parameter for target in test_worker_success.lambda_87; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 87 |
| test_worker_success.lambda_87 | daemon | Callback parameter for daemon in test_worker_success.lambda_87; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 87 |
| test_worker_error_clears_running_flag | system | Parameter for system in test_worker_error_clears_running_flag; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| test_worker_error_clears_running_flag | monkeypatch | Parameter for monkeypatch in test_worker_error_clears_running_flag; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| test_worker_error_clears_running_flag.lambda_101 | target | Callback parameter for target in test_worker_error_clears_running_flag.lambda_101; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 101 |
| test_worker_error_clears_running_flag.lambda_101 | daemon | Callback parameter for daemon in test_worker_error_clears_running_flag.lambda_101; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 101 |
| test_poll_loads_pending_content_once | system | Parameter for system in test_poll_loads_pending_content_once; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_poll_loads_pending_content_once | system.security._pending_request | Attribute for system.security. pending request in test_poll_loads_pending_content_once; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 110 |
| test_poll_loads_pending_content_once | first | Local binding for first in test_poll_loads_pending_content_once; use the enclosing contract and type below. | Return type of poll_system_status; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| test_poll_loads_pending_content_once | second | Local binding for second in test_poll_loads_pending_content_once; use the enclosing contract and type below. | Return type of poll_system_status; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_poll_resets_after_request_finishes | system | Parameter for system in test_poll_resets_after_request_finishes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_poll_resets_after_request_finishes | system.app.state.last_displayed_filepath | Attribute for system.app.state.last displayed filepath in test_poll_resets_after_request_finishes; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 125 |
| test_poll_resets_after_request_finishes | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of poll_system_status; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_poll_renders_final_result | system | Parameter for system in test_poll_renders_final_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_poll_renders_final_result | error | Parameter for error in test_poll_renders_final_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_poll_renders_final_result | response | Bounded response text to render or validate; it is not executable code. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_poll_renders_final_result | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| test_poll_renders_final_result | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_poll_renders_final_result | state.chat_history | Attribute for state.chat history in test_poll_renders_final_result; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 138 |
| test_poll_renders_final_result | state.error_message | Attribute for state.error message in test_poll_renders_final_result; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 141 |
| test_poll_renders_final_result | state.last_response | Attribute for state.last response in test_poll_renders_final_result; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 141 |
| test_poll_renders_final_result | history | Local binding for history in test_poll_renders_final_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_poll_running_displays_activity | system | Parameter for system in test_poll_running_displays_activity; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 147 |
| test_poll_running_displays_activity | system.app.state.is_running | Attribute for system.app.state.is running in test_poll_running_displays_activity; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 149 |
| test_poll_running_displays_activity | system.app.state.chat_history | Attribute for system.app.state.chat history in test_poll_running_displays_activity; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 150 |
| test_approval_and_rejection_callbacks | system | Parameter for system in test_approval_and_rejection_callbacks; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 154 |
| test_approval_and_rejection_callbacks | monkeypatch | Parameter for monkeypatch in test_approval_and_rejection_callbacks; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 154 |
| test_approval_and_rejection_callbacks | resolve | Local binding for resolve in test_approval_and_rejection_callbacks; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 156 |
| test_auto_approval_toggle | system | Parameter for system in test_auto_approval_toggle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_auto_approval_toggle | enabled | Parameter for enabled in test_auto_approval_toggle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_execution_states_have_independent_histories | system | Parameter for system in test_execution_states_have_independent_histories; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 173 |
| test_execution_states_have_independent_histories | first | Local binding for first in test_execution_states_have_independent_histories; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 175 |
| test_execution_states_have_independent_histories | second | Local binding for second in test_execution_states_have_independent_histories; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 175 |
| test_new_execution_state_does_not_inherit_other_state_values | system | Parameter for system in test_new_execution_state_does_not_inherit_other_state_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| test_new_execution_state_does_not_inherit_other_state_values | first | Local binding for first in test_new_execution_state_does_not_inherit_other_state_values; use the enclosing contract and type below. | Return type of state_type; see its callable contract | Enclosing invocation or class/instance lifetime | 181 |
| test_new_execution_state_does_not_inherit_other_state_values | first.is_running | Attribute for first.is running in test_new_execution_state_does_not_inherit_other_state_values; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 183 |
| test_new_execution_state_does_not_inherit_other_state_values | second | Local binding for second in test_new_execution_state_does_not_inherit_other_state_values; use the enclosing contract and type below. | Return type of state_type; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
