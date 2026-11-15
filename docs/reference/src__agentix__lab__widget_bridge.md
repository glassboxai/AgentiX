# Reference for src/agentix/lab/widget_bridge.py

Loopback HTTP bridge serving only native ASGI response events, never widget imports.

Source fingerprint: 2e6da5a6bbb72265706a8eb0e60092407b3f7386c9da4757e0d37322589dcaf9

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### WidgetBridge

One owner-scoped experimental origin with strict route/header/body limits.

Kind: class. Declared return: Not declared / class. Source line: 12.

### WidgetBridge.__init__

Bind the maintained transport to an explicit loopback origin.

Kind: callable. Declared return: None. Source line: 15.

### WidgetBridge.__call__

Forward HTTP bytes over IPC; reject origin spoofing and unsupported routes.

Kind: callable. Declared return: None. Source line: 29.

### WidgetBridge.__call__.advance

Avoid propagating StopIteration through an asyncio Future.

Kind: callable. Declared return: Not declared / class. Source line: 105.

### serve_widget

Expose only one loopback origin and stop its server when the native worker ends.

Kind: callable. Declared return: None. Source line: 186.

### serve_widget.monitor

Close only the owned preview server after native timeout or channel failure.

Kind: callable. Declared return: Not declared / class. Source line: 200.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | asyncio | Imported dependency for asyncio in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | base64 | Imported dependency for base64 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | validate_http_request | Imported dependency for validate http request in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | WidgetSession | Imported dependency for WidgetSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| WidgetBridge.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| WidgetBridge.__init__ | session | Parameter for session in WidgetBridge.__init__; use the enclosing contract and type below. | WidgetSession | Enclosing invocation or class/instance lifetime | 16 |
| WidgetBridge.__init__ | port | Parameter for port in WidgetBridge.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 16 |
| WidgetBridge.__init__ | parent_origin | Parameter for parent origin in WidgetBridge.__init__; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 16 |
| WidgetBridge.__init__ | self.frame_ancestors | Attribute for frame ancestors in WidgetBridge.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| WidgetBridge.__init__ | self.controls | Attribute for controls in WidgetBridge.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 25 |
| WidgetBridge.__init__ | self.session | Attribute for session in WidgetBridge.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| WidgetBridge.__init__ | self.origin | Attribute for origin in WidgetBridge.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 27 |
| WidgetBridge.__call__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| WidgetBridge.__call__ | scope | Parameter for scope in WidgetBridge.__call__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| WidgetBridge.__call__ | receive | Parameter for receive in WidgetBridge.__call__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| WidgetBridge.__call__ | send | Parameter for send in WidgetBridge.__call__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 29 |
| WidgetBridge.__call__ | started | Local binding for started in WidgetBridge.__call__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 33, 147 |
| WidgetBridge.__call__ | iterator | Local binding for iterator in WidgetBridge.__call__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 34, 101 |
| WidgetBridge.__call__ | headers | Local binding for headers in WidgetBridge.__call__; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 36 |
| WidgetBridge.__call__.comprehension_36 | key | Comprehension item for key in WidgetBridge.__call__.comprehension_36; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| WidgetBridge.__call__.comprehension_36 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| WidgetBridge.__call__.comprehension_42 | key | Comprehension item for key in WidgetBridge.__call__.comprehension_42; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| WidgetBridge.__call__.comprehension_42 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| WidgetBridge.__call__ | body | Local binding for body in WidgetBridge.__call__; use the enclosing contract and type below. | Return type of bytearray; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| WidgetBridge.__call__ | event | Local binding for event in WidgetBridge.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| WidgetBridge.__call__ | status | Local binding for status in WidgetBridge.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62 |
| WidgetBridge.__call__ | media | Local binding for media in WidgetBridge.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62 |
| WidgetBridge.__call__ | content | Artifact or review text whose encoding, size and approval state must be checked. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62, 79 |
| WidgetBridge.__call__ | query | Original user request or a trusted test query; avoid payload logging by default. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| WidgetBridge.__call__ | safe_headers | Local binding for safe headers in WidgetBridge.__call__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 96 |
| WidgetBridge.__call__.comprehension_96 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
| WidgetBridge.__call__ | message | Local binding for message in WidgetBridge.__call__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| WidgetBridge.__call__ | response_headers | Local binding for response headers in WidgetBridge.__call__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 121, 131 |
| WidgetBridge.__call__ | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 122 |
| WidgetBridge.__call__ | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 122 |
| serve_widget | session | Parameter for session in serve_widget; use the enclosing contract and type below. | WidgetSession | Enclosing invocation or class/instance lifetime | 186 |
| serve_widget | port | Parameter for port in serve_widget; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 186 |
| serve_widget | uvicorn | Imported dependency for uvicorn in serve_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 188 |
| serve_widget | server | Local binding for server in serve_widget; use the enclosing contract and type below. | Return type of Server; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| serve_widget.monitor | server.should_exit | Attribute for server.should exit in serve_widget.monitor; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 204 |
| serve_widget | thread | Local binding for thread in serve_widget; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 206 |
