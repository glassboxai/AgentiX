# Reference for tests/test_v4_shell.py

Real Gradio structure regressions for the integrated v4 shell.

Source fingerprint: d09ab33f9d29857b751527262cd489ca944b48630fb7f384bd2efa30b759ed9e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ancestors

Return component ancestors from actual Gradio layout data.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_sidebar_is_shared_outside_both_tabs

Catch placing model controls in one tab or duplicating their session state.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### test_tools_callback_names_remain_unambiguous

Catch Applications callbacks shadowing public Tools compatibility names.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### test_sidebar_uses_its_own_backend_for_profile_actions

Catch retaining model-profile operations inside the Tools tab backend.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### test_general_composite_callback_matches_declared_outputs

Actual Gradio callbacks must hide legacy fields and render general results.

Kind: callable. Declared return: Not declared / class. Source line: 91.

### test_composite_callback_clears_stale_table_and_shows_the_contract

A rejected payload must clear named results and still explain the input schema.

Kind: callable. Declared return: Not declared / class. Source line: 123.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| ancestors | layout | Parameter for layout in ancestors; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| ancestors | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| ancestors | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 9 |
| ancestors | child | Loop item for child in ancestors; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 13 |
| ancestors | found | Local binding for found in ancestors; use the enclosing contract and type below. | Return type of ancestors; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| test_sidebar_is_shared_outside_both_tabs | demo | Local binding for demo in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_sidebar_is_shared_outside_both_tabs.lambda_22 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 22 |
| test_sidebar_is_shared_outside_both_tabs | components | Local binding for components in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_sidebar_is_shared_outside_both_tabs | all_tabs | Local binding for all tabs in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 24 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_24 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_24; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| test_sidebar_is_shared_outside_both_tabs | tabs | Local binding for tabs in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 25 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_25 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_25; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 27 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_25.comprehension_28 | t | Comprehension item for t in test_sidebar_is_shared_outside_both_tabs.comprehension_25.comprehension_28; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 28 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_30 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_30; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 30 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_36 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_36; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 36 |
| test_sidebar_is_shared_outside_both_tabs | sidebars | Local binding for sidebars in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 37 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_37 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_37; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| test_sidebar_is_shared_outside_both_tabs | shared | Local binding for shared in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 40 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_40 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_40; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_40.comprehension_43 | t | Comprehension item for t in test_sidebar_is_shared_outside_both_tabs.comprehension_40.comprehension_43; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 43 |
| test_sidebar_is_shared_outside_both_tabs | per_tab | Local binding for per tab in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 48 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_48 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_48; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 50 |
| test_sidebar_is_shared_outside_both_tabs | sidebar | Loop item for sidebar in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 54 |
| test_sidebar_is_shared_outside_both_tabs | owners | Local binding for owners in test_sidebar_is_shared_outside_both_tabs; use the enclosing contract and type below. | Return type of intersection; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_57 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_57; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 57 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_61 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_61; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 61 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_62 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_62; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 62 |
| test_sidebar_is_shared_outside_both_tabs.comprehension_63 | c | Comprehension item for c in test_sidebar_is_shared_outside_both_tabs.comprehension_63; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 63 |
| test_tools_callback_names_remain_unambiguous | demo | Local binding for demo in test_tools_callback_names_remain_unambiguous; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_tools_callback_names_remain_unambiguous.lambda_68 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 68 |
| test_tools_callback_names_remain_unambiguous | names | Local binding for names in test_tools_callback_names_remain_unambiguous; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 69 |
| test_tools_callback_names_remain_unambiguous.comprehension_69 | block | Comprehension item for block in test_tools_callback_names_remain_unambiguous.comprehension_69; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| test_sidebar_uses_its_own_backend_for_profile_actions | SidebarBackend | Imported dependency for SidebarBackend in test_sidebar_uses_its_own_backend_for_profile_actions; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 77 |
| test_sidebar_uses_its_own_backend_for_profile_actions | ToolsBackend | Imported dependency for ToolsBackend in test_sidebar_uses_its_own_backend_for_profile_actions; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
| test_sidebar_uses_its_own_backend_for_profile_actions | demo | Local binding for demo in test_sidebar_uses_its_own_backend_for_profile_actions; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_sidebar_uses_its_own_backend_for_profile_actions.lambda_81 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 81 |
| test_sidebar_uses_its_own_backend_for_profile_actions | methods | Local binding for methods in test_sidebar_uses_its_own_backend_for_profile_actions; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 82 |
| test_sidebar_uses_its_own_backend_for_profile_actions.comprehension_82 | block | Comprehension item for block in test_sidebar_uses_its_own_backend_for_profile_actions.comprehension_82; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 82 |
| test_sidebar_uses_its_own_backend_for_profile_actions.comprehension_83 | method | Comprehension item for method in test_sidebar_uses_its_own_backend_for_profile_actions.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 85 |
| test_general_composite_callback_matches_declared_outputs | tmp_path | Parameter for tmp path in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_general_composite_callback_matches_declared_outputs | monkeypatch | Parameter for monkeypatch in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| test_general_composite_callback_matches_declared_outputs | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 93 |
| test_general_composite_callback_matches_declared_outputs | sessions | Local binding for sessions in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_general_composite_callback_matches_declared_outputs.lambda_96 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 96 |
| test_general_composite_callback_matches_declared_outputs | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_general_composite_callback_matches_declared_outputs | backend.data | Attribute for backend.data in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_general_composite_callback_matches_declared_outputs.lambda_98 | text | Callback parameter for text in test_general_composite_callback_matches_declared_outputs.lambda_98; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 98 |
| test_general_composite_callback_matches_declared_outputs.lambda_98 | token | Callback parameter for token in test_general_composite_callback_matches_declared_outputs.lambda_98; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 98 |
| test_general_composite_callback_matches_declared_outputs.lambda_98 | request | Callback parameter for request in test_general_composite_callback_matches_declared_outputs.lambda_98; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 98 |
| test_general_composite_callback_matches_declared_outputs | backend.data_contract | Attribute for backend.data contract in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_general_composite_callback_matches_declared_outputs.lambda_103 | token | Callback parameter for token in test_general_composite_callback_matches_declared_outputs.lambda_103; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 103 |
| test_general_composite_callback_matches_declared_outputs.lambda_103 | request | Callback parameter for request in test_general_composite_callback_matches_declared_outputs.lambda_103; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 103 |
| test_general_composite_callback_matches_declared_outputs | demo | Local binding for demo in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_general_composite_callback_matches_declared_outputs | callback | Local binding for callback in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_general_composite_callback_matches_declared_outputs.comprehension_105 | block | Comprehension item for block in test_general_composite_callback_matches_declared_outputs.comprehension_105; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 107 |
| test_general_composite_callback_matches_declared_outputs | values | Local binding for values in test_general_composite_callback_matches_declared_outputs; use the enclosing contract and type below. | Return type of fn; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | tmp_path | Parameter for tmp path in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | monkeypatch | Parameter for monkeypatch in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 125 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | sessions | Local binding for sessions in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_128 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 128 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | backend.data | Attribute for backend.data in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130 | text | Callback parameter for text in test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 130 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130 | token | Callback parameter for token in test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 130 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130 | request | Callback parameter for request in test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_130; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 130 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | backend.data_contract | Attribute for backend.data contract in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_135 | token | Callback parameter for token in test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_135; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 135 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_135 | request | Callback parameter for request in test_composite_callback_clears_stale_table_and_shows_the_contract.lambda_135; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 135 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | demo | Local binding for demo in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 136 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | callback | Local binding for callback in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_composite_callback_clears_stale_table_and_shows_the_contract.comprehension_137 | block | Comprehension item for block in test_composite_callback_clears_stale_table_and_shows_the_contract.comprehension_137; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 139 |
| test_composite_callback_clears_stale_table_and_shows_the_contract | values | Local binding for values in test_composite_callback_clears_stale_table_and_shows_the_contract; use the enclosing contract and type below. | Return type of fn; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
