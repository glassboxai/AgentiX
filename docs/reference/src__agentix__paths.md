# Reference for src/agentix/paths.py

Resolved artifact containment and Windows component validation.

No storage is inspected during import. Callers pass a trusted storage root.
Existing links are resolved at call time; this is not race-proof OS isolation.

Source fingerprint: bf8c04d21ec00634be69ea561ba06f8caeefc5872ca824b267103ed73379df2b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SecurityViolationError

An artifact path violates the configured storage boundary.

Kind: class. Declared return: Not declared / class. Source line: 17.

### resolve_artifact_path

Return an absolute artifact path confined to one named tool directory.

Args:
    tool_name: One portable directory component, without drive syntax.
    filename: Relative artifact path; nested directories are supported.

Raises:
    SecurityViolationError: Invalid Windows names, traversal, aliases or
        resolved paths outside the configured root/tool boundary.

Existing links are resolved before checking components. A tool directory
may not alias another directory. This does not eliminate races against a
hostile process changing filesystem links after validation.

Kind: callable. Declared return: str. Source line: 21.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ntpath | Imported dependency for ntpath in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 14 |
| resolve_artifact_path | root_directory | Parameter for root directory in resolve_artifact_path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| resolve_artifact_path | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 21 |
| resolve_artifact_path | filename | Parameter for filename in resolve_artifact_path; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 21 |
| resolve_artifact_path | parts | Local binding for parts in resolve_artifact_path; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| resolve_artifact_path | part | Loop item for part in resolve_artifact_path; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 50 |
| resolve_artifact_path | root | Explicit root directory against which named paths are resolved. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| resolve_artifact_path | expected_tool | Local binding for expected tool in resolve_artifact_path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| resolve_artifact_path | tool_dir | Local binding for tool dir in resolve_artifact_path; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| resolve_artifact_path | target | Local binding for target in resolve_artifact_path; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| resolve_artifact_path | exc | Caught exception for exc in resolve_artifact_path; use the enclosing contract and type below. | (ValueError, OSError, RuntimeError) | Current exception handler; Python clears this binding afterward | 73 |
