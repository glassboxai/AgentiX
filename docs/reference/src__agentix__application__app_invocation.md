# Reference for src/agentix/application/app_invocation.py

Catalog-only application invocation with exact current tool approvals and native data.

Source fingerprint: 74f75ed11931f379d55d54d6ee48869faabc78bca607862750a019f746408e4e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### check_dependencies

Require the approved installed tool versions used by this exact app snapshot.

A missing tool is reported as ``CatalogDependencyError`` naming the tool and
the maintained skip reason, so the owner sees the recovery step instead of a
generic review message. Reasons never include source, prompts or approval
internals.

Kind: callable. Declared return: dict. Source line: 13.

### rebind_dependencies

Re-derive tool digests for unchanged role and function identities.

Only the approved bytes and contract digest may move; a renamed tool or a
changed function identity still requires a new application review.

Kind: callable. Declared return: dict. Source line: 45.

### AppInvocation

Inject library, owner registry and OS boundary; expose no arbitrary file entrypoint.

Kind: class. Declared return: Not declared / class. Source line: 68.

### AppInvocation.__init__

Construct an inert per-owner invocation service without reading artifacts.

Kind: callable. Declared return: None. Source line: 71.

### AppInvocation.catalog

Return safe metadata for approved compatible apps, never source or keys.

Kind: callable. Declared return: list[dict]. Source line: 81.

### AppInvocation.candidates

Return minimal approved metadata for a suggestion prompt.

Only the current catalog identity, display name and description are
exposed. Input contracts, node IDs, parameter names, arguments, source and
results stay host-side, so a recommendation cannot leak or rebuild them.

Kind: callable. Declared return: list[dict]. Source line: 102.

### AppInvocation._input_contract

Describe only the schema-3 public inputs to the model selector.

Kind: callable. Declared return: dict. Source line: 119.

### AppInvocation.execute

Hold a cross-process usage lease for the entire native data operation.

Kind: callable. Declared return: dict. Source line: 124.

### AppInvocation._execute

Recheck catalog/source/tool grants before and after isolated execution.

Kind: callable. Declared return: dict. Source line: 129.

### AppInvocation.observed_answer

Format only the observed native result; model prose cannot substitute it.

Kind: callable. Declared return: str. Source line: 153.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | validate_result | Imported dependency for validate result in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | execute_application | Imported dependency for execute application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ApprovedToolRegistry | Imported dependency for ApprovedToolRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | CatalogDependencyError | Imported dependency for CatalogDependencyError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | InstalledApp | Imported dependency for InstalledApp in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| check_dependencies | app | Parameter for app in check_dependencies; use the enclosing contract and type below. | InstalledApp | Enclosing invocation or class/instance lifetime | 13 |
| check_dependencies | registry | Parameter for registry in check_dependencies; use the enclosing contract and type below. | ApprovedToolRegistry | Enclosing invocation or class/instance lifetime | 13 |
| check_dependencies | tools | Local binding for tools in check_dependencies; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| check_dependencies | missing | Local binding for missing in check_dependencies; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 22 |
| check_dependencies.comprehension_22 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 22 |
| check_dependencies | reason_of | Local binding for reason of in check_dependencies; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| check_dependencies | detail | Local binding for detail in check_dependencies; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| check_dependencies.comprehension_25 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 26 |
| check_dependencies | role | Loop item for role in check_dependencies; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 32 |
| check_dependencies | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 32 |
| check_dependencies | tool | Local binding for tool in check_dependencies; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 33 |
| check_dependencies.comprehension_42 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| rebind_dependencies | app | Parameter for app in rebind_dependencies; use the enclosing contract and type below. | InstalledApp | Enclosing invocation or class/instance lifetime | 45 |
| rebind_dependencies | registry | Parameter for registry in rebind_dependencies; use the enclosing contract and type below. | ApprovedToolRegistry | Enclosing invocation or class/instance lifetime | 45 |
| rebind_dependencies | tools | Local binding for tools in rebind_dependencies; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| rebind_dependencies | rebound | Local binding for rebound in rebind_dependencies; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 52 |
| rebind_dependencies | role | Loop item for role in rebind_dependencies; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 53 |
| rebind_dependencies | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 53 |
| rebind_dependencies | tool | Local binding for tool in rebind_dependencies; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| AppInvocation.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| AppInvocation.__init__ | library | Parameter for library in AppInvocation.__init__; use the enclosing contract and type below. | InstalledApps | Enclosing invocation or class/instance lifetime | 73 |
| AppInvocation.__init__ | registry | Parameter for registry in AppInvocation.__init__; use the enclosing contract and type below. | ApprovedToolRegistry | Enclosing invocation or class/instance lifetime | 74 |
| AppInvocation.__init__ | native | Parameter for native in AppInvocation.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 76 |
| AppInvocation.__init__ | self.library | Attribute for library in AppInvocation.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 79 |
| AppInvocation.__init__ | self.registry | Attribute for registry in AppInvocation.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 79 |
| AppInvocation.__init__ | self.native | Attribute for native in AppInvocation.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 79 |
| AppInvocation.catalog | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| AppInvocation.catalog | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 83 |
| AppInvocation.catalog | app | Loop item for app in AppInvocation.catalog; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 84 |
| AppInvocation.candidates | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 102 |
| AppInvocation.candidates | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 109 |
| AppInvocation.candidates | app | Loop item for app in AppInvocation.candidates; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 110 |
| AppInvocation._input_contract | app | Parameter for app in AppInvocation._input_contract; use the enclosing contract and type below. | InstalledApp | Enclosing invocation or class/instance lifetime | 119 |
| AppInvocation._input_contract | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| AppInvocation.execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| AppInvocation.execute | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 124 |
| AppInvocation.execute | arguments | Parameter for arguments in AppInvocation.execute; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 124 |
| AppInvocation._execute | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| AppInvocation._execute | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 129 |
| AppInvocation._execute | arguments | Parameter for arguments in AppInvocation._execute; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 129, 136 |
| AppInvocation._execute | app | Local binding for app in AppInvocation._execute; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 131 |
| AppInvocation._execute | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| AppInvocation._execute | validate_payload | Imported dependency for validate payload in AppInvocation._execute; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 134 |
| AppInvocation._execute | snapshot | Local binding for snapshot in AppInvocation._execute; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| AppInvocation._execute | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of validate_result; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| AppInvocation._execute | current | Local binding for current in AppInvocation._execute; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| AppInvocation.observed_answer | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 153 |
| AppInvocation.observed_answer | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 153 |
| AppInvocation.observed_answer | arguments | Parameter for arguments in AppInvocation.observed_answer; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 153 |
| AppInvocation.observed_answer | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
