# Reference for tests/test_catalog_routing.py

Read-only routing must select a contract before any tool validation or execution.

Source fingerprint: 7e7ddcb83e6036f5c9a1e93ce8b3abb962a22b8e2f46777bc0f360876437157c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Catalog

Only a calculator exists in this authored fixture.

Kind: class. Declared return: Not declared / class. Source line: 10.

### Catalog.contracts

Return data rather than callable capabilities.

Kind: callable. Declared return: Not declared / class. Source line: 13.

### test_unmatched_query_can_request_creation_without_validating_existing_tool

The model has no verification or execution tool during semantic selection.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### test_unmatched_query_can_request_creation_without_validating_existing_tool.factory

Capture the read-only router input.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_unmatched_query_can_request_creation_without_validating_existing_tool.factory.client

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_creation_route_accepts_the_serialized_empty_argument_transport

Structured output serializes default arguments; creation must still be selected.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_creation_route_accepts_the_serialized_empty_argument_transport.factory

Mirror CrewAI returning the response model as JSON, defaults included.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_creation_route_still_rejects_execution_arguments

A creation proposal never carries execution arguments, empty transport aside.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_creation_route_still_rejects_execution_arguments.factory

Return a creation proposal that smuggles execution arguments.

Kind: callable. Declared return: Not declared / class. Source line: 74.

### test_reuse_with_incompatible_arguments_stops_before_validation

Unknown/missing/type-incompatible ports fail closed.

Kind: callable. Declared return: Not declared / class. Source line: 88.

### test_reuse_with_incompatible_arguments_stops_before_validation.factory

Return a deliberately invalid model routing proposal.

Kind: callable. Declared return: Not declared / class. Source line: 91.

### test_creation_route_does_not_invoke_manager_execution_tools

The unmatched route must reach creation without validating another catalog item.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### test_router_client_never_exposes_framework_tools

Use the session client, but pass an explicitly empty tool list.

Kind: callable. Declared return: Not declared / class. Source line: 131.

### test_real_owner_composition_enables_strict_contract_and_router

Owned coordinators are subclasses, not instances; they must enable production gates.

Kind: callable. Declared return: Not declared / class. Source line: 148.

### test_router_model_errors_do_not_reveal_response_or_credentials

Provider errors may contain request secrets and must not reach the GUI.

Kind: callable. Declared return: Not declared / class. Source line: 179.

### test_tool_routing_decides_before_any_application_suggestion

The exact-contract router is authoritative; suggestions run only on CREATE_TOOL.

Kind: callable. Declared return: Not declared / class. Source line: 194.

### test_malformed_acceptance_is_reviewable_but_routing_remains_strict

Nonfinite model proposals reach only human review, never selected execution.

Kind: callable. Declared return: Not declared / class. Source line: 240.

### test_routing_grammar_is_accepted_by_strict_external_providers

Strict providers reject empty schemas, open maps, unions and recursive refs.

Kind: callable. Declared return: Not declared / class. Source line: 256.

### test_routing_grammar_is_accepted_by_strict_external_providers.violations

Collect every construct the external structured-output subset forbids.

Kind: callable. Declared return: Not declared / class. Source line: 260.

### test_reuse_arguments_accept_scalars_and_nested_lists_only

Objects and nulls are not tool argument values; reject them before execution.

Kind: callable. Declared return: Not declared / class. Source line: 291.

### test_router_converts_argument_pairs_and_rejects_duplicate_names

The pair list becomes the reviewed keyword mapping; duplicates fail closed.

Kind: callable. Declared return: Not declared / class. Source line: 319.

### test_router_converts_argument_pairs_and_rejects_duplicate_names.factory

Return a valid pair list for the authored calculator contract.

Kind: callable. Declared return: Not declared / class. Source line: 323.

### test_router_converts_argument_pairs_and_rejects_duplicate_names.duplicate

Repeat one parameter name with conflicting values.

Kind: callable. Declared return: Not declared / class. Source line: 335.

### test_acceptance_provider_failure_still_requires_manual_valid_cases

A failed proposer may expose an empty review, never fabricated accepted evidence.

Kind: callable. Declared return: Not declared / class. Source line: 348.

### test_acceptance_provider_failure_still_requires_manual_valid_cases.factory

Fail the injected read-only provider with a secret-like body.

Kind: callable. Declared return: Not declared / class. Source line: 352.

