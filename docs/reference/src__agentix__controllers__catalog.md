# Reference for src/agentix/controllers/catalog.py

Session-bound two-step permanent deletion; no Gradio or arbitrary path inputs.

Source fingerprint: 0ae7033758a07424dcdd757eea040319d711918175c876e4634e389ed631189b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### open_directory

Open one already-validated folder with the OS file manager, never a shell.

A refused shell association is reported as ``ValueError`` so the owner sees the
maintained modal instead of a raw framework error.

Kind: callable. Declared return: None. Source line: 22.

### CatalogMaintenanceBackend

Keep one expiring confirmation on its owning controller, never in model context.

Kind: class. Declared return: Not declared / class. Source line: 36.

### CatalogMaintenanceBackend.__init__

Inject sessions/application library, clock, folder opener and window focus.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### CatalogMaintenanceBackend._idle

Reject mutation while this owner's workflow, generation or review is pending.

Kind: callable. Declared return: None. Source line: 58.

### CatalogMaintenanceBackend._service

Compose strict revocation and exact roots, without reading credentials.

Kind: callable. Declared return: Not declared / class. Source line: 66.

### CatalogMaintenanceBackend._service.revoke

Require durable revocation to succeed before removing any package bytes.

Kind: callable. Declared return: Not declared / class. Source line: 72.

### CatalogMaintenanceBackend.choices

List exact server-owned IDs/names; browser values are never filesystem paths.

Kind: callable. Declared return: Not declared / class. Source line: 85.

### CatalogMaintenanceBackend.reseal_tools

Reseal intact approvals, then run the isolated tests of changed tools.

A record whose bytes are unchanged is rebound to the current policy without
executing anything. A missing or changed record is re-verified through the
isolated test runner, which never imports generated code on the host; the
batch stops at the first failure. Acceptance review stays mandatory and is
never granted here.

Kind: callable. Declared return: Not declared / class. Source line: 106.

### CatalogMaintenanceBackend.reveal

Open this owner's installed catalog folder without accepting a browser path.

The root comes from server state, must already exist and must not be a
symbolic link or reparse point. Opening a folder grants the page no read,
write or execution capability, and no directory is created here. After a
completed open the folder window is raised above the browser; a refused
foreground change is logged and never turns the open into a failure.

Kind: callable. Declared return: Not declared / class. Source line: 170.

### CatalogMaintenanceBackend.prepare

Perform read-only checks and mint a one-use owner/content-bound confirmation.

Kind: callable. Declared return: Not declared / class. Source line: 217.

### CatalogMaintenanceBackend._pending

Check the already-resolved owner while holding only its controller lock.

Kind: callable. Declared return: Not declared / class. Source line: 246.

### CatalogMaintenanceBackend.cancel

Discard only this exact confirmation without touching files or grants.

Kind: callable. Declared return: Not declared / class. Source line: 259.

### CatalogMaintenanceBackend.confirm

Consume once; never reacquire the session-registry lock under the owner lock.

