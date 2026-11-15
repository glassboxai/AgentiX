# Reference for tests/unit/test_message_dialog.py

Modal message dialog contract: persistent until the user presses Ok.

Source fingerprint: f3ddf2ca74c768e48c82b47c4b77a2095b2aa819032f487196e92a1eec3265ae

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _build_dialog

Construct the dialog with the real Gradio module inside a Blocks context.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_dialog_starts_hidden_and_toggles_with_ok

The window is hidden by default, shows one message and closes with Ok.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal

Successful streams gain skipped dialog outputs; ValueError opens the modal.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.success

Yield one ordinary six-output row.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.invalid

Raise the same validation error the name check raises.

Kind: callable. Declared return: Not declared / class. Source line: 43.

### test_result_wrapper_shows_status_message_in_modal_and_errors_too

Save confirmations and validation errors persist in the modal until Ok.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_result_wrapper_shows_status_message_in_modal_and_errors_too.saved

Return the ordinary six-output save tuple.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### test_result_wrapper_shows_status_message_in_modal_and_errors_too.invalid

Raise a validation error instead of returning a row.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### test_guard_result_passes_success_through_and_routes_errors_to_modal

Ordinary results keep the dialog hidden; ValueError opens the modal.

Kind: callable. Declared return: Not declared / class. Source line: 88.

### test_guard_result_passes_success_through_and_routes_errors_to_modal.saved

Return an ordinary two-output row.

Kind: callable. Declared return: Not declared / class. Source line: 92.

### test_guard_result_passes_success_through_and_routes_errors_to_modal.silent

Return nothing, as discard-style approval callbacks do.

Kind: callable. Declared return: Not declared / class. Source line: 100.

### test_guard_result_passes_success_through_and_routes_errors_to_modal.scalar

Return one plain string, as status-only backends do.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_guard_result_passes_success_through_and_routes_errors_to_modal.invalid

Raise a validation error instead of returning a row.

Kind: callable. Declared return: Not declared / class. Source line: 116.

### test_guard_history_appends_the_dialog_pair_on_success_and_on_error

Both branches must reach the declared output count; only errors empty the history.

Kind: callable. Declared return: Not declared / class. Source line: 132.

### test_guard_history_appends_the_dialog_pair_on_success_and_on_error.poll

Return the seven outputs the Tools poll backend produces.

Kind: callable. Declared return: Not declared / class. Source line: 138.

### test_guard_history_appends_the_dialog_pair_on_success_and_on_error.rejected

Raise the ownership diagnostic the guard exists for.

Kind: callable. Declared return: Not declared / class. Source line: 156.

### test_wrappers_preserve_the_handler_signature_for_request_injection

Wrapped handlers keep their signature so Gradio still injects the Request slot.

Kind: callable. Declared return: Not declared / class. Source line: 168.

### test_wrappers_preserve_the_handler_signature_for_request_injection.handler

Plain handler shaped like a session-owned backend method.

Kind: callable. Declared return: Not declared / class. Source line: 176.

### test_wrappers_preserve_the_handler_signature_for_request_injection.streaming

Streaming handler shaped like a generating backend method.

Kind: callable. Declared return: Not declared / class. Source line: 180.

### test_guard_result_rejects_streaming_handlers

Generators must use wrap_stream; guard_result fails loudly instead of corrupting outputs.

Kind: callable. Declared return: Not declared / class. Source line: 194.

### test_guard_result_rejects_streaming_handlers.streaming

Stand-in for a streaming backend handler.

Kind: callable. Declared return: Not declared / class. Source line: 198.

### test_wrappers_preserve_the_wrapped_signature_for_request_injection

The shell's bind rewrites request annotations; wrappers must expose them.

Kind: callable. Declared return: Not declared / class. Source line: 211.

### test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler

Stand-in with the same parameter names as a bound backend method.

Kind: callable. Declared return: tuple. Source line: 218.

### test_stream_final_wrapper_opens_modal_only_with_the_last_status

Intermediate rows leave the dialog untouched; the final status opens it.

Kind: callable. Declared return: Not declared / class. Source line: 231.

