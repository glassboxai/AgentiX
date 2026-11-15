# Reference for src/agentix/agents/workflow_policy.py

Maintained system-level workflow obligations shared by application roles.

CrewAI incorporates the backstory into each agent's system instructions. Domain
requests remain task data; these duties do not need repeating in the user query.
Prompts guide cooperation; host artifact, approval and execution gates enforce it.

Source fingerprint: 277b3f4e58ced72586b4e2946668a61dc0875de4a3351ce0e60c90dce2dbec37

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | WORKFLOW_POLICY | Module binding for WORKFLOW POLICY in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| module | APPLICATION_SUGGESTION_POLICY | Module binding for APPLICATION SUGGESTION POLICY in module; use the enclosing contract and type below. | str | Module/process lifetime | 42 |
