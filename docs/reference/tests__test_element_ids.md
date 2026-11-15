# Reference for tests/test_element_ids.py

Readable instance-scoped control identity regressions.

Source fingerprint: 4c08290d6c4db11b61a4cad57070495278f2308360b5c230eb0bf5f1fb54fc6a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### allocator

Import the maintained allocator without importing any generated module.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_duplicate_widget_instances_have_stable_unique_semantic_ids

Two copies of one tool must have distinct DOM IDs and event API names.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_parallel_allocations_do_not_collide

Scope allocation must be atomic even if widget setup becomes concurrent.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### test_invalid_or_foreign_scopes_and_control_roles_are_rejected

Never silently normalize distinct names into the same selector.

Kind: callable. Declared return: Not declared / class. Source line: 44.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ThreadPoolExecutor | Imported dependency for ThreadPoolExecutor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| allocator | ElementIds | Imported dependency for ElementIds in allocator; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_duplicate_widget_instances_have_stable_unique_semantic_ids | ids | Local binding for ids in test_duplicate_widget_instances_have_stable_unique_semantic_ids; use the enclosing contract and type below. | Return type of allocator; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_duplicate_widget_instances_have_stable_unique_semantic_ids | first | Local binding for first in test_duplicate_widget_instances_have_stable_unique_semantic_ids; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 18 |
| test_duplicate_widget_instances_have_stable_unique_semantic_ids | second | Local binding for second in test_duplicate_widget_instances_have_stable_unique_semantic_ids; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 18 |
| test_duplicate_widget_instances_have_stable_unique_semantic_ids.comprehension_26 | scope | Comprehension item for scope in test_duplicate_widget_instances_have_stable_unique_semantic_ids.comprehension_26; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 28 |
| test_duplicate_widget_instances_have_stable_unique_semantic_ids.comprehension_26 | role | Comprehension item for role in test_duplicate_widget_instances_have_stable_unique_semantic_ids.comprehension_26; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 29 |
| test_parallel_allocations_do_not_collide | ids | Local binding for ids in test_parallel_allocations_do_not_collide; use the enclosing contract and type below. | Return type of allocator; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_parallel_allocations_do_not_collide | pool | Managed resource for pool in test_parallel_allocations_do_not_collide; use the enclosing contract and type below. | Return type of ThreadPoolExecutor; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 39 |
| test_parallel_allocations_do_not_collide | scopes | Local binding for scopes in test_parallel_allocations_do_not_collide; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_parallel_allocations_do_not_collide.lambda_40 | _ | Callback parameter for  in test_parallel_allocations_do_not_collide.lambda_40; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 40 |
| test_invalid_or_foreign_scopes_and_control_roles_are_rejected | ids | Local binding for ids in test_invalid_or_foreign_scopes_and_control_roles_are_rejected; use the enclosing contract and type below. | Return type of allocator; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_invalid_or_foreign_scopes_and_control_roles_are_rejected | scope | Local binding for scope in test_invalid_or_foreign_scopes_and_control_roles_are_rejected; use the enclosing contract and type below. | Return type of new_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
