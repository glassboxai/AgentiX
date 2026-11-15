# Reference for tests/application_review_server.py

Disposable real GUI/native server with trusted installed tools and model doubles.

Approval publication below is an explicit trusted test boundary, not a production
approval shortcut. No existing artifacts, live model, API keys or user data are used.

Source fingerprint: 0d010fe390f937097ad9d798d5aff05b108a2b883de452147f68ee675f7215b5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Own temporary installed tool grants and one disposable loopback listener.

Kind: callable. Declared return: Not declared / class. Source line: 37.

### main.record

Persist only bounded test audit metadata, never prompts/secrets.

Kind: callable. Declared return: Not declared / class. Source line: 49.

### main.create

Provide real catalog/ledger services with explicit fixture grants per owner.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### main.create.CountingSandbox

Observe actual fixture unittest requests without claiming native isolation.

Kind: class. Declared return: Not declared / class. Source line: 72.

### main.create.CountingSandbox.execute

Count test invocations independently of orchestration messages.

Kind: callable. Declared return: Not declared / class. Source line: 75.

### main.create.workflow

Simulate background latency without executing model/tool code.

Kind: callable. Declared return: Not declared / class. Source line: 103.

### main.create.models

Simulate local tags latency; no download or inference.

Kind: callable. Declared return: Not declared / class. Source line: 142.

### main.create.ExplanationClient

Synthetic read-only model boundary; no inference or credentials.

Kind: class. Declared return: Not declared / class. Source line: 152.

### main.create.ExplanationClient.call

Retain fixture-only input for independent browser assertions.

Kind: callable. Declared return: Not declared / class. Source line: 155.

### main.client_factory

Return deterministic model proposals, clearly separate from native evidence.

Kind: callable. Declared return: Not declared / class. Source line: 215.

### main.client_factory.client

Use reviewed maintained fixture widgets as model-boundary test doubles.

Kind: callable. Declared return: Not declared / class. Source line: 218.

### main.CodeCasesCoordinator

Use canonical authored calculator fixtures for schema-3 browser review.

Kind: class. Declared return: Not declared / class. Source line: 247.

### main.CodeCasesCoordinator.plan

Return a dependent call with no matching second reviewed value.

Kind: callable. Declared return: Not declared / class. Source line: 250.

### main.CodeCasesCoordinator.widgets

Supply inert widgets with the current named-controls contract.

Kind: callable. Declared return: Not declared / class. Source line: 256.

### main.native

Inject one controlled failure, then use the real Windows isolation boundary.

Kind: callable. Declared return: Not declared / class. Source line: 267.

### main.record_candidate_limit

Record model-double requests without storing descriptions or source.

Kind: callable. Declared return: None. Source line: 332.

### main.observed_pipeline

Record exactly which tool roles reach the unchanged generation boundary.

Kind: callable. Declared return: Any. Source line: 343.

### main.observed_pipeline.generate

Delegate fixture generation and retain only dependency names in the audit.

