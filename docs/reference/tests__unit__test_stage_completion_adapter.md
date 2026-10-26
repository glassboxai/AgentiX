# Reference for tests/unit/test_stage_completion_adapter.py

Stage-ending tools must return control to host gates after a reviewed save.

Source fingerprint: a9f0566bf722993d4735d365b85874daf8f13b9fcab894e2ccd4b5d07cd75437

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_reviewed_specification_and_code_saves_end_the_agent_stage

Catch an adapter that asks the model again after the approved stage result.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution

Verify qa finishes on acceptance but reuse manager continues to execution.

Kind: callable. Declared return: Not declared / class. Source line: 23.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage | system | Parameter for system in test_reviewed_specification_and_code_saves_end_the_agent_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage | registered | Local binding for registered in test_reviewed_specification_and_code_saves_end_the_agent_stage; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 12 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12.lambda_12 | fn | Callback parameter for fn in test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12.lambda_12; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 12 |
| test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution | system | Parameter for system in test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
