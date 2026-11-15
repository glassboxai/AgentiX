# Reference for src/agentix/retrieval/catalog.py

Read the GUI catalog's explicit root into bounded AST-only search descriptors.

No directory is guessed and no generated Python is imported or executed. This
adapter accepts the same ToolCatalog instance/root as the GUI. Scans are read-only;
filesystem changes after a scan become visible on the next synchronization.

Source fingerprint: 910985675bab64c248cc4cf86e59b763f517be2b56487d8894007d1ee0bc4f6f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _stamp

Identify an opened file version to detect ordinary replacement/write races.

Kind: callable. Declared return: tuple[int, ...]. Source line: 22.

### CatalogToolSource

Adapt canonical installed functions from an explicitly injected GUI catalog.

Invalid tools are reported, while directory/read failures abort the snapshot.
Alias and size checks bound metadata reads; they are not execution isolation
or a guarantee against a hostile process racing filesystem checks.

Kind: class. Declared return: Not declared / class. Source line: 27.

### CatalogToolSource.__init__

Remember an absolute catalog root without enumerating or executing tools.

Kind: callable. Declared return: None. Source line: 35.

### CatalogToolSource._read

Read bounded regular unaliased bytes, rejecting changed versions and hard links.

Raise ValueError for unsafe paths, OverflowError for oversized source and
OSError when a complete stable read cannot be established. No source runs.

Kind: callable. Declared return: bytes. Source line: 46.

### CatalogToolSource.snapshot

Return a full source snapshot or propagate directory/read errors.

Missing roots fail explicitly; existing empty roots represent deletion of
all tools. Canonical parse errors, aliases and oversized files are reported
as rejected entries, so stale descriptors are removed during synchronization.

Kind: callable. Declared return: CatalogSnapshot. Source line: 72.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | islice | Imported dependency for islice in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | CatalogRejection | Imported dependency for CatalogRejection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | CatalogSnapshot | Imported dependency for CatalogSnapshot in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| _stamp | value | Value at the current validation/rendering boundary; apply the enclosing contract. | os.stat_result | Enclosing invocation or class/instance lifetime | 22 |
| CatalogToolSource.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| CatalogToolSource.__init__ | catalog | Parameter for catalog in CatalogToolSource.__init__; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 35 |
| CatalogToolSource.__init__ | self.catalog | Attribute for catalog in CatalogToolSource.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| CatalogToolSource.__init__ | self.root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| CatalogToolSource.__init__ | normalized | Local binding for normalized in CatalogToolSource.__init__; use the enclosing contract and type below. | Return type of normcase; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| CatalogToolSource.__init__ | self.identity | Explicit owner identity used by a session factory or fixture. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| CatalogToolSource._read | source | Explicit source document or source-code text; never imported for reference generation. | Path | Enclosing invocation or class/instance lifetime | 46 |
| CatalogToolSource._read | before | Local binding for before in CatalogToolSource._read; use the enclosing contract and type below. | Return type of stat; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| CatalogToolSource._read | stream | Managed resource for stream in CatalogToolSource._read; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 58 |
| CatalogToolSource._read | opened | Local binding for opened in CatalogToolSource._read; use the enclosing contract and type below. | Return type of fstat; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| CatalogToolSource._read | raw | Local binding for raw in CatalogToolSource._read; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| CatalogToolSource._read | after | Local binding for after in CatalogToolSource._read; use the enclosing contract and type below. | Return type of fstat; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| CatalogToolSource._read | current | Local binding for current in CatalogToolSource._read; use the enclosing contract and type below. | Return type of stat; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| CatalogToolSource.snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| CatalogToolSource.snapshot | entries | Local binding for entries in CatalogToolSource.snapshot; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| CatalogToolSource.snapshot | descriptors | Local binding for descriptors in CatalogToolSource.snapshot; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 85 |
| CatalogToolSource.snapshot | rejected | Local binding for rejected in CatalogToolSource.snapshot; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 85 |
| CatalogToolSource.snapshot | folder | Loop item for folder in CatalogToolSource.snapshot; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 86 |
| CatalogToolSource.snapshot | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| CatalogToolSource.snapshot | raw | Local binding for raw in CatalogToolSource.snapshot; use the enclosing contract and type below. | Return type of _read; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| CatalogToolSource.snapshot | descriptor | Local binding for descriptor in CatalogToolSource.snapshot; use the enclosing contract and type below. | Return type of descriptor_from_source; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
