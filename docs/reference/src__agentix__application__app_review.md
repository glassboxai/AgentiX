# Reference for src/agentix/application/app_review.py

Readable, owner-controller-invoked review of whitelisted application artifacts.

Generated source is data on the host. Explicit edits invalidate approval; this
service never imports candidate modules or executes their proposed tests.

Source fingerprint: 53e0dfbef0af820b7d7a2246e0a47ef0a859ae23faf64f2280a064e0a9cea667

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ApplicationReview

Present real files separately from provisional tests and independent cases.

Kind: class. Declared return: Not declared / class. Source line: 20.

### ApplicationReview._contracts

Use the selected catalog closure, retaining explicit legacy compatibility.

Kind: callable. Declared return: dict. Source line: 23.

### ApplicationReview._legacy_contracts

Derive tool modules from the reviewed package files, never a fixed registry.

Kind: callable. Declared return: dict. Source line: 27.

### ApplicationReview._files

Return only source members from the owner-bound manifest.

Kind: callable. Declared return: set[str]. Source line: 35.

### ApplicationReview._editable

Connection logic, reviewed cases, widget source, styles and tests are editable.

Kind: callable. Declared return: set[str]. Source line: 39.

### ApplicationReview._snapshot

Load only the server-owned bounded review, never browser-supplied JSON.

Kind: callable. Declared return: dict. Source line: 47.

### ApplicationReview.entries

Return a finite display-name/key list; keys are not arbitrary paths.

Kind: callable. Declared return: list[tuple[str, str]]. Source line: 51.

### ApplicationReview._review_key

Normalize only a whitelisted general widget-test member to its proposal view.

Kind: callable. Declared return: str. Source line: 81.

### ApplicationReview.read

Read a whitelisted member or virtual proposed test; reject path injection.

Kind: callable. Declared return: tuple[str, bool, str]. Source line: 87.

### ApplicationReview.save

Validate an explicit edit, persist it and report whether the grant was revoked.

The caller holds the owner controller lock and rejects concurrent work.
Executable members revoke the previous application grant before any write.
A scoped ``<tool>_widget.css`` edit returns ``False``: its closed grammar is
the gate, so the approval stays valid and no re-review is required.
No crash-transaction guarantee is made for multiple filesystem writes.

Kind: callable. Declared return: bool. Source line: 129.

### ApplicationReview.panes

Resolve one whitelisted tool-related selection to consistent review buffers.

Kind: callable. Declared return: dict. Source line: 264.

### ApplicationReview.save_group

Validate every pane before writing a pending app/tool revision, never import it.

