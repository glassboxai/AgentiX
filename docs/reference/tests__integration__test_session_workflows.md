# Reference for tests/integration/test_session_workflows.py

Exercise actual owner controllers/callbacks with deterministic parallel workers.

Source fingerprint: 7ab13226ad53d70ab1160ba4a84df7fe9a5a6caa8b313c15cde5a5a895b1fcdd

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity

Verify parallel browser callbacks do not share history approvals or activity.

Kind: callable. Declared return: Not declared / class. Source line: 13.

### test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread

Provide tracked thread for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create

Provide create for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 30.

### test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create.workflow

Provide workflow for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval

Verify same filepath new request refreshes editor and rejects old approval.

Kind: callable. Declared return: Not declared / class. Source line: 73.

### test_busy_submission_cannot_steal_active_answer

Verify busy submission cannot steal active answer.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### test_tool_adapter_restores_owner_context_in_provider_threads

Verify tool adapter restores owner context in provider threads.

Kind: callable. Declared return: Not declared / class. Source line: 113.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | SecurityManager | Imported dependency for SecurityManager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | UiController | Imported dependency for UiController in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | SessionAccessError | Imported dependency for SessionAccessError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SessionCallbacks | Imported dependency for SessionCallbacks in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | tmp_path | Parameter for tmp path in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | monkeypatch | Parameter for monkeypatch in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | release | Local binding for release in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | active | Local binding for active in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of Barrier; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | workers | Local binding for workers in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 19 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | original_thread | Local binding for original thread in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread | args | Parameter for args in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread | thread | Local binding for thread in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.tracked_thread; use the enclosing contract and type below. | Return type of original_thread; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create | token | Parameter for token in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create | security.TOOLS_ROOT_DIR | Attribute for security.TOOLS ROOT DIR in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create | controller | Local binding for controller in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create; use the enclosing contract and type below. | Return type of UiController; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create | controller.state.session_id | Attribute for controller.state.session id in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity.create; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | registry | Local binding for registry in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | callbacks | Local binding for callbacks in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of SessionCallbacks; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | owner_a | Local binding for owner a in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | owner_b | Local binding for owner b in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 47 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | _ | Local binding for  in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of submit; see its callable contract | Enclosing invocation or class/instance lifetime | 51, 52 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | token_a | Local binding for token a in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of submit; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | token_b | Local binding for token b in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Return type of submit; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | alice | Local binding for alice in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 56 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | bob | Local binding for bob in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 56 |
| test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity | worker | Loop item for worker in test_parallel_browser_callbacks_do_not_share_history_approvals_or_activity; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 65 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | system | Parameter for system in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | boundary | Local binding for boundary in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | boundary.owner_id | Attribute for boundary.owner id in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 76 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | boundary._pending_request | Attribute for boundary. pending request in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 77, 86 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | boundary._resolved | Attribute for boundary. resolved in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 87 |
| test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval | snapshot | Local binding for snapshot in test_same_filepath_new_request_refreshes_editor_and_rejects_old_approval; use the enclosing contract and type below. | Return type of poll_with_request; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_busy_submission_cannot_steal_active_answer | system | Parameter for system in test_busy_submission_cannot_steal_active_answer; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_busy_submission_cannot_steal_active_answer | monkeypatch | Parameter for monkeypatch in test_busy_submission_cannot_steal_active_answer; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_busy_submission_cannot_steal_active_answer | targets | Local binding for targets in test_busy_submission_cannot_steal_active_answer; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 98 |
| test_busy_submission_cannot_steal_active_answer.lambda_102 | target | Callback parameter for target in test_busy_submission_cannot_steal_active_answer.lambda_102; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 102 |
| test_busy_submission_cannot_steal_active_answer.lambda_102 | daemon | Callback parameter for daemon in test_busy_submission_cannot_steal_active_answer.lambda_102; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 102 |
| test_busy_submission_cannot_steal_active_answer.lambda_104 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 104 |
| test_busy_submission_cannot_steal_active_answer | history | Local binding for history in test_busy_submission_cannot_steal_active_answer; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_tool_adapter_restores_owner_context_in_provider_threads | system | Parameter for system in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 113 |
| test_tool_adapter_restores_owner_context_in_provider_threads | caplog | Parameter for caplog in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 113 |
| test_tool_adapter_restores_owner_context_in_provider_threads | register_tools | Imported dependency for register tools in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 115 |
| test_tool_adapter_restores_owner_context_in_provider_threads | system.security.owner_id | Attribute for system.security.owner id in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 117 |
| test_tool_adapter_restores_owner_context_in_provider_threads | system.security.operation_id | Attribute for system.security.operation id in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 118 |
| test_tool_adapter_restores_owner_context_in_provider_threads | system.security.auto_approve | Attribute for system.security.auto approve in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 119 |
| test_tool_adapter_restores_owner_context_in_provider_threads | tools | Local binding for tools in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | Return type of register_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| test_tool_adapter_restores_owner_context_in_provider_threads.lambda_120 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 120 |
| test_tool_adapter_restores_owner_context_in_provider_threads.lambda_120.lambda_120 | fn | Callback parameter for fn in test_tool_adapter_restores_owner_context_in_provider_threads.lambda_120.lambda_120; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 120 |
| test_tool_adapter_restores_owner_context_in_provider_threads | results | Local binding for results in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 121 |
| test_tool_adapter_restores_owner_context_in_provider_threads | worker | Local binding for worker in test_tool_adapter_restores_owner_context_in_provider_threads; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
