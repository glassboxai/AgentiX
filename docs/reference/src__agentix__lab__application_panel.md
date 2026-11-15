# Reference for src/agentix/lab/application_panel.py

Reviewed composite application's native lifecycle and optional Lab iframe controls.

Source fingerprint: fd6c494e6822166ea12fa696c6eb9eb2fa26e4f836992c605df504ed2a3ed849

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### reviewed_application

Read host-owned activation only; changes fail before any application import.

Kind: callable. Declared return: ApprovedApplication. Source line: 17.

### ApplicationPreview

One composite worker with direct internal calls and the existing restricted bridge.

Kind: class. Declared return: Not declared / class. Source line: 28.

### ApplicationPreview.__init__

Bind explicit unprivileged port, bounded lifetime and display name before startup.

Kind: callable. Declared return: None. Source line: 31.

### ApplicationPreview.configure_layout

Attach only maintained routes bound to this protected app and preview.

Kind: callable. Declared return: None. Source line: 55.

### ApplicationPreview.cancel_execution

Cancel this complete native worker while retaining its private stopped page.

Kind: callable. Declared return: None. Source line: 67.

### ApplicationPreview.restart_execution

Recreate only the same immutable native snapshot; never execute in the host.

Kind: callable. Declared return: None. Source line: 73.

### ApplicationPreview.request_close

Signal owned shutdown without joining the HTTP thread from its request.

Kind: callable. Declared return: None. Source line: 92.

### ApplicationPreview._create_session

Create an application worker; never silently substitute a host process.

Kind: callable. Declared return: ApplicationSession. Source line: 98.

### ApplicationPanel

Reuse owner reservations/cleanup with a separate application capability factory.

Kind: class. Declared return: Not declared / class. Source line: 103.

### ApplicationPanel.__init__

Keep the application independent of the legacy widget panel and its sessions.

Kind: callable. Declared return: None. Source line: 106.

### ApplicationPanel.status

Expose lifecycle only, with no source, review identity or filesystem details.

Kind: callable. Declared return: str. Source line: 110.

### open_application

Clear the prior frame and publish a reviewed native application after readiness.

Kind: callable. Declared return: Iterator[tuple[str, str]]. Source line: 124.

### build_application_panel

Register stable Gradio controls; no server or native process starts during rendering.

Kind: callable. Declared return: None. Source line: 140.

### build_application_panel.opened

Route the requesting browser to its own application instance.

Kind: callable. Declared return: Not declared / class. Source line: 160.

### build_application_panel.closed

Cancel only the requesting browser's application and clear its iframe.

Kind: callable. Declared return: Not declared / class. Source line: 164.

### build_application_panel.state

Update status without replacing the live iframe and its user input.

