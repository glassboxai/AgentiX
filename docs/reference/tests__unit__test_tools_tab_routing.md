# Reference for tests/unit/test_tools_tab_routing.py

Tools-tab queries execute approved tools and never an installed application.

Source fingerprint: 7f9e3161e806f4fde0b6f350f8a5f976951ec83b679243ba795143e8690f6abf

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _router

Return only the exact-contract decision; acceptance must never rerun.

Kind: callable. Declared return: SimpleNamespace. Source line: 15.

### _applications

Fail on any application suggestion or execution attempt.

Kind: callable. Declared return: SimpleNamespace. Source line: 30.

### test_vowel_query_reuses_the_installed_tool_without_application_routing

A compatible installed tool answers the query; no application path is reached.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### test_calculator_query_reuses_the_installed_tool_without_application_routing

A compatible calculator tool answers the query; no application path is reached.

Kind: callable. Declared return: Not declared / class. Source line: 70.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | authorize_fixture | Imported dependency for authorize fixture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | VOWEL_CODE | Module binding for VOWEL CODE in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | CALCULATOR_CODE | Module binding for CALCULATOR CODE in module; use the enclosing contract and type below. | str | Module/process lifetime | 9 |
| _router | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 15 |
| _router | arguments | Parameter for arguments in _router; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 15 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | system | Parameter for system in test_vowel_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | system.main.operations | Attribute for system.main.operations in test_vowel_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | system.main.applications | Attribute for system.main.applications in test_vowel_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of _applications; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | system.main.router | Attribute for system.main.router in test_vowel_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of _router; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | system.main.Crew | Attribute for system.main.Crew in test_vowel_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_vowel_query_reuses_the_installed_tool_without_application_routing | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | system | Parameter for system in test_calculator_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | system.main.operations | Attribute for system.main.operations in test_calculator_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | system.main.applications | Attribute for system.main.applications in test_calculator_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of _applications; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | system.main.router | Attribute for system.main.router in test_calculator_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of _router; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | system.main.Crew | Attribute for system.main.Crew in test_calculator_query_reuses_the_installed_tool_without_application_routing; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| test_calculator_query_reuses_the_installed_tool_without_application_routing | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
