# Reference for tests/test_catalog_migration.py

V7-047: authenticated relocation uses authored fixtures, never user artifacts.

Source fingerprint: 268252831b1cec68f54a878aafe05a545d34a9e0ce1fee29e593b6dcae36e4d5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### migration_fixture

Build source grants and copied bytes under independent temporary roots.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_readonly_plan_and_reviewed_relocation

A reviewed exact plan makes both grants reusable without changing source.

Kind: callable. Declared return: None. Source line: 62.

### test_changed_or_unauthenticated_bytes_never_migrate

Corruption and policy drift stay blocked; no target grant is minted.

Kind: callable. Declared return: None. Source line: 88.

### test_stale_review_and_destination_conflict_are_preserved

No operation overwrites a new destination grant or uses a stale review.

Kind: callable. Declared return: None. Source line: 113.

### test_application_record_requires_native_browser_verdict

A protected prior review alone never marks an app verified for v7.

Kind: callable. Declared return: None. Source line: 123.

### test_application_record_requires_native_browser_verdict.verified

Stand in for the explicit native/browser boundary, never model execution.

Kind: callable. Declared return: Not declared / class. Source line: 158.

### test_changed_reviewed_cases_require_widget_revalidation

Current tool approval survives; an older widget binding needs fresh gates.

Kind: callable. Declared return: None. Source line: 180.

### test_changed_reviewed_cases_require_widget_revalidation.verify

Record the exact current contract behind a native/browser test double.

Kind: callable. Declared return: Not declared / class. Source line: 203.

### test_verifier_drift_cannot_mint_widget_grant

A successful child claim cannot conceal bytes changed during native checks.

Kind: callable. Declared return: None. Source line: 215.

### test_verifier_drift_cannot_mint_widget_grant.drift

Simulate an untrusted concurrent edit after a nominal verification result.

Kind: callable. Declared return: Not declared / class. Source line: 223.

### test_conflicting_widget_approval_is_never_overwritten

Preserve destination records even when their contents cannot be authenticated.

Kind: callable. Declared return: None. Source line: 235.

### test_hardlinked_input_is_blocked

Do not relocate approvals over a Windows hard-link alias.

Kind: callable. Declared return: None. Source line: 247.

### test_real_widget_migration_checks_reviewed_value

Native/browser gates exercise authored widget fixtures without a real model.

Kind: callable. Declared return: None. Source line: 258.

### test_native_failure_is_reported_without_a_grant

Native startup/test errors retain a receipt and cannot mint widget approval.

Kind: callable. Declared return: None. Source line: 295.

### test_native_failure_is_reported_without_a_grant.failed

Represent a native failure without starting a process in offline tests.

Kind: callable. Declared return: Not declared / class. Source line: 303.

### test_exception_cases_are_compared_outside_child

Never discard reviewed exception cases or give expected values to the child.

Kind: callable. Declared return: None. Source line: 315.

### test_exception_cases_are_compared_outside_child.evaluate

Observe a native boundary double that receives inputs only.

Kind: callable. Declared return: Not declared / class. Source line: 332.

### test_empty_destination_tool_record_does_not_restore_old_grant

An explicit corrupt destination record must not fall back to source trust.

