# Reference for tests/test_application_update.py

V7-048: update only reviewed maintained runtimes using independent fixtures.

Source fingerprint: 38465f87a71e8e723355852907e8d03b0e2cbb8940d8e55459cad79147ca0f60

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### update_fixture

Represent a previously authenticated package with an obsolete maintained template.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_reviewed_update_preserves_logic_layout_and_source

Only the maintained app template and bound metadata may change after fresh gates.

Kind: callable. Declared return: None. Source line: 82.

### test_reviewed_update_preserves_logic_layout_and_source.verified

Stand in for real native/browser verification of the exact reviewed candidate.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_unauthorized_changed_bytes_are_blocked

Runtime refresh cannot legitimize changed generated logic or acceptance data.

Kind: callable. Declared return: None. Source line: 117.

### test_failed_or_changed_verification_keeps_installed_bytes

A failed gate or changed staging package must never activate an application.

Kind: callable. Declared return: None. Source line: 130.

### test_failed_or_changed_verification_keeps_installed_bytes.verify

Inject denial or post-verification drift, without executing any fixture source.

Kind: callable. Declared return: Not declared / class. Source line: 136.

### test_stale_plan_and_missing_dependency_cannot_activate

Reject new edits and absent tools rather than rewriting their approval hashes.

Kind: callable. Declared return: None. Source line: 156.

### test_partial_review_write_failure_restores_installed_state

Ordinary commit errors restore even the file whose write failed partway.

Kind: callable. Declared return: None. Source line: 167.

### test_partial_review_write_failure_restores_installed_state.interrupted

Simulate one partial disk write and allow subsequent rollback writes.

