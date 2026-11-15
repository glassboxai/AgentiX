# Reference for tests/unit/test_agent_workflow_policy.py

Check instructions delivered at agent/task construction, not source-file text.

Source fingerprint: 5c1e946f0e779dacb5f018fe033f34ce4eeade7cc965c40e02834e5c415ffe86

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_agents_receive_application_workflow_obligations

Verify agents receive application workflow obligations.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_roles_do_not_receive_conflicting_creation_responsibilities

Verify roles do not receive conflicting creation responsibilities.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them

Catch prompts that forbid guessed verification but still expose its tool.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 37.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_agents_receive_application_workflow_obligations | system | Parameter for system in test_agents_receive_application_workflow_obligations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_agents_receive_application_workflow_obligations | role | Parameter for role in test_agents_receive_application_workflow_obligations; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_agents_receive_application_workflow_obligations | agent | Local binding for agent in test_agents_receive_application_workflow_obligations; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| test_agents_receive_application_workflow_obligations | delivered | Local binding for delivered in test_agents_receive_application_workflow_obligations; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_agents_receive_application_workflow_obligations | obligation | Loop item for obligation in test_agents_receive_application_workflow_obligations; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 11 |
| test_roles_do_not_receive_conflicting_creation_responsibilities | system | Parameter for system in test_roles_do_not_receive_conflicting_creation_responsibilities; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them | system | Parameter for system in test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them | monkeypatch | Parameter for monkeypatch in test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them | SimpleNamespace | Imported dependency for SimpleNamespace in test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them | assigned | Local binding for assigned in test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 35 |
| test_empty_catalog_manager_has_no_tools_but_execution_manager_keeps_them.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 37 |
