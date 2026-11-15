# Reference for tests/unit/test_iac.py

IAC-001 offline contracts using trusted temporary data and PowerShell providers.

No package manager, network request, installer or application server is started.

Source fingerprint: 57bca57e9ef12e621650bd2c3c07218aa41dffde87400ceb0c8529fa1211fe99

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### powershell

Evaluate a trusted test body, failing on PowerShell errors and malformed JSON.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_plan_is_read_only_and_idempotent

A converged inventory produces no changes and never invokes an actuator.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### test_configuration_rejects_unsafe_or_unknown_values

Models, Python, ports and configuration fields cannot silently widen scope.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### test_schema_two_configuration_selects_separate_home_and_artifact_roots

IAC-010: reviewed schema-2 roots isolate runtime state from tool artifacts.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### test_checked_in_schema_two_configuration_declares_approved_roots

IAC-010: the reviewed profile declares the approved V7 runtime and artifact roots.

Kind: callable. Declared return: Not declared / class. Source line: 88.

### test_schema_two_configuration_rejects_relative_roots

IAC-010: configurable deployment roots must remain explicit absolute paths.

Kind: callable. Declared return: Not declared / class. Source line: 101.

### test_schema_two_configuration_rejects_overlapping_runtime_and_artifact_roots

IAC-010: artifact storage cannot be a writable subdirectory of managed runtime state.

Kind: callable. Declared return: Not declared / class. Source line: 114.

### test_plan_rejects_state_drift_and_tampering

Changes to the configuration, planned actions or observed state invalidate review.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### test_ollama_state_does_not_change_plan_and_port_conflict_blocks

External Ollama state cannot affect IaC planning or trigger provisioning.

Kind: callable. Declared return: Not declared / class. Source line: 135.

### test_failed_resource_stops_dependent_changes

A failed prerequisite is not masked and does not start dependent resources.

Kind: callable. Declared return: Not declared / class. Source line: 148.

### test_paths_and_reparse_boundaries

Managed paths accept spaces but reject siblings and existing links.

Kind: callable. Declared return: Not declared / class. Source line: 162.

### test_runtime_settings_support_managed_launch

Managed startup selects new storage and a port without changing legacy defaults.

Kind: callable. Declared return: Not declared / class. Source line: 172.

### test_runtime_rejects_invalid_port

Invalid deployment configuration fails before network or storage startup.

Kind: callable. Declared return: Not declared / class. Source line: 201.

### test_inventory_fingerprint_accepts_adapted_empty_scalars

IAC-ERR-001: observed process/JSON scalar wrappers must hash without property errors.

Kind: callable. Declared return: Not declared / class. Source line: 209.

### test_converged_apply_does_not_call_actuators

An unchanged second application cannot reinstall packages or rewrite launchers.

Kind: callable. Declared return: Not declared / class. Source line: 217.

### test_ollama_metadata_is_not_an_iac_blocker

Model identity belongs to application-level TOFU, not the installer plan.

Kind: callable. Declared return: Not declared / class. Source line: 225.

### test_configuration_change_invalidates_review

A port change after review requires a new plan even when current observations match.

Kind: callable. Declared return: Not declared / class. Source line: 233.

### test_incompatible_prerequisite_is_not_upgraded

Installed foreign versions are diagnosed, not scheduled for replacement.

Kind: callable. Declared return: Not declared / class. Source line: 241.

### test_managed_file_links_are_rejected

Existing directory junctions cannot redirect managed writes outside their root.

Kind: callable. Declared return: Not declared / class. Source line: 250.

### test_plan_inventory_does_not_create_files_or_contact_network

Real inventory with absent prerequisites is read-only and network is explicitly doubled.

Kind: callable. Declared return: Not declared / class. Source line: 266.

### test_corrupt_download_is_rejected_before_extraction

Pinned archives cannot be applied when a fake downloader returns changed bytes.

Kind: callable. Declared return: Not declared / class. Source line: 277.

### test_environment_refuses_unowned_existing_directory

Provisioning never adopts or clears another environment directory.

Kind: callable. Declared return: Not declared / class. Source line: 288.

### test_invalid_runtime_configuration_fails_before_start

The managed launcher cannot silently reinterpret ambiguous settings.

Kind: callable. Declared return: Not declared / class. Source line: 306.

