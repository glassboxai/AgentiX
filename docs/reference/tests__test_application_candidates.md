# Reference for tests/test_application_candidates.py

RAG-010: candidate acceptance gates application generation and remains owner-bound.

Source fingerprint: 44fb54642cb799fa9b7264223d98b9fd960eedee63e0a8740116e1c3cd1c1898

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### match

Build a candidate from independently authored trusted source, never importing it.

Kind: callable. Declared return: SearchResult. Source line: 22.

### RetrievalDouble

Capture owner-specific searches without model or persistence access.

Kind: class. Declared return: Not declared / class. Source line: 29.

### RetrievalDouble.__init__

Record each query and requested result limit.

Kind: callable. Declared return: None. Source line: 34.

### RetrievalDouble.search

Return one stable candidate over the injected local-model boundary.

Kind: callable. Declared return: list[SearchResult]. Source line: 38.

### setup_backend

Compose the real application backend with independent tool and retrieval doubles.

Kind: callable. Declared return: tuple[ApplicationsBackend, Any, SimpleNamespace, dict[str, Any], RetrievalDouble]. Source line: 46.

### test_selected_registry_supplies_exact_subset_and_rechecks

Unrelated installed tools cannot enter accepted generation dependencies.

Kind: callable. Declared return: None. Source line: 69.

### test_search_does_not_generate_and_limit_is_forwarded

Generate application first requests candidates; changing limit searches again.

Kind: callable. Declared return: None. Source line: 84.

### test_ineligible_candidate_names_portability_instead_of_approval

An approved but non-portable tool must not be reported as unapproved.

Kind: callable. Declared return: None. Source line: 96.

### test_ineligible_candidate_names_portability_instead_of_approval.resolve

Mirror the registry excluding every installed entry.

Kind: callable. Declared return: dict[str, Any]. Source line: 101.

### test_generate_without_name_reports_the_missing_name_before_search

The name warning must appear at Generate, before any retrieval inference.

Kind: callable. Declared return: None. Source line: 123.

### test_acceptance_passes_only_server_snapshot

Acceptance consumes the exact shown selection and passes it to generation once.

Kind: callable. Declared return: None. Source line: 133.

### test_acceptance_passes_only_server_snapshot.generate

Capture the selected server-owned dependency contract without generation.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 141.

### test_changed_or_foreign_selection_cannot_generate

Changed descriptions, limits, source bytes and owners invalidate acceptance.

Kind: callable. Declared return: None. Source line: 167.

### test_startup_failure_is_retriable_and_clients_are_private

Startup failure keeps the GUI available; later owner clients are distinct.

Kind: callable. Declared return: None. Source line: 185.

### test_startup_failure_is_retriable_and_clients_are_private.factory

Fail startup once, then create inert owner-scoped provider clients.

Kind: callable. Declared return: Any. Source line: 189.

### test_candidate_logs_omit_description

Record retrieval/acceptance decisions without logging original request bodies.

Kind: callable. Declared return: None. Source line: 204.

### test_retrieval_handle_transition_is_correlated_and_payload_free

Expose retriever creation without recording the application description.

Kind: callable. Declared return: None. Source line: 216.

### test_selected_registry_preserves_legacy_role_keys

Selection constrains tools without changing existing adapter role contracts.

Kind: callable. Declared return: None. Source line: 234.

### test_real_generation_boundary_receives_only_candidates

Exercise production generation orchestration with a model-boundary spy.

Kind: callable. Declared return: None. Source line: 244.

### test_real_generation_boundary_receives_only_candidates.generate

Record dependencies without invoking agents or executing source.

Kind: callable. Declared return: Any. Source line: 255.

### test_candidate_labels_preserve_metadata_as_plain_text

Labels preserve bounded tool metadata while values carry only snapshot IDs.

Kind: callable. Declared return: None. Source line: 270.

### test_obsolete_search_does_not_replace_newer_description

Discard both successful and failed inference after the user edits the request.

Kind: callable. Declared return: None. Source line: 281.

### test_obsolete_search_does_not_replace_newer_description.slow

Simulate an edit arriving during retrieval without timing-dependent threads.

Kind: callable. Declared return: list[SearchResult]. Source line: 285.

### test_real_gradio_candidate_callback_contract

Construct actual controls and invoke their registered streaming callback in memory.

Kind: callable. Declared return: None. Source line: 301.

### test_real_gradio_accept_label_explains_a_blocked_selection

The disabled accept button must state the blocking reason in its own label.

Kind: callable. Declared return: None. Source line: 322.

### test_bootstrap_initializes_retrieval_once_before_view

Startup invokes index loading once and passes the same service to the backend.

Kind: callable. Declared return: None. Source line: 348.

### test_bootstrap_initializes_retrieval_once_before_view.Startup

Observe composition without opening storage, servers or model clients.

Kind: class. Declared return: Not declared / class. Source line: 368.

### test_bootstrap_initializes_retrieval_once_before_view.Startup.initialize

Record exactly the runtime catalog selected by the GUI startup.

Kind: callable. Declared return: None. Source line: 371.

### test_bootstrap_initializes_retrieval_once_before_view.factory

Provide the explicit startup test boundary.

Kind: callable. Declared return: Startup. Source line: 377.

### test_bootstrap_initializes_retrieval_once_before_view.build

Check startup ordering and injected retrieval identity.

Kind: callable. Declared return: Any. Source line: 386.

### test_retrieval_serializes_owner_index_operations

Two independent owner clients cannot mutate/query their shared index concurrently.

Kind: callable. Declared return: None. Source line: 403.

### test_retrieval_serializes_owner_index_operations.Client