### test_stream_final_wrapper_opens_modal_only_with_the_last_status.progress

Yield two ordinary rows, the last carrying the visible status.

Kind: callable. Declared return: Not declared / class. Source line: 235.

### test_stream_final_wrapper_opens_modal_only_with_the_last_status.empty_status

Yield rows whose final status is empty; no empty modal may open.

Kind: callable. Declared return: Not declared / class. Source line: 249.

### test_stream_final_wrapper_opens_modal_only_with_the_last_status.invalid

Raise after progress; the pending row flushes before the modal error.

Kind: callable. Declared return: Not declared / class. Source line: 257.

### test_result_wrapper_can_mirror_a_custom_status_position

Composite results open the modal with the message at the chosen index.

Kind: callable. Declared return: Not declared / class. Source line: 271.

### test_result_wrapper_can_mirror_a_custom_status_position.computed

Return typed results followed by visibility, status and ownership.

Kind: callable. Declared return: Not declared / class. Source line: 275.

### test_sidebar_starts_closed

The shared model sidebar is collapsed at startup for a cleaner first view.

Kind: callable. Declared return: Not declared / class. Source line: 285.

### test_sidebar_starts_closed.Component

Record constructor kwargs and absorb event bindings.

Kind: class. Declared return: Not declared / class. Source line: 289.

### test_sidebar_starts_closed.Component.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 292.

### test_sidebar_starts_closed.Component.__enter__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 296.

### test_sidebar_starts_closed.Component.__exit__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 299.

### test_sidebar_starts_closed.Component.__getattr__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 302.

### test_sidebar_starts_closed.Component.__getattr__.event

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 303.

### test_sidebar_starts_closed.DialogStub

Absorb dialog wrapping without building real modal components.

Kind: class. Declared return: Not declared / class. Source line: 326.

### test_sidebar_starts_closed.DialogStub.guard_result

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 329.

