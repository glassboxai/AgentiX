# Reference for tests/test_widget_names.py

LAB-004 canonical package filenames must be executable and review-bound.

Source fingerprint: 819919504b27e9c7b523396582b6f99dd0c727c215f541b5df4ea2554dbd705d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_review_loads_canonical_named_widget

Catch loaders still looking for the literal tool_widget.py placeholder.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_generic_filename_is_not_accepted_as_active_package

Prevent silently using an obsolete placeholder after the naming correction.

Kind: callable. Declared return: Not declared / class. Source line: 24.

### test_designer_writes_canonical_artifacts_without_executing_proposals

Exercise real generation storage/parser using only a deterministic network double.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### test_designer_writes_canonical_artifacts_without_executing_proposals.Opener

Substitute only the local model boundary, preserving actual file behavior.

Kind: class. Declared return: Not declared / class. Source line: 47.

### test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 50.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | CONTRACT | Imported dependency for CONTRACT in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | approve_package | Imported dependency for approve package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | package_digest | Imported dependency for package digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| test_review_loads_canonical_named_widget | tmp_path | Parameter for tmp path in test_review_loads_canonical_named_widget; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| test_review_loads_canonical_named_widget | approved | Local binding for approved in test_review_loads_canonical_named_widget; use the enclosing contract and type below. | Return type of approve_package; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_generic_filename_is_not_accepted_as_active_package | tmp_path | Parameter for tmp path in test_generic_filename_is_not_accepted_as_active_package; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 24 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | tmp_path | Parameter for tmp path in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | monkeypatch | Parameter for monkeypatch in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | io | Imported dependency for io in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 36 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | widget_designer | Imported dependency for widget designer in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 38 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | candidate | Local binding for candidate in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 40 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | raw | Local binding for raw in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open | request | Parameter for request in test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open | timeout | Parameter for timeout in test_designer_writes_canonical_artifacts_without_executing_proposals.Opener.open; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | folder | Local binding for folder in test_designer_writes_canonical_artifacts_without_executing_proposals; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_designer_writes_canonical_artifacts_without_executing_proposals | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of generate_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
