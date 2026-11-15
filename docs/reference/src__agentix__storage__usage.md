# Reference for src/agentix/storage/usage.py

User-local application usage leases, shared by GUI previews and headless calls.

Source fingerprint: 7287e58859f4c19e4357388823031328ba752c99fa912366821648f6eeb87dd9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### process_alive

Preserve leases on access denial or uncertain process identity.

Kind: callable. Declared return: bool. Source line: 11.

### AppLease

Own one process receipt; caller acquires the catalog lock before construction.

Kind: class. Declared return: Not declared / class. Source line: 32.

### AppLease.__init__

Create only the validated installed application's private usage receipt.

Kind: callable. Declared return: None. Source line: 35.

### AppLease.close

Release only this lease; a remaining concurrent lease stays effective.

Kind: callable. Declared return: None. Source line: 44.

### AppLease.__enter__

Retain the lease during one bounded native data operation.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### AppLease.__exit__

Release on native failure as well as successful completion.

Kind: callable. Declared return: None. Source line: 57.

### app_in_use

Conservatively inspect only the known application's owned usage directory.

Kind: callable. Declared return: bool. Source line: 62.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| process_alive | pid | Parameter for pid in process_alive; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 11 |
| process_alive | NativeWindows | Imported dependency for NativeWindows in process_alive; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 16 |
| process_alive | native | Local binding for native in process_alive; use the enclosing contract and type below. | Return type of NativeWindows; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| AppLease.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| AppLease.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 35 |
| AppLease.__init__ | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 35 |
| AppLease.__init__ | self.directory | Attribute for directory in AppLease.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| AppLease.__init__ | self.path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| AppLease.__init__ | stream | Managed resource for stream in AppLease.__init__; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 41 |
| AppLease.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| AppLease.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| AppLease.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| AppLease.__exit__ | error | Parameter for error in AppLease.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| app_in_use | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 62 |
| app_in_use | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 62 |
| app_in_use | probe | Parameter for probe in app_in_use; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 62 |
| app_in_use | directory | Local binding for directory in app_in_use; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| app_in_use | entries | Local binding for entries in app_in_use; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| app_in_use | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 71 |
| app_in_use | record | Local binding for record in app_in_use; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