Observe overlap at the real GUI service's injected retrieval boundary.

Kind: class. Declared return: Not declared / class. Source line: 411.

### test_retrieval_serializes_owner_index_operations.Client.search

Block the first owner until the second has attempted access.

Kind: callable. Declared return: list[SearchResult]. Source line: 414.

### test_acceptance_storage_failure_is_safe_and_logged

Unavailable approval storage cannot escape as a raw exception or start generation.

Kind: callable. Declared return: None. Source line: 442.

### test_acceptance_storage_failure_is_safe_and_logged.unavailable

Simulate inaccessible current approval metadata with a sensitive error body.

Kind: callable. Declared return: dict[str, Any]. Source line: 451.

### test_closed_owner_discards_inflight_candidate_result

Closing an application session invalidates its outstanding retrieval revision.

Kind: callable. Declared return: None. Source line: 464.

### test_closed_owner_discards_inflight_candidate_result.closing

Simulate owner cleanup completing before a pending model response returns.

Kind: callable. Declared return: list[SearchResult]. Source line: 468.

### test_repair_keeps_accepted_scope_and_rechecks_source

Repairs reuse the accepted dependency set and cannot adopt modified selected code.

Kind: callable. Declared return: None. Source line: 482.

### test_repair_keeps_accepted_scope_and_rechecks_source.generate

Record original and repair inputs without inference or source execution.

Kind: callable. Declared return: Any. Source line: 493.

### test_reviewed_tool_revision_invalidates_candidate_application

Publishing revised tool bytes requires a fresh candidate choice, never a broader catalog.

Kind: callable. Declared return: None. Source line: 520.

### test_busy_invalidation_is_logged_as_ignored

Log the actual outcome when an active generation retains its original context.

Kind: callable. Declared return: None. Source line: 570.

### test_candidate_subset_rejects_invalid_ids

Empty, foreign and duplicate browser IDs cannot authorize generation.

Kind: callable. Declared return: None. Source line: 588.

### test_candidate_subset_excludes_unchecked_tool

Only checked snapshot IDs reach generation, with current source hashes.

Kind: callable. Declared return: None. Source line: 601.

### test_candidate_subset_excludes_unchecked_tool.generate

Capture accepted dependencies without starting agents.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 613.

### test_unchecked_ineligible_candidate_does_not_block_valid_subset

An unapproved result cannot be selected but may be excluded from generation.

Kind: callable. Declared return: None. Source line: 630.

### test_blocked_acceptance_names_its_reason

A disabled accept button must explain why instead of failing silently.

