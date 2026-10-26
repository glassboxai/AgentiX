# Reference for src/agentix/profile_store.py

User-owned nonsecret model profiles with Windows credential references.

Writes use an interprocess lock and atomic metadata replacement. Credential and
file services are not a transactional database: cleanup references are retained
for retry, while a failed metadata commit keeps the old profile authoritative.
Same-user malware is outside the Windows credential/user filesystem boundary.

Source fingerprint: 21f3361cf68c5fb3595e03361b45e5365e63561e0fc17a976fd3d0378099c67c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SavedProfiles

Persist a bounded catalog; keys live exclusively in an injected vault.

Kind: class. Declared return: Not declared / class. Source line: 29.

### SavedProfiles.__init__

Retain user-local location and external boundaries without creating files.

Kind: callable. Declared return: None. Source line: 32.

### SavedProfiles._path

Reject path input and reparse ancestors before accessing owned metadata.

Kind: callable. Declared return: Path. Source line: 39.

### SavedProfiles._check_path

Deny existing reparse components; never follow metadata links.

Kind: callable. Declared return: None. Source line: 48.

### SavedProfiles.get

Read validated bounded metadata; never read a credential value.

Kind: callable. Declared return: dict[str, Any]. Source line: 58.

### SavedProfiles._validate_name

Limit display names to readable nonmarkup characters.

Kind: callable. Declared return: None. Source line: 114.

### SavedProfiles.list

List bounded validated metadata; corruption is reported rather than hidden.

Kind: callable. Declared return: list[dict[str, Any]]. Source line: 123.

### SavedProfiles._exclusive

Serialize writes across processes; fail after five seconds of contention.

Kind: callable. Declared return: Iterator[None]. Source line: 137.

### SavedProfiles._commit

Replace one metadata file atomically; never include API key values.

Kind: callable. Declared return: None. Source line: 173.

### SavedProfiles.save

Create/update metadata and credentials, rejecting stale edits before IO.

Empty keys retain an existing credential. New keys get new opaque targets;
a failed commit removes the candidate and leaves the original untouched.
Cleanup failures retain old references for retry on update or deletion.

Kind: callable. Declared return: dict[str, Any]. Source line: 188.

### SavedProfiles.delete

Remove exactly the selected profile and its owned credential targets.

A partial vault failure leaves metadata for an explicit retry. Existing
active SDK clients can retain their already loaded credential in memory.

