# Reference for tests/unit/test_iac.py

IAC-001 offline contracts using trusted temporary data and PowerShell providers.

No package manager, network request, installer or application server is started.

Source fingerprint: c86dade24e32b30ec4e00a3616621fb7238b695941a134180e5ee6adb9c44c8a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### powershell

Evaluate a trusted test body, failing on PowerShell errors and malformed JSON.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_plan_is_read_only_and_idempotent

A converged inventory produces no changes and never invokes an actuator.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### test_configuration_rejects_unsafe_or_unknown_values

Models, Python, ports and configuration fields cannot silently widen scope.

Kind: callable. Declared return: Not declared / class. Source line: 58.

### test_plan_rejects_state_drift_and_tampering

Changes to the configuration, planned actions or observed state invalidate review.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_missing_model_requires_explicit_download_and_port_conflict_blocks

Ordinary application of a plan cannot download models or replace listeners.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_failed_resource_stops_dependent_changes

A failed prerequisite is not masked and does not start dependent resources.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### test_paths_and_reparse_boundaries

Managed paths accept spaces but reject siblings and existing links.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_runtime_settings_support_managed_launch

Managed startup selects new storage and a port without changing legacy defaults.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### test_runtime_rejects_invalid_port

Invalid deployment configuration fails before network or storage startup.

Kind: callable. Declared return: Not declared / class. Source line: 140.

### test_inventory_fingerprint_accepts_adapted_empty_scalars

IAC-ERR-001: observed process/JSON scalar wrappers must hash without property errors.

Kind: callable. Declared return: Not declared / class. Source line: 148.

### test_converged_apply_does_not_call_actuators

An unchanged second application cannot reinstall packages or rewrite launchers.

Kind: callable. Declared return: Not declared / class. Source line: 156.

### test_unknown_model_digest_blocks_even_with_download_consent

A changed installed tag must not be silently replaced after review.

Kind: callable. Declared return: Not declared / class. Source line: 164.

### test_configuration_change_invalidates_review

A port change after review requires a new plan even when current observations match.

Kind: callable. Declared return: Not declared / class. Source line: 173.

### test_incompatible_prerequisite_is_not_upgraded

Installed foreign versions are diagnosed, not scheduled for replacement.

Kind: callable. Declared return: Not declared / class. Source line: 181.

### test_managed_file_links_are_rejected

Existing directory junctions cannot redirect managed writes outside their root.

Kind: callable. Declared return: Not declared / class. Source line: 190.

### test_plan_inventory_does_not_create_files_or_contact_network

Real inventory with absent prerequisites is read-only and network is explicitly doubled.

Kind: callable. Declared return: Not declared / class. Source line: 206.

### test_corrupt_download_is_rejected_before_extraction

Pinned archives cannot be applied when a fake downloader returns changed bytes.

Kind: callable. Declared return: Not declared / class. Source line: 217.

### test_environment_refuses_unowned_existing_directory

Provisioning never adopts or clears another environment directory.

Kind: callable. Declared return: Not declared / class. Source line: 228.

### test_invalid_runtime_configuration_fails_before_start

The managed launcher cannot silently reinterpret ambiguous settings.

Kind: callable. Declared return: Not declared / class. Source line: 241.

### test_windows_powershell_adapter_without_ambient_modules

IAC-ERR-002: DSC resources load OS modules without trusting an inherited module path.

Kind: callable. Declared return: Not declared / class. Source line: 249.

### test_launcher_restores_process_configuration_after_failure

IAC-ERR-003: a closed/failed managed launcher must not change later legacy launches.

Kind: callable. Declared return: Not declared / class. Source line: 267.

### test_fingerprints_match_windows_powershell_and_powershell_core

IAC-ERR-004: cross-edition locale sorting cannot invalidate an unchanged DSC plan.

Kind: callable. Declared return: Not declared / class. Source line: 278.

### test_windows_process_adapter_accepts_stderr_with_success

IAC-ERR-005: Windows PowerShell stderr records do not override a native zero exit.

