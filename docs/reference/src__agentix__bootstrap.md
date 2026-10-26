# Reference for src/agentix/bootstrap.py

Explicit composition root for optional frameworks and application startup.

Importing this module is inert. Only startup functions configure logging and
telemetry, create storage, construct models/agents or install stdout capture.

Source fingerprint: 152915a812a14bae9114b01065620b5aa13df5b3f19c66034a3eb25227349eb4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### configure_process

Apply the legacy startup logging/telemetry policy explicitly and safely.

Optional vendor hooks are best-effort, matching prior behavior. The Rich
filter is installed at most once so repeated startup cannot wrap itself.

Kind: callable. Declared return: None. Source line: 30.

### configure_process.filtered_print

Suppress only the legacy tracing panel; forward other output.

Kind: callable. Declared return: Any. Source line: 71.

### create_llm

Construct the existing CrewAI LLM only when explicitly requested.

Kind: callable. Declared return: Any. Source line: 86.

### Runtime

Connected services for one explicit application runtime.

Kind: class. Declared return: Not declared / class. Source line: 102.

### create_runtime

Wire services at startup, without running agents or constructing a UI.

Injectable factories keep framework imports and external work out of service
tests. Production process configuration is the caller's explicit decision.

Kind: callable. Declared return: Runtime. Source line: 114.

### get_default_llm

Lazily provide the compatibility model, applying startup policy first.

Kind: callable. Declared return: Any. Source line: 157.

### get_default_runtime

Provide the single legacy runtime on first explicit workflow access.

Kind: callable. Declared return: Runtime. Source line: 164.

### get_default_tools

Register legacy tools without creating an LLM or running any agents.

Kind: callable. Declared return: SimpleNamespace. Source line: 173.

### get_default_ui

Build the session-aware view and a separate legacy compatibility controller.

Kind: callable. Declared return: tuple[Any, Any]. Source line: 180.

### get_default_ui.create_session

Create independent role objects, approvals and controller for one browser.

Kind: callable. Declared return: UiController. Source line: 197.

### run_ui

Install capture and launch the existing UI; always restore host stdout.

