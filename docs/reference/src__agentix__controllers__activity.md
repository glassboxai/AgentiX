# Reference for src/agentix/controllers/activity.py

Shared central activity status for long-running owner-scoped UI operations.

Source fingerprint: 9d64c8c2b5580a7e73b2897abb007293143d796fad52f7ab9ef763972ef5f8fa

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ActivityBackend

Report background work without obscuring a pending human decision.

Kind: class. Declared return: Not declared / class. Source line: 8.

### ActivityBackend.__init__

Inject the owning registry; construction starts no polling or worker.

Kind: callable. Declared return: None. Source line: 11.

### ActivityBackend.activity_status

Return fixed accessible status HTML; never include prompts or exceptions.

Kind: callable. Declared return: str. Source line: 15.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| ActivityBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| ActivityBackend.__init__ | sessions | Parameter for sessions in ActivityBackend.__init__; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 11 |
| ActivityBackend.__init__ | self.sessions | Attribute for sessions in ActivityBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| ActivityBackend.activity_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| ActivityBackend.activity_status | token | Parameter for token in ActivityBackend.activity_status; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 15 |
| ActivityBackend.activity_status | request | Parameter for request in ActivityBackend.activity_status; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 15 |
| ActivityBackend.activity_status | session | Local binding for session in ActivityBackend.activity_status; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| ActivityBackend.activity_status | controller | Local binding for controller in ActivityBackend.activity_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| ActivityBackend.activity_status | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| ActivityBackend.activity_status | application | Local binding for application in ActivityBackend.activity_status; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| ActivityBackend.activity_status | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| ActivityBackend.activity_status | running | Local binding for running in ActivityBackend.activity_status; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| ActivityBackend.activity_status | labels | Local binding for labels in ActivityBackend.activity_status; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 29 |
| ActivityBackend.activity_status | label | Local binding for label in ActivityBackend.activity_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
