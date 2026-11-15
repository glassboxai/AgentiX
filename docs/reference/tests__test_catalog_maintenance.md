# Reference for tests/test_catalog_maintenance.py

Permanent removal uses trusted temporary packages and authenticated metadata doubles.

Source fingerprint: e07fbe8427b1a8993ad74f9fda5a69bbeab9a6603bd2825e161cb83f4c0a6dc9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### service

Resolve the removal boundary without granting a missing implementation a pass.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_tool_referenced_by_installed_app_is_not_deletable

Installed composite data operations count as dependencies even when GUI is closed.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_invalid_app_source_does_not_hide_dependency

Do not use the executable-only catalog list to decide deletion safety.

Kind: callable. Declared return: Not declared / class. Source line: 32.

### test_confirmed_unused_tool_is_permanently_removed

Preparation is read-only; explicit commit removes only its exact package.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### test_package_change_invalidates_confirmation

A stale prompt cannot permanently delete changed content.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_open_app_lease_blocks_removal_across_library_instances

A second session/process must not delete a package serving an open application.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_browser_paths_are_not_tool_identifiers

Never turn a browser parameter into an unrestricted deletion target.

Kind: callable. Declared return: Not declared / class. Source line: 88.

### test_renamed_member_cannot_preserve_confirmation_digest

File names/content need unambiguous framing, not raw concatenation.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### test_stale_policy_does_not_block_permanent_application_removal

V7-060: removal needs identity, bytes and usage, not a current policy binding.

Kind: callable. Declared return: Not declared / class. Source line: 113.

### test_stale_policy_still_refuses_changed_application_source

A stale policy never authorizes removal of bytes that changed after installation.

Kind: callable. Declared return: Not declared / class. Source line: 129.

### test_copied_app_approval_cannot_authorize_another_library

Protected app records must bind their root, not only a namespace filename.

