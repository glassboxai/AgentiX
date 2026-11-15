# Reference for tests/test_application_presentation.py

Bounded presentation regressions for the composite data-operation surface.

Source fingerprint: eb6a070a79adf4ce33df750b0e2cc8959f5c61a42b495e1aeb13d024bdf89cef

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_input_contract_names_keys_types_and_one_example_payload

V7-073: the owner reads the closed JSON contract before typing a payload.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_input_contract_keeps_model_description_inert_and_bounded

A model-authored description cannot inject markup or grow without a limit.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### test_input_contract_reports_an_application_without_declared_inputs

An empty closed input map is stated instead of rendering an empty table.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### test_named_results_bound_rows_and_cells_without_losing_types

Observed results become bounded text cells; oversized bodies are truncated.

Kind: callable. Declared return: Not declared / class. Source line: 61.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | MAX_RESULT_CELL_LENGTH | Imported dependency for MAX RESULT CELL LENGTH in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | MAX_RESULT_ROWS | Imported dependency for MAX RESULT ROWS in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | describe_data_inputs | Imported dependency for describe data inputs in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | named_result_rows | Imported dependency for named result rows in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_input_contract_names_keys_types_and_one_example_payload | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 13 |
| test_input_contract_names_keys_types_and_one_example_payload | text | Local binding for text in test_input_contract_names_keys_types_and_one_example_payload; use the enclosing contract and type below. | Return type of describe_data_inputs; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_input_contract_keeps_model_description_inert_and_bounded | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 38 |
| test_input_contract_keeps_model_description_inert_and_bounded | text | Local binding for text in test_input_contract_keeps_model_description_inert_and_bounded; use the enclosing contract and type below. | Return type of describe_data_inputs; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_named_results_bound_rows_and_cells_without_losing_types | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict | Enclosing invocation or class/instance lifetime | 63 |
| test_named_results_bound_rows_and_cells_without_losing_types.comprehension_69 | index | Comprehension item for index in test_named_results_bound_rows_and_cells_without_losing_types.comprehension_69; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| test_named_results_bound_rows_and_cells_without_losing_types | rows | Local binding for rows in test_named_results_bound_rows_and_cells_without_losing_types; use the enclosing contract and type below. | Return type of named_result_rows; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
