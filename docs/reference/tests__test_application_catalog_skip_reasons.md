# Reference for tests/test_application_catalog_skip_reasons.py

Portable catalog skip-reason regressions; trusted temporary fixtures only.

Source fingerprint: 2d69d9b896ebdf4233764873393dcb23ad8ce533b96b6fa627c8cb2019263a6a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### FixtureProtector

Authenticate temporary approval records without using Windows credentials.

Kind: class. Declared return: Not declared / class. Source line: 50.

### FixtureProtector.seal

Bind fixture bytes to a test-only key.

Kind: callable. Declared return: bytes. Source line: 53.

### FixtureProtector.unseal

Reject modified fixture bytes before decoding them.

Kind: callable. Declared return: bytes. Source line: 57.

### test_durable_approvals_populate_fresh_catalog_and_candidate_context

Six unchanged reviewed grants become candidates without tool execution.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### install

Publish a fixture catalog entry with an optional host-boundary reuse grant.

Kind: callable. Declared return: Not declared / class. Source line: 130.

### test_valid_portable_tool_resolves_with_schema

A canonical approved fixture remains eligible after the diagnostics change.

Kind: callable. Declared return: Not declared / class. Source line: 152.

### test_missing_reusable_approval_is_named

An installed but unapproved tool must report its actionable skip reason.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### test_unapproved_catalog_skip_is_debug_and_payload_free

Keep repeated eligibility decisions out of INFO logs and omit tool identity.

Kind: callable. Declared return: Not declared / class. Source line: 167.

### test_non_portable_source_is_named

Computation-policy rejection must name the tool and the rejected imports.

Kind: callable. Declared return: Not declared / class. Source line: 185.

### test_non_canonical_contract_is_named

A schema failure must name the tool and the canonical contract reason.

Kind: callable. Declared return: Not declared / class. Source line: 192.

### test_uncovered_canonical_function_is_named

Approval covering only another function must report the coverage gap.

Kind: callable. Declared return: Not declared / class. Source line: 199.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | hmac | Imported dependency for hmac in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | present_candidates | Imported dependency for present candidates in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | CatalogDependencyError | Imported dependency for CatalogDependencyError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | CatalogToolRegistry | Imported dependency for CatalogToolRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | CANONICAL | Module binding for CANONICAL in module; use the enclosing contract and type below. | bytes | Module/process lifetime | 18 |
| module | NON_PORTABLE | Module binding for NON PORTABLE in module; use the enclosing contract and type below. | bytes | Module/process lifetime | 28 |
| module | WRONG_FUNCTION | Module binding for WRONG FUNCTION in module; use the enclosing contract and type below. | bytes | Module/process lifetime | 39 |
| FixtureProtector.seal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| FixtureProtector.seal | data | Parameter for data in FixtureProtector.seal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 53 |
| FixtureProtector.unseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| FixtureProtector.unseal | data | Parameter for data in FixtureProtector.unseal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 57 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | tmp_path | Parameter for tmp path in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | store | Local binding for store in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | names | Local binding for names in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of tuple; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context.comprehension_73 | index | Comprehension item for index in test_durable_approvals_populate_fresh_catalog_and_candidate_context.comprehension_73; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 73 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | sources | Local binding for sources in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 74 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 75, 117 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | source | Explicit source document or source-code text; never imported for reference generation. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 77 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | folder | Local binding for folder in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | ledger | Local binding for ledger in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | context | Local binding for context in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context.comprehension_111 | item | Comprehension item for item in test_durable_approvals_populate_fresh_catalog_and_candidate_context.comprehension_111; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | registry | Local binding for registry in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of CatalogToolRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | results | Local binding for results in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 116 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | descriptor | Local binding for descriptor in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of descriptor_from_source; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_durable_approvals_populate_fresh_catalog_and_candidate_context | view | Local binding for view in test_durable_approvals_populate_fresh_catalog_and_candidate_context; use the enclosing contract and type below. | Return type of present_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| install | tmp_path | Parameter for tmp path in install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| install | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| install | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| install | functions | Parameter for functions in install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| install | grant | Parameter for grant in install; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| install | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| install | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in install; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| install | ledger | Local binding for ledger in install; use the enclosing contract and type below. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| install | folder | Local binding for folder in install; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| install | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 138 |
| test_valid_portable_tool_resolves_with_schema | tmp_path | Parameter for tmp path in test_valid_portable_tool_resolves_with_schema; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 152 |
| test_valid_portable_tool_resolves_with_schema | fixture | Local binding for fixture in test_valid_portable_tool_resolves_with_schema; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_valid_portable_tool_resolves_with_schema | tools | Local binding for tools in test_valid_portable_tool_resolves_with_schema; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| test_missing_reusable_approval_is_named | tmp_path | Parameter for tmp path in test_missing_reusable_approval_is_named; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_missing_reusable_approval_is_named | fixture | Local binding for fixture in test_missing_reusable_approval_is_named; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_unapproved_catalog_skip_is_debug_and_payload_free | tmp_path | Parameter for tmp path in test_unapproved_catalog_skip_is_debug_and_payload_free; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_unapproved_catalog_skip_is_debug_and_payload_free | caplog | Parameter for caplog in test_unapproved_catalog_skip_is_debug_and_payload_free; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_unapproved_catalog_skip_is_debug_and_payload_free | fixture | Local binding for fixture in test_unapproved_catalog_skip_is_debug_and_payload_free; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_non_portable_source_is_named | tmp_path | Parameter for tmp path in test_non_portable_source_is_named; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 185 |
| test_non_portable_source_is_named | fixture | Local binding for fixture in test_non_portable_source_is_named; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_non_canonical_contract_is_named | tmp_path | Parameter for tmp path in test_non_canonical_contract_is_named; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 192 |
| test_non_canonical_contract_is_named | fixture | Local binding for fixture in test_non_canonical_contract_is_named; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 194 |
| test_uncovered_canonical_function_is_named | tmp_path | Parameter for tmp path in test_uncovered_canonical_function_is_named; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 199 |
| test_uncovered_canonical_function_is_named | fixture | Local binding for fixture in test_uncovered_canonical_function_is_named; use the enclosing contract and type below. | Return type of install; see its callable contract | Enclosing invocation or class/instance lifetime | 201 |
