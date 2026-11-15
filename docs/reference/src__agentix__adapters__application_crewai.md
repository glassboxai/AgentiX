# Reference for src/agentix/adapters/application_crewai.py

CrewAI coordination for catalog applications; artifact execution stays native.

Crews produce data and widget source for review. They receive no execution tools,
filesystem capabilities or approval authority. All external dependencies are
injected; the factory below is the local application's composition root.

Source fingerprint: 870326112050e5d5dfa53dc396861fcf44b749e2a8b37f82ef85c2f6fb3453ea

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### CrewApplicationCoordinator

One session-owned model and two sequential creation phases with explicit context.

Kind: class. Declared return: Not declared / class. Source line: 41.

### CrewApplicationCoordinator.__init__

Inject inert framework/model dependencies and a fresh operation evidence path.

Kind: callable. Declared return: None. Source line: 44.

### CrewApplicationCoordinator._save

Persist bounded private task evidence; never publish it in ordinary logs.

Kind: callable. Declared return: None. Source line: 52.

### CrewApplicationCoordinator._agent

Create a bounded verbose role with no tools, delegation or approval authority.

Kind: callable. Declared return: Any. Source line: 60.

### CrewApplicationCoordinator._task

Declare structured task output and explicit predecessor context in CrewAI.

Kind: callable. Declared return: Any. Source line: 76.

### CrewApplicationCoordinator._run

Run one sequential crew, reject missing structured output and release capacity.

Kind: callable. Declared return: list[dict]. Source line: 93.

### CrewApplicationCoordinator.plan

Generate and review persisted connection code; host never interprets a graph.

Kind: callable. Declared return: dict. Source line: 129.

### CrewApplicationCoordinator.widgets

Generate only missing widgets in one sequential crew with the reviewed plan context.

Kind: callable. Declared return: dict[str, dict]. Source line: 158.

### make_application_coordinator

Compose a coordinator, preserving an injected session client when supplied.

The fallback retains the legacy local application profile for direct callers.
Session-owned UI flows inject their validated active client instead.

