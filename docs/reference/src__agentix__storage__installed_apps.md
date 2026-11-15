# Reference for src/agentix/storage/installed_apps.py

Protected installed-app catalog, immutable executable snapshots and separate layout.

Construction performs no reads. Only the maintained supervisor may publish a
human-approved independently verified candidate. UI inputs contain opaque IDs,
never filesystem paths. Descriptions are untrusted display/model data.

Source fingerprint: c49d600cf0868d5318f4ff1c301a4c89abd1b463aa7b1fea567823e8aaa29841

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### InstalledApp

Authenticated catalog metadata; executable bytes are rechecked on every get.

Kind: class. Declared return: Not declared / class. Source line: 53.

### CatalogEntry

One catalog row that keeps a rejected record visible with a bounded reason.

Kind: class. Declared return: Not declared / class. Source line: 66.

### _safe_name

Bound untrusted display text before it reaches a log line or a dropdown.

Kind: callable. Declared return: str. Source line: 76.

### app_policy

Bind the maintained execution boundary and runtime, not catalog services.

Removal, usage leases and presentation geometry are catalog services: they
gate mutation and display but never run inside the child, so their edits must
not invalidate an installed approval.

Kind: callable. Declared return: str. Source line: 83.

### _legacy_digest

Reproduce the pre-V7-076 identity that also hashed scoped stylesheets.

Records sealed before scoped styles left the application identity still carry
that value. Comparing against it proves the installed bytes are unchanged, so a
formula change never reports an untouched application as tampered.

Kind: callable. Declared return: str. Source line: 123.

### _source_digest

Recompute installed bytes, naming maintained-runtime drift apart from tampering.

``application_digest`` rejects both a modified application member and a
maintained runtime member that no longer matches the installed copy. Only the
first is a changed application source; the second is host drift that a
re-approval can resolve, so the bounded reason stays distinguishable. With
``allow_runtime_drift`` the digest is computed over the installed package with
the current runtime members, which never equals the sealed digest.

Kind: callable. Declared return: str. Source line: 140.

### InstalledApps

User-local durable library with authenticated source/dependency bindings.

Kind: class. Declared return: Not declared / class. Source line: 164.

### InstalledApps.__init__

Inject protected storage; do not adopt or inspect old session drafts.

Kind: callable. Declared return: None. Source line: 167.

### InstalledApps.for_user

Compose v4 user storage, independent of v2/v3 and existing tool artifacts.

Kind: callable. Declared return: 'InstalledApps'. Source line: 178.

### InstalledApps._directory

Resolve a safe named folder only through its protected opaque-ID record.

Kind: callable. Declared return: Path. Source line: 183.

### InstalledApps._record_data

Read one bounded authenticated record; unsealed metadata is never trusted.

Kind: callable. Declared return: dict. Source line: 196.

### InstalledApps._write_bytes

Replace one owned file atomically so a crash never leaves a partial grant.

Kind: callable. Declared return: None. Source line: 207.

### InstalledApps._write_record

Seal and atomically replace one protected record; no partial approval survives.

Kind: callable. Declared return: None. Source line: 220.

### InstalledApps._record

Use the existing bounded protected-record naming/containment primitive.

Kind: callable. Declared return: Path. Source line: 227.

### InstalledApps.dependency_references

Check protected references even when a dependent source is currently invalid.

Kind: callable. Declared return: list[str]. Source line: 233.

### InstalledApps.open_lease

Validate and reserve an installed package before starting any native work.

Kind: callable. Declared return: Not declared / class. Source line: 268.

### InstalledApps.in_use

Check shared process receipts; callers hold the catalog mutation lock.

Kind: callable. Declared return: bool. Source line: 277.

### InstalledApps.write_style_member

Rewrite one scoped stylesheet inside an installed package.

Style members are excluded from the application identity, so this keeps the
sealed record and its approval valid while the installed bytes change. The
package is re-verified first, and the member hash in ``application.json`` is
rebound by the maintained writer. Raises ``ValueError`` for an unknown
identity, a changed source, an unsafe declaration or an aliased member.

Kind: callable. Declared return: str. Source line: 284.

### InstalledApps.publish

Serialize publication with removal and bind any already-open preview lease.

Kind: callable. Declared return: InstalledApp. Source line: 315.

### InstalledApps._publish

Copy exact verified bytes; never publish a draft or a child success claim.

Kind: callable. Declared return: InstalledApp. Source line: 328.

### InstalledApps.get

