# Reference for tests/test_maintenance_owners.py

Deletion confirmations are bound to one session, target and current contents.

Source fingerprint: 9abd0b2944cb0bee12616fad2c8ba17a64e1f958e3e7b7c2a0c1101728e21535

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### setup

Compose real temporary storage with fake authorization protection only.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### setup.Security

Minimal tool-root holder mirroring the maintained security contract.

Kind: class. Declared return: Not declared / class. Source line: 37.

### setup.Security.published_tools_root

Return the configured root so a test can point it at a missing folder.

Kind: callable. Declared return: Not declared / class. Source line: 43.

### test_reseal_batch_stops_when_changed_tool_tests_fail

A changed tool is re-run, and a failing suite stops the batch.

Kind: callable. Declared return: Not declared / class. Source line: 51.

### test_reseal_batch_stops_when_changed_tool_tests_fail.Store

Accept every intact tool and report the changed one.

Kind: class. Declared return: Not declared / class. Source line: 56.

### test_reseal_batch_stops_when_changed_tool_tests_fail.Store.reseal

Return the changed reason for the designated tool.

Kind: callable. Declared return: Not declared / class. Source line: 59.

### test_reseal_batch_stops_when_changed_tool_tests_fail.Operations

Report a failing isolated suite without executing generated code.

Kind: class. Declared return: Not declared / class. Source line: 64.

### test_reseal_batch_stops_when_changed_tool_tests_fail.Operations.verify_existing_tool_tool

Fail the isolated suite for the changed tool.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_reseal_batch_reruns_missing_tools_and_requires_acceptance

A missing record is re-run, and acceptance review is never granted here.

Kind: callable. Declared return: Not declared / class. Source line: 89.

### test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store

Report every record as absent without touching storage.

Kind: class. Declared return: Not declared / class. Source line: 94.

### test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store.reseal

Return the missing-record reason for every tool.

Kind: callable. Declared return: Not declared / class. Source line: 97.

### test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Operations

Report a passing isolated suite without executing generated code.

Kind: class. Declared return: Not declared / class. Source line: 101.

### test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Operations.verify_existing_tool_tool

Pass the isolated suite and record the call.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### test_reveal_opens_the_owned_catalog_root_without_browser_paths

V7-063: explorer buttons open server-resolved roots for the owning session only.

Kind: callable. Declared return: Not declared / class. Source line: 125.

### test_reveal_raises_the_opened_folder_above_the_browser

V7-065: focus runs after a valid open, with the resolved folder name and prior handles.

Kind: callable. Declared return: Not declared / class. Source line: 144.

### test_reveal_keeps_success_when_focus_is_refused

A refused foreground change must not turn a completed open into a failed action.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### test_reveal_opens_when_the_window_snapshot_fails

A failed native enumeration must not block the folder the owner asked to open.

Kind: callable. Declared return: Not declared / class. Source line: 175.

### test_reveal_reports_an_opener_failure_as_a_validation_error

V7-064: a refused shell open must reach the modal instead of a raw framework error.

Kind: callable. Declared return: Not declared / class. Source line: 188.

### test_reveal_reports_an_opener_failure_as_a_validation_error.opener

Refuse the open the way a missing shell association does.

Kind: callable. Declared return: Not declared / class. Source line: 194.

### test_reveal_never_focuses_a_foreign_session

Ownership is checked before either the opener or the focus helper runs.

Kind: callable. Declared return: Not declared / class. Source line: 204.

### test_reveal_refuses_a_missing_or_aliased_directory

A deleted or linked catalog root is reported instead of opening another folder.

Kind: callable. Declared return: Not declared / class. Source line: 218.

### test_cancellation_does_not_remove_files

Preparing and cancelling a destructive operation grants no deletion.

Kind: callable. Declared return: Not declared / class. Source line: 230.

### test_confirmation_cannot_cross_sessions_or_be_replayed

A foreign browser or repeated button request cannot reuse a deletion grant.

