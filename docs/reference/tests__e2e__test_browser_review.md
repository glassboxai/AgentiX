# Reference for tests/e2e/test_browser_review.py

E2E-001: real browser review, edited host verdicts and session separation.

No Ollama or existing generated tools participate. The server's execution double
only runs independently authored trusted fixtures, without isolation claims.

Source fingerprint: 0d47991c6be9f7602d20723099f4d030653210db5dffe9a0298fac66b14417c4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### server

Own one disposable server; fail visibly on startup errors and always stop it.

Kind: callable. Declared return: Not declared / class. Source line: 26.

### server.stop

Stop only the currently owned disposable process tree.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### server.start

Start the same fixture deployment with retained temporary storage.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### server.restart

Replace the owned server process, never the user's live instance.

Kind: callable. Declared return: Not declared / class. Source line: 81.

### browser

Use installed Edge by default, or an explicitly configured browser channel.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### submit

Submit through the public browser controls only.

Kind: callable. Declared return: Not declared / class. Source line: 110.

### test_edited_acceptance_is_compared_by_host_and_private

Verify edited acceptance is compared by host and private.

Kind: callable. Declared return: Not declared / class. Source line: 120.

### test_rejected_acceptance_never_verifies

Verify rejected acceptance never verifies.

Kind: callable. Declared return: Not declared / class. Source line: 163.

### test_file_review_uses_edited_content

Verify file review uses edited content.

Kind: callable. Declared return: Not declared / class. Source line: 183.

### test_brand_readable_result_and_bounded_disclosures

Verify actual layout, accessible send control and timer-stable disclosures.

Kind: callable. Declared return: Not declared / class. Source line: 211.

### test_brand_readable_result_and_bounded_disclosures.luminance

Provide luminance for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 269.

### test_model_sidebar_is_hideable_and_key_input_clears

Use the native sidebar toggle and validate session-owned model settings.

Kind: callable. Declared return: Not declared / class. Source line: 302.

### test_saved_profile_lifecycle_and_session_consent

Create/update/reload/delete a synthetic profile through actual browser UI.

Kind: callable. Declared return: Not declared / class. Source line: 341.

### test_saved_profile_lifecycle_and_session_consent.choose

Select a visible native Gradio dropdown option by its accessible role.

Kind: callable. Declared return: Not declared / class. Source line: 348.

### test_local_secret_controls_and_sidebar_button_colors

Match the reference palette and clear external-only inputs on provider changes.

Kind: callable. Declared return: Not declared / class. Source line: 418.

### test_local_profile_save_refresh_reload_and_delete

Reproduce the user's local Save then Refresh flow with persistent metadata.

Kind: callable. Declared return: Not declared / class. Source line: 461.

### test_external_save_failure_survives_refresh_with_safe_reason

A simulated vault denial is visible after the user's Save then Refresh sequence.

Kind: callable. Declared return: Not declared / class. Source line: 502.

### test_reviewed_tool_reuse_has_fresh_result_without_review

Exercise first review and later new inputs through actual Gradio controls.

Kind: callable. Declared return: Not declared / class. Source line: 532.

### test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift

Use actual GUI approval and native protected storage across runtime loss.