Kind: callable. Declared return: Not declared / class. Source line: 177.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | migration_fixture | Imported dependency for migration fixture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | make_code_candidate | Imported dependency for make code candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Protector | Imported dependency for Protector in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | _identity | Imported dependency for identity in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | policy_fingerprint | Imported dependency for policy fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | fingerprint | Imported dependency for fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| update_fixture | tmp_path | Parameter for tmp path in update_fixture; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 19 |
| update_fixture | ApplicationUpdates | Imported dependency for ApplicationUpdates in update_fixture; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 21 |
| update_fixture | migration | Local binding for migration in update_fixture; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| update_fixture | source | Explicit source document or source-code text; never imported for reference generation. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| update_fixture | target | Local binding for target in update_fixture; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| update_fixture | tool | Local binding for tool in update_fixture; use the enclosing contract and type below. | Return type of migration_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| update_fixture | item | Local binding for item in update_fixture; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| update_fixture | item.display_name | Attribute for item.display name in update_fixture; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| update_fixture | item.verified | Attribute for item.verified in update_fixture; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 28 |
| update_fixture | library | Local binding for library in update_fixture; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| update_fixture | installed | Local binding for installed in update_fixture; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| update_fixture | package | Local binding for package in update_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| update_fixture | old | Local binding for old in update_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| update_fixture | manifest_path | Local binding for manifest path in update_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| update_fixture | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| update_fixture | layout | Local binding for layout in update_fixture; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 40 |
| update_fixture | record_path | Local binding for record path in update_fixture; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| update_fixture | record | Local binding for record in update_fixture; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| update_fixture.comprehension_45 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| update_fixture | review_path | Local binding for review path in update_fixture; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| update_fixture | review | Local binding for review in update_fixture; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| update_fixture | area | Loop item for area in update_fixture; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 57 |
| update_fixture | grant | Local binding for grant in update_fixture; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| update_fixture | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 65 |
| update_fixture.comprehension_67 | case | Comprehension item for case in update_fixture.comprehension_67; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| update_fixture | service | Local binding for service in update_fixture; use the enclosing contract and type below. | Return type of ApplicationUpdates; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_reviewed_update_preserves_logic_layout_and_source | tmp_path | Parameter for tmp path in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 82 |
| test_reviewed_update_preserves_logic_layout_and_source | runtime_template | Imported dependency for runtime template in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| test_reviewed_update_preserves_logic_layout_and_source | service | Local binding for service in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_reviewed_update_preserves_logic_layout_and_source | migration | Local binding for migration in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_reviewed_update_preserves_logic_layout_and_source | identity | Explicit owner identity used by a session factory or fixture. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_reviewed_update_preserves_logic_layout_and_source | package | Local binding for package in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_reviewed_update_preserves_logic_layout_and_source | layout | Local binding for layout in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_reviewed_update_preserves_logic_layout_and_source | before | Local binding for before in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 87 |
| test_reviewed_update_preserves_logic_layout_and_source.comprehension_87 | p | Comprehension item for p in test_reviewed_update_preserves_logic_layout_and_source.comprehension_87; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 87 |
| test_reviewed_update_preserves_logic_layout_and_source | logic | Local binding for logic in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_reviewed_update_preserves_logic_layout_and_source | plan | Local binding for plan in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_reviewed_update_preserves_logic_layout_and_source | calls | Local binding for calls in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 92 |
| test_reviewed_update_preserves_logic_layout_and_source.verified | staged | Parameter for staged in test_reviewed_update_preserves_logic_layout_and_source.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_reviewed_update_preserves_logic_layout_and_source.verified | review | Parameter for review in test_reviewed_update_preserves_logic_layout_and_source.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_reviewed_update_preserves_logic_layout_and_source.verified | evidence | Parameter for evidence in test_reviewed_update_preserves_logic_layout_and_source.verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_reviewed_update_preserves_logic_layout_and_source | report | Local binding for report in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_reviewed_update_preserves_logic_layout_and_source.comprehension_106 | p | Comprehension item for p in test_reviewed_update_preserves_logic_layout_and_source.comprehension_106; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 106 |
| test_reviewed_update_preserves_logic_layout_and_source.comprehension_106 | data | Comprehension item for data in test_reviewed_update_preserves_logic_layout_and_source.comprehension_106; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 106 |
| test_reviewed_update_preserves_logic_layout_and_source | library | Local binding for library in test_reviewed_update_preserves_logic_layout_and_source; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_unauthorized_changed_bytes_are_blocked | tmp_path | Parameter for tmp path in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 117 |
| test_unauthorized_changed_bytes_are_blocked | changed | Parameter for changed in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 117 |
| test_unauthorized_changed_bytes_are_blocked | service | Local binding for service in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_unauthorized_changed_bytes_are_blocked | migration | Local binding for migration in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_unauthorized_changed_bytes_are_blocked | identity | Explicit owner identity used by a session factory or fixture. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_unauthorized_changed_bytes_are_blocked | package | Local binding for package in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_unauthorized_changed_bytes_are_blocked | _ | Local binding for  in test_unauthorized_changed_bytes_are_blocked; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_unauthorized_changed_bytes_are_blocked | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_failed_or_changed_verification_keeps_installed_bytes | tmp_path | Parameter for tmp path in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 130 |
| test_failed_or_changed_verification_keeps_installed_bytes | verdict | Parameter for verdict in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| test_failed_or_changed_verification_keeps_installed_bytes | service | Local binding for service in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_failed_or_changed_verification_keeps_installed_bytes | migration | Local binding for migration in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_failed_or_changed_verification_keeps_installed_bytes | identity | Explicit owner identity used by a session factory or fixture. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_failed_or_changed_verification_keeps_installed_bytes | package | Local binding for package in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_failed_or_changed_verification_keeps_installed_bytes | _ | Local binding for  in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_failed_or_changed_verification_keeps_installed_bytes | before | Local binding for before in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 133 |
| test_failed_or_changed_verification_keeps_installed_bytes.comprehension_133 | p | Comprehension item for p in test_failed_or_changed_verification_keeps_installed_bytes.comprehension_133; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 133 |
| test_failed_or_changed_verification_keeps_installed_bytes | plan | Local binding for plan in test_failed_or_changed_verification_keeps_installed_bytes; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_failed_or_changed_verification_keeps_installed_bytes.verify | staged | Parameter for staged in test_failed_or_changed_verification_keeps_installed_bytes.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 136 |
| test_failed_or_changed_verification_keeps_installed_bytes.verify | review | Parameter for review in test_failed_or_changed_verification_keeps_installed_bytes.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 136 |
| test_failed_or_changed_verification_keeps_installed_bytes.verify | evidence | Parameter for evidence in test_failed_or_changed_verification_keeps_installed_bytes.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 136 |
| test_failed_or_changed_verification_keeps_installed_bytes | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| test_failed_or_changed_verification_keeps_installed_bytes.comprehension_145 | p | Comprehension item for p in test_failed_or_changed_verification_keeps_installed_bytes.comprehension_145; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 145 |
| test_stale_plan_and_missing_dependency_cannot_activate | tmp_path | Parameter for tmp path in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 156 |
| test_stale_plan_and_missing_dependency_cannot_activate | service | Local binding for service in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_stale_plan_and_missing_dependency_cannot_activate | migration | Local binding for migration in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_stale_plan_and_missing_dependency_cannot_activate | _ | Local binding for  in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_stale_plan_and_missing_dependency_cannot_activate | package | Local binding for package in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_stale_plan_and_missing_dependency_cannot_activate | plan | Local binding for plan in test_stale_plan_and_missing_dependency_cannot_activate; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 159 |
| test_partial_review_write_failure_restores_installed_state | tmp_path | Parameter for tmp path in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 167 |
| test_partial_review_write_failure_restores_installed_state | monkeypatch | Parameter for monkeypatch in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_partial_review_write_failure_restores_installed_state | service | Local binding for service in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_partial_review_write_failure_restores_installed_state | migration | Local binding for migration in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_partial_review_write_failure_restores_installed_state | identity | Explicit owner identity used by a session factory or fixture. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_partial_review_write_failure_restores_installed_state | package | Local binding for package in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_partial_review_write_failure_restores_installed_state | _ | Local binding for  in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of update_fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_partial_review_write_failure_restores_installed_state | review_path | Local binding for review path in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_partial_review_write_failure_restores_installed_state | old_review | Local binding for old review in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_partial_review_write_failure_restores_installed_state | old_package | Local binding for old package in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 172 |
| test_partial_review_write_failure_restores_installed_state.comprehension_172 | p | Comprehension item for p in test_partial_review_write_failure_restores_installed_state.comprehension_172; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 172 |
| test_partial_review_write_failure_restores_installed_state | plan | Local binding for plan in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| test_partial_review_write_failure_restores_installed_state | original_write | Local binding for original write in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_partial_review_write_failure_restores_installed_state | failed | Local binding for failed in test_partial_review_write_failure_restores_installed_state; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 175 |
| test_partial_review_write_failure_restores_installed_state.interrupted | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 177 |
| test_partial_review_write_failure_restores_installed_state.interrupted | body | Parameter for body in test_partial_review_write_failure_restores_installed_state.interrupted; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 177 |
| test_partial_review_write_failure_restores_installed_state | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of apply; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| test_partial_review_write_failure_restores_installed_state.comprehension_191 | p | Comprehension item for p in test_partial_review_write_failure_restores_installed_state.comprehension_191; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 191 |