### test_acceptance_provider_failure_still_requires_manual_valid_cases.factory.client

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 355.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | CODE | Imported dependency for CODE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ToolRouter | Imported dependency for ToolRouter in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | extract_tool_schema | Imported dependency for extract tool schema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| Catalog.contracts | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 13 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool | tmp_path | Parameter for tmp path in test_unmatched_query_can_request_creation_without_validating_existing_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool | seen | Local binding for seen in test_unmatched_query_can_request_creation_without_validating_existing_tool; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 20 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool.factory.client | role | Parameter for role in test_unmatched_query_can_request_creation_without_validating_existing_tool.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_unmatched_query_can_request_creation_without_validating_existing_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of select; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_creation_route_accepts_the_serialized_empty_argument_transport | tmp_path | Parameter for tmp path in test_creation_route_accepts_the_serialized_empty_argument_transport; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_creation_route_accepts_the_serialized_empty_argument_transport | SimpleNamespace | Imported dependency for SimpleNamespace in test_creation_route_accepts_the_serialized_empty_argument_transport; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 43 |
| test_creation_route_accepts_the_serialized_empty_argument_transport | RoutingModelClient | Imported dependency for RoutingModelClient in test_creation_route_accepts_the_serialized_empty_argument_transport; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| test_creation_route_accepts_the_serialized_empty_argument_transport | ToolRoute | Imported dependency for ToolRoute in test_creation_route_accepts_the_serialized_empty_argument_transport; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| test_creation_route_accepts_the_serialized_empty_argument_transport.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| test_creation_route_accepts_the_serialized_empty_argument_transport.factory | model | Local binding for model in test_creation_route_accepts_the_serialized_empty_argument_transport.factory; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_creation_route_accepts_the_serialized_empty_argument_transport | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of select; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_creation_route_still_rejects_execution_arguments | tmp_path | Parameter for tmp path in test_creation_route_still_rejects_execution_arguments; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_creation_route_still_rejects_execution_arguments | arguments | Parameter for arguments in test_creation_route_still_rejects_execution_arguments; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_creation_route_still_rejects_execution_arguments.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| test_creation_route_still_rejects_execution_arguments.factory.lambda_76 | role | Callback parameter for role in test_creation_route_still_rejects_execution_arguments.factory.lambda_76; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 76 |
| test_creation_route_still_rejects_execution_arguments.factory.lambda_76 | content | Artifact or review text whose encoding, size and approval state must be checked. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 76 |
| test_reuse_with_incompatible_arguments_stops_before_validation | tmp_path | Parameter for tmp path in test_reuse_with_incompatible_arguments_stops_before_validation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| test_reuse_with_incompatible_arguments_stops_before_validation | arguments | Parameter for arguments in test_reuse_with_incompatible_arguments_stops_before_validation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| test_reuse_with_incompatible_arguments_stops_before_validation.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_reuse_with_incompatible_arguments_stops_before_validation.factory.lambda_93 | role | Callback parameter for role in test_reuse_with_incompatible_arguments_stops_before_validation.factory.lambda_93; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 93 |
| test_reuse_with_incompatible_arguments_stops_before_validation.factory.lambda_93 | content | Artifact or review text whose encoding, size and approval state must be checked. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 93 |
| test_creation_route_does_not_invoke_manager_execution_tools | SimpleNamespace | Imported dependency for SimpleNamespace in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 106 |
| test_creation_route_does_not_invoke_manager_execution_tools | Mock | Imported dependency for Mock in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 107 |
| test_creation_route_does_not_invoke_manager_execution_tools | Orchestrator | Imported dependency for Orchestrator in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 109 |
| test_creation_route_does_not_invoke_manager_execution_tools | service | Local binding for service in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_creation_route_does_not_invoke_manager_execution_tools | service.get_installed_tools_catalog | Attribute for service.get installed tools catalog in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_creation_route_does_not_invoke_manager_execution_tools | service.applications | Attribute for service.applications in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 113 |
| test_creation_route_does_not_invoke_manager_execution_tools | service.router | Attribute for service.router in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_creation_route_does_not_invoke_manager_execution_tools.lambda_115 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 115 |
| test_creation_route_does_not_invoke_manager_execution_tools | service.verification | Attribute for service.verification in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_creation_route_does_not_invoke_manager_execution_tools | service.build_tool_pipeline | Attribute for service.build tool pipeline in test_creation_route_does_not_invoke_manager_execution_tools; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_router_client_never_exposes_framework_tools | SimpleNamespace | Imported dependency for SimpleNamespace in test_router_client_never_exposes_framework_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 133 |
| test_router_client_never_exposes_framework_tools | Mock | Imported dependency for Mock in test_router_client_never_exposes_framework_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 134 |
| test_router_client_never_exposes_framework_tools | RoutingModelClient | Imported dependency for RoutingModelClient in test_router_client_never_exposes_framework_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 136 |
| test_router_client_never_exposes_framework_tools | call | Local binding for call in test_router_client_never_exposes_framework_tools; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_real_owner_composition_enables_strict_contract_and_router | tmp_path | Parameter for tmp path in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 148 |
| test_real_owner_composition_enables_strict_contract_and_router | monkeypatch | Parameter for monkeypatch in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 148 |
| test_real_owner_composition_enables_strict_contract_and_router | SimpleNamespace | Imported dependency for SimpleNamespace in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 150 |
| test_real_owner_composition_enables_strict_contract_and_router | create_runtime | Imported dependency for create runtime in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 152 |
| test_real_owner_composition_enables_strict_contract_and_router | SecurityManager | Imported dependency for SecurityManager in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 153 |
| test_real_owner_composition_enables_strict_contract_and_router | Settings | Imported dependency for Settings in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 154 |
| test_real_owner_composition_enables_strict_contract_and_router | agents | Local binding for agents in test_real_owner_composition_enables_strict_contract_and_router; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_real_owner_composition_enables_strict_contract_and_router | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_real_owner_composition_enables_strict_contract_and_router | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_real_owner_composition_enables_strict_contract_and_router.lambda_171 | operations | Callback parameter for operations in test_real_owner_composition_enables_strict_contract_and_router.lambda_171; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 171 |
| test_real_owner_composition_enables_strict_contract_and_router.lambda_172 | model | Callback parameter for model in test_real_owner_composition_enables_strict_contract_and_router.lambda_172; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 172 |
| test_real_owner_composition_enables_strict_contract_and_router.lambda_172 | tools | Callback parameter for tools in test_real_owner_composition_enables_strict_contract_and_router.lambda_172; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 172 |
| test_router_model_errors_do_not_reveal_response_or_credentials | SimpleNamespace | Imported dependency for SimpleNamespace in test_router_model_errors_do_not_reveal_response_or_credentials; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 181 |
| test_router_model_errors_do_not_reveal_response_or_credentials | Mock | Imported dependency for Mock in test_router_model_errors_do_not_reveal_response_or_credentials; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 182 |
| test_router_model_errors_do_not_reveal_response_or_credentials | RoutingModelClient | Imported dependency for RoutingModelClient in test_router_model_errors_do_not_reveal_response_or_credentials; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 184 |
| test_router_model_errors_do_not_reveal_response_or_credentials | client | Local binding for client in test_router_model_errors_do_not_reveal_response_or_credentials; use the enclosing contract and type below. | Return type of RoutingModelClient; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| test_router_model_errors_do_not_reveal_response_or_credentials | error | Managed resource for error in test_router_model_errors_do_not_reveal_response_or_credentials; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 189 |
| test_tool_routing_decides_before_any_application_suggestion | SimpleNamespace | Imported dependency for SimpleNamespace in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 196 |
| test_tool_routing_decides_before_any_application_suggestion | Mock | Imported dependency for Mock in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 197 |
| test_tool_routing_decides_before_any_application_suggestion | Orchestrator | Imported dependency for Orchestrator in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 199 |
| test_tool_routing_decides_before_any_application_suggestion | order | Local binding for order in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 201 |
| test_tool_routing_decides_before_any_application_suggestion | agent | Local binding for agent in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_tool_routing_decides_before_any_application_suggestion | agents | Local binding for agents in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_tool_routing_decides_before_any_application_suggestion | router | Local binding for router in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_tool_routing_decides_before_any_application_suggestion.lambda_208 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 208 |
| test_tool_routing_decides_before_any_application_suggestion | applications | Local binding for applications in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 214 |
| test_tool_routing_decides_before_any_application_suggestion | orchestrator | Local binding for orchestrator in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_tool_routing_decides_before_any_application_suggestion | orchestrator._reuse_selected | Attribute for orchestrator. reuse selected in test_tool_routing_decides_before_any_application_suggestion; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | tmp_path | Parameter for tmp path in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 240 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | SimpleNamespace | Imported dependency for SimpleNamespace in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 242 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | Mock | Imported dependency for Mock in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 243 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | RoutingModelClient | Imported dependency for RoutingModelClient in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 245 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | raw | Local binding for raw in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 247 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | client | Local binding for client in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Return type of RoutingModelClient; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict | router | Local binding for router in test_malformed_acceptance_is_reviewable_but_routing_remains_strict; use the enclosing contract and type below. | Return type of ToolRouter; see its callable contract | Enclosing invocation or class/instance lifetime | 252 |
| test_malformed_acceptance_is_reviewable_but_routing_remains_strict.lambda_252 | path | Path under validation or an explicitly scoped maintained source path. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 252 |
| test_routing_grammar_is_accepted_by_strict_external_providers | ToolRoute | Imported dependency for ToolRoute in test_routing_grammar_is_accepted_by_strict_external_providers; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 258 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | node | Parameter for node in test_routing_grammar_is_accepted_by_strict_external_providers.violations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 260 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 260 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | found | Local binding for found in test_routing_grammar_is_accepted_by_strict_external_providers.violations; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 262 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | key | Loop item for key in test_routing_grammar_is_accepted_by_strict_external_providers.violations; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 274 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 274, 277 |
| test_routing_grammar_is_accepted_by_strict_external_providers.violations | index | Loop item for index in test_routing_grammar_is_accepted_by_strict_external_providers.violations; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 277 |
| test_routing_grammar_is_accepted_by_strict_external_providers | schema | Local binding for schema in test_routing_grammar_is_accepted_by_strict_external_providers; use the enclosing contract and type below. | Return type of model_json_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 281 |
| test_routing_grammar_is_accepted_by_strict_external_providers | arguments | Local binding for arguments in test_routing_grammar_is_accepted_by_strict_external_providers; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_routing_grammar_is_accepted_by_strict_external_providers | pair | Local binding for pair in test_routing_grammar_is_accepted_by_strict_external_providers; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 286 |
| test_reuse_arguments_accept_scalars_and_nested_lists_only | ValidationError | Imported dependency for ValidationError in test_reuse_arguments_accept_scalars_and_nested_lists_only; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 293 |
| test_reuse_arguments_accept_scalars_and_nested_lists_only | ReuseRoute | Imported dependency for ReuseRoute in test_reuse_arguments_accept_scalars_and_nested_lists_only; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 295 |
| test_reuse_arguments_accept_scalars_and_nested_lists_only | route | Local binding for route in test_reuse_arguments_accept_scalars_and_nested_lists_only; use the enclosing contract and type below. | Return type of ReuseRoute; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| test_reuse_arguments_accept_scalars_and_nested_lists_only | invalid | Loop item for invalid in test_reuse_arguments_accept_scalars_and_nested_lists_only; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 309 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names | tmp_path | Parameter for tmp path in test_router_converts_argument_pairs_and_rejects_duplicate_names; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 319 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names | ToolRouter | Imported dependency for ToolRouter in test_router_converts_argument_pairs_and_rejects_duplicate_names; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 321 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 323 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.factory.lambda_325 | role | Callback parameter for role in test_router_converts_argument_pairs_and_rejects_duplicate_names.factory.lambda_325; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 325 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.factory.lambda_325 | content | Artifact or review text whose encoding, size and approval state must be checked. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 325 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names | route | Local binding for route in test_router_converts_argument_pairs_and_rejects_duplicate_names; use the enclosing contract and type below. | Return type of select; see its callable contract | Enclosing invocation or class/instance lifetime | 332 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.duplicate | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 335 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.duplicate.lambda_337 | role | Callback parameter for role in test_router_converts_argument_pairs_and_rejects_duplicate_names.duplicate.lambda_337; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 337 |
| test_router_converts_argument_pairs_and_rejects_duplicate_names.duplicate.lambda_337 | content | Artifact or review text whose encoding, size and approval state must be checked. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 337 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases | tmp_path | Parameter for tmp path in test_acceptance_provider_failure_still_requires_manual_valid_cases; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases | seen | Local binding for seen in test_acceptance_provider_failure_still_requires_manual_valid_cases; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 350 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases.factory | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 352 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases.factory.client | role | Parameter for role in test_acceptance_provider_failure_still_requires_manual_valid_cases.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 355 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 355 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of acceptance; see its callable contract | Enclosing invocation or class/instance lifetime | 361 |
| test_acceptance_provider_failure_still_requires_manual_valid_cases | parse_contract | Imported dependency for parse contract in test_acceptance_provider_failure_still_requires_manual_valid_cases; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 367 |