Kind: callable. Declared return: bool. Source line: 291.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | validate_source | Imported dependency for validate source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | allowed_modules | Imported dependency for allowed modules in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | computation_only | Imported dependency for computation only in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 17 |
| ApplicationReview._contracts | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| ApplicationReview._contracts | item | Parameter for item in ApplicationReview._contracts; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 23 |
| ApplicationReview._legacy_contracts | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| ApplicationReview._legacy_contracts | item | Parameter for item in ApplicationReview._legacy_contracts; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 27 |
| ApplicationReview._legacy_contracts | package | Local binding for package in ApplicationReview._legacy_contracts; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| ApplicationReview._legacy_contracts.comprehension_30 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| ApplicationReview._legacy_contracts.comprehension_30.comprehension_32 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 32 |
| ApplicationReview._files | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| ApplicationReview._files | item | Parameter for item in ApplicationReview._files; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 35 |
| ApplicationReview._editable | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| ApplicationReview._editable | item | Parameter for item in ApplicationReview._editable; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 39 |
| ApplicationReview._editable.comprehension_41 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 43 |
| ApplicationReview._snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| ApplicationReview._snapshot | item | Parameter for item in ApplicationReview._snapshot; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 47 |
| ApplicationReview.entries | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| ApplicationReview.entries | item | Parameter for item in ApplicationReview.entries; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 51 |
| ApplicationReview.entries | tool_sources | Local binding for tool sources in ApplicationReview.entries; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 53 |
| ApplicationReview.entries.comprehension_53 | contract | Validated declarative acceptance data bound to current artifact identities. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 53 |
| ApplicationReview.entries | entries | Local binding for entries in ApplicationReview.entries; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 54 |
| ApplicationReview.entries.comprehension_54 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 66 |
| ApplicationReview.entries.comprehension_75 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 77 |
| ApplicationReview._review_key | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| ApplicationReview._review_key | item | Parameter for item in ApplicationReview._review_key; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 81 |
| ApplicationReview._review_key | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 81 |
| ApplicationReview.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 87 |
| ApplicationReview.read | item | Parameter for item in ApplicationReview.read; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 87 |
| ApplicationReview.read | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 87, 101 |
| ApplicationReview.read.comprehension_89 | _ | Comprehension item for  in ApplicationReview.read.comprehension_89; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 89 |
| ApplicationReview.read.comprehension_89 | key | Comprehension item for key in ApplicationReview.read.comprehension_89; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 89 |
| ApplicationReview.read | acceptance_status | Imported dependency for acceptance status in ApplicationReview.read; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationReview.read | snapshot | Local binding for snapshot in ApplicationReview.read; use the enclosing contract and type below. | Return type of _snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| ApplicationReview.read | acceptance | Local binding for acceptance in ApplicationReview.read; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 95 |
| ApplicationReview.read.comprehension_97 | key | Comprehension item for key in ApplicationReview.read.comprehension_97; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 97 |
| ApplicationReview.read | tool_name | Validated public tool identifier within the configured storage boundary. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 102 |
| ApplicationReview.read | source | Explicit source document or source-code text; never imported for reference generation. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 102 |
| ApplicationReview.read | role | Local binding for role in ApplicationReview.read; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| ApplicationReview.read | text | Local binding for text in ApplicationReview.read; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 117, 119 |
| ApplicationReview.read | editable | Local binding for editable in ApplicationReview.read; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationReview.save | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| ApplicationReview.save | item | Parameter for item in ApplicationReview.save; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 129 |
| ApplicationReview.save | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 129, 139 |
| ApplicationReview.save | text | Parameter for text in ApplicationReview.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 129 |
| ApplicationReview.save | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 129 |
| ApplicationReview.save | _ | Local binding for  in ApplicationReview.save; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| ApplicationReview.save | editable | Local binding for editable in ApplicationReview.save; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| ApplicationReview.save | validate_acceptance | Imported dependency for validate acceptance in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 145 |
| ApplicationReview.save | snapshot | Local binding for snapshot in ApplicationReview.save; use the enclosing contract and type below. | Return type of _snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 147, 187, 200 |
| ApplicationReview.save | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of validate_acceptance; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| ApplicationReview.save | error | Caught exception for error in ApplicationReview.save; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 150, 198 |
| ApplicationReview.save | acceptance_status | Imported dependency for acceptance status in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 151 |
| ApplicationReview.save | item.approved | Attribute for item.approved in ApplicationReview.save; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 161, 220 |
| ApplicationReview.save | item.verified | Attribute for item.verified in ApplicationReview.save; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 161, 220 |
| ApplicationReview.save | item.snapshot | Attribute for item.snapshot in ApplicationReview.save; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 162, 221 |
| ApplicationReview.save | item.identity | Attribute for item.identity in ApplicationReview.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 163, 223 |
| ApplicationReview.save | item.review_text | Attribute for item.review text in ApplicationReview.save; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 165, 192, 257 |
| ApplicationReview.save | validate_connection_source | Imported dependency for validate connection source in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 169 |
| ApplicationReview.save | write_style_member | Imported dependency for write style member in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 173 |
| ApplicationReview.save | validate_widget_css | Imported dependency for validate widget css in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 174 |
| ApplicationReview.save.comprehension_178 | role | Comprehension item for role in ApplicationReview.save.comprehension_178; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 180 |
| ApplicationReview.save.comprehension_178 | contract | Validated declarative acceptance data bound to current artifact identities. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 180 |
| ApplicationReview.save | role | Local binding for role in ApplicationReview.save; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 202, 226 |
| ApplicationReview.save | imports | Local binding for imports in ApplicationReview.save; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 205 |
| ApplicationReview.save.comprehension_214 | contract | Validated declarative acceptance data bound to current artifact identities. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 214 |
| ApplicationReview.save | item.catalog_id | Attribute for item.catalog id in ApplicationReview.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 222 |
| ApplicationReview.save | proposal | Loop item for proposal in ApplicationReview.save; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 226 |
| ApplicationReview.save | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 232 |
| ApplicationReview.save | extract_tool_schema | Imported dependency for extract tool schema in ApplicationReview.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 233 |
| ApplicationReview.save.comprehension_235 | tool | Comprehension item for tool in ApplicationReview.save.comprehension_235; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 239 |
| ApplicationReview.save.comprehension_241 | key | Comprehension item for key in ApplicationReview.save.comprehension_241; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 243 |
| ApplicationReview.save | item.digest | Attribute for item.digest in ApplicationReview.save; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| ApplicationReview.save.comprehension_250 | key | Comprehension item for key in ApplicationReview.save.comprehension_250; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 252 |
| ApplicationReview.panes | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 264 |
| ApplicationReview.panes | item | Parameter for item in ApplicationReview.panes; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 264 |
| ApplicationReview.panes | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 264 |
| ApplicationReview.panes | snapshot | Local binding for snapshot in ApplicationReview.panes; use the enclosing contract and type below. | Return type of _snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 266 |
| ApplicationReview.panes | role | Loop item for role in ApplicationReview.panes; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 267 |
| ApplicationReview.panes | contract | Validated declarative acceptance data bound to current artifact identities. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 267 |
| ApplicationReview.panes | tool | Local binding for tool in ApplicationReview.panes; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 268 |
| ApplicationReview.panes | names | Local binding for names in ApplicationReview.panes; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 269 |
| ApplicationReview.panes | proposal | Local binding for proposal in ApplicationReview.panes; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 277 |
| ApplicationReview.save_group | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 291 |
| ApplicationReview.save_group | item | Parameter for item in ApplicationReview.save_group; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 291 |
| ApplicationReview.save_group | values | Parameter for values in ApplicationReview.save_group; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 291, 303 |
| ApplicationReview.save_group | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 291 |
| ApplicationReview.save_group | role | Local binding for role in ApplicationReview.save_group; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 299, 368 |
| ApplicationReview.save_group | current | Local binding for current in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 300 |
| ApplicationReview.save_group | key | Loop item for key in ApplicationReview.save_group; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 304, 317, 350 |
| ApplicationReview.save_group | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 309 |
| ApplicationReview.save_group | tool | Local binding for tool in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 310 |
| ApplicationReview.save_group | snapshot | Local binding for snapshot in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of _snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| ApplicationReview.save_group | function | Local binding for function in ApplicationReview.save_group; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 312 |
| ApplicationReview.save_group | text | Local binding for text in ApplicationReview.save_group; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 318 |
| ApplicationReview.save_group | error | Caught exception for error in ApplicationReview.save_group; use the enclosing contract and type below. | (SyntaxError, ValueError, RecursionError) | Current exception handler; Python clears this binding afterward | 323 |
| ApplicationReview.save_group | original_code | Local binding for original code in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 329 |
| ApplicationReview.save_group | original_tests | Local binding for original tests in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| ApplicationReview.save_group | base | Local binding for base in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of setdefault; see its callable contract | Enclosing invocation or class/instance lifetime | 331 |
| ApplicationReview.save_group | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of setdefault; see its callable contract | Enclosing invocation or class/instance lifetime | 334 |
| ApplicationReview.save_group | item.approved | Attribute for item.approved in ApplicationReview.save_group; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 344 |
| ApplicationReview.save_group | item.verified | Attribute for item.verified in ApplicationReview.save_group; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 344 |
| ApplicationReview.save_group | item.snapshot | Attribute for item.snapshot in ApplicationReview.save_group; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 345 |
| ApplicationReview.save_group | item.catalog_id | Attribute for item.catalog id in ApplicationReview.save_group; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 346 |
| ApplicationReview.save_group | item.identity | Attribute for item.identity in ApplicationReview.save_group; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 347 |
| ApplicationReview.save_group | revision | Local binding for revision in ApplicationReview.save_group; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 348 |
| ApplicationReview.save_group | suffix | Loop item for suffix in ApplicationReview.save_group; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 350 |
| ApplicationReview.save_group | widgets | Local binding for widgets in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of setdefault; see its callable contract | Enclosing invocation or class/instance lifetime | 363 |
| ApplicationReview.save_group | proposal | Local binding for proposal in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of setdefault; see its callable contract | Enclosing invocation or class/instance lifetime | 364, 368 |
| ApplicationReview.save_group | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 374 |
| ApplicationReview.save_group | extract_tool_schema | Imported dependency for extract tool schema in ApplicationReview.save_group; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 375 |
| ApplicationReview.save_group.comprehension_377 | tool | Comprehension item for tool in ApplicationReview.save_group.comprehension_377; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 381 |
| ApplicationReview.save_group.comprehension_383 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 385 |
| ApplicationReview.save_group | item.digest | Attribute for item.digest in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 390 |
| ApplicationReview.save_group.comprehension_392 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 394 |
| ApplicationReview.save_group | item.review_text | Attribute for item.review text in ApplicationReview.save_group; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 399 |
