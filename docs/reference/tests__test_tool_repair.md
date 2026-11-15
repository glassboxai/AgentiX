# Reference for tests/test_tool_repair.py

Rejected-tool repair preserves human acceptance and host-compared execution.

Source fingerprint: 298b5d06b32fc184d4df2161f623ce7adb2fa4058dc228cb959ff82c450e2d35

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### fixture

Compose the real protocol with an explicitly non-native trusted-fixture double.

Kind: callable. Declared return: Not declared / class. Source line: 34.

### repair_service

Fail until the explicitly approved repair workflow exists.

Kind: callable. Declared return: Not declared / class. Source line: 46.

### test_invalid_tests_leave_both_files_unchanged

Validate every buffer before revocation or the first filesystem write.

Kind: callable. Declared return: Not declared / class. Source line: 57.

### test_repair_retests_requires_review_and_establishes_reuse

Unit test success cannot skip manual acceptance or the real worker protocol.

Kind: callable. Declared return: Not declared / class. Source line: 71.

### test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection

Retain the proposed bytes even when rejecting the file prevented its creation.

Kind: callable. Declared return: Not declared / class. Source line: 84.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | library | Imported dependency for library in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Protector | Imported dependency for Protector in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | TrustedFixtureSandbox | Imported dependency for TrustedFixtureSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | approve_next_review | Imported dependency for approve next review in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ArtifactTools | Imported dependency for ArtifactTools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | CODE | Module binding for CODE in module; use the enclosing contract and type below. | str | Module/process lifetime | 18 |
| module | TESTS | Module binding for TESTS in module; use the enclosing contract and type below. | str | Module/process lifetime | 19 |
| module | CASES | Module binding for CASES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 20 |
| fixture | tmp_path | Parameter for tmp path in fixture; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| fixture | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| fixture | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| fixture | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in fixture; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| fixture | security.operation_id | Attribute for security.operation id in fixture; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 40 |
| fixture | store | Local binding for store in fixture; use the enclosing contract and type below. | Return type of ApprovalStore; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| fixture | operations | Local binding for operations in fixture; use the enclosing contract and type below. | Return type of ArtifactTools; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| repair_service | tmp_path | Parameter for tmp path in repair_service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| repair_service | security | Owner-scoped approval and path boundary injected into this service. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| repair_service | operations | Parameter for operations in repair_service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| repair_service | RejectedTool | Imported dependency for RejectedTool in repair_service; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| repair_service | ToolRepair | Imported dependency for ToolRepair in repair_service; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| repair_service.lambda_53 | context | Callback parameter for context in repair_service.lambda_53; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 53 |
| test_invalid_tests_leave_both_files_unchanged | tmp_path | Parameter for tmp path in test_invalid_tests_leave_both_files_unchanged; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_invalid_tests_leave_both_files_unchanged | root | Explicit root directory against which named paths are resolved. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_invalid_tests_leave_both_files_unchanged | security | Owner-scoped approval and path boundary injected into this service. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_invalid_tests_leave_both_files_unchanged | operations | Local binding for operations in test_invalid_tests_leave_both_files_unchanged; use the enclosing contract and type below. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_invalid_tests_leave_both_files_unchanged | service | Local binding for service in test_invalid_tests_leave_both_files_unchanged; use the enclosing contract and type below. | Return type of repair_service; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_invalid_tests_leave_both_files_unchanged | draft | Local binding for draft in test_invalid_tests_leave_both_files_unchanged; use the enclosing contract and type below. | Return type of repair_service; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_invalid_tests_leave_both_files_unchanged | folder | Local binding for folder in test_invalid_tests_leave_both_files_unchanged; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_repair_retests_requires_review_and_establishes_reuse | tmp_path | Parameter for tmp path in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| test_repair_retests_requires_review_and_establishes_reuse | root | Explicit root directory against which named paths are resolved. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_repair_retests_requires_review_and_establishes_reuse | security | Owner-scoped approval and path boundary injected into this service. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_repair_retests_requires_review_and_establishes_reuse | operations | Local binding for operations in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_repair_retests_requires_review_and_establishes_reuse | service | Local binding for service in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Return type of repair_service; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_repair_retests_requires_review_and_establishes_reuse | draft | Local binding for draft in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Return type of repair_service; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_repair_retests_requires_review_and_establishes_reuse | thread | Local binding for thread in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_repair_retests_requires_review_and_establishes_reuse | errors | Local binding for errors in test_repair_retests_requires_review_and_establishes_reuse; use the enclosing contract and type below. | Return type of approve_next_review; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_repair_retests_requires_review_and_establishes_reuse | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of save_and_validate; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | tmp_path | Parameter for tmp path in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 84 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | root | Explicit root directory against which named paths are resolved. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | security | Owner-scoped approval and path boundary injected into this service. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | operations | Local binding for operations in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Return type of fixture; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | controller | Local binding for controller in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection.lambda_88 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 88 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | worker | Local binding for worker in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | deadline | Local binding for deadline in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection | draft | Local binding for draft in test_rejected_unwritten_code_is_recoverable_only_after_valid_rejection; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 109 |
