# Reference for tests/test_workflow_bindings.py

V5-ERR-041-01: general dataflow must preserve shared values and typed sources.

Source fingerprint: 188cce93e98de5887d7dd2ad1be786d05f1fb456a0bcaa92a2950f714b6c7a73

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### workflow

Return a fork with repeated tools, one shared source and one sampled item.

Kind: callable. Declared return: dict. Source line: 23.

### reviewed_tools

Author independent values with an early incompatible choice requiring backtracking.

Kind: callable. Declared return: dict. Source line: 52.

### make_workflow_candidate

Package only independently authored trusted fixtures, never existing artifacts.

Kind: callable. Declared return: Candidate. Source line: 80.

### make_workflow_candidate.factory

Inject fixture proposals without a model or subprocess.

Kind: callable. Declared return: Callable[[str, dict], dict]. Source line: 137.

### make_workflow_candidate.factory.client

Return independently authored proposals for the requested fixture role.

Kind: callable. Declared return: dict. Source line: 140.

### test_packaged_plan_retains_sources_and_independent_acceptance

The exact review binds flat inputs, the widget inventory and final results.

Kind: callable. Declared return: None. Source line: 170.

### test_native_shared_projected_fork_has_independent_results

Host-observed native results match authored expectations without live servers.

Kind: callable. Declared return: None. Source line: 200.

### test_real_gradio_shares_one_input_and_updates_connected_controls

Execute maintained callbacks in memory using only trusted fixture modules.

Kind: callable. Declared return: None. Source line: 217.

### test_native_browser_composition_uses_only_the_shared_external_input

A disposable native preview verifies real controls and every connected result.

Kind: callable. Declared return: None. Source line: 275.

### test_numeric_display_comparison_preserves_exact_value

V5-ERR-041-02: integer-formatted floats match without accepting numeric prefixes.

