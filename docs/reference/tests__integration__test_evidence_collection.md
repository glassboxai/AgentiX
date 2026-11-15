# Reference for tests/integration/test_evidence_collection.py

Regress metadata inspection and constrain reporting to local transport.

Source fingerprint: 859d38b78c339863e45a70def76c6ee2ea2dd238a79268702646f462d1880cbf

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### load_helper

Load a standalone maintenance helper without application imports.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_missing_distribution_does_not_abort_other_versions

Verify missing distribution does not abort other versions.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### test_remote_or_ambiguous_report_endpoint_is_rejected

Verify remote or ambiguous report endpoint is rejected.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### test_loopback_report_endpoint_is_allowed

Verify loopback report endpoint is allowed.

Kind: callable. Declared return: Not declared / class. Source line: 54.

### test_report_redirects_are_refused

Verify report redirects are refused.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_report_draft_is_prose_only_and_retains_provenance

Verify report draft is prose only and retains provenance.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_incomplete_model_output_is_not_reported_as_success

Verify incomplete model output is not reported as success.

Kind: callable. Declared return: Not declared / class. Source line: 86.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3, 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| load_helper | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| load_helper | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 13 |
| load_helper | spec | Local binding for spec in load_helper; use the enclosing contract and type below. | Return type of spec_from_file_location; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| load_helper | module | Local binding for module in load_helper; use the enclosing contract and type below. | Return type of module_from_spec; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_missing_distribution_does_not_abort_other_versions | monkeypatch | Parameter for monkeypatch in test_missing_distribution_does_not_abort_other_versions; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 20 |
| test_missing_distribution_does_not_abort_other_versions | helper | Local binding for helper in test_missing_distribution_does_not_abort_other_versions; use the enclosing contract and type below. | Return type of load_helper; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_remote_or_ambiguous_report_endpoint_is_rejected | endpoint | Parameter for endpoint in test_remote_or_ambiguous_report_endpoint_is_rejected; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_loopback_report_endpoint_is_allowed | endpoint | Parameter for endpoint in test_loopback_report_endpoint_is_allowed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| test_report_draft_is_prose_only_and_retains_provenance | monkeypatch | Parameter for monkeypatch in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_report_draft_is_prose_only_and_retains_provenance | helper | Local binding for helper in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of load_helper; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_report_draft_is_prose_only_and_retains_provenance | response | Bounded response text to render or validate; it is not executable code. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_report_draft_is_prose_only_and_retains_provenance | response.__enter__ | Attribute for response.  enter in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_report_draft_is_prose_only_and_retains_provenance | response.__exit__ | Attribute for response.  exit in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_report_draft_is_prose_only_and_retains_provenance | response.read.return_value | Attribute for response.read.return value in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 75 |
| test_report_draft_is_prose_only_and_retains_provenance | opener | Local binding for opener in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_report_draft_is_prose_only_and_retains_provenance | opener.open.return_value | Attribute for opener.open.return value in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| test_report_draft_is_prose_only_and_retains_provenance | text | Local binding for text in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of draft; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_report_draft_is_prose_only_and_retains_provenance | provenance | Local binding for provenance in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Return type of draft; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_report_draft_is_prose_only_and_retains_provenance | request | Local binding for request in test_report_draft_is_prose_only_and_retains_provenance; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_incomplete_model_output_is_not_reported_as_success | monkeypatch | Parameter for monkeypatch in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 86 |
| test_incomplete_model_output_is_not_reported_as_success | helper | Local binding for helper in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Return type of load_helper; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_incomplete_model_output_is_not_reported_as_success | response | Bounded response text to render or validate; it is not executable code. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_incomplete_model_output_is_not_reported_as_success | response.__enter__ | Attribute for response.  enter in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_incomplete_model_output_is_not_reported_as_success | response.__exit__ | Attribute for response.  exit in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_incomplete_model_output_is_not_reported_as_success | response.read.return_value | Attribute for response.read.return value in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 92 |
| test_incomplete_model_output_is_not_reported_as_success | opener | Local binding for opener in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_incomplete_model_output_is_not_reported_as_success | opener.open.return_value | Attribute for opener.open.return value in test_incomplete_model_output_is_not_reported_as_success; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 94 |
