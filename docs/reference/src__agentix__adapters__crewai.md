# Reference for src/agentix/adapters/crewai.py

Explicit CrewAI tool registration and agent construction.

Factories import optional dependencies only when called. The manager can request
session-owned reuse preparation or first-use isolated verification; prompts are not the
security boundary, which remains in the application services.

Source fingerprint: ffdf8f7a201a3e8e29d558fee300a9b060070d93639702d7d922a59b156419f7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### AgentSet

Session-owned workflow roles and separate tool-free classification managers.

Kind: class. Declared return: Not declared / class. Source line: 50.

### _bind_operation

Expose a bound service method as a function with its public signature.

CrewAI introspects function metadata to create Pydantic schemas. Preserve
annotations/docstrings and omit the already-bound self parameter explicitly.

Kind: callable. Declared return: Callable[..., str]. Source line: 61.

### _bind_operation.wrapper

Forward arguments to the owning service without changing its result.

Kind: callable. Declared return: str. Source line: 69.

### register_tools

Register bound operation signatures under their existing public tool names.

Kind: callable. Declared return: SimpleNamespace. Source line: 85.

### register_tools.conditional

Return the service result and set terminality from its outcome.

Kind: callable. Declared return: str. Source line: 112.

### build_agents

Construct verbose role instructions without executing any agent tasks.

Kind: callable. Declared return: AgentSet. Source line: 139.

### build_agents.Agent

Apply finite role budgets while preserving existing verbose behavior.

Kind: callable. Declared return: Any. Source line: 146.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | APPLICATION_SUGGESTION_POLICY | Imported dependency for APPLICATION SUGGESTION POLICY in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | WORKFLOW_POLICY | Imported dependency for WORKFLOW POLICY in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | SECURITY_GUARDRAILS | Module binding for SECURITY GUARDRAILS in module; use the enclosing contract and type below. | str | Module/process lifetime | 19 |
| module | AGENT_MAX_ITERATIONS | Module binding for AGENT MAX ITERATIONS in module; use the enclosing contract and type below. | int | Module/process lifetime | 29 |
| module | AGENT_MAX_EXECUTION_SECONDS | Module binding for AGENT MAX EXECUTION SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 30 |
| module | AGENT_MAX_RETRY_LIMIT | Module binding for AGENT MAX RETRY LIMIT in module; use the enclosing contract and type below. | int | Module/process lifetime | 31 |
| module | TERMINAL_RESULT_TOOLS | Module binding for TERMINAL RESULT TOOLS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 33 |
| module | REPAIRABLE_RESULT_TOOLS | Module binding for REPAIRABLE RESULT TOOLS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 42 |
| module | REJECTION_PREFIXES | Module binding for REJECTION PREFIXES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 43 |
| module | ACCEPTANCE_REVIEW_TOOL | Module binding for ACCEPTANCE REVIEW TOOL in module; use the enclosing contract and type below. | str | Module/process lifetime | 45 |
| module | FINISH_ACCEPTANCE_TOOL | Module binding for FINISH ACCEPTANCE TOOL in module; use the enclosing contract and type below. | str | Module/process lifetime | 46 |
| AgentSet | manager | Typed binding for manager in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 53 |
| AgentSet | architect | Typed binding for architect in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 54 |
| AgentSet | coder | Typed binding for coder in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 55 |
| AgentSet | tester | Typed binding for tester in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 56 |
| AgentSet | creation_manager | Typed binding for creation manager in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 57 |
| AgentSet | application_selector | Typed binding for application selector in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 58 |
| _bind_operation | operation | Parameter for operation in _bind_operation; use the enclosing contract and type below. | Callable[..., str] | Enclosing invocation or class/instance lifetime | 61 |
| _bind_operation.wrapper | args | Parameter for args in _bind_operation.wrapper; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 69 |
| _bind_operation.wrapper | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 69 |
| _bind_operation.wrapper | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 73 |
| _bind_operation | wrapper.__signature__ | Attribute for wrapper.  signature in _bind_operation; use the enclosing contract and type below. | Return type of signature; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| register_tools | operations | Parameter for operations in register_tools; use the enclosing contract and type below. | ArtifactTools | Enclosing invocation or class/instance lifetime | 85 |
| register_tools | decorator | Parameter for decorator in register_tools; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 85, 88 |
| register_tools | names | Local binding for names in register_tools; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 89 |
| register_tools | registered | Local binding for registered in register_tools; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 103 |
| register_tools | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| register_tools | display_name | Loop item for display name in register_tools; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| register_tools | bound | Local binding for bound in register_tools; use the enclosing contract and type below. | Return type of _bind_operation; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| register_tools | holder | Typed binding for holder in register_tools; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 109 |
| register_tools.conditional | __bound | Parameter for bound in register_tools.conditional; use the enclosing contract and type below. | Callable[..., str] | Enclosing invocation or class/instance lifetime | 112 |
| register_tools.conditional | args | Parameter for args in register_tools.conditional; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 112 |
| register_tools.conditional | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 112 |
| register_tools.conditional | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of __bound; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| register_tools.conditional | holder['tool'].result_as_answer | Attribute for holder['tool'].result as answer in register_tools.conditional; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 115 |
| register_tools | conditional.__signature__ | Attribute for conditional.  signature in register_tools; use the enclosing contract and type below. | Return type of signature; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| register_tools | registered[name].result_as_answer | Attribute for registered[name].result as answer in register_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 121, 128 |
| register_tools | terminal_review | Local binding for terminal review in register_tools; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| register_tools | terminal_review.result_as_answer | Attribute for terminal review.result as answer in register_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 134 |
| build_agents | local_llm | Parameter for local llm in build_agents; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 140 |
| build_agents | tools | Parameter for tools in build_agents; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 140 |
| build_agents | agent_factory | Parameter for agent factory in build_agents; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 140, 144 |
| build_agents.Agent | options | Parameter for options in build_agents.Agent; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 146 |
| build_agents | manager_options | Local binding for manager options in build_agents; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| build_agents | manager_agent | Local binding for manager agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| build_agents | creation_manager | Local binding for creation manager in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| build_agents | application_selector | Local binding for application selector in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| build_agents | architect_agent | Local binding for architect agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| build_agents | coder_agent | Local binding for coder agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 212 |
| build_agents | tester_agent | Local binding for tester agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