### test_windows_powershell_adapter_without_ambient_modules

IAC-ERR-002: DSC resources load OS modules without trusting an inherited module path.

Kind: callable. Declared return: Not declared / class. Source line: 319.

### test_launcher_restores_process_configuration_after_failure

IAC-ERR-003: a closed/failed managed launcher must not change later legacy launches.

Kind: callable. Declared return: Not declared / class. Source line: 337.

### test_fingerprints_match_windows_powershell_and_powershell_core

IAC-ERR-004: cross-edition locale sorting cannot invalidate an unchanged DSC plan.

Kind: callable. Declared return: Not declared / class. Source line: 348.

### test_windows_process_adapter_accepts_stderr_with_success

IAC-ERR-005: Windows PowerShell stderr records do not override a native zero exit.

Kind: callable. Declared return: Not declared / class. Source line: 368.

### test_iac_process_forwards_stdout_and_stderr_before_exit

IAC-012 forwards each native stream while the child is still running.

Kind: callable. Declared return: Not declared / class. Source line: 388.

### test_iac_process_forward_output_preserves_stream_labels

IAC-012 emits concise labeled console records for both native streams.

Kind: callable. Declared return: Not declared / class. Source line: 414.

### test_iac_process_drains_concurrent_streams_without_failure

IAC-012 drains concurrent stdout/stderr and accepts zero-exit stderr output.

Kind: callable. Declared return: Not declared / class. Source line: 430.

### test_iac_process_preserves_failure_timeout_and_bounded_diagnostics

IAC-012 retains exit failures, deadlines and bounded native diagnostics.

Kind: callable. Declared return: Not declared / class. Source line: 451.

### test_apply_summarizes_dsc_result_without_emitting_its_raw_json

IAC-013 keeps DSC's machine JSON out of the interactive Apply transcript.

Kind: callable. Declared return: Not declared / class. Source line: 472.

### test_zero_exit_without_convergence_stops_dependents

IAC-ERR-006: a successful installer exit alone cannot authorize dependent work.

Kind: callable. Declared return: Not declared / class. Source line: 490.

### test_managed_root_resolves_windows_host_redirection

IAC-ERR-007: managed launch paths use the OS-resolved location, not an app-host alias.

Kind: callable. Declared return: Not declared / class. Source line: 499.

### test_prerequisite_signatures_reject_invalid_or_foreign_publishers

New native prerequisites require a valid signature from their expected publisher.

Kind: callable. Declared return: Not declared / class. Source line: 520.

### test_prerequisite_signature_accepts_reviewed_publisher

A verified vendor signature permits the already hash-pinned prerequisite.

Kind: callable. Declared return: Not declared / class. Source line: 532.

### test_missing_package_manager_blocks_missing_python

A missing Windows package manager is diagnosed before dependent installation.

Kind: callable. Declared return: Not declared / class. Source line: 540.

### test_dependency_install_cannot_inherit_pip_target_or_extra_sources

IAC-ERR-008: ambient pip variables cannot redirect writes outside the owned environment.

Kind: callable. Declared return: Not declared / class. Source line: 548.

### test_environment_install_downloads_only_missing_playwright_chromium

IAC-011 installs Chromium after dependencies when the venv lacks its expected binary.

Kind: callable. Declared return: Not declared / class. Source line: 564.

### test_environment_install_skips_existing_compatible_playwright_chromium

IAC-011 leaves the matching Playwright Chromium binary untouched.

Kind: callable. Declared return: Not declared / class. Source line: 582.

### test_environment_install_reports_playwright_chromium_failure

IAC-011 fails with a Chromium-specific diagnostic when Playwright cannot install it.

Kind: callable. Declared return: Not declared / class. Source line: 601.

### test_launcher_uses_venv_playwright_chromium_path

IAC-011 exports the installed venv Playwright Chromium path to the launcher.

Kind: callable. Declared return: Not declared / class. Source line: 618.

### test_native_argument_quoting_preserves_data

Spaces, quotes, trailing backslashes and shell-like text stay literal arguments.

Kind: callable. Declared return: Not declared / class. Source line: 634.

### test_launcher_preserves_absent_environment_variables

IAC-ERR-009: unset legacy settings must remain absent, not empty strings.

Kind: callable. Declared return: Not declared / class. Source line: 653.

