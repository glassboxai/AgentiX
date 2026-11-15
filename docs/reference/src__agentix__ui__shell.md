# Reference for src/agentix/ui/shell.py

V4 composition root: common sidebar and separately implemented tab frontends.

Source fingerprint: 4b5f201564b00a6a4ca79e3147ee92713047af806440edf4efee757d89f9e191

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### View

Constructed Gradio Blocks and launch theme; owns no running server.

Kind: class. Declared return: Not declared / class. Source line: 27.

### build_view

Compose one session-owned sidebar outside Tools and Applications tabs.

Kind: callable. Declared return: View. Source line: 34.

### build_view.bind

Tell Gradio to inject Request instead of treating it as a user input.

Kind: callable. Declared return: Any. Source line: 43.

### build_view.bind.callback

Dispatch only after the session callback checks token ownership.

Kind: callable. Declared return: Any. Source line: 47.

### build_view.bind.streaming_callback

Preserve stage streaming while retaining framework Request injection.

Kind: callable. Declared return: Not declared / class. Source line: 55.

### launch

Start the existing queued loopback UI and open the browser.

Kind: callable. Declared return: None. Source line: 127.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | inspect | Imported dependency for inspect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ActivityBackend | Imported dependency for ActivityBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | ApplicationsBackend | Imported dependency for ApplicationsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | CatalogMaintenanceBackend | Imported dependency for CatalogMaintenanceBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SidebarBackend | Imported dependency for SidebarBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ToolRepairBackend | Imported dependency for ToolRepairBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ToolsBackend | Imported dependency for ToolsBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | HostRequirements | Imported dependency for HostRequirements in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | build_applications_frontend | Imported dependency for build applications frontend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | header | Imported dependency for header in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | launch_options | Imported dependency for launch options in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | build_sidebar | Imported dependency for build sidebar in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | create_theme | Imported dependency for create theme in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | build_tools_frontend | Imported dependency for build tools frontend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | SESSION_STATE_TTL_SECONDS | Module binding for SESSION STATE TTL SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 22 |
| module | ACTIVITY_TIMER_SECONDS | Module binding for ACTIVITY TIMER SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 23 |
| View | demo | Typed binding for demo in View; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 30 |
| View | theme | Typed binding for theme in View; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 31 |
| build_view | sessions | Parameter for sessions in build_view; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 35 |
| build_view | gradio_module | Parameter for gradio module in build_view; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 35, 39 |
| build_view | applications_backend | Parameter for applications backend in build_view; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 35 |
| build_view | gr | Local binding for gr in build_view; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| build_view | callbacks | Local binding for callbacks in build_view; use the enclosing contract and type below. | Return type of ToolsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| build_view.bind | method | Parameter for method in build_view.bind; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 43 |
| build_view.bind | discard_result | Parameter for discard result in build_view.bind; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 43 |
| build_view.bind.callback | args | Parameter for args in build_view.bind.callback; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 47 |
| build_view.bind.callback | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 47 |
| build_view.bind.callback | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of method; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| build_view.bind.streaming_callback | args | Parameter for args in build_view.bind.streaming_callback; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 55 |
| build_view.bind.streaming_callback | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Any | Enclosing invocation or class/instance lifetime | 55 |
| build_view.bind | callback | Local binding for callback in build_view.bind; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| build_view.bind | callback.__annotations__ | Attribute for callback.  annotations in build_view.bind; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| build_view.bind | signature | Local binding for signature in build_view.bind; use the enclosing contract and type below. | Return type of signature; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| build_view.bind | callback.__signature__ | Attribute for callback.  signature in build_view.bind; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| build_view.bind.comprehension_64 | parameter | Comprehension item for parameter in build_view.bind.comprehension_64; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| build_view.bind | owner | Local binding for owner in build_view.bind; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 71, 73 |
| build_view.bind | callback.__name__ | Attribute for callback.  name in build_view.bind; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| build_view | theme | Local binding for theme in build_view; use the enclosing contract and type below. | Return type of create_theme; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| build_view | applications | Local binding for applications in build_view; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| build_view | maintenance | Local binding for maintenance in build_view; use the enclosing contract and type below. | Return type of CatalogMaintenanceBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| build_view | repairs | Local binding for repairs in build_view; use the enclosing contract and type below. | Return type of ToolRepairBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| build_view | demo | Managed resource for demo in build_view; use the enclosing contract and type below. | Return type of Blocks; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 87 |
| build_view | session_state | Local binding for session state in build_view; use the enclosing contract and type below. | Return type of State; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| build_view | request_state | Local binding for request state in build_view; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| build_view | progress | Local binding for progress in build_view; use the enclosing contract and type below. | Return type of HTML; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| build_view | MessageDialog | Imported dependency for MessageDialog in build_view; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| build_view | dialog | Local binding for dialog in build_view; use the enclosing contract and type below. | Return type of MessageDialog; see its callable contract | Enclosing invocation or class/instance lifetime | 96 |
| launch | view | Parameter for view in launch; use the enclosing contract and type below. | View | Enclosing invocation or class/instance lifetime | 127 |
| launch | server_port | Parameter for server port in launch; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 127 |
| launch | open_browser | Parameter for open browser in launch; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 127 |
