# Reference for tests/test_widget_reuse.py

Persistent widget reuse tests use trusted temporary tools and explicit protection doubles.

Source fingerprint: 82ff26ec11211931291aad46c8650425ec11404abdf7eefa31f3e0064ab12d51

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Protector

Authenticated fixture boundary; not a claim of Windows DPAPI execution.

Kind: class. Declared return: Not declared / class. Source line: 12.

### Protector.seal

Encode one trusted fixture record.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### Protector.unseal

Reject unsigned fixture metadata.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### store

Build the production store over trusted fixture directories.

Kind: callable. Declared return: Not declared / class. Source line: 26.

### test_widget_is_colocated_and_reused_after_store_recreation

Exact approved widget bytes survive a fresh host adapter without a designer call.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### test_changed_widget_is_not_still_approved

Human edits become a fresh unapproved proposal, never an inherited grant.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_corrupt_protected_metadata_cannot_authorize_a_widget

An untrusted local metadata edit cannot publish a trusted widget grant.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### test_pipeline_reuses_published_widgets_without_another_designer_call

A new application may call Assembler, but must not regenerate approved widgets.

Kind: callable. Declared return: Not declared / class. Source line: 93.

### test_pipeline_reuses_published_widgets_without_another_designer_call.factory

Count model role calls while returning independently authored source fixtures.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client

Never use a real model in ordinary persistence tests.

Kind: callable. Declared return: Not declared / class. Source line: 107.

### test_widget_write_cannot_alias_the_approved_tool_source

Reject a resolved widget filename alias before any tool code can be overwritten.

Kind: callable. Declared return: Not declared / class. Source line: 167.

### test_changed_tool_contract_or_widget_policy_requires_new_review

Persisted widget approval cannot survive a changed dependency or runtime policy.

Kind: callable. Declared return: Not declared / class. Source line: 183.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | patch | Imported dependency for patch in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | widget_source | Imported dependency for widget source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | installed | Imported dependency for installed in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | registry | Imported dependency for registry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| Protector.seal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| Protector.seal | data | Parameter for data in Protector.seal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| Protector.unseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| Protector.unseal | data | Parameter for data in Protector.unseal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| store | tmp_path | Parameter for tmp path in store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| store | fixture | Parameter for fixture in store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| store | WidgetStore | Imported dependency for WidgetStore in store; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 28 |
| test_widget_is_colocated_and_reused_after_store_recreation | tmp_path | Parameter for tmp path in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| test_widget_is_colocated_and_reused_after_store_recreation | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_widget_is_colocated_and_reused_after_store_recreation | fixture | Local binding for fixture in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_widget_is_colocated_and_reused_after_store_recreation | tool | Local binding for tool in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_widget_is_colocated_and_reused_after_store_recreation | proposal | Local binding for proposal in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 44 |
| test_widget_is_colocated_and_reused_after_store_recreation | service | Local binding for service in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_widget_is_colocated_and_reused_after_store_recreation | saved | Local binding for saved in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_widget_is_colocated_and_reused_after_store_recreation | loaded | Local binding for loaded in test_widget_is_colocated_and_reused_after_store_recreation; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_changed_widget_is_not_still_approved | tmp_path | Parameter for tmp path in test_changed_widget_is_not_still_approved; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| test_changed_widget_is_not_still_approved | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_changed_widget_is_not_still_approved | fixture | Local binding for fixture in test_changed_widget_is_not_still_approved; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_changed_widget_is_not_still_approved | tool | Local binding for tool in test_changed_widget_is_not_still_approved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_changed_widget_is_not_still_approved | service | Local binding for service in test_changed_widget_is_not_still_approved; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_changed_widget_is_not_still_approved | proposal | Local binding for proposal in test_changed_widget_is_not_still_approved; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 65 |
| test_changed_widget_is_not_still_approved | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | tmp_path | Parameter for tmp path in test_corrupt_protected_metadata_cannot_authorize_a_widget; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | fixture | Local binding for fixture in test_corrupt_protected_metadata_cannot_authorize_a_widget; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | tool | Local binding for tool in test_corrupt_protected_metadata_cannot_authorize_a_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | service | Local binding for service in test_corrupt_protected_metadata_cannot_authorize_a_widget; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_corrupt_protected_metadata_cannot_authorize_a_widget | record | Local binding for record in test_corrupt_protected_metadata_cannot_authorize_a_widget; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | tmp_path | Parameter for tmp path in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | ApplicationPipeline | Imported dependency for ApplicationPipeline in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 95 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 95 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | fixture | Local binding for fixture in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | tools | Local binding for tools in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | service | Local binding for service in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | calls | Local binding for calls in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 102 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory | folder | Parameter for folder in test_pipeline_reuses_published_widgets_without_another_designer_call.factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client | role | Parameter for role in test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 107 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 107 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client | module | Local binding for module in test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client | catalog | Local binding for catalog in test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client.comprehension_125 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 125 |
| test_pipeline_reuses_published_widgets_without_another_designer_call.factory.client.comprehension_130 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 131 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | pipeline | Local binding for pipeline in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of ApplicationPipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | item | Local binding for item in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 140 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | supervisor | Local binding for supervisor in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_pipeline_reuses_published_widgets_without_another_designer_call | second | Local binding for second in test_pipeline_reuses_published_widgets_without_another_designer_call; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| test_widget_write_cannot_alias_the_approved_tool_source | tmp_path | Parameter for tmp path in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_widget_write_cannot_alias_the_approved_tool_source | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_widget_write_cannot_alias_the_approved_tool_source | fixture | Local binding for fixture in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_widget_write_cannot_alias_the_approved_tool_source | tool | Local binding for tool in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 172 |
| test_widget_write_cannot_alias_the_approved_tool_source | service | Local binding for service in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| test_widget_write_cannot_alias_the_approved_tool_source | target | Local binding for target in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_widget_write_cannot_alias_the_approved_tool_source | fixture.ledger.security.validate_and_resolve_path | Attribute for fixture.ledger.security.validate and resolve path in test_widget_write_cannot_alias_the_approved_tool_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | tmp_path | Parameter for tmp path in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | replace | Imported dependency for replace in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 185 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | WidgetStore | Imported dependency for WidgetStore in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 187 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | fixture | Local binding for fixture in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | tool | Local binding for tool in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | service | Local binding for service in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Return type of store; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| test_changed_tool_contract_or_widget_policy_requires_new_review | other | Local binding for other in test_changed_tool_contract_or_widget_policy_requires_new_review; use the enclosing contract and type below. | Return type of WidgetStore; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
