# Reference for src/agentix/ui/view.py

Gradio view with server-owned sessions and browser-snapshot approval IDs.

Source fingerprint: 0da401fb8456401927d32083299a3ec5eadc60fd62acecc1d552505654b65343

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### View

Constructed Blocks object and launch-time theme, without a running server.

Kind: class. Declared return: Not declared / class. Source line: 13.

### build_view

Build widgets/bindings on demand; importing this module never loads Gradio.

Kind: callable. Declared return: View. Source line: 20.

### build_view.bind

Tell Gradio to inject Request instead of treating it as a user input.

Kind: callable. Declared return: Any. Source line: 27.

### build_view.bind.callback

Dispatch only after the session callback checks token ownership.

Kind: callable. Declared return: Any. Source line: 31.

### build_view.provider_defaults

Separate installed local choices from explicit external model names.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 174.

### build_view.profile_action

Translate owned profile results into a dropdown update without key data.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 195.

### build_view.refresh_local

Refresh installed names without automatically changing the active model.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 233.

### build_view.apply_selected

Activate only the model field appropriate to the selected provider.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 299.

### launch

Start the existing queued loopback UI and open the browser.

Kind: callable. Declared return: None. Source line: 384.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | header | Imported dependency for header in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | SessionCallbacks | Imported dependency for SessionCallbacks in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| View | demo | Typed binding for demo in View; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| View | theme | Typed binding for theme in View; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 17 |
| build_view | sessions | Parameter for sessions in build_view; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 20 |
| build_view | gradio_module | Parameter for gradio module in build_view; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 20, 23 |
| build_view | gr | Local binding for gr in build_view; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| build_view | callbacks | Local binding for callbacks in build_view; use the enclosing contract and type below. | Return type of SessionCallbacks; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| build_view.bind | method | Parameter for method in build_view.bind; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 27 |
| build_view.bind | discard_result | Parameter for discard result in build_view.bind; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 27 |
| build_view.bind.callback | args | Parameter for args in build_view.bind.callback; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 31 |
| build_view.bind.callback | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 31 |
| build_view.bind.callback | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of method; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| build_view.bind | callback.__annotations__ | Attribute for callback.  annotations in build_view.bind; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| build_view.bind | signature | Local binding for signature in build_view.bind; use the enclosing contract and type below. | Return type of signature; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| build_view.bind | callback.__signature__ | Attribute for callback.  signature in build_view.bind; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| build_view.bind.comprehension_39 | parameter | Comprehension item for parameter in build_view.bind.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 43 |
| build_view | theme | Local binding for theme in build_view; use the enclosing contract and type below. | Return type of Base; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| build_view | demo | Managed resource for demo in build_view; use the enclosing contract and type below. | Return type of Blocks; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 55 |
| build_view | session_state | Local binding for session state in build_view; use the enclosing contract and type below. | Return type of State; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| build_view | request_state | Local binding for request state in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| build_view | provider | Local binding for provider in build_view; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| build_view | profile_choice | Local binding for profile choice in build_view; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| build_view | profile_name | Local binding for profile name in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| build_view | model_name | Local binding for model name in build_view; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| build_view | external_model | Local binding for external model in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| build_view | refresh_models | Local binding for refresh models in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| build_view | endpoint | Local binding for endpoint in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| build_view | api_key | Local binding for api key in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| build_view | remote_consent | Local binding for remote consent in build_view; use the enclosing contract and type below. | Return type of Checkbox; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| build_view | save_profile | Local binding for save profile in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| build_view | delete_profile | Local binding for delete profile in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| build_view | refresh_profiles | Local binding for refresh profiles in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| build_view | apply_model | Local binding for apply model in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| build_view | model_status | Local binding for model status in build_view; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| build_view | chatbot | Local binding for chatbot in build_view; use the enclosing contract and type below. | Return type of Chatbot; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| build_view | msg_input | Local binding for msg input in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| build_view | submit_btn | Local binding for submit btn in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| build_view | catalog_display | Local binding for catalog display in build_view; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| build_view | validation_display | Local binding for validation display in build_view; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| build_view | auto_approve_check | Local binding for auto approve check in build_view; use the enclosing contract and type below. | Return type of Checkbox; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| build_view | approval_group | Managed resource for approval group in build_view; use the enclosing contract and type below. | Return type of Group; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 159 |
| build_view | pending_info | Local binding for pending info in build_view; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| build_view | preview_box | Local binding for preview box in build_view; use the enclosing contract and type below. | Return type of TextArea; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| build_view | approve_btn | Local binding for approve btn in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| build_view | reject_btn | Local binding for reject btn in build_view; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| build_view.provider_defaults | choice | Parameter for choice in build_view.provider_defaults; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 174 |
| build_view.provider_defaults | local | Local binding for local in build_view.provider_defaults; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| build_view.profile_action | action | Parameter for action in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 196 |
| build_view.profile_action | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 197 |
| build_view.profile_action | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 198 |
| build_view.profile_action | selected_provider | Parameter for selected provider in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 199 |
| build_view.profile_action | selected_model | Parameter for selected model in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 200 |
| build_view.profile_action | selected_external_model | Parameter for selected external model in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 201 |
| build_view.profile_action | selected_endpoint | Parameter for selected endpoint in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 202 |
| build_view.profile_action | key | Parameter for key in build_view.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 203 |
| build_view.profile_action | token | Parameter for token in build_view.profile_action; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 204 |
| build_view.profile_action | request | Parameter for request in build_view.profile_action; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 205 |
| build_view.profile_action | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of model_menu; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| build_view.profile_action | local | Local binding for local in build_view.profile_action; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 219 |
| build_view.refresh_local | selected_endpoint | Parameter for selected endpoint in build_view.refresh_local; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 234 |
| build_view.refresh_local | token | Parameter for token in build_view.refresh_local; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 234 |
| build_view.refresh_local | request | Parameter for request in build_view.refresh_local; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 234 |
| build_view.refresh_local | names | Local binding for names in build_view.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| build_view.refresh_local | status | Local binding for status in build_view.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| build_view.refresh_local | owned_token | Local binding for owned token in build_view.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| build_view | profile_inputs | Local binding for profile inputs in build_view; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 240 |
| build_view | profile_outputs | Local binding for profile outputs in build_view; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 250 |
| build_view | button | Loop item for button in build_view; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 262 |
| build_view | action | Loop item for action in build_view; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 262 |
| build_view.apply_selected | selected_provider | Parameter for selected provider in build_view.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 300 |
| build_view.apply_selected | local_model | Parameter for local model in build_view.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 301 |
| build_view.apply_selected | remote_model | Parameter for remote model in build_view.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 302 |
| build_view.apply_selected | selected_endpoint | Parameter for selected endpoint in build_view.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 303 |
| build_view.apply_selected | key | Parameter for key in build_view.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 304 |
| build_view.apply_selected | consent | Parameter for consent in build_view.apply_selected; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 305 |
| build_view.apply_selected | token | Parameter for token in build_view.apply_selected; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 306 |
| build_view.apply_selected | request | Parameter for request in build_view.apply_selected; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 307 |
| build_view | status_timer | Local binding for status timer in build_view; use the enclosing contract and type below. | Return type of Timer; see its callable contract | Enclosing invocation or class/instance lifetime | 359 |
| launch | view | Parameter for view in launch; use the enclosing contract and type below. | View | Enclosing invocation or class/instance lifetime | 384 |
| launch | server_port | Parameter for server port in launch; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 384 |
| launch | open_browser | Parameter for open browser in launch; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 384 |
