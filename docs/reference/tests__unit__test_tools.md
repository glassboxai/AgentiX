# Reference for tests/unit/test_tools.py

Exercise actual artifact functions; replace only service and process boundaries.

Source fingerprint: eca3ff406294cc4bdfed386b8c54042ca664e5cae7224632b6dc24abdb4e68e4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### write_tool

Install a trusted test fixture into temporary tool storage.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### observe_fixture

Simulate the OS boundary observation for trusted call-focused fixtures.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_compile_strips_markdown_and_saves

Verify compile strips markdown and saves.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_invalid_syntax_logs_incident_without_saving_code

Verify invalid syntax logs incident without saving code.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_compilation_does_not_execute_code

Verify compilation does not execute code.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_save_specifications

Verify save specifications.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### test_incidence_logging_appends

Verify incidence logging appends.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_read_existing_artifact

Verify read existing artifact.

Kind: callable. Declared return: Not declared / class. Source line: 87.

### test_read_missing_artifact

Verify read missing artifact.

Kind: callable. Declared return: Not declared / class. Source line: 93.

### test_read_traversal_returns_error

Verify read traversal returns error.

Kind: callable. Declared return: Not declared / class. Source line: 98.

### test_execute_function_arguments

Verify execute function arguments.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_execute_missing_file

Verify execute missing file.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### test_execute_unknown_function_is_rejected

Verify execute unknown function is rejected.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### test_execute_invalid_json

Verify execute invalid json.

Kind: callable. Declared return: Not declared / class. Source line: 131.

### test_execute_errors_are_reported

Verify execute errors are reported.

Kind: callable. Declared return: Not declared / class. Source line: 146.

### test_test_runner_captures_results

Verify test runner captures results.

Kind: callable. Declared return: Not declared / class. Source line: 158.

### test_runner_failure_records_incident

Verify runner failure records incident.

Kind: callable. Declared return: Not declared / class. Source line: 190.

### test_rejected_test_file_is_never_executed

Verify rejected test file is never executed.

Kind: callable. Declared return: Not declared / class. Source line: 200.

### test_edited_python_is_validated_before_save

Verify edited python is validated before save.

Kind: callable. Declared return: Not declared / class. Source line: 211.

### test_invalid_edited_tests_are_not_executed

The same final-content validation must protect test-script persistence.

