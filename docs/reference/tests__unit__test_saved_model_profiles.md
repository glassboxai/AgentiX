# Reference for tests/unit/test_saved_model_profiles.py

Persistent profile and local model discovery contracts, with fake external IO.

Source fingerprint: e9922de83ec3dd330f5639207fc54cbc1b79eaad79026c8823b59e3fc6fdf108

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### feature

Produce an explicit missing-feature assertion before implementation.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### vault

Model credential operations without touching Windows or real keys.

Kind: callable. Declared return: Not declared / class. Source line: 19.

### test_profiles_survive_repository_restart_without_plaintext_keys

Persist metadata and reload it without exposing API key bytes.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_key_update_failure_retains_original_profile_and_key

A rejected vault update cannot invalidate a working saved credential.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_stale_profile_edit_does_not_overwrite_newer_key

Reject a stale browser edit before changing any credential.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### test_delete_removes_only_selected_owned_profile

Never enumerate or remove unrelated Windows credentials.

Kind: callable. Declared return: Not declared / class. Source line: 95.

### test_profile_identifier_cannot_escape_store

Use only closed UUID filenames, never browser-provided paths.

Kind: callable. Declared return: Not declared / class. Source line: 108.

### test_corrupt_metadata_is_denied_not_silently_replaced

A mismatched credential namespace cannot authorize a key lookup.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_ollama_discovery_reads_tags_only_and_filters_invalid_names

Discover installed models without model downloads or inference.

Kind: callable. Declared return: Not declared / class. Source line: 127.

### test_ollama_discovery_reads_tags_only_and_filters_invalid_names.read

Return a bounded deterministic Ollama response fixture.

Kind: callable. Declared return: Not declared / class. Source line: 133.

### test_ollama_unavailable_is_payload_free

Network exceptions cannot leak configuration or response bodies.

Kind: callable. Declared return: Not declared / class. Source line: 147.

### test_saved_activation_requires_fresh_consent_and_survives_session_close

Persistence never implies remote startup or remembered task-transfer consent.

Kind: callable. Declared return: Not declared / class. Source line: 159.

### test_saved_activation_requires_fresh_consent_and_survives_session_close.service

Create another independent browser configuration over shared saved profiles.

Kind: callable. Declared return: Not declared / class. Source line: 168.

### test_saved_key_cannot_be_sent_to_edited_endpoint

A changed destination requires saving a reviewed profile rather than reusing its key.

Kind: callable. Declared return: Not declared / class. Source line: 199.

### test_failed_metadata_commit_preserves_original_credential

A disk failure after candidate credential creation must not replace old state.

Kind: callable. Declared return: Not declared / class. Source line: 223.

### test_failed_metadata_commit_preserves_original_credential.fail

Simulate disk-full while keeping the existing metadata intact.

Kind: callable. Declared return: Not declared / class. Source line: 230.

### test_stale_displayed_profile_id_cannot_save_another_selection

A queued browser action must match the session's selected profile identity.

Kind: callable. Declared return: Not declared / class. Source line: 249.

### test_local_profiles_persist_without_any_credential_operations

Local metadata supports full lifecycle even when Windows credentials are blocked.

Kind: callable. Declared return: Not declared / class. Source line: 267.

### test_local_profiles_persist_without_any_credential_operations.deny

Fail if local operations touch a credential boundary.

Kind: callable. Declared return: Not declared / class. Source line: 270.

### test_local_session_profile_does_not_construct_vault

Opening and saving local profiles does not require native credential availability.

Kind: callable. Declared return: Not declared / class. Source line: 292.

### test_local_session_profile_does_not_construct_vault.deny

Represent blocked Windows Credential Manager initialization.

Kind: callable. Declared return: Not declared / class. Source line: 296.

### test_remote_to_local_conversion_retires_credentials

Provider changes cannot leave an active local credential or lose the old record on failure.

Kind: callable. Declared return: Not declared / class. Source line: 315.

### test_credential_failure_has_safe_phase_code

Distinguish a native-vault write failure without publishing its exception body.

Kind: callable. Declared return: Not declared / class. Source line: 341.

### test_metadata_failure_has_distinct_safe_phase_code

A file-write failure is distinguishable from the credential boundary.

Kind: callable. Declared return: Not declared / class. Source line: 351.