Kind: callable. Declared return: Not declared / class. Source line: 298.

### test_zero_exit_without_convergence_stops_dependents

IAC-ERR-006: a successful installer exit alone cannot authorize dependent work.

Kind: callable. Declared return: Not declared / class. Source line: 318.

### test_managed_root_resolves_windows_host_redirection

IAC-ERR-007: managed launch paths use the OS-resolved location, not an app-host alias.

Kind: callable. Declared return: Not declared / class. Source line: 327.

### test_prerequisite_signatures_reject_invalid_or_foreign_publishers

New native prerequisites require a valid signature from their expected publisher.

Kind: callable. Declared return: Not declared / class. Source line: 348.

### test_prerequisite_signature_accepts_reviewed_publisher

A verified vendor signature permits the already hash-pinned prerequisite.

Kind: callable. Declared return: Not declared / class. Source line: 360.

### test_missing_package_manager_blocks_missing_python

A missing Windows package manager is diagnosed before dependent installation.

Kind: callable. Declared return: Not declared / class. Source line: 368.

### test_dependency_install_cannot_inherit_pip_target_or_extra_sources

IAC-ERR-008: ambient pip variables cannot redirect writes outside the owned environment.

Kind: callable. Declared return: Not declared / class. Source line: 376.

### test_native_argument_quoting_preserves_data

Spaces, quotes, trailing backslashes and shell-like text stay literal arguments.

Kind: callable. Declared return: Not declared / class. Source line: 392.

### test_launcher_preserves_absent_environment_variables

IAC-ERR-009: unset legacy settings must remain absent, not empty strings.

Kind: callable. Declared return: Not declared / class. Source line: 411.

### test_location_receipt_keeps_deployment_independent_of_host_alias

IAC-ERR-007: a normal terminal must find the physical deployment created by a packaged host.