Kind: callable. Declared return: None. Source line: 244.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | lru_cache | Imported dependency for lru cache in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | build_agents | Imported dependency for build agents in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | register_tools | Imported dependency for register tools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | user_approval_store | Imported dependency for user approval store in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | activity_output | Imported dependency for activity output in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | Orchestrator | Imported dependency for Orchestrator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 27 |
| configure_process | SecretFilter | Imported dependency for SecretFilter in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 46 |
| configure_process | handler | Loop item for handler in configure_process; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 53 |
| configure_process.comprehension_54 | item | Comprehension item for item in configure_process.comprehension_54; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 54 |
| configure_process | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 56 |
| configure_process | set_suppress_tracing_messages | Imported dependency for set suppress tracing messages in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 59 |
| configure_process | Console | Imported dependency for Console in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 65 |
| configure_process | Panel | Imported dependency for Panel in configure_process; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 66 |
| configure_process | original_print | Local binding for original print in configure_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| configure_process.filtered_print | console | Parameter for console in configure_process.filtered_print; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 71 |
| configure_process.filtered_print | args | Parameter for args in configure_process.filtered_print; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 71 |
| configure_process.filtered_print | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 71 |
| configure_process.filtered_print.comprehension_73 | arg | Comprehension item for arg in configure_process.filtered_print.comprehension_73; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 75 |
| configure_process | filtered_print._agentix_filter | Attribute for filtered print. agentix filter in configure_process; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 80 |
| configure_process | Console.print | Attribute for Console.print in configure_process; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| create_llm | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 86 |
| create_llm | LLM | Imported dependency for LLM in create_llm; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 88 |
| Runtime | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 105 |
| Runtime | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 106 |
| Runtime | operations | Typed binding for operations in Runtime; use the enclosing contract and type below. | ArtifactTools | Enclosing invocation or class/instance lifetime | 107 |
| Runtime | catalog | Typed binding for catalog in Runtime; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 108 |
| Runtime | registered_tools | Typed binding for registered tools in Runtime; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 109 |
| Runtime | orchestrator | Typed binding for orchestrator in Runtime; use the enclosing contract and type below. | Orchestrator | Enclosing invocation or class/instance lifetime | 110 |
| Runtime | llm | Typed binding for llm in Runtime; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 111 |
| create_runtime | settings | Immutable startup configuration; constructing it does not start external services. | Settings | Enclosing invocation or class/instance lifetime | 115 |
| create_runtime | llm_factory | Parameter for llm factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 117 |
| create_runtime | tool_factory | Parameter for tool factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 118 |
| create_runtime | agent_factory | Parameter for agent factory in create_runtime; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 119 |
| create_runtime | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 120, 150 |
| create_runtime | security | Owner-scoped approval and path boundary injected into this service. | Any | Enclosing invocation or class/instance lifetime | 121, 133 |
| create_runtime | llm | Parameter for llm in create_runtime; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 122 |
| create_runtime | owner_id | Session owner identity used to prevent cross-session authorization. | str &#124; None | Enclosing invocation or class/instance lifetime | 123 |
| create_runtime | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend &#124; None | Enclosing invocation or class/instance lifetime | 124 |
| create_runtime | approval_store | Parameter for approval store in create_runtime; use the enclosing contract and type below. | ApprovalStore &#124; None | Enclosing invocation or class/instance lifetime | 125 |
| create_runtime | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in create_runtime; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| create_runtime | execution_backend | One process boundary selected by the composition root for all owner services. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| create_runtime | operations | Local binding for operations in create_runtime; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| create_runtime | catalog | Local binding for catalog in create_runtime; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| create_runtime | model | Local binding for model in create_runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 146 |
| create_runtime | registered | Local binding for registered in create_runtime; use the enclosing contract and type below. | Return type of tool_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| create_runtime | agents | Local binding for agents in create_runtime; use the enclosing contract and type below. | Return type of agent_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| create_runtime | orchestrator | Local binding for orchestrator in create_runtime; use the enclosing contract and type below. | Return type of Orchestrator; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| get_default_ui | UiController | Imported dependency for UiController in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 182 |
| get_default_ui | build_view | Imported dependency for build view in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 183 |
| get_default_ui | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of get_default_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 185 |
| get_default_ui | gr | Imported dependency for gr in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 186 |
| get_default_ui | controller | Local binding for controller in get_default_ui; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| get_default_ui | SessionRegistry | Imported dependency for SessionRegistry in get_default_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| get_default_ui.create_session | session_id | Browser or terminal session identifier for state and diagnostic ownership. | str | Enclosing invocation or class/instance lifetime | 197 |
| get_default_ui.create_session | local_settings | Local binding for local settings in get_default_ui.create_session; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| get_default_ui.create_session | owned_runtime | Local binding for owned runtime in get_default_ui.create_session; use the enclosing contract and type below. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 205 |
| get_default_ui.create_session | owned_controller | Local binding for owned controller in get_default_ui.create_session; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| get_default_ui.create_session | Path | Imported dependency for Path in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 213 |
| get_default_ui.create_session | SessionModelConfiguration | Imported dependency for SessionModelConfiguration in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 215 |
| get_default_ui.create_session | SavedProfiles | Imported dependency for SavedProfiles in get_default_ui.create_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 216 |
| get_default_ui.create_session | owned_controller.state.session_id | Attribute for owned controller.state.session id in get_default_ui.create_session; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 218 |
| get_default_ui.create_session | owned_controller.model_configuration | Attribute for owned controller.model configuration in get_default_ui.create_session; use the enclosing contract and type below. | Return type of SessionModelConfiguration; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| get_default_ui.create_session.lambda_221 | client | Callback parameter for client in get_default_ui.create_session.lambda_221; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 221 |
| get_default_ui.create_session.lambda_227 | vault | Callback parameter for vault in get_default_ui.create_session.lambda_227; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 227 |
| get_default_ui | view | Local binding for view in get_default_ui; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 240 |
| run_ui | launch | Imported dependency for launch in run_ui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 246 |
| run_ui | controller | Local binding for controller in run_ui; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| run_ui | view | Local binding for view in run_ui; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| run_ui | settings | Immutable startup configuration; constructing it does not start external services. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 251 |