### test_location_receipt_binds_the_configured_deployment_root

IAC-010: receipts preserve only the reviewed schema-2 runtime root.

Kind: callable. Declared return: Not declared / class. Source line: 663.

### test_iac_launch_ignores_external_ollama_state

Managed launch is independent of a reachable server and never provisions it.

Kind: callable. Declared return: Not declared / class. Source line: 673.

### test_iac_configuration_rejects_removed_ollama_fields

Ollama versions and model pins cannot return through installer configuration.

Kind: callable. Declared return: Not declared / class. Source line: 684.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | MODULE | Module binding for MODULE in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 18 |
| module | PWSH | Module binding for PWSH in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 19 |
| powershell | body | Parameter for body in powershell; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22, 25 |
| powershell.lambda_27 | match | Callback parameter for match in powershell.lambda_27; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 27 |
| powershell | command | Local binding for command in powershell; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31, 43 |
| powershell | local | Managed resource for local in powershell; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 42 |
| powershell | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_plan_is_read_only_and_idempotent | tmp_path | Parameter for tmp path in test_plan_is_read_only_and_idempotent; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_plan_is_read_only_and_idempotent | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_configuration_rejects_unsafe_or_unknown_values | field | Parameter for field in test_configuration_rejects_unsafe_or_unknown_values; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| test_configuration_rejects_unsafe_or_unknown_values | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_schema_two_configuration_selects_separate_home_and_artifact_roots | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_checked_in_schema_two_configuration_declares_approved_roots | configuration | Local binding for configuration in test_checked_in_schema_two_configuration_declares_approved_roots; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_schema_two_configuration_rejects_relative_roots | field | Parameter for field in test_schema_two_configuration_rejects_relative_roots; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_schema_two_configuration_rejects_relative_roots | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_schema_two_configuration_rejects_relative_roots | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_schema_two_configuration_rejects_overlapping_runtime_and_artifact_roots | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| test_plan_rejects_state_drift_and_tampering | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_ollama_state_does_not_change_plan_and_port_conflict_blocks | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_failed_resource_stops_dependent_changes | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_paths_and_reparse_boundaries | tmp_path | Parameter for tmp path in test_paths_and_reparse_boundaries; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 162 |
| test_paths_and_reparse_boundaries | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_runtime_settings_support_managed_launch | tmp_path | Parameter for tmp path in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| test_runtime_settings_support_managed_launch | Settings | Imported dependency for Settings in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 174 |
| test_runtime_settings_support_managed_launch | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| test_runtime_settings_support_managed_launch | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_runtime_settings_support_managed_launch | legacy | Local binding for legacy in test_runtime_settings_support_managed_launch; use the enclosing contract and type below. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| test_runtime_rejects_invalid_port | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 201 |
| test_runtime_rejects_invalid_port | tmp_path | Parameter for tmp path in test_runtime_rejects_invalid_port; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 201 |
| test_runtime_rejects_invalid_port | Settings | Imported dependency for Settings in test_runtime_rejects_invalid_port; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 203 |
| test_inventory_fingerprint_accepts_adapted_empty_scalars | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 211 |
| test_converged_apply_does_not_call_actuators | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| test_ollama_metadata_is_not_an_iac_blocker | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| test_configuration_change_invalidates_review | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 235 |
| test_incompatible_prerequisite_is_not_upgraded | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| test_managed_file_links_are_rejected | tmp_path | Parameter for tmp path in test_managed_file_links_are_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 250 |
| test_managed_file_links_are_rejected | outside | Local binding for outside in test_managed_file_links_are_rejected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 252 |
| test_managed_file_links_are_rejected | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 254 |
| test_managed_file_links_are_rejected | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 256 |
| test_plan_inventory_does_not_create_files_or_contact_network | tmp_path | Parameter for tmp path in test_plan_inventory_does_not_create_files_or_contact_network; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 266 |
| test_plan_inventory_does_not_create_files_or_contact_network | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 268 |
| test_corrupt_download_is_rejected_before_extraction | tmp_path | Parameter for tmp path in test_corrupt_download_is_rejected_before_extraction; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 277 |
| test_corrupt_download_is_rejected_before_extraction | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 279 |
| test_environment_refuses_unowned_existing_directory | tmp_path | Parameter for tmp path in test_environment_refuses_unowned_existing_directory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 288 |
| test_environment_refuses_unowned_existing_directory | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 290 |
| test_invalid_runtime_configuration_fails_before_start | overrides | Parameter for overrides in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 306 |
| test_invalid_runtime_configuration_fails_before_start | tmp_path | Parameter for tmp path in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 306 |
| test_invalid_runtime_configuration_fails_before_start | Settings | Imported dependency for Settings in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 308 |
| test_invalid_runtime_configuration_fails_before_start | environment | Local binding for environment in test_invalid_runtime_configuration_fails_before_start; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 310 |
| test_windows_powershell_adapter_without_ambient_modules | executable | Local binding for executable in test_windows_powershell_adapter_without_ambient_modules; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 321 |
| test_windows_powershell_adapter_without_ambient_modules | command | Local binding for command in test_windows_powershell_adapter_without_ambient_modules; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 322 |
| test_windows_powershell_adapter_without_ambient_modules | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 327 |
| test_launcher_restores_process_configuration_after_failure | tmp_path | Parameter for tmp path in test_launcher_restores_process_configuration_after_failure; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 337 |
| test_launcher_restores_process_configuration_after_failure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| test_fingerprints_match_windows_powershell_and_powershell_core | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 350 |
| test_fingerprints_match_windows_powershell_and_powershell_core | executable | Local binding for executable in test_fingerprints_match_windows_powershell_and_powershell_core; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 351 |
| test_fingerprints_match_windows_powershell_and_powershell_core | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 352 |
| test_windows_process_adapter_accepts_stderr_with_success | executable | Local binding for executable in test_windows_process_adapter_accepts_stderr_with_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 370 |
| test_windows_process_adapter_accepts_stderr_with_success | command | Local binding for command in test_windows_process_adapter_accepts_stderr_with_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 371 |
| test_windows_process_adapter_accepts_stderr_with_success | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run; see its callable contract | Enclosing invocation or class/instance lifetime | 378 |
| test_iac_process_forwards_stdout_and_stderr_before_exit | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 390 |
| test_iac_process_forwards_stdout_and_stderr_before_exit | payload | Local binding for payload in test_iac_process_forwards_stdout_and_stderr_before_exit; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 394 |
| test_iac_process_forwards_stdout_and_stderr_before_exit | executable | Local binding for executable in test_iac_process_forwards_stdout_and_stderr_before_exit; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 395 |
| test_iac_process_forwards_stdout_and_stderr_before_exit | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 396 |
| test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_407 | event | Comprehension item for event in test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_407; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 407 |
| test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_408 | event | Comprehension item for event in test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_408; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 408 |
| test_iac_process_forwards_stdout_and_stderr_before_exit | timings | Local binding for timings in test_iac_process_forwards_stdout_and_stderr_before_exit; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 409 |
| test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_409 | event | Comprehension item for event in test_iac_process_forwards_stdout_and_stderr_before_exit.comprehension_409; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 409 |
| test_iac_process_forward_output_preserves_stream_labels | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 416 |
| test_iac_process_forward_output_preserves_stream_labels | payload | Local binding for payload in test_iac_process_forward_output_preserves_stream_labels; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 417 |
| test_iac_process_forward_output_preserves_stream_labels | executable | Local binding for executable in test_iac_process_forward_output_preserves_stream_labels; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 418 |
| test_iac_process_forward_output_preserves_stream_labels | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 419 |
| test_iac_process_drains_concurrent_streams_without_failure | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 432 |
| test_iac_process_drains_concurrent_streams_without_failure | payload | Local binding for payload in test_iac_process_drains_concurrent_streams_without_failure; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 438 |
| test_iac_process_drains_concurrent_streams_without_failure | executable | Local binding for executable in test_iac_process_drains_concurrent_streams_without_failure; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 439 |
| test_iac_process_drains_concurrent_streams_without_failure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 440 |
| test_iac_process_preserves_failure_timeout_and_bounded_diagnostics | executable | Local binding for executable in test_iac_process_preserves_failure_timeout_and_bounded_diagnostics; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 453 |
| test_iac_process_preserves_failure_timeout_and_bounded_diagnostics | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 454 |
| test_apply_summarizes_dsc_result_without_emitting_its_raw_json | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 474 |
| test_zero_exit_without_convergence_stops_dependents | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 492 |
| test_managed_root_resolves_windows_host_redirection | tmp_path | Parameter for tmp path in test_managed_root_resolves_windows_host_redirection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 499 |
| test_managed_root_resolves_windows_host_redirection | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 501 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | status | Parameter for status in test_prerequisite_signatures_reject_invalid_or_foreign_publishers; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 520 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | publisher | Parameter for publisher in test_prerequisite_signatures_reject_invalid_or_foreign_publishers; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 520 |
| test_prerequisite_signatures_reject_invalid_or_foreign_publishers | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 522 |
| test_prerequisite_signature_accepts_reviewed_publisher | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 534 |
| test_missing_package_manager_blocks_missing_python | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 542 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | tmp_path | Parameter for tmp path in test_dependency_install_cannot_inherit_pip_target_or_extra_sources; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 548 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | body | Local binding for body in test_dependency_install_cannot_inherit_pip_target_or_extra_sources; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 550 |
| test_dependency_install_cannot_inherit_pip_target_or_extra_sources | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 555 |
| test_environment_install_downloads_only_missing_playwright_chromium | tmp_path | Parameter for tmp path in test_environment_install_downloads_only_missing_playwright_chromium; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 564 |
| test_environment_install_downloads_only_missing_playwright_chromium | browser | Local binding for browser in test_environment_install_downloads_only_missing_playwright_chromium; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 566 |
| test_environment_install_downloads_only_missing_playwright_chromium | body | Local binding for body in test_environment_install_downloads_only_missing_playwright_chromium; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 567 |
| test_environment_install_downloads_only_missing_playwright_chromium | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 577 |
| test_environment_install_downloads_only_missing_playwright_chromium.comprehension_578 | call | Comprehension item for call in test_environment_install_downloads_only_missing_playwright_chromium.comprehension_578; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 578 |
| test_environment_install_skips_existing_compatible_playwright_chromium | tmp_path | Parameter for tmp path in test_environment_install_skips_existing_compatible_playwright_chromium; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 582 |
| test_environment_install_skips_existing_compatible_playwright_chromium | browser | Local binding for browser in test_environment_install_skips_existing_compatible_playwright_chromium; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 584 |
| test_environment_install_skips_existing_compatible_playwright_chromium | body | Local binding for body in test_environment_install_skips_existing_compatible_playwright_chromium; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 587 |
| test_environment_install_skips_existing_compatible_playwright_chromium | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 597 |
| test_environment_install_reports_playwright_chromium_failure | tmp_path | Parameter for tmp path in test_environment_install_reports_playwright_chromium_failure; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 601 |
| test_environment_install_reports_playwright_chromium_failure | browser | Local binding for browser in test_environment_install_reports_playwright_chromium_failure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 603 |
| test_environment_install_reports_playwright_chromium_failure | body | Local binding for body in test_environment_install_reports_playwright_chromium_failure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 604 |
| test_environment_install_reports_playwright_chromium_failure | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 613 |
| test_launcher_uses_venv_playwright_chromium_path | tmp_path | Parameter for tmp path in test_launcher_uses_venv_playwright_chromium_path; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 618 |
| test_launcher_uses_venv_playwright_chromium_path | browser | Local binding for browser in test_launcher_uses_venv_playwright_chromium_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 620 |
| test_launcher_uses_venv_playwright_chromium_path | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 623 |
| test_native_argument_quoting_preserves_data | values | Local binding for values in test_native_argument_quoting_preserves_data; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 636 |
| test_native_argument_quoting_preserves_data | payload | Local binding for payload in test_native_argument_quoting_preserves_data; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 642 |
| test_native_argument_quoting_preserves_data | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 643 |
| test_launcher_preserves_absent_environment_variables | tmp_path | Parameter for tmp path in test_launcher_preserves_absent_environment_variables; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 653 |
| test_launcher_preserves_absent_environment_variables | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 655 |
| test_location_receipt_binds_the_configured_deployment_root | tmp_path | Parameter for tmp path in test_location_receipt_binds_the_configured_deployment_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 663 |
| test_location_receipt_binds_the_configured_deployment_root | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 665 |
| test_iac_launch_ignores_external_ollama_state | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 675 |
| test_iac_configuration_rejects_removed_ollama_fields | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of powershell; see its callable contract | Enclosing invocation or class/instance lifetime | 686 |
