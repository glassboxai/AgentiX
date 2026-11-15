# Reference for src/agentix/ui/chathelper.py

Floating Gradio code-help view; movement/resize behavior lives in chathelper.js.

Source fingerprint: f9b95b462e42d651bed640f3be722039ea5c638806e60a00101dfea164174234

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build_chathelper

Build one session-owned read-only helper, initially hidden by maintained CSS.

Kind: callable. Declared return: Not declared / class. Source line: 6.

### build_chathelper.ask

Use fixed safe errors; vendor messages, code and credentials are never echoed.

Kind: callable. Declared return: Not declared / class. Source line: 29.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ChatHelperBackend | Imported dependency for ChatHelperBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| build_chathelper | gr | Parameter for gr in build_chathelper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | backend | Injected framework/execution provider; callers determine the required protocol. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | bind | Parameter for bind in build_chathelper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | selected_file | Parameter for selected file in build_chathelper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | session_state | Parameter for session state in build_chathelper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | panes | Parameter for panes in build_chathelper; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 6 |
| build_chathelper | helper | Local binding for helper in build_chathelper; use the enclosing contract and type below. | Return type of ChatHelperBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 8 |
| build_chathelper | pane | Local binding for pane in build_chathelper; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| build_chathelper | transcript | Local binding for transcript in build_chathelper; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| build_chathelper | question | Local binding for question in build_chathelper; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| build_chathelper | send | Local binding for send in build_chathelper; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| build_chathelper | status | Local binding for status in build_chathelper; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| build_chathelper.ask | pane | Parameter for pane in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | selected | Parameter for selected in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | code | Source snapshot passed through approval, syntax checks and isolated staging. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | widget | Parameter for widget in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | tool_tests | Parameter for tool tests in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | widget_tests | Parameter for widget tests in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | question | Parameter for question in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | token | Parameter for token in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | request | Parameter for request in build_chathelper.ask; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| build_chathelper.ask | buffers | Local binding for buffers in build_chathelper.ask; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 32 |
| build_chathelper.ask | text | Local binding for text in build_chathelper.ask; use the enclosing contract and type below. | Return type of ask; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| build_chathelper.ask | cleared | Local binding for cleared in build_chathelper.ask; use the enclosing contract and type below. | Return type of ask; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| build_chathelper.ask | owned | Local binding for owned in build_chathelper.ask; use the enclosing contract and type below. | Return type of ask; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