Kind: callable. Declared return: Not declared / class. Source line: 421.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| module | MODULE | Module binding for MODULE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | PWSH | Module binding for PWSH in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 18 |
| powershell | body | Parameter for body in powershell; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| powershell | command | Local binding for command in powershell; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 23, 35 |
| powershell | local | Managed resource for local in powershell; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 34 |
| powershell | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_plan_is_read_only_and_idempotent | tmp_path | Parameter for tmp path in test_plan_is_read_only_and_idempotent; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_plan_is_read_only_and_idempotent | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_configuration_rejects_unsafe_or_unknown_values | field | Parameter for field in test_configuration_rejects_unsafe_or_unknown_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| test_configuration_rejects_unsafe_or_unknown_values | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_plan_rejects_state_drift_and_tampering | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_missing_model_requires_explicit_download_and_port_conflict_blocks | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_failed_resource_stops_dependent_changes | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| test_paths_and_reparse_boundaries | tmp_path | Parameter for tmp path in test_paths_and_reparse_boundaries; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_paths_and_reparse_boundaries | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_runtime_settings_support_managed_launch | tmp_path | Parameter for tmp path in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_runtime_settings_support_managed_launch | Settings | Imported dependency for Settings in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 120 |
| test_runtime_settings_support_managed_launch | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 122 |
| test_runtime_settings_support_managed_launch | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| test_runtime_settings_support_managed_launch | legacy | Local binding for legacy in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_runtime_rejects_invalid_port | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_runtime_rejects_invalid_port | tmp_path | Parameter for tmp path in test_runtime_rejects_invalid_port; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_runtime_rejects_invalid_port | Settings | Imported dependency for Settings in test_runtime_rejects_invalid_port; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 142 |
| test_inventory_fingerprint_accepts_adapted_empty_scalars | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_converged_apply_does_not_call_actuators | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| test_unknown_model_digest_blocks_even_with_download_consent | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_configuration_change_invalidates_review | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_incompatible_prerequisite_is_not_upgraded | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| test_managed_file_links_are_rejected | tmp_path | Parameter for tmp path in test_managed_file_links_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 190 |
| test_managed_file_links_are_rejected | outside | Local binding for outside in test_managed_file_links_are_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_managed_file_links_are_rejected | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 194 |
| test_managed_file_links_are_rejected | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_plan_inventory_does_not_create_files_or_contact_network | tmp_path | Parameter for tmp path in test_plan_inventory_does_not_create_files_or_contact_network; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 206 |
| test_plan_inventory_does_not_create_files_or_contact_network | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_corrupt_download_is_rejected_before_extraction | tmp_path | Parameter for tmp path in test_corrupt_download_is_rejected_before_extraction; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 217 |
| test_corrupt_download_is_rejected_before_extraction | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_environment_refuses_unowned_existing_directory | tmp_path | Parameter for tmp path in test_environment_refuses_unowned_existing_directory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 228 |
| test_environment_refuses_unowned_existing_directory | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| test_invalid_runtime_configuration_fails_before_start | environment | Parameter for environment in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 241 |
| test_invalid_runtime_configuration_fails_before_start | tmp_path | Parameter for tmp path in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 241 |
| test_invalid_runtime_configuration_fails_before_start | Settings | Imported dependency for Settings in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 243 |
| test_windows_powershell_adapter_without_ambient_modules | executable | Local binding for executable in test_windows_powershell_adapter_without_ambient_modules; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 251 |
| test_windows_powershell_adapter_without_ambient_modules | command | Local binding for command in test_windows_powershell_adapter_without_ambient_modules; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 252 |
| test_windows_powershell_adapter_without_ambient_modules | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
| test_launcher_restores_process_configuration_after_failure | tmp_path | Parameter for tmp path in test_launcher_restores_process_configuration_after_failure; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| test_launcher_restores_process_configuration_after_failure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 269 |
| test_fingerprints_match_windows_powershell_and_powershell_core | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 280 |
| test_fingerprints_match_windows_powershell_and_powershell_core | executable | Local binding for executable in test_fingerprints_match_windows_powershell_and_powershell_core; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 281 |
| test_fingerprints_match_windows_powershell_and_powershell_core | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 282 |
| test_windows_process_adapter_accepts_stderr_with_success | executable | Local binding for executable in test_windows_process_adapter_accepts_stderr_with_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 300 |
| test_windows_process_adapter_accepts_stderr_with_success | command | Local binding for command in test_windows_process_adapter_accepts_stderr_with_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 301 |
| test_windows_process_adapter_accepts_stderr_with_success | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
| test_zero_exit_without_convergence_stops_dependents | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 320 |
| test_managed_root_resolves_windows_host_redirection | tmp_path | Parameter for tmp path in test_managed_root_resolves_windows_host_redirection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 327 |
| test_managed_root_resolves_windows_host_redirection | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | status | Parameter for status in test_prerequisite_signatures_reject_invalid_or_foreign_publishers; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | publisher | Parameter for publisher in test_prerequisite_signatures_reject_invalid_or_foreign_publishers; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 348 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 350 |
| test_prerequisite_signature_accepts_reviewed_publisher | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 362 |
| test_missing_package_manager_blocks_missing_python | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 370 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | tmp_path | Parameter for tmp path in test_dependency_install_cannot_inherit_pip_target_or_extra_sources; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 376 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | body | Local binding for body in test_dependency_install_cannot_inherit_pip_target_or_extra_sources; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 378 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 383 |
| test_native_argument_quoting_preserves_data | values | Local binding for values in test_native_argument_quoting_preserves_data; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 394 |
| test_native_argument_quoting_preserves_data | payload | Local binding for payload in test_native_argument_quoting_preserves_data; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 400 |
| test_native_argument_quoting_preserves_data | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 401 |
| test_launcher_preserves_absent_environment_variables | tmp_path | Parameter for tmp path in test_launcher_preserves_absent_environment_variables; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 411 |
| test_launcher_preserves_absent_environment_variables | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 413 |
| test_location_receipt_keeps_deployment_independent_of_host_alias | tmp_path | Parameter for tmp path in test_location_receipt_keeps_deployment_independent_of_host_alias; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 421 |
| test_location_receipt_keeps_deployment_independent_of_host_alias | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 423 |
