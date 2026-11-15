# Reference for tests/test_application_routing.py

Application suggestions are bounded recommendations, never execution grants.

Source fingerprint: f1f9af78bf3a2a67ae55ff082152988ed4a48bd6757f7d2c5fcacd809efdac15

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_application_selector_has_no_tools_and_keeps_budgets

Prevent SDK tool-call bias from bypassing the catalog-only decision.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments

Malformed or ambiguous decisions fail closed instead of becoming a suggestion.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match

A recommendation names one current catalog row and carries no arguments.

Kind: callable. Declared return: Not declared / class. Source line: 52.

### test_single_matching_application_is_only_recommended

A complete match yields a safe message; no execution path is reachable.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_invalid_or_ambiguous_suggestion_keeps_the_creation_route

A rejected suggestion never blocks creation and never executes an application.

Kind: callable. Declared return: Not declared / class. Source line: 100.

### test_explicit_no_match_keeps_the_creation_route

Only an explicit no-match continues to the existing new-tool flow.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_no_installed_application_skips_the_suggestion_model_call

An empty catalog must not spend a model turn on application classification.

Kind: callable. Declared return: Not declared / class. Source line: 142.

### test_suggestion_prompt_carries_only_identity_name_and_description

Node IDs, parameter names and arguments must never reach the suggestion prompt.

Kind: callable. Declared return: Not declared / class. Source line: 160.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | APP | Module binding for APP in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 10 |
| module | OTHER | Module binding for OTHER in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 11 |
| module | CANDIDATES | Module binding for CANDIDATES in module; use the enclosing contract and type below. | list | Module/process lifetime | 12 |
| module | MESSAGE | Module binding for MESSAGE in module; use the enclosing contract and type below. | str | Module/process lifetime | 13 |
| test_application_selector_has_no_tools_and_keeps_budgets | system | Parameter for system in test_application_selector_has_no_tools_and_keeps_budgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 19 |
| test_application_selector_has_no_tools_and_keeps_budgets | selector | Local binding for selector in test_application_selector_has_no_tools_and_keeps_budgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments | raw | Parameter for raw in test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments | parse_application_suggestion | Imported dependency for parse application suggestion in test_suggestion_rejects_prose_extra_fields_duplicates_unknown_ids_and_arguments; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match | parse_application_suggestion | Imported dependency for parse application suggestion in test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match | suggestion | Local binding for suggestion in test_suggestion_accepts_only_one_catalog_id_or_explicit_no_match; use the enclosing contract and type below. | Return type of parse_application_suggestion; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_single_matching_application_is_only_recommended | system | Parameter for system in test_single_matching_application_is_only_recommended; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_single_matching_application_is_only_recommended | caplog | Parameter for caplog in test_single_matching_application_is_only_recommended; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_single_matching_application_is_only_recommended | system.main.applications | Attribute for system.main.applications in test_single_matching_application_is_only_recommended; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_single_matching_application_is_only_recommended | system.main.Crew | Attribute for system.main.Crew in test_single_matching_application_is_only_recommended; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_single_matching_application_is_only_recommended | system.main.build_tool_pipeline | Attribute for system.main.build tool pipeline in test_single_matching_application_is_only_recommended; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_single_matching_application_is_only_recommended | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_invalid_or_ambiguous_suggestion_keeps_the_creation_route | system | Parameter for system in test_invalid_or_ambiguous_suggestion_keeps_the_creation_route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_invalid_or_ambiguous_suggestion_keeps_the_creation_route | raw | Parameter for raw in test_invalid_or_ambiguous_suggestion_keeps_the_creation_route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 100 |
| test_invalid_or_ambiguous_suggestion_keeps_the_creation_route | system.main.applications | Attribute for system.main.applications in test_invalid_or_ambiguous_suggestion_keeps_the_creation_route; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_invalid_or_ambiguous_suggestion_keeps_the_creation_route | system.main.Crew | Attribute for system.main.Crew in test_invalid_or_ambiguous_suggestion_keeps_the_creation_route; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_invalid_or_ambiguous_suggestion_keeps_the_creation_route | system.main.build_tool_pipeline | Attribute for system.main.build tool pipeline in test_invalid_or_ambiguous_suggestion_keeps_the_creation_route; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_explicit_no_match_keeps_the_creation_route | system | Parameter for system in test_explicit_no_match_keeps_the_creation_route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| test_explicit_no_match_keeps_the_creation_route | system.main.applications | Attribute for system.main.applications in test_explicit_no_match_keeps_the_creation_route; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_explicit_no_match_keeps_the_creation_route | system.main.Crew | Attribute for system.main.Crew in test_explicit_no_match_keeps_the_creation_route; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_explicit_no_match_keeps_the_creation_route | system.main.build_tool_pipeline | Attribute for system.main.build tool pipeline in test_explicit_no_match_keeps_the_creation_route; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_no_installed_application_skips_the_suggestion_model_call | system | Parameter for system in test_no_installed_application_skips_the_suggestion_model_call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 142 |
| test_no_installed_application_skips_the_suggestion_model_call | system.main.applications | Attribute for system.main.applications in test_no_installed_application_skips_the_suggestion_model_call; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_no_installed_application_skips_the_suggestion_model_call | system.main.Crew | Attribute for system.main.Crew in test_no_installed_application_skips_the_suggestion_model_call; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_no_installed_application_skips_the_suggestion_model_call | system.main.build_tool_pipeline | Attribute for system.main.build tool pipeline in test_no_installed_application_skips_the_suggestion_model_call; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_suggestion_prompt_carries_only_identity_name_and_description | system | Parameter for system in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_suggestion_prompt_carries_only_identity_name_and_description | system.main.applications | Attribute for system.main.applications in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_suggestion_prompt_carries_only_identity_name_and_description | system.main.Crew | Attribute for system.main.Crew in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| test_suggestion_prompt_carries_only_identity_name_and_description | system.main.build_tool_pipeline | Attribute for system.main.build tool pipeline in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_suggestion_prompt_carries_only_identity_name_and_description | description | Local binding for description in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_suggestion_prompt_carries_only_identity_name_and_description | forbidden | Loop item for forbidden in test_suggestion_prompt_carries_only_identity_name_and_description; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 179 |
