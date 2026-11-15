# Reference for tests/test_retrieval_catalog.py

Exercise authoritative catalog synchronization using trusted temporary sources.

Source fingerprint: 115a8592043d81339c61fc4c62a972a550f4ead0f85e95aa1bb4d1498b64fed2

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### write_tool

Write a trusted source fixture which must only ever be parsed, never executed.

Kind: callable. Declared return: Path. Source line: 12.

### CountingEmbeddings

Count embeddings to distinguish incremental synchronization from full rebuilds.

Kind: class. Declared return: Not declared / class. Source line: 25.

### CountingEmbeddings.__init__

Start with no inference requests.

Kind: callable. Declared return: None. Source line: 28.

### CountingEmbeddings.embed

Count actual batches and delegate deterministic vectors.

Kind: callable. Declared return: list[list[float]]. Source line: 32.

### bound_retriever

Bind exactly the ToolCatalog root used by a GUI runtime.

Kind: callable. Declared return: ToolRetriever. Source line: 38.

### test_initial_load_and_unchanged_sync

Load on binding, then skip embeddings for unchanged descriptors.

Kind: callable. Declared return: None. Source line: 50.

### test_search_reflects_add_modify_delete

Refresh additions, content changes and deleted source files before querying.

Kind: callable. Declared return: None. Source line: 65.

### test_invalid_modified_source_removes_stale_entry

A tool that stops parsing cannot retain its old searchable descriptor.

Kind: callable. Declared return: None. Source line: 87.

### test_missing_root_is_failure_not_empty_snapshot

An unavailable root never wipes an index or silently serves stale results.

Kind: callable. Declared return: None. Source line: 98.

### test_source_binding_survives_reopen

Reopening preserves synchronization and rejects unrelated or unbound access.

Kind: callable. Declared return: None. Source line: 112.

### test_hardlinked_tool_source_rejected

Reject source aliases without reading outside the catalog boundary.

Kind: callable. Declared return: None. Source line: 127.

### test_embedding_failure_blocks_search_and_retries

Failed synchronization cannot return old matches; a later attempt recovers.

Kind: callable. Declared return: None. Source line: 138.

### test_embedding_failure_blocks_search_and_retries.fail

Simulate an explicit unavailable embedding boundary.

Kind: callable. Declared return: list[list[float]]. Source line: 147.

### test_same_size_and_mtime_change_is_detected

Use source content identity rather than trusting timestamps and file sizes.

Kind: callable. Declared return: None. Source line: 159.

### test_deleted_directory_is_removed

Remove a whole tool directory from results on the next search.

Kind: callable. Declared return: None. Source line: 174.

### test_reject_oversized_and_noncanonical_sources

Report unsafe resource sizes and unsupported canonical contracts explicitly.

Kind: callable. Declared return: None. Source line: 185.

### test_nonempty_manual_index_is_not_adopted

Do not silently prune unrelated manually indexed tools when binding a catalog.

Kind: callable. Declared return: None. Source line: 199.

### test_cli_uses_gui_settings_root

Resolve the source from the same Settings field as GUI runtime composition.

Kind: callable. Declared return: None. Source line: 212.

### test_bound_catalog_root_cannot_change_silently

Reject a redirected catalog object instead of pruning the originally bound index.

Kind: callable. Declared return: None. Source line: 236.

### test_catalog_stage_durations_are_measured

Measure both the complete catalog scan and index reconciliation stages.

