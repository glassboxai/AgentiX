# Reference for tests/integration/test_widget_protection.py

Opt-in real Windows DPAPI widget record reload using trusted temporary fixtures.

Source fingerprint: f37addf9e9e2230cd26b33fa69099f05710d2da3ba958461afd0bb94022440ce

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_real_widget_approval_can_be_reloaded_by_a_new_process

No existing credential/artifact is read; metadata survives a fresh process.

Kind: callable. Declared return: Not declared / class. Source line: 18.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | installed | Imported dependency for installed in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | registry | Imported dependency for registry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | list | Module/process lifetime | 12 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | tmp_path | Parameter for tmp path in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | WidgetStore | Imported dependency for WidgetStore in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | fixture | Local binding for fixture in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | tool | Local binding for tool in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | directory | Local binding for directory in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | service | Local binding for service in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Return type of WidgetStore; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | payload | Local binding for payload in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 36 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process.comprehension_36 | key | Comprehension item for key in test_real_widget_approval_can_be_reloaded_by_a_new_process.comprehension_36; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process.comprehension_36 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | script | Local binding for script in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 40 |
| test_real_widget_approval_can_be_reloaded_by_a_new_process | child | Local binding for child in test_real_widget_approval_can_be_reloaded_by_a_new_process; use the enclosing contract and type below. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
