# Reference for src/agentix/storage/catalog_migration.py

Reviewed, bounded relocation of authenticated catalog grants, without model calls.

Source storage is read-only. Unchanged same-policy tools/widgets may retain their
reviewed grants at an explicitly approved destination. Applications additionally
require current package validation and an injected native/browser verifier.

Source fingerprint: dc8d57cf128ad054521b00327d284e5dcb6d33ca5c9935218f67b9e3419c9a52

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### fingerprint

Return a SHA-256 content identity; this never establishes authorization.

Kind: callable. Declared return: str. Source line: 32.

### CatalogMigration

Own a single explicit source/destination plan; never overwrite target grants.

Not thread-safe: use one instance per operator. CatalogLock serializes apply
with normal destination mutations. Filesystem checks do not defeat a hostile
same-user process; rechecks detect ordinary concurrent edits before writes.

Kind: class. Declared return: Not declared / class. Source line: 37.

### CatalogMigration.__init__

Inject roots, authenticated protection and optional real app verification.

Construction rejects aliases, nested/shared roots and excluded artifacts;
it creates no files and never imports generated code.

Kind: callable. Declared return: None. Source line: 45.

### CatalogMigration._read

Capture bounded nonlinked file bytes for later freshness verification.

Kind: callable. Declared return: bytes | None. Source line: 81.

### CatalogMigration._path

Use the existing bounded approval namespace and name contract.

Kind: callable. Declared return: Path. Source line: 96.

### CatalogMigration._records

Enumerate at most 512 records in the explicit authenticated source namespace.

Kind: callable. Declared return: list[Path]. Source line: 102.

### CatalogMigration._decode

Unseal bounded metadata; never trust a tool-supplied JSON approval.

Kind: callable. Declared return: tuple[dict, bytes]. Source line: 111.

### CatalogMigration._grant

Reuse the production validator in disposable metadata storage.

Its revocation-on-error behavior can touch only the temporary record;
source and destination approvals are never passed to that mutating loader.

Kind: callable. Declared return: dict. Source line: 122.

### CatalogMigration._tool

Validate unchanged source grants or preserve valid newer destination grants.

Kind: callable. Declared return: tuple[Path, dict, bytes] | None. Source line: 140.

### CatalogMigration._widget

Require identical widget bytes, tool review, CSS, tests and widget policy.

Kind: callable. Declared return: tuple[Path, dict, bytes] | None. Source line: 171.

### CatalogMigration._application

Bind original review and current package; stale templates remain blocked.

Kind: callable. Declared return: tuple[Path, dict, bytes] | None. Source line: 219.

### CatalogMigration.plan

Return safe statuses and a digest binding all observed inputs, without target writes.

Kind: callable. Declared return: dict. Source line: 269.

### CatalogMigration._fresh

Reject input drift and newly introduced aliases immediately before publication.

Kind: callable. Declared return: None. Source line: 301.

### CatalogMigration.apply

Apply one exact reviewed plan with backups; applications require fresh real gates.

Existing grants are never overwritten. Errors leave original grants intact;
per-entry outcomes and backups allow an operator to inspect partial progress.
This is not a crash-atomic multi-file transaction.

