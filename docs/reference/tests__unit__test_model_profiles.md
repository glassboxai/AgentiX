# Reference for tests/unit/test_model_profiles.py

Regression contracts for session model configuration and secret boundaries.

Source fingerprint: 5a4525e3b7fb0c2b957fcee5c840c6bcfb756cbc4e7d8bcc7c0780d5c6bb1897

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### profiles

Load the feature with an actionable failure before implementation.

Kind: callable. Declared return: Not declared / class. Source line: 9.

### test_default_local_profile_preserves_required_model

Keep the validated local model as the default.

Kind: callable. Declared return: Not declared / class. Source line: 17.

### test_remote_endpoint_rejects_unsafe_destinations

Reject plaintext, private targets, embedded credentials and URL payloads.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_remote_requires_explicit_consent

Never enable remote data transfer implicitly.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_dns_private_resolution_rejected

Reject a public-looking name that resolves to a private address.

Kind: callable. Declared return: Not declared / class. Source line: 48.

### test_secret_not_in_profile_repr

Profile data contains a credential reference rather than the API key.

Kind: callable. Declared return: Not declared / class. Source line: 56.

### test_local_endpoint_must_be_loopback

Ollama configuration cannot become an arbitrary HTTP request destination.

Kind: callable. Declared return: Not declared / class. Source line: 62.

### test_session_configuration_denies_running_and_pending

A model change cannot replace an active or awaiting-review workflow.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_remote_client_uses_explicit_key_and_limits

Inject the key without process environment mutation or unbounded retries.

Kind: callable. Declared return: Not declared / class. Source line: 83.

### test_client_failure_is_secret_free

Do not expose provider exceptions that may contain Authorization headers.

Kind: callable. Declared return: Not declared / class. Source line: 102.

### test_client_failure_is_secret_free.fail

Simulate a provider leaking credentials into its exception.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### test_model_identifiers_are_bounded

Reject control characters, path traversal and oversized names.

Kind: callable. Declared return: Not declared / class. Source line: 116.

### test_model_switch_is_transactional_and_invalidates_old_services

Commit fresh services only after successful provider initialization.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_failed_model_switch_removes_new_credential_and_retains_old_runtime

A provider failure cannot leave a stored key or partially swap services.

Kind: callable. Declared return: Not declared / class. Source line: 161.

### test_failed_model_switch_removes_new_credential_and_retains_old_runtime.fail

Deny runtime composition after client creation.

Kind: callable. Declared return: Not declared / class. Source line: 176.

### test_host_redacts_vendor_exception_and_activity

Keys cannot appear in formatted application/vendor logs or activity.

Kind: callable. Declared return: Not declared / class. Source line: 193.

### test_review_container_is_single_below_validation_and_outside_sidebar

Inspect actual Gradio component ancestry, rather than matching source text.

Kind: callable. Declared return: Not declared / class. Source line: 209.

### test_review_container_is_single_below_validation_and_outside_sidebar.visit

Record real layout ancestry for each rendered native component.

Kind: callable. Declared return: Not declared / class. Source line: 235.

### test_oversized_query_cannot_start_worker

Deny oversized task data before logging, history retention or model work.

Kind: callable. Declared return: Not declared / class. Source line: 256.

### test_remote_request_policy_denies_destination_changes

No credential-bearing request can change its approved origin or base path.

Kind: callable. Declared return: Not declared / class. Source line: 279.

### test_remote_policy_rejects_redirect_and_rechecks_dns

Prevent redirect following and detect private resolution on later calls.

Kind: callable. Declared return: Not declared / class. Source line: 290.

### test_agents_have_finite_work_limits

All roles retain verbose output but have bounded iteration/time/retry policy.

Kind: callable. Declared return: Not declared / class. Source line: 306.

### test_foreign_session_cannot_configure_model

Reject a stolen token before touching model or credential services.

Kind: callable. Declared return: Not declared / class. Source line: 314.

### test_global_work_capacity_rejects_without_contacting_model

Overload is denied immediately instead of queueing unlimited model work.

Kind: callable. Declared return: Not declared / class. Source line: 339.

### test_cli_query_limit_precedes_model_work

The shared orchestration service also bounds terminal requests.

Kind: callable. Declared return: Not declared / class. Source line: 350.

