# Reference for tests/test_v5_code_assistance.py

Read-only code explanation uses bounded, explicitly selected context.

Source fingerprint: b26cf5b5031f520a66c746deaba0dfa093b4cd7a8da2cbbeac1ac6544af09bd6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### assistant

Resolve the application service without importing Gradio or a provider SDK.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### test_explanation_receives_selected_source_and_specs_without_execution

Catch omission of the current editor buffer or unexpected source execution.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_explanation_receives_selected_source_and_specs_without_execution.Client

Synthetic model boundary; no provider SDK or network.

Kind: class. Declared return: Not declared / class. Source line: 18.

### test_explanation_receives_selected_source_and_specs_without_execution.Client.call

Observe the exact request or reproduce a provider failure.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_excessive_context_is_rejected_before_provider_call

Avoid silently sending unbounded files or user input to a model.

Kind: callable. Declared return: Not declared / class. Source line: 37.

### test_provider_exception_is_redacted

SDK error bodies and credentials must not be shown or logged.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_provider_exception_is_redacted.Client

Synthetic model boundary; no provider SDK or network.

Kind: class. Declared return: Not declared / class. Source line: 51.

### test_provider_exception_is_redacted.Client.call

Observe the exact request or reproduce a provider failure.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### test_foreign_session_is_rejected_before_context_access

The helper must not read another browser's candidate or specification.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_external_explanation_requires_fresh_remote_consent

A saved provider profile never implicitly authorizes sharing editor content.

Kind: callable. Declared return: Not declared / class. Source line: 92.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| assistant | explain_code | Imported dependency for explain code in assistant; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_explanation_receives_selected_source_and_specs_without_execution.Client.call | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_explanation_receives_selected_source_and_specs_without_execution.Client.call | messages | Parameter for messages in test_explanation_receives_selected_source_and_specs_without_execution.Client.call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_explanation_receives_selected_source_and_specs_without_execution | context | Local binding for context in test_explanation_receives_selected_source_and_specs_without_execution; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 28 |
| test_provider_exception_is_redacted.Client.call | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| test_provider_exception_is_redacted.Client.call | messages | Parameter for messages in test_provider_exception_is_redacted.Client.call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| test_provider_exception_is_redacted | error | Managed resource for error in test_provider_exception_is_redacted; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 58 |
| test_foreign_session_is_rejected_before_context_access | SimpleNamespace | Imported dependency for SimpleNamespace in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 70 |
| test_foreign_session_is_rejected_before_context_access | registry | Imported dependency for registry in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 72 |
| test_foreign_session_is_rejected_before_context_access | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| test_foreign_session_is_rejected_before_context_access | ChatHelperBackend | Imported dependency for ChatHelperBackend in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 75 |
| test_foreign_session_is_rejected_before_context_access | SessionAccessError | Imported dependency for SessionAccessError in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 76 |
| test_foreign_session_is_rejected_before_context_access | sessions | Local binding for sessions in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_foreign_session_is_rejected_before_context_access | owner | Local binding for owner in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_foreign_session_is_rejected_before_context_access | helper | Local binding for helper in test_foreign_session_is_rejected_before_context_access; use the enclosing contract and type below. | Return type of ChatHelperBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_external_explanation_requires_fresh_remote_consent | ModelProfile | Imported dependency for ModelProfile in test_external_explanation_requires_fresh_remote_consent; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_external_explanation_requires_fresh_remote_consent | create_profile_llm | Imported dependency for create profile llm in test_external_explanation_requires_fresh_remote_consent; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_external_explanation_requires_fresh_remote_consent | profile | Local binding for profile in test_external_explanation_requires_fresh_remote_consent; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_external_explanation_requires_fresh_remote_consent.lambda_104 | host | Callback parameter for host in test_external_explanation_requires_fresh_remote_consent.lambda_104; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 104 |
