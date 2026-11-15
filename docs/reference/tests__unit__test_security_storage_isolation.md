# Reference for tests/unit/test_security_storage_isolation.py

Storage roots are owned by the exact coordinator class that configured them.

``SecurityManager`` keeps tool roots in mutable class attributes. A subclass that
only overrides ``TOOLS_ROOT_DIR`` must never inherit a base-class runtime
configuration, otherwise its drafts or publication land in another owner's
catalog. Every path here is a pytest temporary directory.

Source fingerprint: 7ba0ca731160213a7a74cd51d929b9664bb19e9e6d65a2c4c2d172f0ba1594c0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### coordinator

Build one isolated coordinator subclass with an explicit tool root.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### stage

Write the three reviewed members and return the staged tool directory.

Kind: callable. Declared return: Path. Source line: 40.

### base_configured

Configure the base class exactly as a runtime would, then restore it.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_subclass_ignores_base_roots_for_draft_and_publication

A subclass with only its own tool root stages and publishes inside it.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### test_restore_does_not_replace_subclass_root_with_inherited_base_path

Restoration must not adopt a base-class published root.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_publication_without_an_owned_draft_fails_closed

An inherited active draft cannot authorize publication in a subclass.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### test_independent_coordinators_keep_independent_roots

Two coordinators configured separately never share a catalog.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_publication_still_refuses_to_overwrite_an_existing_tool

Fail-closed overwrite protection is unchanged by the ownership fix.

Kind: callable. Declared return: Not declared / class. Source line: 133.

### test_compatibility_then_creation_stage_order_stays_isolated

The reported order must pass without writing to the configured base root.

Kind: callable. Declared return: Not declared / class. Source line: 149.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 19 |
| coordinator | base | Parameter for base in coordinator; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| coordinator | tools_root | Parameter for tools root in coordinator; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 22 |
| coordinator | attributes | Parameter for attributes in coordinator; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| stage | security | Owner-scoped approval and path boundary injected into this service. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| stage | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 40 |
| stage | suffix | Loop item for suffix in stage; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 43 |
| stage | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 43 |
| base_configured | tmp_path | Parameter for tmp path in base_configured; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| base_configured | published | Local binding for published in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| base_configured | drafts | Local binding for drafts in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| base_configured | original | Local binding for original in base_configured; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 59 |
| base_configured | SecurityManager.TOOLS_ROOT_DIR | Attribute for SecurityManager.TOOLS ROOT DIR in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| base_configured | SecurityManager.PUBLISHED_TOOLS_ROOT_DIR | Attribute for SecurityManager.PUBLISHED TOOLS ROOT DIR in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| base_configured | SecurityManager.DRAFTS_ROOT_DIR | Attribute for SecurityManager.DRAFTS ROOT DIR in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| base_configured | SecurityManager._active_draft_root | Attribute for SecurityManager. active draft root in base_configured; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_subclass_ignores_base_roots_for_draft_and_publication | base_configured | Parameter for base configured in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_subclass_ignores_base_roots_for_draft_and_publication | tmp_path | Parameter for tmp path in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| test_subclass_ignores_base_roots_for_draft_and_publication | base_published | Local binding for base published in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_subclass_ignores_base_roots_for_draft_and_publication | _ | Local binding for  in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_subclass_ignores_base_roots_for_draft_and_publication | public | Local binding for public in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_subclass_ignores_base_roots_for_draft_and_publication | security | Owner-scoped approval and path boundary injected into this service. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_subclass_ignores_base_roots_for_draft_and_publication | staged | Local binding for staged in test_subclass_ignores_base_roots_for_draft_and_publication; use the enclosing contract and type below. | Return type of stage; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | base_configured | Parameter for base configured in test_restore_does_not_replace_subclass_root_with_inherited_base_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | tmp_path | Parameter for tmp path in test_restore_does_not_replace_subclass_root_with_inherited_base_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 94 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | base_published | Local binding for base published in test_restore_does_not_replace_subclass_root_with_inherited_base_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | _ | Local binding for  in test_restore_does_not_replace_subclass_root_with_inherited_base_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | public | Local binding for public in test_restore_does_not_replace_subclass_root_with_inherited_base_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_restore_does_not_replace_subclass_root_with_inherited_base_path | security | Owner-scoped approval and path boundary injected into this service. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_publication_without_an_owned_draft_fails_closed | base_configured | Parameter for base configured in test_publication_without_an_owned_draft_fails_closed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_publication_without_an_owned_draft_fails_closed | tmp_path | Parameter for tmp path in test_publication_without_an_owned_draft_fails_closed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_publication_without_an_owned_draft_fails_closed | security | Owner-scoped approval and path boundary injected into this service. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_publication_without_an_owned_draft_fails_closed | SecurityManager._active_draft_root | Attribute for SecurityManager. active draft root in test_publication_without_an_owned_draft_fails_closed; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| test_independent_coordinators_keep_independent_roots | base_configured | Parameter for base configured in test_independent_coordinators_keep_independent_roots; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_independent_coordinators_keep_independent_roots | tmp_path | Parameter for tmp path in test_independent_coordinators_keep_independent_roots; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_independent_coordinators_keep_independent_roots | first | Local binding for first in test_independent_coordinators_keep_independent_roots; use the enclosing contract and type below. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_independent_coordinators_keep_independent_roots | second | Local binding for second in test_independent_coordinators_keep_independent_roots; use the enclosing contract and type below. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | base_configured | Parameter for base configured in test_publication_still_refuses_to_overwrite_an_existing_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 133 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | tmp_path | Parameter for tmp path in test_publication_still_refuses_to_overwrite_an_existing_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 133 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | public | Local binding for public in test_publication_still_refuses_to_overwrite_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | security | Owner-scoped approval and path boundary injected into this service. | Return type of coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | existing | Local binding for existing in test_publication_still_refuses_to_overwrite_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_publication_still_refuses_to_overwrite_an_existing_tool | original | Local binding for original in test_publication_still_refuses_to_overwrite_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 139 |
| test_compatibility_then_creation_stage_order_stays_isolated | tmp_path | Parameter for tmp path in test_compatibility_then_creation_stage_order_stays_isolated; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 149 |
| test_compatibility_then_creation_stage_order_stays_isolated | home | Local binding for home in test_compatibility_then_creation_stage_order_stays_isolated; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_compatibility_then_creation_stage_order_stays_isolated | environment | Local binding for environment in test_compatibility_then_creation_stage_order_stays_isolated; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| test_compatibility_then_creation_stage_order_stays_isolated | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