Kind: callable. Declared return: None. Source line: 307.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | SCHEMAS | Module binding for SCHEMAS in module; use the enclosing contract and type below. | dict | Module/process lifetime | 10 |
| reviewed_tools | SimpleNamespace | Imported dependency for SimpleNamespace in reviewed_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| reviewed_tools | tables | Local binding for tables in reviewed_tools; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 56 |
| reviewed_tools.comprehension_61.comprehension_66 | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 72 |
| reviewed_tools.comprehension_61.comprehension_66 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 72 |
| reviewed_tools.comprehension_61 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 76 |
| reviewed_tools.comprehension_61 | table | Comprehension item for table in reviewed_tools.comprehension_61; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 76 |
| make_workflow_candidate | tmp_path | Parameter for tmp path in make_workflow_candidate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 80 |
| make_workflow_candidate | ApplicationPipeline | Imported dependency for ApplicationPipeline in make_workflow_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 82 |
| make_workflow_candidate | extract_tool_schema | Imported dependency for extract tool schema in make_workflow_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 83 |
| make_workflow_candidate | ApprovedTool | Imported dependency for ApprovedTool in make_workflow_candidate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| make_workflow_candidate | bodies | Local binding for bodies in make_workflow_candidate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 86 |
| make_workflow_candidate | tools | Local binding for tools in make_workflow_candidate; use the enclosing contract and type below. | Return type of reviewed_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| make_workflow_candidate | widgets | Local binding for widgets in make_workflow_candidate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 92 |
| make_workflow_candidate | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 93 |
| make_workflow_candidate | body | Loop item for body in make_workflow_candidate; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 93 |
| make_workflow_candidate | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| make_workflow_candidate | schema | Local binding for schema in make_workflow_candidate; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| make_workflow_candidate | params | Local binding for params in make_workflow_candidate; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| make_workflow_candidate | controls | Local binding for controls in make_workflow_candidate; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 109 |
| make_workflow_candidate.comprehension_109 | parameter | Comprehension item for parameter in make_workflow_candidate.comprehension_109; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| make_workflow_candidate.comprehension_109 | shape | Comprehension item for shape in make_workflow_candidate.comprehension_109; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| make_workflow_candidate.comprehension_130 | parameter | Comprehension item for parameter in make_workflow_candidate.comprehension_130; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 130 |
| make_workflow_candidate.factory | folder | Parameter for folder in make_workflow_candidate.factory; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 137 |
| make_workflow_candidate.factory.client | role | Parameter for role in make_workflow_candidate.factory.client; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 140 |
| make_workflow_candidate.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | dict | Enclosing invocation or class/instance lifetime | 140 |
| make_workflow_candidate.factory.client.comprehension_145 | node | Comprehension item for node in make_workflow_candidate.factory.client.comprehension_145; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 146 |
| make_workflow_candidate.factory.client | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 160 |
| test_packaged_plan_retains_sources_and_independent_acceptance | tmp_path | Parameter for tmp path in test_packaged_plan_retains_sources_and_independent_acceptance; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 170 |
| test_packaged_plan_retains_sources_and_independent_acceptance | json | Imported dependency for json in test_packaged_plan_retains_sources_and_independent_acceptance; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 172 |
| test_packaged_plan_retains_sources_and_independent_acceptance | candidate | Local binding for candidate in test_packaged_plan_retains_sources_and_independent_acceptance; use the enclosing contract and type below. | Return type of make_workflow_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_packaged_plan_retains_sources_and_independent_acceptance | review | Local binding for review in test_packaged_plan_retains_sources_and_independent_acceptance; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_packaged_plan_retains_sources_and_independent_acceptance | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_native_shared_projected_fork_has_independent_results | tmp_path | Parameter for tmp path in test_native_shared_projected_fork_has_independent_results; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 200 |
| test_native_shared_projected_fork_has_independent_results | approve_application | Imported dependency for approve application in test_native_shared_projected_fork_has_independent_results; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| test_native_shared_projected_fork_has_independent_results | execute_application | Imported dependency for execute application in test_native_shared_projected_fork_has_independent_results; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 203 |
| test_native_shared_projected_fork_has_independent_results | candidate | Local binding for candidate in test_native_shared_projected_fork_has_independent_results; use the enclosing contract and type below. | Return type of make_workflow_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_native_shared_projected_fork_has_independent_results | approved | Local binding for approved in test_native_shared_projected_fork_has_independent_results; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | tmp_path | Parameter for tmp path in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 218 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | monkeypatch | Parameter for monkeypatch in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 218 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | importlib | Imported dependency for importlib in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 221 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | sys | Imported dependency for sys in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 222 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | runtime_template | Imported dependency for runtime template in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 224 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | bindings | Imported dependency for bindings in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 225 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | candidate | Local binding for candidate in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of make_workflow_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 229, 259 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | spec | Local binding for spec in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | module | Local binding for module in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | demo | Local binding for demo in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of create_application; see its callable contract | Enclosing invocation or class/instance lifetime | 245 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | callback | Local binding for callback in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| test_real_gradio_shares_one_input_and_updates_connected_controls.comprehension_247 | event | Comprehension item for event in test_real_gradio_shares_one_input_and_updates_connected_controls.comprehension_247; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 247 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | updates | Local binding for updates in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| test_real_gradio_shares_one_input_and_updates_connected_controls.comprehension_253 | component | Comprehension item for component in test_real_gradio_shares_one_input_and_updates_connected_controls.comprehension_253; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 253 |
| test_real_gradio_shares_one_input_and_updates_connected_controls | failed | Local binding for failed in test_real_gradio_shares_one_input_and_updates_connected_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 254 |
| test_native_browser_composition_uses_only_the_shared_external_input | tmp_path | Parameter for tmp path in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 275 |
| test_native_browser_composition_uses_only_the_shared_external_input | json | Imported dependency for json in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 277 |
| test_native_browser_composition_uses_only_the_shared_external_input | browser_verify | Imported dependency for browser verify in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 279 |
| test_native_browser_composition_uses_only_the_shared_external_input | approve_application | Imported dependency for approve application in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 280 |
| test_native_browser_composition_uses_only_the_shared_external_input | ApplicationPreview | Imported dependency for ApplicationPreview in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 281 |
| test_native_browser_composition_uses_only_the_shared_external_input | candidate | Local binding for candidate in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Return type of make_workflow_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_native_browser_composition_uses_only_the_shared_external_input | preview | Local binding for preview in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Return type of ApplicationPreview; see its callable contract | Enclosing invocation or class/instance lifetime | 284 |
| test_native_browser_composition_uses_only_the_shared_external_input | review | Local binding for review in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 285 |
| test_native_browser_composition_uses_only_the_shared_external_input | evidence | Local binding for evidence in test_native_browser_composition_uses_only_the_shared_external_input; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| test_numeric_display_comparison_preserves_exact_value | expected | Reviewed expected observation kept outside untrusted child execution. | int &#124; float | Enclosing invocation or class/instance lifetime | 307 |
| test_numeric_display_comparison_preserves_exact_value | display_expectation | Imported dependency for display expectation in test_numeric_display_comparison_preserves_exact_value; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 309 |
| test_numeric_display_comparison_preserves_exact_value | matcher | Local binding for matcher in test_numeric_display_comparison_preserves_exact_value; use the enclosing contract and type below. | Return type of display_expectation; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| test_numeric_display_comparison_preserves_exact_value | wrong | Loop item for wrong in test_numeric_display_comparison_preserves_exact_value; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 315 |
