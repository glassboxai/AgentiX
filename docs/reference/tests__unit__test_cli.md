# Reference for tests/unit/test_cli.py

Preserve CLI exit, blank-input and failure recovery behavior.

Source fingerprint: a3edf32511e7a3bb13291c1e795bb88b207c69f24281b7d7b44dc819fa6e17a1

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_exit_aliases_do_not_run_workflow

Verify exit aliases do not run workflow.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_blank_input_is_ignored_and_valid_query_is_trimmed

Verify blank input is ignored and valid query is trimmed.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_cli_reports_workflow_failure_and_accepts_next_query

Verify cli reports workflow failure and accepts next query.

Kind: callable. Declared return: Not declared / class. Source line: 32.

### test_cli_diagnostics_do_not_log_exception_payload

Verify cli diagnostics do not log exception payload.

Kind: callable. Declared return: Not declared / class. Source line: 44.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | run_cli | Imported dependency for run cli in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_exit_aliases_do_not_run_workflow | monkeypatch | Parameter for monkeypatch in test_exit_aliases_do_not_run_workflow; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| test_exit_aliases_do_not_run_workflow | alias | Parameter for alias in test_exit_aliases_do_not_run_workflow; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| test_exit_aliases_do_not_run_workflow.lambda_13 | prompt | Callback parameter for prompt in test_exit_aliases_do_not_run_workflow.lambda_13; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 13 |
| test_exit_aliases_do_not_run_workflow | workflow | Local binding for workflow in test_exit_aliases_do_not_run_workflow; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_exit_aliases_do_not_run_workflow | stopped | Managed resource for stopped in test_exit_aliases_do_not_run_workflow; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 15 |
| test_blank_input_is_ignored_and_valid_query_is_trimmed | monkeypatch | Parameter for monkeypatch in test_blank_input_is_ignored_and_valid_query_is_trimmed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_blank_input_is_ignored_and_valid_query_is_trimmed | capsys | Parameter for capsys in test_blank_input_is_ignored_and_valid_query_is_trimmed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_blank_input_is_ignored_and_valid_query_is_trimmed | inputs | Local binding for inputs in test_blank_input_is_ignored_and_valid_query_is_trimmed; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_blank_input_is_ignored_and_valid_query_is_trimmed.lambda_24 | prompt | Callback parameter for prompt in test_blank_input_is_ignored_and_valid_query_is_trimmed.lambda_24; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 24 |
| test_blank_input_is_ignored_and_valid_query_is_trimmed | workflow | Local binding for workflow in test_blank_input_is_ignored_and_valid_query_is_trimmed; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_cli_reports_workflow_failure_and_accepts_next_query | monkeypatch | Parameter for monkeypatch in test_cli_reports_workflow_failure_and_accepts_next_query; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| test_cli_reports_workflow_failure_and_accepts_next_query | capsys | Parameter for capsys in test_cli_reports_workflow_failure_and_accepts_next_query; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| test_cli_reports_workflow_failure_and_accepts_next_query | inputs | Local binding for inputs in test_cli_reports_workflow_failure_and_accepts_next_query; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_cli_reports_workflow_failure_and_accepts_next_query.lambda_35 | prompt | Callback parameter for prompt in test_cli_reports_workflow_failure_and_accepts_next_query.lambda_35; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 35 |
| test_cli_reports_workflow_failure_and_accepts_next_query | workflow | Local binding for workflow in test_cli_reports_workflow_failure_and_accepts_next_query; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_cli_reports_workflow_failure_and_accepts_next_query | output | Local binding for output in test_cli_reports_workflow_failure_and_accepts_next_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_cli_diagnostics_do_not_log_exception_payload | monkeypatch | Parameter for monkeypatch in test_cli_diagnostics_do_not_log_exception_payload; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_cli_diagnostics_do_not_log_exception_payload | caplog | Parameter for caplog in test_cli_diagnostics_do_not_log_exception_payload; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_cli_diagnostics_do_not_log_exception_payload | inputs | Local binding for inputs in test_cli_diagnostics_do_not_log_exception_payload; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_cli_diagnostics_do_not_log_exception_payload.lambda_47 | prompt | Callback parameter for prompt in test_cli_diagnostics_do_not_log_exception_payload.lambda_47; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 47 |