Kind: callable. Declared return: None. Source line: 254.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | FakeEmbeddings | Imported dependency for FakeEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | FakeKeywords | Imported dependency for FakeKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | CatalogToolSource | Imported dependency for CatalogToolSource in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| write_tool | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 12 |
| write_tool | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 12 |
| write_tool | description | Parameter for description in write_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 12 |
| write_tool | folder | Local binding for folder in write_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 14 |
| write_tool | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 16 |
| CountingEmbeddings.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| CountingEmbeddings.__init__ | self.calls | Attribute for calls in CountingEmbeddings.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 30 |
| CountingEmbeddings.embed | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| CountingEmbeddings.embed | texts | Parameter for texts in CountingEmbeddings.embed; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 32 |
| CountingEmbeddings.embed | self.calls | Attribute for calls in CountingEmbeddings.embed; use the enclosing contract and type below. | Preserved or operator-dependent type | Enclosing invocation or class/instance lifetime | 34 |
| bound_retriever | tmp_path | Parameter for tmp path in bound_retriever; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 39 |
| bound_retriever | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 39 |
| bound_retriever | provider | Parameter for provider in bound_retriever; use the enclosing contract and type below. | CountingEmbeddings &#124; None | Enclosing invocation or class/instance lifetime | 39 |
| test_initial_load_and_unchanged_sync | tmp_path | Parameter for tmp path in test_initial_load_and_unchanged_sync; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 50 |
| test_initial_load_and_unchanged_sync | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_initial_load_and_unchanged_sync | provider | Local binding for provider in test_initial_load_and_unchanged_sync; use the enclosing contract and type below. | Return type of CountingEmbeddings; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_initial_load_and_unchanged_sync | service | Local binding for service in test_initial_load_and_unchanged_sync; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_initial_load_and_unchanged_sync | report | Local binding for report in test_initial_load_and_unchanged_sync; use the enclosing contract and type below. | Return type of synchronize; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_search_reflects_add_modify_delete | tmp_path | Parameter for tmp path in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 65 |
| test_search_reflects_add_modify_delete | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_search_reflects_add_modify_delete | first | Local binding for first in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_search_reflects_add_modify_delete | service | Local binding for service in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_search_reflects_add_modify_delete | original | Local binding for original in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_search_reflects_add_modify_delete | changed | Local binding for changed in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_search_reflects_add_modify_delete | second | Local binding for second in test_search_reflects_add_modify_delete; use the enclosing contract and type below. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_search_reflects_add_modify_delete.comprehension_80 | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 80 |
| test_invalid_modified_source_removes_stale_entry | tmp_path | Parameter for tmp path in test_invalid_modified_source_removes_stale_entry; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 87 |
| test_invalid_modified_source_removes_stale_entry | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_invalid_modified_source_removes_stale_entry | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_invalid_modified_source_removes_stale_entry | service | Local binding for service in test_invalid_modified_source_removes_stale_entry; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_missing_root_is_failure_not_empty_snapshot | tmp_path | Parameter for tmp path in test_missing_root_is_failure_not_empty_snapshot; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 98 |
| test_missing_root_is_failure_not_empty_snapshot | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_missing_root_is_failure_not_empty_snapshot | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_missing_root_is_failure_not_empty_snapshot | service | Local binding for service in test_missing_root_is_failure_not_empty_snapshot; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_missing_root_is_failure_not_empty_snapshot | moved | Local binding for moved in test_missing_root_is_failure_not_empty_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_source_binding_survives_reopen | tmp_path | Parameter for tmp path in test_source_binding_survives_reopen; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 112 |
| test_source_binding_survives_reopen | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_source_binding_survives_reopen | reopened | Local binding for reopened in test_source_binding_survives_reopen; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_source_binding_survives_reopen | other | Local binding for other in test_source_binding_survives_reopen; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_hardlinked_tool_source_rejected | tmp_path | Parameter for tmp path in test_hardlinked_tool_source_rejected; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 127 |
| test_hardlinked_tool_source_rejected | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_hardlinked_tool_source_rejected | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_hardlinked_tool_source_rejected | outside | Local binding for outside in test_hardlinked_tool_source_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_hardlinked_tool_source_rejected | service | Local binding for service in test_hardlinked_tool_source_rejected; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| test_embedding_failure_blocks_search_and_retries | tmp_path | Parameter for tmp path in test_embedding_failure_blocks_search_and_retries; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 138 |
| test_embedding_failure_blocks_search_and_retries | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 140 |
| test_embedding_failure_blocks_search_and_retries | provider | Local binding for provider in test_embedding_failure_blocks_search_and_retries; use the enclosing contract and type below. | Return type of CountingEmbeddings; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_embedding_failure_blocks_search_and_retries | service | Local binding for service in test_embedding_failure_blocks_search_and_retries; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| test_embedding_failure_blocks_search_and_retries | original | Local binding for original in test_embedding_failure_blocks_search_and_retries; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 145 |
| test_embedding_failure_blocks_search_and_retries.fail | texts | Parameter for texts in test_embedding_failure_blocks_search_and_retries.fail; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 147 |
| test_embedding_failure_blocks_search_and_retries | provider.embed | Attribute for provider.embed in test_embedding_failure_blocks_search_and_retries; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 151, 154 |
| test_same_size_and_mtime_change_is_detected | tmp_path | Parameter for tmp path in test_same_size_and_mtime_change_is_detected; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 159 |
| test_same_size_and_mtime_change_is_detected | os | Imported dependency for os in test_same_size_and_mtime_change_is_detected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 161 |
| test_same_size_and_mtime_change_is_detected | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_same_size_and_mtime_change_is_detected | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_same_size_and_mtime_change_is_detected | service | Local binding for service in test_same_size_and_mtime_change_is_detected; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_same_size_and_mtime_change_is_detected | before | Local binding for before in test_same_size_and_mtime_change_is_detected; use the enclosing contract and type below. | Return type of stat; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_deleted_directory_is_removed | tmp_path | Parameter for tmp path in test_deleted_directory_is_removed; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 174 |
| test_deleted_directory_is_removed | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_deleted_directory_is_removed | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_deleted_directory_is_removed | service | Local binding for service in test_deleted_directory_is_removed; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| test_reject_oversized_and_noncanonical_sources | tmp_path | Parameter for tmp path in test_reject_oversized_and_noncanonical_sources; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 185 |
| test_reject_oversized_and_noncanonical_sources | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_reject_oversized_and_noncanonical_sources | source | Explicit source document or source-code text; never imported for reference generation. | Return type of write_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| test_reject_oversized_and_noncanonical_sources | service | Local binding for service in test_reject_oversized_and_noncanonical_sources; use the enclosing contract and type below. | Return type of bound_retriever; see its callable contract | Enclosing invocation or class/instance lifetime | 191 |
| test_reject_oversized_and_noncanonical_sources.comprehension_192 | entry | Comprehension item for entry in test_reject_oversized_and_noncanonical_sources.comprehension_192; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 192 |
| test_nonempty_manual_index_is_not_adopted | tmp_path | Parameter for tmp path in test_nonempty_manual_index_is_not_adopted; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 199 |
| test_nonempty_manual_index_is_not_adopted | descriptor | Imported dependency for descriptor in test_nonempty_manual_index_is_not_adopted; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 201 |
| test_nonempty_manual_index_is_not_adopted | manual | Local binding for manual in test_nonempty_manual_index_is_not_adopted; use the enclosing contract and type below. | Return type of ToolRetriever; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_nonempty_manual_index_is_not_adopted | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_cli_uses_gui_settings_root | tmp_path | Parameter for tmp path in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 213 |
| test_cli_uses_gui_settings_root | monkeypatch | Parameter for monkeypatch in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 213 |
| test_cli_uses_gui_settings_root | capsys | Parameter for capsys in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | pytest.CaptureFixture[str] | Enclosing invocation or class/instance lifetime | 213 |
| test_cli_uses_gui_settings_root | json | Imported dependency for json in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 216 |
| test_cli_uses_gui_settings_root | SimpleNamespace | Imported dependency for SimpleNamespace in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 217 |
| test_cli_uses_gui_settings_root | sync_tool_registry | Imported dependency for sync tool registry in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 219 |
| test_cli_uses_gui_settings_root | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 221 |
| test_cli_uses_gui_settings_root.lambda_228 | client | Callback parameter for client in test_cli_uses_gui_settings_root.lambda_228; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 228 |
| test_cli_uses_gui_settings_root.lambda_229 | client | Callback parameter for client in test_cli_uses_gui_settings_root.lambda_229; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 229 |
| test_cli_uses_gui_settings_root | summary | Local binding for summary in test_cli_uses_gui_settings_root; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| test_bound_catalog_root_cannot_change_silently | tmp_path | Parameter for tmp path in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 236 |
| test_bound_catalog_root_cannot_change_silently | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 238 |
| test_bound_catalog_root_cannot_change_silently | catalog | Local binding for catalog in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 240 |
| test_bound_catalog_root_cannot_change_silently | adapter | Local binding for adapter in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Return type of CatalogToolSource; see its callable contract | Enclosing invocation or class/instance lifetime | 241 |
| test_bound_catalog_root_cannot_change_silently | service | Local binding for service in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Return type of ToolRetriever; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| test_bound_catalog_root_cannot_change_silently | other | Local binding for other in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 245 |
| test_bound_catalog_root_cannot_change_silently | catalog.root | Attribute for catalog.root in test_bound_catalog_root_cannot_change_silently; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 247, 250 |
| test_catalog_stage_durations_are_measured | tmp_path | Parameter for tmp path in test_catalog_stage_durations_are_measured; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 255 |
| test_catalog_stage_durations_are_measured | caplog | Parameter for caplog in test_catalog_stage_durations_are_measured; use the enclosing contract and type below. | pytest.LogCaptureFixture | Enclosing invocation or class/instance lifetime | 255 |
| test_catalog_stage_durations_are_measured | logging | Imported dependency for logging in test_catalog_stage_durations_are_measured; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 258 |
| test_catalog_stage_durations_are_measured | re | Imported dependency for re in test_catalog_stage_durations_are_measured; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 259 |
| test_catalog_stage_durations_are_measured | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 261 |
| test_catalog_stage_durations_are_measured | durations | Local binding for durations in test_catalog_stage_durations_are_measured; use the enclosing contract and type below. | Return type of findall; see its callable contract | Enclosing invocation or class/instance lifetime | 265 |
| test_catalog_stage_durations_are_measured.comprehension_270 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 270 |
