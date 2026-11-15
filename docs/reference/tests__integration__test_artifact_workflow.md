# Reference for tests/integration/test_artifact_workflow.py

Integrate storage, compilation, unittest protocol and execution gating.

Only trusted fixture code is executed. CrewAI and widgets remain substituted;
The native OS observation is doubled. This is not a native isolation, live LLM
or browser end-to-end test; those security checks are explicitly opt-in.

Source fingerprint: c3cdc60772048fd5c0ccdcd565d81dc5d3431109c62cad79a3e4fc3e8b14b34f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_complete_trusted_tool_lifecycle

Verify complete trusted tool lifecycle.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_real_failing_generated_test_creates_incident

Verify real failing generated test creates incident.

Kind: callable. Declared return: Not declared / class. Source line: 47.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | approve_next_review | Imported dependency for approve next review in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| test_complete_trusted_tool_lifecycle | system | Parameter for system in test_complete_trusted_tool_lifecycle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| test_complete_trusted_tool_lifecycle | system.security.auto_approve | Attribute for system.security.auto approve in test_complete_trusted_tool_lifecycle; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 13 |
| test_complete_trusted_tool_lifecycle | tools | Local binding for tools in test_complete_trusted_tool_lifecycle; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_complete_trusted_tool_lifecycle | test_code | Proposed unittest source requiring approval and isolated execution. | str | Enclosing invocation or class/instance lifetime | 19 |
| test_complete_trusted_tool_lifecycle | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_complete_trusted_tool_lifecycle | thread | Local binding for thread in test_complete_trusted_tool_lifecycle; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_complete_trusted_tool_lifecycle | errors | Local binding for errors in test_complete_trusted_tool_lifecycle; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_real_failing_generated_test_creates_incident | system | Parameter for system in test_real_failing_generated_test_creates_incident; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_real_failing_generated_test_creates_incident | system.security.auto_approve | Attribute for system.security.auto approve in test_real_failing_generated_test_creates_incident; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 49 |
| test_real_failing_generated_test_creates_incident | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 51 |
| test_real_failing_generated_test_creates_incident | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
