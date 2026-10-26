# Reference for tests/unit/test_presentation.py

UI-012 presentation contracts use independent data, never generated artifacts.

Source fingerprint: 18de58689f6af7f913cc71f803f897fc99e2afcbc31370f850fe44b8ae6b6b00

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_observed_bill_has_readable_currency_and_collapsed_raw_evidence

Verify observed bill has readable currency and collapsed raw evidence.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_no_currency_is_invented_for_an_arbitrary_result

Verify no currency is invented for an arbitrary result.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_presentation_never_rounds_away_an_observed_rate

Verify presentation never rounds away an observed rate.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_result_payload_is_data_never_markup_or_executable

Verify result payload is data never markup or executable.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### test_catalog_details_are_collapsed_and_escape_untrusted_descriptions

Verify catalog details are collapsed and escape untrusted descriptions.

Kind: callable. Declared return: Not declared / class. Source line: 46.

### test_validation_summarizes_and_collapses_case_evidence

Verify validation summarizes and collapses case evidence.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded

Verify literal calls are never evaluated and oversized data is bounded.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### test_brand_has_requested_order_and_local_assets

Verify brand has requested order and local assets.

Kind: callable. Declared return: Not declared / class. Source line: 86.

### test_controller_formats_result_and_keeps_catalog_disclosure

Verify controller formats result and keeps catalog disclosure.

Kind: callable. Declared return: Not declared / class. Source line: 105.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | format_catalog | Imported dependency for format catalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | format_result | Imported dependency for format result in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | render_validation | Imported dependency for render validation in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_observed_bill_has_readable_currency_and_collapsed_raw_evidence | response | Bounded response text to render or validate; it is not executable code. | str | Enclosing invocation or class/instance lifetime | 8 |
| test_observed_bill_has_readable_currency_and_collapsed_raw_evidence | rendered | Local binding for rendered in test_observed_bill_has_readable_currency_and_collapsed_raw_evidence; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_no_currency_is_invented_for_an_arbitrary_result | rendered | Local binding for rendered in test_no_currency_is_invented_for_an_arbitrary_result; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_presentation_never_rounds_away_an_observed_rate | rendered | Local binding for rendered in test_presentation_never_rounds_away_an_observed_rate; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_result_payload_is_data_never_markup_or_executable | rendered | Local binding for rendered in test_result_payload_is_data_never_markup_or_executable; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_catalog_details_are_collapsed_and_escape_untrusted_descriptions | original | Local binding for original in test_catalog_details_are_collapsed_and_escape_untrusted_descriptions; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 48 |
| test_catalog_details_are_collapsed_and_escape_untrusted_descriptions | rendered | Local binding for rendered in test_catalog_details_are_collapsed_and_escape_untrusted_descriptions; use the enclosing contract and type below. | Return type of format_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_validation_summarizes_and_collapses_case_evidence | status | Local binding for status in test_validation_summarizes_and_collapses_case_evidence; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 57 |
| test_validation_summarizes_and_collapses_case_evidence | rendered | Local binding for rendered in test_validation_summarizes_and_collapses_case_evidence; use the enclosing contract and type below. | Return type of render_validation; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded | payload | Local binding for payload in test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 79 |
| test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded | rendered | Local binding for rendered in test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded | oversized | Local binding for oversized in test_literal_calls_are_never_evaluated_and_oversized_data_is_bounded; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_brand_has_requested_order_and_local_assets | header | Imported dependency for header in test_brand_has_requested_order_and_local_assets; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 88 |
| test_brand_has_requested_order_and_local_assets | launch_options | Imported dependency for launch options in test_brand_has_requested_order_and_local_assets; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 88 |
| test_brand_has_requested_order_and_local_assets | brand | Local binding for brand in test_brand_has_requested_order_and_local_assets; use the enclosing contract and type below. | Return type of header; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_brand_has_requested_order_and_local_assets | options | Local binding for options in test_brand_has_requested_order_and_local_assets; use the enclosing contract and type below. | Return type of launch_options; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_controller_formats_result_and_keeps_catalog_disclosure | system | Parameter for system in test_controller_formats_result_and_keeps_catalog_disclosure; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_controller_formats_result_and_keeps_catalog_disclosure | system.app.state.chat_history | Attribute for system.app.state.chat history in test_controller_formats_result_and_keeps_catalog_disclosure; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 107 |
| test_controller_formats_result_and_keeps_catalog_disclosure | system.app.state.last_response | Attribute for system.app.state.last response in test_controller_formats_result_and_keeps_catalog_disclosure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 111 |
| test_controller_formats_result_and_keeps_catalog_disclosure | system.app.state.is_running | Attribute for system.app.state.is running in test_controller_formats_result_and_keeps_catalog_disclosure; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 114 |
| test_controller_formats_result_and_keeps_catalog_disclosure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 115 |
