# Reference for tests/test_application_review.py

Editable review regressions use only the maintained temporary fixture package.

Source fingerprint: 0e30b0556dbc2d9fe3b3d723905a7a4edd5e98aad07780831b8b587d81b4828f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### reviewed

Return the real schema-3 review snapshot without executing reviewed source.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### generated

Build a real schema-3 candidate from approved catalog tools without model inference.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### generated.factory

Return authored artifacts across the production coordinator boundary.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### generated.factory.client

Never infer with a real model in review regressions.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### service

Import the service at the test boundary so missing behavior fails visibly.

Kind: callable. Declared return: Not declared / class. Source line: 73.

### test_review_lists_real_files_and_proposed_tests_separately

A readable file inventory replaces a single JSON dump.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_save_widget_invalidates_review_and_updates_exact_manifest

Do not execute modified source under an old application approval.

Kind: callable. Declared return: Not declared / class. Source line: 90.

### test_unknown_paths_and_approved_dependencies_cannot_be_edited

The editor cannot modify approved tools or supervisor-maintained dependencies.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_stale_invalid_and_oversized_edits_preserve_the_previous_draft

Reject invalid drafts before changing package bytes or review identity.

Kind: callable. Declared return: Not declared / class. Source line: 120.

### test_proposed_tests_edit_remains_provisional_and_requires_new_review

Saving test text never executes it or creates an approval.

Kind: callable. Declared return: Not declared / class. Source line: 134.

### test_editor_accepts_the_designers_approved_typing_dependency

Editing a valid model widget must retain the same approved import contract.

Kind: callable. Declared return: Not declared / class. Source line: 147.

### test_editor_still_rejects_unapproved_runtime_dependencies

The typing consistency fix must not authorize files, networking or processes.

Kind: callable. Declared return: Not declared / class. Source line: 167.

### test_tool_related_selection_opens_three_consistent_panes

Selecting implementation/widget/tests resolves the same tool triplet.

Kind: callable. Declared return: Not declared / class. Source line: 179.

### test_batch_save_prevalidates_all_buffers_before_any_file_change

One invalid pane must not partially save another valid pane.

Kind: callable. Declared return: Not declared / class. Source line: 205.

### test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite

App approval cannot silently authorize altered installed tool implementations.

Kind: callable. Declared return: Not declared / class. Source line: 217.

### test_gradio_outer_whitespace_does_not_create_a_tool_revision

Submitting an unchanged Code pane preserves approved source/test bytes.

Kind: callable. Declared return: Not declared / class. Source line: 238.

### test_tool_source_inventory_identifies_revision_editor

Tool source selection must not be mislabeled read-only when it opens editable panes.

