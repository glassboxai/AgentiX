# Reference for src/agentix/workflow_policy.py

Maintained system-level workflow obligations shared by application roles.

CrewAI incorporates the backstory into each agent's system instructions. Domain
requests remain task data; these duties do not need repeating in the user query.
Prompts guide cooperation; host artifact, approval and execution gates enforce it.

Source fingerprint: de5f368b426abd90161b6b81e1aa9db6c0874d44d82a7f5928671ff88ff4cb19

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | WORKFLOW_POLICY | Module binding for WORKFLOW POLICY in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
