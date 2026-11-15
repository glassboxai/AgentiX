# Reference for tests/test_typed_results.py

Typed result presentation does not expose raw JSON as the default output.

Source fingerprint: 604e6d31be626ad45d7b1c10198b1fb04e68024455c142906671b8f9a09cba37

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_text_number_boolean_and_table_use_corresponding_readonly_components

Output contracts drive components; no model HTML or JSON renderer is needed.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_text_number_boolean_and_table_use_corresponding_readonly_components.component

Record construction only, without requiring a browser.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### test_result_values_validate_types_and_clear_on_failure

False must not be rendered as a numerical zero; invalid output remains unpublished.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_tables_reject_unbounded_or_nonfinite_cells

Dataframe presentation accepts bounded scalar JSON data only.

Kind: callable. Declared return: Not declared / class. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components | ResultField | Imported dependency for ResultField in test_text_number_boolean_and_table_use_corresponding_readonly_components; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components | build_results | Imported dependency for build results in test_text_number_boolean_and_table_use_corresponding_readonly_components; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components | calls | Local binding for calls in test_text_number_boolean_and_table_use_corresponding_readonly_components; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 12 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components.component | kind | Parameter for kind in test_text_number_boolean_and_table_use_corresponding_readonly_components.component; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components | gr | Local binding for gr in test_text_number_boolean_and_table_use_corresponding_readonly_components; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components | fields | Local binding for fields in test_text_number_boolean_and_table_use_corresponding_readonly_components; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 24 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_31 | kind | Comprehension item for kind in test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_31; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 31 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_31 | _ | Comprehension item for  in test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_31; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 31 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_32 | _ | Comprehension item for  in test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_32; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_32 | values | Comprehension item for values in test_text_number_boolean_and_table_use_corresponding_readonly_components.comprehension_32; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| test_result_values_validate_types_and_clear_on_failure | ResultField | Imported dependency for ResultField in test_result_values_validate_types_and_clear_on_failure; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 37 |
| test_result_values_validate_types_and_clear_on_failure | result_values | Imported dependency for result values in test_result_values_validate_types_and_clear_on_failure; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 37 |
| test_result_values_validate_types_and_clear_on_failure | fields | Local binding for fields in test_result_values_validate_types_and_clear_on_failure; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 39 |
| test_tables_reject_unbounded_or_nonfinite_cells | cell | Parameter for cell in test_tables_reject_unbounded_or_nonfinite_cells; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_tables_reject_unbounded_or_nonfinite_cells | ResultField | Imported dependency for ResultField in test_tables_reject_unbounded_or_nonfinite_cells; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| test_tables_reject_unbounded_or_nonfinite_cells | result_values | Imported dependency for result values in test_tables_reject_unbounded_or_nonfinite_cells; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
