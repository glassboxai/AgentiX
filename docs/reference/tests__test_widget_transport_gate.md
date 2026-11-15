# Reference for tests/test_widget_transport_gate.py

LAB-002 native transport gate; authored temporary fixture, never generated code.

Source fingerprint: e7c5bdf99c0da41c146ecd5540db79b2481e8e93a3aa4e78a66caa4eb2c87666

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_native_widget_server_can_serve_host_browser

A reachable isolated HTTP server is necessary, not sufficient, for Gradio.

Kind: callable. Declared return: Not declared / class. Source line: 21.

### test_native_widget_server_can_serve_host_browser.Control

Demonstrate the host HTTP route works independently of the child.

Kind: class. Declared return: Not declared / class. Source line: 24.

### test_native_widget_server_can_serve_host_browser.Control.do_GET

Return one bounded response and no user data.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_native_widget_server_can_serve_host_browser.Control.log_message

Suppress benign access logs without hiding assertions.

Kind: callable. Declared return: Not declared / class. Source line: 33.

### test_native_widget_server_can_serve_host_browser.execute

Keep native ownership on one thread and expose result only after joining.

Kind: callable. Declared return: Not declared / class. Source line: 72.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | BaseHTTPRequestHandler | Imported dependency for BaseHTTPRequestHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | HTTPServer | Imported dependency for HTTPServer in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | URLError | Imported dependency for URLError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| test_native_widget_server_can_serve_host_browser | tmp_path | Parameter for tmp path in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_native_widget_server_can_serve_host_browser.Control.do_GET | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_native_widget_server_can_serve_host_browser.Control.log_message | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| test_native_widget_server_can_serve_host_browser.Control.log_message | args | Parameter for args in test_native_widget_server_can_serve_host_browser.Control.log_message; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| test_native_widget_server_can_serve_host_browser | control | Local binding for control in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Return type of HTTPServer; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_native_widget_server_can_serve_host_browser | control.timeout | Attribute for control.timeout in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 37 |
| test_native_widget_server_can_serve_host_browser | control_thread | Local binding for control thread in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_native_widget_server_can_serve_host_browser | opener | Local binding for opener in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_native_widget_server_can_serve_host_browser | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 42, 88 |
| test_native_widget_server_can_serve_host_browser | port | Local binding for port in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_native_widget_server_can_serve_host_browser | source | Explicit source document or source-code text; never imported for reference generation. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_native_widget_server_can_serve_host_browser | observation | Local binding for observation in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 70 |
| test_native_widget_server_can_serve_host_browser.execute | error | Caught exception for error in test_native_widget_server_can_serve_host_browser.execute; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 78 |
| test_native_widget_server_can_serve_host_browser | thread | Local binding for thread in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Return type of Thread; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| test_native_widget_server_can_serve_host_browser | reached | Local binding for reached in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 83, 89 |
| test_native_widget_server_can_serve_host_browser | connection_errors | Local binding for connection errors in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 84 |
| test_native_widget_server_can_serve_host_browser | deadline | Local binding for deadline in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_native_widget_server_can_serve_host_browser | error | Caught exception for error in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | (URLError, TimeoutError, OSError) | Current exception handler; Python clears this binding afterward | 92 |
| test_native_widget_server_can_serve_host_browser | reason | Local binding for reason in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_native_widget_server_can_serve_host_browser | category | Local binding for category in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_native_widget_server_can_serve_host_browser | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_native_widget_server_can_serve_host_browser | evidence | Local binding for evidence in test_native_widget_server_can_serve_host_browser; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 99 |