Kind: callable. Declared return: CrewApplicationCoordinator. Source line: 185.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | MODEL_GATE | Imported dependency for MODEL GATE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | WidgetProposal | Imported dependency for WidgetProposal in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | CatalogWidgetDesigner | Imported dependency for CatalogWidgetDesigner in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ApplicationCode | Imported dependency for ApplicationCode in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 22 |
| module | MAX_EVIDENCE_BYTES | Module binding for MAX EVIDENCE BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 24 |
| module | AGENT_MAX_ITERATIONS | Module binding for AGENT MAX ITERATIONS in module; use the enclosing contract and type below. | int | Module/process lifetime | 26 |
| module | AGENT_MAX_RETRY_LIMIT | Module binding for AGENT MAX RETRY LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 27 |
| module | AGENT_MAX_EXECUTION_SECONDS | Module binding for AGENT MAX EXECUTION SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 28 |
| module | TASK_GUARDRAIL_MAX_RETRIES | Module binding for TASK GUARDRAIL MAX RETRIES in module; use the enclosing contract and type below. | int | Module/process lifetime | 30 |
| module | DEFAULT_MODEL_TIMEOUT_SECONDS | Module binding for DEFAULT MODEL TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 32 |
| module | MIN_MODEL_TIMEOUT_SECONDS | Module binding for MIN MODEL TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 33 |
| module | MAX_MODEL_TIMEOUT_SECONDS | Module binding for MAX MODEL TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 34 |
| module | MODEL_TEMPERATURE | Module binding for MODEL TEMPERATURE in module; use the enclosing contract and type below. | float | Module/process lifetime | 36 |
| module | MODEL_MAX_TOKENS | Module binding for MODEL MAX TOKENS in module; use the enclosing contract and type below. | int | Module/process lifetime | 37 |
| module | MODEL_MAX_RETRIES | Module binding for MODEL MAX RETRIES in module; use the enclosing contract and type below. | int | Module/process lifetime | 38 |
| CrewApplicationCoordinator.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| CrewApplicationCoordinator.__init__ | evidence | Parameter for evidence in CrewApplicationCoordinator.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 44 |
| CrewApplicationCoordinator.__init__ | llm | Parameter for llm in CrewApplicationCoordinator.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 44 |
| CrewApplicationCoordinator.__init__ | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 44 |
| CrewApplicationCoordinator.__init__ | self.evidence | Attribute for evidence in CrewApplicationCoordinator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| CrewApplicationCoordinator.__init__ | self.llm | Attribute for llm in CrewApplicationCoordinator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| CrewApplicationCoordinator.__init__ | self.backend | Injected framework/execution provider; callers determine the required protocol. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| CrewApplicationCoordinator.__init__ | self.plan_task | Attribute for plan task in CrewApplicationCoordinator.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 50 |
| CrewApplicationCoordinator._save | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| CrewApplicationCoordinator._save | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 52 |
| CrewApplicationCoordinator._save | value | Value at the current validation/rendering boundary; apply the enclosing contract. | dict | Enclosing invocation or class/instance lifetime | 52 |
| CrewApplicationCoordinator._save | encoded | Local binding for encoded in CrewApplicationCoordinator._save; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| CrewApplicationCoordinator._agent | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| CrewApplicationCoordinator._agent | role | Parameter for role in CrewApplicationCoordinator._agent; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 60 |
| CrewApplicationCoordinator._agent | goal | Parameter for goal in CrewApplicationCoordinator._agent; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 60 |
| CrewApplicationCoordinator._task | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._task | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._task | agent | Parameter for agent in CrewApplicationCoordinator._task; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._task | request | Parameter for request in CrewApplicationCoordinator._task; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._task | response | Bounded response text to render or validate; it is not executable code. | type[BaseModel] | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._task | context | Parameter for context in CrewApplicationCoordinator._task; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 77 |
| CrewApplicationCoordinator._run | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| CrewApplicationCoordinator._run | stage | Parameter for stage in CrewApplicationCoordinator._run; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 93 |
| CrewApplicationCoordinator._run | agents | Parameter for agents in CrewApplicationCoordinator._run; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 93 |
| CrewApplicationCoordinator._run | tasks | Parameter for tasks in CrewApplicationCoordinator._run; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 93 |
| CrewApplicationCoordinator._run | started | Local binding for started in CrewApplicationCoordinator._run; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| CrewApplicationCoordinator._run | crew | Local binding for crew in CrewApplicationCoordinator._run; use the enclosing contract and type below. | Return type of Crew; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| CrewApplicationCoordinator._run | outputs | Local binding for outputs in CrewApplicationCoordinator._run; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 109 |
| CrewApplicationCoordinator._run | task | Loop item for task in CrewApplicationCoordinator._run; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 110 |
| CrewApplicationCoordinator._run | model | Local binding for model in CrewApplicationCoordinator._run; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| CrewApplicationCoordinator._run | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of model_dump; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| CrewApplicationCoordinator._run | error | Caught exception for error in CrewApplicationCoordinator._run; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 120 |
| CrewApplicationCoordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| CrewApplicationCoordinator.plan | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 129 |
| CrewApplicationCoordinator.plan | schemas | Parameter for schemas in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 129 |
| CrewApplicationCoordinator.plan | feedback | Parameter for feedback in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 129 |
| CrewApplicationCoordinator.plan | request | Local binding for request in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 131 |
| CrewApplicationCoordinator.plan | planner | Local binding for planner in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Return type of _agent; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| CrewApplicationCoordinator.plan | integrator | Local binding for integrator in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Return type of _agent; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| CrewApplicationCoordinator.plan | first | Local binding for first in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Return type of _task; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| CrewApplicationCoordinator.plan | review | Local binding for review in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| CrewApplicationCoordinator.plan | final | Local binding for final in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Return type of _task; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| CrewApplicationCoordinator.plan | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 153, 154 |
| CrewApplicationCoordinator.plan | self.plan_task | Attribute for plan task in CrewApplicationCoordinator.plan; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 155 |
| CrewApplicationCoordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 158 |
| CrewApplicationCoordinator.widgets | tools | Parameter for tools in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 158 |
| CrewApplicationCoordinator.widgets | feedback | Parameter for feedback in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 158 |
| CrewApplicationCoordinator.widgets | designer | Local binding for designer in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | Return type of _agent; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| CrewApplicationCoordinator.widgets | tasks | Local binding for tasks in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 168 |
| CrewApplicationCoordinator.widgets.comprehension_168 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 176 |
| CrewApplicationCoordinator.widgets.comprehension_168 | tool | Comprehension item for tool in CrewApplicationCoordinator.widgets.comprehension_168; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 176 |
| CrewApplicationCoordinator.widgets | outputs | Local binding for outputs in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | Return type of _run; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| CrewApplicationCoordinator.widgets | proposals | Local binding for proposals in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| CrewApplicationCoordinator.widgets | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 180 |
| CrewApplicationCoordinator.widgets | proposal | Loop item for proposal in CrewApplicationCoordinator.widgets; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 180 |
| make_application_coordinator | evidence | Parameter for evidence in make_application_coordinator; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 186 |
| make_application_coordinator | timeout | Parameter for timeout in make_application_coordinator; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 188 |
| make_application_coordinator | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 189, 204 |
| make_application_coordinator | llm_factory | Parameter for llm factory in make_application_coordinator; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 190 |
| make_application_coordinator | llm | Parameter for llm in make_application_coordinator; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 191, 207 |
| make_application_coordinator | factory | Local binding for factory in make_application_coordinator; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 206 |
