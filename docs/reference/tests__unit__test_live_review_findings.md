# Reference for tests/unit/test_live_review_findings.py

Desired regressions for requirements lost during the supervised GUI run.

Source fingerprint: ab12f0d6a1eea30a4b6716b6c7a64f9741424c410f467b6992dc39522ae7dab3

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_creation_pipeline_retains_original_user_contract

A shortened manager purpose must not remove the user's input/error contract.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_creation_pipeline_retains_original_user_contract.downstream

Observe the actual contract received by the creation-stage boundary.

Kind: callable. Declared return: Not declared / class. Source line: 16.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| test_creation_pipeline_retains_original_user_contract | system | Parameter for system in test_creation_pipeline_retains_original_user_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_creation_pipeline_retains_original_user_contract | monkeypatch | Parameter for monkeypatch in test_creation_pipeline_retains_original_user_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_creation_pipeline_retains_original_user_contract | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 9 |
| test_creation_pipeline_retains_original_user_contract | decision | Local binding for decision in test_creation_pipeline_retains_original_user_contract; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 10 |
| test_creation_pipeline_retains_original_user_contract | received | Local binding for received in test_creation_pipeline_retains_original_user_contract; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 14 |
| test_creation_pipeline_retains_original_user_contract.downstream | tool_name | Validated public tool identifier within the configured storage boundary. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_creation_pipeline_retains_original_user_contract.downstream | user_requirement | Parameter for user requirement in test_creation_pipeline_retains_original_user_contract.downstream; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
