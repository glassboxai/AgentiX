# Reference for src/agentix/agents/repair_acceptance.py

Bounded data-only acceptance proposals for explicitly repaired tools.

Source fingerprint: 045d975af0525bd00e374855af53d960825a48d41ed73e785bd68019e23c7d57

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### propose_repair_cases

Propose English JSON cases, never edit source/tests or claim observed success.

Kind: callable. Declared return: str. Source line: 14.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | create_profile_llm | Imported dependency for create profile llm in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 8 |
| module | MAX_REPAIR_CONTEXT_BYTES | Module binding for MAX REPAIR CONTEXT BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | MAX_ACCEPTANCE_PROPOSAL_BYTES | Module binding for MAX ACCEPTANCE PROPOSAL BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| propose_repair_cases | context | Parameter for context in propose_repair_cases; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 14 |
| propose_repair_cases | configuration | Parameter for configuration in propose_repair_cases; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| propose_repair_cases | body | Local binding for body in propose_repair_cases; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| propose_repair_cases | client | Local binding for client in propose_repair_cases; use the enclosing contract and type below. | Return type of create_profile_llm; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| propose_repair_cases | system | Local binding for system in propose_repair_cases; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22 |
| propose_repair_cases | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of call; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