Kind: callable. Declared return: Any. Source line: 348.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | gr | Imported dependency for gr in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | widget_source | Imported dependency for widget source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | installed | Imported dependency for installed in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | TrustedFixtureSandbox | Imported dependency for TrustedFixtureSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | ApplicationPipeline | Imported dependency for ApplicationPipeline in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | execute_application | Imported dependency for execute application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| module | ModelProfile | Imported dependency for ModelProfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 30 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 31 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 32 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 33 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 34 |
| main | port | Local binding for port in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 40 |
| main | root | Explicit root directory against which named paths are resolved. | tuple | Enclosing invocation or class/instance lifetime | 40 |
| main | audit | Local binding for audit in main; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 42 |
| main | controllers_by_catalog | Typed binding for controllers by catalog in main; use the enclosing contract and type below. | dict[str, UiController] | Enclosing invocation or class/instance lifetime | 55 |
| main.create | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| main.create | folder | Local binding for folder in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| main.create | fixture | Local binding for fixture in main.create; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| main.create | mode | Local binding for mode in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62 |
| main.create | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| main.create | WindowsSandbox | Imported dependency for WindowsSandbox in main.create; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 68 |
| main.create | sandbox_type | Local binding for sandbox type in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| main.create.CountingSandbox.execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | tests | Optional unittest source snapshot; child-authored success remains provisional. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | tool_name | Validated public tool identifier within the configured storage boundary. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | function_name | Public callable selected for the current operation; empty selects test mode. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create.CountingSandbox.execute | observation | Parameter for observation in main.create.CountingSandbox.execute; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| main.create | operations | Local binding for operations in main.create; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| main.create | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 86, 147 |
| main.create | grant | Loop item for grant in main.create; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 86 |
| main.create | function | Local binding for function in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| main.create | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 88 |
| main.create | fixture.ledger | Attribute for fixture.ledger in main.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| main.create.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 103 |
| main.create.workflow | package | Local binding for package in main.create.workflow; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 107 |
| main.create.workflow | execution | Local binding for execution in main.create.workflow; use the enclosing contract and type below. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| main.create.workflow | observed | Returned observation checked against the reviewed host-side expectation. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 122 |
| main.create | controller | Local binding for controller in main.create; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| main.create.models | url | Parameter for url in main.create.models; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 142 |
| main.create.ExplanationClient.call | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 155 |
| main.create.ExplanationClient.call | messages | Parameter for messages in main.create.ExplanationClient.call; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 155 |
| main.create | controller.model_configuration | Attribute for controller.model configuration in main.create; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 203 |
| main.client_factory | folder | Parameter for folder in main.client_factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 215 |
| main.client_factory.client | role | Parameter for role in main.client_factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 218 |
| main.client_factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 218 |
| main.client_factory.client | module | Local binding for module in main.client_factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 224 |
| main.client_factory.client | catalog | Local binding for catalog in main.client_factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 230 |
| main.client_factory.client.comprehension_233 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 233 |
| main.client_factory.client.comprehension_238 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 239 |
| main.CodeCasesCoordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 250 |
| main.CodeCasesCoordinator.plan | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 250 |
| main.CodeCasesCoordinator.plan | schemas | Parameter for schemas in main.CodeCasesCoordinator.plan; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 250 |
| main.CodeCasesCoordinator.plan | feedback | Parameter for feedback in main.CodeCasesCoordinator.plan; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 250 |
| main.CodeCasesCoordinator.plan | proposal | Imported dependency for proposal in main.CodeCasesCoordinator.plan; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 252 |
| main.CodeCasesCoordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 256 |
| main.CodeCasesCoordinator.widgets | tools | Parameter for tools in main.CodeCasesCoordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 256 |
| main.CodeCasesCoordinator.widgets | feedback | Parameter for feedback in main.CodeCasesCoordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 256 |
| main.CodeCasesCoordinator.widgets | WIDGET | Imported dependency for WIDGET in main.CodeCasesCoordinator.widgets; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 258 |
| main.CodeCasesCoordinator.widgets.comprehension_260 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 262 |
| main | failures | Local binding for failures in main; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 265 |
| main.native | snapshot | Parameter for snapshot in main.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| main.native | payload | Parameter for payload in main.native; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| main | sessions | Local binding for sessions in main; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 277 |
| main | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 278 |
| main.lambda_280 | folder | Callback parameter for folder in main.lambda_280; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 280 |
| main.lambda_280.lambda_283 | _ | Callback parameter for  in main.lambda_280.lambda_283; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 283 |
| main | approved_tool | Imported dependency for approved tool in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 292 |
| main | backend.pipeline_factory | Attribute for backend.pipeline factory in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 295, 359 |
| main.lambda_295 | folder | Callback parameter for folder in main.lambda_295; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 295 |
| main.lambda_295.lambda_297 | _ | Callback parameter for  in main.lambda_295.lambda_297; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 297 |
| main | backend.registry_factory | Attribute for backend.registry factory in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 300 |
| main.lambda_300 | controller | Callback parameter for controller in main.lambda_300; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 300 |
| main.lambda_300.lambda_301 | tools | Callback parameter for tools in main.lambda_300.lambda_301; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 301 |
| main | published_with_tools | Imported dependency for published with tools in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 305 |
| main | seed_root | Local binding for seed root in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 307 |
| main | seed_library | Local binding for seed library in main; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 309 |
| main | seeded | Local binding for seeded in main; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 309 |
| main | fixture | Local binding for fixture in main; use the enclosing contract and type below. | Return type of published_with_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 309 |
| main | uuid4 | Imported dependency for uuid4 in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 312 |
| main | Candidate | Imported dependency for Candidate in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 314 |
| main | approve_application | Imported dependency for approve application in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| main | item | Local binding for item in main; use the enclosing contract and type below. | Return type of Candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 317 |
| main | RegistryRetrievalDouble | Imported dependency for RegistryRetrievalDouble in main; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 330 |
| main.record_candidate_limit | limit | Parameter for limit in main.record_candidate_limit; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 332 |
| main | backend.retrieval | Attribute for backend.retrieval in main; use the enclosing contract and type below. | Return type of RegistryRetrievalDouble; see its callable contract | Enclosing invocation or class/instance lifetime | 337 |
| main.lambda_338 | catalog | Callback parameter for catalog in main.lambda_338; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 338 |
| main | original_pipeline_factory | Local binding for original pipeline factory in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 341 |
| main.observed_pipeline | folder | Parameter for folder in main.observed_pipeline; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 343 |
| main.observed_pipeline | pipeline | Local binding for pipeline in main.observed_pipeline; use the enclosing contract and type below. | Return type of original_pipeline_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 345 |
| main.observed_pipeline | original_generate | Local binding for original generate in main.observed_pipeline; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 346 |
| main.observed_pipeline.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 348 |
| main.observed_pipeline.generate | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 348 |
| main.observed_pipeline | pipeline.generate | Attribute for pipeline.generate in main.observed_pipeline; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 356 |
| main | view | Local binding for view in main; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 360 |