Kind: callable. Declared return: dict. Source line: 314.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | extract_tool_schema | Imported dependency for extract tool schema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | DataProtector | Imported dependency for DataProtector in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | policy_fingerprint | Imported dependency for policy fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | CatalogLock | Imported dependency for CatalogLock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | PURPOSE | Imported dependency for PURPOSE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | app_policy | Imported dependency for app policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | WidgetStore | Imported dependency for WidgetStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | widget_policy | Imported dependency for widget policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | validate_widget_css | Imported dependency for validate widget css in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 29 |
| fingerprint | value | Value at the current validation/rendering boundary; apply the enclosing contract. | bytes | Enclosing invocation or class/instance lifetime | 32 |
| CatalogMigration.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| CatalogMigration.__init__ | source_home | Parameter for source home in CatalogMigration.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 47 |
| CatalogMigration.__init__ | source_tools | Parameter for source tools in CatalogMigration.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 48 |
| CatalogMigration.__init__ | target_home | Parameter for target home in CatalogMigration.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 49 |
| CatalogMigration.__init__ | protector | Parameter for protector in CatalogMigration.__init__; use the enclosing contract and type below. | DataProtector | Enclosing invocation or class/instance lifetime | 51 |
| CatalogMigration.__init__ | application_verifier | Parameter for application verifier in CatalogMigration.__init__; use the enclosing contract and type below. | Callable[[Path, dict, Path], bool] &#124; None | Enclosing invocation or class/instance lifetime | 52 |
| CatalogMigration.__init__ | widget_verifier | Parameter for widget verifier in CatalogMigration.__init__; use the enclosing contract and type below. | Callable[[ApprovedTool, dict, str, Path], bool] &#124; None | Enclosing invocation or class/instance lifetime | 53 |
| CatalogMigration.__init__ | root | Explicit root directory against which named paths are resolved. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| CatalogMigration.__init__.comprehension_62 | p | Comprehension item for p in CatalogMigration.__init__.comprehension_62; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 62 |
| CatalogMigration.__init__ | self.source | Explicit source document or source-code text; never imported for reference generation. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| CatalogMigration.__init__ | self.source_tools | Attribute for source tools in CatalogMigration.__init__; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| CatalogMigration.__init__ | self.target | Attribute for target in CatalogMigration.__init__; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| CatalogMigration.__init__ | self.tools | Attribute for tools in CatalogMigration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 69 |
| CatalogMigration.__init__ | self.protector | Attribute for protector in CatalogMigration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 74 |
| CatalogMigration.__init__ | self.verifier | Attribute for verifier in CatalogMigration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 74 |
| CatalogMigration.__init__ | self.widget_verifier | Attribute for widget verifier in CatalogMigration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| CatalogMigration.__init__ | self.inputs | Attribute for inputs in CatalogMigration.__init__; use the enclosing contract and type below. | dict[Path, bytes &#124; None] | Enclosing invocation or class/instance lifetime | 76 |
| CatalogMigration.__init__ | self.pending | Defensive pending-approval snapshot; never a capability to approve another owner. | list[tuple[dict, Path, dict, bytes]] | Enclosing invocation or class/instance lifetime | 77 |
| CatalogMigration.__init__ | self.effective | Attribute for effective in CatalogMigration.__init__; use the enclosing contract and type below. | dict[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 78 |
| CatalogMigration.__init__ | self.policies | Attribute for policies in CatalogMigration.__init__; use the enclosing contract and type below. | tuple[str, str, str] | Enclosing invocation or class/instance lifetime | 79 |
| CatalogMigration._read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| CatalogMigration._read | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 81 |
| CatalogMigration._read | optional | Parameter for optional in CatalogMigration._read; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 81 |
| CatalogMigration._read | limit | Parameter for limit in CatalogMigration._read; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 81 |
| CatalogMigration._read | stream | Managed resource for stream in CatalogMigration._read; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 89 |
| CatalogMigration._read | data | Local binding for data in CatalogMigration._read; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| CatalogMigration._path | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| CatalogMigration._path | home | Parameter for home in CatalogMigration._path; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 96 |
| CatalogMigration._path | kind | Parameter for kind in CatalogMigration._path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 96 |
| CatalogMigration._path | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 96 |
| CatalogMigration._path | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 96 |
| CatalogMigration._records | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 102 |
| CatalogMigration._records | kind | Parameter for kind in CatalogMigration._records; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 102 |
| CatalogMigration._records | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 102 |
| CatalogMigration._records | parent | Local binding for parent in CatalogMigration._records; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 104 |
| CatalogMigration._records | paths | Local binding for paths in CatalogMigration._records; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| CatalogMigration._decode | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| CatalogMigration._decode | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 111 |
| CatalogMigration._decode | raw | Local binding for raw in CatalogMigration._decode; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| CatalogMigration._decode | plain | Local binding for plain in CatalogMigration._decode; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 114 |
| CatalogMigration._decode | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| CatalogMigration._grant | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | raw | Parameter for raw in CatalogMigration._grant; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 122 |
| CatalogMigration._grant | temporary | Managed resource for temporary in CatalogMigration._grant; use the enclosing contract and type below. | Return type of TemporaryDirectory; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 128 |
| CatalogMigration._grant | store | Local binding for store in CatalogMigration._grant; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| CatalogMigration._grant | path | Path under validation or an explicitly scoped maintained source path. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| CatalogMigration._grant | record | Local binding for record in CatalogMigration._grant; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| CatalogMigration._tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| CatalogMigration._tool | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 140 |
| CatalogMigration._tool | item | Parameter for item in CatalogMigration._tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 140 |
| CatalogMigration._tool | old | Local binding for old in CatalogMigration._tool; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| CatalogMigration._tool | raw | Local binding for raw in CatalogMigration._tool; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| CatalogMigration._tool | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 143 |
| CatalogMigration._tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| CatalogMigration._tool | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| CatalogMigration._tool | destination | Local binding for destination in CatalogMigration._tool; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| CatalogMigration._tool | current | Local binding for current in CatalogMigration._tool; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| CatalogMigration._tool | record | Local binding for record in CatalogMigration._tool; use the enclosing contract and type below. | Return type of _grant; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| CatalogMigration._tool | schema | Local binding for schema in CatalogMigration._tool; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| CatalogMigration._widget | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 171 |
| CatalogMigration._widget | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 171 |
| CatalogMigration._widget | item | Parameter for item in CatalogMigration._widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 171 |
| CatalogMigration._widget | record | Local binding for record in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| CatalogMigration._widget | raw | Local binding for raw in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| CatalogMigration._widget | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 176 |
| CatalogMigration._widget | tool | Local binding for tool in CatalogMigration._widget; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| CatalogMigration._widget | service | Local binding for service in CatalogMigration._widget; use the enclosing contract and type below. | Return type of WidgetStore; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| CatalogMigration._widget | binding | Local binding for binding in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _binding; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| CatalogMigration._widget | old_binding | Local binding for old binding in CatalogMigration._widget; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| CatalogMigration._widget.comprehension_190 | k | Comprehension item for k in CatalogMigration._widget.comprehension_190; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 190, 191 |
| CatalogMigration._widget.comprehension_190 | v | Comprehension item for v in CatalogMigration._widget.comprehension_190; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 190, 191 |
| CatalogMigration._widget | proposal | Local binding for proposal in CatalogMigration._widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 195 |
| CatalogMigration._widget | suffix | Loop item for suffix in CatalogMigration._widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 197 |
| CatalogMigration._widget | key | Loop item for key in CatalogMigration._widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 197 |
| CatalogMigration._widget | proposal_key | Loop item for proposal key in CatalogMigration._widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 197 |
| CatalogMigration._widget | body | Local binding for body in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| CatalogMigration._widget | destination | Local binding for destination in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| CatalogMigration._widget | existing | Local binding for existing in CatalogMigration._widget; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 211 |
| CatalogMigration._application | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 219 |
| CatalogMigration._application | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 219 |
| CatalogMigration._application | item | Parameter for item in CatalogMigration._application; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 219 |
| CatalogMigration._application | record | Local binding for record in CatalogMigration._application; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| CatalogMigration._application | raw | Local binding for raw in CatalogMigration._application; use the enclosing contract and type below. | Return type of _decode; see its callable contract | Enclosing invocation or class/instance lifetime | 221 |
| CatalogMigration._application | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 222 |
| CatalogMigration._application | folder | Local binding for folder in CatalogMigration._application; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 222 |
| CatalogMigration._application | old_root | Local binding for old root in CatalogMigration._application; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 228 |
| CatalogMigration._application | new_root | Local binding for new root in CatalogMigration._application; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 228 |
| CatalogMigration._application | review | Local binding for review in CatalogMigration._application; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 235 |
| CatalogMigration._application | package | Local binding for package in CatalogMigration._application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 238 |
| CatalogMigration._application | member | Loop item for member in CatalogMigration._application; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 240 |
| CatalogMigration._application | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 245 |
| CatalogMigration._application | dependency | Loop item for dependency in CatalogMigration._application; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 245 |
| CatalogMigration._application | tool | Local binding for tool in CatalogMigration._application; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| CatalogMigration._application.comprehension_247 | key | Comprehension item for key in CatalogMigration._application.comprehension_247; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 249 |
| CatalogMigration._application.comprehension_247 | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 249 |
| CatalogMigration._application | destination | Local binding for destination in CatalogMigration._application; use the enclosing contract and type below. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
| CatalogMigration._application | existing | Local binding for existing in CatalogMigration._application; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 259 |
| CatalogMigration.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 269 |
| CatalogMigration.plan | self.inputs | Attribute for inputs in CatalogMigration.plan; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 271 |
| CatalogMigration.plan | self.pending | Defensive pending-approval snapshot; never a capability to approve another owner. | tuple | Enclosing invocation or class/instance lifetime | 271 |
| CatalogMigration.plan | self.effective | Attribute for effective in CatalogMigration.plan; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 271 |
| CatalogMigration.plan | self.policies | Attribute for policies in CatalogMigration.plan; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 272 |
| CatalogMigration.plan | items | Local binding for items in CatalogMigration.plan; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 273 |
| CatalogMigration.plan | kind | Loop item for kind in CatalogMigration.plan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 274 |
| CatalogMigration.plan | root | Explicit root directory against which named paths are resolved. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 274 |
| CatalogMigration.plan | check | Loop item for check in CatalogMigration.plan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 274 |
| CatalogMigration.plan | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 279 |
| CatalogMigration.plan | item | Local binding for item in CatalogMigration.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 280 |
| CatalogMigration.plan | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of check; see its callable contract | Enclosing invocation or class/instance lifetime | 282 |
| CatalogMigration.plan | error | Caught exception for error in CatalogMigration.plan; use the enclosing contract and type below. | (OSError, ValueError, KeyError, TypeError, SyntaxError) | Current exception handler; Python clears this binding afterward | 285 |
| CatalogMigration.plan | binding | Local binding for binding in CatalogMigration.plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 288 |
| CatalogMigration.plan.comprehension_290 | p | Comprehension item for p in CatalogMigration.plan.comprehension_290; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 292 |
| CatalogMigration.plan.comprehension_290 | b | Comprehension item for b in CatalogMigration.plan.comprehension_290; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 292 |
| CatalogMigration._fresh | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 301 |
| CatalogMigration._fresh | snapshot | Local binding for snapshot in CatalogMigration._fresh; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 305 |
| CatalogMigration._fresh | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 307 |
| CatalogMigration._fresh | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 307 |
| CatalogMigration._fresh | actual | Local binding for actual in CatalogMigration._fresh; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
| CatalogMigration._fresh | self.inputs | Attribute for inputs in CatalogMigration._fresh; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 312 |
| CatalogMigration.apply | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 314 |
| CatalogMigration.apply | reviewed_digest | Parameter for reviewed digest in CatalogMigration.apply; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 314 |
| CatalogMigration.apply | plan | Local binding for plan in CatalogMigration.apply; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 322 |
| CatalogMigration.apply | operation | Local binding for operation in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 325 |
| CatalogMigration.apply | item | Loop item for item in CatalogMigration.apply; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 328 |
| CatalogMigration.apply | destination | Loop item for destination in CatalogMigration.apply; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 328 |
| CatalogMigration.apply | record | Loop item for record in CatalogMigration.apply; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 328 |
| CatalogMigration.apply | raw | Loop item for raw in CatalogMigration.apply; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 328 |
| CatalogMigration.apply | started | Local binding for started in CatalogMigration.apply; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| CatalogMigration.apply | tool | Local binding for tool in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 337 |
| CatalogMigration.apply | css | Local binding for css in CatalogMigration.apply; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 338 |
| CatalogMigration.apply | evidence | Local binding for evidence in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 341, 358 |
| CatalogMigration.apply | package | Local binding for package in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 354 |
| CatalogMigration.apply | review | Local binding for review in CatalogMigration.apply; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 355 |
| CatalogMigration.apply | backup | Local binding for backup in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 365 |
| CatalogMigration.apply | sealed | Local binding for sealed in CatalogMigration.apply; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 367 |
| CatalogMigration.apply | stream | Managed resource for stream in CatalogMigration.apply; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 372 |
| CatalogMigration.apply | error | Caught exception for error in CatalogMigration.apply; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 378 |
| CatalogMigration.apply | reason | Local binding for reason in CatalogMigration.apply; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 380 |
