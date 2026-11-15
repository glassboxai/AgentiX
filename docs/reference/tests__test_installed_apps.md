# Reference for tests/test_installed_apps.py

Persistent application catalog tests use reviewed maintained fixtures only.

Source fingerprint: e69ff793a3f2cbeb6786006b8dd185db38260520b9a2b24fcb89b76a0183e588

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### library

Inject authenticated fixture protection instead of claiming Windows execution.

Kind: callable. Declared return: Not declared / class. Source line: 13.

### verified

Publish a trusted fixture verification boundary, not a model-supplied claim.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### test_only_verified_apps_can_be_installed_and_loaded_after_restart

A durable catalog must neither list drafts nor depend on their old session.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### test_source_tampering_invalidates_catalog_approval

A JSON manifest or old receipt cannot approve changed executable bytes.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code

Presentation config is bounded data and separate from executable identity.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_manager_application_decision_uses_only_a_catalog_id_and_typed_text

Reject path/function injection instead of treating an app request as tool creation.

Kind: callable. Declared return: Not declared / class. Source line: 88.

### published_with_tools

Construct a verified catalog fixture with exact installed tool dependency hashes.

Kind: callable. Declared return: Not declared / class. Source line: 111.

### published_with_tools.factory

Supply trusted widget/workflow fixtures without model inference.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### published_with_tools.factory.client

Return reviewed test data, never execute its source on the host.

Kind: callable. Declared return: Not declared / class. Source line: 125.

### test_library_load_does_not_generate_or_execute_code

Loading a verified app restores a draft snapshot without model/test calls.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required

Discovery retains a protected app while loading still enforces tool approvals.

Kind: callable. Declared return: Not declared / class. Source line: 189.

### test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies

A manager-selected app calls the injected native boundary without model/test work.

Kind: callable. Declared return: Not declared / class. Source line: 213.

### test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies.native

Record only the trusted boundary contract, not child semantic proof.

Kind: callable. Declared return: Not declared / class. Source line: 222.

### test_invocation_rejects_tool_changes_during_native_execution

A result is not accepted after a dependency changes while the child runs.

Kind: callable. Declared return: Not declared / class. Source line: 245.

### test_invocation_rejects_tool_changes_during_native_execution.native

Simulate an external edit during an otherwise successful computation.

Kind: callable. Declared return: Not declared / class. Source line: 253.

### test_publishing_reviewed_revision_preserves_valid_presentation_config

A code revision may require new approval without discarding the user's layout.

Kind: callable. Declared return: Not declared / class. Source line: 264.

### test_name_availability_reflects_existing_install_folder

Publication reserves the display-name folder; availability must report it.

Kind: callable. Declared return: Not declared / class. Source line: 277.

### test_catalog_removal_service_is_outside_the_execution_policy

V7-061: fixing removal must not invalidate every installed application.

Kind: callable. Declared return: Not declared / class. Source line: 285.

### stale_library

Publish under one policy, then reopen the same storage under a changed policy.

Kind: callable. Declared return: Not declared / class. Source line: 309.

### test_rejected_record_logs_identity_and_one_summary

A rejection warning must name the application and not repeat per refresh.

Kind: callable. Declared return: Not declared / class. Source line: 317.

### test_catalog_keeps_stale_app_visible_without_granting_it

Discovery retains a stale record while get() still refuses to authorize it.

Kind: callable. Declared return: Not declared / class. Source line: 338.

### test_stale_load_returns_exact_installed_bytes_without_policy_grant

Re-approval needs the installed bytes even when the host policy changed.

Kind: callable. Declared return: Not declared / class. Source line: 351.

### test_reseal_replaces_only_the_policy_binding_atomically

Re-sealing must keep package and review bytes and leave no partial record.

Kind: callable. Declared return: Not declared / class. Source line: 360.

### test_reseal_refuses_changed_source

A stale policy never authorizes bytes that changed after installation.

Kind: callable. Declared return: Not declared / class. Source line: 373.

### test_maintained_runtime_drift_is_reported_apart_from_changed_source

A moved maintained template must not be reported as tampered application source.

Kind: callable. Declared return: Not declared / class. Source line: 382.

### test_runtime_refresh_loads_installed_bytes_with_current_runtime

An explicit refresh keeps application bytes and replaces only runtime members.

Kind: callable. Declared return: Not declared / class. Source line: 403.

### test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime

Re-approval after runtime drift reseals the new digest and installed runtime bytes.

Kind: callable. Declared return: Not declared / class. Source line: 436.

### test_acceptance_save_keeps_installed_catalog_identity

Saving acceptance cases for a re-approval must reseal, not create a second folder.

Kind: callable. Declared return: Not declared / class. Source line: 474.

### test_publish_reseals_existing_catalog_identity_without_new_folder

Re-approving a loaded app replaces its record instead of duplicating storage.

Kind: callable. Declared return: Not declared / class. Source line: 498.

### test_catalog_entries_labels_stale_app_for_reapproval

The dropdown must show a stale application instead of hiding it.

Kind: callable. Declared return: Not declared / class. Source line: 510.

### test_load_app_restores_stale_app_for_reapproval

Loading a stale app must restore reviewable bytes and request approval again.

Kind: callable. Declared return: Not declared / class. Source line: 532.

### drift_tool_contract

Simulate a re-approved tool whose contract digest moved after installation.

Kind: callable. Declared return: Not declared / class. Source line: 557.

### test_load_app_rebinds_changed_tool_contracts_for_reapproval

A changed tool contract must load for re-approval instead of failing outright.

Kind: callable. Declared return: Not declared / class. Source line: 572.

### test_load_app_reports_the_missing_catalog_approval_actionably

V7-064: a catalog without reusable approvals must name the recovery, not the type.

Kind: callable. Declared return: Not declared / class. Source line: 596.

### test_reverify_app_reports_the_missing_catalog_approval_actionably

V7-064: re-verification must explain the missing approval instead of the type name.

Kind: callable. Declared return: Not declared / class. Source line: 626.

### test_check_dependencies_names_the_tool_without_a_reusable_approval

V7-064: the dependency failure must name the tool and its maintained skip reason.

Kind: callable. Declared return: Not declared / class. Source line: 657.

### test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry

Expose the maintained skip reason without an approved tool.

Kind: class. Declared return: Not declared / class. Source line: 664.

### test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry.resolve

Return no approved tool so the application dependency is missing.

Kind: callable. Declared return: Not declared / class. Source line: 667.

### test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry._skip_reason

Return the owner-actionable reason for the missing approval.

Kind: callable. Declared return: Not declared / class. Source line: 671.

### test_reverify_refuses_dependency_drift_with_actionable_message

Dependency drift needs a new human review, not an automatic reseal.

Kind: callable. Declared return: Not declared / class. Source line: 684.

### test_reapproval_reseals_rebound_tool_dependencies

Approving a reloaded app must store the current tool digests it was verified against.

Kind: callable. Declared return: Not declared / class. Source line: 706.

### test_reapproval_reseals_rebound_tool_dependencies.Supervisor

Exercise the production dependency check without native or browser claims.

Kind: class. Declared return: Not declared / class. Source line: 722.

### test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve

Run the same dependency recheck the production supervisor runs.

Kind: callable. Declared return: Not declared / class. Source line: 725.

### test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify

Mark verified without claiming a real gate execution.

Kind: callable. Declared return: Not declared / class. Source line: 730.

### test_describe_app_drops_stale_guidance_after_reseal