### test_invalid_key_error_is_classified_without_key_echo

Key validation has a fixed code rather than an unstructured native error.

Kind: callable. Declared return: Not declared / class. Source line: 364.

### test_ui_retains_safe_failed_save_reason_after_refresh

The reported Save-then-Refresh path must not erase the useful failure reason.

Kind: callable. Declared return: Not declared / class. Source line: 374.

### test_oversized_native_blob_is_rejected_before_windows_call

Preserve legacy encoding while reporting its native byte limit explicitly.

Kind: callable. Declared return: Not declared / class. Source line: 400.

### test_candidate_cleanup_failure_preserves_original_safe_reason

A second failure during cleanup must not hide the primary credential failure.

Kind: callable. Declared return: Not declared / class. Source line: 413.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| vault | data | Local binding for data in vault; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 21 |
| vault.lambda_24 | ref | Callback parameter for ref in vault.lambda_24; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 24 |
| vault.lambda_24 | key | Callback parameter for key in vault.lambda_24; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 24 |
| vault.lambda_25 | ref | Callback parameter for ref in vault.lambda_25; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 25 |
| vault.lambda_26 | ref | Callback parameter for ref in vault.lambda_26; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 26 |
| test_profiles_survive_repository_restart_without_plaintext_keys | tmp_path | Parameter for tmp path in test_profiles_survive_repository_restart_without_plaintext_keys; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_profiles_survive_repository_restart_without_plaintext_keys | vault | Parameter for vault in test_profiles_survive_repository_restart_without_plaintext_keys; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_profiles_survive_repository_restart_without_plaintext_keys | store | Local binding for store in test_profiles_survive_repository_restart_without_plaintext_keys; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_profiles_survive_repository_restart_without_plaintext_keys.lambda_32 | host | Callback parameter for host in test_profiles_survive_repository_restart_without_plaintext_keys.lambda_32; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 32 |
| test_profiles_survive_repository_restart_without_plaintext_keys | saved | Local binding for saved in test_profiles_survive_repository_restart_without_plaintext_keys; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_profiles_survive_repository_restart_without_plaintext_keys | again | Local binding for again in test_profiles_survive_repository_restart_without_plaintext_keys; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_profiles_survive_repository_restart_without_plaintext_keys.lambda_36 | host | Callback parameter for host in test_profiles_survive_repository_restart_without_plaintext_keys.lambda_36; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 36 |
| test_profiles_survive_repository_restart_without_plaintext_keys.comprehension_40 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 40 |
| test_key_update_failure_retains_original_profile_and_key | tmp_path | Parameter for tmp path in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_key_update_failure_retains_original_profile_and_key | vault | Parameter for vault in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_key_update_failure_retains_original_profile_and_key | store | Local binding for store in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_key_update_failure_retains_original_profile_and_key.lambda_46 | host | Callback parameter for host in test_key_update_failure_retains_original_profile_and_key.lambda_46; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 46 |
| test_key_update_failure_retains_original_profile_and_key | saved | Local binding for saved in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_key_update_failure_retains_original_profile_and_key | vault.write | Attribute for vault.write in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_key_update_failure_retains_original_profile_and_key.lambda_50 | ref | Callback parameter for ref in test_key_update_failure_retains_original_profile_and_key.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_key_update_failure_retains_original_profile_and_key.lambda_50 | key | Callback parameter for key in test_key_update_failure_retains_original_profile_and_key.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| test_key_update_failure_retains_original_profile_and_key.lambda_50.comprehension_50 | _ | Comprehension item for  in test_key_update_failure_retains_original_profile_and_key.lambda_50.comprehension_50; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 50 |
| test_key_update_failure_retains_original_profile_and_key | failure | Managed resource for failure in test_key_update_failure_retains_original_profile_and_key; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 51 |
| test_stale_profile_edit_does_not_overwrite_newer_key | tmp_path | Parameter for tmp path in test_stale_profile_edit_does_not_overwrite_newer_key; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| test_stale_profile_edit_does_not_overwrite_newer_key | vault | Parameter for vault in test_stale_profile_edit_does_not_overwrite_newer_key; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| test_stale_profile_edit_does_not_overwrite_newer_key | store | Local binding for store in test_stale_profile_edit_does_not_overwrite_newer_key; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_stale_profile_edit_does_not_overwrite_newer_key.lambda_68 | host | Callback parameter for host in test_stale_profile_edit_does_not_overwrite_newer_key.lambda_68; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 68 |
| test_stale_profile_edit_does_not_overwrite_newer_key | saved | Local binding for saved in test_stale_profile_edit_does_not_overwrite_newer_key; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_stale_profile_edit_does_not_overwrite_newer_key | updated | Local binding for updated in test_stale_profile_edit_does_not_overwrite_newer_key; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_delete_removes_only_selected_owned_profile | tmp_path | Parameter for tmp path in test_delete_removes_only_selected_owned_profile; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| test_delete_removes_only_selected_owned_profile | vault | Parameter for vault in test_delete_removes_only_selected_owned_profile; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| test_delete_removes_only_selected_owned_profile | store | Local binding for store in test_delete_removes_only_selected_owned_profile; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_delete_removes_only_selected_owned_profile.lambda_97 | host | Callback parameter for host in test_delete_removes_only_selected_owned_profile.lambda_97; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 97 |
| test_delete_removes_only_selected_owned_profile | saved | Local binding for saved in test_delete_removes_only_selected_owned_profile; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_profile_identifier_cannot_escape_store | tmp_path | Parameter for tmp path in test_profile_identifier_cannot_escape_store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_profile_identifier_cannot_escape_store | vault | Parameter for vault in test_profile_identifier_cannot_escape_store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_profile_identifier_cannot_escape_store | profile_id | Parameter for profile id in test_profile_identifier_cannot_escape_store; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| test_profile_identifier_cannot_escape_store | store | Local binding for store in test_profile_identifier_cannot_escape_store; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| test_corrupt_metadata_is_denied_not_silently_replaced | tmp_path | Parameter for tmp path in test_corrupt_metadata_is_denied_not_silently_replaced; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_corrupt_metadata_is_denied_not_silently_replaced | vault | Parameter for vault in test_corrupt_metadata_is_denied_not_silently_replaced; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| test_corrupt_metadata_is_denied_not_silently_replaced | store | Local binding for store in test_corrupt_metadata_is_denied_not_silently_replaced; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_corrupt_metadata_is_denied_not_silently_replaced.lambda_117 | host | Callback parameter for host in test_corrupt_metadata_is_denied_not_silently_replaced.lambda_117; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 117 |
| test_corrupt_metadata_is_denied_not_silently_replaced | saved | Local binding for saved in test_corrupt_metadata_is_denied_not_silently_replaced; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| test_ollama_discovery_reads_tags_only_and_filters_invalid_names | model_profiles | Imported dependency for model profiles in test_ollama_discovery_reads_tags_only_and_filters_invalid_names; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 129 |
| test_ollama_discovery_reads_tags_only_and_filters_invalid_names | calls | Local binding for calls in test_ollama_discovery_reads_tags_only_and_filters_invalid_names; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 131 |
| test_ollama_discovery_reads_tags_only_and_filters_invalid_names.read | url | Parameter for url in test_ollama_discovery_reads_tags_only_and_filters_invalid_names.read; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 133 |
| test_ollama_unavailable_is_payload_free | model_profiles | Imported dependency for model profiles in test_ollama_unavailable_is_payload_free; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 149 |
| test_ollama_unavailable_is_payload_free | failure | Managed resource for failure in test_ollama_unavailable_is_payload_free; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 151 |
| test_ollama_unavailable_is_payload_free.lambda_154 | url | Callback parameter for url in test_ollama_unavailable_is_payload_free.lambda_154; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 154 |
| test_ollama_unavailable_is_payload_free.lambda_154.comprehension_154 | _ | Comprehension item for  in test_ollama_unavailable_is_payload_free.lambda_154.comprehension_154; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 154 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | tmp_path | Parameter for tmp path in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 159 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | vault | Parameter for vault in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 159 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 161 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | store | Local binding for store in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.lambda_163 | host | Callback parameter for host in test_saved_activation_requires_fresh_consent_and_survives_session_close.lambda_163; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 163 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | saved | Local binding for saved in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.service | controller | Local binding for controller in test_saved_activation_requires_fresh_consent_and_survives_session_close.service; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.service | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_181 | llm | Callback parameter for llm in test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_181; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 181 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_184 | host | Callback parameter for host in test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_184; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 184 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_185 | vault | Callback parameter for vault in test_saved_activation_requires_fresh_consent_and_survives_session_close.service.lambda_185; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 185 |
| test_saved_activation_requires_fresh_consent_and_survives_session_close | first | Local binding for first in test_saved_activation_requires_fresh_consent_and_survives_session_close; use the enclosing contract and type below. | Return type of service; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | tmp_path | Parameter for tmp path in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 199 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | vault | Parameter for vault in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 199 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 201 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | store | Local binding for store in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_203 | host | Callback parameter for host in test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_203; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 203 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | saved | Local binding for saved in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | controller | Local binding for controller in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| test_saved_key_cannot_be_sent_to_edited_endpoint | service | Local binding for service in test_saved_key_cannot_be_sent_to_edited_endpoint; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 211 |
| test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_213 | llm | Callback parameter for llm in test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_213; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 213 |
| test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_215 | vault | Callback parameter for vault in test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_215; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 215 |
| test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_216 | host | Callback parameter for host in test_saved_key_cannot_be_sent_to_edited_endpoint.lambda_216; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 216 |
| test_failed_metadata_commit_preserves_original_credential | tmp_path | Parameter for tmp path in test_failed_metadata_commit_preserves_original_credential; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_failed_metadata_commit_preserves_original_credential | vault | Parameter for vault in test_failed_metadata_commit_preserves_original_credential; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_failed_metadata_commit_preserves_original_credential | monkeypatch | Parameter for monkeypatch in test_failed_metadata_commit_preserves_original_credential; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| test_failed_metadata_commit_preserves_original_credential | store | Local binding for store in test_failed_metadata_commit_preserves_original_credential; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 225 |
| test_failed_metadata_commit_preserves_original_credential.lambda_225 | host | Callback parameter for host in test_failed_metadata_commit_preserves_original_credential.lambda_225; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 225 |
| test_failed_metadata_commit_preserves_original_credential | saved | Local binding for saved in test_failed_metadata_commit_preserves_original_credential; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 226 |
| test_failed_metadata_commit_preserves_original_credential.fail | record | Parameter for record in test_failed_metadata_commit_preserves_original_credential.fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 230 |
| test_stale_displayed_profile_id_cannot_save_another_selection | Mock | Imported dependency for Mock in test_stale_displayed_profile_id_cannot_save_another_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 251 |
| test_stale_displayed_profile_id_cannot_save_another_selection | UiController | Imported dependency for UiController in test_stale_displayed_profile_id_cannot_save_another_selection; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 253 |
| test_stale_displayed_profile_id_cannot_save_another_selection | controller | Local binding for controller in test_stale_displayed_profile_id_cannot_save_another_selection; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 255 |
| test_stale_displayed_profile_id_cannot_save_another_selection.lambda_255 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 255 |
| test_stale_displayed_profile_id_cannot_save_another_selection | save | Local binding for save in test_stale_displayed_profile_id_cannot_save_another_selection; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 256 |
| test_stale_displayed_profile_id_cannot_save_another_selection | controller.model_configuration | Attribute for controller.model configuration in test_stale_displayed_profile_id_cannot_save_another_selection; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
| test_stale_displayed_profile_id_cannot_save_another_selection | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of profile_action; see its callable contract | Enclosing invocation or class/instance lifetime | 260 |
| test_local_profiles_persist_without_any_credential_operations | tmp_path | Parameter for tmp path in test_local_profiles_persist_without_any_credential_operations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| test_local_profiles_persist_without_any_credential_operations.deny | args | Parameter for args in test_local_profiles_persist_without_any_credential_operations.deny; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 270 |
| test_local_profiles_persist_without_any_credential_operations | store | Local binding for store in test_local_profiles_persist_without_any_credential_operations; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 274 |
| test_local_profiles_persist_without_any_credential_operations | saved | Local binding for saved in test_local_profiles_persist_without_any_credential_operations; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 275 |
| test_local_profiles_persist_without_any_credential_operations | updated | Local binding for updated in test_local_profiles_persist_without_any_credential_operations; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 278 |
| test_local_session_profile_does_not_construct_vault | tmp_path | Parameter for tmp path in test_local_session_profile_does_not_construct_vault; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 292 |
| test_local_session_profile_does_not_construct_vault | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in test_local_session_profile_does_not_construct_vault; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 294 |
| test_local_session_profile_does_not_construct_vault | controller | Local binding for controller in test_local_session_profile_does_not_construct_vault; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 300 |
| test_local_session_profile_does_not_construct_vault | config | Local binding for config in test_local_session_profile_does_not_construct_vault; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 304 |
| test_local_session_profile_does_not_construct_vault.lambda_306 | llm | Callback parameter for llm in test_local_session_profile_does_not_construct_vault.lambda_306; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 306 |
| test_local_session_profile_does_not_construct_vault.lambda_308 | vault | Callback parameter for vault in test_local_session_profile_does_not_construct_vault.lambda_308; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 308 |
| test_remote_to_local_conversion_retires_credentials | tmp_path | Parameter for tmp path in test_remote_to_local_conversion_retires_credentials; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 315 |
| test_remote_to_local_conversion_retires_credentials | vault | Parameter for vault in test_remote_to_local_conversion_retires_credentials; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 315 |
| test_remote_to_local_conversion_retires_credentials | store | Local binding for store in test_remote_to_local_conversion_retires_credentials; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 317 |
| test_remote_to_local_conversion_retires_credentials.lambda_317 | host | Callback parameter for host in test_remote_to_local_conversion_retires_credentials.lambda_317; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 317 |
| test_remote_to_local_conversion_retires_credentials | saved | Local binding for saved in test_remote_to_local_conversion_retires_credentials; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 318 |
| test_remote_to_local_conversion_retires_credentials | local | Local binding for local in test_remote_to_local_conversion_retires_credentials; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 319 |
| test_credential_failure_has_safe_phase_code | tmp_path | Parameter for tmp path in test_credential_failure_has_safe_phase_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 341 |
| test_credential_failure_has_safe_phase_code | vault | Parameter for vault in test_credential_failure_has_safe_phase_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 341 |
| test_credential_failure_has_safe_phase_code | store | Local binding for store in test_credential_failure_has_safe_phase_code; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 343 |
| test_credential_failure_has_safe_phase_code.lambda_343 | host | Callback parameter for host in test_credential_failure_has_safe_phase_code.lambda_343; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 343 |
| test_credential_failure_has_safe_phase_code | vault.write | Attribute for vault.write in test_credential_failure_has_safe_phase_code; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 344 |
| test_credential_failure_has_safe_phase_code.lambda_344.comprehension_344 | _ | Comprehension item for  in test_credential_failure_has_safe_phase_code.lambda_344.comprehension_344; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 344 |
| test_credential_failure_has_safe_phase_code | caught | Managed resource for caught in test_credential_failure_has_safe_phase_code; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 345 |
| test_metadata_failure_has_distinct_safe_phase_code | tmp_path | Parameter for tmp path in test_metadata_failure_has_distinct_safe_phase_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| test_metadata_failure_has_distinct_safe_phase_code | vault | Parameter for vault in test_metadata_failure_has_distinct_safe_phase_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| test_metadata_failure_has_distinct_safe_phase_code | monkeypatch | Parameter for monkeypatch in test_metadata_failure_has_distinct_safe_phase_code; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| test_metadata_failure_has_distinct_safe_phase_code | store | Local binding for store in test_metadata_failure_has_distinct_safe_phase_code; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 353 |
| test_metadata_failure_has_distinct_safe_phase_code.lambda_353 | host | Callback parameter for host in test_metadata_failure_has_distinct_safe_phase_code.lambda_353; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 353 |
| test_metadata_failure_has_distinct_safe_phase_code.lambda_355 | record | Callback parameter for record in test_metadata_failure_has_distinct_safe_phase_code.lambda_355; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 355 |
| test_metadata_failure_has_distinct_safe_phase_code.lambda_355.comprehension_355 | _ | Comprehension item for  in test_metadata_failure_has_distinct_safe_phase_code.lambda_355.comprehension_355; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 355 |
| test_metadata_failure_has_distinct_safe_phase_code | caught | Managed resource for caught in test_metadata_failure_has_distinct_safe_phase_code; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 357 |
| test_invalid_key_error_is_classified_without_key_echo | register_secret | Imported dependency for register secret in test_invalid_key_error_is_classified_without_key_echo; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 366 |
| test_invalid_key_error_is_classified_without_key_echo | caught | Managed resource for caught in test_invalid_key_error_is_classified_without_key_echo; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 368 |
| test_ui_retains_safe_failed_save_reason_after_refresh | tmp_path | Parameter for tmp path in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 374 |
| test_ui_retains_safe_failed_save_reason_after_refresh | vault | Parameter for vault in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 374 |
| test_ui_retains_safe_failed_save_reason_after_refresh | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 376 |
| test_ui_retains_safe_failed_save_reason_after_refresh | UiController | Imported dependency for UiController in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 377 |
| test_ui_retains_safe_failed_save_reason_after_refresh | security | Owner-scoped approval and path boundary injected into this service. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 379 |
| test_ui_retains_safe_failed_save_reason_after_refresh | controller | Local binding for controller in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 380 |
| test_ui_retains_safe_failed_save_reason_after_refresh.lambda_380 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 380 |
| test_ui_retains_safe_failed_save_reason_after_refresh | store | Local binding for store in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 381 |
| test_ui_retains_safe_failed_save_reason_after_refresh.lambda_381 | host | Callback parameter for host in test_ui_retains_safe_failed_save_reason_after_refresh.lambda_381; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 381 |
| test_ui_retains_safe_failed_save_reason_after_refresh | controller.model_configuration | Attribute for controller.model configuration in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 382 |
| test_ui_retains_safe_failed_save_reason_after_refresh.lambda_384 | llm | Callback parameter for llm in test_ui_retains_safe_failed_save_reason_after_refresh.lambda_384; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 384 |
| test_ui_retains_safe_failed_save_reason_after_refresh.lambda_386 | boundary | Callback parameter for boundary in test_ui_retains_safe_failed_save_reason_after_refresh.lambda_386; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 386 |
| test_ui_retains_safe_failed_save_reason_after_refresh | vault.write | Attribute for vault.write in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 388 |
| test_ui_retains_safe_failed_save_reason_after_refresh.lambda_388.comprehension_388 | _ | Comprehension item for  in test_ui_retains_safe_failed_save_reason_after_refresh.lambda_388.comprehension_388; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 388 |
| test_ui_retains_safe_failed_save_reason_after_refresh | first | Local binding for first in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Return type of profile_action; see its callable contract | Enclosing invocation or class/instance lifetime | 389 |
| test_ui_retains_safe_failed_save_reason_after_refresh | again | Local binding for again in test_ui_retains_safe_failed_save_reason_after_refresh; use the enclosing contract and type below. | Return type of profile_action; see its callable contract | Enclosing invocation or class/instance lifetime | 393 |
| test_oversized_native_blob_is_rejected_before_windows_call | WindowsCredentialVault | Imported dependency for WindowsCredentialVault in test_oversized_native_blob_is_rejected_before_windows_call; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 402 |
| test_oversized_native_blob_is_rejected_before_windows_call | vault | Local binding for vault in test_oversized_native_blob_is_rejected_before_windows_call; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 404 |
| test_oversized_native_blob_is_rejected_before_windows_call | vault.api | Attribute for vault.api in test_oversized_native_blob_is_rejected_before_windows_call; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 405 |
| test_oversized_native_blob_is_rejected_before_windows_call | caught | Managed resource for caught in test_oversized_native_blob_is_rejected_before_windows_call; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 408 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | tmp_path | Parameter for tmp path in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 413 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | vault | Parameter for vault in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 413 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | ProfileError | Imported dependency for ProfileError in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 415 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | store | Local binding for store in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 417 |
| test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_417 | host | Callback parameter for host in test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_417; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 417 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | vault.write | Attribute for vault.write in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 418 |
| test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_418.comprehension_418 | _ | Comprehension item for  in test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_418.comprehension_418; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 418 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | vault.delete | Attribute for vault.delete in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 419 |
| test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_419.comprehension_419 | _ | Comprehension item for  in test_candidate_cleanup_failure_preserves_original_safe_reason.lambda_419.comprehension_419; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 419 |
| test_candidate_cleanup_failure_preserves_original_safe_reason | caught | Managed resource for caught in test_candidate_cleanup_failure_preserves_original_safe_reason; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 420 |