Kind: callable. Declared return: Not declared / class. Source line: 140.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | installed | Imported dependency for installed in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | library | Imported dependency for library in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | published_with_tools | Imported dependency for published with tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| service | tmp_path | Parameter for tmp path in service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| service | fixture | Parameter for fixture in service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| service | apps | Parameter for apps in service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| service | CatalogMaintenance | Imported dependency for CatalogMaintenance in service; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| service.lambda_20 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 20 |
| test_tool_referenced_by_installed_app_is_not_deletable | tmp_path | Parameter for tmp path in test_tool_referenced_by_installed_app_is_not_deletable; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_tool_referenced_by_installed_app_is_not_deletable | apps | Local binding for apps in test_tool_referenced_by_installed_app_is_not_deletable; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_tool_referenced_by_installed_app_is_not_deletable | app | Local binding for app in test_tool_referenced_by_installed_app_is_not_deletable; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_tool_referenced_by_installed_app_is_not_deletable | fixture | Local binding for fixture in test_tool_referenced_by_installed_app_is_not_deletable; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_invalid_app_source_does_not_hide_dependency | tmp_path | Parameter for tmp path in test_invalid_app_source_does_not_hide_dependency; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| test_invalid_app_source_does_not_hide_dependency | apps | Local binding for apps in test_invalid_app_source_does_not_hide_dependency; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_invalid_app_source_does_not_hide_dependency | app | Local binding for app in test_invalid_app_source_does_not_hide_dependency; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_invalid_app_source_does_not_hide_dependency | fixture | Local binding for fixture in test_invalid_app_source_does_not_hide_dependency; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_confirmed_unused_tool_is_permanently_removed | tmp_path | Parameter for tmp path in test_confirmed_unused_tool_is_permanently_removed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_confirmed_unused_tool_is_permanently_removed | tools | Local binding for tools in test_confirmed_unused_tool_is_permanently_removed; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_confirmed_unused_tool_is_permanently_removed | fixture | Local binding for fixture in test_confirmed_unused_tool_is_permanently_removed; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_confirmed_unused_tool_is_permanently_removed | operations | Local binding for operations in test_confirmed_unused_tool_is_permanently_removed; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_confirmed_unused_tool_is_permanently_removed | snapshot | Local binding for snapshot in test_confirmed_unused_tool_is_permanently_removed; use the enclosing contract and type below. | Return type of prepare_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_package_change_invalidates_confirmation | tmp_path | Parameter for tmp path in test_package_change_invalidates_confirmation; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_package_change_invalidates_confirmation | tools | Local binding for tools in test_package_change_invalidates_confirmation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_package_change_invalidates_confirmation | fixture | Local binding for fixture in test_package_change_invalidates_confirmation; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_package_change_invalidates_confirmation | operations | Local binding for operations in test_package_change_invalidates_confirmation; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_package_change_invalidates_confirmation | snapshot | Local binding for snapshot in test_package_change_invalidates_confirmation; use the enclosing contract and type below. | Return type of prepare_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_open_app_lease_blocks_removal_across_library_instances | tmp_path | Parameter for tmp path in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_open_app_lease_blocks_removal_across_library_instances | apps | Local binding for apps in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_open_app_lease_blocks_removal_across_library_instances | app | Local binding for app in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_open_app_lease_blocks_removal_across_library_instances | fixture | Local binding for fixture in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_open_app_lease_blocks_removal_across_library_instances | lease | Local binding for lease in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of open_lease; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_open_app_lease_blocks_removal_across_library_instances | operations | Local binding for operations in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_open_app_lease_blocks_removal_across_library_instances | snapshot | Local binding for snapshot in test_open_app_lease_blocks_removal_across_library_instances; use the enclosing contract and type below. | Return type of prepare_app; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_browser_paths_are_not_tool_identifiers | tmp_path | Parameter for tmp path in test_browser_paths_are_not_tool_identifiers; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| test_browser_paths_are_not_tool_identifiers | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| test_browser_paths_are_not_tool_identifiers | tools | Local binding for tools in test_browser_paths_are_not_tool_identifiers; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_browser_paths_are_not_tool_identifiers | fixture | Local binding for fixture in test_browser_paths_are_not_tool_identifiers; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_renamed_member_cannot_preserve_confirmation_digest | tmp_path | Parameter for tmp path in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_renamed_member_cannot_preserve_confirmation_digest | tools | Local binding for tools in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_renamed_member_cannot_preserve_confirmation_digest | fixture | Local binding for fixture in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| test_renamed_member_cannot_preserve_confirmation_digest | operations | Local binding for operations in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| test_renamed_member_cannot_preserve_confirmation_digest | folder | Local binding for folder in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_renamed_member_cannot_preserve_confirmation_digest | snapshot | Local binding for snapshot in test_renamed_member_cannot_preserve_confirmation_digest; use the enclosing contract and type below. | Return type of prepare_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_stale_policy_does_not_block_permanent_application_removal | tmp_path | Parameter for tmp path in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 113 |
| test_stale_policy_does_not_block_permanent_application_removal | monkeypatch | Parameter for monkeypatch in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 113 |
| test_stale_policy_does_not_block_permanent_application_removal | apps | Local binding for apps in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_policy_does_not_block_permanent_application_removal | app | Local binding for app in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_policy_does_not_block_permanent_application_removal | fixture | Local binding for fixture in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| test_stale_policy_does_not_block_permanent_application_removal | stale | Local binding for stale in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_stale_policy_does_not_block_permanent_application_removal | operations | Local binding for operations in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_stale_policy_does_not_block_permanent_application_removal | snapshot | Local binding for snapshot in test_stale_policy_does_not_block_permanent_application_removal; use the enclosing contract and type below. | Return type of prepare_app; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_stale_policy_still_refuses_changed_application_source | tmp_path | Parameter for tmp path in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_stale_policy_still_refuses_changed_application_source | monkeypatch | Parameter for monkeypatch in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_stale_policy_still_refuses_changed_application_source | apps | Local binding for apps in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_stale_policy_still_refuses_changed_application_source | app | Local binding for app in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_stale_policy_still_refuses_changed_application_source | fixture | Local binding for fixture in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_stale_policy_still_refuses_changed_application_source | operations | Local binding for operations in test_stale_policy_still_refuses_changed_application_source; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_copied_app_approval_cannot_authorize_another_library | tmp_path | Parameter for tmp path in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_copied_app_approval_cannot_authorize_another_library | shutil | Imported dependency for shutil in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 142 |
| test_copied_app_approval_cannot_authorize_another_library | Protector | Imported dependency for Protector in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 144 |
| test_copied_app_approval_cannot_authorize_another_library | InstalledApps | Imported dependency for InstalledApps in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 146 |
| test_copied_app_approval_cannot_authorize_another_library | apps | Local binding for apps in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_copied_app_approval_cannot_authorize_another_library | app | Local binding for app in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_copied_app_approval_cannot_authorize_another_library | fixture | Local binding for fixture in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_copied_app_approval_cannot_authorize_another_library | other | Local binding for other in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_copied_app_approval_cannot_authorize_another_library | review | Local binding for review in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 154 |
| test_copied_app_approval_cannot_authorize_another_library | record | Local binding for record in test_copied_app_approval_cannot_authorize_another_library; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
