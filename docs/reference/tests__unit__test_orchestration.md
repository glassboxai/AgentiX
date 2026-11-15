# Reference for tests/unit/test_orchestration.py

Characterize catalog inspection and manager routing without LLM calls.

Source fingerprint: a3787f4908ef5d03e9aaa6db716aca78944fcb4c9f780bb1ee42e2d02f68d3c0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### install

Create a catalog input fixture without executing it.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_catalog_missing_root

Verify catalog missing root.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_catalog_empty_root

Verify catalog empty root.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_catalog_extracts_public_function_and_first_docstring_line

Verify catalog extracts public function and first docstring line.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### test_catalog_never_executes_module

Verify catalog never executes module.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_catalog_order_is_stable

Verify catalog order is stable.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### test_catalog_reports_syntax_error_and_continues

Verify catalog reports syntax error and continues.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_catalog_ignores_missing_code_and_plain_files

Verify catalog ignores missing code and plain files.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_catalog_reports_no_functions

Verify catalog reports no functions.

Kind: callable. Declared return: Not declared / class. Source line: 70.

### test_catalog_default_description

Verify catalog default description.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_existing_tool_answer_does_not_create_pipeline

Verify existing tool answer does not create pipeline.

Kind: callable. Declared return: Not declared / class. Source line: 82.

### test_create_tool_routing

Verify create tool routing.

Kind: callable. Declared return: Not declared / class. Source line: 105.

### test_create_tool_routing.execute

Provide execute for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_create_tool_routing.completed

Provide completed for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 121.

### test_malformed_decision_is_rejected_without_fallback

Approved FLOW-02 replaces the formerly characterized arbitrary fallback.

Kind: callable. Declared return: Not declared / class. Source line: 150.

### test_pipeline_preserves_task_order_and_context

Approved staged design stops at an unsaved specification instead of advancing.

Kind: callable. Declared return: Not declared / class. Source line: 164.

### test_manager_failure_propagates

Verify manager failure propagates.

Kind: callable. Declared return: Not declared / class. Source line: 175.

### test_legacy_run_application_answer_never_executes_from_the_tools_tab

A legacy RUN_APPLICATION answer fails closed instead of running an application.

Kind: callable. Declared return: Not declared / class. Source line: 186.

### test_manager_system_instructions_keep_tools_authoritative

The role must not imply that a Tools-tab query may execute an application.

Kind: callable. Declared return: Not declared / class. Source line: 229.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| install | system | Parameter for system in install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| install | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| install | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| install | folder | Local binding for folder in install; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_catalog_missing_root | system | Parameter for system in test_catalog_missing_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| test_catalog_empty_root | system | Parameter for system in test_catalog_empty_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_catalog_extracts_public_function_and_first_docstring_line | system | Parameter for system in test_catalog_extracts_public_function_and_first_docstring_line; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| test_catalog_extracts_public_function_and_first_docstring_line | catalog | Local binding for catalog in test_catalog_extracts_public_function_and_first_docstring_line; use the enclosing contract and type below. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_catalog_never_executes_module | system | Parameter for system in test_catalog_never_executes_module; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_catalog_order_is_stable | system | Parameter for system in test_catalog_order_is_stable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_catalog_order_is_stable | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_catalog_reports_syntax_error_and_continues | system | Parameter for system in test_catalog_reports_syntax_error_and_continues; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_catalog_reports_syntax_error_and_continues | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_catalog_ignores_missing_code_and_plain_files | system | Parameter for system in test_catalog_ignores_missing_code_and_plain_files; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_catalog_reports_no_functions | system | Parameter for system in test_catalog_reports_no_functions; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_catalog_default_description | system | Parameter for system in test_catalog_default_description; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_existing_tool_answer_does_not_create_pipeline | system | Parameter for system in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_existing_tool_answer_does_not_create_pipeline | monkeypatch | Parameter for monkeypatch in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_existing_tool_answer_does_not_create_pipeline | caplog | Parameter for caplog in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| test_existing_tool_answer_does_not_create_pipeline | pipeline | Local binding for pipeline in test_existing_tool_answer_does_not_create_pipeline; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_create_tool_routing | system | Parameter for system in test_create_tool_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_create_tool_routing | monkeypatch | Parameter for monkeypatch in test_create_tool_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_create_tool_routing | response | Bounded response text to render or validate; it is not executable code. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 105 |
| test_create_tool_routing | crew | Local binding for crew in test_create_tool_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| test_create_tool_routing.completed | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| test_create_tool_routing.completed | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_create_tool_routing.completed | ledger | Local binding for ledger in test_create_tool_routing.completed; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_create_tool_routing.completed | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_create_tool_routing.completed | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_create_tool_routing | pipeline | Local binding for pipeline in test_create_tool_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_malformed_decision_is_rejected_without_fallback | system | Parameter for system in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 150 |
| test_malformed_decision_is_rejected_without_fallback | monkeypatch | Parameter for monkeypatch in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 150 |
| test_malformed_decision_is_rejected_without_fallback | pipeline | Local binding for pipeline in test_malformed_decision_is_rejected_without_fallback; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_pipeline_preserves_task_order_and_context | system | Parameter for system in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 164 |
| test_pipeline_preserves_task_order_and_context | monkeypatch | Parameter for monkeypatch in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 164 |
| test_pipeline_preserves_task_order_and_context | crew | Local binding for crew in test_pipeline_preserves_task_order_and_context; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_manager_failure_propagates | system | Parameter for system in test_manager_failure_propagates; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 175 |
| test_manager_failure_propagates | monkeypatch | Parameter for monkeypatch in test_manager_failure_propagates; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 175 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | json | Imported dependency for json in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 188 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | Orchestrator | Imported dependency for Orchestrator in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 190 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | agent | Local binding for agent in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | agents | Local binding for agents in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | apps | Local binding for apps in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | orchestrator | Local binding for orchestrator in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_legacy_run_application_answer_never_executes_from_the_tools_tab | orchestrator.build_tool_pipeline | Attribute for orchestrator.build tool pipeline in test_legacy_run_application_answer_never_executes_from_the_tools_tab; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_manager_system_instructions_keep_tools_authoritative | system | Parameter for system in test_manager_system_instructions_keep_tools_authoritative; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 229 |
| test_manager_system_instructions_keep_tools_authoritative | manager | Local binding for manager in test_manager_system_instructions_keep_tools_authoritative; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 231 |
