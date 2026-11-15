# Reference for tests/e2e/server.py

Disposable real UI with trusted fixtures; never load a model or project artifacts.

This executable is test infrastructure only. Its OS boundary double must never
be used for untrusted input. The parent owns process and temporary-directory cleanup.

Source fingerprint: e9c40df95c0c1eef39a743d8cc0b5c9493b9e6de95939eef7d0f87e438210cea

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Serve only loopback on the supplied temporary port and artifact root.

Kind: callable. Declared return: None. Source line: 34.

### main.fixture_write

Model validation and a deterministic denial without exposing the key.

Kind: callable. Declared return: Not declared / class. Source line: 40.

### main.create

Give each browser its own real approvals, ledger and artifact services.

Kind: callable. Declared return: UiController. Source line: 55.

### main.create.workflow

Exercise actual storage, provisional tests, review and host comparison.

Kind: callable. Declared return: str. Source line: 63.

### main.create.local_catalog

Make the manual refresh reveal an additional installed model.

Kind: callable. Declared return: Not declared / class. Source line: 228.

### main.create.configured_runtime

Expose the configured fake client identity through the real query UI.

Kind: callable. Declared return: Not declared / class. Source line: 234.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | gr | Imported dependency for gr in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | TrustedFixtureSandbox | Imported dependency for TrustedFixtureSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 30 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 31 |
| main | folder | Local binding for folder in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| main | port | Local binding for port in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| main | fixture_values | Local binding for fixture values in main; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 38 |
| main.fixture_write | reference | Parameter for reference in main.fixture_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| main.fixture_write | key | Parameter for key in main.fixture_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| main.fixture_write | register_secret | Imported dependency for register secret in main.fixture_write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| main | fixture_vault | Local binding for fixture vault in main; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| main.lambda_51 | ref | Callback parameter for ref in main.lambda_51; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 51 |
| main.lambda_52 | ref | Callback parameter for ref in main.lambda_52; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 52 |
| main.create | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 55 |
| main.create | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| main.create | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in main.create; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| main.create | service | Local binding for service in main.create; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| main.create | reuse_counts | Local binding for reuse counts in main.create; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 61 |
| main.create.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 63 |
| main.create.workflow | ApprovalStore | Imported dependency for ApprovalStore in main.create.workflow; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| main.create.workflow | WindowsDataProtection | Imported dependency for WindowsDataProtection in main.create.workflow; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| main.create.workflow | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in main.create.workflow; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| main.create.workflow | service.verification.store | Attribute for service.verification.store in main.create.workflow; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| main.create.workflow | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 84 |
| main.create.workflow | security.operation_id | Attribute for security.operation id in main.create.workflow; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| main.create.workflow | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 90, 186 |
| main.create.workflow | provisional | Local binding for provisional in main.create.workflow; use the enclosing contract and type below. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 92, 190 |
| main.create.workflow | acceptance | Local binding for acceptance in main.create.workflow; use the enclosing contract and type below. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| main.create.workflow | prepared | Local binding for prepared in main.create.workflow; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| main.create.workflow | reviewed | Local binding for reviewed in main.create.workflow; use the enclosing contract and type below. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| main.create.workflow | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| main.create.workflow | receipt | Local binding for receipt in main.create.workflow; use the enclosing contract and type below. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| main.create.workflow | cases | Local binding for cases in main.create.workflow; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 155 |
| main.create.workflow.comprehension_155 | i | Comprehension item for i in main.create.workflow.comprehension_155; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 162 |
| main.create.workflow | controller.validation | Attribute for controller.validation in main.create.workflow; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| main.create.workflow | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 193 |
| main.create | controller | Local binding for controller in main.create; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
| main.create | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in main.create; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 217 |
| main.create | SavedProfiles | Imported dependency for SavedProfiles in main.create; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 218 |
| main.create | controller.state.session_id | Attribute for controller.state.session id in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 220 |
| main.create | fixture_runtime | Local binding for fixture runtime in main.create; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| main.create | catalog_reads | Local binding for catalog reads in main.create; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 226 |
| main.create.local_catalog | url | Parameter for url in main.create.local_catalog; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 228 |
| main.create.local_catalog | names | Local binding for names in main.create.local_catalog; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 231 |
| main.create.local_catalog.comprehension_232 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 232 |
| main.create.configured_runtime | client | Parameter for client in main.create.configured_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 234 |
| main.create.configured_runtime.lambda_238 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 238 |
| main.create | controller.model_configuration | Attribute for controller.model configuration in main.create; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| main.create.lambda_251 | vault | Callback parameter for vault in main.create.lambda_251; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 251 |
| main.create.lambda_251.lambda_252 | host | Callback parameter for host in main.create.lambda_251.lambda_252; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 252 |
| main.create.lambda_254 | host | Callback parameter for host in main.create.lambda_254; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 254 |
| main | registry | Local binding for registry in main; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 259 |
| main | view | Local binding for view in main; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 260 |
