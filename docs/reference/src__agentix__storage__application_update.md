# Reference for src/agentix/storage/application_update.py

V7-048: stage exact authenticated applications for reviewed runtime updates.

Only the schema-3 maintained app.py may change executable bytes. Generated logic,
widgets, dependency code/tests, independent cases and geometry remain unchanged.
Current native/browser gates precede any installed write. No model is constructed.

Source fingerprint: 618502e2451b6dc02bcf0816cd0f05cc28a5f9bfe38c3254aceadd3bea958dcd

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Update

Immutable-by-contract staged bytes and original proof for one review lifetime.

Kind: class. Declared return: Not declared / class. Source line: 32.

### ApplicationUpdates

Compose the catalog's authenticated snapshot reader with package staging.

A single operator owns this instance. CatalogMigration owns bounded input
capture/freshness and current tool-grant validation; this service owns only
application transformations and installation. Source remains read-only.

Kind: class. Declared return: Not declared / class. Source line: 46.

### ApplicationUpdates.__init__

Inject an explicit migration snapshot; construction performs no writes.

Kind: callable. Declared return: None. Source line: 54.

### ApplicationUpdates._prepare

Authenticate old bytes and prepare the only permitted runtime/metadata edits.

Kind: callable. Declared return: Update | None. Source line: 60.

### ApplicationUpdates._dependencies

Refresh case bindings only when current approved dependency bytes match exactly.

Kind: callable. Declared return: dict. Source line: 196.

### ApplicationUpdates._stage

Write closed server-selected filename bytes to a fresh owned staging directory.

Kind: callable. Declared return: None. Source line: 218.

### ApplicationUpdates.plan

Return exact candidate identities without changing installed bytes or grants.

Kind: callable. Declared return: dict. Source line: 223.

### ApplicationUpdates.apply

Verify staged candidates, then install selective edits with backups and rollback.

A current destination grant is never overwritten. Installed files may be
updated only by this explicitly reviewed operation. Failure before commit
changes no live bytes; ordinary commit errors restore backed-up bytes.
Crash-atomic multi-file replacement is outside this operation's contract.

Kind: callable. Declared return: dict. Source line: 270.

### ApplicationUpdates._commit

Install changed maintained bytes/review and create the protected grant last.

