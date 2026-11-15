# Reference for tests/unit/test_stage_completion_adapter.py

Stage-ending tools must return control to host gates after a reviewed save.

Source fingerprint: 3f9a5fb0f31041918eddbd0df1fdef956197978f06796e83806978e61c355aa8

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_reviewed_specification_and_code_saves_end_the_agent_stage

Catch an adapter that asks the model again after the approved stage result.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_contract_rejection_keeps_the_coder_turn_open

A rejected contract is repairable inside the turn; only a save ends it.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution

Verify qa finishes on acceptance but reuse manager continues to execution.

Kind: callable. Declared return: Not declared / class. Source line: 56.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage | system | Parameter for system in test_reviewed_specification_and_code_saves_end_the_agent_stage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage | registered | Local binding for registered in test_reviewed_specification_and_code_saves_end_the_agent_stage; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 12 |
| test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12.lambda_12 | fn | Callback parameter for fn in test_reviewed_specification_and_code_saves_end_the_agent_stage.lambda_12.lambda_12; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 12 |
| test_contract_rejection_keeps_the_coder_turn_open | system | Parameter for system in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| test_contract_rejection_keeps_the_coder_turn_open | system.security.strict_tool_contract | Attribute for system.security.strict tool contract in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 25 |
| test_contract_rejection_keeps_the_coder_turn_open | registered | Local binding for registered in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_contract_rejection_keeps_the_coder_turn_open.lambda_28 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 28 |
| test_contract_rejection_keeps_the_coder_turn_open.lambda_28.lambda_28 | fn | Callback parameter for fn in test_contract_rejection_keeps_the_coder_turn_open.lambda_28.lambda_28; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 28 |
| test_contract_rejection_keeps_the_coder_turn_open | tool | Local binding for tool in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_contract_rejection_keeps_the_coder_turn_open | rejection | Local binding for rejection in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_contract_rejection_keeps_the_coder_turn_open | system.security.auto_approve | Attribute for system.security.auto approve in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 39 |
| test_contract_rejection_keeps_the_coder_turn_open | saved | Local binding for saved in test_contract_rejection_keeps_the_coder_turn_open; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution | system | Parameter for system in test_qa_finishes_on_acceptance_but_reuse_manager_continues_to_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 56 |
