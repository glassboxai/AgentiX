# Reference for src/agentix/sandbox/profile_cleanup.py

Ownership-tracked empty AppContainer residue cleanup; never delete file contents.

Source fingerprint: 93e46c1f72f474664b80256648c42646ff40e25690814ed443a6462e85173819

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ProfileCleanup

Track v5 profiles before use and retain failed cleanup for later recovery.

Kind: class. Declared return: Not declared / class. Source line: 14.

### ProfileCleanup.__init__

Inject exact Windows Packages and owned pending-record roots; do no IO.

Kind: callable. Declared return: None. Source line: 17.

### ProfileCleanup.for_user

Use the Windows profile location and separate v5 cleanup metadata.

Kind: callable. Declared return: 'ProfileCleanup'. Source line: 22.

### ProfileCleanup._safe

Reject reparse points in any existing ancestor before traversal or deletion.

Kind: callable. Declared return: None. Source line: 31.

### ProfileCleanup._record

Accept only this release's UUID profile names, never browser paths.

Kind: callable. Declared return: Path. Source line: 40.

### ProfileCleanup.track

Record process ownership before executing any child; fail closed on IO errors.

Kind: callable. Declared return: None. Source line: 48.

### ProfileCleanup.release

After native deletion, remove only empty owned directories, then the receipt.

Nonempty files, linked directories and inaccessible resources are retained.
The caller must already have closed the job and deleted the native profile.

Kind: callable. Declared return: bool. Source line: 55.

### ProfileCleanup.recover

Retry recorded dead-owner profiles only; unknown/live owners are preserved.

Kind: callable. Declared return: None. Source line: 88.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 11 |
| ProfileCleanup.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 17 |
| ProfileCleanup.__init__ | packages | Parameter for packages in ProfileCleanup.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 17 |
| ProfileCleanup.__init__ | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Path | Enclosing invocation or class/instance lifetime | 17 |
| ProfileCleanup.__init__ | self.packages | Attribute for packages in ProfileCleanup.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 19 |
| ProfileCleanup.__init__ | self.pending | Defensive pending-approval snapshot; never a capability to approve another owner. | tuple | Enclosing invocation or class/instance lifetime | 19 |
| ProfileCleanup.for_user | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| ProfileCleanup.for_user | user_home | Imported dependency for user home in ProfileCleanup.for_user; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 24 |
| ProfileCleanup._safe | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 31 |
| ProfileCleanup._safe | part | Loop item for part in ProfileCleanup._safe; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 33 |
| ProfileCleanup._record | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| ProfileCleanup._record | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 40 |
| ProfileCleanup._record | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| ProfileCleanup.track | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| ProfileCleanup.track | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 48 |
| ProfileCleanup.track | record | Local binding for record in ProfileCleanup.track; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| ProfileCleanup.track | stream | Managed resource for stream in ProfileCleanup.track; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 52 |
| ProfileCleanup.release | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ProfileCleanup.release | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 55 |
| ProfileCleanup.release | record | Local binding for record in ProfileCleanup.release; use the enclosing contract and type below. | Return type of _record; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| ProfileCleanup.release | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| ProfileCleanup.release | directories | Local binding for directories in ProfileCleanup.release; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 68 |
| ProfileCleanup.release | current | Loop item for current in ProfileCleanup.release; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 69 |
| ProfileCleanup.release | child | Loop item for child in ProfileCleanup.release; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 70 |
| ProfileCleanup.release | directory | Loop item for directory in ProfileCleanup.release; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 79 |
| ProfileCleanup.recover | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 89 |
| ProfileCleanup.recover | is_alive | Parameter for is alive in ProfileCleanup.recover; use the enclosing contract and type below. | Callable[[int], bool] | Enclosing invocation or class/instance lifetime | 89 |
| ProfileCleanup.recover | delete_profile | Parameter for delete profile in ProfileCleanup.recover; use the enclosing contract and type below. | Callable[[str], bool] | Enclosing invocation or class/instance lifetime | 89 |
| ProfileCleanup.recover | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 95 |
| ProfileCleanup.recover | record | Local binding for record in ProfileCleanup.recover; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| ProfileCleanup.recover | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 101 |
| ProfileCleanup.recover | pid | Local binding for pid in ProfileCleanup.recover; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 101 |