Kind: callable. Declared return: Not declared / class. Source line: 244.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | installed | Imported dependency for installed in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | registry | Imported dependency for registry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | library | Imported dependency for library in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| setup | tmp_path | Parameter for tmp path in setup; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| setup | CatalogMaintenanceBackend | Imported dependency for CatalogMaintenanceBackend in setup; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 14 |
| setup | ApplicationsBackend | Imported dependency for ApplicationsBackend in setup; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 17 |
| setup | CatalogMaintenance | Imported dependency for CatalogMaintenance in setup; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| setup | tools | Local binding for tools in setup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| setup | fixture | Local binding for fixture in setup; use the enclosing contract and type below. | Return type of installed; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| setup | apps | Local binding for apps in setup; use the enclosing contract and type below. | Return type of library; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| setup | sessions | Local binding for sessions in setup; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| setup | actions | Local binding for actions in setup; use the enclosing contract and type below. | Return type of CatalogMaintenanceBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| setup.lambda_29 | controller | Callback parameter for controller in setup.lambda_29; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 29 |
| setup.lambda_29.lambda_30 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 30 |
| setup.lambda_33 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 33 |
| setup.lambda_33 | before | Callback parameter for before in setup.lambda_33; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 33 |
| setup | owner | Local binding for owner in setup; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| setup.Security | TOOLS_ROOT_DIR | Local binding for TOOLS ROOT DIR in setup.Security; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| setup.Security.published_tools_root | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| setup | owner.controller.security | Attribute for owner.controller.security in setup; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | tmp_path | Parameter for tmp path in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | actions | Local binding for actions in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | owner | Local binding for owner in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | tools | Local binding for tools in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | _apps | Local binding for apps in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | calls | Local binding for calls in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 54 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Store.reseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Store.reseal | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Store.reseal | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Store.reseal | tests | Optional unittest source snapshot; child-authored success remains provisional. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Operations | verification | Content-bound ledger used to authorize only the current approved operation. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Operations.verify_existing_tool_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_reseal_batch_stops_when_changed_tool_tests_fail.Operations.verify_existing_tool_tool | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | owner.controller.tool_operations | Attribute for owner.controller.tool operations in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of Operations; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 74 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | folder | Local binding for folder in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | request | Local binding for request in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | message | Local binding for message in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_reseal_batch_stops_when_changed_tool_tests_fail | token | Local binding for token in test_reseal_batch_stops_when_changed_tool_tests_fail; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | tmp_path | Parameter for tmp path in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 89 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | actions | Local binding for actions in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | owner | Local binding for owner in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | tools | Local binding for tools in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | _apps | Local binding for apps in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | ran | Local binding for ran in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 92 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store.reseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store.reseal | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store.reseal | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Store.reseal | tests | Optional unittest source snapshot; child-authored success remains provisional. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Operations | verification | Content-bound ledger used to authorize only the current approved operation. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Operations.verify_existing_tool_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance.Operations.verify_existing_tool_tool | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | owner.controller.tool_operations | Attribute for owner.controller.tool operations in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of Operations; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | folder | Local binding for folder in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | message | Local binding for message in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_reseal_batch_reruns_missing_tools_and_requires_acceptance | _token | Local binding for token in test_reseal_batch_reruns_missing_tools_and_requires_acceptance; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | tmp_path | Parameter for tmp path in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 125 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | SessionAccessError | Imported dependency for SessionAccessError in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 127 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | actions | Local binding for actions in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | owner | Local binding for owner in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | tools | Local binding for tools in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | apps | Local binding for apps in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | opened | Local binding for opened in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 130 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | actions.opener | Attribute for actions.opener in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_reveal_opens_the_owned_catalog_root_without_browser_paths | request | Local binding for request in test_reveal_opens_the_owned_catalog_root_without_browser_paths; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_reveal_raises_the_opened_folder_above_the_browser | tmp_path | Parameter for tmp path in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 144 |
| test_reveal_raises_the_opened_folder_above_the_browser | actions | Local binding for actions in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_reveal_raises_the_opened_folder_above_the_browser | owner | Local binding for owner in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_reveal_raises_the_opened_folder_above_the_browser | tools | Local binding for tools in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_reveal_raises_the_opened_folder_above_the_browser | apps | Local binding for apps in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| test_reveal_raises_the_opened_folder_above_the_browser | opened | Local binding for opened in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 147 |
| test_reveal_raises_the_opened_folder_above_the_browser | focused | Local binding for focused in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 147 |
| test_reveal_raises_the_opened_folder_above_the_browser | actions.opener | Attribute for actions.opener in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_reveal_raises_the_opened_folder_above_the_browser | actions.window_snapshot | Attribute for actions.window snapshot in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 149 |
| test_reveal_raises_the_opened_folder_above_the_browser | actions.focus_window | Attribute for actions.focus window in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_reveal_raises_the_opened_folder_above_the_browser.lambda_150 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 150 |
| test_reveal_raises_the_opened_folder_above_the_browser.lambda_150 | before | Callback parameter for before in test_reveal_raises_the_opened_folder_above_the_browser.lambda_150; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 150 |
| test_reveal_raises_the_opened_folder_above_the_browser | request | Local binding for request in test_reveal_raises_the_opened_folder_above_the_browser; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| test_reveal_keeps_success_when_focus_is_refused | tmp_path | Parameter for tmp path in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 160 |
| test_reveal_keeps_success_when_focus_is_refused | actions | Local binding for actions in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_reveal_keeps_success_when_focus_is_refused | owner | Local binding for owner in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_reveal_keeps_success_when_focus_is_refused | tools | Local binding for tools in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_reveal_keeps_success_when_focus_is_refused | apps | Local binding for apps in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| test_reveal_keeps_success_when_focus_is_refused | opened | Local binding for opened in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 163 |
| test_reveal_keeps_success_when_focus_is_refused | focused | Local binding for focused in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 163 |
| test_reveal_keeps_success_when_focus_is_refused | actions.opener | Attribute for actions.opener in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 164 |
| test_reveal_keeps_success_when_focus_is_refused | actions.window_snapshot | Attribute for actions.window snapshot in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 165 |
| test_reveal_keeps_success_when_focus_is_refused | actions.focus_window | Attribute for actions.focus window in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_reveal_keeps_success_when_focus_is_refused.lambda_166 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 166 |
| test_reveal_keeps_success_when_focus_is_refused.lambda_166 | before | Callback parameter for before in test_reveal_keeps_success_when_focus_is_refused.lambda_166; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 166 |
| test_reveal_keeps_success_when_focus_is_refused.lambda_166.comprehension_166 | _ | Comprehension item for  in test_reveal_keeps_success_when_focus_is_refused.lambda_166.comprehension_166; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 166 |
| test_reveal_keeps_success_when_focus_is_refused | request | Local binding for request in test_reveal_keeps_success_when_focus_is_refused; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 169 |
| test_reveal_opens_when_the_window_snapshot_fails | tmp_path | Parameter for tmp path in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 175 |
| test_reveal_opens_when_the_window_snapshot_fails | actions | Local binding for actions in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_reveal_opens_when_the_window_snapshot_fails | owner | Local binding for owner in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_reveal_opens_when_the_window_snapshot_fails | tools | Local binding for tools in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_reveal_opens_when_the_window_snapshot_fails | apps | Local binding for apps in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_reveal_opens_when_the_window_snapshot_fails | opened | Local binding for opened in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 178 |
| test_reveal_opens_when_the_window_snapshot_fails | focused | Local binding for focused in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 178 |
| test_reveal_opens_when_the_window_snapshot_fails | actions.opener | Attribute for actions.opener in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 179 |
| test_reveal_opens_when_the_window_snapshot_fails | actions.window_snapshot | Attribute for actions.window snapshot in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 180 |
| test_reveal_opens_when_the_window_snapshot_fails.lambda_180.comprehension_180 | _ | Comprehension item for  in test_reveal_opens_when_the_window_snapshot_fails.lambda_180.comprehension_180; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 180 |
| test_reveal_opens_when_the_window_snapshot_fails | actions.focus_window | Attribute for actions.focus window in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 181 |
| test_reveal_opens_when_the_window_snapshot_fails.lambda_181 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 181 |
| test_reveal_opens_when_the_window_snapshot_fails.lambda_181 | before | Callback parameter for before in test_reveal_opens_when_the_window_snapshot_fails.lambda_181; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 181 |
| test_reveal_opens_when_the_window_snapshot_fails | request | Local binding for request in test_reveal_opens_when_the_window_snapshot_fails; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | tmp_path | Parameter for tmp path in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 188 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | actions | Local binding for actions in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | owner | Local binding for owner in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | tools | Local binding for tools in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | apps | Local binding for apps in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | actions.window_snapshot | Attribute for actions.window snapshot in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 191 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | actions.focus_window | Attribute for actions.focus window in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_reveal_reports_an_opener_failure_as_a_validation_error.lambda_192 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 192 |
| test_reveal_reports_an_opener_failure_as_a_validation_error.lambda_192 | before | Callback parameter for before in test_reveal_reports_an_opener_failure_as_a_validation_error.lambda_192; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 192 |
| test_reveal_reports_an_opener_failure_as_a_validation_error.opener | path | Path under validation or an explicitly scoped maintained source path. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 194 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | actions.opener | Attribute for actions.opener in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 198 |
| test_reveal_reports_an_opener_failure_as_a_validation_error | error | Managed resource for error in test_reveal_reports_an_opener_failure_as_a_validation_error; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 199 |
| test_reveal_never_focuses_a_foreign_session | tmp_path | Parameter for tmp path in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 204 |
| test_reveal_never_focuses_a_foreign_session | SessionAccessError | Imported dependency for SessionAccessError in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 206 |
| test_reveal_never_focuses_a_foreign_session | actions | Local binding for actions in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_reveal_never_focuses_a_foreign_session | owner | Local binding for owner in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_reveal_never_focuses_a_foreign_session | tools | Local binding for tools in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_reveal_never_focuses_a_foreign_session | apps | Local binding for apps in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| test_reveal_never_focuses_a_foreign_session | opened | Local binding for opened in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 209 |
| test_reveal_never_focuses_a_foreign_session | focused | Local binding for focused in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 209 |
| test_reveal_never_focuses_a_foreign_session | actions.opener | Attribute for actions.opener in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 210 |
| test_reveal_never_focuses_a_foreign_session | actions.window_snapshot | Attribute for actions.window snapshot in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211 |
| test_reveal_never_focuses_a_foreign_session | actions.focus_window | Attribute for actions.focus window in test_reveal_never_focuses_a_foreign_session; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 212 |
| test_reveal_never_focuses_a_foreign_session.lambda_212 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 212 |
| test_reveal_never_focuses_a_foreign_session.lambda_212 | before | Callback parameter for before in test_reveal_never_focuses_a_foreign_session.lambda_212; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 212 |
| test_reveal_refuses_a_missing_or_aliased_directory | tmp_path | Parameter for tmp path in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 218 |
| test_reveal_refuses_a_missing_or_aliased_directory | actions | Local binding for actions in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_reveal_refuses_a_missing_or_aliased_directory | owner | Local binding for owner in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_reveal_refuses_a_missing_or_aliased_directory | tools | Local binding for tools in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_reveal_refuses_a_missing_or_aliased_directory | apps | Local binding for apps in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 220 |
| test_reveal_refuses_a_missing_or_aliased_directory | opened | Local binding for opened in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 221 |
| test_reveal_refuses_a_missing_or_aliased_directory | actions.opener | Attribute for actions.opener in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 222 |
| test_reveal_refuses_a_missing_or_aliased_directory | request | Local binding for request in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 223 |
| test_reveal_refuses_a_missing_or_aliased_directory | owner.controller.security.TOOLS_ROOT_DIR | Attribute for owner.controller.security.TOOLS ROOT DIR in test_reveal_refuses_a_missing_or_aliased_directory; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| test_cancellation_does_not_remove_files | tmp_path | Parameter for tmp path in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 230 |
| test_cancellation_does_not_remove_files | actions | Local binding for actions in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 232 |
| test_cancellation_does_not_remove_files | owner | Local binding for owner in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 232 |
| test_cancellation_does_not_remove_files | tools | Local binding for tools in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 232 |
| test_cancellation_does_not_remove_files | apps | Local binding for apps in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 232 |
| test_cancellation_does_not_remove_files | request | Local binding for request in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| test_cancellation_does_not_remove_files | message | Local binding for message in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| test_cancellation_does_not_remove_files | confirmation | Local binding for confirmation in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| test_cancellation_does_not_remove_files | token | Local binding for token in test_cancellation_does_not_remove_files; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | tmp_path | Parameter for tmp path in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 244 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | actions | Local binding for actions in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | owner | Local binding for owner in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | tools | Local binding for tools in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | apps | Local binding for apps in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of setup; see its callable contract | Enclosing invocation or class/instance lifetime | 246 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | request | Local binding for request in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | _ | Local binding for  in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | confirmation | Local binding for confirmation in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_confirmation_cannot_cross_sessions_or_be_replayed | token | Local binding for token in test_confirmation_cannot_cross_sessions_or_be_replayed; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
