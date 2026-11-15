# Reference for src/agentix/controllers/tool_controller.py

UI-independent workflow callbacks with injected application dependencies.

Source fingerprint: 03402ab12bb0ea6cb5c75b149630762800e4e893b66fec38a9234e53b171cbf3

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### format_thoughts_markdown

Render the existing activity accordion, preserving open/closed markup.

Kind: callable. Declared return: str. Source line: 27.

### UiController

Own one session's state, activity and callbacks without browser widgets.

Kind: class. Declared return: Not declared / class. Source line: 55.

### UiController.__init__

Connect services; stdout interception is installed only by startup.

Kind: callable. Declared return: None. Source line: 58.

### UiController.validation_status

Render owned host verdicts as escaped text, independently of model replies.

Kind: callable. Declared return: str. Source line: 89.

### UiController.approval_readiness

Return the review control state using the maintained acceptance parser.

This only guides the browser. ``on_approve`` and the acceptance evaluator
still validate the exact text and request identity at the security boundary.

Kind: callable. Declared return: tuple[Any, str]. Source line: 96.

### UiController.process_user_query

Atomically accept one workflow for this session.

Kind: callable. Declared return: tuple[str, list[dict[str, str]]]. Source line: 117.

### UiController._process_user_query

Submit a nonblank query to one daemon worker and return chat updates.

Busy submissions retain the existing wait-message behavior. Worker errors
are captured into state and rendered by polling, rather than propagated
across the thread boundary. The registry gives each owner a separate controller.

Kind: callable. Declared return: tuple[str, list[dict[str, str]]]. Source line: 126.

### UiController._process_user_query.worker

Run with explicit owner/activity context and synchronized state updates.

Kind: callable. Declared return: None. Source line: 176.

### UiController.poll_system_status

Read one coherent session snapshot without overwriting in-progress edits.

Kind: callable. Declared return: tuple[list[dict[str, str]], Any, str, Any, str]. Source line: 204.

### UiController.poll_with_request

Return the UI snapshot and exact request ID displayed in that snapshot.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 209.

### UiController._poll_system_status

Polled every second by gr.Timer:
1. Updates live thoughts and final answer.
2. Shows approval card and loads text ONCE (so user edits are never overwritten by timer).
3. Refreshes tools catalog.

Kind: callable. Declared return: tuple[list[dict[str, str]], Any, str, Any, str]. Source line: 214.

### UiController.on_approve

Approve only the ID sent with the displayed editor snapshot.

Kind: callable. Declared return: bool. Source line: 316.

### UiController.on_reject

Deny the exact request and retain its proposal as an unapproved repair draft.

Kind: callable. Declared return: bool. Source line: 323.

### UiController.on_toggle_auto_approve

Change only this owner's setting; do not resolve pending requests.

Kind: callable. Declared return: None. Source line: 341.

### UiController.profile_action

Serialize profile actions with this owner's execution and review state.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 350.

### UiController.configure_model

Change only this idle owner; preserve the runtime if configuration fails.

Kind: callable. Declared return: str. Source line: 438.

### UiController.close

Stop accepting callbacks and cancel pending/future owner writes.

