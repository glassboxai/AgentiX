# Reference for src/agentix/application/style_member.py

Owner-scoped rewrite of one scoped widget stylesheet without revoking approval.

The application identity excludes ``<tool>_widget.css`` members, so the closed
grammar in :mod:`agentix.widgets.styles` is the only gate a style edit passes.
This writer keeps the package self-consistent: it rewrites the member hash in
``application.json`` so capture still proves the bytes on disk are declared.

Source fingerprint: 8bcc18a4fcb410e6147aa652dcec1066fb00c3ba3172cecdaeca403da3dd961b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### style_member_name

Resolve a canonical tool identifier to its scoped stylesheet member.

Kind: callable. Declared return: str. Source line: 20.

### write_style_member

Validate and persist one scoped stylesheet, rebinding only its manifest hash.

Parameters: an absolute package folder, a ``<role>_widget.css`` member name and
the complete replacement text. Returns the new SHA-256 of the written bytes.
Raises ``ValueError`` for an unknown member, an unsafe declaration, an aliased
path or a hard-linked file. No crash transaction is claimed across the two
writes; a failure leaves capture rejecting the package rather than approving it.

Kind: callable. Declared return: str. Source line: 27.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | reject_alias | Imported dependency for reject alias in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | STYLE_SUFFIX | Imported dependency for STYLE SUFFIX in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | validate_widget_css | Imported dependency for validate widget css in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | MAX_STYLE_BYTES | Module binding for MAX STYLE BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 17 |
| style_member_name | tool | Parameter for tool in style_member_name; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| write_style_member | folder | Parameter for folder in write_style_member; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 27 |
| write_style_member | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 27 |
| write_style_member | css | Parameter for css in write_style_member; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27 |
| write_style_member | role | Local binding for role in write_style_member; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| write_style_member | body | Local binding for body in write_style_member; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| write_style_member | member | Local binding for member in write_style_member; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| write_style_member | manifest_path | Local binding for manifest path in write_style_member; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| write_style_member | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
