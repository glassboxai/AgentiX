# Reference for tests/recover_review_server.py

Disposable GUI recovery of a real model draft; never a new inference claim.

Operator supplies one already captured v4 review/package. No approval is copied:
complete source is redisplayed, and the new owner must explicitly review it again.
This test-only composition root uses the production frontend/backend/supervisor.

Source fingerprint: 208e4604be1f207abbb1d959b2c4c7902492cd493a0bc0f9387d294bd3b20330

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Recover one operator-selected draft; preserve bytes and require a fresh review.

Kind: callable. Declared return: None. Source line: 30.

### main.RecoveryPipeline

Load only this exact real-model draft, with no LLM boundary or inherited grant.

Kind: class. Declared return: Not declared / class. Source line: 46.

### main.RecoveryPipeline.__init__

Keep production's injected pipeline interface; use owned disposable storage.

Kind: callable. Declared return: Not declared / class. Source line: 49.

### main.RecoveryPipeline.generate

Copy unchanged bytes into a new review; never label this fresh generation.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### main.controller

Create owner controls without constructing an unused model for this recovery.

Kind: callable. Declared return: Not declared / class. Source line: 74.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| module | gr | Imported dependency for gr in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | FILES | Imported dependency for FILES in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | build_view | Imported dependency for build view in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| main | port | Local binding for port in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32 |
| main | work | Local binding for work in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32 |
| main | package | Local binding for package in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32 |
| main | captured | Local binding for captured in main; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32 |
| main | snapshot | Local binding for snapshot in main; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| main | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 40 |
| main.RecoveryPipeline.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| main.RecoveryPipeline.__init__ | root | Explicit root directory against which named paths are resolved. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| main.RecoveryPipeline.__init__ | self.root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| main.RecoveryPipeline.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| main.RecoveryPipeline.generate | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| main.RecoveryPipeline.generate | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| main.RecoveryPipeline.generate | folder | Local binding for folder in main.RecoveryPipeline.generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| main.RecoveryPipeline.generate | target | Local binding for target in main.RecoveryPipeline.generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| main.RecoveryPipeline.generate | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 61 |
| main.RecoveryPipeline.generate | review | Local binding for review in main.RecoveryPipeline.generate; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| main.controller | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| main.controller | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| main.controller | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in main.controller; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| main.controller.lambda_79 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 79 |
| main | registry | Local binding for registry in main; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| main | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| main | demo | Local binding for demo in main; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
