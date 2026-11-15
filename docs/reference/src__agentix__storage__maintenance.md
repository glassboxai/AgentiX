# Reference for src/agentix/storage/maintenance.py

Confirmed permanent package removal; no generated source is imported or executed.

Source fingerprint: 00f046d29e98bd2df4c7822f5242d92d290bb09c40d6ba822e77a87b94471ee7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Removal

Server-only exact target/content binding; never serialized as a browser path.

Kind: class. Declared return: Not declared / class. Source line: 16.

### package_digest

Bound and hash one explicit owned tree; reject aliases before reading members.

Kind: callable. Declared return: str. Source line: 26.

### remove_tree

Remove an already checked exact tree, keeping the catalog entry until last.

Repeat alias checks before each unlink. Never follow links or widen to parent
directories. OS errors propagate; authorization is already revoked on failure.

Kind: callable. Declared return: None. Source line: 71.

### CatalogMaintenance

Inject catalogs and strict revocation services; no mutation during construction.

Kind: class. Declared return: Not declared / class. Source line: 87.

### CatalogMaintenance.__init__

Bind trusted roots, never browser-selected directories or executable callbacks.

Kind: callable. Declared return: Not declared / class. Source line: 90.

### CatalogMaintenance._prepare

Check current dependencies/usage and capture the exact package state.

Application removal binds identity, exact installed bytes and the review
digest through ``load_stale`` instead of ``get``: a policy binding that no
longer matches the current host policy blocks execution, not deletion, and
the usage/dependency checks below remain the safety conditions for removal.

Kind: callable. Declared return: Removal. Source line: 95.

### CatalogMaintenance.prepare_tool

Prepare a read-only, exact-content tool deletion confirmation.

Kind: callable. Declared return: Removal. Source line: 130.

### CatalogMaintenance.prepare_app

Prepare only after application usage and dependency checks succeed.

Kind: callable. Declared return: Removal. Source line: 135.

### CatalogMaintenance.confirm

Recheck under the cross-process lock, revoke, then permanently remove.

Kind: callable. Declared return: None. Source line: 140.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | CatalogLock | Imported dependency for CatalogLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 12 |
| Removal | kind | Typed binding for kind in Removal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 19 |
| Removal | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 20 |
| Removal | package | Typed binding for package in Removal; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 21 |
| Removal | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 22 |
| Removal | metadata | Typed binding for metadata in Removal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| package_digest | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 26 |
| package_digest | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of sha256; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| package_digest | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | tuple | Enclosing invocation or class/instance lifetime | 32 |
| package_digest | total | Local binding for total in package_digest; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32, 50 |
| package_digest | count | Local binding for count in package_digest; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 32, 36 |
| package_digest | directory | Loop item for directory in package_digest; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 33 |
| package_digest | member | Loop item for member in package_digest; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 34 |
| package_digest | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of as_posix; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| package_digest | encoded_name | Local binding for encoded name in package_digest; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| package_digest | before | Local binding for before in package_digest; use the enclosing contract and type below. | Return type of stat; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| package_digest | size | Local binding for size in package_digest; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| package_digest | observed | Returned observation checked against the reviewed host-side expectation. | int | Enclosing invocation or class/instance lifetime | 53, 56 |
| package_digest | stream | Managed resource for stream in package_digest; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 54 |
| package_digest | block | Loop item for block in package_digest; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 55 |
| package_digest | after | Local binding for after in package_digest; use the enclosing contract and type below. | Return type of stat; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| remove_tree | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 71 |
| remove_tree | code_last | Parameter for code last in remove_tree; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 71 |
| remove_tree | member | Loop item for member in remove_tree; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 78 |
| remove_tree.lambda_78 | path | Path under validation or an explicitly scoped maintained source path. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 78 |
| CatalogMaintenance.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMaintenance.__init__ | tools | Parameter for tools in CatalogMaintenance.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMaintenance.__init__ | apps | Parameter for apps in CatalogMaintenance.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMaintenance.__init__ | revoke_tool | Parameter for revoke tool in CatalogMaintenance.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMaintenance.__init__ | revoke_widget | Parameter for revoke widget in CatalogMaintenance.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMaintenance.__init__ | self.tools | Attribute for tools in CatalogMaintenance.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 92 |
| CatalogMaintenance.__init__ | self.apps | Attribute for apps in CatalogMaintenance.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 92 |
| CatalogMaintenance.__init__ | self.revoke_tool | Attribute for revoke tool in CatalogMaintenance.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 93 |
| CatalogMaintenance.__init__ | self.revoke_widget | Attribute for revoke widget in CatalogMaintenance.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 93 |
| CatalogMaintenance._prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 95 |
| CatalogMaintenance._prepare | kind | Parameter for kind in CatalogMaintenance._prepare; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 95 |
| CatalogMaintenance._prepare | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 95 |
| CatalogMaintenance._prepare | dependents | Local binding for dependents in CatalogMaintenance._prepare; use the enclosing contract and type below. | Return type of dependency_references; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| CatalogMaintenance._prepare | package | Local binding for package in CatalogMaintenance._prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 114, 124 |
| CatalogMaintenance._prepare | metadata | Local binding for metadata in CatalogMaintenance._prepare; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 117, 125 |
| CatalogMaintenance._prepare | app | Local binding for app in CatalogMaintenance._prepare; use the enclosing contract and type below. | Return type of load_stale; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| CatalogMaintenance.prepare_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| CatalogMaintenance.prepare_tool | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 130 |
| CatalogMaintenance.prepare_app | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 135 |
| CatalogMaintenance.prepare_app | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 135 |
| CatalogMaintenance.confirm | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| CatalogMaintenance.confirm | removal | Parameter for removal in CatalogMaintenance.confirm; use the enclosing contract and type below. | Removal | Enclosing invocation or class/instance lifetime | 140 |
| CatalogMaintenance.confirm | current | Local binding for current in CatalogMaintenance.confirm; use the enclosing contract and type below. | Return type of _prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| CatalogMaintenance.confirm | review | Local binding for review in CatalogMaintenance.confirm; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 157 |
