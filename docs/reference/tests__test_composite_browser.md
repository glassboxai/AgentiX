# Reference for tests/test_composite_browser.py

Real Playwright acceptance of the independent native application.

Source fingerprint: 7de17a8aee95e624bcb02f5760fd052fea1999a749ab1998bfe9eb07ab86a610

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### free_port

Choose a disposable test port; production launchers require an explicit port.

Kind: callable. Declared return: Not declared / class. Source line: 20.

### await_http

Wait for an owned listener without touching any live Lab process.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### check_analysis

Use literal independent expected values, read from the visible application result.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### test_standalone_launcher_gui_without_lab

Launch the same package without Lab, operate it and observe automatic native expiry.

Kind: callable. Declared return: Not declared / class. Source line: 57.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | URLError | Imported dependency for URLError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | schema3_package | Imported dependency for schema3 package in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 16 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| free_port | listener | Managed resource for listener in free_port; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 22 |
| await_http | url | Parameter for url in await_http; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| await_http | process | Parameter for process in await_http; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| await_http | logpath | Parameter for logpath in await_http; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| await_http | opener | Local binding for opener in await_http; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| await_http | deadline | Local binding for deadline in await_http; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| check_analysis | frame | Parameter for frame in check_analysis; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| check_analysis | text | Parameter for text in check_analysis; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| check_analysis | words | Parameter for words in check_analysis; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| check_analysis | vowels | Parameter for vowels in check_analysis; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| check_analysis | expect | Imported dependency for expect in check_analysis; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 44 |
| test_standalone_launcher_gui_without_lab | tmp_path | Parameter for tmp path in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| test_standalone_launcher_gui_without_lab | sync_playwright | Imported dependency for sync playwright in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 59 |
| test_standalone_launcher_gui_without_lab | application_digest | Imported dependency for application digest in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| test_standalone_launcher_gui_without_lab | package | Local binding for package in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of package; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_standalone_launcher_gui_without_lab | port | Local binding for port in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| test_standalone_launcher_gui_without_lab | logpath | Local binding for logpath in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 65 |
| test_standalone_launcher_gui_without_lab | evidence | Local binding for evidence in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 65 |
| test_standalone_launcher_gui_without_lab | log | Managed resource for log in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 66 |
| test_standalone_launcher_gui_without_lab | process | Local binding for process in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_standalone_launcher_gui_without_lab | url | Local binding for url in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_standalone_launcher_gui_without_lab | driver | Managed resource for driver in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 89 |
| test_standalone_launcher_gui_without_lab | browser | Local binding for browser in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| test_standalone_launcher_gui_without_lab | page | Local binding for page in test_standalone_launcher_gui_without_lab; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
