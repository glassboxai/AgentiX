# Reference for tests/e2e/server.py

Disposable real UI with trusted fixtures; never load a model or project artifacts.

This executable is test infrastructure only. Its OS boundary double must never
be used for untrusted input. The parent owns process and temporary-directory cleanup.

Source fingerprint: 240dc2214287b28cce9c898366e9e768ee1d8dd1a33ae0dfac2e8e04404a4161

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Serve only loopback on the supplied temporary port and artifact root.

Kind: callable. Declared return: None. Source line: 32.

### main.fixture_write

Model validation and a deterministic denial without exposing the key.

Kind: callable. Declared return: Not declared / class. Source line: 38.

### main.create

Give each browser its own real approvals, ledger and artifact services.

Kind: callable. Declared return: UiController. Source line: 53.

### main.create.workflow

Exercise actual storage, provisional tests, review and host comparison.

Kind: callable. Declared return: str. Source line: 61.

### main.create.local_catalog

Make the manual refresh reveal an additional installed model.

Kind: callable. Declared return: Not declared / class. Source line: 226.

### main.create.configured_runtime

Expose the configured fake client identity through the real query UI.

Kind: callable. Declared return: Not declared / class. Source line: 232.

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
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| main | folder | Local binding for folder in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 34 |
| main | port | Local binding for port in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 34 |
| main | fixture_values | Local binding for fixture values in main; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 36 |
| main.fixture_write | reference | Parameter for reference in main.fixture_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| main.fixture_write | key | Parameter for key in main.fixture_write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| main.fixture_write | register_secret | Imported dependency for register secret in main.fixture_write; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 40 |
| main | fixture_vault | Local binding for fixture vault in main; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| main.lambda_49 | ref | Callback parameter for ref in main.lambda_49; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 49 |
| main.lambda_50 | ref | Callback parameter for ref in main.lambda_50; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 50 |
| main.create | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 53 |
| main.create | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| main.create | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in main.create; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| main.create | service | Local binding for service in main.create; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| main.create | reuse_counts | Local binding for reuse counts in main.create; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 59 |
| main.create.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 61 |
| main.create.workflow | ApprovalStore | Imported dependency for ApprovalStore in main.create.workflow; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 71 |
| main.create.workflow | WindowsDataProtection | Imported dependency for WindowsDataProtection in main.create.workflow; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 72 |
| main.create.workflow | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in main.create.workflow; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| main.create.workflow | service.verification.store | Attribute for service.verification.store in main.create.workflow; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| main.create.workflow | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 82 |
| main.create.workflow | security.operation_id | Attribute for security.operation id in main.create.workflow; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| main.create.workflow | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 88, 184 |
| main.create.workflow | provisional | Local binding for provisional in main.create.workflow; use the enclosing contract and type below. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 90, 188 |
| main.create.workflow | acceptance | Local binding for acceptance in main.create.workflow; use the enclosing contract and type below. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| main.create.workflow | prepared | Local binding for prepared in main.create.workflow; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| main.create.workflow | reviewed | Local binding for reviewed in main.create.workflow; use the enclosing contract and type below. | Return type of submit_acceptance_cases_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| main.create.workflow | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| main.create.workflow | receipt | Local binding for receipt in main.create.workflow; use the enclosing contract and type below. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| main.create.workflow | cases | Local binding for cases in main.create.workflow; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 153 |
| main.create.workflow.comprehension_153 | i | Comprehension item for i in main.create.workflow.comprehension_153; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 160 |
| main.create.workflow | controller.validation | Attribute for controller.validation in main.create.workflow; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| main.create.workflow | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 191 |
| main.create | controller | Local binding for controller in main.create; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| main.create | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in main.create; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 215 |
| main.create | SavedProfiles | Imported dependency for SavedProfiles in main.create; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 216 |
| main.create | controller.state.session_id | Attribute for controller.state.session id in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 218 |
| main.create | fixture_runtime | Local binding for fixture runtime in main.create; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| main.create | catalog_reads | Local binding for catalog reads in main.create; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 224 |
| main.create.local_catalog | url | Parameter for url in main.create.local_catalog; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 226 |
| main.create.local_catalog | names | Local binding for names in main.create.local_catalog; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 229 |
| main.create.local_catalog.comprehension_230 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 230 |
| main.create.configured_runtime | client | Parameter for client in main.create.configured_runtime; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
| main.create.configured_runtime.lambda_236 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 236 |
| main.create | controller.model_configuration | Attribute for controller.model configuration in main.create; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 244 |
| main.create.lambda_249 | vault | Callback parameter for vault in main.create.lambda_249; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 249 |
| main.create.lambda_249.lambda_250 | host | Callback parameter for host in main.create.lambda_249.lambda_250; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 250 |
| main.create.lambda_252 | host | Callback parameter for host in main.create.lambda_252; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 252 |
| main | view | Local binding for view in main; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
