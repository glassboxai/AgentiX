# Reference for src/agentix/ui/catalog_actions.py

Reusable explicit confirmation controls for permanent catalog deletion.

Source fingerprint: 68040c3a3354c4f88a83ea0f73f008b811deb387584db2736b27a54d8eec51df

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build_delete_controls

Render prepare/confirm/cancel; all authority remains in the owner controller.

Kind: callable. Declared return: None. Source line: 6.

### build_delete_controls.prepare

Display dependency failures without exposing native/storage exception bodies.

Kind: callable. Declared return: Not declared / class. Source line: 41.

### build_delete_controls.commit

Clear selection after success; failed/stale requests require a new confirmation.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### build_delete_controls.dismiss

Cancel without granting deletion even when a prompt became stale.

Kind: callable. Declared return: Not declared / class. Source line: 87.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| build_delete_controls | gr | Parameter for gr in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 7 |
| build_delete_controls | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 8 |
| build_delete_controls | bind | Parameter for bind in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 9 |
| build_delete_controls | kind | Parameter for kind in build_delete_controls; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 10 |
| build_delete_controls | selected | Parameter for selected in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 11 |
| build_delete_controls | session_state | Parameter for session state in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 12 |
| build_delete_controls | status | Parameter for status in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 13 |
| build_delete_controls | dialog | Parameter for dialog in build_delete_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 14, 20 |
| build_delete_controls | MessageDialog | Imported dependency for MessageDialog in build_delete_controls; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| build_delete_controls | prefix | Local binding for prefix in build_delete_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| build_delete_controls | select_message | Local binding for select message in build_delete_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| build_delete_controls | delete | Local binding for delete in build_delete_controls; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| build_delete_controls | notice | Local binding for notice in build_delete_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| build_delete_controls | nonce | Local binding for nonce in build_delete_controls; use the enclosing contract and type below. | Return type of State; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| build_delete_controls | panel | Managed resource for panel in build_delete_controls; use the enclosing contract and type below. | Return type of Column; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 33 |
| build_delete_controls | prompt | Local binding for prompt in build_delete_controls; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| build_delete_controls | confirm | Local binding for confirm in build_delete_controls; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| build_delete_controls | cancel | Local binding for cancel in build_delete_controls; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| build_delete_controls.prepare | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 41 |
| build_delete_controls.prepare | token | Parameter for token in build_delete_controls.prepare; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 41 |
| build_delete_controls.prepare | request | Parameter for request in build_delete_controls.prepare; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 41 |
| build_delete_controls.prepare | message | Local binding for message in build_delete_controls.prepare; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 53, 58 |
| build_delete_controls.prepare | confirmation | Local binding for confirmation in build_delete_controls.prepare; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| build_delete_controls.prepare | owned | Local binding for owned in build_delete_controls.prepare; use the enclosing contract and type below. | Return type of prepare; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| build_delete_controls.prepare | error | Caught exception for error in build_delete_controls.prepare; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 55 |
| build_delete_controls.commit | confirmation | Parameter for confirmation in build_delete_controls.commit; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 61 |
| build_delete_controls.commit | token | Parameter for token in build_delete_controls.commit; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 61 |
| build_delete_controls.commit | request | Parameter for request in build_delete_controls.commit; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 61 |
| build_delete_controls.commit | message | Local binding for message in build_delete_controls.commit; use the enclosing contract and type below. | Return type of confirm; see its callable contract | Enclosing invocation or class/instance lifetime | 64, 84 |
| build_delete_controls.commit | owned | Local binding for owned in build_delete_controls.commit; use the enclosing contract and type below. | Return type of confirm; see its callable contract | Enclosing invocation or class/instance lifetime | 64, 65 |
| build_delete_controls.commit | choices | Local binding for choices in build_delete_controls.commit; use the enclosing contract and type below. | Return type of choices; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| build_delete_controls.commit | error | Caught exception for error in build_delete_controls.commit; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 74 |
| build_delete_controls.dismiss | confirmation | Parameter for confirmation in build_delete_controls.dismiss; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 87 |
| build_delete_controls.dismiss | token | Parameter for token in build_delete_controls.dismiss; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 87 |
| build_delete_controls.dismiss | request | Parameter for request in build_delete_controls.dismiss; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 87 |
| build_delete_controls.dismiss | message | Local binding for message in build_delete_controls.dismiss; use the enclosing contract and type below. | Return type of cancel; see its callable contract | Enclosing invocation or class/instance lifetime | 90, 93 |
| build_delete_controls.dismiss | owned | Local binding for owned in build_delete_controls.dismiss; use the enclosing contract and type below. | Return type of cancel; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