Kind: callable. Declared return: None. Source line: 291.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | contextmanager | Imported dependency for contextmanager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ModelProfile | Imported dependency for ModelProfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | resolve_addresses | Imported dependency for resolve addresses in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | ProfileError | Imported dependency for ProfileError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 26 |
| SavedProfiles.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| SavedProfiles.__init__ | directory | Parameter for directory in SavedProfiles.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 33 |
| SavedProfiles.__init__ | vault | Parameter for vault in SavedProfiles.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| SavedProfiles.__init__ | resolver | Parameter for resolver in SavedProfiles.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 33 |
| SavedProfiles.__init__ | self.directory | Attribute for directory in SavedProfiles.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| SavedProfiles.__init__ | self.vault | Attribute for vault in SavedProfiles.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| SavedProfiles.__init__ | self.resolver | Attribute for resolver in SavedProfiles.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 36 |
| SavedProfiles.__init__ | self._lock | Attribute for lock in SavedProfiles.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| SavedProfiles._path | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| SavedProfiles._path | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 39 |
| SavedProfiles._path | target | Local binding for target in SavedProfiles._path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| SavedProfiles._check_path | target | Parameter for target in SavedProfiles._check_path; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 48 |
| SavedProfiles._check_path | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 50 |
| SavedProfiles._check_path | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of lstat; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| SavedProfiles.get | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| SavedProfiles.get | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 58 |
| SavedProfiles.get | stream | Managed resource for stream in SavedProfiles.get; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 61 |
| SavedProfiles.get | raw | Local binding for raw in SavedProfiles.get; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| SavedProfiles.get | record | Local binding for record in SavedProfiles.get; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| SavedProfiles.get | fields | Local binding for fields in SavedProfiles.get; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 66 |
| SavedProfiles.get.lambda_90 | host | Callback parameter for host in SavedProfiles.get.lambda_90; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 90 |
| SavedProfiles.get | reference | Local binding for reference in SavedProfiles.get; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 91 |
| SavedProfiles.get | references | Local binding for references in SavedProfiles.get; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| SavedProfiles.get.comprehension_102 | ref | Comprehension item for ref in SavedProfiles.get.comprehension_102; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 105 |
| SavedProfiles._validate_name | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 114 |
| SavedProfiles._validate_name.comprehension_119 | character | Comprehension item for character in SavedProfiles._validate_name.comprehension_119; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 119 |
| SavedProfiles.list | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 123 |
| SavedProfiles.list | paths | Local binding for paths in SavedProfiles.list; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 126 |
| SavedProfiles.list | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 127 |
| SavedProfiles.list.comprehension_132 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 132 |
| SavedProfiles.list.lambda_133 | item | Callback parameter for item in SavedProfiles.list.lambda_133; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 133 |
| SavedProfiles._exclusive | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 137 |
| SavedProfiles._exclusive | stream | Managed resource for stream in SavedProfiles._exclusive; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 142 |
| SavedProfiles._exclusive | deadline | Local binding for deadline in SavedProfiles._exclusive; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 147 |
| SavedProfiles._exclusive | msvcrt | Imported dependency for msvcrt in SavedProfiles._exclusive; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 152 |
| SavedProfiles._exclusive | fcntl | Imported dependency for fcntl in SavedProfiles._exclusive; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 156 |
| SavedProfiles._commit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 173 |
| SavedProfiles._commit | record | Parameter for record in SavedProfiles._commit; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 173 |
| SavedProfiles._commit | target | Local binding for target in SavedProfiles._commit; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| SavedProfiles._commit | descriptor | Local binding for descriptor in SavedProfiles._commit; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| SavedProfiles._commit | temporary | Local binding for temporary in SavedProfiles._commit; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| SavedProfiles._commit | stream | Managed resource for stream in SavedProfiles._commit; use the enclosing contract and type below. | Return type of fdopen; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 180 |
| SavedProfiles.save | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 189 |
| SavedProfiles.save | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 190, 205 |
| SavedProfiles.save | provider | Parameter for provider in SavedProfiles.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 191 |
| SavedProfiles.save | model | Parameter for model in SavedProfiles.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 192 |
| SavedProfiles.save | endpoint | Parameter for endpoint in SavedProfiles.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 193 |
| SavedProfiles.save | key | Parameter for key in SavedProfiles.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 194 |
| SavedProfiles.save | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 195, 219 |
| SavedProfiles.save | version | Parameter for version in SavedProfiles.save; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 196 |
| SavedProfiles.save | remote | Local binding for remote in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 206 |
| SavedProfiles.save | old | Local binding for old in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 212 |
| SavedProfiles.save | write_key | Local binding for write key in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 220 |
| SavedProfiles.save | reference | Local binding for reference in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 221 |
| SavedProfiles.save | retired | Local binding for retired in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 226 |
| SavedProfiles.save | record | Local binding for record in SavedProfiles.save; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| SavedProfiles.save | phase | Local binding for phase in SavedProfiles.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 241, 245 |
| SavedProfiles.save | error | Caught exception for error in SavedProfiles.save; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 247, 272, 281 |
| SavedProfiles.save | cleanup_error | Caught exception for cleanup error in SavedProfiles.save; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 258 |
| SavedProfiles.save | remaining | Local binding for remaining in SavedProfiles.save; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 268 |
| SavedProfiles.save | obsolete | Loop item for obsolete in SavedProfiles.save; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 269 |
| SavedProfiles.delete | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 291 |
| SavedProfiles.delete | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 291 |
| SavedProfiles.delete | version | Parameter for version in SavedProfiles.delete; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 291 |
| SavedProfiles.delete | record | Local binding for record in SavedProfiles.delete; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| SavedProfiles.delete | reference | Loop item for reference in SavedProfiles.delete; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 302 |
