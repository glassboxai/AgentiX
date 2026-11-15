# Reference for src/agentix/bootstrap.py

Explicit composition root for optional frameworks and application startup.

Importing this module is inert. Only startup functions configure logging and
telemetry, create storage, construct models/agents or install stdout capture.

Source fingerprint: c72c7bafe973a2bcb2e4f48673c0d8e484a5dcf4c9b964ea91bd8ea6c73c6247

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _install_file_log

Attach one bounded rotating file handler under data/logs, at most once.

Payload-free event lines persist across restarts so operators can diagnose
failed operations after the console closes. Best-effort: a missing or
unwritable home never blocks startup.

Kind: callable. Declared return: None. Source line: 30.

### configure_process

Apply the legacy startup logging/telemetry policy explicitly and safely.

Optional vendor hooks are best-effort, matching prior behavior. The Rich
filter is installed at most once so repeated startup cannot wrap itself.

Kind: callable. Declared return: None. Source line: 62.

### configure_process.filtered_print

Suppress only the legacy tracing panel; forward other output.

Kind: callable. Declared return: Any. Source line: 107.

### create_llm

Construct the existing CrewAI LLM only when explicitly requested.

Kind: callable. Declared return: Any. Source line: 122.

### Runtime

Connected services for one explicit application runtime.

Kind: class. Declared return: Not declared / class. Source line: 138.

### create_runtime

Wire services at startup, without running agents or constructing a UI.

Injectable factories keep framework imports and external work out of service
tests. Production process configuration is the caller's explicit decision.

Kind: callable. Declared return: Runtime. Source line: 150.

### get_default_llm

Lazily provide the compatibility model, applying startup policy first.

Kind: callable. Declared return: Any. Source line: 235.

### get_default_runtime

Provide the single legacy runtime on first explicit workflow access.

Kind: callable. Declared return: Runtime. Source line: 242.

### get_default_tools

Register legacy tools without creating an LLM or running any agents.

Kind: callable. Declared return: SimpleNamespace. Source line: 251.

### get_default_ui

Build the session-owned view with optional explicit application-model wiring.

The default transport retains its normal resource bounds. Validation launchers
may inject a bounded client factory without changing other GUI processes or
replacing model, approval, native execution or session ownership boundaries.

Kind: callable. Declared return: tuple[Any, Any]. Source line: 258.

### get_default_ui.create_session

Create independent role objects, approvals and controller for one browser.

Kind: callable. Declared return: UiController. Source line: 285.

### run_ui

Install capture and launch the existing UI; always restore host stdout.