Kind: callable. Declared return: None. Source line: 449.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | html | Imported dependency for html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | deepcopy | Imported dependency for deepcopy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ExecutionState | Imported dependency for ExecutionState in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ProfileError | Imported dependency for ProfileError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | redact | Imported dependency for redact in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SecurityViolationError | Imported dependency for SecurityViolationError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | format_catalog | Imported dependency for format catalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | format_result | Imported dependency for format result in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | render_validation | Imported dependency for render validation in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 20 |
| module | MAX_QUERY_CHARACTERS | Module binding for MAX QUERY CHARACTERS in module; use the enclosing contract and type below. | int | Module/process lifetime | 22 |
| module | LIVE_LOG_TAIL_LINES | Module binding for LIVE LOG TAIL LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 23 |
| module | FINAL_LOG_TAIL_LINES | Module binding for FINAL LOG TAIL LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 24 |
| format_thoughts_markdown | thoughts_text | Parameter for thoughts text in format_thoughts_markdown; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 27, 38 |
| format_thoughts_markdown | is_open | Parameter for is open in format_thoughts_markdown; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 27 |
| format_thoughts_markdown | lines | Local binding for lines in format_thoughts_markdown; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 30 |
| format_thoughts_markdown | line | Current source or text line scoped to parsing; no implicit execution occurs. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 31, 34, 36 |
| format_thoughts_markdown | trimmed | Local binding for trimmed in format_thoughts_markdown; use the enclosing contract and type below. | Return type of lstrip; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| format_thoughts_markdown | open_attr | Local binding for open attr in format_thoughts_markdown; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| format_thoughts_markdown | status_label | Local binding for status label in format_thoughts_markdown; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| format_thoughts_markdown | content | Artifact or review text whose encoding, size and approval state must be checked. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| UiController.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 59 |
| UiController.__init__ | run_system | Parameter for run system in UiController.__init__; use the enclosing contract and type below. | Callable[[str], str] | Enclosing invocation or class/instance lifetime | 60 |
| UiController.__init__ | catalog | Parameter for catalog in UiController.__init__; use the enclosing contract and type below. | Callable[[], str] | Enclosing invocation or class/instance lifetime | 61 |
| UiController.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 62 |
| UiController.__init__ | update | Parameter for update in UiController.__init__; use the enclosing contract and type below. | Callable[..., Any] | Enclosing invocation or class/instance lifetime | 63 |
| UiController.__init__ | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | ExecutionState &#124; None | Enclosing invocation or class/instance lifetime | 64 |
| UiController.__init__ | capture | Parameter for capture in UiController.__init__; use the enclosing contract and type below. | ConsoleThoughtsCapture &#124; None | Enclosing invocation or class/instance lifetime | 65 |
| UiController.__init__ | validation | Parameter for validation in UiController.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 66 |
| UiController.__init__ | tool_operations | Parameter for tool operations in UiController.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 67 |
| UiController.__init__ | self.run_system | Attribute for run system in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| UiController.__init__ | self.get_installed_tools_catalog | Attribute for get installed tools catalog in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 71 |
| UiController.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| UiController.__init__ | self._lock | Attribute for lock in UiController.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| UiController.__init__ | self._closed | Attribute for closed in UiController.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 74 |
| UiController.__init__ | self.application_cleanup | Attribute for application cleanup in UiController.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 75 |
| UiController.__init__ | self.update | Attribute for update in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| UiController.__init__ | self.state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| UiController.__init__ | self.captured_stdout | Attribute for captured stdout in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| UiController.__init__ | self.security.activity_capture | Attribute for security.activity capture in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 83 |
| UiController.__init__ | self.validation | Attribute for validation in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 84 |
| UiController.__init__ | self.tool_operations | Attribute for tool operations in UiController.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| UiController.__init__ | self.model_configuration | Attribute for model configuration in UiController.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 86 |
| UiController.__init__ | self._last_profile_save_error | Attribute for last profile save error in UiController.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 87 |
| UiController.validation_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 89 |
| UiController.validation_status | status | Local binding for status in UiController.validation_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 91 |
| UiController.approval_readiness | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| UiController.approval_readiness | text | Parameter for text in UiController.approval_readiness; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 96 |
| UiController.approval_readiness | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str &#124; None | Enclosing invocation or class/instance lifetime | 96 |
| UiController.approval_readiness | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| UiController.approval_readiness | parse_contract | Imported dependency for parse contract in UiController.approval_readiness; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 109 |
| UiController.process_user_query | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| UiController.process_user_query | message | Parameter for message in UiController.process_user_query; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 118 |
| UiController.process_user_query | operation | Parameter for operation in UiController.process_user_query; use the enclosing contract and type below. | Callable[[str], str] &#124; None | Enclosing invocation or class/instance lifetime | 118 |
| UiController._process_user_query | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 127 |
| UiController._process_user_query | message | Parameter for message in UiController._process_user_query; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 127 |
| UiController._process_user_query | operation | Parameter for operation in UiController._process_user_query; use the enclosing contract and type below. | Callable[[str], str] &#124; None | Enclosing invocation or class/instance lifetime | 127 |
| UiController._process_user_query | clean_msg | Local binding for clean msg in UiController._process_user_query; use the enclosing contract and type below. | Return type of redact; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| UiController._process_user_query | self.state.is_running | Attribute for state.is running in UiController._process_user_query; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 152 |
| UiController._process_user_query | self.state.operation_id | Attribute for state.operation id in UiController._process_user_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 153 |
| UiController._process_user_query | self.security.operation_id | Attribute for security.operation id in UiController._process_user_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 154 |
| UiController._process_user_query | self.state.last_response | Attribute for state.last response in UiController._process_user_query; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 155 |
| UiController._process_user_query | self.state.error_message | Attribute for state.error message in UiController._process_user_query; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 156 |
| UiController._process_user_query | self.state.last_displayed_filepath | Attribute for state.last displayed filepath in UiController._process_user_query; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 157 |
| UiController._process_user_query | self.state.last_displayed_request_id | Attribute for state.last displayed request id in UiController._process_user_query; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 158 |
| UiController._process_user_query | initial_thoughts | Local binding for initial thoughts in UiController._process_user_query; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| UiController._process_user_query | self.state.active_message_index | Attribute for state.active message index in UiController._process_user_query; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 174 |
| UiController._process_user_query.worker | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| UiController._process_user_query.worker | self.state.last_response | Attribute for state.last response in UiController._process_user_query.worker; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 185 |
| UiController._process_user_query.worker | exc | Caught exception for exc in UiController._process_user_query.worker; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 190 |
| UiController._process_user_query.worker | self.state.error_message | Attribute for state.error message in UiController._process_user_query.worker; use the enclosing contract and type below. | Return type of redact; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| UiController._process_user_query.worker | self.state.is_running | Attribute for state.is running in UiController._process_user_query.worker; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 196 |
| UiController._process_user_query | thread | Local binding for thread in UiController._process_user_query; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| UiController.poll_system_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 204 |
| UiController.poll_with_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 209 |
| UiController._poll_system_status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 214 |
| UiController._poll_system_status | index | Local binding for index in UiController._poll_system_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 222, 224 |
| UiController._poll_system_status | last_item | Local binding for last item in UiController._poll_system_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 230 |
| UiController._poll_system_status | live_logs | Local binding for live logs in UiController._poll_system_status; use the enclosing contract and type below. | Return type of get_logs; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| UiController._poll_system_status | thoughts_box | Local binding for thoughts box in UiController._poll_system_status; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| UiController._poll_system_status | final_logs | Local binding for final logs in UiController._poll_system_status; use the enclosing contract and type below. | Return type of get_logs; see its callable contract | Enclosing invocation or class/instance lifetime | 242 |
| UiController._poll_system_status | collapsed_thoughts | Local binding for collapsed thoughts in UiController._poll_system_status; use the enclosing contract and type below. | Return type of format_thoughts_markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 243 |
| UiController._poll_system_status | query | Original user request or a trusted test query; avoid payload logging by default. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 250 |
| UiController._poll_system_status.comprehension_251 | item | Comprehension item for item in UiController._poll_system_status.comprehension_251; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 253 |
| UiController._poll_system_status | answer | Local binding for answer in UiController._poll_system_status; use the enclosing contract and type below. | Return type of format_result; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| UiController._poll_system_status | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| UiController._poll_system_status | approval_visibility | Local binding for approval visibility in UiController._poll_system_status; use the enclosing contract and type below. | Return type of update; see its callable contract | Enclosing invocation or class/instance lifetime | 265, 301 |
| UiController._poll_system_status | pending_file_text | Local binding for pending file text in UiController._poll_system_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 266, 271, 284, 302 |
| UiController._poll_system_status | context | Local binding for context in UiController._poll_system_status; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 270 |
| UiController._poll_system_status | self.state.last_displayed_filepath | Attribute for state.last displayed filepath in UiController._poll_system_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 292, 299 |
| UiController._poll_system_status | self.state.last_displayed_request_id | Attribute for state.last displayed request id in UiController._poll_system_status; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 293, 300 |
| UiController._poll_system_status | preview_update | Local binding for preview update in UiController._poll_system_status; use the enclosing contract and type below. | Return type of update; see its callable contract | Enclosing invocation or class/instance lifetime | 294, 297, 303 |
| UiController._poll_system_status | catalog_text | Local binding for catalog text in UiController._poll_system_status; use the enclosing contract and type below. | Return type of format_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 306 |
| UiController.on_approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 316 |
| UiController.on_approve | edited_text | Parameter for edited text in UiController.on_approve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 316 |
| UiController.on_approve | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str &#124; None | Enclosing invocation or class/instance lifetime | 316 |
| UiController.on_reject | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 323 |
| UiController.on_reject | request_id | Displayed approval identity checked against the owner and expiry; not a secret. | str &#124; None | Enclosing invocation or class/instance lifetime | 323 |
| UiController.on_reject | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 326 |
| UiController.on_reject | resolved | Local binding for resolved in UiController.on_reject; use the enclosing contract and type below. | Return type of resolve_pending_request; see its callable contract | Enclosing invocation or class/instance lifetime | 327 |
| UiController.on_reject | capture_rejection | Imported dependency for capture rejection in UiController.on_reject; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 331 |
| UiController.on_reject | draft | Local binding for draft in UiController.on_reject; use the enclosing contract and type below. | Return type of capture_rejection; see its callable contract | Enclosing invocation or class/instance lifetime | 334 |
| UiController.on_reject | self._rejected_tool | Attribute for rejected tool in UiController.on_reject; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 336 |
| UiController.on_toggle_auto_approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 341 |
| UiController.on_toggle_auto_approve | is_checked | Parameter for is checked in UiController.on_toggle_auto_approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 341 |
| UiController.on_toggle_auto_approve | self.security.auto_approve | Attribute for security.auto approve in UiController.on_toggle_auto_approve; use the enclosing contract and type below. | Return type of bool; see its callable contract | Enclosing invocation or class/instance lifetime | 346 |
| UiController.profile_action | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 351 |
| UiController.profile_action | action | Parameter for action in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 352 |
| UiController.profile_action | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 353 |
| UiController.profile_action | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 354, 372, 376, 388, 399 |
| UiController.profile_action | provider | Parameter for provider in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 355, 372, 376, 399 |
| UiController.profile_action | model | Parameter for model in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 356, 372, 376, 399 |
| UiController.profile_action | endpoint | Parameter for endpoint in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 357, 372, 376, 399 |
| UiController.profile_action | key | Parameter for key in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 358 |
| UiController.profile_action | configuration | Local binding for configuration in UiController.profile_action; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 363 |
| UiController.profile_action | consent | Local binding for consent in UiController.profile_action; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 366, 423 |
| UiController.profile_action | record | Local binding for record in UiController.profile_action; use the enclosing contract and type below. | Return type of select_saved; see its callable contract | Enclosing invocation or class/instance lifetime | 370, 397 |
| UiController.profile_action.comprehension_372 | field | Comprehension item for field in UiController.profile_action.comprehension_372; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 373 |
| UiController.profile_action | status | Local binding for status in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 382, 384, 387, 390, 392, 403, 431, 433 |
| UiController.profile_action | self._last_profile_save_error | Attribute for last profile save error in UiController.profile_action; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 385, 435 |
| UiController.profile_action | saved | Local binding for saved in UiController.profile_action; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 395 |
| UiController.profile_action.comprehension_395 | choice | Comprehension item for choice in UiController.profile_action.comprehension_395; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 395 |
| UiController.profile_action.comprehension_399 | field | Comprehension item for field in UiController.profile_action.comprehension_399; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 401 |
| UiController.profile_action | choices | Local binding for choices in UiController.profile_action; use the enclosing contract and type below. | Return type of saved_choices; see its callable contract | Enclosing invocation or class/instance lifetime | 409, 423, 426 |
| UiController.profile_action | selected | Local binding for selected in UiController.profile_action; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 410, 423, 427 |
| UiController.profile_action | error | Caught exception for error in UiController.profile_action; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 411 |
| UiController.profile_action | trace | Local binding for trace in UiController.profile_action; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 412, 414 |
| UiController.configure_model | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | provider | Parameter for provider in UiController.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | model | Parameter for model in UiController.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | endpoint | Parameter for endpoint in UiController.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | key | Parameter for key in UiController.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | consent | Parameter for consent in UiController.configure_model; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 439 |
| UiController.configure_model | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of configure; see its callable contract | Enclosing invocation or class/instance lifetime | 445 |
| UiController.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 449 |
| UiController.close | self._closed | Attribute for closed in UiController.close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 452 |
| UiController.close | error | Caught exception for error in UiController.close; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 459 |