### test_sidebar_starts_closed.DialogStub.outputs

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 332.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| _build_dialog | gr | Imported dependency for gr in _build_dialog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 8 |
| _build_dialog | MessageDialog | Imported dependency for MessageDialog in _build_dialog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| _build_dialog | dialog | Local binding for dialog in _build_dialog; use the enclosing contract and type below. | Return type of MessageDialog; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_dialog_starts_hidden_and_toggles_with_ok | dialog | Local binding for dialog in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_dialog_starts_hidden_and_toggles_with_ok | gr | Local binding for gr in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_dialog_starts_hidden_and_toggles_with_ok | update | Local binding for update in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of show; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_dialog_starts_hidden_and_toggles_with_ok | text | Local binding for text in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of show; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_dialog_starts_hidden_and_toggles_with_ok | skipped | Local binding for skipped in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of skip; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_dialog_starts_hidden_and_toggles_with_ok | skip_type | Local binding for skip type in test_dialog_starts_hidden_and_toggles_with_ok; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_dialog_starts_hidden_and_toggles_with_ok.comprehension_27 | item | Comprehension item for item in test_dialog_starts_hidden_and_toggles_with_ok.comprehension_27; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 27 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal | dialog | Local binding for dialog in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal | gr | Local binding for gr in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal | rows | Local binding for rows in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 38, 48 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal | skip_type | Local binding for skip type in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.comprehension_41 | item | Comprehension item for item in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.comprehension_41; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 41 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal | row | Local binding for row in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.comprehension_52 | item | Comprehension item for item in test_stream_wrapper_passes_rows_through_and_routes_validation_errors_to_modal.comprehension_52; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too | dialog | Local binding for dialog in test_result_wrapper_shows_status_message_in_modal_and_errors_too; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too | gr | Local binding for gr in test_result_wrapper_shows_status_message_in_modal_and_errors_too; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too.saved | args | Parameter for args in test_result_wrapper_shows_status_message_in_modal_and_errors_too.saved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too | row | Local binding for row in test_result_wrapper_shows_status_message_in_modal_and_errors_too; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 65, 81 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too.invalid | args | Parameter for args in test_result_wrapper_shows_status_message_in_modal_and_errors_too.invalid; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_result_wrapper_shows_status_message_in_modal_and_errors_too.comprehension_83 | item | Comprehension item for item in test_result_wrapper_shows_status_message_in_modal_and_errors_too.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal | dialog | Local binding for dialog in test_guard_result_passes_success_through_and_routes_errors_to_modal; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal | gr | Local binding for gr in test_guard_result_passes_success_through_and_routes_errors_to_modal; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.saved | args | Parameter for args in test_guard_result_passes_success_through_and_routes_errors_to_modal.saved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 92 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal | row | Local binding for row in test_guard_result_passes_success_through_and_routes_errors_to_modal; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 96, 104, 112, 120, 126 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_98 | item | Comprehension item for item in test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_98; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.silent | args | Parameter for args in test_guard_result_passes_success_through_and_routes_errors_to_modal.silent; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_106 | item | Comprehension item for item in test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_106; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 106 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.scalar | args | Parameter for args in test_guard_result_passes_success_through_and_routes_errors_to_modal.scalar; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_114 | item | Comprehension item for item in test_guard_result_passes_success_through_and_routes_errors_to_modal.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 114 |
| test_guard_result_passes_success_through_and_routes_errors_to_modal.invalid | args | Parameter for args in test_guard_result_passes_success_through_and_routes_errors_to_modal.invalid; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 116 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error | dialog | Local binding for dialog in test_guard_history_appends_the_dialog_pair_on_success_and_on_error; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error | gr | Local binding for gr in test_guard_history_appends_the_dialog_pair_on_success_and_on_error; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error | skip_type | Local binding for skip type in test_guard_history_appends_the_dialog_pair_on_success_and_on_error; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 136 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.poll | token | Parameter for token in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.poll; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.poll | request | Parameter for request in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.poll; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error | row | Local binding for row in test_guard_history_appends_the_dialog_pair_on_success_and_on_error; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 150, 160 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.comprehension_154 | item | Comprehension item for item in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.comprehension_154; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 154 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.rejected | token | Parameter for token in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 156 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.rejected | request | Parameter for request in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 156 |
| test_guard_history_appends_the_dialog_pair_on_success_and_on_error.comprehension_163 | item | Comprehension item for item in test_guard_history_appends_the_dialog_pair_on_success_and_on_error.comprehension_163; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 163 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | inspect | Imported dependency for inspect in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 170 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | helpers | Imported dependency for helpers in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 172 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | dialog | Local binding for dialog in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | gr | Local binding for gr in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.handler | message | Parameter for message in test_wrappers_preserve_the_handler_signature_for_request_injection.handler; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.handler | token | Parameter for token in test_wrappers_preserve_the_handler_signature_for_request_injection.handler; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.handler | request | Parameter for request in test_wrappers_preserve_the_handler_signature_for_request_injection.handler; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.streaming | message | Parameter for message in test_wrappers_preserve_the_handler_signature_for_request_injection.streaming; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 180 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.streaming | token | Parameter for token in test_wrappers_preserve_the_handler_signature_for_request_injection.streaming; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 180 |
| test_wrappers_preserve_the_handler_signature_for_request_injection.streaming | request | Parameter for request in test_wrappers_preserve_the_handler_signature_for_request_injection.streaming; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 180 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | wrapped | Loop item for wrapped in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 185 |
| test_wrappers_preserve_the_handler_signature_for_request_injection | inputs | Local binding for inputs in test_wrappers_preserve_the_handler_signature_for_request_injection; use the enclosing contract and type below. | Return type of special_args; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_guard_result_rejects_streaming_handlers | dialog | Local binding for dialog in test_guard_result_rejects_streaming_handlers; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_guard_result_rejects_streaming_handlers | gr | Local binding for gr in test_guard_result_rejects_streaming_handlers; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_guard_result_rejects_streaming_handlers | wrapped | Local binding for wrapped in test_guard_result_rejects_streaming_handlers; use the enclosing contract and type below. | Return type of guard_result; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_guard_result_rejects_streaming_handlers | error | Caught exception for error in test_guard_result_rejects_streaming_handlers; use the enclosing contract and type below. | TypeError | Current exception handler; Python clears this binding afterward | 205 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | inspect | Imported dependency for inspect in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 213 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | Any | Imported dependency for Any in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 214 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | dialog | Local binding for dialog in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | gr | Local binding for gr in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 218 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 218 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler | token | Parameter for token in test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 218 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler | request | Parameter for request in test_wrappers_preserve_the_wrapped_signature_for_request_injection.handler; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 218 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | wrapper | Loop item for wrapper in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 222 |
| test_wrappers_preserve_the_wrapped_signature_for_request_injection | parameters | Local binding for parameters in test_wrappers_preserve_the_wrapped_signature_for_request_injection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 226 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status | dialog | Local binding for dialog in test_stream_final_wrapper_opens_modal_only_with_the_last_status; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status | gr | Local binding for gr in test_stream_final_wrapper_opens_modal_only_with_the_last_status; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status | rows | Local binding for rows in test_stream_final_wrapper_opens_modal_only_with_the_last_status; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 240, 254, 262 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status | skip_type | Local binding for skip type in test_stream_final_wrapper_opens_modal_only_with_the_last_status; use the enclosing contract and type below. | Return type of type; see its callable contract | Enclosing invocation or class/instance lifetime | 241 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_244 | item | Comprehension item for item in test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_244; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 244 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_255 | item | Comprehension item for item in test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_255; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 255 |
| test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_265 | item | Comprehension item for item in test_stream_final_wrapper_opens_modal_only_with_the_last_status.comprehension_265; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 265 |
| test_result_wrapper_can_mirror_a_custom_status_position | dialog | Local binding for dialog in test_result_wrapper_can_mirror_a_custom_status_position; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_result_wrapper_can_mirror_a_custom_status_position | gr | Local binding for gr in test_result_wrapper_can_mirror_a_custom_status_position; use the enclosing contract and type below. | Return type of _build_dialog; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_result_wrapper_can_mirror_a_custom_status_position.computed | args | Parameter for args in test_result_wrapper_can_mirror_a_custom_status_position.computed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 275 |
| test_result_wrapper_can_mirror_a_custom_status_position | row | Local binding for row in test_result_wrapper_can_mirror_a_custom_status_position; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 279 |
| test_sidebar_starts_closed | created | Local binding for created in test_sidebar_starts_closed; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 287 |
| test_sidebar_starts_closed.Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 292 |
| test_sidebar_starts_closed.Component.__init__ | args | Parameter for args in test_sidebar_starts_closed.Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 292 |
| test_sidebar_starts_closed.Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 292 |
| test_sidebar_starts_closed.Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 293 |
| test_sidebar_starts_closed.Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 296 |
| test_sidebar_starts_closed.Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 299 |
| test_sidebar_starts_closed.Component.__exit__ | args | Parameter for args in test_sidebar_starts_closed.Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 299 |
| test_sidebar_starts_closed.Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 302 |
| test_sidebar_starts_closed.Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 302 |
| test_sidebar_starts_closed.Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 303 |
| test_sidebar_starts_closed | gr | Local binding for gr in test_sidebar_starts_closed; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
| test_sidebar_starts_closed.comprehension_309 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 311 |
| test_sidebar_starts_closed.DialogStub.guard_result | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 329 |
| test_sidebar_starts_closed.DialogStub.guard_result | fn | Parameter for fn in test_sidebar_starts_closed.DialogStub.guard_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 329 |
| test_sidebar_starts_closed.DialogStub.guard_result | size | Parameter for size in test_sidebar_starts_closed.DialogStub.guard_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 329 |
| test_sidebar_starts_closed.DialogStub.outputs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 332 |
| test_sidebar_starts_closed | build_sidebar | Imported dependency for build sidebar in test_sidebar_starts_closed; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 335 |
| test_sidebar_starts_closed.lambda_341 | fn | Callback parameter for fn in test_sidebar_starts_closed.lambda_341; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 341 |
| test_sidebar_starts_closed | sidebar | Local binding for sidebar in test_sidebar_starts_closed; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 346 |
| test_sidebar_starts_closed.comprehension_346 | item | Comprehension item for item in test_sidebar_starts_closed.comprehension_346; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 346 |
