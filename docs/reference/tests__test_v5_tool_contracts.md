# Reference for tests/test_v5_tool_contracts.py

Strict generated-tool contracts and presentation regression tests.

Source fingerprint: 55e6ab330523ed2f560340e2cbee3c4587e4cc779cf5cc3f4a5ac009c435d42a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_schema_uses_canonical_function_and_annotated_metadata

Extract JSON-safe strict types and descriptions without source execution.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_invalid_public_contract_rejected

Naming and meaningful Annotated descriptions are mandatory.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_activity_removes_decorative_pipes_only

Keep internal operators and raw diagnostic text intact.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_pure_private_helpers_and_seeded_random_are_portable

Private local helpers and stdlib randomness do not require host capabilities.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### test_activity_preserves_code_indentation_and_escapes_nested_markup

Removing frames must not destroy Python structure or activate generated HTML.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_agent_catalog_includes_annotated_parameter_meaning

The manager must actually receive metadata, not only bare argument names.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### test_activity_strips_trailing_border_on_interleaved_console_fragment

Rich and diagnostic fragments may split a frame, leaving only its right edge.

Kind: callable. Declared return: Not declared / class. Source line: 78.

### test_discard_comprehension_target_is_pure_but_private_loads_stay_blocked

The random tool's conventional underscore loop variable is not introspection.

Kind: callable. Declared return: Not declared / class. Source line: 85.

### test_literal_metadata_keeps_boolean_distinct_from_integer

Strict JSON contracts must not describe a Literal boolean as an integer.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_new_tool_module_documentation_is_mandatory

Generated production APIs cannot silently omit their module documentation.

Kind: callable. Declared return: Not declared / class. Source line: 107.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | format_thoughts_markdown | Imported dependency for format thoughts markdown in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | extract_tool_schema | Imported dependency for extract tool schema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | CODE | Module binding for CODE in module; use the enclosing contract and type below. | Return type of join; see its callable contract | Module/process lifetime | 8 |
| test_schema_uses_canonical_function_and_annotated_metadata | schema | Local binding for schema in test_schema_uses_canonical_function_and_annotated_metadata; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_invalid_public_contract_rejected | source | Explicit source document or source-code text; never imported for reference generation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_activity_removes_decorative_pipes_only | raw | Local binding for raw in test_activity_removes_decorative_pipes_only; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 43 |
| test_activity_removes_decorative_pipes_only | rendered | Local binding for rendered in test_activity_removes_decorative_pipes_only; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_pure_private_helpers_and_seeded_random_are_portable | computation_only | Imported dependency for computation only in test_pure_private_helpers_and_seeded_random_are_portable; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| test_pure_private_helpers_and_seeded_random_are_portable | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 54 |
| test_activity_preserves_code_indentation_and_escapes_nested_markup | text | Local binding for text in test_activity_preserves_code_indentation_and_escapes_nested_markup; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 60 |
| test_activity_preserves_code_indentation_and_escapes_nested_markup | rendered | Local binding for rendered in test_activity_preserves_code_indentation_and_escapes_nested_markup; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_agent_catalog_includes_annotated_parameter_meaning | tmp_path | Parameter for tmp path in test_agent_catalog_includes_annotated_parameter_meaning; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| test_agent_catalog_includes_annotated_parameter_meaning | ToolCatalog | Imported dependency for ToolCatalog in test_agent_catalog_includes_annotated_parameter_meaning; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 68 |
| test_agent_catalog_includes_annotated_parameter_meaning | folder | Local binding for folder in test_agent_catalog_includes_annotated_parameter_meaning; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_agent_catalog_includes_annotated_parameter_meaning | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of render; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_activity_strips_trailing_border_on_interleaved_console_fragment | rendered | Local binding for rendered in test_activity_strips_trailing_border_on_interleaved_console_fragment; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_discard_comprehension_target_is_pure_but_private_loads_stay_blocked | computation_only | Imported dependency for computation only in test_discard_comprehension_target_is_pure_but_private_loads_stay_blocked; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 87 |
| test_literal_metadata_keeps_boolean_distinct_from_integer | source | Explicit source document or source-code text; never imported for reference generation. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_literal_metadata_keeps_boolean_distinct_from_integer | mixed | Local binding for mixed in test_literal_metadata_keeps_boolean_distinct_from_integer; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_new_tool_module_documentation_is_mandatory | source | Explicit source document or source-code text; never imported for reference generation. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
