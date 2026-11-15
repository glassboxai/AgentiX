# Reference for tests/test_code_application.py

V5-043: generated connection code persists without a graph or host imports.

Source fingerprint: 0e0d927bd7cc25a4b138008915d4b365046eed1e194dc6aa9bbb92373f643ffc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### proposal

Provide independently authored code and presentation metadata, without edges.

Kind: callable. Declared return: dict. Source line: 21.

### test_proposal_checks_source_without_importing_it

Host inspection must not run module-level generated code.

Kind: callable. Declared return: None. Source line: 31.

### test_public_input_schema_rejects_numeric_bounds_with_a_named_key

V7-059: a model-supplied bound is rejected by name, never silently accepted.

Kind: callable. Declared return: None. Source line: 49.

### test_public_input_schema_names_every_unsupported_key

The bounded message lists all offending keys of one input in sorted order.

Kind: callable. Declared return: None. Source line: 61.

### test_contract_error_never_carries_the_rejected_value

A closed diagnostic must not leak model or user payload into UI or logs.

Kind: callable. Declared return: None. Source line: 79.

### test_supported_input_shapes_still_validate

The closed key list keeps accepting the four documented keys and arrays.

Kind: callable. Declared return: None. Source line: 92.

### test_new_package_has_no_graph_and_requires_independent_cases

Creation succeeds before acceptance; approval cannot accept missing host cases.

Kind: callable. Declared return: None. Source line: 109.

### test_new_package_has_no_graph_and_requires_independent_cases.Coordinator

Return inert authored artifacts across the production coordinator boundary.

Kind: class. Declared return: Not declared / class. Source line: 116.

### test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.plan

Return generated connection code.

Kind: callable. Declared return: Not declared / class. Source line: 119.

### test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets

Return a reusable widget contract.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### test_invalid_code_contract_is_rejected

Reject unknown dependencies, duplicate widget IDs and forbidden imports.

Kind: callable. Declared return: None. Source line: 160.

### make_code_candidate

Create a trusted temporary package and independently supply expected values.

Kind: callable. Declared return: Not declared / class. Source line: 170.

### test_manifest_tampering_and_strict_public_contracts

Reject altered maintained runtime bytes, coercion and changed call output types.

Kind: callable. Declared return: None. Source line: 198.

### test_native_connection_code_runs_without_agents_or_graph

Real AppContainer executes dependent calls from persisted Python only.

Kind: callable. Declared return: None. Source line: 222.

### test_native_missing_or_repeated_calls_fail

Incomplete/repeated execution cannot publish partial results or run on host.

Kind: callable. Declared return: None. Source line: 241.

### test_native_browser_for_code_package

Real isolated widgets show results and arguments from generated code on repeat runs.

Kind: callable. Declared return: None. Source line: 267.

### test_real_gradio_code_compositor_with_trusted_fixtures

Only authored fixtures run in memory; production generated imports stay native.

Kind: callable. Declared return: None. Source line: 285.

### test_trusted_code_runtime_rejects_partial_calls

Authored fixture calls exercise failure contracts independently of OS readiness.

Kind: callable. Declared return: None. Source line: 348.

### test_v6_044_code_widgets_have_editable_persistable_geometry

V6-044: named widget controls move/resize while toolbar IDs stay forbidden.

Kind: callable. Declared return: None. Source line: 369.

### test_v7_062_layout_hidden_visibility_contract

V7-062: hidden controls share the movable allowlist and stay optional.

Kind: callable. Declared return: None. Source line: 401.

### test_v7_063_layout_groups_bind_widget_controls_to_their_tool

V7-063: handles of one tool share a group; public inputs and Status stay separate.

Kind: callable. Declared return: None. Source line: 432.

### test_v7_062_editor_hides_unchecked_controls_after_edit

Unchecking a control in Edit hides it outside Edit and survives a reload.

Kind: callable. Declared return: None. Source line: 459.

### test_v7_062_editor_hides_unchecked_controls_after_edit.route

Return inert HTML or validate the editor's data-only layout request.

Kind: callable. Declared return: None. Source line: 491.

### test_v7_063_editor_colors_only_the_move_handle_per_tool

Same tool shares one handle color; leaving Edit restores the base color.

Kind: callable. Declared return: None. Source line: 550.

### test_v7_063_editor_colors_only_the_move_handle_per_tool.route

Serve inert HTML and a fixed authorized layout payload.

Kind: callable. Declared return: None. Source line: 586.

### test_v7_063_editor_colors_only_the_move_handle_per_tool.color

