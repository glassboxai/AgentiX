# Reference for src/agentix/ui/tool_repair.py

Gradio editors for the owning session's explicitly rejected tool proposal.

Source fingerprint: 2e25e0da814c19e3fda309e83c985afc0ff72634a971d3998ffb316ba34abe99

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build_tool_repair

Keep source/tests editable while retaining ordinary human acceptance controls.

Kind: callable. Declared return: None. Source line: 6.

### build_tool_repair.load_draft

Display a safe fixed error for absent/stale owner proposals.

Kind: callable. Declared return: Not declared / class. Source line: 33.

### build_tool_repair.resume

Dispatch explicitly; model/native work runs in the existing owner worker.

Kind: callable. Declared return: Not declared / class. Source line: 42.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| build_tool_repair | gr | Parameter for gr in build_tool_repair; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 6 |
| build_tool_repair | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 6 |
| build_tool_repair | bind | Parameter for bind in build_tool_repair; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 6 |
| build_tool_repair | session_state | Parameter for session state in build_tool_repair; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 6 |
| build_tool_repair | status | Local binding for status in build_tool_repair; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 9 |
| build_tool_repair | load | Local binding for load in build_tool_repair; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| build_tool_repair | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 14 |
| build_tool_repair | revision | Local binding for revision in build_tool_repair; use the enclosing contract and type below. | Return type of State; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| build_tool_repair | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| build_tool_repair | tests | Optional unittest source snapshot; child-authored success remains provisional. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| build_tool_repair | restart | Local binding for restart in build_tool_repair; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| build_tool_repair.load_draft | token | Parameter for token in build_tool_repair.load_draft; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 33 |
| build_tool_repair.load_draft | request | Parameter for request in build_tool_repair.load_draft; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| build_tool_repair.load_draft | error | Caught exception for error in build_tool_repair.load_draft; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 37 |
| build_tool_repair.resume | revision | Parameter for revision in build_tool_repair.resume; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 42 |
| build_tool_repair.resume | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 42 |
| build_tool_repair.resume | tests | Optional unittest source snapshot; child-authored success remains provisional. | str | Enclosing invocation or class/instance lifetime | 42 |
| build_tool_repair.resume | token | Parameter for token in build_tool_repair.resume; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 42 |
| build_tool_repair.resume | request | Parameter for request in build_tool_repair.resume; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 42 |
| build_tool_repair.resume | error | Caught exception for error in build_tool_repair.resume; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 46 |