Recheck protected identity, review and exact source before returning metadata.

Kind: callable. Declared return: InstalledApp. Source line: 395.

### InstalledApps.load_stale

Return exact installed bytes for re-approval without granting current policy.

Kind: callable. Declared return: InstalledApp. Source line: 399.

### InstalledApps.load_for_runtime_refresh

Return an installed record whose only drift is the maintained runtime.

The returned package still holds the installed bytes; callers must capture
them with ``capture_with_current_runtime`` and re-run the independent gates.
Changed application source, a changed review or an invalid identity is
refused exactly as ``load_stale`` does.

Kind: callable. Declared return: InstalledApp. Source line: 403.

### InstalledApps._validated

Bind identity, review and source bytes; policy is optional for re-approval.

Kind: callable. Declared return: InstalledApp. Source line: 420.

### InstalledApps.reseal

Rebind one unchanged installed package to the current host policy atomically.

The caller must already have re-run the independent gates on these exact
bytes; this method never re-approves changed source or a changed review.

Kind: callable. Declared return: InstalledApp. Source line: 462.

### InstalledApps._reseal

Replace only the policy binding after exact bytes and review were rechecked.

Kind: callable. Declared return: InstalledApp. Source line: 473.

### InstalledApps._reseal_candidate

Replace one installed record after the reviewed candidate passed current gates.

Kind: callable. Declared return: InstalledApp. Source line: 497.

### InstalledApps.name_available

Report whether the display-name install folder is free for publication.

Kind: callable. Declared return: bool. Source line: 537.

### InstalledApps.entry

Return one catalog row, keeping a rejected record visible with its reason.

Kind: callable. Declared return: CatalogEntry. Source line: 543.

### InstalledApps.entries

List every managed record with its current status; never import app modules.

Kind: callable. Declared return: list[CatalogEntry]. Source line: 564.

### InstalledApps.list

List only currently authorized apps; rejected records stay visible via entries().

Kind: callable. Declared return: list[InstalledApp]. Source line: 597.

### InstalledApps.layout_controls

Return only the reviewed manifest's movable controls, never browser selectors.

Kind: callable. Declared return: set[str] | None. Source line: 601.

### InstalledApps.layout_groups

Return the reviewed tool grouping of movable controls, never browser data.

Kind: callable. Declared return: dict[str, str]. Source line: 611.

### InstalledApps.read_layout

Read bounded presentation data; invalid geometry never becomes executable CSS.

Kind: callable. Declared return: dict. Source line: 619.

### InstalledApps.save_layout

Persist only safe numeric layout, without changing executable approval.

