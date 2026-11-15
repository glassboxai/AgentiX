# Reference for tests/integration/test_windows_isolation.py

Opt-in native boundary checks using only independently authored fixtures.

Source fingerprint: 0fa964364cf56c26622ea4ed40248faa2a32f1125bb9f36c687043bc3e1d80f0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_python_isolated_execution_and_unittest

Verify native python isolated execution and unittest.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### test_native_denies_host_write_read_and_network

Verify native denies host write read and network.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### test_native_terminates_endless_execution

Verify native terminates endless execution.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_native_bounds_output

Verify native bounds output.

Kind: callable. Declared return: Not declared / class. Source line: 82.

### test_native_staging_is_read_only_and_environment_omits_secrets

Verify native staging is read only and environment omits secrets.

Kind: callable. Declared return: Not declared / class. Source line: 93.

### test_native_limits_memory_without_stalling_host

Verify native limits memory without stalling host.

Kind: callable. Declared return: Not declared / class. Source line: 112.

### test_native_service_lifecycle_uses_verified_current_bytes

Verify native service lifecycle uses verified current bytes.

Kind: callable. Declared return: Not declared / class. Source line: 124.

### test_native_limits_child_count_and_cleans_resources

Verify native limits child count and cleans resources.

Kind: callable. Declared return: Not declared / class. Source line: 163.

### test_native_typed_observations_and_function_exceptions

Verify native typed observations and function exceptions.

Kind: callable. Declared return: Not declared / class. Source line: 193.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | list | Module/process lifetime | 8 |
| test_native_python_isolated_execution_and_unittest | tmp_path | Parameter for tmp path in test_native_python_isolated_execution_and_unittest; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| test_native_python_isolated_execution_and_unittest | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_python_isolated_execution_and_unittest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| test_native_python_isolated_execution_and_unittest | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of WindowsSandbox; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_native_python_isolated_execution_and_unittest | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 19 |
| test_native_python_isolated_execution_and_unittest | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 20, 24 |
| test_native_python_isolated_execution_and_unittest | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 23 |
| test_native_denies_host_write_read_and_network | tmp_path | Parameter for tmp path in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| test_native_denies_host_write_read_and_network | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_native_denies_host_write_read_and_network | secret | Local binding for secret in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_native_denies_host_write_read_and_network | target | Local binding for target in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_native_denies_host_write_read_and_network | listener | Local binding for listener in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Return type of socket; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_native_denies_host_write_read_and_network | port | Local binding for port in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_native_denies_host_write_read_and_network | connection | Local binding for connection in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Return type of accept; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_native_denies_host_write_read_and_network | _ | Local binding for  in test_native_denies_host_write_read_and_network; use the enclosing contract and type below. | Return type of accept; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_native_denies_host_write_read_and_network | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_native_denies_host_write_read_and_network | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_native_terminates_endless_execution | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_terminates_endless_execution; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| test_native_terminates_endless_execution | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_native_bounds_output | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_bounds_output; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| test_native_bounds_output | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_native_staging_is_read_only_and_environment_omits_secrets | monkeypatch | Parameter for monkeypatch in test_native_staging_is_read_only_and_environment_omits_secrets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_native_staging_is_read_only_and_environment_omits_secrets | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_staging_is_read_only_and_environment_omits_secrets; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 95 |
| test_native_staging_is_read_only_and_environment_omits_secrets | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 98 |
| test_native_staging_is_read_only_and_environment_omits_secrets | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_native_limits_memory_without_stalling_host | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_limits_memory_without_stalling_host; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 114 |
| test_native_limits_memory_without_stalling_host | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 116 |
| test_native_limits_memory_without_stalling_host | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_native_service_lifecycle_uses_verified_current_bytes | tmp_path | Parameter for tmp path in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| test_native_service_lifecycle_uses_verified_current_bytes | approve_next_review | Imported dependency for approve next review in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 126 |
| test_native_service_lifecycle_uses_verified_current_bytes | SecurityManager | Imported dependency for SecurityManager in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 128 |
| test_native_service_lifecycle_uses_verified_current_bytes | ArtifactTools | Imported dependency for ArtifactTools in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 129 |
| test_native_service_lifecycle_uses_verified_current_bytes | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_native_service_lifecycle_uses_verified_current_bytes | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_native_service_lifecycle_uses_verified_current_bytes | security.auto_approve | Attribute for security.auto approve in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 133 |
| test_native_service_lifecycle_uses_verified_current_bytes | operations | Local binding for operations in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| test_native_service_lifecycle_uses_verified_current_bytes | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 136 |
| test_native_service_lifecycle_uses_verified_current_bytes | thread | Local binding for thread in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_native_service_lifecycle_uses_verified_current_bytes | errors | Local binding for errors in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_native_service_lifecycle_uses_verified_current_bytes | security.operation_id | Attribute for security.operation id in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 149 |
| test_native_service_lifecycle_uses_verified_current_bytes | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 155 |
| test_native_service_lifecycle_uses_verified_current_bytes | original | Local binding for original in test_native_service_lifecycle_uses_verified_current_bytes; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 156 |
| test_native_limits_child_count_and_cleans_resources | os | Imported dependency for os in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 165 |
| test_native_limits_child_count_and_cleans_resources | tempfile | Imported dependency for tempfile in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 166 |
| test_native_limits_child_count_and_cleans_resources | Path | Imported dependency for Path in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 167 |
| test_native_limits_child_count_and_cleans_resources | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 169 |
| test_native_limits_child_count_and_cleans_resources | packages | Local binding for packages in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_native_limits_child_count_and_cleans_resources | temporary | Local binding for temporary in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 172 |
| test_native_limits_child_count_and_cleans_resources | profiles_before | Local binding for profiles before in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| test_native_limits_child_count_and_cleans_resources | folders_before | Local binding for folders before in test_native_limits_child_count_and_cleans_resources; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_native_limits_child_count_and_cleans_resources | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 175 |
| test_native_limits_child_count_and_cleans_resources | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_native_typed_observations_and_function_exceptions | WindowsSandbox | Imported dependency for WindowsSandbox in test_native_typed_observations_and_function_exceptions; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| test_native_typed_observations_and_function_exceptions | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 197 |
| test_native_typed_observations_and_function_exceptions | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of WindowsSandbox; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| test_native_typed_observations_and_function_exceptions | returned | Local binding for returned in test_native_typed_observations_and_function_exceptions; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_native_typed_observations_and_function_exceptions | raised | Local binding for raised in test_native_typed_observations_and_function_exceptions; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
