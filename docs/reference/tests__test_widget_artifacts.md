# Reference for tests/test_widget_artifacts.py

LAB-003 artifact review binds widget, tool and contract before native staging.

Source fingerprint: 3236c6b71496eb3ec378e6f603415e7de5060835b7987eefcc1c2560a3b42385

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_review_refuses_changed_widget_after_digest

Catch approving one source snapshot and executing a later edit.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_generated_widget_policy_rejects_unsupported_capabilities

Catch executable imports, host-style access and unsupported browser content.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### test_review_accepts_bounded_nonexecutable_presentation_options

Catch rejection of harmless model output without allowing executable options.

Kind: callable. Declared return: Not declared / class. Source line: 37.

### test_review_refuses_changed_related_artifact

Catch stale review when tool implementation, proposed tests or contract changes.

Kind: callable. Declared return: Not declared / class. Source line: 55.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | approve_package | Imported dependency for approve package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | package_digest | Imported dependency for package digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | validate_widget | Imported dependency for validate widget in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_review_refuses_changed_widget_after_digest | tmp_path | Parameter for tmp path in test_review_refuses_changed_widget_after_digest; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_review_refuses_changed_widget_after_digest | Path | Imported dependency for Path in test_review_refuses_changed_widget_after_digest; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_review_refuses_changed_widget_after_digest | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_bytes; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_review_refuses_changed_widget_after_digest | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of package_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_generated_widget_policy_rejects_unsupported_capabilities | source | Explicit source document or source-code text; never imported for reference generation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| test_review_accepts_bounded_nonexecutable_presentation_options | Path | Imported dependency for Path in test_review_accepts_bounded_nonexecutable_presentation_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 39 |
| test_review_accepts_bounded_nonexecutable_presentation_options | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 41, 42, 43 |
| test_review_refuses_changed_related_artifact | tmp_path | Parameter for tmp path in test_review_refuses_changed_related_artifact; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_review_refuses_changed_related_artifact | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| test_review_refuses_changed_related_artifact | json | Imported dependency for json in test_review_refuses_changed_related_artifact; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 57 |
| test_review_refuses_changed_related_artifact | Path | Imported dependency for Path in test_review_refuses_changed_related_artifact; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_review_refuses_changed_related_artifact | CONTRACT | Imported dependency for CONTRACT in test_review_refuses_changed_related_artifact; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_review_refuses_changed_related_artifact | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of package_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_review_refuses_changed_related_artifact | handle | Managed resource for handle in test_review_refuses_changed_related_artifact; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 69 |