A successful re-approval must remove the re-approval guidance from the panel.

Kind: callable. Declared return: Not declared / class. Source line: 747.

### test_describe_app_drops_stale_guidance_after_reverify

A successful re-verification must remove the re-approval guidance from the panel.

Kind: callable. Declared return: Not declared / class. Source line: 772.

### test_describe_app_drops_stale_guidance_after_reverify.Supervisor

Accept the installed bytes without claiming a real gate execution.

Kind: class. Declared return: Not declared / class. Source line: 788.

### test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify

Mark the candidate verified for the reseal path.

Kind: callable. Declared return: Not declared / class. Source line: 791.

### test_catalog_view_refreshes_label_and_description_together

One refresh must drop both the stale dropdown label and its guidance text.

Kind: callable. Declared return: Not declared / class. Source line: 806.

### test_catalog_view_refreshes_label_and_description_together.Dropdown

Capture the update payload without building a real Gradio component.

Kind: class. Declared return: Not declared / class. Source line: 825.

### test_catalog_view_refreshes_label_and_description_together.Dropdown.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 828.

### test_catalog_refresh_binding_updates_description_with_choices

The status refresh must repaint the description so stale guidance disappears.

Kind: callable. Declared return: Not declared / class. Source line: 845.

### test_catalog_refresh_binding_updates_description_with_choices.Component

Record constructor kwargs and absorb event bindings.

Kind: class. Declared return: Not declared / class. Source line: 855.

### test_catalog_refresh_binding_updates_description_with_choices.Component.__init__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 858.

### test_catalog_refresh_binding_updates_description_with_choices.Component.__enter__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 863.

### test_catalog_refresh_binding_updates_description_with_choices.Component.__exit__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 866.

### test_catalog_refresh_binding_updates_description_with_choices.Component.__getattr__

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 869.

### test_catalog_refresh_binding_updates_description_with_choices.Component.__getattr__.event

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 870.

### test_catalog_refresh_binding_updates_description_with_choices.Dialog

Absorb dialog wrapping without building real modal components.

Kind: class. Declared return: Not declared / class. Source line: 876.

### test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 879.

### test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 882.

### test_catalog_refresh_binding_updates_description_with_choices.Dialog.outputs

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 885.

### test_reverify_reseals_only_after_independent_gates_pass

D3 re-runs real gates on installed bytes and reseals only on success.

Kind: callable. Declared return: Not declared / class. Source line: 926.

### test_reverify_reseals_only_after_independent_gates_pass.Supervisor

Record gate invocation without claiming native or browser execution.

Kind: class. Declared return: Not declared / class. Source line: 938.

### test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify

Accept only the exact installed bytes under test.

Kind: callable. Declared return: Not declared / class. Source line: 941.

### test_reverify_keeps_stale_record_when_gates_fail

A failed gate must leave the stale record untouched and unapproved.

Kind: callable. Declared return: Not declared / class. Source line: 961.

### test_reverify_keeps_stale_record_when_gates_fail.Supervisor

Fail the gate without touching storage.

Kind: class. Declared return: Not declared / class. Source line: 972.

### test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify

Report an independent acceptance failure.