Kind: callable. Declared return: None. Source line: 648.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | approved_tool | Imported dependency for approved tool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | registry | Imported dependency for registry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | AcceptedCandidates | Imported dependency for AcceptedCandidates in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | SelectedToolRegistry | Imported dependency for SelectedToolRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | GuiToolRetrieval | Imported dependency for GuiToolRetrieval in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | RetrieverHandle | Imported dependency for RetrieverHandle in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| match | tool | Local binding for tool in match; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| match | descriptor | Local binding for descriptor in match; use the enclosing contract and type below. | Return type of descriptor_from_source; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| RetrievalDouble | startup_message | Local binding for startup message in RetrievalDouble; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 32 |
| RetrievalDouble.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| RetrievalDouble.__init__ | self.calls | Attribute for calls in RetrievalDouble.__init__; use the enclosing contract and type below. | list[tuple[str, int]] | Enclosing invocation or class/instance lifetime | 36 |
| RetrievalDouble.search | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| RetrievalDouble.search | catalog | Parameter for catalog in RetrievalDouble.search; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 39 |
| RetrievalDouble.search | handle | Parameter for handle in RetrievalDouble.search; use the enclosing contract and type below. | RetrieverHandle | Enclosing invocation or class/instance lifetime | 39 |
| RetrievalDouble.search | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 39 |
| RetrievalDouble.search | limit | Parameter for limit in RetrievalDouble.search; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 39 |
| setup_backend | tmp_path | Parameter for tmp path in setup_backend; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 47 |
| setup_backend | sessions | Local binding for sessions in setup_backend; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| setup_backend | owner | Local binding for owner in setup_backend; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| setup_backend | owner.controller.security | Attribute for owner.controller.security in setup_backend; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| setup_backend | catalog | Local binding for catalog in setup_backend; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| setup_backend | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in setup_backend; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| setup_backend | tools | Local binding for tools in setup_backend; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 55 |
| setup_backend | retrieval | Local binding for retrieval in setup_backend; use the enclosing contract and type below. | Return type of RetrievalDouble; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| setup_backend | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| setup_backend.lambda_63 | controller | Callback parameter for controller in setup_backend.lambda_63; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 63 |
| setup_backend.lambda_64.lambda_64 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_selected_registry_supplies_exact_subset_and_rechecks | tool | Local binding for tool in test_selected_registry_supplies_exact_subset_and_rechecks; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_selected_registry_supplies_exact_subset_and_rechecks | values | Local binding for values in test_selected_registry_supplies_exact_subset_and_rechecks; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 72 |
| test_selected_registry_supplies_exact_subset_and_rechecks | selected | Local binding for selected in test_selected_registry_supplies_exact_subset_and_rechecks; use the enclosing contract and type below. | Return type of SelectedToolRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_search_does_not_generate_and_limit_is_forwarded | tmp_path | Parameter for tmp path in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 84 |
| test_search_does_not_generate_and_limit_is_forwarded | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_search_does_not_generate_and_limit_is_forwarded | owner | Local binding for owner in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_search_does_not_generate_and_limit_is_forwarded | request | Local binding for request in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_search_does_not_generate_and_limit_is_forwarded | tools | Local binding for tools in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_search_does_not_generate_and_limit_is_forwarded | retrieval | Local binding for retrieval in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_search_does_not_generate_and_limit_is_forwarded | view | Local binding for view in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_search_does_not_generate_and_limit_is_forwarded | token | Local binding for token in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_search_does_not_generate_and_limit_is_forwarded | refreshed | Local binding for refreshed in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_search_does_not_generate_and_limit_is_forwarded | _ | Local binding for  in test_search_does_not_generate_and_limit_is_forwarded; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_ineligible_candidate_names_portability_instead_of_approval | present_candidates | Imported dependency for present candidates in test_ineligible_candidate_names_portability_instead_of_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_ineligible_candidate_names_portability_instead_of_approval | CatalogDependencyError | Imported dependency for CatalogDependencyError in test_ineligible_candidate_names_portability_instead_of_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 99 |
| test_ineligible_candidate_names_portability_instead_of_approval | registry | Local binding for registry in test_ineligible_candidate_names_portability_instead_of_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_ineligible_candidate_names_portability_instead_of_approval | view | Local binding for view in test_ineligible_candidate_names_portability_instead_of_approval; use the enclosing contract and type below. | Return type of present_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_generate_without_name_reports_the_missing_name_before_search | tmp_path | Parameter for tmp path in test_generate_without_name_reports_the_missing_name_before_search; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 123 |
| test_generate_without_name_reports_the_missing_name_before_search | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_generate_without_name_reports_the_missing_name_before_search | owner | Local binding for owner in test_generate_without_name_reports_the_missing_name_before_search; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_generate_without_name_reports_the_missing_name_before_search | request | Local binding for request in test_generate_without_name_reports_the_missing_name_before_search; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_generate_without_name_reports_the_missing_name_before_search | _tools | Local binding for tools in test_generate_without_name_reports_the_missing_name_before_search; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_generate_without_name_reports_the_missing_name_before_search | retrieval | Local binding for retrieval in test_generate_without_name_reports_the_missing_name_before_search; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_acceptance_passes_only_server_snapshot | tmp_path | Parameter for tmp path in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 134 |
| test_acceptance_passes_only_server_snapshot | monkeypatch | Parameter for monkeypatch in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 134 |
| test_acceptance_passes_only_server_snapshot | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_acceptance_passes_only_server_snapshot | owner | Local binding for owner in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_acceptance_passes_only_server_snapshot | request | Local binding for request in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_acceptance_passes_only_server_snapshot | tools | Local binding for tools in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_acceptance_passes_only_server_snapshot | retrieval | Local binding for retrieval in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_acceptance_passes_only_server_snapshot | view | Local binding for view in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_acceptance_passes_only_server_snapshot | token | Local binding for token in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_acceptance_passes_only_server_snapshot | calls | Local binding for calls in test_acceptance_passes_only_server_snapshot; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 139 |
| test_acceptance_passes_only_server_snapshot.generate | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 142 |
| test_acceptance_passes_only_server_snapshot.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 143 |
| test_acceptance_passes_only_server_snapshot.generate | token | Parameter for token in test_acceptance_passes_only_server_snapshot.generate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 144 |
| test_acceptance_passes_only_server_snapshot.generate | request | Parameter for request in test_acceptance_passes_only_server_snapshot.generate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 145 |
| test_acceptance_passes_only_server_snapshot.generate | selected | Parameter for selected in test_acceptance_passes_only_server_snapshot.generate; use the enclosing contract and type below. | AcceptedCandidates &#124; None | Enclosing invocation or class/instance lifetime | 147 |
| test_changed_or_foreign_selection_cannot_generate | tmp_path | Parameter for tmp path in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 167 |
| test_changed_or_foreign_selection_cannot_generate | change | Parameter for change in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 167 |
| test_changed_or_foreign_selection_cannot_generate | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_changed_or_foreign_selection_cannot_generate | owner | Local binding for owner in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_changed_or_foreign_selection_cannot_generate | request | Local binding for request in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 169, 179 |
| test_changed_or_foreign_selection_cannot_generate | tools | Local binding for tools in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_changed_or_foreign_selection_cannot_generate | retrieval | Local binding for retrieval in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_changed_or_foreign_selection_cannot_generate | view | Local binding for view in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_changed_or_foreign_selection_cannot_generate | token | Local binding for token in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_changed_or_foreign_selection_cannot_generate | query | Original user request or a trusted test query; avoid payload logging by default. | tuple | Enclosing invocation or class/instance lifetime | 171, 173 |
| test_changed_or_foreign_selection_cannot_generate | limit | Local binding for limit in test_changed_or_foreign_selection_cannot_generate; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 171, 175 |
| test_startup_failure_is_retriable_and_clients_are_private | tmp_path | Parameter for tmp path in test_startup_failure_is_retriable_and_clients_are_private; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 185 |
| test_startup_failure_is_retriable_and_clients_are_private | calls | Local binding for calls in test_startup_failure_is_retriable_and_clients_are_private; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 187 |
| test_startup_failure_is_retriable_and_clients_are_private.factory | catalog | Parameter for catalog in test_startup_failure_is_retriable_and_clients_are_private.factory; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 189 |
| test_startup_failure_is_retriable_and_clients_are_private.factory.lambda_194 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 194 |
| test_startup_failure_is_retriable_and_clients_are_private.factory.lambda_194 | limit | Callback parameter for limit in test_startup_failure_is_retriable_and_clients_are_private.factory.lambda_194; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 194 |
| test_startup_failure_is_retriable_and_clients_are_private | service | Local binding for service in test_startup_failure_is_retriable_and_clients_are_private; use the enclosing contract and type below. | Return type of GuiToolRetrieval; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_startup_failure_is_retriable_and_clients_are_private | first | Local binding for first in test_startup_failure_is_retriable_and_clients_are_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 198 |
| test_startup_failure_is_retriable_and_clients_are_private | second | Local binding for second in test_startup_failure_is_retriable_and_clients_are_private; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 198 |
| test_candidate_logs_omit_description | tmp_path | Parameter for tmp path in test_candidate_logs_omit_description; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 204 |
| test_candidate_logs_omit_description | caplog | Parameter for caplog in test_candidate_logs_omit_description; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 204 |
| test_candidate_logs_omit_description | logging | Imported dependency for logging in test_candidate_logs_omit_description; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 206 |
| test_candidate_logs_omit_description | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_candidate_logs_omit_description | owner | Local binding for owner in test_candidate_logs_omit_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_candidate_logs_omit_description | request | Local binding for request in test_candidate_logs_omit_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_candidate_logs_omit_description | tools | Local binding for tools in test_candidate_logs_omit_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_candidate_logs_omit_description | retrieval | Local binding for retrieval in test_candidate_logs_omit_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_retrieval_handle_transition_is_correlated_and_payload_free | tmp_path | Parameter for tmp path in test_retrieval_handle_transition_is_correlated_and_payload_free; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 217 |
| test_retrieval_handle_transition_is_correlated_and_payload_free | caplog | Parameter for caplog in test_retrieval_handle_transition_is_correlated_and_payload_free; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 217 |
| test_retrieval_handle_transition_is_correlated_and_payload_free | operation_scope | Imported dependency for operation scope in test_retrieval_handle_transition_is_correlated_and_payload_free; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 220 |
| test_retrieval_handle_transition_is_correlated_and_payload_free | service | Local binding for service in test_retrieval_handle_transition_is_correlated_and_payload_free; use the enclosing contract and type below. | Return type of GuiToolRetrieval; see its callable contract | Enclosing invocation or class/instance lifetime | 222 |
| test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223 | _catalog | Callback parameter for catalog in test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 223 |
| test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223.lambda_223 | _query | Callback parameter for query in test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223.lambda_223; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 223 |
| test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223.lambda_223 | limit | Callback parameter for limit in test_retrieval_handle_transition_is_correlated_and_payload_free.lambda_223.lambda_223; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 223 |
| test_selected_registry_preserves_legacy_role_keys | tool | Local binding for tool in test_selected_registry_preserves_legacy_role_keys; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 236 |
| test_selected_registry_preserves_legacy_role_keys | selected | Local binding for selected in test_selected_registry_preserves_legacy_role_keys; use the enclosing contract and type below. | Return type of SelectedToolRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 237 |
| test_real_generation_boundary_receives_only_candidates | tmp_path | Parameter for tmp path in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 245 |
| test_real_generation_boundary_receives_only_candidates | monkeypatch | Parameter for monkeypatch in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 245 |
| test_real_generation_boundary_receives_only_candidates | candidate | Imported dependency for candidate in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 248 |
| test_real_generation_boundary_receives_only_candidates | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_real_generation_boundary_receives_only_candidates | owner | Local binding for owner in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_real_generation_boundary_receives_only_candidates | request | Local binding for request in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_real_generation_boundary_receives_only_candidates | tools | Local binding for tools in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_real_generation_boundary_receives_only_candidates | retrieval | Local binding for retrieval in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| test_real_generation_boundary_receives_only_candidates | item | Local binding for item in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_real_generation_boundary_receives_only_candidates | item.review_text | Attribute for item.review text in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 252 |
| test_real_generation_boundary_receives_only_candidates | calls | Local binding for calls in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 253 |
| test_real_generation_boundary_receives_only_candidates.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 255 |
| test_real_generation_boundary_receives_only_candidates.generate | tools | Parameter for tools in test_real_generation_boundary_receives_only_candidates.generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 255 |
| test_real_generation_boundary_receives_only_candidates | backend.pipeline_factory | Attribute for backend.pipeline factory in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 260 |
| test_real_generation_boundary_receives_only_candidates.lambda_260 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 260 |
| test_real_generation_boundary_receives_only_candidates | view | Local binding for view in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 261 |
| test_real_generation_boundary_receives_only_candidates | token | Local binding for token in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 261 |
| test_real_generation_boundary_receives_only_candidates | rows | Local binding for rows in test_real_generation_boundary_receives_only_candidates; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_candidate_labels_preserve_metadata_as_plain_text | candidate_choices | Imported dependency for candidate choices in test_candidate_labels_preserve_metadata_as_plain_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 272 |
| test_candidate_labels_preserve_metadata_as_plain_text | choices | Local binding for choices in test_candidate_labels_preserve_metadata_as_plain_text; use the enclosing contract and type below. | Return type of candidate_choices; see its callable contract | Enclosing invocation or class/instance lifetime | 274 |
| test_obsolete_search_does_not_replace_newer_description | tmp_path | Parameter for tmp path in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 281 |
| test_obsolete_search_does_not_replace_newer_description | failure | Parameter for failure in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 281 |
| test_obsolete_search_does_not_replace_newer_description | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_obsolete_search_does_not_replace_newer_description | owner | Local binding for owner in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_obsolete_search_does_not_replace_newer_description | request | Local binding for request in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_obsolete_search_does_not_replace_newer_description | tools | Local binding for tools in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_obsolete_search_does_not_replace_newer_description | retrieval | Local binding for retrieval in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_obsolete_search_does_not_replace_newer_description.slow | catalog | Parameter for catalog in test_obsolete_search_does_not_replace_newer_description.slow; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 286 |
| test_obsolete_search_does_not_replace_newer_description.slow | handle | Parameter for handle in test_obsolete_search_does_not_replace_newer_description.slow; use the enclosing contract and type below. | RetrieverHandle | Enclosing invocation or class/instance lifetime | 286 |
| test_obsolete_search_does_not_replace_newer_description.slow | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 286 |
| test_obsolete_search_does_not_replace_newer_description.slow | limit | Parameter for limit in test_obsolete_search_does_not_replace_newer_description.slow; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 286 |
| test_obsolete_search_does_not_replace_newer_description | retrieval.search | Attribute for retrieval.search in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 294 |
| test_obsolete_search_does_not_replace_newer_description | view | Local binding for view in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 295 |
| test_obsolete_search_does_not_replace_newer_description | token | Local binding for token in test_obsolete_search_does_not_replace_newer_description; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 295 |
| test_real_gradio_candidate_callback_contract | tmp_path | Parameter for tmp path in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 301 |
| test_real_gradio_candidate_callback_contract | gr | Imported dependency for gr in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 303 |
| test_real_gradio_candidate_callback_contract | build_view | Imported dependency for build view in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 305 |
| test_real_gradio_candidate_callback_contract | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_candidate_callback_contract | owner | Local binding for owner in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_candidate_callback_contract | request | Local binding for request in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_candidate_callback_contract | tools | Local binding for tools in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_candidate_callback_contract | retrieval | Local binding for retrieval in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| test_real_gradio_candidate_callback_contract | demo | Local binding for demo in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 308 |
| test_real_gradio_candidate_callback_contract | callback | Local binding for callback in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 309 |
| test_real_gradio_candidate_callback_contract.comprehension_309 | item | Comprehension item for item in test_real_gradio_candidate_callback_contract.comprehension_309; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 310 |
| test_real_gradio_candidate_callback_contract | rows | Local binding for rows in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 312 |
| test_real_gradio_candidate_callback_contract | controls | Local binding for controls in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 315 |
| test_real_gradio_candidate_callback_contract.comprehension_315 | item | Comprehension item for item in test_real_gradio_candidate_callback_contract.comprehension_315; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 315 |
| test_real_gradio_candidate_callback_contract | number | Local binding for number in test_real_gradio_candidate_callback_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 316 |
| test_real_gradio_accept_label_explains_a_blocked_selection | tmp_path | Parameter for tmp path in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 323 |
| test_real_gradio_accept_label_explains_a_blocked_selection | monkeypatch | Parameter for monkeypatch in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 323 |
| test_real_gradio_accept_label_explains_a_blocked_selection | gr | Imported dependency for gr in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 326 |
| test_real_gradio_accept_label_explains_a_blocked_selection | build_view | Imported dependency for build view in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 328 |
| test_real_gradio_accept_label_explains_a_blocked_selection | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| test_real_gradio_accept_label_explains_a_blocked_selection | owner | Local binding for owner in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| test_real_gradio_accept_label_explains_a_blocked_selection | request | Local binding for request in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| test_real_gradio_accept_label_explains_a_blocked_selection | tools | Local binding for tools in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| test_real_gradio_accept_label_explains_a_blocked_selection | retrieval | Local binding for retrieval in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| test_real_gradio_accept_label_explains_a_blocked_selection | bad | Local binding for bad in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 331 |
| test_real_gradio_accept_label_explains_a_blocked_selection | view | Local binding for view in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 333 |
| test_real_gradio_accept_label_explains_a_blocked_selection | token | Local binding for token in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 333 |
| test_real_gradio_accept_label_explains_a_blocked_selection | demo | Local binding for demo in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 334 |
| test_real_gradio_accept_label_explains_a_blocked_selection | callback | Local binding for callback in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| test_real_gradio_accept_label_explains_a_blocked_selection.comprehension_335 | item | Comprehension item for item in test_real_gradio_accept_label_explains_a_blocked_selection.comprehension_335; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 336 |
| test_real_gradio_accept_label_explains_a_blocked_selection | blocked | Local binding for blocked in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of fn; see its callable contract | Enclosing invocation or class/instance lifetime | 338 |
| test_real_gradio_accept_label_explains_a_blocked_selection | allowed | Local binding for allowed in test_real_gradio_accept_label_explains_a_blocked_selection; use the enclosing contract and type below. | Return type of fn; see its callable contract | Enclosing invocation or class/instance lifetime | 343 |
| test_bootstrap_initializes_retrieval_once_before_view | tmp_path | Parameter for tmp path in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 349 |
| test_bootstrap_initializes_retrieval_once_before_view | monkeypatch | Parameter for monkeypatch in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 349 |
| test_bootstrap_initializes_retrieval_once_before_view | sys | Imported dependency for sys in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 352 |
| test_bootstrap_initializes_retrieval_once_before_view | ModuleType | Imported dependency for ModuleType in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 353 |
| test_bootstrap_initializes_retrieval_once_before_view | bootstrap | Imported dependency for bootstrap in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 355 |
| test_bootstrap_initializes_retrieval_once_before_view | Settings | Imported dependency for Settings in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 356 |
| test_bootstrap_initializes_retrieval_once_before_view | events | Local binding for events in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 358 |
| test_bootstrap_initializes_retrieval_once_before_view | catalog | Local binding for catalog in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 359 |
| test_bootstrap_initializes_retrieval_once_before_view | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 360 |
| test_bootstrap_initializes_retrieval_once_before_view.lambda_363 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 363 |
| test_bootstrap_initializes_retrieval_once_before_view.Startup.initialize | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 371 |
| test_bootstrap_initializes_retrieval_once_before_view.Startup.initialize | actual_catalog | Parameter for actual catalog in test_bootstrap_initializes_retrieval_once_before_view.Startup.initialize; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 371 |
| test_bootstrap_initializes_retrieval_once_before_view | service | Local binding for service in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Return type of Startup; see its callable contract | Enclosing invocation or class/instance lifetime | 375 |
| test_bootstrap_initializes_retrieval_once_before_view | gr | Local binding for gr in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Return type of ModuleType; see its callable contract | Enclosing invocation or class/instance lifetime | 382 |
| test_bootstrap_initializes_retrieval_once_before_view | gr.update | Attribute for gr.update in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 383 |
| test_bootstrap_initializes_retrieval_once_before_view.build | sessions | Parameter for sessions in test_bootstrap_initializes_retrieval_once_before_view.build; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 386 |
| test_bootstrap_initializes_retrieval_once_before_view.build | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 386 |
| test_bootstrap_initializes_retrieval_once_before_view | first | Local binding for first in test_bootstrap_initializes_retrieval_once_before_view; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 396 |
| test_retrieval_serializes_owner_index_operations | tmp_path | Parameter for tmp path in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 403 |
| test_retrieval_serializes_owner_index_operations | ThreadPoolExecutor | Imported dependency for ThreadPoolExecutor in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 405 |
| test_retrieval_serializes_owner_index_operations | Event | Imported dependency for Event in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 406 |
| test_retrieval_serializes_owner_index_operations | entered | Local binding for entered in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 408 |
| test_retrieval_serializes_owner_index_operations | release | Local binding for release in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 408 |
| test_retrieval_serializes_owner_index_operations | sequence | Local binding for sequence in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 409 |
| test_retrieval_serializes_owner_index_operations.Client.search | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 414 |
| test_retrieval_serializes_owner_index_operations.Client.search | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 414 |
| test_retrieval_serializes_owner_index_operations.Client.search | limit | Parameter for limit in test_retrieval_serializes_owner_index_operations.Client.search; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 414 |
| test_retrieval_serializes_owner_index_operations | service | Local binding for service in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Return type of GuiToolRetrieval; see its callable contract | Enclosing invocation or class/instance lifetime | 423 |
| test_retrieval_serializes_owner_index_operations.lambda_423 | catalog | Callback parameter for catalog in test_retrieval_serializes_owner_index_operations.lambda_423; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 423 |
| test_retrieval_serializes_owner_index_operations | catalog | Local binding for catalog in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 424 |
| test_retrieval_serializes_owner_index_operations | pool | Managed resource for pool in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Return type of ThreadPoolExecutor; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 425 |
| test_retrieval_serializes_owner_index_operations | first | Local binding for first in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Return type of submit; see its callable contract | Enclosing invocation or class/instance lifetime | 426 |
| test_retrieval_serializes_owner_index_operations | second | Local binding for second in test_retrieval_serializes_owner_index_operations; use the enclosing contract and type below. | Return type of submit; see its callable contract | Enclosing invocation or class/instance lifetime | 428 |
| test_acceptance_storage_failure_is_safe_and_logged | tmp_path | Parameter for tmp path in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 443 |
| test_acceptance_storage_failure_is_safe_and_logged | caplog | Parameter for caplog in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 443 |
| test_acceptance_storage_failure_is_safe_and_logged | logging | Imported dependency for logging in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 446 |
| test_acceptance_storage_failure_is_safe_and_logged | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_acceptance_storage_failure_is_safe_and_logged | owner | Local binding for owner in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_acceptance_storage_failure_is_safe_and_logged | request | Local binding for request in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_acceptance_storage_failure_is_safe_and_logged | tools | Local binding for tools in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_acceptance_storage_failure_is_safe_and_logged | retrieval | Local binding for retrieval in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| test_acceptance_storage_failure_is_safe_and_logged | view | Local binding for view in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 449 |
| test_acceptance_storage_failure_is_safe_and_logged | token | Local binding for token in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 449 |
| test_acceptance_storage_failure_is_safe_and_logged | backend.registry_factory | Attribute for backend.registry factory in test_acceptance_storage_failure_is_safe_and_logged; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 455 |
| test_acceptance_storage_failure_is_safe_and_logged.lambda_455 | controller | Callback parameter for controller in test_acceptance_storage_failure_is_safe_and_logged.lambda_455; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 455 |
| test_closed_owner_discards_inflight_candidate_result | tmp_path | Parameter for tmp path in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 464 |
| test_closed_owner_discards_inflight_candidate_result | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 466 |
| test_closed_owner_discards_inflight_candidate_result | owner | Local binding for owner in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 466 |
| test_closed_owner_discards_inflight_candidate_result | request | Local binding for request in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 466 |
| test_closed_owner_discards_inflight_candidate_result | tools | Local binding for tools in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 466 |
| test_closed_owner_discards_inflight_candidate_result | retrieval | Local binding for retrieval in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 466 |
| test_closed_owner_discards_inflight_candidate_result.closing | catalog | Parameter for catalog in test_closed_owner_discards_inflight_candidate_result.closing; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 469 |
| test_closed_owner_discards_inflight_candidate_result.closing | handle | Parameter for handle in test_closed_owner_discards_inflight_candidate_result.closing; use the enclosing contract and type below. | RetrieverHandle | Enclosing invocation or class/instance lifetime | 469 |
| test_closed_owner_discards_inflight_candidate_result.closing | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 469 |
| test_closed_owner_discards_inflight_candidate_result.closing | limit | Parameter for limit in test_closed_owner_discards_inflight_candidate_result.closing; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 469 |
| test_closed_owner_discards_inflight_candidate_result | retrieval.search | Attribute for retrieval.search in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 475 |
| test_closed_owner_discards_inflight_candidate_result | view | Local binding for view in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 476 |
| test_closed_owner_discards_inflight_candidate_result | token | Local binding for token in test_closed_owner_discards_inflight_candidate_result; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 476 |
| test_repair_keeps_accepted_scope_and_rechecks_source | tmp_path | Parameter for tmp path in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 482 |
| test_repair_keeps_accepted_scope_and_rechecks_source | changed | Parameter for changed in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 482 |
| test_repair_keeps_accepted_scope_and_rechecks_source | json | Imported dependency for json in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 484 |
| test_repair_keeps_accepted_scope_and_rechecks_source | candidate | Imported dependency for candidate in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 486 |
| test_repair_keeps_accepted_scope_and_rechecks_source | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| test_repair_keeps_accepted_scope_and_rechecks_source | owner | Local binding for owner in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| test_repair_keeps_accepted_scope_and_rechecks_source | request | Local binding for request in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| test_repair_keeps_accepted_scope_and_rechecks_source | tools | Local binding for tools in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| test_repair_keeps_accepted_scope_and_rechecks_source | retrieval | Local binding for retrieval in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| test_repair_keeps_accepted_scope_and_rechecks_source | item | Local binding for item in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 489 |
| test_repair_keeps_accepted_scope_and_rechecks_source | item.review_text | Attribute for item.review text in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 490 |
| test_repair_keeps_accepted_scope_and_rechecks_source | calls | Local binding for calls in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 491 |
| test_repair_keeps_accepted_scope_and_rechecks_source.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 493 |
| test_repair_keeps_accepted_scope_and_rechecks_source.generate | tools | Parameter for tools in test_repair_keeps_accepted_scope_and_rechecks_source.generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 493 |
| test_repair_keeps_accepted_scope_and_rechecks_source.generate | feedback | Parameter for feedback in test_repair_keeps_accepted_scope_and_rechecks_source.generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 493 |
| test_repair_keeps_accepted_scope_and_rechecks_source | backend.pipeline_factory | Attribute for backend.pipeline factory in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 498 |
| test_repair_keeps_accepted_scope_and_rechecks_source.lambda_498 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 498 |
| test_repair_keeps_accepted_scope_and_rechecks_source | view | Local binding for view in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 499 |
| test_repair_keeps_accepted_scope_and_rechecks_source | token | Local binding for token in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 499 |
| test_repair_keeps_accepted_scope_and_rechecks_source | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 505 |
| test_repair_keeps_accepted_scope_and_rechecks_source | state.repair_allowed | Attribute for state.repair allowed in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 506 |
| test_repair_keeps_accepted_scope_and_rechecks_source | owner.controller.state.application_review_pending | Attribute for owner.controller.state.application review pending in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 507 |
| test_repair_keeps_accepted_scope_and_rechecks_source | rows | Local binding for rows in test_repair_keeps_accepted_scope_and_rechecks_source; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 510 |
| test_repair_keeps_accepted_scope_and_rechecks_source.comprehension_516 | query | Original user request or a trusted test query; avoid payload logging by default. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 516 |
| test_repair_keeps_accepted_scope_and_rechecks_source.comprehension_516 | names | Comprehension item for names in test_repair_keeps_accepted_scope_and_rechecks_source.comprehension_516; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 516 |
| test_repair_keeps_accepted_scope_and_rechecks_source.comprehension_516 | _ | Comprehension item for  in test_repair_keeps_accepted_scope_and_rechecks_source.comprehension_516; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 516 |
| test_reviewed_tool_revision_invalidates_candidate_application | tmp_path | Parameter for tmp path in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 520 |
| test_reviewed_tool_revision_invalidates_candidate_application | json | Imported dependency for json in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 522 |
| test_reviewed_tool_revision_invalidates_candidate_application | candidate | Imported dependency for candidate in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 524 |
| test_reviewed_tool_revision_invalidates_candidate_application | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_reviewed_tool_revision_invalidates_candidate_application | owner | Local binding for owner in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_reviewed_tool_revision_invalidates_candidate_application | request | Local binding for request in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_reviewed_tool_revision_invalidates_candidate_application | tools | Local binding for tools in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_reviewed_tool_revision_invalidates_candidate_application | retrieval | Local binding for retrieval in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_reviewed_tool_revision_invalidates_candidate_application | item | Local binding for item in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 527 |
| test_reviewed_tool_revision_invalidates_candidate_application | item.review_text | Attribute for item.review text in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 528, 544 |
| test_reviewed_tool_revision_invalidates_candidate_application | backend.pipeline_factory | Attribute for backend.pipeline factory in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 529 |
| test_reviewed_tool_revision_invalidates_candidate_application.lambda_529 | root | Explicit root directory against which named paths are resolved. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 529 |
| test_reviewed_tool_revision_invalidates_candidate_application.lambda_529.lambda_529 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 529 |
| test_reviewed_tool_revision_invalidates_candidate_application | view | Local binding for view in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 530 |
| test_reviewed_tool_revision_invalidates_candidate_application | token | Local binding for token in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 530 |
| test_reviewed_tool_revision_invalidates_candidate_application | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 532 |
| test_reviewed_tool_revision_invalidates_candidate_application | owner.controller.tool_operations | Attribute for owner.controller.tool operations in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 557 |
| test_reviewed_tool_revision_invalidates_candidate_application | rows | Local binding for rows in test_reviewed_tool_revision_invalidates_candidate_application; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 563 |
| test_busy_invalidation_is_logged_as_ignored | tmp_path | Parameter for tmp path in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 571 |
| test_busy_invalidation_is_logged_as_ignored | caplog | Parameter for caplog in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 571 |
| test_busy_invalidation_is_logged_as_ignored | logging | Imported dependency for logging in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 574 |
| test_busy_invalidation_is_logged_as_ignored | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 576 |
| test_busy_invalidation_is_logged_as_ignored | owner | Local binding for owner in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 576 |
| test_busy_invalidation_is_logged_as_ignored | request | Local binding for request in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 576 |
| test_busy_invalidation_is_logged_as_ignored | tools | Local binding for tools in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 576 |
| test_busy_invalidation_is_logged_as_ignored | retrieval | Local binding for retrieval in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 576 |
| test_busy_invalidation_is_logged_as_ignored | view | Local binding for view in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 577 |
| test_busy_invalidation_is_logged_as_ignored | token | Local binding for token in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 577 |
| test_busy_invalidation_is_logged_as_ignored | owner.controller.state.application_busy | Attribute for owner.controller.state.application busy in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 578 |
| test_busy_invalidation_is_logged_as_ignored | owner.controller.state.application_phase | Attribute for owner.controller.state.application phase in test_busy_invalidation_is_logged_as_ignored; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 579 |
| test_candidate_subset_rejects_invalid_ids | tmp_path | Parameter for tmp path in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 588 |
| test_candidate_subset_rejects_invalid_ids | chosen | Parameter for chosen in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 588 |
| test_candidate_subset_rejects_invalid_ids | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 590 |
| test_candidate_subset_rejects_invalid_ids | owner | Local binding for owner in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 590 |
| test_candidate_subset_rejects_invalid_ids | request | Local binding for request in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 590 |
| test_candidate_subset_rejects_invalid_ids | tools | Local binding for tools in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 590 |
| test_candidate_subset_rejects_invalid_ids | retrieval | Local binding for retrieval in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 590 |
| test_candidate_subset_rejects_invalid_ids | view | Local binding for view in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 591 |
| test_candidate_subset_rejects_invalid_ids | token | Local binding for token in test_candidate_subset_rejects_invalid_ids; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 591 |
| test_candidate_subset_excludes_unchecked_tool | tmp_path | Parameter for tmp path in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 602 |
| test_candidate_subset_excludes_unchecked_tool | monkeypatch | Parameter for monkeypatch in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 602 |
| test_candidate_subset_excludes_unchecked_tool | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_candidate_subset_excludes_unchecked_tool | owner | Local binding for owner in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_candidate_subset_excludes_unchecked_tool | request | Local binding for request in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_candidate_subset_excludes_unchecked_tool | tools | Local binding for tools in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_candidate_subset_excludes_unchecked_tool | retrieval | Local binding for retrieval in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| test_candidate_subset_excludes_unchecked_tool | extra | Local binding for extra in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 606 |
| test_candidate_subset_excludes_unchecked_tool | view | Local binding for view in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 610 |
| test_candidate_subset_excludes_unchecked_tool | token | Local binding for token in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 610 |
| test_candidate_subset_excludes_unchecked_tool | captured | Local binding for captured in test_candidate_subset_excludes_unchecked_tool; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 611 |
| test_candidate_subset_excludes_unchecked_tool.generate | selected | Parameter for selected in test_candidate_subset_excludes_unchecked_tool.generate; use the enclosing contract and type below. | AcceptedCandidates | Enclosing invocation or class/instance lifetime | 614 |
| test_candidate_subset_excludes_unchecked_tool.generate | args | Parameter for args in test_candidate_subset_excludes_unchecked_tool.generate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 614 |
| test_candidate_subset_excludes_unchecked_tool.generate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 614 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | tmp_path | Parameter for tmp path in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 631 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | monkeypatch | Parameter for monkeypatch in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 631 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 634 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | owner | Local binding for owner in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 634 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | request | Local binding for request in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 634 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | tools | Local binding for tools in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 634 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | retrieval | Local binding for retrieval in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 634 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | bad | Local binding for bad in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 635 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | view | Local binding for view in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 637 |
| test_unchecked_ineligible_candidate_does_not_block_valid_subset | token | Local binding for token in test_unchecked_ineligible_candidate_does_not_block_valid_subset; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 637 |
| test_blocked_acceptance_names_its_reason | tmp_path | Parameter for tmp path in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 649 |
| test_blocked_acceptance_names_its_reason | monkeypatch | Parameter for monkeypatch in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 649 |
| test_blocked_acceptance_names_its_reason | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 652 |
| test_blocked_acceptance_names_its_reason | owner | Local binding for owner in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 652 |
| test_blocked_acceptance_names_its_reason | request | Local binding for request in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 652 |
| test_blocked_acceptance_names_its_reason | tools | Local binding for tools in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 652 |
| test_blocked_acceptance_names_its_reason | retrieval | Local binding for retrieval in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of setup_backend; see its callable contract | Enclosing invocation or class/instance lifetime | 652 |
| test_blocked_acceptance_names_its_reason | bad | Local binding for bad in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 653 |
| test_blocked_acceptance_names_its_reason | view | Local binding for view in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 655 |
| test_blocked_acceptance_names_its_reason | token | Local binding for token in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 655 |
| test_blocked_acceptance_names_its_reason | idle | Local binding for idle in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 656 |
| test_blocked_acceptance_names_its_reason | ready | Local binding for ready in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 656 |
| test_blocked_acceptance_names_its_reason | owned | Local binding for owned in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 656 |
| test_blocked_acceptance_names_its_reason | reason | Local binding for reason in test_blocked_acceptance_names_its_reason; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 656 |
