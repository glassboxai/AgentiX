# Reference for src/agentix/storage/catalog_lock.py

Cross-process catalog mutation lock; never an execution-isolation mechanism.

Source fingerprint: bfa7d76b13e91bb7ef9d76910a01d52ac8e6ffef5dc7f094db30c8c1cc0ada35

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### reject_alias

Reject existing reparse ancestors before catalog mutation or traversal.

Kind: callable. Declared return: None. Source line: 12.

### CatalogLock

Serialize publication, usage acquisition and removal under one managed root.

Kind: class. Declared return: Not declared / class. Source line: 21.

### CatalogLock.__init__

Remember the bounded acquisition deadline; construction performs no IO.

Kind: callable. Declared return: None. Source line: 24.

### CatalogLock.__enter__

Acquire a byte-range lock; report busy rather than waiting indefinitely.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### CatalogLock.__exit__

Close the handle even if the OS reports an unlock error.

Kind: callable. Declared return: None. Source line: 67.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | _THREAD_LOCK | Module binding for THREAD LOCK in module; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Module/process lifetime | 9 |
| reject_alias | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 12 |
| reject_alias | part | Loop item for part in reject_alias; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 14 |
| CatalogLock.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| CatalogLock.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 24 |
| CatalogLock.__init__ | timeout | Parameter for timeout in CatalogLock.__init__; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 24 |
| CatalogLock.__init__ | self.root | Explicit root directory against which named paths are resolved. | tuple | Enclosing invocation or class/instance lifetime | 26 |
| CatalogLock.__init__ | self.timeout | Attribute for timeout in CatalogLock.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 26 |
| CatalogLock.__init__ | self.stream | Attribute for stream in CatalogLock.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 26 |
| CatalogLock.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| CatalogLock.__enter__ | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| CatalogLock.__enter__ | self.stream | Attribute for stream in CatalogLock.__enter__; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| CatalogLock.__enter__ | deadline | Local binding for deadline in CatalogLock.__enter__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| CatalogLock.__enter__ | msvcrt | Imported dependency for msvcrt in CatalogLock.__enter__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| CatalogLock.__enter__ | fcntl | Imported dependency for fcntl in CatalogLock.__enter__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 53 |
| CatalogLock.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| CatalogLock.__exit__ | error | Parameter for error in CatalogLock.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| CatalogLock.__exit__ | msvcrt | Imported dependency for msvcrt in CatalogLock.__exit__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| CatalogLock.__exit__ | fcntl | Imported dependency for fcntl in CatalogLock.__exit__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 78 |
