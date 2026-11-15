# Reference for src/agentix/security/__init__.py

Compatibility security facade composing approval, draft and public tool storage.

Source fingerprint: 8321575c613a34e49b3399f398abd726e36f57abe61332441d2869eada4a49fc

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SecurityManager

Preserve the class API used by callbacks and tool operations.

Runtime-specific subclasses receive explicit storage roots. The default class
retains the legacy process-wide coordinator for compatibility imports.

Kind: class. Declared return: Not declared / class. Source line: 14.

### SecurityManager._own_root

Return a storage root only when this exact class configured it.

Roots are mutable class state. Reading them through normal attribute
lookup would let a subclass inherit a base-class runtime configuration
and route its drafts or publication into another owner's catalog, so
only the defining class's own namespace counts here.

Kind: callable. Declared return: str | None. Source line: 27.

### SecurityManager._tools_root

Resolve the effective tool root, failing closed when unconfigured.

The default class resolves AGENTIX_TOOLS_ROOT lazily so importing this
module never requires deployment configuration or creates storage.

Kind: callable. Declared return: str. Source line: 38.

### SecurityManager.published_tools_root

Return the installed catalog root, never an active draft directory.

``TOOLS_ROOT_DIR`` points at the isolated proposal while a tool is being
created, so an explorer action must resolve the published root instead.
Nothing is created and no directory is enumerated here.

Kind: callable. Declared return: str. Source line: 50.

### SecurityManager.configure_tool_storage

Bind public catalog and proposal roots without creating either directory.

Kind: callable. Declared return: None. Source line: 60.

### SecurityManager.begin_tool_draft

Route one creation operation to its isolated proposal root.

Kind: callable. Declared return: None. Source line: 68.

### SecurityManager.publish_current_draft

Publish current staged bytes to the public catalog after host acceptance.

Kind: callable. Declared return: None. Source line: 88.

### SecurityManager.restore_public_tool_storage

Leave a failed or completed proposal and restore public-catalog access.

Kind: callable. Declared return: None. Source line: 101.

### SecurityManager.validate_and_resolve_path

Delegate to the root-specific resolved containment policy.

Kind: callable. Declared return: str. Source line: 109.

### SecurityManager.safe_write_file

Delegate persistence using this exact coordinator for approval state.

Kind: callable. Declared return: str. Source line: 114.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | ApprovalCoordinator | Imported dependency for ApprovalCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | SecurityViolationError | Imported dependency for SecurityViolationError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | resolve_artifact_path | Imported dependency for resolve artifact path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ArtifactStore | Imported dependency for ArtifactStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | __all__ | Module binding for all in module; use the enclosing contract and type below. | list | Module/process lifetime | 11 |
| SecurityManager | TOOLS_ROOT_DIR | Typed binding for TOOLS ROOT DIR in SecurityManager; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| SecurityManager | PUBLISHED_TOOLS_ROOT_DIR | Typed binding for PUBLISHED TOOLS ROOT DIR in SecurityManager; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 22 |
| SecurityManager | DRAFTS_ROOT_DIR | Typed binding for DRAFTS ROOT DIR in SecurityManager; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 23 |
| SecurityManager | _active_draft_root | Typed binding for active draft root in SecurityManager; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 24 |
| SecurityManager._own_root | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| SecurityManager._own_root | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 27 |
| SecurityManager._tools_root | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 38 |
| SecurityManager._tools_root | configured | Local binding for configured in SecurityManager._tools_root; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| SecurityManager.published_tools_root | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| SecurityManager.configure_tool_storage | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| SecurityManager.configure_tool_storage | public_root | Parameter for public root in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 60 |
| SecurityManager.configure_tool_storage | drafts_root | Parameter for drafts root in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 60 |
| SecurityManager.configure_tool_storage | cls.PUBLISHED_TOOLS_ROOT_DIR | Attribute for cls.PUBLISHED TOOLS ROOT DIR in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| SecurityManager.configure_tool_storage | cls.DRAFTS_ROOT_DIR | Attribute for cls.DRAFTS ROOT DIR in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| SecurityManager.configure_tool_storage | cls.TOOLS_ROOT_DIR | Attribute for cls.TOOLS ROOT DIR in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| SecurityManager.configure_tool_storage | cls._active_draft_root | Attribute for cls. active draft root in SecurityManager.configure_tool_storage; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 65 |
| SecurityManager.begin_tool_draft | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| SecurityManager.begin_tool_draft | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 68 |
| SecurityManager.begin_tool_draft | owner | Local binding for owner in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 72 |
| SecurityManager.begin_tool_draft | operation | Local binding for operation in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 72 |
| SecurityManager.begin_tool_draft.comprehension_73 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 74 |
| SecurityManager.begin_tool_draft | public | Local binding for public in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| SecurityManager.begin_tool_draft | drafts | Local binding for drafts in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| SecurityManager.begin_tool_draft | active | Local binding for active in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| SecurityManager.begin_tool_draft | cls.PUBLISHED_TOOLS_ROOT_DIR | Attribute for cls.PUBLISHED TOOLS ROOT DIR in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| SecurityManager.begin_tool_draft | cls.DRAFTS_ROOT_DIR | Attribute for cls.DRAFTS ROOT DIR in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| SecurityManager.begin_tool_draft | cls._active_draft_root | Attribute for cls. active draft root in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| SecurityManager.begin_tool_draft | cls.TOOLS_ROOT_DIR | Attribute for cls.TOOLS ROOT DIR in SecurityManager.begin_tool_draft; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| SecurityManager.publish_current_draft | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 88 |
| SecurityManager.publish_current_draft | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 88 |
| SecurityManager.publish_current_draft | publish_tool_draft | Imported dependency for publish tool draft in SecurityManager.publish_current_draft; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 90 |
| SecurityManager.publish_current_draft | active_draft | Local binding for active draft in SecurityManager.publish_current_draft; use the enclosing contract and type below. | Return type of _own_root; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| SecurityManager.publish_current_draft | published | Local binding for published in SecurityManager.publish_current_draft; use the enclosing contract and type below. | Return type of _own_root; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| SecurityManager.publish_current_draft | cls.TOOLS_ROOT_DIR | Attribute for cls.TOOLS ROOT DIR in SecurityManager.publish_current_draft; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 97 |
| SecurityManager.publish_current_draft | cls._active_draft_root | Attribute for cls. active draft root in SecurityManager.publish_current_draft; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 98 |
| SecurityManager.restore_public_tool_storage | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| SecurityManager.restore_public_tool_storage | published | Local binding for published in SecurityManager.restore_public_tool_storage; use the enclosing contract and type below. | Return type of _own_root; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| SecurityManager.restore_public_tool_storage | cls.TOOLS_ROOT_DIR | Attribute for cls.TOOLS ROOT DIR in SecurityManager.restore_public_tool_storage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 105 |
| SecurityManager.restore_public_tool_storage | cls._active_draft_root | Attribute for cls. active draft root in SecurityManager.restore_public_tool_storage; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 106 |
| SecurityManager.validate_and_resolve_path | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 109 |
| SecurityManager.validate_and_resolve_path | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 109 |
| SecurityManager.validate_and_resolve_path | filename | Parameter for filename in SecurityManager.validate_and_resolve_path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 109 |
| SecurityManager.safe_write_file | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| SecurityManager.safe_write_file | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 114 |
| SecurityManager.safe_write_file | filename | Parameter for filename in SecurityManager.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 114 |
| SecurityManager.safe_write_file | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 114 |
| SecurityManager.safe_write_file | mode | Parameter for mode in SecurityManager.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 114 |