Kind: callable. Declared return: None. Source line: 351.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | approved_tool | Imported dependency for approved tool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | WIDGET | Imported dependency for WIDGET in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Protector | Imported dependency for Protector in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | policy_fingerprint | Imported dependency for policy fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | WidgetStore | Imported dependency for WidgetStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| migration_fixture | tmp_path | Parameter for tmp path in migration_fixture; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 17 |
| migration_fixture | CatalogMigration | Imported dependency for CatalogMigration in migration_fixture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| migration_fixture | source | Explicit source document or source-code text; never imported for reference generation. | tuple | Enclosing invocation or class/instance lifetime | 21 |
| migration_fixture | target | Local binding for target in migration_fixture; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 21 |
| migration_fixture | tools | Local binding for tools in migration_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| migration_fixture | tool | Local binding for tool in migration_fixture; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| migration_fixture | folder | Local binding for folder in migration_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| migration_fixture | grant | Local binding for grant in migration_fixture; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| migration_fixture | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 31 |
| migration_fixture.comprehension_33 | case | Comprehension item for case in migration_fixture.comprehension_33; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 34 |
| migration_fixture | widgets | Local binding for widgets in migration_fixture; use the enclosing contract and type below. | Return type of WidgetStore; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| migration_fixture | resolve_artifact_path | Imported dependency for resolve artifact path in migration_fixture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 51 |
| migration_fixture | widgets.security.validate_and_resolve_path | Attribute for widgets.security.validate and resolve path in migration_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| migration_fixture.lambda_53 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 53 |
| migration_fixture.lambda_53 | file | Callback parameter for file in migration_fixture.lambda_53; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 53 |
| migration_fixture | service | Local binding for service in migration_fixture; use the enclosing contract and type below. | Return type of CatalogMigration; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_readonly_plan_and_reviewed_relocation | tmp_path | Parameter for tmp path in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 62 |
| test_readonly_plan_and_reviewed_relocation | service | Local binding for service in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_readonly_plan_and_reviewed_relocation | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_readonly_plan_and_reviewed_relocation | target | Local binding for target in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_readonly_plan_and_reviewed_relocation | tool | Local binding for tool in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_readonly_plan_and_reviewed_relocation | before | Local binding for before in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 65 |
| test_readonly_plan_and_reviewed_relocation.comprehension_65 | p | Comprehension item for p in test_readonly_plan_and_reviewed_relocation.comprehension_65; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 65 |
| test_readonly_plan_and_reviewed_relocation | plan | Local binding for plan in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_readonly_plan_and_reviewed_relocation.comprehension_67 | i | Comprehension item for i in test_readonly_plan_and_reviewed_relocation.comprehension_67; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 67 |
| test_readonly_plan_and_reviewed_relocation | report | Local binding for report in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_readonly_plan_and_reviewed_relocation.comprehension_75 | i | Comprehension item for i in test_readonly_plan_and_reviewed_relocation.comprehension_75; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 75 |
| test_readonly_plan_and_reviewed_relocation | fresh | Local binding for fresh in test_readonly_plan_and_reviewed_relocation; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_readonly_plan_and_reviewed_relocation.comprehension_83 | p | Comprehension item for p in test_readonly_plan_and_reviewed_relocation.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_readonly_plan_and_reviewed_relocation.comprehension_83 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_readonly_plan_and_reviewed_relocation.comprehension_84 | i | Comprehension item for i in test_readonly_plan_and_reviewed_relocation.comprehension_84; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 84 |
| test_changed_or_unauthenticated_bytes_never_migrate | tmp_path | Parameter for tmp path in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 88 |
| test_changed_or_unauthenticated_bytes_never_migrate | change | Parameter for change in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 88 |
| test_changed_or_unauthenticated_bytes_never_migrate | service | Local binding for service in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_changed_or_unauthenticated_bytes_never_migrate | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_changed_or_unauthenticated_bytes_never_migrate | target | Local binding for target in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_changed_or_unauthenticated_bytes_never_migrate | _ | Local binding for  in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_changed_or_unauthenticated_bytes_never_migrate | path | Path under validation or an explicitly scoped maintained source path. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 92, 95 |
| test_changed_or_unauthenticated_bytes_never_migrate | record | Local binding for record in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_changed_or_unauthenticated_bytes_never_migrate | suffix | Local binding for suffix in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_changed_or_unauthenticated_bytes_never_migrate | plan | Local binding for plan in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_changed_or_unauthenticated_bytes_never_migrate.comprehension_108 | i | Comprehension item for i in test_changed_or_unauthenticated_bytes_never_migrate.comprehension_108; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 108 |
| test_changed_or_unauthenticated_bytes_never_migrate | report | Local binding for report in test_changed_or_unauthenticated_bytes_never_migrate; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| test_changed_or_unauthenticated_bytes_never_migrate.comprehension_110 | i | Comprehension item for i in test_changed_or_unauthenticated_bytes_never_migrate.comprehension_110; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 110 |
| test_stale_review_and_destination_conflict_are_preserved | tmp_path | Parameter for tmp path in test_stale_review_and_destination_conflict_are_preserved; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 113 |
| test_stale_review_and_destination_conflict_are_preserved | service | Local binding for service in test_stale_review_and_destination_conflict_are_preserved; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_review_and_destination_conflict_are_preserved | _ | Local binding for  in test_stale_review_and_destination_conflict_are_preserved; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_review_and_destination_conflict_are_preserved | target | Local binding for target in test_stale_review_and_destination_conflict_are_preserved; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_review_and_destination_conflict_are_preserved | plan | Local binding for plan in test_stale_review_and_destination_conflict_are_preserved; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| test_application_record_requires_native_browser_verdict | tmp_path | Parameter for tmp path in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 123 |
| test_application_record_requires_native_browser_verdict | make_code_candidate | Imported dependency for make code candidate in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 125 |
| test_application_record_requires_native_browser_verdict | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 127 |
| test_application_record_requires_native_browser_verdict | InstalledApps | Imported dependency for InstalledApps in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 128 |
| test_application_record_requires_native_browser_verdict | service | Local binding for service in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_application_record_requires_native_browser_verdict | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_application_record_requires_native_browser_verdict | target | Local binding for target in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_application_record_requires_native_browser_verdict | _ | Local binding for  in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_application_record_requires_native_browser_verdict | item | Local binding for item in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_application_record_requires_native_browser_verdict | item.verified | Attribute for item.verified in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 133 |
| test_application_record_requires_native_browser_verdict | library | Local binding for library in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_application_record_requires_native_browser_verdict | plan | Local binding for plan in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_application_record_requires_native_browser_verdict.comprehension_142 | i | Comprehension item for i in test_application_record_requires_native_browser_verdict.comprehension_142; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 142 |
| test_application_record_requires_native_browser_verdict | report | Local binding for report in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 143, 165 |
| test_application_record_requires_native_browser_verdict | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_application_record_requires_native_browser_verdict.comprehension_144 | i | Comprehension item for i in test_application_record_requires_native_browser_verdict.comprehension_144; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 144 |
| test_application_record_requires_native_browser_verdict | calls | Local binding for calls in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 156 |
| test_application_record_requires_native_browser_verdict.verified | package | Parameter for package in test_application_record_requires_native_browser_verdict.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_application_record_requires_native_browser_verdict.verified | review | Parameter for review in test_application_record_requires_native_browser_verdict.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_application_record_requires_native_browser_verdict.verified | evidence | Parameter for evidence in test_application_record_requires_native_browser_verdict.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| test_application_record_requires_native_browser_verdict | service.verifier | Attribute for service.verifier in test_application_record_requires_native_browser_verdict; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_application_record_requires_native_browser_verdict.comprehension_167 | i | Comprehension item for i in test_application_record_requires_native_browser_verdict.comprehension_167; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 167 |
| test_changed_reviewed_cases_require_widget_revalidation | tmp_path | Parameter for tmp path in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 180 |
| test_changed_reviewed_cases_require_widget_revalidation | service | Local binding for service in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_changed_reviewed_cases_require_widget_revalidation | _ | Local binding for  in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_changed_reviewed_cases_require_widget_revalidation | target | Local binding for target in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_changed_reviewed_cases_require_widget_revalidation | tool | Local binding for tool in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_changed_reviewed_cases_require_widget_revalidation | grant | Local binding for grant in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_changed_reviewed_cases_require_widget_revalidation | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 189 |
| test_changed_reviewed_cases_require_widget_revalidation.comprehension_191 | case | Comprehension item for case in test_changed_reviewed_cases_require_widget_revalidation.comprehension_191; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 192 |
| test_changed_reviewed_cases_require_widget_revalidation | plan | Local binding for plan in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_changed_reviewed_cases_require_widget_revalidation | report | Local binding for report in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 199, 209 |
| test_changed_reviewed_cases_require_widget_revalidation | calls | Local binding for calls in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 201 |
| test_changed_reviewed_cases_require_widget_revalidation.verify | current | Parameter for current in test_changed_reviewed_cases_require_widget_revalidation.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 203 |
| test_changed_reviewed_cases_require_widget_revalidation.verify | proposal | Parameter for proposal in test_changed_reviewed_cases_require_widget_revalidation.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 203 |
| test_changed_reviewed_cases_require_widget_revalidation.verify | css | Parameter for css in test_changed_reviewed_cases_require_widget_revalidation.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 203 |
| test_changed_reviewed_cases_require_widget_revalidation.verify | evidence | Parameter for evidence in test_changed_reviewed_cases_require_widget_revalidation.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 203 |
| test_changed_reviewed_cases_require_widget_revalidation | service.widget_verifier | Attribute for service.widget verifier in test_changed_reviewed_cases_require_widget_revalidation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_verifier_drift_cannot_mint_widget_grant | tmp_path | Parameter for tmp path in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 215 |
| test_verifier_drift_cannot_mint_widget_grant | service | Local binding for service in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_verifier_drift_cannot_mint_widget_grant | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_verifier_drift_cannot_mint_widget_grant | target | Local binding for target in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_verifier_drift_cannot_mint_widget_grant | _ | Local binding for  in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_verifier_drift_cannot_mint_widget_grant | path | Path under validation or an explicitly scoped maintained source path. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 218 |
| test_verifier_drift_cannot_mint_widget_grant | record | Local binding for record in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_verifier_drift_cannot_mint_widget_grant.drift | args | Parameter for args in test_verifier_drift_cannot_mint_widget_grant.drift; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_verifier_drift_cannot_mint_widget_grant | service.widget_verifier | Attribute for service.widget verifier in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 228 |
| test_verifier_drift_cannot_mint_widget_grant | report | Local binding for report in test_verifier_drift_cannot_mint_widget_grant; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 229 |
| test_conflicting_widget_approval_is_never_overwritten | tmp_path | Parameter for tmp path in test_conflicting_widget_approval_is_never_overwritten; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 235 |
| test_conflicting_widget_approval_is_never_overwritten | service | Local binding for service in test_conflicting_widget_approval_is_never_overwritten; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| test_conflicting_widget_approval_is_never_overwritten | _ | Local binding for  in test_conflicting_widget_approval_is_never_overwritten; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| test_conflicting_widget_approval_is_never_overwritten | target | Local binding for target in test_conflicting_widget_approval_is_never_overwritten; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| test_conflicting_widget_approval_is_never_overwritten | path | Path under validation or an explicitly scoped maintained source path. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| test_conflicting_widget_approval_is_never_overwritten | plan | Local binding for plan in test_conflicting_widget_approval_is_never_overwritten; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 241 |
| test_hardlinked_input_is_blocked | tmp_path | Parameter for tmp path in test_hardlinked_input_is_blocked; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 247 |
| test_hardlinked_input_is_blocked | service | Local binding for service in test_hardlinked_input_is_blocked; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| test_hardlinked_input_is_blocked | _ | Local binding for  in test_hardlinked_input_is_blocked; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| test_hardlinked_input_is_blocked | target | Local binding for target in test_hardlinked_input_is_blocked; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| test_hardlinked_input_is_blocked | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_hardlinked_input_is_blocked | alias | Local binding for alias in test_hardlinked_input_is_blocked; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_real_widget_migration_checks_reviewed_value | tmp_path | Parameter for tmp path in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 258 |
| test_real_widget_migration_checks_reviewed_value | monkeypatch | Parameter for monkeypatch in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 258 |
| test_real_widget_migration_checks_reviewed_value | verify_widget | Imported dependency for verify widget in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 260 |
| test_real_widget_migration_checks_reviewed_value | service | Local binding for service in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_real_widget_migration_checks_reviewed_value | _ | Local binding for  in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_real_widget_migration_checks_reviewed_value | target | Local binding for target in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_real_widget_migration_checks_reviewed_value | tool | Local binding for tool in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_real_widget_migration_checks_reviewed_value | evidence | Local binding for evidence in test_real_widget_migration_checks_reviewed_value; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 264 |
| test_native_failure_is_reported_without_a_grant | tmp_path | Parameter for tmp path in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 295 |
| test_native_failure_is_reported_without_a_grant | service | Local binding for service in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| test_native_failure_is_reported_without_a_grant | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| test_native_failure_is_reported_without_a_grant | _ | Local binding for  in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| test_native_failure_is_reported_without_a_grant | path | Path under validation or an explicitly scoped maintained source path. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| test_native_failure_is_reported_without_a_grant | record | Local binding for record in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 299 |
| test_native_failure_is_reported_without_a_grant.failed | args | Parameter for args in test_native_failure_is_reported_without_a_grant.failed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 303 |
| test_native_failure_is_reported_without_a_grant | service.widget_verifier | Attribute for service.widget verifier in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_native_failure_is_reported_without_a_grant | report | Local binding for report in test_native_failure_is_reported_without_a_grant; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
| test_exception_cases_are_compared_outside_child | tmp_path | Parameter for tmp path in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 316 |
| test_exception_cases_are_compared_outside_child | observed_type | Parameter for observed type in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 316 |
| test_exception_cases_are_compared_outside_child | passes | Parameter for passes in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 316 |
| test_exception_cases_are_compared_outside_child | replace | Imported dependency for replace in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 319 |
| test_exception_cases_are_compared_outside_child | verify_exception_cases | Imported dependency for verify exception cases in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 321 |
| test_exception_cases_are_compared_outside_child | case | Local binding for case in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 323 |
| test_exception_cases_are_compared_outside_child | tool | Local binding for tool in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| test_exception_cases_are_compared_outside_child | calls | Local binding for calls in test_exception_cases_are_compared_outside_child; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 330 |
| test_exception_cases_are_compared_outside_child.evaluate | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 332 |
| test_exception_cases_are_compared_outside_child.evaluate | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 332 |
| test_exception_cases_are_compared_outside_child.evaluate | function | Parameter for function in test_exception_cases_are_compared_outside_child.evaluate; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 332 |
| test_exception_cases_are_compared_outside_child.evaluate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 332 |
| test_empty_destination_tool_record_does_not_restore_old_grant | tmp_path | Parameter for tmp path in test_empty_destination_tool_record_does_not_restore_old_grant; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 351 |
| test_empty_destination_tool_record_does_not_restore_old_grant | service | Local binding for service in test_empty_destination_tool_record_does_not_restore_old_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_empty_destination_tool_record_does_not_restore_old_grant | _ | Local binding for  in test_empty_destination_tool_record_does_not_restore_old_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_empty_destination_tool_record_does_not_restore_old_grant | target | Local binding for target in test_empty_destination_tool_record_does_not_restore_old_grant; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_empty_destination_tool_record_does_not_restore_old_grant | path | Path under validation or an explicitly scoped maintained source path. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 354 |
| test_empty_destination_tool_record_does_not_restore_old_grant | plan | Local binding for plan in test_empty_destination_tool_record_does_not_restore_old_grant; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 357 |