Kind: callable. Declared return: Not declared / class. Source line: 169.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ApprovedApplication | Imported dependency for ApprovedApplication in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | ApplicationSession | Imported dependency for ApplicationSession in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | NativePreview | Imported dependency for NativePreview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | WidgetPanel | Imported dependency for WidgetPanel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | iframe_html | Imported dependency for iframe html in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 13 |
| module | REVIEW_PATH | Module binding for REVIEW PATH in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| reviewed_application | record | Local binding for record in reviewed_application; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 19 |
| ApplicationPreview.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 32 |
| ApplicationPreview.__init__ | approved | Parameter for approved in ApplicationPreview.__init__; use the enclosing contract and type below. | ApprovedApplication | Enclosing invocation or class/instance lifetime | 33 |
| ApplicationPreview.__init__ | parent_origin | Parameter for parent origin in ApplicationPreview.__init__; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 34 |
| ApplicationPreview.__init__ | port | Parameter for port in ApplicationPreview.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 36 |
| ApplicationPreview.__init__ | lifetime | Parameter for lifetime in ApplicationPreview.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 37 |
| ApplicationPreview.__init__ | display_name | Parameter for display name in ApplicationPreview.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 38 |
| ApplicationPreview.__init__ | self.lifetime | Attribute for lifetime in ApplicationPreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| ApplicationPreview.__init__ | self.display_name | Attribute for display name in ApplicationPreview.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| ApplicationPreview.__init__ | self.lifecycle_lock | Attribute for lifecycle lock in ApplicationPreview.__init__; use the enclosing contract and type below. | Return type of Lock; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| ApplicationPreview.configure_layout | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationPreview.configure_layout | library | Parameter for library in ApplicationPreview.configure_layout; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationPreview.configure_layout | identity | Explicit owner identity used by a session factory or fixture. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationPreview.configure_layout | check | Parameter for check in ApplicationPreview.configure_layout; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| ApplicationPreview.configure_layout | ApplicationControls | Imported dependency for ApplicationControls in ApplicationPreview.configure_layout; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 57 |
| ApplicationPreview.configure_layout | self.bridge.controls | Attribute for bridge.controls in ApplicationPreview.configure_layout; use the enclosing contract and type below. | Return type of ApplicationControls; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| ApplicationPreview.cancel_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| ApplicationPreview.cancel_execution | self.paused | Attribute for paused in ApplicationPreview.cancel_execution; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 70 |
| ApplicationPreview.restart_execution | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| ApplicationPreview.restart_execution | session | Local binding for session in ApplicationPreview.restart_execution; use the enclosing contract and type below. | Return type of _create_session; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| ApplicationPreview.restart_execution | self.session | Attribute for session in ApplicationPreview.restart_execution; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| ApplicationPreview.restart_execution | self.bridge.session | Attribute for bridge.session in ApplicationPreview.restart_execution; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| ApplicationPreview.restart_execution | self.paused | Attribute for paused in ApplicationPreview.restart_execution; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 88 |
| ApplicationPreview.request_close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationPreview.request_close | self.server.should_exit | Attribute for server.should exit in ApplicationPreview.request_close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 96 |
| ApplicationPreview._create_session | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 98 |
| ApplicationPreview._create_session | approved | Parameter for approved in ApplicationPreview._create_session; use the enclosing contract and type below. | ApprovedApplication | Enclosing invocation or class/instance lifetime | 98 |
| ApplicationPanel.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 106 |
| ApplicationPanel.status | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 110 |
| ApplicationPanel.status | owner | Parameter for owner in ApplicationPanel.status; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 110 |
| open_application | panel | Parameter for panel in open_application; use the enclosing contract and type below. | WidgetPanel | Enclosing invocation or class/instance lifetime | 124 |
| open_application | owner | Parameter for owner in open_application; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 124 |
| open_application | origin | Parameter for origin in open_application; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 124 |
| open_application | preview | Local binding for preview in open_application; use the enclosing contract and type below. | Return type of open; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| open_application | error | Caught exception for error in open_application; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 135 |
| build_application_panel | panel | Parameter for panel in build_application_panel; use the enclosing contract and type below. | WidgetPanel | Enclosing invocation or class/instance lifetime | 140 |
| build_application_panel | origin | Parameter for origin in build_application_panel; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 140 |
| build_application_panel | gr | Imported dependency for gr in build_application_panel; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 142 |
| build_application_panel | start | Local binding for start in build_application_panel; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| build_application_panel | stop | Local binding for stop in build_application_panel; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| build_application_panel | status | Local binding for status in build_application_panel; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| build_application_panel | frame | Local binding for frame in build_application_panel; use the enclosing contract and type below. | Return type of HTML; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| build_application_panel | timer | Local binding for timer in build_application_panel; use the enclosing contract and type below. | Return type of Timer; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| build_application_panel.opened | request | Parameter for request in build_application_panel.opened; use the enclosing contract and type below. | gr.Request | Enclosing invocation or class/instance lifetime | 160 |
| build_application_panel.closed | request | Parameter for request in build_application_panel.closed; use the enclosing contract and type below. | gr.Request | Enclosing invocation or class/instance lifetime | 164 |
| build_application_panel.state | request | Parameter for request in build_application_panel.state; use the enclosing contract and type below. | gr.Request | Enclosing invocation or class/instance lifetime | 169 |