Kind: callable. Declared return: None. Source line: 640.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | CODE_SHARED | Imported dependency for CODE SHARED in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | _identity | Imported dependency for identity in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | application_layout_groups | Imported dependency for application layout groups in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | application_layout_ids | Imported dependency for application layout ids in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | validate_layout | Imported dependency for validate layout in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | WindowsDataProtection | Imported dependency for WindowsDataProtection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 29 |
| module | PURPOSE | Module binding for PURPOSE in module; use the enclosing contract and type below. | str | Module/process lifetime | 31 |
| module | STALE_APPROVAL | Module binding for STALE APPROVAL in module; use the enclosing contract and type below. | str | Module/process lifetime | 40 |
| module | CHANGED_SOURCE | Module binding for CHANGED SOURCE in module; use the enclosing contract and type below. | str | Module/process lifetime | 41 |
| module | CHANGED_RUNTIME | Module binding for CHANGED RUNTIME in module; use the enclosing contract and type below. | str | Module/process lifetime | 42 |
| module | CHANGED_REVIEW | Module binding for CHANGED REVIEW in module; use the enclosing contract and type below. | str | Module/process lifetime | 43 |
| module | STATUS_BY_REASON | Module binding for STATUS BY REASON in module; use the enclosing contract and type below. | dict | Module/process lifetime | 44 |
| InstalledApp | id | Typed binding for id in InstalledApp; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| InstalledApp | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 57 |
| InstalledApp | description | Typed binding for description in InstalledApp; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 58 |
| InstalledApp | package | Typed binding for package in InstalledApp; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 59 |
| InstalledApp | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 60 |
| InstalledApp | dependencies | Typed binding for dependencies in InstalledApp; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 61 |
| InstalledApp | review | Typed binding for review in InstalledApp; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 62 |
| CatalogEntry | id | Typed binding for id in CatalogEntry; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 69 |
| CatalogEntry | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 70 |
| CatalogEntry | status | Typed binding for status in CatalogEntry; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 71 |
| CatalogEntry | reason | Typed binding for reason in CatalogEntry; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 72 |
| CatalogEntry | app | Typed binding for app in CatalogEntry; use the enclosing contract and type below. | InstalledApp &#124; None | Enclosing invocation or class/instance lifetime | 73 |
| _safe_name | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Any | Enclosing invocation or class/instance lifetime | 76 |
| app_policy | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 90 |
| app_policy | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of sha256; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| app_policy | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 92 |
| _legacy_digest | package | Parameter for package in _legacy_digest; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 123 |
| _legacy_digest | capture | Imported dependency for capture in _legacy_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 130 |
| _legacy_digest | files | Local binding for files in _legacy_digest; use the enclosing contract and type below. | Return type of capture; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| _legacy_digest.comprehension_135 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 135 |
| _legacy_digest.comprehension_135 | body | Comprehension item for body in _legacy_digest.comprehension_135; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 135 |
| _source_digest | package | Parameter for package in _source_digest; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 140 |
| _source_digest | allow_runtime_drift | Parameter for allow runtime drift in _source_digest; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 140 |
| _source_digest | RuntimeSourceChanged | Imported dependency for RuntimeSourceChanged in _source_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 150 |
| _source_digest | error | Caught exception for error in _source_digest; use the enclosing contract and type below. | RuntimeSourceChanged | Current exception handler; Python clears this binding afterward | 154, 160 |
| _source_digest | capture_with_current_runtime | Imported dependency for capture with current runtime in _source_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 157 |
| InstalledApps.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| InstalledApps.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 167 |
| InstalledApps.__init__ | records | Parameter for records in InstalledApps.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 167 |
| InstalledApps.__init__ | protector | Parameter for protector in InstalledApps.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 167 |
| InstalledApps.__init__ | self.root | Explicit root directory against which named paths are resolved. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| InstalledApps.__init__ | self.records | Attribute for records in InstalledApps.__init__; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| InstalledApps.for_user | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 178 |
| InstalledApps.for_user | data | Local binding for data in InstalledApps.for_user; use the enclosing contract and type below. | Return type of data_directory; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| InstalledApps._directory | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 183 |
| InstalledApps._directory | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 183 |
| InstalledApps._directory | record | Local binding for record in InstalledApps._directory; use the enclosing contract and type below. | Return type of _record_data; see its callable contract | Enclosing invocation or class/instance lifetime | 185 |
| InstalledApps._directory | folder | Local binding for folder in InstalledApps._directory; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| InstalledApps._directory | directory | Local binding for directory in InstalledApps._directory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 191 |
| InstalledApps._record_data | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 196 |
| InstalledApps._record_data | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 196 |
| InstalledApps._record_data | stream | Managed resource for stream in InstalledApps._record_data; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 198 |
| InstalledApps._record_data | sealed | Local binding for sealed in InstalledApps._record_data; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| InstalledApps._record_data | raw | Local binding for raw in InstalledApps._record_data; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| InstalledApps._write_bytes | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 207 |
| InstalledApps._write_bytes | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 207 |
| InstalledApps._write_bytes | data | Parameter for data in InstalledApps._write_bytes; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 207 |
| InstalledApps._write_bytes | descriptor | Local binding for descriptor in InstalledApps._write_bytes; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| InstalledApps._write_bytes | temporary | Local binding for temporary in InstalledApps._write_bytes; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| InstalledApps._write_bytes | stream | Managed resource for stream in InstalledApps._write_bytes; use the enclosing contract and type below. | Return type of fdopen; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 212 |
| InstalledApps._write_record | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 220 |
| InstalledApps._write_record | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 220 |
| InstalledApps._write_record | record | Parameter for record in InstalledApps._write_record; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 220 |
| InstalledApps._write_record | sealed | Local binding for sealed in InstalledApps._write_record; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 222 |
| InstalledApps._record | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 227 |
| InstalledApps._record | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 227 |
| InstalledApps.dependency_references | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 233 |
| InstalledApps.dependency_references | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 233 |
| InstalledApps.dependency_references | kind | Parameter for kind in InstalledApps.dependency_references; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 233 |
| InstalledApps.dependency_references | namespace | Local binding for namespace in InstalledApps.dependency_references; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 235 |
| InstalledApps.dependency_references | reject_alias | Imported dependency for reject alias in InstalledApps.dependency_references; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 236 |
| InstalledApps.dependency_references | paths | Local binding for paths in InstalledApps.dependency_references; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 241 |
| InstalledApps.dependency_references | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 244 |
| InstalledApps.dependency_references | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 245 |
| InstalledApps.dependency_references | raw | Local binding for raw in InstalledApps.dependency_references; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| InstalledApps.dependency_references | record | Local binding for record in InstalledApps.dependency_references; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 252 |
| InstalledApps.dependency_references | dependency | Loop item for dependency in InstalledApps.dependency_references; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 260 |
| InstalledApps.dependency_references | key | Local binding for key in InstalledApps.dependency_references; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 263 |
| InstalledApps.open_lease | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 268 |
| InstalledApps.open_lease | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 268 |
| InstalledApps.open_lease | CatalogLock | Imported dependency for CatalogLock in InstalledApps.open_lease; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 270 |
| InstalledApps.open_lease | AppLease | Imported dependency for AppLease in InstalledApps.open_lease; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 271 |
| InstalledApps.in_use | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 277 |
| InstalledApps.in_use | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 277 |
| InstalledApps.in_use | app_in_use | Imported dependency for app in use in InstalledApps.in_use; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 279 |
| InstalledApps.write_style_member | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 284 |
| InstalledApps.write_style_member | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 284 |
| InstalledApps.write_style_member | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 284 |
| InstalledApps.write_style_member | css | Parameter for css in InstalledApps.write_style_member; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 284 |
| InstalledApps.write_style_member | write_style_member | Imported dependency for write style member in InstalledApps.write_style_member; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 293 |
| InstalledApps.write_style_member | app | Local binding for app in InstalledApps.write_style_member; use the enclosing contract and type below. | Return type of _validated; see its callable contract | Enclosing invocation or class/instance lifetime | 296, 300 |
| InstalledApps.write_style_member | error | Caught exception for error in InstalledApps.write_style_member; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 297 |
| InstalledApps.write_style_member | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of write_style_member; see its callable contract | Enclosing invocation or class/instance lifetime | 301 |
| InstalledApps.write_style_member | record | Local binding for record in InstalledApps.write_style_member; use the enclosing contract and type below. | Return type of _record_data; see its callable contract | Enclosing invocation or class/instance lifetime | 302 |
| InstalledApps.publish | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 315 |
| InstalledApps.publish | candidate | Parameter for candidate in InstalledApps.publish; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 315 |
| InstalledApps.publish | CatalogLock | Imported dependency for CatalogLock in InstalledApps.publish; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 317 |
| InstalledApps.publish | AppLease | Imported dependency for AppLease in InstalledApps.publish; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 318 |
| InstalledApps.publish | app | Local binding for app in InstalledApps.publish; use the enclosing contract and type below. | Return type of _publish; see its callable contract | Enclosing invocation or class/instance lifetime | 323 |
| InstalledApps.publish | candidate.library_lease | Attribute for candidate.library lease in InstalledApps.publish; use the enclosing contract and type below. | Return type of AppLease; see its callable contract | Enclosing invocation or class/instance lifetime | 325 |
| InstalledApps._publish | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 328 |
| InstalledApps._publish | candidate | Parameter for candidate in InstalledApps._publish; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 328 |
| InstalledApps._publish | snapshot | Local binding for snapshot in InstalledApps._publish; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 332 |
| InstalledApps._publish | existing | Local binding for existing in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 339 |
| InstalledApps._publish | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 342 |
| InstalledApps._publish | application_folder | Imported dependency for application folder in InstalledApps._publish; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 343 |
| InstalledApps._publish | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 345 |
| InstalledApps._publish | folder | Local binding for folder in InstalledApps._publish; use the enclosing contract and type below. | Return type of application_folder; see its callable contract | Enclosing invocation or class/instance lifetime | 346 |
| InstalledApps._publish | directory | Local binding for directory in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 347 |
| InstalledApps._publish | package | Local binding for package in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 348 |
| InstalledApps._publish | filename | Loop item for filename in InstalledApps._publish; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 353 |
| InstalledApps._publish | data | Loop item for data in InstalledApps._publish; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 353 |
| InstalledApps._publish | layout_path | Local binding for layout path in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 355 |
| InstalledApps._publish | layout | Local binding for layout in InstalledApps._publish; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 356, 364 |
| InstalledApps._publish | stream | Managed resource for stream in InstalledApps._publish; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 360 |
| InstalledApps._publish | raw_layout | Local binding for raw layout in InstalledApps._publish; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 361 |
| InstalledApps._publish | review | Local binding for review in InstalledApps._publish; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 371 |
| InstalledApps._publish | review_raw | Local binding for review raw in InstalledApps._publish; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 372 |
| InstalledApps._publish | review_directory | Local binding for review directory in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 375 |
| InstalledApps._publish | description | Local binding for description in InstalledApps._publish; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 378 |
| InstalledApps._publish | record | Local binding for record in InstalledApps._publish; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 379 |
| InstalledApps.get | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 395 |
| InstalledApps.get | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 395 |
| InstalledApps.load_stale | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 399 |
| InstalledApps.load_stale | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 399 |
| InstalledApps.load_for_runtime_refresh | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 403 |
| InstalledApps.load_for_runtime_refresh | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 403 |
| InstalledApps.load_for_runtime_refresh | error | Caught exception for error in InstalledApps.load_for_runtime_refresh; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 413 |
| InstalledApps.load_for_runtime_refresh | app | Local binding for app in InstalledApps.load_for_runtime_refresh; use the enclosing contract and type below. | Return type of _validated; see its callable contract | Enclosing invocation or class/instance lifetime | 416 |
| InstalledApps._validated | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 421 |
| InstalledApps._validated | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 421 |
| InstalledApps._validated | require_policy | Parameter for require policy in InstalledApps._validated; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 421 |
| InstalledApps._validated | allow_runtime_drift | Parameter for allow runtime drift in InstalledApps._validated; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 421 |
| InstalledApps._validated | directory | Local binding for directory in InstalledApps._validated; use the enclosing contract and type below. | Return type of _directory; see its callable contract | Enclosing invocation or class/instance lifetime | 425 |
| InstalledApps._validated | record | Local binding for record in InstalledApps._validated; use the enclosing contract and type below. | Return type of _record_data; see its callable contract | Enclosing invocation or class/instance lifetime | 426 |
| InstalledApps._validated | package | Local binding for package in InstalledApps._validated; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 433 |
| InstalledApps._validated | actual | Local binding for actual in InstalledApps._validated; use the enclosing contract and type below. | Return type of _source_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 434 |
| InstalledApps._validated | review_path | Local binding for review path in InstalledApps._validated; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 440 |
| InstalledApps._validated | stream | Managed resource for stream in InstalledApps._validated; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 443 |
| InstalledApps._validated | review_raw | Local binding for review raw in InstalledApps._validated; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 444 |
| InstalledApps._validated | error | Caught exception for error in InstalledApps._validated; use the enclosing contract and type below. | (OSError, KeyError, TypeError, json.JSONDecodeError) | Current exception handler; Python clears this binding afterward | 459 |
| InstalledApps.reseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 462 |
| InstalledApps.reseal | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 462 |
| InstalledApps.reseal | CatalogLock | Imported dependency for CatalogLock in InstalledApps.reseal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 468 |
| InstalledApps._reseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 473 |
| InstalledApps._reseal | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 473 |
| InstalledApps._reseal | record | Local binding for record in InstalledApps._reseal; use the enclosing contract and type below. | Return type of _record_data; see its callable contract | Enclosing invocation or class/instance lifetime | 475 |
| InstalledApps._reseal | directory | Local binding for directory in InstalledApps._reseal; use the enclosing contract and type below. | Return type of _directory; see its callable contract | Enclosing invocation or class/instance lifetime | 482 |
| InstalledApps._reseal | review_path | Local binding for review path in InstalledApps._reseal; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 485 |
| InstalledApps._reseal | stream | Managed resource for stream in InstalledApps._reseal; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 488 |
| InstalledApps._reseal | review_raw | Local binding for review raw in InstalledApps._reseal; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 489 |
| InstalledApps._reseal_candidate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 497 |
| InstalledApps._reseal_candidate | candidate | Parameter for candidate in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 497 |
| InstalledApps._reseal_candidate | snapshot | Parameter for snapshot in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 497 |
| InstalledApps._reseal_candidate | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 497 |
| InstalledApps._reseal_candidate | record | Local binding for record in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Return type of _record_data; see its callable contract | Enclosing invocation or class/instance lifetime | 499 |
| InstalledApps._reseal_candidate | directory | Local binding for directory in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Return type of _directory; see its callable contract | Enclosing invocation or class/instance lifetime | 506 |
| InstalledApps._reseal_candidate | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 510 |
| InstalledApps._reseal_candidate | body | Loop item for body in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 510 |
| InstalledApps._reseal_candidate | review | Local binding for review in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 521 |
| InstalledApps._reseal_candidate | review_raw | Local binding for review raw in InstalledApps._reseal_candidate; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 522 |
| InstalledApps.name_available | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 537 |
| InstalledApps.name_available | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 537 |
| InstalledApps.name_available | application_folder | Imported dependency for application folder in InstalledApps.name_available; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 539 |
| InstalledApps.entry | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 543 |
| InstalledApps.entry | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 543 |
| InstalledApps.entry | app | Local binding for app in InstalledApps.entry; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 546 |
| InstalledApps.entry | error | Caught exception for error in InstalledApps.entry; use the enclosing contract and type below. | (OSError, ValueError, KeyError, TypeError) | Current exception handler; Python clears this binding afterward | 547 |
| InstalledApps.entry | status | Local binding for status in InstalledApps.entry; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 548 |
| InstalledApps.entry | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 549, 551, 553 |
| InstalledApps.entries | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 564 |
| InstalledApps.entries | namespace | Local binding for namespace in InstalledApps.entries; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 566 |
| InstalledApps.entries | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 569 |
| InstalledApps.entries | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 570 |
| InstalledApps.entries | raw | Local binding for raw in InstalledApps.entries; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 574 |
| InstalledApps.entries | identity | Explicit owner identity used by a session factory or fixture. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 577 |
| InstalledApps.entries | error | Caught exception for error in InstalledApps.entries; use the enclosing contract and type below. | (OSError, ValueError, KeyError, TypeError) | Current exception handler; Python clears this binding afterward | 580 |
| InstalledApps.entries | valid | Local binding for valid in InstalledApps.entries; use the enclosing contract and type below. | Return type of sum; see its callable contract | Enclosing invocation or class/instance lifetime | 588 |
| InstalledApps.entries.comprehension_588 | entry | Comprehension item for entry in InstalledApps.entries.comprehension_588; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 588 |
| InstalledApps.list | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 597 |
| InstalledApps.list.comprehension_599 | entry | Comprehension item for entry in InstalledApps.list.comprehension_599; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 599 |
| InstalledApps.layout_controls | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 602 |
| InstalledApps.layout_controls | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 602 |
| InstalledApps.layout_controls | allow_runtime_drift | Parameter for allow runtime drift in InstalledApps.layout_controls; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 602 |
| InstalledApps.layout_controls | app | Local binding for app in InstalledApps.layout_controls; use the enclosing contract and type below. | Return type of _validated; see its callable contract | Enclosing invocation or class/instance lifetime | 605 |
| InstalledApps.layout_controls | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 608 |
| InstalledApps.layout_groups | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 611 |
| InstalledApps.layout_groups | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 611 |
| InstalledApps.layout_groups | allow_runtime_drift | Parameter for allow runtime drift in InstalledApps.layout_groups; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 611 |
| InstalledApps.layout_groups | app | Local binding for app in InstalledApps.layout_groups; use the enclosing contract and type below. | Return type of _validated; see its callable contract | Enclosing invocation or class/instance lifetime | 613 |
| InstalledApps.layout_groups | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 616 |
| InstalledApps.read_layout | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 619 |
| InstalledApps.read_layout | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 619 |
| InstalledApps.read_layout | allow_runtime_drift | Parameter for allow runtime drift in InstalledApps.read_layout; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 619 |
| InstalledApps.read_layout | app | Local binding for app in InstalledApps.read_layout; use the enclosing contract and type below. | Return type of _validated; see its callable contract | Enclosing invocation or class/instance lifetime | 621 |
| InstalledApps.read_layout | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 625 |
| InstalledApps.read_layout | stream | Managed resource for stream in InstalledApps.read_layout; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 628 |
| InstalledApps.read_layout | raw | Local binding for raw in InstalledApps.read_layout; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 629 |
| InstalledApps.save_layout | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 640 |
| InstalledApps.save_layout | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 640 |
| InstalledApps.save_layout | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 640 |
| InstalledApps.save_layout | app | Local binding for app in InstalledApps.save_layout; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 642 |
| InstalledApps.save_layout | layout | Local binding for layout in InstalledApps.save_layout; use the enclosing contract and type below. | Return type of validate_layout; see its callable contract | Enclosing invocation or class/instance lifetime | 643 |
| InstalledApps.save_layout | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 644 |