Kind: callable. Declared return: None. Source line: 346.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | lru_cache | Imported dependency for lru cache in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | partial | Imported dependency for partial in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | build_agents | Imported dependency for build agents in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | Orchestrator | Imported dependency for Orchestrator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | activity_output | Imported dependency for activity output in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | user_approval_store | Imported dependency for user approval store in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 27 |
| _install_file_log | root | Explicit root directory against which named paths are resolved. | Return type of getLogger; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| _install_file_log.comprehension_38 | handler | Comprehension item for handler in _install_file_log.comprehension_38; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| _install_file_log | RotatingFileHandler | Imported dependency for RotatingFileHandler in _install_file_log; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 41 |
| _install_file_log | data_directory | Imported dependency for data directory in _install_file_log; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 43 |
| _install_file_log | folder | Local binding for folder in _install_file_log; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| _install_file_log | handler | Local binding for handler in _install_file_log; use the enclosing contract and type below. | Return type of RotatingFileHandler; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| _install_file_log | handler._agentix_file_log | Attribute for handler. agentix file log in _install_file_log; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 58 |
| configure_process | SecretFilter | Imported dependency for SecretFilter in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
| configure_process | handler | Loop item for handler in configure_process; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 89 |
| configure_process.comprehension_90 | item | Comprehension item for item in configure_process.comprehension_90; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 90 |
| configure_process | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 92 |
| configure_process | set_suppress_tracing_messages | Imported dependency for set suppress tracing messages in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 95 |
| configure_process | Console | Imported dependency for Console in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 101 |
| configure_process | Panel | Imported dependency for Panel in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 102 |
| configure_process | original_print | Local binding for original print in configure_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 105 |
| configure_process.filtered_print | console | Parameter for console in configure_process.filtered_print; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 107 |
| configure_process.filtered_print | args | Parameter for args in configure_process.filtered_print; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 107 |
| configure_process.filtered_print | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 107 |
| configure_process.filtered_print.comprehension_109 | arg | Comprehension item for arg in configure_process.filtered_print.comprehension_109; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| configure_process | filtered_print._agentix_filter | Attribute for filtered print. agentix filter in configure_process; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 116 |
| configure_process | Console.print | Attribute for Console.print in configure_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| create_llm | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 122 |
| create_llm | LLM | Imported dependency for LLM in create_llm; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 124 |
| Runtime | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 141 |
| Runtime | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 142 |
| Runtime | operations | Typed binding for operations in Runtime; use the enclosing contract and type below. | ArtifactTools | Enclosing invocation or class/instance lifetime | 143 |
| Runtime | catalog | Typed binding for catalog in Runtime; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 144 |
| Runtime | registered_tools | Typed binding for registered tools in Runtime; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 145 |
| Runtime | orchestrator | Typed binding for orchestrator in Runtime; use the enclosing contract and type below. | Orchestrator | Enclosing invocation or class/instance lifetime | 146 |
| Runtime | llm | Typed binding for llm in Runtime; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 147 |
| create_runtime | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 151 |
| create_runtime | llm_factory | Parameter for llm factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 153 |
| create_runtime | tool_factory | Parameter for tool factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 154 |
| create_runtime | agent_factory | Parameter for agent factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 155 |
| create_runtime | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 156, 199 |
| create_runtime | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 157, 175 |
| create_runtime | llm | Parameter for llm in create_runtime; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 158 |
| create_runtime | owner_id | Session owner identity used to prevent cross-session authorization. | str &#124; None | Enclosing invocation or class/instance lifetime | 159 |
| create_runtime | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend &#124; None | Enclosing invocation or class/instance lifetime | 160 |
| create_runtime | approval_store | Parameter for approval store in create_runtime; use the enclosing contract and type below. | ApprovalStore &#124; None | Enclosing invocation or class/instance lifetime | 161 |
| create_runtime | require_v7_namespace | Imported dependency for require v7 namespace in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 169 |
| create_runtime | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in create_runtime; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| create_runtime | configure_storage | Local binding for configure storage in create_runtime; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| create_runtime | drafts_root | Local binding for drafts root in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 179 |
| create_runtime | execution_backend | One process boundary selected by the composition root for all owner services. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 183 |
| create_runtime | security.strict_tool_contract | Attribute for security.strict tool contract in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 186 |
| create_runtime | operations | Local binding for operations in create_runtime; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| create_runtime | catalog | Local binding for catalog in create_runtime; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 194 |
| create_runtime | model | Local binding for model in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 195 |
| create_runtime | registered | Local binding for registered in create_runtime; use the enclosing contract and type below. | Return type of tool_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| create_runtime | agents | Local binding for agents in create_runtime; use the enclosing contract and type below. | Return type of agent_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| create_runtime | AppInvocation | Imported dependency for AppInvocation in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 200 |
| create_runtime | CatalogToolRegistry | Imported dependency for CatalogToolRegistry in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 201 |
| create_runtime | InstalledApps | Imported dependency for InstalledApps in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| create_runtime | applications | Local binding for applications in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 204 |
| create_runtime | RoutingModelClient | Imported dependency for RoutingModelClient in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| create_runtime | ToolRouter | Imported dependency for ToolRouter in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| create_runtime | data_directory | Imported dependency for data directory in create_runtime; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 212 |
| create_runtime | router | Local binding for router in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 214 |
| create_runtime.lambda_216 | evidence | Callback parameter for evidence in create_runtime.lambda_216; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 216 |
| create_runtime | orchestrator | Local binding for orchestrator in create_runtime; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| get_default_ui | application_coordinator_factory | Parameter for application coordinator factory in get_default_ui; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 260 |
| get_default_ui | retrieval_service_factory | Parameter for retrieval service factory in get_default_ui; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 261 |
| get_default_ui | UiController | Imported dependency for UiController in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 269 |
| get_default_ui | build_view | Imported dependency for build view in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 270 |
| get_default_ui | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of get_default_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 272 |
| get_default_ui | gr | Imported dependency for gr in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 273 |
| get_default_ui | controller | Local binding for controller in get_default_ui; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 275 |
| get_default_ui | SessionRegistry | Imported dependency for SessionRegistry in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 283 |
| get_default_ui.create_session | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str | Enclosing invocation or class/instance lifetime | 285 |
| get_default_ui.create_session | local_settings | Local binding for local settings in get_default_ui.create_session; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 290 |
| get_default_ui.create_session | owned_runtime | Local binding for owned runtime in get_default_ui.create_session; use the enclosing contract and type below. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 293 |
| get_default_ui.create_session | owned_controller | Local binding for owned controller in get_default_ui.create_session; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 294 |
| get_default_ui.create_session | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 302 |
| get_default_ui.create_session | data_directory | Imported dependency for data directory in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 303 |
| get_default_ui.create_session | SavedProfiles | Imported dependency for SavedProfiles in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 304 |
| get_default_ui.create_session | owned_controller.state.session_id | Attribute for owned controller.state.session id in get_default_ui.create_session; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 306 |
| get_default_ui.create_session | owned_controller.model_configuration | Attribute for owned controller.model configuration in get_default_ui.create_session; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 307 |
| get_default_ui.create_session.lambda_309 | client | Callback parameter for client in get_default_ui.create_session.lambda_309; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 309 |
| get_default_ui.create_session.lambda_316 | vault | Callback parameter for vault in get_default_ui.create_session.lambda_316; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 316 |
| get_default_ui | sessions | Local binding for sessions in get_default_ui; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 323 |
| get_default_ui | ApplicationPipeline | Imported dependency for ApplicationPipeline in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 324 |
| get_default_ui | ApplicationsBackend | Imported dependency for ApplicationsBackend in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 325 |
| get_default_ui | HostRequirements | Imported dependency for HostRequirements in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 326 |
| get_default_ui | GuiToolRetrieval | Imported dependency for GuiToolRetrieval in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 327 |
| get_default_ui | retrieval | Local binding for retrieval in get_default_ui; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| get_default_ui | application_options | Local binding for application options in get_default_ui; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 331 |
| get_default_ui | applications | Local binding for applications in get_default_ui; use the enclosing contract and type below. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 336 |
| get_default_ui | view | Local binding for view in get_default_ui; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 342 |
| run_ui | launch | Imported dependency for launch in run_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 348 |
| run_ui | controller | Local binding for controller in run_ui; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 350 |
| run_ui | view | Local binding for view in run_ui; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 350 |
| run_ui | settings | Immutable startup configuration; constructing it does not start external services. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 353 |