Kind: callable. Declared return: Not declared / class. Source line: 256.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | widget_source | Imported dependency for widget source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | candidate | Imported dependency for candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| reviewed | tmp_path | Parameter for tmp path in reviewed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| module | CONNECTION_CODE | Module binding for CONNECTION CODE in module; use the enclosing contract and type below. | Return type of join; see its callable contract | Module/process lifetime | 17 |
| generated | tmp_path | Parameter for tmp path in generated; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| generated | installed | Imported dependency for installed in generated; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| generated | registry | Imported dependency for registry in generated; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| generated | ApplicationPipeline | Imported dependency for ApplicationPipeline in generated; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| generated | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| generated | tools | Local binding for tools in generated; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| generated.factory | folder | Parameter for folder in generated.factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| generated.factory.client | role | Parameter for role in generated.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| generated.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| generated.factory.client | module | Local binding for module in generated.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| generated.factory.client.comprehension_58 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 60 |
| service | ApplicationReview | Imported dependency for ApplicationReview in service; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 75 |
| test_review_lists_real_files_and_proposed_tests_separately | tmp_path | Parameter for tmp path in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_review_lists_real_files_and_proposed_tests_separately | item | Local binding for item in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_review_lists_real_files_and_proposed_tests_separately | names | Local binding for names in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 83 |
| test_review_lists_real_files_and_proposed_tests_separately.comprehension_83 | _ | Comprehension item for  in test_review_lists_real_files_and_proposed_tests_separately.comprehension_83; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_review_lists_real_files_and_proposed_tests_separately.comprehension_83 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_review_lists_real_files_and_proposed_tests_separately | text | Local binding for text in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_review_lists_real_files_and_proposed_tests_separately | editable | Local binding for editable in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_review_lists_real_files_and_proposed_tests_separately | _ | Local binding for  in test_review_lists_real_files_and_proposed_tests_separately; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | tmp_path | Parameter for tmp path in test_save_widget_invalidates_review_and_updates_exact_manifest; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 90 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | application_digest | Imported dependency for application digest in test_save_widget_invalidates_review_and_updates_exact_manifest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 92 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | item | Local binding for item in test_save_widget_invalidates_review_and_updates_exact_manifest; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | item.verified | Attribute for item.verified in test_save_widget_invalidates_review_and_updates_exact_manifest; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 96 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | before | Local binding for before in test_save_widget_invalidates_review_and_updates_exact_manifest; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_save_widget_invalidates_review_and_updates_exact_manifest | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_unknown_paths_and_approved_dependencies_cannot_be_edited | tmp_path | Parameter for tmp path in test_unknown_paths_and_approved_dependencies_cannot_be_edited; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_unknown_paths_and_approved_dependencies_cannot_be_edited | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_unknown_paths_and_approved_dependencies_cannot_be_edited | item | Local binding for item in test_unknown_paths_and_approved_dependencies_cannot_be_edited; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| test_stale_invalid_and_oversized_edits_preserve_the_previous_draft | tmp_path | Parameter for tmp path in test_stale_invalid_and_oversized_edits_preserve_the_previous_draft; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 120 |
| test_stale_invalid_and_oversized_edits_preserve_the_previous_draft | item | Local binding for item in test_stale_invalid_and_oversized_edits_preserve_the_previous_draft; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_stale_invalid_and_oversized_edits_preserve_the_previous_draft | before | Local binding for before in test_stale_invalid_and_oversized_edits_preserve_the_previous_draft; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_stale_invalid_and_oversized_edits_preserve_the_previous_draft | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 124 |
| test_stale_invalid_and_oversized_edits_preserve_the_previous_draft | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 124 |
| test_proposed_tests_edit_remains_provisional_and_requires_new_review | tmp_path | Parameter for tmp path in test_proposed_tests_edit_remains_provisional_and_requires_new_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 134 |
| test_proposed_tests_edit_remains_provisional_and_requires_new_review | item | Local binding for item in test_proposed_tests_edit_remains_provisional_and_requires_new_review; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| test_editor_accepts_the_designers_approved_typing_dependency | tmp_path | Parameter for tmp path in test_editor_accepts_the_designers_approved_typing_dependency; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 147 |
| test_editor_accepts_the_designers_approved_typing_dependency | WidgetDesigner | Imported dependency for WidgetDesigner in test_editor_accepts_the_designers_approved_typing_dependency; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 149 |
| test_editor_accepts_the_designers_approved_typing_dependency | item | Local binding for item in test_editor_accepts_the_designers_approved_typing_dependency; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_editor_accepts_the_designers_approved_typing_dependency | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 152 |
| test_editor_accepts_the_designers_approved_typing_dependency | proposal | Local binding for proposal in test_editor_accepts_the_designers_approved_typing_dependency; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 153 |
| test_editor_still_rejects_unapproved_runtime_dependencies | tmp_path | Parameter for tmp path in test_editor_still_rejects_unapproved_runtime_dependencies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_editor_still_rejects_unapproved_runtime_dependencies | module | Parameter for module in test_editor_still_rejects_unapproved_runtime_dependencies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| test_editor_still_rejects_unapproved_runtime_dependencies | item | Local binding for item in test_editor_still_rejects_unapproved_runtime_dependencies; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_tool_related_selection_opens_three_consistent_panes | tmp_path | Parameter for tmp path in test_tool_related_selection_opens_three_consistent_panes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| test_tool_related_selection_opens_three_consistent_panes | item | Local binding for item in test_tool_related_selection_opens_three_consistent_panes; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 181 |
| test_tool_related_selection_opens_three_consistent_panes | snapshot | Local binding for snapshot in test_tool_related_selection_opens_three_consistent_panes; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_tool_related_selection_opens_three_consistent_panes | item.review_text | Attribute for item.review text in test_tool_related_selection_opens_three_consistent_panes; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_tool_related_selection_opens_three_consistent_panes | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 193 |
| test_tool_related_selection_opens_three_consistent_panes | panes | Local binding for panes in test_tool_related_selection_opens_three_consistent_panes; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_batch_save_prevalidates_all_buffers_before_any_file_change | tmp_path | Parameter for tmp path in test_batch_save_prevalidates_all_buffers_before_any_file_change; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 205 |
| test_batch_save_prevalidates_all_buffers_before_any_file_change | item | Local binding for item in test_batch_save_prevalidates_all_buffers_before_any_file_change; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_batch_save_prevalidates_all_buffers_before_any_file_change | panes | Local binding for panes in test_batch_save_prevalidates_all_buffers_before_any_file_change; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_batch_save_prevalidates_all_buffers_before_any_file_change | before | Local binding for before in test_batch_save_prevalidates_all_buffers_before_any_file_change; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 209 |
| test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite | tmp_path | Parameter for tmp path in test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 217 |
| test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite | item | Local binding for item in test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite | panes | Local binding for panes in test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite | snapshot | Local binding for snapshot in test_edited_tool_code_is_a_pending_revision_not_an_approved_shared_overwrite; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision | tmp_path | Parameter for tmp path in test_gradio_outer_whitespace_does_not_create_a_tool_revision; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 238 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision | SOURCES | Imported dependency for SOURCES in test_gradio_outer_whitespace_does_not_create_a_tool_revision; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 240 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision | item | Local binding for item in test_gradio_outer_whitespace_does_not_create_a_tool_revision; use the enclosing contract and type below. | Return type of generated; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision | panes | Local binding for panes in test_gradio_outer_whitespace_does_not_create_a_tool_revision; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 246, 247 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision.comprehension_247 | key | Comprehension item for key in test_gradio_outer_whitespace_does_not_create_a_tool_revision.comprehension_247; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 247 |
| test_gradio_outer_whitespace_does_not_create_a_tool_revision.comprehension_247 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 247 |
| test_tool_source_inventory_identifies_revision_editor | tmp_path | Parameter for tmp path in test_tool_source_inventory_identifies_revision_editor; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 256 |
| test_tool_source_inventory_identifies_revision_editor | labels | Local binding for labels in test_tool_source_inventory_identifies_revision_editor; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 258 |
| test_tool_source_inventory_identifies_revision_editor.comprehension_258 | label | Comprehension item for label in test_tool_source_inventory_identifies_revision_editor.comprehension_258; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 258 |
| test_tool_source_inventory_identifies_revision_editor.comprehension_258 | key | Comprehension item for key in test_tool_source_inventory_identifies_revision_editor.comprehension_258; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 258 |