### test_namespaced_installed_model_identifiers_are_supported

Accept ordinary Ollama/provider namespaces without permitting traversal.

Kind: callable. Declared return: Not declared / class. Source line: 357.

### test_remote_resolution_rejects_multicast_addresses

Python is_global alone includes multicast, which is not a public API host.

Kind: callable. Declared return: Not declared / class. Source line: 363.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_default_local_profile_preserves_required_model | profile | Local binding for profile in test_default_local_profile_preserves_required_model; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| test_remote_endpoint_rejects_unsafe_destinations | url | Parameter for url in test_remote_endpoint_rejects_unsafe_destinations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_remote_endpoint_rejects_unsafe_destinations.lambda_38 | host | Callback parameter for host in test_remote_endpoint_rejects_unsafe_destinations.lambda_38; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 38 |
| test_dns_private_resolution_rejected.lambda_53 | host | Callback parameter for host in test_dns_private_resolution_rejected.lambda_53; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 53 |
| test_secret_not_in_profile_repr | profile | Local binding for profile in test_secret_not_in_profile_repr; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_session_configuration_denies_running_and_pending | module | Local binding for module in test_session_configuration_denies_running_and_pending; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_session_configuration_denies_running_and_pending | controller | Local binding for controller in test_session_configuration_denies_running_and_pending; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_session_configuration_denies_running_and_pending | controller.state.is_running | Attribute for controller.state.is running in test_session_configuration_denies_running_and_pending; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 77 |
| test_session_configuration_denies_running_and_pending | controller.security.get_pending_request | Attribute for controller.security.get pending request in test_session_configuration_denies_running_and_pending; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| test_remote_client_uses_explicit_key_and_limits | module | Local binding for module in test_remote_client_uses_explicit_key_and_limits; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_remote_client_uses_explicit_key_and_limits | calls | Local binding for calls in test_remote_client_uses_explicit_key_and_limits; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 86 |
| test_remote_client_uses_explicit_key_and_limits | vault | Local binding for vault in test_remote_client_uses_explicit_key_and_limits; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_remote_client_uses_explicit_key_and_limits.lambda_87 | reference | Callback parameter for reference in test_remote_client_uses_explicit_key_and_limits.lambda_87; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 87 |
| test_remote_client_uses_explicit_key_and_limits | profile | Local binding for profile in test_remote_client_uses_explicit_key_and_limits; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_remote_client_uses_explicit_key_and_limits.lambda_93 | host | Callback parameter for host in test_remote_client_uses_explicit_key_and_limits.lambda_93; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 93 |
| test_client_failure_is_secret_free | module | Local binding for module in test_client_failure_is_secret_free; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_client_failure_is_secret_free.fail | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_client_failure_is_secret_free | failure | Managed resource for failure in test_client_failure_is_secret_free; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 110 |
| test_model_identifiers_are_bounded | model | Parameter for model in test_model_identifiers_are_bounded; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 116 |
| test_model_switch_is_transactional_and_invalidates_old_services | module | Local binding for module in test_model_switch_is_transactional_and_invalidates_old_services; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| test_model_switch_is_transactional_and_invalidates_old_services | values | Local binding for values in test_model_switch_is_transactional_and_invalidates_old_services; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 125 |
| test_model_switch_is_transactional_and_invalidates_old_services | vault | Local binding for vault in test_model_switch_is_transactional_and_invalidates_old_services; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_127 | ref | Callback parameter for ref in test_model_switch_is_transactional_and_invalidates_old_services.lambda_127; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 127 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_127 | key | Callback parameter for key in test_model_switch_is_transactional_and_invalidates_old_services.lambda_127; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 127 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_128 | ref | Callback parameter for ref in test_model_switch_is_transactional_and_invalidates_old_services.lambda_128; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 128 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_129 | ref | Callback parameter for ref in test_model_switch_is_transactional_and_invalidates_old_services.lambda_129; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 129 |
| test_model_switch_is_transactional_and_invalidates_old_services | security | Owner-scoped approval and path boundary injected into this service. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_model_switch_is_transactional_and_invalidates_old_services | controller | Local binding for controller in test_model_switch_is_transactional_and_invalidates_old_services; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_model_switch_is_transactional_and_invalidates_old_services | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| test_model_switch_is_transactional_and_invalidates_old_services | service | Local binding for service in test_model_switch_is_transactional_and_invalidates_old_services; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_146 | llm | Callback parameter for llm in test_model_switch_is_transactional_and_invalidates_old_services.lambda_146; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 146 |
| test_model_switch_is_transactional_and_invalidates_old_services.lambda_149 | host | Callback parameter for host in test_model_switch_is_transactional_and_invalidates_old_services.lambda_149; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 149 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | module | Local binding for module in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | values | Local binding for values in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 164 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | vault | Local binding for vault in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_166 | ref | Callback parameter for ref in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_166; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 166 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_166 | key | Callback parameter for key in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_166; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 166 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_167 | ref | Callback parameter for ref in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_167; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 167 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_168 | ref | Callback parameter for ref in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_168; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 168 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | controller | Local binding for controller in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.fail | llm | Parameter for llm in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | service | Local binding for service in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_185 | host | Callback parameter for host in test_failed_model_switch_removes_new_credential_and_retains_old_runtime.lambda_185; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 185 |
| test_failed_model_switch_removes_new_credential_and_retains_old_runtime | error | Managed resource for error in test_failed_model_switch_removes_new_credential_and_retains_old_runtime; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 187 |
| test_host_redacts_vendor_exception_and_activity | logging | Imported dependency for logging in test_host_redacts_vendor_exception_and_activity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| test_host_redacts_vendor_exception_and_activity | credentials | Imported dependency for credentials in test_host_redacts_vendor_exception_and_activity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 197 |
| test_host_redacts_vendor_exception_and_activity | record | Local binding for record in test_host_redacts_vendor_exception_and_activity; use the enclosing contract and type below. | Return type of LogRecord; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_review_container_is_single_below_validation_and_outside_sidebar | gr | Imported dependency for gr in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| test_review_container_is_single_below_validation_and_outside_sidebar | SessionRegistry | Imported dependency for SessionRegistry in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 213 |
| test_review_container_is_single_below_validation_and_outside_sidebar | build_view | Imported dependency for build view in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 214 |
| test_review_container_is_single_below_validation_and_outside_sidebar | view | Local binding for view in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| test_review_container_is_single_below_validation_and_outside_sidebar.lambda_216 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 216 |
| test_review_container_is_single_below_validation_and_outside_sidebar | config | Local binding for config in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Return type of get_config_file; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| test_review_container_is_single_below_validation_and_outside_sidebar | components | Local binding for components in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 218 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_218 | item | Comprehension item for item in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_218; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 218 |
| test_review_container_is_single_below_validation_and_outside_sidebar | sidebar_ids | Local binding for sidebar ids in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 219 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_219 | key | Comprehension item for key in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_219; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 219 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_219 | item | Comprehension item for item in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_219; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 219 |
| test_review_container_is_single_below_validation_and_outside_sidebar | editor_ids | Local binding for editor ids in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 221 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_221 | key | Comprehension item for key in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_221; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 223 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_221 | item | Comprehension item for item in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_221; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 223 |
| test_review_container_is_single_below_validation_and_outside_sidebar | validation | Local binding for validation in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_228 | key | Comprehension item for key in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_228; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 230 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_228 | item | Comprehension item for item in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_228; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 230 |
| test_review_container_is_single_below_validation_and_outside_sidebar | chains | Local binding for chains in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 233 |
| test_review_container_is_single_below_validation_and_outside_sidebar.visit | node | Parameter for node in test_review_container_is_single_below_validation_and_outside_sidebar.visit; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 235 |
| test_review_container_is_single_below_validation_and_outside_sidebar.visit | ancestors | Parameter for ancestors in test_review_container_is_single_below_validation_and_outside_sidebar.visit; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 235 |
| test_review_container_is_single_below_validation_and_outside_sidebar.visit | child | Loop item for child in test_review_container_is_single_below_validation_and_outside_sidebar.visit; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 238 |
| test_review_container_is_single_below_validation_and_outside_sidebar | editor | Local binding for editor in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 242 |
| test_review_container_is_single_below_validation_and_outside_sidebar | validation_parent | Local binding for validation parent in test_review_container_is_single_below_validation_and_outside_sidebar; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 244 |
| test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_249 | item | Comprehension item for item in test_review_container_is_single_below_validation_and_outside_sidebar.comprehension_249; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 250 |
| test_oversized_query_cannot_start_worker | UiController | Imported dependency for UiController in test_oversized_query_cannot_start_worker; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 258 |
| test_oversized_query_cannot_start_worker | controller | Local binding for controller in test_oversized_query_cannot_start_worker; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 260 |
| test_oversized_query_cannot_start_worker.lambda_261 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 261 |
| test_remote_request_policy_denies_destination_changes | destination | Parameter for destination in test_remote_request_policy_denies_destination_changes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 279 |
| test_remote_request_policy_denies_destination_changes | module | Local binding for module in test_remote_request_policy_denies_destination_changes; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 281 |
| test_remote_request_policy_denies_destination_changes | policy | Local binding for policy in test_remote_request_policy_denies_destination_changes; use the enclosing contract and type below. | Return type of RemoteRequestPolicy; see its callable contract | Enclosing invocation or class/instance lifetime | 282 |
| test_remote_request_policy_denies_destination_changes.lambda_284 | host | Callback parameter for host in test_remote_request_policy_denies_destination_changes.lambda_284; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 284 |
| test_remote_policy_rejects_redirect_and_rechecks_dns | module | Local binding for module in test_remote_policy_rejects_redirect_and_rechecks_dns; use the enclosing contract and type below. | Return type of profiles; see its callable contract | Enclosing invocation or class/instance lifetime | 292 |
| test_remote_policy_rejects_redirect_and_rechecks_dns | addresses | Local binding for addresses in test_remote_policy_rejects_redirect_and_rechecks_dns; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 293 |
| test_remote_policy_rejects_redirect_and_rechecks_dns | policy | Local binding for policy in test_remote_policy_rejects_redirect_and_rechecks_dns; use the enclosing contract and type below. | Return type of RemoteRequestPolicy; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| test_remote_policy_rejects_redirect_and_rechecks_dns.lambda_296 | host | Callback parameter for host in test_remote_policy_rejects_redirect_and_rechecks_dns.lambda_296; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 296 |
| test_agents_have_finite_work_limits | system | Parameter for system in test_agents_have_finite_work_limits; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 306 |
| test_agents_have_finite_work_limits | call | Loop item for call in test_agents_have_finite_work_limits; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 308 |
| test_foreign_session_cannot_configure_model | SessionAccessError | Imported dependency for SessionAccessError in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 316 |
| test_foreign_session_cannot_configure_model | SessionCallbacks | Imported dependency for SessionCallbacks in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 316 |
| test_foreign_session_cannot_configure_model | SessionRegistry | Imported dependency for SessionRegistry in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 316 |
| test_foreign_session_cannot_configure_model | calls | Local binding for calls in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 318 |
| test_foreign_session_cannot_configure_model | registry | Local binding for registry in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 319 |
| test_foreign_session_cannot_configure_model.lambda_320 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 320 |
| test_foreign_session_cannot_configure_model | alice | Local binding for alice in test_foreign_session_cannot_configure_model; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 325 |
| test_global_work_capacity_rejects_without_contacting_model | system | Parameter for system in test_global_work_capacity_rejects_without_contacting_model; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_global_work_capacity_rejects_without_contacting_model | monkeypatch | Parameter for monkeypatch in test_global_work_capacity_rejects_without_contacting_model; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 339 |
| test_global_work_capacity_rejects_without_contacting_model | module | Imported dependency for module in test_global_work_capacity_rejects_without_contacting_model; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 341 |
| test_global_work_capacity_rejects_without_contacting_model | gate | Local binding for gate in test_global_work_capacity_rejects_without_contacting_model; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 343 |
| test_cli_query_limit_precedes_model_work | system | Parameter for system in test_cli_query_limit_precedes_model_work; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 350 |
| test_remote_resolution_rejects_multicast_addresses | address | Parameter for address in test_remote_resolution_rejects_multicast_addresses; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 363 |
| test_remote_resolution_rejects_multicast_addresses.lambda_368 | host | Callback parameter for host in test_remote_resolution_rejects_multicast_addresses.lambda_368; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 368 |