Kind: callable. Declared return: Not declared / class. Source line: 567.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | URLError | Imported dependency for URLError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 20 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 21 |
| module | EDITOR | Module binding for EDITOR in module; use the enclosing contract and type below. | str | Module/process lifetime | 22 |
| server | tmp_path_factory | Parameter for tmp path factory in server; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| server | folder | Local binding for folder in server; use the enclosing contract and type below. | Return type of mktemp; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| server | listener | Managed resource for listener in server; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 29 |
| server | port | Local binding for port in server; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| server | url | Local binding for url in server; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| server | log | Managed resource for log in server; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 33 |
| server | process | Local binding for process in server; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 34 |
| server.stop | process | Local binding for process in server.stop; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 52 |
| server.start | process | Local binding for process in server.start; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| server.start | deadline | Local binding for deadline in server.start; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| server.start | opener | Local binding for opener in server.start; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| server.start | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 74 |
| server.restart | old_pid | Local binding for old pid in server.restart; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 83 |
| server.restart | new_pid | Local binding for new pid in server.restart; use the enclosing contract and type below. | Return type of start; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| browser | sync_playwright | Imported dependency for sync playwright in browser; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 99 |
| browser | driver | Managed resource for driver in browser; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 101 |
| browser | channel | Local binding for channel in browser; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| browser | instance | Local binding for instance in browser; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| submit | page | Parameter for page in submit; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 110 |
| submit | text | Parameter for text in submit; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 110 |
| submit | sidebar | Local binding for sidebar in submit; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| test_edited_acceptance_is_compared_by_host_and_private | browser | Parameter for browser in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 120 |
| test_edited_acceptance_is_compared_by_host_and_private | server | Parameter for server in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 120 |
| test_edited_acceptance_is_compared_by_host_and_private | expect | Imported dependency for expect in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 122 |
| test_edited_acceptance_is_compared_by_host_and_private | alice | Local binding for alice in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 124 |
| test_edited_acceptance_is_compared_by_host_and_private | bob | Local binding for bob in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 124 |
| test_edited_acceptance_is_compared_by_host_and_private | page | Local binding for page in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 126 |
| test_edited_acceptance_is_compared_by_host_and_private | other | Local binding for other in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 126 |
| test_edited_acceptance_is_compared_by_host_and_private | editor | Local binding for editor in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_edited_acceptance_is_compared_by_host_and_private | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_edited_acceptance_is_compared_by_host_and_private | output | Expression binding for output in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_edited_acceptance_is_compared_by_host_and_private | destination | Local binding for destination in test_edited_acceptance_is_compared_by_host_and_private; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| test_rejected_acceptance_never_verifies | browser | Parameter for browser in test_rejected_acceptance_never_verifies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 163 |
| test_rejected_acceptance_never_verifies | server | Parameter for server in test_rejected_acceptance_never_verifies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 163 |
| test_rejected_acceptance_never_verifies | expect | Imported dependency for expect in test_rejected_acceptance_never_verifies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 165 |
| test_rejected_acceptance_never_verifies | context | Local binding for context in test_rejected_acceptance_never_verifies; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| test_rejected_acceptance_never_verifies | page | Local binding for page in test_rejected_acceptance_never_verifies; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_file_review_uses_edited_content | browser | Parameter for browser in test_file_review_uses_edited_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_file_review_uses_edited_content | server | Parameter for server in test_file_review_uses_edited_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_file_review_uses_edited_content | expect | Imported dependency for expect in test_file_review_uses_edited_content; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 185 |
| test_file_review_uses_edited_content | context | Local binding for context in test_file_review_uses_edited_content; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_file_review_uses_edited_content | page | Local binding for page in test_file_review_uses_edited_content; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_file_review_uses_edited_content | editor | Local binding for editor in test_file_review_uses_edited_content; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_file_review_uses_edited_content | saved | Local binding for saved in test_file_review_uses_edited_content; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| test_file_review_uses_edited_content.comprehension_205 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 205 |
| test_brand_readable_result_and_bounded_disclosures | browser | Parameter for browser in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| test_brand_readable_result_and_bounded_disclosures | server | Parameter for server in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| test_brand_readable_result_and_bounded_disclosures | width | Parameter for width in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| test_brand_readable_result_and_bounded_disclosures | expect | Imported dependency for expect in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 213 |
| test_brand_readable_result_and_bounded_disclosures | context | Local binding for context in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_brand_readable_result_and_bounded_disclosures | page | Local binding for page in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_brand_readable_result_and_bounded_disclosures | project | Local binding for project in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 222 |
| test_brand_readable_result_and_bounded_disclosures | selector | Loop item for selector in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 226 |
| test_brand_readable_result_and_bounded_disclosures | checkbox | Local binding for checkbox in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_brand_readable_result_and_bounded_disclosures | send | Local binding for send in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 244 |
| test_brand_readable_result_and_bounded_disclosures | colors | Local binding for colors in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_brand_readable_result_and_bounded_disclosures | output | Expression binding for output in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 263, 293 |
| test_brand_readable_result_and_bounded_disclosures.luminance | color | Parameter for color in test_brand_readable_result_and_bounded_disclosures.luminance; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 269 |
| test_brand_readable_result_and_bounded_disclosures.luminance | channels | Local binding for channels in test_brand_readable_result_and_bounded_disclosures.luminance; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 271 |
| test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_271 | x | Comprehension item for x in test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_271; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 271 |
| test_brand_readable_result_and_bounded_disclosures.luminance | values | Local binding for values in test_brand_readable_result_and_bounded_disclosures.luminance; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 272 |
| test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_272 | x | Comprehension item for x in test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_272; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 272 |
| test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_273 | a | Comprehension item for a in test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_273; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 273 |
| test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_273 | b | Comprehension item for b in test_brand_readable_result_and_bounded_disclosures.luminance.comprehension_273; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 273 |
| test_brand_readable_result_and_bounded_disclosures | lights | Local binding for lights in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 275 |
| test_brand_readable_result_and_bounded_disclosures | cases | Local binding for cases in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 279 |
| test_brand_readable_result_and_bounded_disclosures | catalog | Local binding for catalog in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 287 |
| test_brand_readable_result_and_bounded_disclosures | destination | Local binding for destination in test_brand_readable_result_and_bounded_disclosures; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| test_model_sidebar_is_hideable_and_key_input_clears | browser | Parameter for browser in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 302 |
| test_model_sidebar_is_hideable_and_key_input_clears | server | Parameter for server in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 302 |
| test_model_sidebar_is_hideable_and_key_input_clears | expect | Imported dependency for expect in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 304 |
| test_model_sidebar_is_hideable_and_key_input_clears | context | Local binding for context in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 306 |
| test_model_sidebar_is_hideable_and_key_input_clears | page | Local binding for page in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
| test_model_sidebar_is_hideable_and_key_input_clears | sidebar | Local binding for sidebar in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 310 |
| test_model_sidebar_is_hideable_and_key_input_clears | destination | Local binding for destination in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| test_model_sidebar_is_hideable_and_key_input_clears | toggle | Local binding for toggle in test_model_sidebar_is_hideable_and_key_input_clears; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 332 |
| test_saved_profile_lifecycle_and_session_consent | browser | Parameter for browser in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 341 |
| test_saved_profile_lifecycle_and_session_consent | server | Parameter for server in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 341 |
| test_saved_profile_lifecycle_and_session_consent | expect | Imported dependency for expect in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 343 |
| test_saved_profile_lifecycle_and_session_consent | first | Local binding for first in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 345 |
| test_saved_profile_lifecycle_and_session_consent | second | Local binding for second in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 346 |
| test_saved_profile_lifecycle_and_session_consent.choose | page | Parameter for page in test_saved_profile_lifecycle_and_session_consent.choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_saved_profile_lifecycle_and_session_consent.choose | selector | Parameter for selector in test_saved_profile_lifecycle_and_session_consent.choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_saved_profile_lifecycle_and_session_consent.choose | label | Parameter for label in test_saved_profile_lifecycle_and_session_consent.choose; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_saved_profile_lifecycle_and_session_consent | page | Local binding for page in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 354 |
| test_saved_profile_lifecycle_and_session_consent | other | Local binding for other in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 357 |
| test_saved_profile_lifecycle_and_session_consent | key | Local binding for key in test_saved_profile_lifecycle_and_session_consent; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 366 |
| test_local_secret_controls_and_sidebar_button_colors | browser | Parameter for browser in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 418 |
| test_local_secret_controls_and_sidebar_button_colors | server | Parameter for server in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 418 |
| test_local_secret_controls_and_sidebar_button_colors | expect | Imported dependency for expect in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 420 |
| test_local_secret_controls_and_sidebar_button_colors | context | Local binding for context in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 422 |
| test_local_secret_controls_and_sidebar_button_colors | page | Local binding for page in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 424 |
| test_local_secret_controls_and_sidebar_button_colors | identifier | Loop item for identifier in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 429 |
| test_local_secret_controls_and_sidebar_button_colors | button | Local binding for button in test_local_secret_controls_and_sidebar_button_colors; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 436 |
| test_local_profile_save_refresh_reload_and_delete | browser | Parameter for browser in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 461 |
| test_local_profile_save_refresh_reload_and_delete | server | Parameter for server in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 461 |
| test_local_profile_save_refresh_reload_and_delete | expect | Imported dependency for expect in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 463 |
| test_local_profile_save_refresh_reload_and_delete | first | Local binding for first in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 465 |
| test_local_profile_save_refresh_reload_and_delete | second | Local binding for second in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 465 |
| test_local_profile_save_refresh_reload_and_delete | page | Local binding for page in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 467 |
| test_local_profile_save_refresh_reload_and_delete | other | Local binding for other in test_local_profile_save_refresh_reload_and_delete; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 477 |
| test_external_save_failure_survives_refresh_with_safe_reason | browser | Parameter for browser in test_external_save_failure_survives_refresh_with_safe_reason; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 502 |
| test_external_save_failure_survives_refresh_with_safe_reason | server | Parameter for server in test_external_save_failure_survives_refresh_with_safe_reason; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 502 |
| test_external_save_failure_survives_refresh_with_safe_reason | expect | Imported dependency for expect in test_external_save_failure_survives_refresh_with_safe_reason; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 504 |
| test_external_save_failure_survives_refresh_with_safe_reason | context | Local binding for context in test_external_save_failure_survives_refresh_with_safe_reason; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 506 |
| test_external_save_failure_survives_refresh_with_safe_reason | page | Local binding for page in test_external_save_failure_survives_refresh_with_safe_reason; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 508 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | browser | Parameter for browser in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 532 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | server | Parameter for server in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 532 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | expect | Imported dependency for expect in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 534 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | context | Local binding for context in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 536 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | page | Local binding for page in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 538 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | editor | Local binding for editor in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 542 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | validation_box | Local binding for validation box in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 546 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | editor_box | Local binding for editor box in test_reviewed_tool_reuse_has_fresh_result_without_review; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 547 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 551 |
| test_reviewed_tool_reuse_has_fresh_result_without_review | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | browser | Parameter for browser in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 567 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | server | Parameter for server in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 567 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | expect | Imported dependency for expect in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 569 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | context | Local binding for context in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 571 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | other_context | Local binding for other context in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 571 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | page | Local binding for page in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 573 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | editor | Local binding for editor in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 577 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | contrast | Local binding for contrast in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 583 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | background_chain | Local binding for background chain in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 596 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | capture | Expression binding for capture in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | other | Local binding for other in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 620 |
| test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift | output | Local binding for output in test_durable_reuse_survives_reload_other_browser_restart_and_detects_drift; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 635 |