Read the computed handle background, not the widget surface.

Kind: callable. Declared return: str. Source line: 602.

### test_v6_044_editor_moves_resizes_and_restores_code_widget_controls

Exercise the real editor with inert DOM controls and an isolated layout route.

Kind: callable. Declared return: None. Source line: 642.

### test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route

Return inert HTML or validate the editor's data-only layout request.

Kind: callable. Declared return: None. Source line: 668.

### test_v7_066_widget_source_name_accepts_only_a_tool_identifier

A double-clicked widget resolves to <tool>_widget.py and nothing else.

Kind: callable. Declared return: None. Source line: 740.

### test_v7_066_editor_posts_the_double_clicked_widget_tool

Only a widget control of one tool reports its tool name to the parent page.

Kind: callable. Declared return: None. Source line: 751.

### test_v7_066_editor_posts_the_double_clicked_widget_tool.route

Serve inert HTML and the authorized layout payload.

Kind: callable. Declared return: None. Source line: 780.

### test_v7_066_parent_selects_the_widget_file_from_a_frame_message

Only the framed application's valid tool name reaches the hidden selector.

Kind: callable. Declared return: None. Source line: 825.

### test_v7_066_parent_selects_the_widget_file_from_a_frame_message.route

Serve the parent page and one inert framed child.

