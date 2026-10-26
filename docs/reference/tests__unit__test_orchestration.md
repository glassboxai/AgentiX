# Reference for tests/unit/test_orchestration.py

Characterize catalog inspection and manager routing without LLM calls.

Source fingerprint: 25542ba650aaebcc263bf3a9f332c9b2abe36e3c97c60c46534540ec22e550d5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### install

Create a catalog input fixture without executing it.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_catalog_missing_root

Verify catalog missing root.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### test_catalog_empty_root

Verify catalog empty root.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_catalog_extracts_public_function_and_first_docstring_line

Verify catalog extracts public function and first docstring line.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_catalog_never_executes_module

Verify catalog never executes module.

Kind: callable. Declared return: Not declared / class. Source line: 40.

### test_catalog_order_is_stable

Verify catalog order is stable.

Kind: callable. Declared return: Not declared / class. Source line: 46.

### test_catalog_reports_syntax_error_and_continues

Verify catalog reports syntax error and continues.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### test_catalog_ignores_missing_code_and_plain_files

Verify catalog ignores missing code and plain files.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_catalog_reports_no_functions

Verify catalog reports no functions.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_catalog_default_description

Verify catalog default description.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_existing_tool_answer_does_not_create_pipeline

Verify existing tool answer does not create pipeline.

Kind: callable. Declared return: Not declared / class. Source line: 81.

### test_create_tool_routing

Verify create tool routing.

Kind: callable. Declared return: Not declared / class. Source line: 100.

### test_create_tool_routing.execute

Provide execute for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 103.

### test_create_tool_routing.completed

Provide completed for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 116.

### test_malformed_decision_is_rejected_without_fallback

Approved FLOW-02 replaces the formerly characterized arbitrary fallback.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### test_pipeline_preserves_task_order_and_context

Approved staged design stops at an unsaved specification instead of advancing.

Kind: callable. Declared return: Not declared / class. Source line: 159.

### test_manager_failure_propagates

Verify manager failure propagates.

Kind: callable. Declared return: Not declared / class. Source line: 170.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| install | system | Parameter for system in install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| install | folder | Local binding for folder in install; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_catalog_missing_root | system | Parameter for system in test_catalog_missing_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_catalog_empty_root | system | Parameter for system in test_catalog_empty_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_catalog_extracts_public_function_and_first_docstring_line | system | Parameter for system in test_catalog_extracts_public_function_and_first_docstring_line; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_catalog_extracts_public_function_and_first_docstring_line | catalog | Local binding for catalog in test_catalog_extracts_public_function_and_first_docstring_line; use the enclosing contract and type below. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_catalog_never_executes_module | system | Parameter for system in test_catalog_never_executes_module; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| test_catalog_order_is_stable | system | Parameter for system in test_catalog_order_is_stable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| test_catalog_order_is_stable | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_catalog_reports_syntax_error_and_continues | system | Parameter for system in test_catalog_reports_syntax_error_and_continues; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| test_catalog_reports_syntax_error_and_continues | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_catalog_ignores_missing_code_and_plain_files | system | Parameter for system in test_catalog_ignores_missing_code_and_plain_files; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| test_catalog_reports_no_functions | system | Parameter for system in test_catalog_reports_no_functions; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_catalog_default_description | system | Parameter for system in test_catalog_default_description; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_existing_tool_answer_does_not_create_pipeline | system | Parameter for system in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| test_existing_tool_answer_does_not_create_pipeline | monkeypatch | Parameter for monkeypatch in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| test_existing_tool_answer_does_not_create_pipeline | pipeline | Local binding for pipeline in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_create_tool_routing | system | Parameter for system in test_create_tool_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_create_tool_routing | monkeypatch | Parameter for monkeypatch in test_create_tool_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_create_tool_routing | response | Bounded response text to render or validate; it is not executable code. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_create_tool_routing | crew | Local binding for crew in test_create_tool_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_create_tool_routing.completed | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 116 |
| test_create_tool_routing.completed | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_create_tool_routing.completed | ledger | Local binding for ledger in test_create_tool_routing.completed; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_create_tool_routing.completed | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_create_tool_routing.completed | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_create_tool_routing | pipeline | Local binding for pipeline in test_create_tool_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_malformed_decision_is_rejected_without_fallback | system | Parameter for system in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_malformed_decision_is_rejected_without_fallback | monkeypatch | Parameter for monkeypatch in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| test_malformed_decision_is_rejected_without_fallback | pipeline | Local binding for pipeline in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| test_pipeline_preserves_task_order_and_context | system | Parameter for system in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 159 |
| test_pipeline_preserves_task_order_and_context | monkeypatch | Parameter for monkeypatch in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 159 |
| test_pipeline_preserves_task_order_and_context | crew | Local binding for crew in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| test_manager_failure_propagates | system | Parameter for system in test_manager_failure_propagates; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 170 |
| test_manager_failure_propagates | monkeypatch | Parameter for monkeypatch in test_manager_failure_propagates; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 170 |
