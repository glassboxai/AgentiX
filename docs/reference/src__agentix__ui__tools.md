# Reference for src/agentix/ui/tools.py

Tools tab Gradio controls and bindings; business behavior lives in agentix.controllers.tools.

Source fingerprint: c7f18565701f58fbf7f5fec6224c884bfcf5ca0be61a4b0cc6570493f4bfa5e6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build_tools_frontend

Render the conversation plus one collapsible right sidebar for catalog and review.

Kind: callable. Declared return: None. Source line: 20.

### build_tools_frontend.reseal_all

Rebind intact approvals under the current policy; never execute here.

Kind: callable. Declared return: Not declared / class. Source line: 94.

### build_tools_frontend.refresh_tools

Refresh selectable installed tool IDs without importing source.

Kind: callable. Declared return: Not declared / class. Source line: 110.

### build_tools_frontend.reveal_tools_folder

Open this owner's installed tools folder; no browser path is accepted.

Kind: callable. Declared return: Not declared / class. Source line: 126.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | CHATBOT_HEIGHT_PIXELS | Module binding for CHATBOT HEIGHT PIXELS in module; use the enclosing contract and type below. | int | Module/process lifetime | 5 |
| module | QUERY_INPUT_LINES | Module binding for QUERY INPUT LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 6 |
| module | QUERY_INPUT_SCALE | Module binding for QUERY INPUT SCALE in module; use the enclosing contract and type below. | int | Module/process lifetime | 7 |
| module | SEND_BUTTON_MIN_WIDTH | Module binding for SEND BUTTON MIN WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 8 |
| module | CHAT_COLUMN_SCALE | Module binding for CHAT COLUMN SCALE in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | TOOLS_SIDEBAR_WIDTH_PIXELS | Module binding for TOOLS SIDEBAR WIDTH PIXELS in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| module | APPROVAL_PREVIEW_LINES | Module binding for APPROVAL PREVIEW LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | STATUS_TIMER_SECONDS | Module binding for STATUS TIMER SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 12 |
| module | REFRESH_OUTPUT_COUNT | Module binding for REFRESH OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| module | SUBMIT_OUTPUT_COUNT | Module binding for SUBMIT OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 14 |
| module | READINESS_OUTPUT_COUNT | Module binding for READINESS OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 15 |
| module | POLL_OUTPUT_COUNT | Module binding for POLL OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 16 |
| module | VALIDATION_OUTPUT_COUNT | Module binding for VALIDATION OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 17 |
| build_tools_frontend | gr | Parameter for gr in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 21 |
| build_tools_frontend | callbacks | Parameter for callbacks in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_tools_frontend | bind | Parameter for bind in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 23 |
| build_tools_frontend | session_state | Parameter for session state in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 24 |
| build_tools_frontend | request_state | Parameter for request state in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 25 |
| build_tools_frontend | progress | Parameter for progress in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 26 |
| build_tools_frontend | maintenance | Parameter for maintenance in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 27 |
| build_tools_frontend | repair_backend | Parameter for repair backend in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 28 |
| build_tools_frontend | dialog | Parameter for dialog in build_tools_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 29, 38 |
| build_tools_frontend | operation | Local binding for operation in build_tools_frontend; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| build_tools_frontend | MessageDialog | Imported dependency for MessageDialog in build_tools_frontend; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 36 |
| build_tools_frontend | chatbot | Local binding for chatbot in build_tools_frontend; use the enclosing contract and type below. | Return type of Chatbot; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| build_tools_frontend | msg_input | Local binding for msg input in build_tools_frontend; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| build_tools_frontend | submit_btn | Local binding for submit btn in build_tools_frontend; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| build_tools_frontend | reveal_tools | Local binding for reveal tools in build_tools_frontend; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| build_tools_frontend | catalog_display | Local binding for catalog display in build_tools_frontend; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| build_tools_frontend | build_delete_controls | Imported dependency for build delete controls in build_tools_frontend; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 82 |
| build_tools_frontend | reseal_tools | Local binding for reseal tools in build_tools_frontend; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| build_tools_frontend | reseal_status | Local binding for reseal status in build_tools_frontend; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| build_tools_frontend | selected_tool | Local binding for selected tool in build_tools_frontend; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| build_tools_frontend.reseal_all | token | Parameter for token in build_tools_frontend.reseal_all; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 94 |
| build_tools_frontend.reseal_all | request | Parameter for request in build_tools_frontend.reseal_all; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 94 |
| build_tools_frontend.reseal_all | message | Local binding for message in build_tools_frontend.reseal_all; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| build_tools_frontend.reseal_all | owned | Local binding for owned in build_tools_frontend.reseal_all; use the enclosing contract and type below. | Return type of reseal_tools; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| build_tools_frontend.refresh_tools | selected | Parameter for selected in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 110 |
| build_tools_frontend.refresh_tools | token | Parameter for token in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 110 |
| build_tools_frontend.refresh_tools | request | Parameter for request in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 110 |
| build_tools_frontend.refresh_tools | choices | Local binding for choices in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | Return type of choices; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| build_tools_frontend.refresh_tools | owned | Local binding for owned in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | Return type of choices; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| build_tools_frontend.refresh_tools | names | Local binding for names in build_tools_frontend.refresh_tools; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 113 |
| build_tools_frontend.refresh_tools.comprehension_113 | _ | Comprehension item for  in build_tools_frontend.refresh_tools.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| build_tools_frontend.refresh_tools.comprehension_113 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| build_tools_frontend.reveal_tools_folder | token | Parameter for token in build_tools_frontend.reveal_tools_folder; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 126 |
| build_tools_frontend.reveal_tools_folder | request | Parameter for request in build_tools_frontend.reveal_tools_folder; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 126 |
| build_tools_frontend | validation_display | Local binding for validation display in build_tools_frontend; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| build_tools_frontend | auto_approve_check | Local binding for auto approve check in build_tools_frontend; use the enclosing contract and type below. | Return type of Checkbox; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| build_tools_frontend | approval_group | Managed resource for approval group in build_tools_frontend; use the enclosing contract and type below. | Return type of Column; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 149 |
| build_tools_frontend | pending_info | Local binding for pending info in build_tools_frontend; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| build_tools_frontend | preview_box | Local binding for preview box in build_tools_frontend; use the enclosing contract and type below. | Return type of TextArea; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| build_tools_frontend | approval_validation | Local binding for approval validation in build_tools_frontend; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| build_tools_frontend | approve_btn | Local binding for approve btn in build_tools_frontend; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| build_tools_frontend | reject_btn | Local binding for reject btn in build_tools_frontend; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| build_tools_frontend | build_tool_repair | Imported dependency for build tool repair in build_tools_frontend; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 167 |
| build_tools_frontend | status_timer | Local binding for status timer in build_tools_frontend; use the enclosing contract and type below. | Return type of Timer; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
| build_tools_frontend | poll_event | Local binding for poll event in build_tools_frontend; use the enclosing contract and type below. | Return type of tick; see its callable contract | Enclosing invocation or class/instance lifetime | 207 |
