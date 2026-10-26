# Reference for src/agentix/adapters/crewai.py

Explicit CrewAI tool registration and agent construction.

Factories import optional dependencies only when called. The manager can request
session-owned reuse preparation or first-use isolated verification; prompts are not the
security boundary, which remains in the application services.

Source fingerprint: 74da0dc5e2ffe1fc2382669340d090010d1c864f638c2744199d129ae1473aac

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### AgentSet

Session-owned workflow roles plus a tool-free creation-decision manager.

Kind: class. Declared return: Not declared / class. Source line: 30.

### _bind_operation

Expose a bound service method as a function with its public signature.

CrewAI introspects function metadata to create Pydantic schemas. Preserve
annotations/docstrings and omit the already-bound self parameter explicitly.

Kind: callable. Declared return: Callable[..., str]. Source line: 40.

### _bind_operation.wrapper

Forward arguments to the owning service without changing its result.

Kind: callable. Declared return: str. Source line: 48.

### register_tools

Register bound operation signatures under their existing public tool names.

Kind: callable. Declared return: SimpleNamespace. Source line: 64.

### build_agents

Construct verbose role instructions without executing any agent tasks.

Kind: callable. Declared return: AgentSet. Source line: 104.

### build_agents.Agent

Apply finite role budgets while preserving existing verbose behavior.

Kind: callable. Declared return: Any. Source line: 111.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | WORKFLOW_POLICY | Imported dependency for WORKFLOW POLICY in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | SECURITY_GUARDRAILS | Module binding for SECURITY GUARDRAILS in module; use the enclosing contract and type below. | str | Module/process lifetime | 19 |
| AgentSet | manager | Typed binding for manager in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| AgentSet | architect | Typed binding for architect in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| AgentSet | coder | Typed binding for coder in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 35 |
| AgentSet | tester | Typed binding for tester in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 36 |
| AgentSet | creation_manager | Typed binding for creation manager in AgentSet; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 37 |
| _bind_operation | operation | Parameter for operation in _bind_operation; use the enclosing contract and type below. | Callable[..., str] | Enclosing invocation or class/instance lifetime | 40 |
| _bind_operation.wrapper | args | Parameter for args in _bind_operation.wrapper; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 48 |
| _bind_operation.wrapper | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 48 |
| _bind_operation.wrapper | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| _bind_operation | wrapper.__signature__ | Attribute for wrapper.  signature in _bind_operation; use the enclosing contract and type below. | Return type of signature; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| register_tools | operations | Parameter for operations in register_tools; use the enclosing contract and type below. | ArtifactTools | Enclosing invocation or class/instance lifetime | 64 |
| register_tools | decorator | Parameter for decorator in register_tools; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 64, 67 |
| register_tools | names | Local binding for names in register_tools; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 68 |
| register_tools | registered | Local binding for registered in register_tools; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 82 |
| register_tools | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 83 |
| register_tools | display_name | Loop item for display name in register_tools; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 83 |
| register_tools | registered[name].result_as_answer | Attribute for registered[name].result as answer in register_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 93 |
| register_tools | terminal_review | Local binding for terminal review in register_tools; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| register_tools | terminal_review.result_as_answer | Attribute for terminal review.result as answer in register_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 99 |
| build_agents | local_llm | Parameter for local llm in build_agents; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 105 |
| build_agents | tools | Parameter for tools in build_agents; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 105 |
| build_agents | agent_factory | Parameter for agent factory in build_agents; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 105, 109 |
| build_agents.Agent | options | Parameter for options in build_agents.Agent; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 111 |
| build_agents | manager_options | Local binding for manager options in build_agents; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| build_agents | manager_agent | Local binding for manager agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| build_agents | creation_manager | Local binding for creation manager in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| build_agents | architect_agent | Local binding for architect agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| build_agents | coder_agent | Local binding for coder agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| build_agents | tester_agent | Local binding for tester agent in build_agents; use the enclosing contract and type below. | Return type of Agent; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
