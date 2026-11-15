# Reference for src/agentix/storage/tool_publication.py

Publish exact reviewed draft members into the public tool catalog.

Source fingerprint: 3c215f084fdcbe69b2674633faa039fe9ce3c4cb9eb922a3391e49e32801431d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### publish_tool_draft

Copy exact reviewed draft bytes to a new public directory without overwrite.

The caller must have completed human acceptance for the current bytes. This
helper performs no approval decision and retains the source draft as evidence.

Kind: callable. Declared return: None. Source line: 13.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | shutil | Imported dependency for shutil in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | uuid | Imported dependency for uuid in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | resolve_artifact_path | Imported dependency for resolve artifact path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | _MEMBERS | Module binding for MEMBERS in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 10 |
| publish_tool_draft | staging_root | Parameter for staging root in publish_tool_draft; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 13 |
| publish_tool_draft | public_root | Parameter for public root in publish_tool_draft; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 13 |
| publish_tool_draft | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 13 |
| publish_tool_draft | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 19 |
| publish_tool_draft | destination | Local binding for destination in publish_tool_draft; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| publish_tool_draft | files | Local binding for files in publish_tool_draft; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 25 |
| publish_tool_draft.comprehension_25 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 25 |
| publish_tool_draft | payloads | Local binding for payloads in publish_tool_draft; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 28 |
| publish_tool_draft | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 29, 40 |
| publish_tool_draft | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 29 |
| publish_tool_draft | content | Artifact or review text whose encoding, size and approval state must be checked. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 32, 40 |
| publish_tool_draft | temporary | Local binding for temporary in publish_tool_draft; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| publish_tool_draft.comprehension_43 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 45 |
| publish_tool_draft.comprehension_43 | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 45 |
