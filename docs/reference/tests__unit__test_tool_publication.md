# Reference for tests/unit/test_tool_publication.py

Approved tool publication keeps provisional bytes outside the public catalog.

Source fingerprint: fca143db90c9a6daf287d9d122e4baf3c7167d21e5c582fc274ae843f5bb1b6b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_draft_bytes_publish_only_to_an_empty_public_tool_directory

Publish exact reviewed members without exposing a draft in the public catalog.

Kind: callable. Declared return: None. Source line: 8.

### test_publication_never_overwrites_an_existing_tool

A staged proposal cannot replace a public tool with the same identity.

Kind: callable. Declared return: None. Source line: 36.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | system | Parameter for system in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | tmp_path | Parameter for tmp path in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | public_root | Local binding for public root in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | drafts_root | Local binding for drafts root in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | system.security.operation_id | Attribute for system.security.operation id in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 13 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | system.security.auto_approve | Attribute for system.security.auto approve in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 14 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | suffix | Loop item for suffix in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 17 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 17 |
| test_draft_bytes_publish_only_to_an_empty_public_tool_directory | staged | Local binding for staged in test_draft_bytes_publish_only_to_an_empty_public_tool_directory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 27 |
| test_publication_never_overwrites_an_existing_tool | system | Parameter for system in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 36 |
| test_publication_never_overwrites_an_existing_tool | tmp_path | Parameter for tmp path in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 36 |
| test_publication_never_overwrites_an_existing_tool | public_root | Local binding for public root in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_publication_never_overwrites_an_existing_tool | drafts_root | Local binding for drafts root in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_publication_never_overwrites_an_existing_tool | existing | Local binding for existing in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_publication_never_overwrites_an_existing_tool | original | Local binding for original in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_publication_never_overwrites_an_existing_tool | system.security.operation_id | Attribute for system.security.operation id in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 45 |
| test_publication_never_overwrites_an_existing_tool | system.security.auto_approve | Attribute for system.security.auto approve in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 46 |
| test_publication_never_overwrites_an_existing_tool | suffix | Loop item for suffix in test_publication_never_overwrites_an_existing_tool; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 48 |
| test_publication_never_overwrites_an_existing_tool | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 48 |
