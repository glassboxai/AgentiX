# Reference for src/agentix/application/app_controls.py

Host-owned, origin-bound presentation and lifecycle routes for one preview.

Source fingerprint: a59bf5fbe77beeff9df09c222480265d58ee2ab81a18853a62567609e0022ddd

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### PreviewControl

Owned listener identity and lifecycle operations; never accepts a host path.

Kind: class. Declared return: Not declared / class. Source line: 17.

### PreviewControl.cancel_execution

Stop the owned native worker.

Kind: callable. Declared return: None. Source line: 23.

### PreviewControl.restart_execution

Start the same reviewed snapshot again.

Kind: callable. Declared return: None. Source line: 27.

### PreviewControl.request_close

Signal owned listener and worker shutdown.

Kind: callable. Declared return: None. Source line: 31.

### ApplicationControls

Authorize bounded layout writes without granting file or Python capabilities.

Kind: class. Declared return: Not declared / class. Source line: 36.

### ApplicationControls.__init__

Bind one preview, optional protected identity and its private staging root.

``root`` is resolved per request because a restart replaces the staging
directory; it never exposes a host path to the iframe.

Kind: callable. Declared return: None. Source line: 39.

### ApplicationControls.handle

Return status, media type and bytes; reject malformed or foreign mutations.

Kind: callable. Declared return: tuple[int, str, bytes]. Source line: 60.

### ApplicationControls.handle.unique

Reject ambiguous JSON object keys before validation.

Kind: callable. Declared return: dict[str, Any]. Source line: 112.

### ApplicationControls._json

Encode only maintained response data.

Kind: callable. Declared return: tuple[int, str, bytes]. Source line: 153.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | secrets | Imported dependency for secrets in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 13 |
| module | ASSETS | Module binding for ASSETS in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| PreviewControl | port | Typed binding for port in PreviewControl; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 20 |
| PreviewControl | paused | Typed binding for paused in PreviewControl; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 21 |
| PreviewControl.cancel_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| PreviewControl.restart_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| PreviewControl.request_close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| ApplicationControls.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| ApplicationControls.__init__ | preview | Parameter for preview in ApplicationControls.__init__; use the enclosing contract and type below. | PreviewControl | Enclosing invocation or class/instance lifetime | 41 |
| ApplicationControls.__init__ | library | Parameter for library in ApplicationControls.__init__; use the enclosing contract and type below. | InstalledApps &#124; None | Enclosing invocation or class/instance lifetime | 43 |
| ApplicationControls.__init__ | identity | Explicit owner identity used by a session factory or fixture. | str &#124; None | Enclosing invocation or class/instance lifetime | 44 |
| ApplicationControls.__init__ | check | Parameter for check in ApplicationControls.__init__; use the enclosing contract and type below. | Callable[[], None] &#124; None | Enclosing invocation or class/instance lifetime | 45 |
| ApplicationControls.__init__ | root | Explicit root directory against which named paths are resolved. | Callable[[], Path] &#124; None | Enclosing invocation or class/instance lifetime | 46 |
| ApplicationControls.__init__ | self.preview | Attribute for preview in ApplicationControls.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| ApplicationControls.__init__ | self.library | Attribute for library in ApplicationControls.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| ApplicationControls.__init__ | self.identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationControls.__init__ | self.check | Attribute for check in ApplicationControls.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| ApplicationControls.__init__ | self.root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| ApplicationControls.__init__ | self.token | Attribute for token in ApplicationControls.__init__; use the enclosing contract and type below. | Return type of token_urlsafe; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| ApplicationControls.handle | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| ApplicationControls.handle | method | Parameter for method in ApplicationControls.handle; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 61 |
| ApplicationControls.handle | path | Path under validation or an explicitly scoped maintained source path. | str | Enclosing invocation or class/instance lifetime | 61 |
| ApplicationControls.handle | headers | Parameter for headers in ApplicationControls.handle; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 61 |
| ApplicationControls.handle | body | Parameter for body in ApplicationControls.handle; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 61 |
| ApplicationControls.handle | started | Local binding for started in ApplicationControls.handle; use the enclosing contract and type below. | Return type of monotonic; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| ApplicationControls.handle | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 77 |
| ApplicationControls.handle | media | Local binding for media in ApplicationControls.handle; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| ApplicationControls.handle | editable | Local binding for editable in ApplicationControls.handle; use the enclosing contract and type below. | Return type of bool; see its callable contract | Enclosing invocation or class/instance lifetime | 81, 91 |
| ApplicationControls.handle | layout | Local binding for layout in ApplicationControls.handle; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 82, 87 |
| ApplicationControls.handle | controls | Local binding for controls in ApplicationControls.handle; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 83, 88 |
| ApplicationControls.handle | groups | Local binding for groups in ApplicationControls.handle; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 84, 89 |
| ApplicationControls.handle.unique | pairs | Parameter for pairs in ApplicationControls.handle.unique; use the enclosing contract and type below. | list[tuple[str, Any]] | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationControls.handle.unique | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 114 |
| ApplicationControls.handle.unique | key | Loop item for key in ApplicationControls.handle.unique; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 115 |
| ApplicationControls.handle.unique | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 115 |
| ApplicationControls.handle | payload | Local binding for payload in ApplicationControls.handle; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| ApplicationControls.handle | action | Local binding for action in ApplicationControls.handle; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 130 |
| ApplicationControls._json | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 153 |