Kind: callable. Declared return: Not declared / class. Source line: 222.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| write_tool | system | Parameter for system in write_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| write_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| write_tool | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| write_tool | directory | Local binding for directory in write_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 12 |
| observe_fixture | system | Parameter for system in observe_fixture; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| observe_fixture | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| observe_fixture | ledger | Local binding for ledger in observe_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| observe_fixture | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| observe_fixture | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_compile_strips_markdown_and_saves | system | Parameter for system in test_compile_strips_markdown_and_saves; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_compile_strips_markdown_and_saves | wrapper | Parameter for wrapper in test_compile_strips_markdown_and_saves; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_compile_strips_markdown_and_saves | system.security.auto_approve | Attribute for system.security.auto approve in test_compile_strips_markdown_and_saves; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 36 |
| test_compile_strips_markdown_and_saves | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 37 |
| test_invalid_syntax_logs_incident_without_saving_code | system | Parameter for system in test_invalid_syntax_logs_incident_without_saving_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_invalid_syntax_logs_incident_without_saving_code | system.security.auto_approve | Attribute for system.security.auto approve in test_invalid_syntax_logs_incident_without_saving_code; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 46 |
| test_invalid_syntax_logs_incident_without_saving_code | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of compile_and_save_code_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_compilation_does_not_execute_code | system | Parameter for system in test_compilation_does_not_execute_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_compilation_does_not_execute_code | system.security.auto_approve | Attribute for system.security.auto approve in test_compilation_does_not_execute_code; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 55 |
| test_save_specifications | system | Parameter for system in test_save_specifications; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| test_save_specifications | system.security.auto_approve | Attribute for system.security.auto approve in test_save_specifications; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 63 |
| test_incidence_logging_appends | system | Parameter for system in test_incidence_logging_appends; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_incidence_logging_appends | function | Parameter for function in test_incidence_logging_appends; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_incidence_logging_appends | suffix | Parameter for suffix in test_incidence_logging_appends; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 76 |
| test_incidence_logging_appends | system.security.auto_approve | Attribute for system.security.auto approve in test_incidence_logging_appends; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 78 |
| test_incidence_logging_appends | log | Local binding for log in test_incidence_logging_appends; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_incidence_logging_appends | content | Artifact or review text whose encoding, size and approval state must be checked. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_read_existing_artifact | system | Parameter for system in test_read_existing_artifact; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| test_read_missing_artifact | system | Parameter for system in test_read_missing_artifact; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_read_traversal_returns_error | system | Parameter for system in test_read_traversal_returns_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 98 |
| test_execute_function_arguments | system | Parameter for system in test_execute_function_arguments; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_execute_function_arguments | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_execute_function_arguments | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_execute_missing_file | system | Parameter for system in test_execute_missing_file; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_execute_unknown_function_is_rejected | system | Parameter for system in test_execute_unknown_function_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_execute_unknown_function_is_rejected | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_execute_invalid_json | system | Parameter for system in test_execute_invalid_json; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 131 |
| test_execute_errors_are_reported | system | Parameter for system in test_execute_errors_are_reported; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_execute_errors_are_reported | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_execute_errors_are_reported | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 146 |
| test_test_runner_captures_results | system | Parameter for system in test_test_runner_captures_results; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_test_runner_captures_results | monkeypatch | Parameter for monkeypatch in test_test_runner_captures_results; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_test_runner_captures_results | returncode | Parameter for returncode in test_test_runner_captures_results; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_test_runner_captures_results | prefix | Parameter for prefix in test_test_runner_captures_results; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_test_runner_captures_results | system.security.auto_approve | Attribute for system.security.auto approve in test_test_runner_captures_results; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 160 |
| test_test_runner_captures_results | runner | Local binding for runner in test_test_runner_captures_results; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_test_runner_captures_results | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| test_runner_failure_records_incident | system | Parameter for system in test_runner_failure_records_incident; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_runner_failure_records_incident | monkeypatch | Parameter for monkeypatch in test_runner_failure_records_incident; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_runner_failure_records_incident | error | Parameter for error in test_runner_failure_records_incident; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_runner_failure_records_incident | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_runner_failure_records_incident | system.security.auto_approve | Attribute for system.security.auto approve in test_runner_failure_records_incident; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 192 |
| test_runner_failure_records_incident | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 195 |
| test_rejected_test_file_is_never_executed | system | Parameter for system in test_rejected_test_file_is_never_executed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_rejected_test_file_is_never_executed | monkeypatch | Parameter for monkeypatch in test_rejected_test_file_is_never_executed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 200 |
| test_rejected_test_file_is_never_executed | runner | Local binding for runner in test_rejected_test_file_is_never_executed; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_edited_python_is_validated_before_save | system | Parameter for system in test_edited_python_is_validated_before_save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| test_edited_python_is_validated_before_save | monkeypatch | Parameter for monkeypatch in test_edited_python_is_validated_before_save; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| test_edited_python_is_validated_before_save | target | Local binding for target in test_edited_python_is_validated_before_save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 218 |
| test_invalid_edited_tests_are_not_executed | system | Parameter for system in test_invalid_edited_tests_are_not_executed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| test_invalid_edited_tests_are_not_executed | monkeypatch | Parameter for monkeypatch in test_invalid_edited_tests_are_not_executed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| test_invalid_edited_tests_are_not_executed | runner | Local binding for runner in test_invalid_edited_tests_are_not_executed; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| test_invalid_edited_tests_are_not_executed | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