Kind: callable. Declared return: None. Source line: 844.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | approved_tool | Imported dependency for approved tool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | LOGIC | Module binding for LOGIC in module; use the enclosing contract and type below. | Return type of join; see its callable contract | Module/process lifetime | 9 |
| test_proposal_checks_source_without_importing_it | tmp_path | Parameter for tmp path in test_proposal_checks_source_without_importing_it; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 31 |
| test_proposal_checks_source_without_importing_it | ApplicationCode | Imported dependency for ApplicationCode in test_proposal_checks_source_without_importing_it; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| test_proposal_checks_source_without_importing_it | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_public_input_schema_rejects_numeric_bounds_with_a_named_key | ApplicationCode | Imported dependency for ApplicationCode in test_public_input_schema_rejects_numeric_bounds_with_a_named_key; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 51 |
| test_public_input_schema_rejects_numeric_bounds_with_a_named_key | ApplicationContractError | Imported dependency for ApplicationContractError in test_public_input_schema_rejects_numeric_bounds_with_a_named_key; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 51 |
| test_public_input_schema_rejects_numeric_bounds_with_a_named_key | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_public_input_schema_names_every_unsupported_key | ApplicationCode | Imported dependency for ApplicationCode in test_public_input_schema_names_every_unsupported_key; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 63 |
| test_public_input_schema_names_every_unsupported_key | ApplicationContractError | Imported dependency for ApplicationContractError in test_public_input_schema_names_every_unsupported_key; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 63 |
| test_public_input_schema_names_every_unsupported_key | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_public_input_schema_names_every_unsupported_key | caught | Managed resource for caught in test_public_input_schema_names_every_unsupported_key; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 69 |
| test_public_input_schema_names_every_unsupported_key | message | Local binding for message in test_public_input_schema_names_every_unsupported_key; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_contract_error_never_carries_the_rejected_value | ApplicationCode | Imported dependency for ApplicationCode in test_contract_error_never_carries_the_rejected_value; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 81 |
| test_contract_error_never_carries_the_rejected_value | ApplicationContractError | Imported dependency for ApplicationContractError in test_contract_error_never_carries_the_rejected_value; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 81 |
| test_contract_error_never_carries_the_rejected_value | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_contract_error_never_carries_the_rejected_value | caught | Managed resource for caught in test_contract_error_never_carries_the_rejected_value; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 85 |
| test_supported_input_shapes_still_validate | ApplicationCode | Imported dependency for ApplicationCode in test_supported_input_shapes_still_validate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_supported_input_shapes_still_validate | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_new_package_has_no_graph_and_requires_independent_cases | tmp_path | Parameter for tmp path in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 109 |
| test_new_package_has_no_graph_and_requires_independent_cases | WIDGET | Imported dependency for WIDGET in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 111 |
| test_new_package_has_no_graph_and_requires_independent_cases | ApplicationReview | Imported dependency for ApplicationReview in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 113 |
| test_new_package_has_no_graph_and_requires_independent_cases | ApplicationPipeline | Imported dependency for ApplicationPipeline in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 114 |
| test_new_package_has_no_graph_and_requires_independent_cases | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 114 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 119 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.plan | args | Parameter for args in test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.plan; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 119 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets | tools | Parameter for tools in test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets | feedback | Parameter for feedback in test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_new_package_has_no_graph_and_requires_independent_cases.Coordinator.widgets.comprehension_125 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 127 |
| test_new_package_has_no_graph_and_requires_independent_cases | item | Local binding for item in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_new_package_has_no_graph_and_requires_independent_cases.lambda_130 | _ | Callback parameter for  in test_new_package_has_no_graph_and_requires_independent_cases.lambda_130; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 130 |
| test_new_package_has_no_graph_and_requires_independent_cases | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_new_package_has_no_graph_and_requires_independent_cases | supervisor | Local binding for supervisor in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_new_package_has_no_graph_and_requires_independent_cases | review | Local binding for review in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | Return type of ApplicationReview; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_new_package_has_no_graph_and_requires_independent_cases | cases | Local binding for cases in test_new_package_has_no_graph_and_requires_independent_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 144 |
| test_invalid_code_contract_is_rejected | change | Parameter for change in test_invalid_code_contract_is_rejected; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 160 |
| test_invalid_code_contract_is_rejected | ApplicationCode | Imported dependency for ApplicationCode in test_invalid_code_contract_is_rejected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 162 |
| make_code_candidate | tmp_path | Parameter for tmp path in make_code_candidate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 170 |
| make_code_candidate | logic | Parameter for logic in make_code_candidate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 170 |
| make_code_candidate | SimpleNamespace | Imported dependency for SimpleNamespace in make_code_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 172 |
| make_code_candidate | WIDGET | Imported dependency for WIDGET in make_code_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 174 |
| make_code_candidate | ApplicationReview | Imported dependency for ApplicationReview in make_code_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 176 |
| make_code_candidate | ApplicationPipeline | Imported dependency for ApplicationPipeline in make_code_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 177 |
| make_code_candidate | coordinator | Local binding for coordinator in make_code_candidate; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| make_code_candidate.lambda_181 | tools | Callback parameter for tools in make_code_candidate.lambda_181; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 181 |
| make_code_candidate.lambda_181 | feedback | Callback parameter for feedback in make_code_candidate.lambda_181; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 181 |
| make_code_candidate.lambda_181.comprehension_181 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 183 |
| make_code_candidate | item | Local binding for item in make_code_candidate; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| make_code_candidate.lambda_186 | _ | Callback parameter for  in make_code_candidate.lambda_186; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 186 |
| test_manifest_tampering_and_strict_public_contracts | tmp_path | Parameter for tmp path in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 198 |
| test_manifest_tampering_and_strict_public_contracts | hashlib | Imported dependency for hashlib in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 200 |
| test_manifest_tampering_and_strict_public_contracts | validate_payload | Imported dependency for validate payload in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| test_manifest_tampering_and_strict_public_contracts | validate_results | Imported dependency for validate results in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| test_manifest_tampering_and_strict_public_contracts | application_digest | Imported dependency for application digest in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 203 |
| test_manifest_tampering_and_strict_public_contracts | item | Local binding for item in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_manifest_tampering_and_strict_public_contracts | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_manifest_tampering_and_strict_public_contracts | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_manifest_tampering_and_strict_public_contracts | bad | Loop item for bad in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 208 |
| test_manifest_tampering_and_strict_public_contracts | member | Local binding for member in test_manifest_tampering_and_strict_public_contracts; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 213 |
| test_native_connection_code_runs_without_agents_or_graph | tmp_path | Parameter for tmp path in test_native_connection_code_runs_without_agents_or_graph; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 222 |
| test_native_connection_code_runs_without_agents_or_graph | approve_application | Imported dependency for approve application in test_native_connection_code_runs_without_agents_or_graph; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 224 |
| test_native_connection_code_runs_without_agents_or_graph | execute_application | Imported dependency for execute application in test_native_connection_code_runs_without_agents_or_graph; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 225 |
| test_native_connection_code_runs_without_agents_or_graph | item | Local binding for item in test_native_connection_code_runs_without_agents_or_graph; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_native_connection_code_runs_without_agents_or_graph | approved | Local binding for approved in test_native_connection_code_runs_without_agents_or_graph; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| test_native_missing_or_repeated_calls_fail | tmp_path | Parameter for tmp path in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 241 |
| test_native_missing_or_repeated_calls_fail | logic | Parameter for logic in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 241 |
| test_native_missing_or_repeated_calls_fail | approve_application | Imported dependency for approve application in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 243 |
| test_native_missing_or_repeated_calls_fail | ApplicationSession | Imported dependency for ApplicationSession in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 244 |
| test_native_missing_or_repeated_calls_fail | item | Local binding for item in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_native_missing_or_repeated_calls_fail | session | Local binding for session in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| test_native_missing_or_repeated_calls_fail | observation | Local binding for observation in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 253 |
| test_native_missing_or_repeated_calls_fail | detail | Local binding for detail in test_native_missing_or_repeated_calls_fail; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| test_native_browser_for_code_package | tmp_path | Parameter for tmp path in test_native_browser_for_code_package; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 267 |
| test_native_browser_for_code_package | browser_verify | Imported dependency for browser verify in test_native_browser_for_code_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 269 |
| test_native_browser_for_code_package | approve_application | Imported dependency for approve application in test_native_browser_for_code_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 270 |
| test_native_browser_for_code_package | ApplicationPreview | Imported dependency for ApplicationPreview in test_native_browser_for_code_package; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 271 |
| test_native_browser_for_code_package | item | Local binding for item in test_native_browser_for_code_package; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_native_browser_for_code_package | preview | Local binding for preview in test_native_browser_for_code_package; use the enclosing contract and type below. | Return type of ApplicationPreview; see its callable contract | Enclosing invocation or class/instance lifetime | 274 |
| test_native_browser_for_code_package | report | Local binding for report in test_native_browser_for_code_package; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 277 |
| test_real_gradio_code_compositor_with_trusted_fixtures | tmp_path | Parameter for tmp path in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 286 |
| test_real_gradio_code_compositor_with_trusted_fixtures | monkeypatch | Parameter for monkeypatch in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 286 |
| test_real_gradio_code_compositor_with_trusted_fixtures | importlib | Imported dependency for importlib in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 289 |
| test_real_gradio_code_compositor_with_trusted_fixtures | sys | Imported dependency for sys in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 290 |
| test_real_gradio_code_compositor_with_trusted_fixtures | runtime_template | Imported dependency for runtime template in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 292 |
| test_real_gradio_code_compositor_with_trusted_fixtures | item | Local binding for item in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| test_real_gradio_code_compositor_with_trusted_fixtures | names | Local binding for names in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 295 |
| test_real_gradio_code_compositor_with_trusted_fixtures | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 305, 333 |
| test_real_gradio_code_compositor_with_trusted_fixtures | spec | Local binding for spec in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_code_compositor_with_trusted_fixtures | module | Local binding for module in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 310 |
| test_real_gradio_code_compositor_with_trusted_fixtures | demo | Local binding for demo in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of create_application; see its callable contract | Enclosing invocation or class/instance lifetime | 312 |
| test_real_gradio_code_compositor_with_trusted_fixtures | callback | Local binding for callback in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 314 |
| test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_314 | event | Comprehension item for event in test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_314; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 314 |
| test_real_gradio_code_compositor_with_trusted_fixtures | canvas | Local binding for canvas in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 316 |
| test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_316 | block | Comprehension item for block in test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_316; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 318 |
| test_real_gradio_code_compositor_with_trusted_fixtures | descendants | Local binding for descendants in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 321 |
| test_real_gradio_code_compositor_with_trusted_fixtures | child | Loop item for child in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 322 |
| test_real_gradio_code_compositor_with_trusted_fixtures | output | Local binding for output in test_real_gradio_code_compositor_with_trusted_fixtures; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 326 |
| test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_329 | component | Comprehension item for component in test_real_gradio_code_compositor_with_trusted_fixtures.comprehension_329; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 329 |
| test_trusted_code_runtime_rejects_partial_calls | tmp_path | Parameter for tmp path in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 349 |
| test_trusted_code_runtime_rejects_partial_calls | monkeypatch | Parameter for monkeypatch in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 349 |
| test_trusted_code_runtime_rejects_partial_calls | logic | Parameter for logic in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 349 |
| test_trusted_code_runtime_rejects_partial_calls | message | Parameter for message in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 349 |
| test_trusted_code_runtime_rejects_partial_calls | importlib | Imported dependency for importlib in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 352 |
| test_trusted_code_runtime_rejects_partial_calls | sys | Imported dependency for sys in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 353 |
| test_trusted_code_runtime_rejects_partial_calls | item | Local binding for item in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 355 |
| test_trusted_code_runtime_rejects_partial_calls | names | Local binding for names in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 356 |
| test_trusted_code_runtime_rejects_partial_calls | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 358, 365 |
| test_trusted_code_runtime_rejects_partial_calls | operation | Local binding for operation in test_trusted_code_runtime_rejects_partial_calls; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 361 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | application_layout_ids | Imported dependency for application layout ids in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 371 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | validate_layout | Imported dependency for validate layout in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 371 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 373 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | allowed | Local binding for allowed in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 379 |
| test_v6_044_code_widgets_have_editable_persistable_geometry.comprehension_380 | instance | Comprehension item for instance in test_v6_044_code_widgets_have_editable_persistable_geometry.comprehension_380; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 382 |
| test_v6_044_code_widgets_have_editable_persistable_geometry.comprehension_380 | role | Comprehension item for role in test_v6_044_code_widgets_have_editable_persistable_geometry.comprehension_380; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 383 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | positions | Local binding for positions in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 385 |
| test_v6_044_code_widgets_have_editable_persistable_geometry.comprehension_385 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 385 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | layout | Local binding for layout in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 386 |
| test_v6_044_code_widgets_have_editable_persistable_geometry | forbidden | Loop item for forbidden in test_v6_044_code_widgets_have_editable_persistable_geometry; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 388 |
| test_v7_062_layout_hidden_visibility_contract | application_layout_ids | Imported dependency for application layout ids in test_v7_062_layout_hidden_visibility_contract; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 403 |
| test_v7_062_layout_hidden_visibility_contract | validate_layout | Imported dependency for validate layout in test_v7_062_layout_hidden_visibility_contract; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 403 |
| test_v7_062_layout_hidden_visibility_contract | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 405 |
| test_v7_062_layout_hidden_visibility_contract | allowed | Local binding for allowed in test_v7_062_layout_hidden_visibility_contract; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 411 |
| test_v7_062_layout_hidden_visibility_contract | layout | Local binding for layout in test_v7_062_layout_hidden_visibility_contract; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 412 |
| test_v7_062_layout_hidden_visibility_contract | forbidden | Loop item for forbidden in test_v7_062_layout_hidden_visibility_contract; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 422 |
| test_v7_063_layout_groups_bind_widget_controls_to_their_tool | application_layout_groups | Imported dependency for application layout groups in test_v7_063_layout_groups_bind_widget_controls_to_their_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 434 |
| test_v7_063_layout_groups_bind_widget_controls_to_their_tool | application_layout_ids | Imported dependency for application layout ids in test_v7_063_layout_groups_bind_widget_controls_to_their_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 434 |
| test_v7_063_layout_groups_bind_widget_controls_to_their_tool | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 436 |
| test_v7_063_layout_groups_bind_widget_controls_to_their_tool | groups | Local binding for groups in test_v7_063_layout_groups_bind_widget_controls_to_their_tool; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 449 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | os | Imported dependency for os in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 461 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | expect | Imported dependency for expect in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 463 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | sync_playwright | Imported dependency for sync playwright in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 463 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | application_layout_ids | Imported dependency for application layout ids in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 465 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | validate_layout | Imported dependency for validate layout in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 465 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 467 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | allowed | Local binding for allowed in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 473 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | dict | Enclosing invocation or class/instance lifetime | 474 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.comprehension_476 | index | Comprehension item for index in test_v7_062_editor_hides_unchecked_controls_after_edit.comprehension_476; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 478 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.comprehension_476 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 478 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | saves | Local binding for saves in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 481 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | html | Local binding for html in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 482 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.comprehension_484 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 486 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.route | request_route | Parameter for request route in test_v7_062_editor_hides_unchecked_controls_after_edit.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 491 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.route | request | Local binding for request in test_v7_062_editor_hides_unchecked_controls_after_edit.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 494 |
| test_v7_062_editor_hides_unchecked_controls_after_edit.route | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of validate_layout; see its callable contract | Enclosing invocation or class/instance lifetime | 497 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | driver | Managed resource for driver in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 512 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | browser | Local binding for browser in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 513 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | page | Local binding for page in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 517 |
| test_v7_062_editor_hides_unchecked_controls_after_edit | toggle | Local binding for toggle in test_v7_062_editor_hides_unchecked_controls_after_edit; use the enclosing contract and type below. | Return type of get_by_label; see its callable contract | Enclosing invocation or class/instance lifetime | 527 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | os | Imported dependency for os in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 552 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | expect | Imported dependency for expect in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 554 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | sync_playwright | Imported dependency for sync playwright in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 554 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | application_layout_groups | Imported dependency for application layout groups in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 556 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | application_layout_ids | Imported dependency for application layout ids in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 556 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 558 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | allowed | Local binding for allowed in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 571 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | groups | Local binding for groups in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 572 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | positions | Local binding for positions in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 573 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.comprehension_573 | index | Comprehension item for index in test_v7_063_editor_colors_only_the_move_handle_per_tool.comprehension_573; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 575 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.comprehension_573 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 575 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | html | Local binding for html in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 577 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.comprehension_579 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 581 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.route | request_route | Parameter for request route in test_v7_063_editor_colors_only_the_move_handle_per_tool.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 586 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.route | request | Local binding for request in test_v7_063_editor_colors_only_the_move_handle_per_tool.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 588 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.color | page | Parameter for page in test_v7_063_editor_colors_only_the_move_handle_per_tool.color; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 602 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool.color | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 602 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | driver | Managed resource for driver in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 611 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | browser | Local binding for browser in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 612 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | page | Local binding for page in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 616 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | first | Local binding for first in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of color; see its callable contract | Enclosing invocation or class/instance lifetime | 628 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | second | Local binding for second in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of color; see its callable contract | Enclosing invocation or class/instance lifetime | 629 |
| test_v7_063_editor_colors_only_the_move_handle_per_tool | third | Local binding for third in test_v7_063_editor_colors_only_the_move_handle_per_tool; use the enclosing contract and type below. | Return type of color; see its callable contract | Enclosing invocation or class/instance lifetime | 630 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | os | Imported dependency for os in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 644 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | sync_playwright | Imported dependency for sync playwright in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 646 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | application_layout_ids | Imported dependency for application layout ids in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 648 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | validate_layout | Imported dependency for validate layout in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 648 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 650 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | allowed | Local binding for allowed in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 656 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | dict | Enclosing invocation or class/instance lifetime | 657 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | saves | Local binding for saves in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 658 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | html | Local binding for html in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 659 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.comprehension_661 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 663 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route | request_route | Parameter for request route in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 668 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route | request | Local binding for request in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 671 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls.route | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of validate_layout; see its callable contract | Enclosing invocation or class/instance lifetime | 674 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | driver | Managed resource for driver in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 689 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | browser | Local binding for browser in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 690 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | page | Local binding for page in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 694 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 702, 725 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | control | Local binding for control in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 708 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | before | Local binding for before in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 709 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | after | Local binding for after in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 712 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | box | Loop item for box in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 725 |
| test_v6_044_editor_moves_resizes_and_restores_code_widget_controls | restored | Local binding for restored in test_v6_044_editor_moves_resizes_and_restores_code_widget_controls; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 726 |
| test_v7_066_widget_source_name_accepts_only_a_tool_identifier | widget_source_name | Imported dependency for widget source name in test_v7_066_widget_source_name_accepts_only_a_tool_identifier; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 742 |
| test_v7_066_widget_source_name_accepts_only_a_tool_identifier | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 745 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | os | Imported dependency for os in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 753 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | sync_playwright | Imported dependency for sync playwright in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 755 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | application_layout_groups | Imported dependency for application layout groups in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 757 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | application_layout_ids | Imported dependency for application layout ids in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 757 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 759 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | allowed | Local binding for allowed in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 765 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | groups | Local binding for groups in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 766 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | positions | Local binding for positions in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 767 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool.comprehension_767 | index | Comprehension item for index in test_v7_066_editor_posts_the_double_clicked_widget_tool.comprehension_767; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 769 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool.comprehension_767 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 769 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | html | Local binding for html in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 771 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool.comprehension_773 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 775 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool.route | request_route | Parameter for request route in test_v7_066_editor_posts_the_double_clicked_widget_tool.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 780 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | driver | Managed resource for driver in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 795 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | browser | Local binding for browser in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 796 |
| test_v7_066_editor_posts_the_double_clicked_widget_tool | page | Local binding for page in test_v7_066_editor_posts_the_double_clicked_widget_tool; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 800 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | os | Imported dependency for os in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 827 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | expect | Imported dependency for expect in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 829 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | sync_playwright | Imported dependency for sync playwright in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 829 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | html | Local binding for html in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 831 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | child | Local binding for child in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 839 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message.route | request_route | Parameter for request route in test_v7_066_parent_selects_the_widget_file_from_a_frame_message.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 844 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | driver | Managed resource for driver in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 851 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | browser | Local binding for browser in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 852 |
| test_v7_066_parent_selects_the_widget_file_from_a_frame_message | page | Local binding for page in test_v7_066_parent_selects_the_widget_file_from_a_frame_message; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 856 |