Kind: callable. Declared return: None. Source line: 345.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | copy | Imported dependency for copy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | validate_manifest | Imported dependency for validate manifest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | _identity | Imported dependency for identity in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | application_layout_ids | Imported dependency for application layout ids in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | validate_layout | Imported dependency for validate layout in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | CatalogLock | Imported dependency for CatalogLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | CatalogMigration | Imported dependency for CatalogMigration in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | fingerprint | Imported dependency for fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | PURPOSE | Imported dependency for PURPOSE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | app_policy | Imported dependency for app policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | app_in_use | Imported dependency for app in use in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 28 |
| Update | item | Typed binding for item in Update; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 35 |
| Update | record | Typed binding for record in Update; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 36 |
| Update | source_record | Typed binding for source record in Update; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 37 |
| Update | original | Typed binding for original in Update; use the enclosing contract and type below. | dict[str, bytes] | Enclosing invocation or class/instance lifetime | 38 |
| Update | updated | Typed binding for updated in Update; use the enclosing contract and type below. | dict[str, bytes] | Enclosing invocation or class/instance lifetime | 39 |
| Update | review_path | Typed binding for review path in Update; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 40 |
| Update | old_review | Typed binding for old review in Update; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 41 |
| Update | new_review | Typed binding for new review in Update; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 42 |
| Update | approval_path | Typed binding for approval path in Update; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 43 |
| ApplicationUpdates.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| ApplicationUpdates.__init__ | migration | Parameter for migration in ApplicationUpdates.__init__; use the enclosing contract and type below. | CatalogMigration | Enclosing invocation or class/instance lifetime | 54 |
| ApplicationUpdates.__init__ | self.migration | Attribute for migration in ApplicationUpdates.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| ApplicationUpdates.__init__ | self.prepared | Attribute for prepared in ApplicationUpdates.__init__; use the enclosing contract and type below. | list[Update] | Enclosing invocation or class/instance lifetime | 57 |
| ApplicationUpdates.__init__ | self.widget_approvals | Attribute for widget approvals in ApplicationUpdates.__init__; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 58 |
| ApplicationUpdates._prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| ApplicationUpdates._prepare | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 60 |
| ApplicationUpdates._prepare | item | Parameter for item in ApplicationUpdates._prepare; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 60 |
| ApplicationUpdates._prepare | m | Local binding for m in ApplicationUpdates._prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62 |
| ApplicationUpdates._prepare | record | Local binding for record in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| ApplicationUpdates._prepare | source_record | Local binding for source record in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| ApplicationUpdates._prepare | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 64 |
| ApplicationUpdates._prepare | folder | Local binding for folder in ApplicationUpdates._prepare; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 64 |
| ApplicationUpdates._prepare | approval | Local binding for approval in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| ApplicationUpdates._prepare | existing | Local binding for existing in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| ApplicationUpdates._prepare | library | Local binding for library in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of InstalledApps; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| ApplicationUpdates._prepare | current | Local binding for current in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| ApplicationUpdates._prepare | review_path | Local binding for review path in ApplicationUpdates._prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationUpdates._prepare | old_review | Local binding for old review in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| ApplicationUpdates._prepare | review | Local binding for review in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| ApplicationUpdates._prepare | package | Local binding for package in ApplicationUpdates._prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| ApplicationUpdates._prepare | manifest_raw | Local binding for manifest raw in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| ApplicationUpdates._prepare | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 100, 135 |
| ApplicationUpdates._prepare | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| ApplicationUpdates._prepare.comprehension_102 | p | Comprehension item for p in ApplicationUpdates._prepare.comprehension_102; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 102 |
| ApplicationUpdates._prepare | original | Local binding for original in ApplicationUpdates._prepare; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 104 |
| ApplicationUpdates._prepare.comprehension_104 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 104 |
| ApplicationUpdates._prepare | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 109, 117, 156 |
| ApplicationUpdates._prepare | expected_hash | Loop item for expected hash in ApplicationUpdates._prepare; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 109 |
| ApplicationUpdates._prepare | layout | Local binding for layout in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationUpdates._prepare | dependencies | Local binding for dependencies in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of _dependencies; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationUpdates._prepare | tool | Local binding for tool in ApplicationUpdates._prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 118 |
| ApplicationUpdates._prepare | updated | Local binding for updated in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| ApplicationUpdates._prepare | changed | Local binding for changed in ApplicationUpdates._prepare; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 128 |
| ApplicationUpdates._prepare | runtime_template | Imported dependency for runtime template in ApplicationUpdates._prepare; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 130 |
| ApplicationUpdates._prepare | current_template | Local binding for current template in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| ApplicationUpdates._prepare | temporary | Managed resource for temporary in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 141 |
| ApplicationUpdates._prepare | staged | Local binding for staged in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| ApplicationUpdates._prepare | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| ApplicationUpdates._prepare | new_review | Local binding for new review in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of deepcopy; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| ApplicationUpdates._prepare.comprehension_147 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 149 |
| ApplicationUpdates._prepare.comprehension_147 | body | Comprehension item for body in ApplicationUpdates._prepare.comprehension_147; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 149 |
| ApplicationUpdates._prepare.comprehension_153 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 154 |
| ApplicationUpdates._prepare | matches | Local binding for matches in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of all; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| ApplicationUpdates._prepare.comprehension_157 | suffix | Comprehension item for suffix in ApplicationUpdates._prepare.comprehension_157; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 159 |
| ApplicationUpdates._prepare | new_raw | Local binding for new raw in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| ApplicationUpdates._prepare | new_record | Local binding for new record in ApplicationUpdates._prepare; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| ApplicationUpdates._dependencies | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 196 |
| ApplicationUpdates._dependencies | previous | Parameter for previous in ApplicationUpdates._dependencies; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 196 |
| ApplicationUpdates._dependencies | m | Local binding for m in ApplicationUpdates._dependencies; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 198 |
| ApplicationUpdates._dependencies | current | Local binding for current in ApplicationUpdates._dependencies; use the enclosing contract and type below. | Return type of deepcopy; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| ApplicationUpdates._dependencies | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 200 |
| ApplicationUpdates._dependencies | dependency | Loop item for dependency in ApplicationUpdates._dependencies; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 200 |
| ApplicationUpdates._dependencies | tool | Local binding for tool in ApplicationUpdates._dependencies; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 201 |
| ApplicationUpdates._dependencies.comprehension_202 | key | Comprehension item for key in ApplicationUpdates._dependencies.comprehension_202; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 204 |
| ApplicationUpdates._dependencies.comprehension_202 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 204 |
| ApplicationUpdates._dependencies | grant | Local binding for grant in ApplicationUpdates._dependencies; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 212 |
| ApplicationUpdates._stage | folder | Parameter for folder in ApplicationUpdates._stage; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 218 |
| ApplicationUpdates._stage | files | Parameter for files in ApplicationUpdates._stage; use the enclosing contract and type below. | dict[str, bytes] | Enclosing invocation or class/instance lifetime | 218 |
| ApplicationUpdates._stage | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 220 |
| ApplicationUpdates._stage | body | Loop item for body in ApplicationUpdates._stage; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 220 |
| ApplicationUpdates.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationUpdates.plan | names | Parameter for names in ApplicationUpdates.plan; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationUpdates.plan | m | Local binding for m in ApplicationUpdates.plan; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 227 |
| ApplicationUpdates.plan | catalog_plan | Local binding for catalog plan in ApplicationUpdates.plan; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| ApplicationUpdates.plan | self.widget_approvals | Attribute for widget approvals in ApplicationUpdates.plan; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 229 |
| ApplicationUpdates.plan.comprehension_229 | item | Comprehension item for item in ApplicationUpdates.plan.comprehension_229; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 231 |
| ApplicationUpdates.plan | self.prepared | Attribute for prepared in ApplicationUpdates.plan; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 234 |
| ApplicationUpdates.plan | items | Local binding for items in ApplicationUpdates.plan; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 235 |
| ApplicationUpdates.plan | found | Local binding for found in ApplicationUpdates.plan; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 236 |
| ApplicationUpdates.plan | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 237 |
| ApplicationUpdates.plan | record | Local binding for record in ApplicationUpdates.plan; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| ApplicationUpdates.plan | _ | Local binding for  in ApplicationUpdates.plan; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 238 |
| ApplicationUpdates.plan | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 239, 253 |
| ApplicationUpdates.plan | item | Local binding for item in ApplicationUpdates.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 245 |
| ApplicationUpdates.plan | update | Local binding for update in ApplicationUpdates.plan; use the enclosing contract and type below. | Return type of _prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| ApplicationUpdates.plan | error | Caught exception for error in ApplicationUpdates.plan; use the enclosing contract and type below. | (OSError, ValueError, KeyError, TypeError, SyntaxError) | Current exception handler; Python clears this binding afterward | 250 |
| ApplicationUpdates.plan | binding | Local binding for binding in ApplicationUpdates.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 257 |
| ApplicationUpdates.plan.comprehension_259 | p | Comprehension item for p in ApplicationUpdates.plan.comprehension_259; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 261 |
| ApplicationUpdates.plan.comprehension_259 | b | Comprehension item for b in ApplicationUpdates.plan.comprehension_259; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 261 |
| ApplicationUpdates.apply | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 271 |
| ApplicationUpdates.apply | names | Parameter for names in ApplicationUpdates.apply; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 272 |
| ApplicationUpdates.apply | reviewed_digest | Parameter for reviewed digest in ApplicationUpdates.apply; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 273 |
| ApplicationUpdates.apply | verifier | Parameter for verifier in ApplicationUpdates.apply; use the enclosing contract and type below. | Callable[[Path, dict, Path], bool] | Enclosing invocation or class/instance lifetime | 275 |
| ApplicationUpdates.apply | m | Local binding for m in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 284 |
| ApplicationUpdates.apply | plan | Local binding for plan in ApplicationUpdates.apply; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 286 |
| ApplicationUpdates.apply | operation | Local binding for operation in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 289 |
| ApplicationUpdates.apply | update | Loop item for update in ApplicationUpdates.apply; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 292 |
| ApplicationUpdates.apply | started | Local binding for started in ApplicationUpdates.apply; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 293 |
| ApplicationUpdates.apply | item | Local binding for item in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 294 |
| ApplicationUpdates.apply | package | Local binding for package in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 295 |
| ApplicationUpdates.apply | evidence | Local binding for evidence in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 296 |
| ApplicationUpdates.apply | staged | Local binding for staged in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 298 |
| ApplicationUpdates.apply | review | Local binding for review in ApplicationUpdates.apply; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 305 |
| ApplicationUpdates.apply.comprehension_312 | p | Comprehension item for p in ApplicationUpdates.apply.comprehension_312; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 312 |
| ApplicationUpdates.apply | backup | Local binding for backup in ApplicationUpdates.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 316 |
| ApplicationUpdates.apply | error | Caught exception for error in ApplicationUpdates.apply; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 326 |
| ApplicationUpdates._commit | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 345 |
| ApplicationUpdates._commit | update | Parameter for update in ApplicationUpdates._commit; use the enclosing contract and type below. | Update | Enclosing invocation or class/instance lifetime | 345 |
| ApplicationUpdates._commit | package | Parameter for package in ApplicationUpdates._commit; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 345 |
| ApplicationUpdates._commit | m | Local binding for m in ApplicationUpdates._commit; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 347 |
| ApplicationUpdates._commit | changes | Local binding for changes in ApplicationUpdates._commit; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 348 |
| ApplicationUpdates._commit.comprehension_348 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 350 |
| ApplicationUpdates._commit.comprehension_348 | body | Comprehension item for body in ApplicationUpdates._commit.comprehension_348; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 350 |
| ApplicationUpdates._commit | originals | Local binding for originals in ApplicationUpdates._commit; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 354 |
| ApplicationUpdates._commit.comprehension_354 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 354 |
| ApplicationUpdates._commit | sealed | Local binding for sealed in ApplicationUpdates._commit; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 355 |
| ApplicationUpdates._commit | written | Local binding for written in ApplicationUpdates._commit; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 360 |
| ApplicationUpdates._commit | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 362, 368 |
| ApplicationUpdates._commit | body | Loop item for body in ApplicationUpdates._commit; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 362 |
| ApplicationUpdates._commit | stream | Managed resource for stream in ApplicationUpdates._commit; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 365 |
