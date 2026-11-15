# Reference for tests/unit/test_generation_identity.py

Security contracts for TOFU local generation identities.

Source fingerprint: 1684a9fd465e6caaac9b7aecaece3840df93d1d0b7fd90d860e0145356b8172c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_local_generation_identity_requires_matching_trusted_digest

A local model cannot authorize generation until its current digest matches trust.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_local_generation_identity_rejects_missing_or_invalid_trusted_digests

Malformed or absent profile trust never becomes a generation authorization.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest

A first-use baseline is stable until an explicit reset is requested.

Kind: callable. Declared return: Not declared / class. Source line: 44.

### test_saved_local_profile_preserves_only_an_unchanged_tofu_identity

Profile edits cannot silently retain a baseline for another model identity.

Kind: callable. Declared return: Not declared / class. Source line: 65.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_local_generation_identity_requires_matching_trusted_digest | verify_generation_identity | Imported dependency for verify generation identity in test_local_generation_identity_requires_matching_trusted_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_local_generation_identity_requires_matching_trusted_digest | ModelProfile | Imported dependency for ModelProfile in test_local_generation_identity_requires_matching_trusted_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 11 |
| test_local_generation_identity_requires_matching_trusted_digest | profile | Local binding for profile in test_local_generation_identity_requires_matching_trusted_digest; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_local_generation_identity_requires_matching_trusted_digest.lambda_18 | endpoint | Callback parameter for endpoint in test_local_generation_identity_requires_matching_trusted_digest.lambda_18; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 18 |
| test_local_generation_identity_requires_matching_trusted_digest.lambda_28 | endpoint | Callback parameter for endpoint in test_local_generation_identity_requires_matching_trusted_digest.lambda_28; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 28 |
| test_local_generation_identity_rejects_missing_or_invalid_trusted_digests | digest | Content fingerprint for change detection; not a substitute for human approval. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_local_generation_identity_rejects_missing_or_invalid_trusted_digests | verify_generation_identity | Imported dependency for verify generation identity in test_local_generation_identity_rejects_missing_or_invalid_trusted_digests; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 37 |
| test_local_generation_identity_rejects_missing_or_invalid_trusted_digests | ModelProfile | Imported dependency for ModelProfile in test_local_generation_identity_rejects_missing_or_invalid_trusted_digests; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 38 |
| test_local_generation_identity_rejects_missing_or_invalid_trusted_digests.lambda_41 | endpoint | Callback parameter for endpoint in test_local_generation_identity_rejects_missing_or_invalid_trusted_digests.lambda_41; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 41 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | tmp_path | Parameter for tmp path in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | ProfileError | Imported dependency for ProfileError in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | SavedProfiles | Imported dependency for SavedProfiles in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 47 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | store | Local binding for store in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | saved | Local binding for saved in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | trusted | Local binding for trusted in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Return type of trust_generation_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest | reset | Local binding for reset in test_saved_local_profile_records_tofu_baseline_and_rejects_changed_digest; use the enclosing contract and type below. | Return type of trust_generation_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | tmp_path | Parameter for tmp path in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | SavedProfiles | Imported dependency for SavedProfiles in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 67 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | store | Local binding for store in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Return type of SavedProfiles; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | saved | Local binding for saved in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | trusted | Local binding for trusted in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Return type of trust_generation_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | renamed | Local binding for renamed in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_saved_local_profile_preserves_only_an_unchanged_tofu_identity | changed | Local binding for changed in test_saved_local_profile_preserves_only_an_unchanged_tofu_identity; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
