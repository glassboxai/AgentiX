# Reference for src/agentix/ui/sidebar.py

Shared model sidebar, composed once outside the tab container.

Source fingerprint: c85c3af4e54ced19534f318c30efe3d2a014788d4da1c4eaf1a96b7b9de54457

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build_sidebar

Render persistent session model settings and bind secure profile operations.

Kind: callable. Declared return: None. Source line: 14.

### build_sidebar.provider_defaults

Separate installed local choices from explicit external model names.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 100.

### build_sidebar.profile_action

Translate owned profile results into a dropdown update without key data.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 121.

### build_sidebar.refresh_local

Refresh installed names without automatically changing the active model.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 159.

### build_sidebar.inspect_local_generation

Display an inspected digest without persisting trust or activating a model.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 219.

### build_sidebar.apply_selected

Activate only the model field appropriate to the selected provider.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 252.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SIDEBAR_WIDTH_PIXELS | Module binding for SIDEBAR WIDTH PIXELS in module; use the enclosing contract and type below. | int | Module/process lifetime | 5 |
| module | PROFILE_NAME_MAX_LENGTH | Module binding for PROFILE NAME MAX LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 6 |
| module | PROFILE_OUTPUT_COUNT | Module binding for PROFILE OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 7 |
| module | REFRESH_OUTPUT_COUNT | Module binding for REFRESH OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 8 |
| module | GENERATION_OUTPUT_COUNT | Module binding for GENERATION OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | RESET_OUTPUT_COUNT | Module binding for RESET OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | APPLY_OUTPUT_COUNT | Module binding for APPLY OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| build_sidebar | gr | Parameter for gr in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 15 |
| build_sidebar | demo | Parameter for demo in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| build_sidebar | callbacks | Parameter for callbacks in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 17 |
| build_sidebar | bind | Parameter for bind in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 18 |
| build_sidebar | session_state | Parameter for session state in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 19 |
| build_sidebar | progress | Parameter for progress in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 20 |
| build_sidebar | dialog | Parameter for dialog in build_sidebar; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 21, 30 |
| build_sidebar | operation | Local binding for operation in build_sidebar; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| build_sidebar | MessageDialog | Imported dependency for MessageDialog in build_sidebar; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| build_sidebar | provider | Local binding for provider in build_sidebar; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| build_sidebar | profile_choice | Local binding for profile choice in build_sidebar; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| build_sidebar | profile_name | Local binding for profile name in build_sidebar; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| build_sidebar | model_name | Local binding for model name in build_sidebar; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| build_sidebar | external_model | Local binding for external model in build_sidebar; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| build_sidebar | refresh_models | Local binding for refresh models in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| build_sidebar | inspect_generation | Local binding for inspect generation in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| build_sidebar | generation_digest | Local binding for generation digest in build_sidebar; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| build_sidebar | reset_generation | Local binding for reset generation in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| build_sidebar | endpoint | Local binding for endpoint in build_sidebar; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| build_sidebar | api_key | Local binding for api key in build_sidebar; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| build_sidebar | remote_consent | Local binding for remote consent in build_sidebar; use the enclosing contract and type below. | Return type of Checkbox; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| build_sidebar | save_profile | Local binding for save profile in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| build_sidebar | delete_profile | Local binding for delete profile in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| build_sidebar | refresh_profiles | Local binding for refresh profiles in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| build_sidebar | apply_model | Local binding for apply model in build_sidebar; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| build_sidebar | model_status | Local binding for model status in build_sidebar; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| build_sidebar.provider_defaults | choice | Parameter for choice in build_sidebar.provider_defaults; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 100 |
| build_sidebar.provider_defaults | local | Local binding for local in build_sidebar.provider_defaults; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 102 |
| build_sidebar.profile_action | action | Parameter for action in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 122 |
| build_sidebar.profile_action | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 123 |
| build_sidebar.profile_action | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 124 |
| build_sidebar.profile_action | selected_provider | Parameter for selected provider in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 125 |
| build_sidebar.profile_action | selected_model | Parameter for selected model in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 126 |
| build_sidebar.profile_action | selected_external_model | Parameter for selected external model in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 127 |
| build_sidebar.profile_action | selected_endpoint | Parameter for selected endpoint in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 128 |
| build_sidebar.profile_action | key | Parameter for key in build_sidebar.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 129 |
| build_sidebar.profile_action | token | Parameter for token in build_sidebar.profile_action; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 130 |
| build_sidebar.profile_action | request | Parameter for request in build_sidebar.profile_action; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 131 |
| build_sidebar.profile_action | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of model_menu; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| build_sidebar.profile_action | local | Local binding for local in build_sidebar.profile_action; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 145 |
| build_sidebar.refresh_local | selected_endpoint | Parameter for selected endpoint in build_sidebar.refresh_local; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 159 |
| build_sidebar.refresh_local | token | Parameter for token in build_sidebar.refresh_local; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 159 |
| build_sidebar.refresh_local | request | Parameter for request in build_sidebar.refresh_local; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 159 |
| build_sidebar.refresh_local | names | Local binding for names in build_sidebar.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| build_sidebar.refresh_local | status | Local binding for status in build_sidebar.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| build_sidebar.refresh_local | owned_token | Local binding for owned token in build_sidebar.refresh_local; use the enclosing contract and type below. | Return type of refresh_models; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| build_sidebar | profile_inputs | Local binding for profile inputs in build_sidebar; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 164 |
| build_sidebar | profile_outputs | Local binding for profile outputs in build_sidebar; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 174 |
| build_sidebar | button | Loop item for button in build_sidebar; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 186 |
| build_sidebar | action | Loop item for action in build_sidebar; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 186 |
| build_sidebar.inspect_local_generation | selected_model | Parameter for selected model in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 220 |
| build_sidebar.inspect_local_generation | selected_endpoint | Parameter for selected endpoint in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 220 |
| build_sidebar.inspect_local_generation | token | Parameter for token in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 220 |
| build_sidebar.inspect_local_generation | request | Parameter for request in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 220 |
| build_sidebar.inspect_local_generation | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of inspect_generation_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 223 |
| build_sidebar.inspect_local_generation | status | Local binding for status in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | Return type of inspect_generation_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 223 |
| build_sidebar.inspect_local_generation | owned_token | Local binding for owned token in build_sidebar.inspect_local_generation; use the enclosing contract and type below. | Return type of inspect_generation_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 223 |
| build_sidebar.apply_selected | selected_provider | Parameter for selected provider in build_sidebar.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 253 |
| build_sidebar.apply_selected | local_model | Parameter for local model in build_sidebar.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 254 |
| build_sidebar.apply_selected | remote_model | Parameter for remote model in build_sidebar.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 255 |
| build_sidebar.apply_selected | selected_endpoint | Parameter for selected endpoint in build_sidebar.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 256 |
| build_sidebar.apply_selected | key | Parameter for key in build_sidebar.apply_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 257 |
| build_sidebar.apply_selected | consent | Parameter for consent in build_sidebar.apply_selected; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 258 |
| build_sidebar.apply_selected | token | Parameter for token in build_sidebar.apply_selected; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 259 |
| build_sidebar.apply_selected | request | Parameter for request in build_sidebar.apply_selected; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 260 |