Kind: callable. Declared return: Not declared / class. Source line: 267.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | secrets | Imported dependency for secrets in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | explorer_window | Imported dependency for explorer window in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SessionOwnerAccess | Imported dependency for SessionOwnerAccess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | CatalogMaintenance | Imported dependency for CatalogMaintenance in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | WidgetStore | Imported dependency for WidgetStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 17 |
| module | CONFIRMATION_TTL_SECONDS | Module binding for CONFIRMATION TTL SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 19 |
| open_directory | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 22 |
| open_directory | error | Caught exception for error in open_directory; use the enclosing contract and type below. | OSError | Current exception handler; Python clears this binding afterward | 32 |
| CatalogMaintenanceBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| CatalogMaintenanceBackend.__init__ | registry | Parameter for registry in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| CatalogMaintenanceBackend.__init__ | applications | Parameter for applications in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| CatalogMaintenanceBackend.__init__ | service_factory | Parameter for service factory in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 44 |
| CatalogMaintenanceBackend.__init__ | clock | Parameter for clock in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| CatalogMaintenanceBackend.__init__ | opener | Parameter for opener in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| CatalogMaintenanceBackend.__init__ | window_snapshot | Parameter for window snapshot in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| CatalogMaintenanceBackend.__init__ | focus_window | Parameter for focus window in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| CatalogMaintenanceBackend.__init__ | self.applications | Attribute for applications in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 52 |
| CatalogMaintenanceBackend.__init__ | self.service_factory | Attribute for service factory in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 52 |
| CatalogMaintenanceBackend.__init__ | self.clock | Attribute for clock in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 52 |
| CatalogMaintenanceBackend.__init__ | self.opener | Attribute for opener in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| CatalogMaintenanceBackend.__init__ | self.window_snapshot | Attribute for window snapshot in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| CatalogMaintenanceBackend.__init__ | self.focus_window | Attribute for focus window in CatalogMaintenanceBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 55 |
| CatalogMaintenanceBackend._idle | controller | Parameter for controller in CatalogMaintenanceBackend._idle; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 58 |
| CatalogMaintenanceBackend._idle.comprehension_60 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 62 |
| CatalogMaintenanceBackend._service | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| CatalogMaintenanceBackend._service | controller | Parameter for controller in CatalogMaintenanceBackend._service; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| CatalogMaintenanceBackend._service | operations | Local binding for operations in CatalogMaintenanceBackend._service; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| CatalogMaintenanceBackend._service.revoke | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| CatalogMaintenanceBackend.choices | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| CatalogMaintenanceBackend.choices | kind | Parameter for kind in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| CatalogMaintenanceBackend.choices | token | Parameter for token in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 85 |
| CatalogMaintenanceBackend.choices | request | Parameter for request in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| CatalogMaintenanceBackend.choices | session | Local binding for session in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| CatalogMaintenanceBackend.choices | choices | Local binding for choices in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 89, 95 |
| CatalogMaintenanceBackend.choices | owned | Local binding for owned in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| CatalogMaintenanceBackend.choices | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| CatalogMaintenanceBackend.choices | catalog | Local binding for catalog in CatalogMaintenanceBackend.choices; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| CatalogMaintenanceBackend.choices.comprehension_96 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 98 |
| CatalogMaintenanceBackend.reseal_tools | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| CatalogMaintenanceBackend.reseal_tools | token | Parameter for token in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 106 |
| CatalogMaintenanceBackend.reseal_tools | request | Parameter for request in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| CatalogMaintenanceBackend.reseal_tools | session | Local binding for session in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| CatalogMaintenanceBackend.reseal_tools | controller | Local binding for controller in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 116 |
| CatalogMaintenanceBackend.reseal_tools | operations | Local binding for operations in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| CatalogMaintenanceBackend.reseal_tools | store | Local binding for store in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| CatalogMaintenanceBackend.reseal_tools | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| CatalogMaintenanceBackend.reseal_tools | catalog | Local binding for catalog in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| CatalogMaintenanceBackend.reseal_tools | names | Local binding for names in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 125 |
| CatalogMaintenanceBackend.reseal_tools.comprehension_126 | path | Path under validation or an explicitly scoped maintained source path. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 126 |
| CatalogMaintenanceBackend.reseal_tools | resealed | Local binding for resealed in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 132 |
| CatalogMaintenanceBackend.reseal_tools | ran | Local binding for ran in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 132 |
| CatalogMaintenanceBackend.reseal_tools | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 133 |
| CatalogMaintenanceBackend.reseal_tools | folder | Local binding for folder in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 134 |
| CatalogMaintenanceBackend.reseal_tools | code_path | Local binding for code path in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 135 |
| CatalogMaintenanceBackend.reseal_tools | tests_path | Local binding for tests path in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 135 |
| CatalogMaintenanceBackend.reseal_tools | outcome | Local binding for outcome in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of reseal; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| CatalogMaintenanceBackend.reseal_tools | status | Local binding for status in CatalogMaintenanceBackend.reseal_tools; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| CatalogMaintenanceBackend.reveal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 170 |
| CatalogMaintenanceBackend.reveal | kind | Parameter for kind in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 170 |
| CatalogMaintenanceBackend.reveal | token | Parameter for token in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 170 |
| CatalogMaintenanceBackend.reveal | request | Parameter for request in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 170 |
| CatalogMaintenanceBackend.reveal | session | Local binding for session in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| CatalogMaintenanceBackend.reveal | candidate | Local binding for candidate in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 181, 184 |
| CatalogMaintenanceBackend.reveal | label | Local binding for label in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 182, 185 |
| CatalogMaintenanceBackend.reveal | resolved | Local binding for resolved in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| CatalogMaintenanceBackend.reveal | attributes | Local binding for attributes in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| CatalogMaintenanceBackend.reveal | before | Local binding for before in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | Return type of window_snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 197, 199 |
| CatalogMaintenanceBackend.reveal | error | Caught exception for error in CatalogMaintenanceBackend.reveal; use the enclosing contract and type below. | OSError | Current exception handler; Python clears this binding afterward | 202, 208 |
| CatalogMaintenanceBackend.prepare | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 217 |
| CatalogMaintenanceBackend.prepare | kind | Parameter for kind in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 217 |
| CatalogMaintenanceBackend.prepare | selected | Parameter for selected in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 217 |
| CatalogMaintenanceBackend.prepare | token | Parameter for token in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 217 |
| CatalogMaintenanceBackend.prepare | request | Parameter for request in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 217 |
| CatalogMaintenanceBackend.prepare | session | Local binding for session in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 219 |
| CatalogMaintenanceBackend.prepare | controller | Local binding for controller in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 220 |
| CatalogMaintenanceBackend.prepare | service | Local binding for service in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Return type of _service; see its callable contract | Enclosing invocation or class/instance lifetime | 223 |
| CatalogMaintenanceBackend.prepare | snapshot | Local binding for snapshot in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 224 |
| CatalogMaintenanceBackend.prepare | confirmation | Local binding for confirmation in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | Return type of token_urlsafe; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| CatalogMaintenanceBackend.prepare | controller._catalog_pending | Attribute for controller. catalog pending in CatalogMaintenanceBackend.prepare; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 234 |
| CatalogMaintenanceBackend._pending | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 246 |
| CatalogMaintenanceBackend._pending | confirmation | Parameter for confirmation in CatalogMaintenanceBackend._pending; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 246 |
| CatalogMaintenanceBackend._pending | session | Parameter for session in CatalogMaintenanceBackend._pending; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 246 |
| CatalogMaintenanceBackend._pending | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| CatalogMaintenanceBackend.cancel | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 259 |
| CatalogMaintenanceBackend.cancel | confirmation | Parameter for confirmation in CatalogMaintenanceBackend.cancel; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 259 |
| CatalogMaintenanceBackend.cancel | token | Parameter for token in CatalogMaintenanceBackend.cancel; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 259 |
| CatalogMaintenanceBackend.cancel | request | Parameter for request in CatalogMaintenanceBackend.cancel; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 259 |
| CatalogMaintenanceBackend.cancel | session | Local binding for session in CatalogMaintenanceBackend.cancel; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 261 |
| CatalogMaintenanceBackend.cancel | session.controller._catalog_pending | Attribute for session.controller. catalog pending in CatalogMaintenanceBackend.cancel; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 264 |
| CatalogMaintenanceBackend.confirm | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| CatalogMaintenanceBackend.confirm | confirmation | Parameter for confirmation in CatalogMaintenanceBackend.confirm; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 267 |
| CatalogMaintenanceBackend.confirm | token | Parameter for token in CatalogMaintenanceBackend.confirm; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 267 |
| CatalogMaintenanceBackend.confirm | request | Parameter for request in CatalogMaintenanceBackend.confirm; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 267 |
| CatalogMaintenanceBackend.confirm | session | Local binding for session in CatalogMaintenanceBackend.confirm; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 269 |
| CatalogMaintenanceBackend.confirm | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of _pending; see its callable contract | Enclosing invocation or class/instance lifetime | 271 |
| CatalogMaintenanceBackend.confirm | session.controller._catalog_pending | Attribute for session.controller. catalog pending in CatalogMaintenanceBackend.confirm; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 272 |