Kind: callable. Declared return: Not declared / class. Source line: 975.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | widget_source | Imported dependency for widget source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | candidate | Imported dependency for candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Protector | Imported dependency for Protector in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| library | tmp_path | Parameter for tmp path in library; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 13 |
| library | InstalledApps | Imported dependency for InstalledApps in library; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 15 |
| verified | tmp_path | Parameter for tmp path in verified; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| verified | item | Local binding for item in verified; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| verified | item.verified | Attribute for item.verified in verified; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 24 |
| verified | item.review_text | Attribute for item.review text in verified; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | tmp_path | Parameter for tmp path in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 36 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | item | Local binding for item in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | service | Local binding for service in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | item.verified | Attribute for item.verified in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 40, 43 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | record | Local binding for record in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | fresh | Local binding for fresh in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart.comprehension_47 | app | Comprehension item for app in test_only_verified_apps_can_be_installed_and_loaded_after_restart.comprehension_47; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| test_only_verified_apps_can_be_installed_and_loaded_after_restart | loaded | Local binding for loaded in test_only_verified_apps_can_be_installed_and_loaded_after_restart; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_source_tampering_invalidates_catalog_approval | tmp_path | Parameter for tmp path in test_source_tampering_invalidates_catalog_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_source_tampering_invalidates_catalog_approval | service | Local binding for service in test_source_tampering_invalidates_catalog_approval; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_source_tampering_invalidates_catalog_approval | app | Local binding for app in test_source_tampering_invalidates_catalog_approval; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code | tmp_path | Parameter for tmp path in test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code | service | Local binding for service in test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code | app | Local binding for app in test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code | layout | Local binding for layout in test_layout_changes_do_not_approve_code_or_invalidate_unchanged_code; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 67 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | RunApplicationDecision | Imported dependency for RunApplicationDecision in test_manager_application_decision_uses_only_a_catalog_id_and_typed_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 90 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | parse_manager_response | Imported dependency for parse manager response in test_manager_application_decision_uses_only_a_catalog_id_and_typed_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 90 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of parse_manager_response; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | app_id | Loop item for app id in test_manager_application_decision_uses_only_a_catalog_id_and_typed_text; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 100 |
| test_manager_application_decision_uses_only_a_catalog_id_and_typed_text | arguments | Loop item for arguments in test_manager_application_decision_uses_only_a_catalog_id_and_typed_text; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 100 |
| published_with_tools | tmp_path | Parameter for tmp path in published_with_tools; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| published_with_tools | installed | Imported dependency for installed in published_with_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 113 |
| published_with_tools | registry | Imported dependency for registry in published_with_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 113 |
| published_with_tools | ApplicationPipeline | Imported dependency for ApplicationPipeline in published_with_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 115 |
| published_with_tools | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| published_with_tools | fixture | Local binding for fixture in published_with_tools; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| published_with_tools | tools | Local binding for tools in published_with_tools; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| published_with_tools.factory | folder | Parameter for folder in published_with_tools.factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| published_with_tools.factory.client | role | Parameter for role in published_with_tools.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| published_with_tools.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| published_with_tools.factory.client | module | Local binding for module in published_with_tools.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
| published_with_tools.factory.client | catalog | Local binding for catalog in published_with_tools.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 134 |
| published_with_tools.factory.client.comprehension_137 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 137 |
| published_with_tools.factory.client.comprehension_142 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 143 |
| published_with_tools | item | Local binding for item in published_with_tools; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| published_with_tools | item.verified | Attribute for item.verified in published_with_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 155 |
| published_with_tools | service | Local binding for service in published_with_tools; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 156 |
| test_library_load_does_not_generate_or_execute_code | tmp_path | Parameter for tmp path in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_library_load_does_not_generate_or_execute_code | SimpleNamespace | Imported dependency for SimpleNamespace in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 162 |
| test_library_load_does_not_generate_or_execute_code | registry | Imported dependency for registry in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 164 |
| test_library_load_does_not_generate_or_execute_code | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 166 |
| test_library_load_does_not_generate_or_execute_code | service | Local binding for service in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| test_library_load_does_not_generate_or_execute_code | app | Local binding for app in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| test_library_load_does_not_generate_or_execute_code | fixture | Local binding for fixture in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| test_library_load_does_not_generate_or_execute_code | sessions | Local binding for sessions in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_library_load_does_not_generate_or_execute_code | owner | Local binding for owner in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_library_load_does_not_generate_or_execute_code | owner.controller.security | Attribute for owner.controller.security in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_library_load_does_not_generate_or_execute_code | owner.controller.validation | Attribute for owner.controller.validation in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 172 |
| test_library_load_does_not_generate_or_execute_code | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 173 |
| test_library_load_does_not_generate_or_execute_code | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_library_load_does_not_generate_or_execute_code | rows | Local binding for rows in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_library_load_does_not_generate_or_execute_code | _ | Local binding for  in test_library_load_does_not_generate_or_execute_code; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_library_load_does_not_generate_or_execute_code | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | tmp_path | Parameter for tmp path in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 189 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | SimpleNamespace | Imported dependency for SimpleNamespace in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 191 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | registry | Imported dependency for registry in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 193 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | service | Local binding for service in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | app | Local binding for app in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | fixture | Local binding for fixture in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | sessions | Local binding for sessions in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | owner | Local binding for owner in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | owner.controller.security | Attribute for owner.controller.security in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | owner.controller.validation | Attribute for owner.controller.validation in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 201 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 202 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | request | Local binding for request in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | choices | Local binding for choices in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | _ | Local binding for  in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required | rows | Local binding for rows in test_catalog_keeps_protected_app_visible_when_tool_reapproval_is_required; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 209 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | tmp_path | Parameter for tmp path in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 213 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | registry | Imported dependency for registry in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 215 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | AppInvocation | Imported dependency for AppInvocation in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 217 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | service | Local binding for service in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | app | Local binding for app in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | fixture | Local binding for fixture in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | calls | Local binding for calls in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 220 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies.native | snapshot | Parameter for snapshot in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies.native | payload | Parameter for payload in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 222 |
| test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies | invocation | Local binding for invocation in test_catalog_invocation_uses_approved_snapshot_and_rechecks_dependencies; use the enclosing contract and type below. | Return type of AppInvocation; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_invocation_rejects_tool_changes_during_native_execution | tmp_path | Parameter for tmp path in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 245 |
| test_invocation_rejects_tool_changes_during_native_execution | registry | Imported dependency for registry in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 247 |
| test_invocation_rejects_tool_changes_during_native_execution | AppInvocation | Imported dependency for AppInvocation in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 249 |
| test_invocation_rejects_tool_changes_during_native_execution | service | Local binding for service in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_invocation_rejects_tool_changes_during_native_execution | app | Local binding for app in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_invocation_rejects_tool_changes_during_native_execution | fixture | Local binding for fixture in test_invocation_rejects_tool_changes_during_native_execution; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_invocation_rejects_tool_changes_during_native_execution.native | snapshot | Parameter for snapshot in test_invocation_rejects_tool_changes_during_native_execution.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 253 |
| test_invocation_rejects_tool_changes_during_native_execution.native | payload | Parameter for payload in test_invocation_rejects_tool_changes_during_native_execution.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 253 |
| test_publishing_reviewed_revision_preserves_valid_presentation_config | tmp_path | Parameter for tmp path in test_publishing_reviewed_revision_preserves_valid_presentation_config; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 264 |
| test_publishing_reviewed_revision_preserves_valid_presentation_config | item | Local binding for item in test_publishing_reviewed_revision_preserves_valid_presentation_config; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 266 |
| test_publishing_reviewed_revision_preserves_valid_presentation_config | layout | Local binding for layout in test_publishing_reviewed_revision_preserves_valid_presentation_config; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 267 |
| test_publishing_reviewed_revision_preserves_valid_presentation_config | service | Local binding for service in test_publishing_reviewed_revision_preserves_valid_presentation_config; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 272 |
| test_publishing_reviewed_revision_preserves_valid_presentation_config | app | Local binding for app in test_publishing_reviewed_revision_preserves_valid_presentation_config; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_name_availability_reflects_existing_install_folder | tmp_path | Parameter for tmp path in test_name_availability_reflects_existing_install_folder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 277 |
| test_name_availability_reflects_existing_install_folder | service | Local binding for service in test_name_availability_reflects_existing_install_folder; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 279 |
| test_name_availability_reflects_existing_install_folder | app | Local binding for app in test_name_availability_reflects_existing_install_folder; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 280 |
| test_catalog_removal_service_is_outside_the_execution_policy | tmp_path | Parameter for tmp path in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 285 |
| test_catalog_removal_service_is_outside_the_execution_policy | monkeypatch | Parameter for monkeypatch in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 285 |
| test_catalog_removal_service_is_outside_the_execution_policy | importlib | Imported dependency for importlib in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 287 |
| test_catalog_removal_service_is_outside_the_execution_policy | shutil | Imported dependency for shutil in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 288 |
| test_catalog_removal_service_is_outside_the_execution_policy | Path | Imported dependency for Path in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 289 |
| test_catalog_removal_service_is_outside_the_execution_policy | checkout | Local binding for checkout in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 291 |
| test_catalog_removal_service_is_outside_the_execution_policy | target | Local binding for target in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Return type of import_module; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| test_catalog_removal_service_is_outside_the_execution_policy | relative | Local binding for relative in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Return type of relative_to; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| test_catalog_removal_service_is_outside_the_execution_policy | before | Local binding for before in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Return type of app_policy; see its callable contract | Enclosing invocation or class/instance lifetime | 300 |
| test_catalog_removal_service_is_outside_the_execution_policy | removal | Local binding for removal in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 301 |
| test_catalog_removal_service_is_outside_the_execution_policy | boundary | Local binding for boundary in test_catalog_removal_service_is_outside_the_execution_policy; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 304 |
| stale_library | tmp_path | Parameter for tmp path in stale_library; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 309 |
| stale_library | monkeypatch | Parameter for monkeypatch in stale_library; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 309 |
| stale_library | service | Local binding for service in stale_library; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| stale_library | app | Local binding for app in stale_library; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 312 |
| test_rejected_record_logs_identity_and_one_summary | tmp_path | Parameter for tmp path in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 317 |
| test_rejected_record_logs_identity_and_one_summary | monkeypatch | Parameter for monkeypatch in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 317 |
| test_rejected_record_logs_identity_and_one_summary | caplog | Parameter for caplog in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 317 |
| test_rejected_record_logs_identity_and_one_summary | logging | Imported dependency for logging in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 319 |
| test_rejected_record_logs_identity_and_one_summary | service | Local binding for service in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 321 |
| test_rejected_record_logs_identity_and_one_summary | app | Local binding for app in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 321 |
| test_rejected_record_logs_identity_and_one_summary | entries | Local binding for entries in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | Return type of entries; see its callable contract | Enclosing invocation or class/instance lifetime | 323 |
| test_rejected_record_logs_identity_and_one_summary.comprehension_324 | entry | Comprehension item for entry in test_rejected_record_logs_identity_and_one_summary.comprehension_324; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 324 |
| test_rejected_record_logs_identity_and_one_summary | rejected | Local binding for rejected in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 325 |
| test_rejected_record_logs_identity_and_one_summary.comprehension_325 | record | Comprehension item for record in test_rejected_record_logs_identity_and_one_summary.comprehension_325; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 326 |
| test_rejected_record_logs_identity_and_one_summary | summary | Local binding for summary in test_rejected_record_logs_identity_and_one_summary; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 331 |
| test_rejected_record_logs_identity_and_one_summary.comprehension_331 | record | Comprehension item for record in test_rejected_record_logs_identity_and_one_summary.comprehension_331; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 332 |
| test_catalog_keeps_stale_app_visible_without_granting_it | tmp_path | Parameter for tmp path in test_catalog_keeps_stale_app_visible_without_granting_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 338 |
| test_catalog_keeps_stale_app_visible_without_granting_it | monkeypatch | Parameter for monkeypatch in test_catalog_keeps_stale_app_visible_without_granting_it; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 338 |
| test_catalog_keeps_stale_app_visible_without_granting_it | service | Local binding for service in test_catalog_keeps_stale_app_visible_without_granting_it; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 340 |
| test_catalog_keeps_stale_app_visible_without_granting_it | app | Local binding for app in test_catalog_keeps_stale_app_visible_without_granting_it; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 340 |
| test_catalog_keeps_stale_app_visible_without_granting_it | entries | Local binding for entries in test_catalog_keeps_stale_app_visible_without_granting_it; use the enclosing contract and type below. | Return type of entries; see its callable contract | Enclosing invocation or class/instance lifetime | 341 |
| test_catalog_keeps_stale_app_visible_without_granting_it.comprehension_342 | entry | Comprehension item for entry in test_catalog_keeps_stale_app_visible_without_granting_it.comprehension_342; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 342 |
| test_stale_load_returns_exact_installed_bytes_without_policy_grant | tmp_path | Parameter for tmp path in test_stale_load_returns_exact_installed_bytes_without_policy_grant; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| test_stale_load_returns_exact_installed_bytes_without_policy_grant | monkeypatch | Parameter for monkeypatch in test_stale_load_returns_exact_installed_bytes_without_policy_grant; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| test_stale_load_returns_exact_installed_bytes_without_policy_grant | service | Local binding for service in test_stale_load_returns_exact_installed_bytes_without_policy_grant; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_stale_load_returns_exact_installed_bytes_without_policy_grant | app | Local binding for app in test_stale_load_returns_exact_installed_bytes_without_policy_grant; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_stale_load_returns_exact_installed_bytes_without_policy_grant | stale | Local binding for stale in test_stale_load_returns_exact_installed_bytes_without_policy_grant; use the enclosing contract and type below. | Return type of load_stale; see its callable contract | Enclosing invocation or class/instance lifetime | 354 |
| test_reseal_replaces_only_the_policy_binding_atomically | tmp_path | Parameter for tmp path in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 360 |
| test_reseal_replaces_only_the_policy_binding_atomically | monkeypatch | Parameter for monkeypatch in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 360 |
| test_reseal_replaces_only_the_policy_binding_atomically | application_digest | Imported dependency for application digest in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 362 |
| test_reseal_replaces_only_the_policy_binding_atomically | service | Local binding for service in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 364 |
| test_reseal_replaces_only_the_policy_binding_atomically | app | Local binding for app in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 364 |
| test_reseal_replaces_only_the_policy_binding_atomically | before | Local binding for before in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 365 |
| test_reseal_replaces_only_the_policy_binding_atomically | resealed | Local binding for resealed in test_reseal_replaces_only_the_policy_binding_atomically; use the enclosing contract and type below. | Return type of reseal; see its callable contract | Enclosing invocation or class/instance lifetime | 366 |
| test_reseal_refuses_changed_source | tmp_path | Parameter for tmp path in test_reseal_refuses_changed_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 373 |
| test_reseal_refuses_changed_source | monkeypatch | Parameter for monkeypatch in test_reseal_refuses_changed_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 373 |
| test_reseal_refuses_changed_source | service | Local binding for service in test_reseal_refuses_changed_source; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 375 |
| test_reseal_refuses_changed_source | app | Local binding for app in test_reseal_refuses_changed_source; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 375 |
| test_reseal_refuses_changed_source.comprehension_379 | entry | Comprehension item for entry in test_reseal_refuses_changed_source.comprehension_379; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 379 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | tmp_path | Parameter for tmp path in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 382 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | monkeypatch | Parameter for monkeypatch in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 382 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | general_package | Imported dependency for general package in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 384 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | service | Local binding for service in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 386 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | app | Local binding for app in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 387 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | original | Local binding for original in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 388 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | changed | Local binding for changed in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 389 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source.lambda_394 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 394 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source | entries | Local binding for entries in test_maintained_runtime_drift_is_reported_apart_from_changed_source; use the enclosing contract and type below. | Return type of entries; see its callable contract | Enclosing invocation or class/instance lifetime | 396 |
| test_maintained_runtime_drift_is_reported_apart_from_changed_source.comprehension_397 | entry | Comprehension item for entry in test_maintained_runtime_drift_is_reported_apart_from_changed_source.comprehension_397; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 397 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | tmp_path | Parameter for tmp path in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 403 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | monkeypatch | Parameter for monkeypatch in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 403 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | general_package | Imported dependency for general package in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 405 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | approve_application | Imported dependency for approve application in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 406 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | service | Local binding for service in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 408 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | app | Local binding for app in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 409 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | original | Local binding for original in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 410 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | changed | Local binding for changed in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 411 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | moved | Local binding for moved in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 412 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime.lambda_417 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 417 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | refreshed | Local binding for refreshed in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Return type of load_for_runtime_refresh; see its callable contract | Enclosing invocation or class/instance lifetime | 419 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | snapshot | Local binding for snapshot in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 424 |
| test_runtime_refresh_loads_installed_bytes_with_current_runtime | files | Local binding for files in test_runtime_refresh_loads_installed_bytes_with_current_runtime; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 425 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | tmp_path | Parameter for tmp path in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 436 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | monkeypatch | Parameter for monkeypatch in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 436 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | SimpleNamespace | Imported dependency for SimpleNamespace in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 438 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | general_package | Imported dependency for general package in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 440 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | approve_application | Imported dependency for approve application in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 441 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | service | Local binding for service in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 443 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | app | Local binding for app in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 444 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | original | Local binding for original in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 445 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | changed | Local binding for changed in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 446 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | moved | Local binding for moved in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 447 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime.lambda_452 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 452 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | snapshot | Local binding for snapshot in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 454 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | candidate | Local binding for candidate in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 455 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime | resealed | Local binding for resealed in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 468 |
| test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime.comprehension_471 | entry | Comprehension item for entry in test_reseal_after_runtime_refresh_updates_digest_and_installed_runtime.comprehension_471; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 471 |
| test_acceptance_save_keeps_installed_catalog_identity | tmp_path | Parameter for tmp path in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 474 |
| test_acceptance_save_keeps_installed_catalog_identity | ApplicationReview | Imported dependency for ApplicationReview in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 476 |
| test_acceptance_save_keeps_installed_catalog_identity | service | Local binding for service in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 478 |
| test_acceptance_save_keeps_installed_catalog_identity | item | Local binding for item in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Return type of candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 479 |
| test_acceptance_save_keeps_installed_catalog_identity | item.verified | Attribute for item.verified in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 481 |
| test_acceptance_save_keeps_installed_catalog_identity | app | Local binding for app in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 482 |
| test_acceptance_save_keeps_installed_catalog_identity | item.catalog_id | Attribute for item.catalog id in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 483 |
| test_acceptance_save_keeps_installed_catalog_identity | item.runtime_refresh | Attribute for item.runtime refresh in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 484 |
| test_acceptance_save_keeps_installed_catalog_identity | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 485 |
| test_acceptance_save_keeps_installed_catalog_identity | acceptance | Local binding for acceptance in test_acceptance_save_keeps_installed_catalog_identity; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 486 |
| test_acceptance_save_keeps_installed_catalog_identity.comprehension_487 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 487 |
| test_acceptance_save_keeps_installed_catalog_identity.comprehension_488 | widget | Comprehension item for widget in test_acceptance_save_keeps_installed_catalog_identity.comprehension_488; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 488 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | tmp_path | Parameter for tmp path in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 498 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | monkeypatch | Parameter for monkeypatch in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 498 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | service | Local binding for service in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 500 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | app | Local binding for app in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Return type of stale_library; see its callable contract | Enclosing invocation or class/instance lifetime | 500 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | item | Local binding for item in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Return type of verified; see its callable contract | Enclosing invocation or class/instance lifetime | 501 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | item.catalog_id | Attribute for item.catalog id in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 502 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | folders | Local binding for folders in test_publish_reseals_existing_catalog_identity_without_new_folder; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 503 |
| test_publish_reseals_existing_catalog_identity_without_new_folder.comprehension_503 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 503 |
| test_publish_reseals_existing_catalog_identity_without_new_folder | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 504 |
| test_publish_reseals_existing_catalog_identity_without_new_folder.comprehension_506 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 506 |
| test_catalog_entries_labels_stale_app_for_reapproval | tmp_path | Parameter for tmp path in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 510 |
| test_catalog_entries_labels_stale_app_for_reapproval | monkeypatch | Parameter for monkeypatch in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 510 |
| test_catalog_entries_labels_stale_app_for_reapproval | SimpleNamespace | Imported dependency for SimpleNamespace in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 512 |
| test_catalog_entries_labels_stale_app_for_reapproval | registry | Imported dependency for registry in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 514 |
| test_catalog_entries_labels_stale_app_for_reapproval | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 516 |
| test_catalog_entries_labels_stale_app_for_reapproval | service | Local binding for service in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 518 |
| test_catalog_entries_labels_stale_app_for_reapproval | app | Local binding for app in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 518 |
| test_catalog_entries_labels_stale_app_for_reapproval | fixture | Local binding for fixture in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 518 |
| test_catalog_entries_labels_stale_app_for_reapproval | sessions | Local binding for sessions in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 520 |
| test_catalog_entries_labels_stale_app_for_reapproval | owner | Local binding for owner in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 521 |
| test_catalog_entries_labels_stale_app_for_reapproval | owner.controller.security | Attribute for owner.controller.security in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 522 |
| test_catalog_entries_labels_stale_app_for_reapproval | owner.controller.validation | Attribute for owner.controller.validation in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 523 |
| test_catalog_entries_labels_stale_app_for_reapproval | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 524 |
| test_catalog_entries_labels_stale_app_for_reapproval | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 525 |
| test_catalog_entries_labels_stale_app_for_reapproval | choices | Local binding for choices in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_catalog_entries_labels_stale_app_for_reapproval | _ | Local binding for  in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 526 |
| test_catalog_entries_labels_stale_app_for_reapproval | described | Local binding for described in test_catalog_entries_labels_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of describe_app; see its callable contract | Enclosing invocation or class/instance lifetime | 528 |
| test_load_app_restores_stale_app_for_reapproval | tmp_path | Parameter for tmp path in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 532 |
| test_load_app_restores_stale_app_for_reapproval | monkeypatch | Parameter for monkeypatch in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 532 |
| test_load_app_restores_stale_app_for_reapproval | SimpleNamespace | Imported dependency for SimpleNamespace in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 534 |
| test_load_app_restores_stale_app_for_reapproval | registry | Imported dependency for registry in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 536 |
| test_load_app_restores_stale_app_for_reapproval | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 538 |
| test_load_app_restores_stale_app_for_reapproval | service | Local binding for service in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 540 |
| test_load_app_restores_stale_app_for_reapproval | app | Local binding for app in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 540 |
| test_load_app_restores_stale_app_for_reapproval | fixture | Local binding for fixture in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 540 |
| test_load_app_restores_stale_app_for_reapproval | sessions | Local binding for sessions in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 542 |
| test_load_app_restores_stale_app_for_reapproval | owner | Local binding for owner in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 543 |
| test_load_app_restores_stale_app_for_reapproval | owner.controller.security | Attribute for owner.controller.security in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 544 |
| test_load_app_restores_stale_app_for_reapproval | owner.controller.validation | Attribute for owner.controller.validation in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 545 |
| test_load_app_restores_stale_app_for_reapproval | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 546 |
| test_load_app_restores_stale_app_for_reapproval | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 547 |
| test_load_app_restores_stale_app_for_reapproval | request | Local binding for request in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 548 |
| test_load_app_restores_stale_app_for_reapproval | rows | Local binding for rows in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 549 |
| test_load_app_restores_stale_app_for_reapproval | _ | Local binding for  in test_load_app_restores_stale_app_for_reapproval; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 551 |
| test_load_app_restores_stale_app_for_reapproval | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 551 |
| drift_tool_contract | fixture | Parameter for fixture in drift_tool_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 557 |
| drift_tool_contract | role | Parameter for role in drift_tool_contract; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 557 |
| drift_tool_contract | tool_name | Validated public tool identifier within the configured storage boundary. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 559 |
| drift_tool_contract | owner | Local binding for owner in drift_tool_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| drift_tool_contract | code | Source snapshot passed through approval, syntax checks and isolated staging. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| drift_tool_contract | tests | Optional unittest source snapshot; child-authored success remains provisional. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| drift_tool_contract | digest | Content fingerprint for change detection; not a substitute for human approval. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| drift_tool_contract | functions | Local binding for functions in drift_tool_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| drift_tool_contract | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 560 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | tmp_path | Parameter for tmp path in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 572 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | monkeypatch | Parameter for monkeypatch in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 572 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | SimpleNamespace | Imported dependency for SimpleNamespace in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 574 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | registry | Imported dependency for registry in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 576 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 578 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | service | Local binding for service in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 580 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | app | Local binding for app in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 580 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | fixture | Local binding for fixture in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 580 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | sessions | Local binding for sessions in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 582 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | owner | Local binding for owner in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 583 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | owner.controller.security | Attribute for owner.controller.security in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 584 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | owner.controller.validation | Attribute for owner.controller.validation in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 585 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 586 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 587 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | request | Local binding for request in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 588 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | rows | Local binding for rows in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 589 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | _ | Local binding for  in test_load_app_rebinds_changed_tool_contracts_for_reapproval; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 591 |
| test_load_app_rebinds_changed_tool_contracts_for_reapproval | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 591 |
| test_load_app_reports_the_missing_catalog_approval_actionably | tmp_path | Parameter for tmp path in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 596 |
| test_load_app_reports_the_missing_catalog_approval_actionably | SimpleNamespace | Imported dependency for SimpleNamespace in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 598 |
| test_load_app_reports_the_missing_catalog_approval_actionably | registry | Imported dependency for registry in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 600 |
| test_load_app_reports_the_missing_catalog_approval_actionably | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 602 |
| test_load_app_reports_the_missing_catalog_approval_actionably | CatalogToolRegistry | Imported dependency for CatalogToolRegistry in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 603 |
| test_load_app_reports_the_missing_catalog_approval_actionably | ToolCatalog | Imported dependency for ToolCatalog in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 604 |
| test_load_app_reports_the_missing_catalog_approval_actionably | service | Local binding for service in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 606 |
| test_load_app_reports_the_missing_catalog_approval_actionably | app | Local binding for app in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 606 |
| test_load_app_reports_the_missing_catalog_approval_actionably | fixture | Local binding for fixture in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 606 |
| test_load_app_reports_the_missing_catalog_approval_actionably | empty | Local binding for empty in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 607 |
| test_load_app_reports_the_missing_catalog_approval_actionably | sessions | Local binding for sessions in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 609 |
| test_load_app_reports_the_missing_catalog_approval_actionably | owner | Local binding for owner in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 610 |
| test_load_app_reports_the_missing_catalog_approval_actionably | owner.controller.security | Attribute for owner.controller.security in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 611 |
| test_load_app_reports_the_missing_catalog_approval_actionably | owner.controller.validation | Attribute for owner.controller.validation in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 612 |
| test_load_app_reports_the_missing_catalog_approval_actionably | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 613 |
| test_load_app_reports_the_missing_catalog_approval_actionably | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 614 |
| test_load_app_reports_the_missing_catalog_approval_actionably.lambda_617 | controller | Callback parameter for controller in test_load_app_reports_the_missing_catalog_approval_actionably.lambda_617; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 617 |
| test_load_app_reports_the_missing_catalog_approval_actionably | rows | Local binding for rows in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 619 |
| test_load_app_reports_the_missing_catalog_approval_actionably | message | Local binding for message in test_load_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 620 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | tmp_path | Parameter for tmp path in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 626 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | monkeypatch | Parameter for monkeypatch in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 626 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | SimpleNamespace | Imported dependency for SimpleNamespace in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 628 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | registry | Imported dependency for registry in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 630 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 632 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | CatalogToolRegistry | Imported dependency for CatalogToolRegistry in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 633 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | ToolCatalog | Imported dependency for ToolCatalog in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 634 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | service | Local binding for service in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 636 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | app | Local binding for app in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 636 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | fixture | Local binding for fixture in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 636 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | empty | Local binding for empty in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 638 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | sessions | Local binding for sessions in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 640 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | owner | Local binding for owner in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 641 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | owner.controller.security | Attribute for owner.controller.security in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 642 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | owner.controller.validation | Attribute for owner.controller.validation in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 643 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 644 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 645 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably.lambda_648 | controller | Callback parameter for controller in test_reverify_app_reports_the_missing_catalog_approval_actionably.lambda_648; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 648 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | rows | Local binding for rows in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 650 |
| test_reverify_app_reports_the_missing_catalog_approval_actionably | message | Local binding for message in test_reverify_app_reports_the_missing_catalog_approval_actionably; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 651 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval | SimpleNamespace | Imported dependency for SimpleNamespace in test_check_dependencies_names_the_tool_without_a_reusable_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 659 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval | check_dependencies | Imported dependency for check dependencies in test_check_dependencies_names_the_tool_without_a_reusable_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 661 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval | CatalogDependencyError | Imported dependency for CatalogDependencyError in test_check_dependencies_names_the_tool_without_a_reusable_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 662 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 667 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry._skip_reason | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 671 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval.Registry._skip_reason | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 671 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval | app | Local binding for app in test_check_dependencies_names_the_tool_without_a_reusable_approval; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 675 |
| test_check_dependencies_names_the_tool_without_a_reusable_approval | error | Managed resource for error in test_check_dependencies_names_the_tool_without_a_reusable_approval; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 678 |
| test_reverify_refuses_dependency_drift_with_actionable_message | tmp_path | Parameter for tmp path in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 684 |
| test_reverify_refuses_dependency_drift_with_actionable_message | monkeypatch | Parameter for monkeypatch in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 684 |
| test_reverify_refuses_dependency_drift_with_actionable_message | SimpleNamespace | Imported dependency for SimpleNamespace in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 686 |
| test_reverify_refuses_dependency_drift_with_actionable_message | registry | Imported dependency for registry in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 688 |
| test_reverify_refuses_dependency_drift_with_actionable_message | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 690 |
| test_reverify_refuses_dependency_drift_with_actionable_message | service | Local binding for service in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 692 |
| test_reverify_refuses_dependency_drift_with_actionable_message | app | Local binding for app in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 692 |
| test_reverify_refuses_dependency_drift_with_actionable_message | fixture | Local binding for fixture in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 692 |
| test_reverify_refuses_dependency_drift_with_actionable_message | sessions | Local binding for sessions in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 695 |
| test_reverify_refuses_dependency_drift_with_actionable_message | owner | Local binding for owner in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 696 |
| test_reverify_refuses_dependency_drift_with_actionable_message | owner.controller.security | Attribute for owner.controller.security in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 697 |
| test_reverify_refuses_dependency_drift_with_actionable_message | owner.controller.validation | Attribute for owner.controller.validation in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 698 |
| test_reverify_refuses_dependency_drift_with_actionable_message | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 699 |
| test_reverify_refuses_dependency_drift_with_actionable_message | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 700 |
| test_reverify_refuses_dependency_drift_with_actionable_message | rows | Local binding for rows in test_reverify_refuses_dependency_drift_with_actionable_message; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 701 |
| test_reverify_refuses_dependency_drift_with_actionable_message.comprehension_703 | entry | Comprehension item for entry in test_reverify_refuses_dependency_drift_with_actionable_message.comprehension_703; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 703 |
| test_reapproval_reseals_rebound_tool_dependencies | tmp_path | Parameter for tmp path in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 706 |
| test_reapproval_reseals_rebound_tool_dependencies | monkeypatch | Parameter for monkeypatch in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 706 |
| test_reapproval_reseals_rebound_tool_dependencies | SimpleNamespace | Imported dependency for SimpleNamespace in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 708 |
| test_reapproval_reseals_rebound_tool_dependencies | registry | Imported dependency for registry in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 710 |
| test_reapproval_reseals_rebound_tool_dependencies | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 712 |
| test_reapproval_reseals_rebound_tool_dependencies | service | Local binding for service in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 714 |
| test_reapproval_reseals_rebound_tool_dependencies | app | Local binding for app in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 714 |
| test_reapproval_reseals_rebound_tool_dependencies | fixture | Local binding for fixture in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 714 |
| test_reapproval_reseals_rebound_tool_dependencies | tool_name | Validated public tool identifier within the configured storage boundary. | Return type of drift_tool_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 715 |
| test_reapproval_reseals_rebound_tool_dependencies | sessions | Local binding for sessions in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 716 |
| test_reapproval_reseals_rebound_tool_dependencies | owner | Local binding for owner in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 717 |
| test_reapproval_reseals_rebound_tool_dependencies | owner.controller.security | Attribute for owner.controller.security in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 718 |
| test_reapproval_reseals_rebound_tool_dependencies | owner.controller.validation | Attribute for owner.controller.validation in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 719 |
| test_reapproval_reseals_rebound_tool_dependencies | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 720 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 725 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve | candidate | Parameter for candidate in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 725 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 725 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve | reviewed | Parameter for reviewed in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 725 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve | candidate.approved | Attribute for candidate.approved in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 728 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 730 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify | candidate | Parameter for candidate in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 730 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify | origin | Parameter for origin in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 730 |
| test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify | candidate.verified | Attribute for candidate.verified in test_reapproval_reseals_rebound_tool_dependencies.Supervisor.verify; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 732 |
| test_reapproval_reseals_rebound_tool_dependencies | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 735 |
| test_reapproval_reseals_rebound_tool_dependencies | request | Local binding for request in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 738 |
| test_reapproval_reseals_rebound_tool_dependencies | rows | Local binding for rows in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 740 |
| test_reapproval_reseals_rebound_tool_dependencies | stored | Local binding for stored in test_reapproval_reseals_rebound_tool_dependencies; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 742 |
| test_describe_app_drops_stale_guidance_after_reseal | tmp_path | Parameter for tmp path in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 747 |
| test_describe_app_drops_stale_guidance_after_reseal | monkeypatch | Parameter for monkeypatch in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 747 |
| test_describe_app_drops_stale_guidance_after_reseal | SimpleNamespace | Imported dependency for SimpleNamespace in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 749 |
| test_describe_app_drops_stale_guidance_after_reseal | registry | Imported dependency for registry in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 751 |
| test_describe_app_drops_stale_guidance_after_reseal | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 753 |
| test_describe_app_drops_stale_guidance_after_reseal | service | Local binding for service in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 755 |
| test_describe_app_drops_stale_guidance_after_reseal | app | Local binding for app in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 755 |
| test_describe_app_drops_stale_guidance_after_reseal | fixture | Local binding for fixture in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 755 |
| test_describe_app_drops_stale_guidance_after_reseal | sessions | Local binding for sessions in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 757 |
| test_describe_app_drops_stale_guidance_after_reseal | owner | Local binding for owner in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 758 |
| test_describe_app_drops_stale_guidance_after_reseal | owner.controller.security | Attribute for owner.controller.security in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 759 |
| test_describe_app_drops_stale_guidance_after_reseal | owner.controller.validation | Attribute for owner.controller.validation in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 760 |
| test_describe_app_drops_stale_guidance_after_reseal | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 761 |
| test_describe_app_drops_stale_guidance_after_reseal | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 762 |
| test_describe_app_drops_stale_guidance_after_reseal | request | Local binding for request in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 763 |
| test_describe_app_drops_stale_guidance_after_reseal | described | Local binding for described in test_describe_app_drops_stale_guidance_after_reseal; use the enclosing contract and type below. | Return type of describe_app; see its callable contract | Enclosing invocation or class/instance lifetime | 766 |
| test_describe_app_drops_stale_guidance_after_reverify | tmp_path | Parameter for tmp path in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 772 |
| test_describe_app_drops_stale_guidance_after_reverify | monkeypatch | Parameter for monkeypatch in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 772 |
| test_describe_app_drops_stale_guidance_after_reverify | SimpleNamespace | Imported dependency for SimpleNamespace in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 774 |
| test_describe_app_drops_stale_guidance_after_reverify | registry | Imported dependency for registry in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 776 |
| test_describe_app_drops_stale_guidance_after_reverify | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 778 |
| test_describe_app_drops_stale_guidance_after_reverify | service | Local binding for service in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 780 |
| test_describe_app_drops_stale_guidance_after_reverify | app | Local binding for app in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 780 |
| test_describe_app_drops_stale_guidance_after_reverify | fixture | Local binding for fixture in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 780 |
| test_describe_app_drops_stale_guidance_after_reverify | sessions | Local binding for sessions in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 782 |
| test_describe_app_drops_stale_guidance_after_reverify | owner | Local binding for owner in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 783 |
| test_describe_app_drops_stale_guidance_after_reverify | owner.controller.security | Attribute for owner.controller.security in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 784 |
| test_describe_app_drops_stale_guidance_after_reverify | owner.controller.validation | Attribute for owner.controller.validation in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 785 |
| test_describe_app_drops_stale_guidance_after_reverify | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 786 |
| test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 791 |
| test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify | candidate | Parameter for candidate in test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 791 |
| test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify | origin | Parameter for origin in test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 791 |
| test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify | candidate.verified | Attribute for candidate.verified in test_describe_app_drops_stale_guidance_after_reverify.Supervisor.verify; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 793 |
| test_describe_app_drops_stale_guidance_after_reverify | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 796 |
| test_describe_app_drops_stale_guidance_after_reverify | request | Local binding for request in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 799 |
| test_describe_app_drops_stale_guidance_after_reverify | described | Local binding for described in test_describe_app_drops_stale_guidance_after_reverify; use the enclosing contract and type below. | Return type of describe_app; see its callable contract | Enclosing invocation or class/instance lifetime | 801 |
| test_catalog_view_refreshes_label_and_description_together | tmp_path | Parameter for tmp path in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 806 |
| test_catalog_view_refreshes_label_and_description_together | monkeypatch | Parameter for monkeypatch in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 806 |
| test_catalog_view_refreshes_label_and_description_together | SimpleNamespace | Imported dependency for SimpleNamespace in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 808 |
| test_catalog_view_refreshes_label_and_description_together | registry | Imported dependency for registry in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 810 |
| test_catalog_view_refreshes_label_and_description_together | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 812 |
| test_catalog_view_refreshes_label_and_description_together | catalog_view | Imported dependency for catalog view in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 813 |
| test_catalog_view_refreshes_label_and_description_together | service | Local binding for service in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 815 |
| test_catalog_view_refreshes_label_and_description_together | app | Local binding for app in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 815 |
| test_catalog_view_refreshes_label_and_description_together | fixture | Local binding for fixture in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 815 |
| test_catalog_view_refreshes_label_and_description_together | sessions | Local binding for sessions in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 817 |
| test_catalog_view_refreshes_label_and_description_together | owner | Local binding for owner in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 818 |
| test_catalog_view_refreshes_label_and_description_together | owner.controller.security | Attribute for owner.controller.security in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 819 |
| test_catalog_view_refreshes_label_and_description_together | owner.controller.validation | Attribute for owner.controller.validation in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 820 |
| test_catalog_view_refreshes_label_and_description_together | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 821 |
| test_catalog_view_refreshes_label_and_description_together | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 822 |
| test_catalog_view_refreshes_label_and_description_together | request | Local binding for request in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 823 |
| test_catalog_view_refreshes_label_and_description_together.Dropdown.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 828 |
| test_catalog_view_refreshes_label_and_description_together.Dropdown.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 828 |
| test_catalog_view_refreshes_label_and_description_together.Dropdown.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 829 |
| test_catalog_view_refreshes_label_and_description_together | gr | Local binding for gr in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 831 |
| test_catalog_view_refreshes_label_and_description_together | update | Local binding for update in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of catalog_view; see its callable contract | Enclosing invocation or class/instance lifetime | 832, 839 |
| test_catalog_view_refreshes_label_and_description_together | described | Local binding for described in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of catalog_view; see its callable contract | Enclosing invocation or class/instance lifetime | 832, 839 |
| test_catalog_view_refreshes_label_and_description_together | owned | Local binding for owned in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of catalog_view; see its callable contract | Enclosing invocation or class/instance lifetime | 832 |
| test_catalog_view_refreshes_label_and_description_together | _ | Local binding for  in test_catalog_view_refreshes_label_and_description_together; use the enclosing contract and type below. | Return type of catalog_view; see its callable contract | Enclosing invocation or class/instance lifetime | 839 |
| test_catalog_refresh_binding_updates_description_with_choices | tmp_path | Parameter for tmp path in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 845 |
| test_catalog_refresh_binding_updates_description_with_choices | monkeypatch | Parameter for monkeypatch in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 845 |
| test_catalog_refresh_binding_updates_description_with_choices | SimpleNamespace | Imported dependency for SimpleNamespace in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 847 |
| test_catalog_refresh_binding_updates_description_with_choices | candidates | Imported dependency for candidates in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 849 |
| test_catalog_refresh_binding_updates_description_with_choices | build_apps_catalog | Imported dependency for build apps catalog in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 850 |
| test_catalog_refresh_binding_updates_description_with_choices | bindings | Local binding for bindings in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 853 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 858 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__init__ | args | Parameter for args in test_catalog_refresh_binding_updates_description_with_choices.Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 858 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 858 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 859 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__init__ | self.events | Attribute for events in test_catalog_refresh_binding_updates_description_with_choices.Component.__init__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 860 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 863 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 866 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__exit__ | args | Parameter for args in test_catalog_refresh_binding_updates_description_with_choices.Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 866 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 869 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 869 |
| test_catalog_refresh_binding_updates_description_with_choices.Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 870 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 879 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result | fn | Parameter for fn in test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 879 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result | size | Parameter for size in test_catalog_refresh_binding_updates_description_with_choices.Dialog.guard_result; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 879 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 882 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final | fn | Parameter for fn in test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 882 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final | size | Parameter for size in test_catalog_refresh_binding_updates_description_with_choices.Dialog.wrap_stream_final; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 882 |
| test_catalog_refresh_binding_updates_description_with_choices.Dialog.outputs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 885 |
| test_catalog_refresh_binding_updates_description_with_choices | gr | Local binding for gr in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 888 |
| test_catalog_refresh_binding_updates_description_with_choices.comprehension_889 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 891 |
| test_catalog_refresh_binding_updates_description_with_choices | gr.skip | Attribute for gr.skip in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 907 |
| test_catalog_refresh_binding_updates_description_with_choices | gr.update | Attribute for gr.update in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 908 |
| test_catalog_refresh_binding_updates_description_with_choices | status | Local binding for status in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Return type of Component; see its callable contract | Enclosing invocation or class/instance lifetime | 909 |
| test_catalog_refresh_binding_updates_description_with_choices | workspace | Local binding for workspace in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 910 |
| test_catalog_refresh_binding_updates_description_with_choices | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 911 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_912 | token | Callback parameter for token in test_catalog_refresh_binding_updates_description_with_choices.lambda_912; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 912 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_912 | request | Callback parameter for request in test_catalog_refresh_binding_updates_description_with_choices.lambda_912; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 912 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_913 | selected | Callback parameter for selected in test_catalog_refresh_binding_updates_description_with_choices.lambda_913; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 913 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_913 | token | Callback parameter for token in test_catalog_refresh_binding_updates_description_with_choices.lambda_913; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 913 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_913 | request | Callback parameter for request in test_catalog_refresh_binding_updates_description_with_choices.lambda_913; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 913 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_914 | owned | Callback parameter for owned in test_catalog_refresh_binding_updates_description_with_choices.lambda_914; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 914 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_914 | request | Callback parameter for request in test_catalog_refresh_binding_updates_description_with_choices.lambda_914; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 914 |
| test_catalog_refresh_binding_updates_description_with_choices.lambda_916 | fn | Callback parameter for fn in test_catalog_refresh_binding_updates_description_with_choices.lambda_916; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 916 |
| test_catalog_refresh_binding_updates_description_with_choices | outputs | Local binding for outputs in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 917 |
| test_catalog_refresh_binding_updates_description_with_choices | refreshed | Local binding for refreshed in test_catalog_refresh_binding_updates_description_with_choices; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 921 |
| test_reverify_reseals_only_after_independent_gates_pass | tmp_path | Parameter for tmp path in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 926 |
| test_reverify_reseals_only_after_independent_gates_pass | monkeypatch | Parameter for monkeypatch in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 926 |
| test_reverify_reseals_only_after_independent_gates_pass | SimpleNamespace | Imported dependency for SimpleNamespace in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 928 |
| test_reverify_reseals_only_after_independent_gates_pass | registry | Imported dependency for registry in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 930 |
| test_reverify_reseals_only_after_independent_gates_pass | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 932 |
| test_reverify_reseals_only_after_independent_gates_pass | service | Local binding for service in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 934 |
| test_reverify_reseals_only_after_independent_gates_pass | app | Local binding for app in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 934 |
| test_reverify_reseals_only_after_independent_gates_pass | fixture | Local binding for fixture in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 934 |
| test_reverify_reseals_only_after_independent_gates_pass | calls | Local binding for calls in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 936 |
| test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 941 |
| test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify | candidate | Parameter for candidate in test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 941 |
| test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify | origin | Parameter for origin in test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 941 |
| test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify | candidate.verified | Attribute for candidate.verified in test_reverify_reseals_only_after_independent_gates_pass.Supervisor.verify; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 944 |
| test_reverify_reseals_only_after_independent_gates_pass | sessions | Local binding for sessions in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 947 |
| test_reverify_reseals_only_after_independent_gates_pass | owner | Local binding for owner in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 948 |
| test_reverify_reseals_only_after_independent_gates_pass | owner.controller.security | Attribute for owner.controller.security in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 949 |
| test_reverify_reseals_only_after_independent_gates_pass | owner.controller.validation | Attribute for owner.controller.validation in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 950 |
| test_reverify_reseals_only_after_independent_gates_pass | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 951 |
| test_reverify_reseals_only_after_independent_gates_pass | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 952 |
| test_reverify_reseals_only_after_independent_gates_pass | rows | Local binding for rows in test_reverify_reseals_only_after_independent_gates_pass; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 955 |
| test_reverify_keeps_stale_record_when_gates_fail | tmp_path | Parameter for tmp path in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 961 |
| test_reverify_keeps_stale_record_when_gates_fail | monkeypatch | Parameter for monkeypatch in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 961 |
| test_reverify_keeps_stale_record_when_gates_fail | SimpleNamespace | Imported dependency for SimpleNamespace in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 963 |
| test_reverify_keeps_stale_record_when_gates_fail | registry | Imported dependency for registry in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 965 |
| test_reverify_keeps_stale_record_when_gates_fail | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 967 |
| test_reverify_keeps_stale_record_when_gates_fail | service | Local binding for service in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 969 |
| test_reverify_keeps_stale_record_when_gates_fail | app | Local binding for app in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 969 |
| test_reverify_keeps_stale_record_when_gates_fail | fixture | Local binding for fixture in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 969 |
| test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 975 |
| test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify | candidate | Parameter for candidate in test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 975 |
| test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify | origin | Parameter for origin in test_reverify_keeps_stale_record_when_gates_fail.Supervisor.verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 975 |
| test_reverify_keeps_stale_record_when_gates_fail | sessions | Local binding for sessions in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 979 |
| test_reverify_keeps_stale_record_when_gates_fail | owner | Local binding for owner in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 980 |
| test_reverify_keeps_stale_record_when_gates_fail | owner.controller.security | Attribute for owner.controller.security in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 981 |
| test_reverify_keeps_stale_record_when_gates_fail | owner.controller.validation | Attribute for owner.controller.validation in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 982 |
| test_reverify_keeps_stale_record_when_gates_fail | owner.controller.get_installed_tools_catalog | Attribute for owner.controller.get installed tools catalog in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 983 |
| test_reverify_keeps_stale_record_when_gates_fail | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 984 |
| test_reverify_keeps_stale_record_when_gates_fail | rows | Local binding for rows in test_reverify_keeps_stale_record_when_gates_fail; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 987 |
| test_reverify_keeps_stale_record_when_gates_fail.comprehension_989 | entry | Comprehension item for entry in test_reverify_keeps_stale_record_when_gates_fail.comprehension_989; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 989 |
