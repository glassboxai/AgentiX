# Reference for src/agentix/security.py

Compatibility security facade composing independent policy and storage services.

Source fingerprint: f152d2ab14c94d066e1998bf4e7b81c1407f475ed3ffd58f421b5298cb1225d4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SecurityManager

Preserve the class API used by callbacks and tool operations.

Runtime-specific subclasses receive explicit storage roots. The default class
retains the legacy process-wide coordinator for compatibility imports.

Kind: class. Declared return: Not declared / class. Source line: 11.

### SecurityManager.validate_and_resolve_path

Delegate to the root-specific resolved containment policy.

Kind: callable. Declared return: str. Source line: 21.

### SecurityManager.safe_write_file

Delegate persistence using this exact coordinator for approval state.

Kind: callable. Declared return: str. Source line: 26.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ApprovalCoordinator | Imported dependency for ApprovalCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SecurityViolationError | Imported dependency for SecurityViolationError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | resolve_artifact_path | Imported dependency for resolve artifact path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ArtifactStore | Imported dependency for ArtifactStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | __all__ | Module binding for all in module; use the enclosing contract and type below. | list | Module/process lifetime | 8 |
| SecurityManager | TOOLS_ROOT_DIR | Typed binding for TOOLS ROOT DIR in SecurityManager; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 18 |
| SecurityManager.validate_and_resolve_path | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| SecurityManager.validate_and_resolve_path | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 21 |
| SecurityManager.validate_and_resolve_path | filename | Parameter for filename in SecurityManager.validate_and_resolve_path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| SecurityManager.safe_write_file | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| SecurityManager.safe_write_file | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 26 |
| SecurityManager.safe_write_file | filename | Parameter for filename in SecurityManager.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| SecurityManager.safe_write_file | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 26 |
| SecurityManager.safe_write_file | mode | Parameter for mode in SecurityManager.safe_write_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
