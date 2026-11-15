# Reference for tests/test_widget_panel_browser.py

LAB-004 Playwright begins in Lab and operates the actual isolated embedded widget.

Source fingerprint: a001f711a2bb4ca31b87fac3d398e96fe91e741c20e2db819dc482373a56da23

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_lab_opens_native_widget_in_its_own_gui

Verify real iframe counts, owner separation, close/reopen and native receipts.

Kind: callable. Declared return: Not declared / class. Source line: 21.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | URLError | Imported dependency for URLError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 17 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 18 |
| test_lab_opens_native_widget_in_its_own_gui | tmp_path | Parameter for tmp path in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| test_lab_opens_native_widget_in_its_own_gui | expect | Imported dependency for expect in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 25 |
| test_lab_opens_native_widget_in_its_own_gui | sync_playwright | Imported dependency for sync playwright in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 25 |
| test_lab_opens_native_widget_in_its_own_gui | listener | Managed resource for listener in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 27 |
| test_lab_opens_native_widget_in_its_own_gui | port | Local binding for port in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_lab_opens_native_widget_in_its_own_gui | url | Local binding for url in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_lab_opens_native_widget_in_its_own_gui | audit | Local binding for audit in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_lab_opens_native_widget_in_its_own_gui | logpath | Local binding for logpath in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_lab_opens_native_widget_in_its_own_gui | log | Managed resource for log in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 33 |
| test_lab_opens_native_widget_in_its_own_gui | process | Local binding for process in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_lab_opens_native_widget_in_its_own_gui | deadline | Local binding for deadline in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_lab_opens_native_widget_in_its_own_gui | opener | Local binding for opener in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| test_lab_opens_native_widget_in_its_own_gui | driver | Managed resource for driver in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 54 |
| test_lab_opens_native_widget_in_its_own_gui | browser | Local binding for browser in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_lab_opens_native_widget_in_its_own_gui | first | Local binding for first in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| test_lab_opens_native_widget_in_its_own_gui | second | Local binding for second in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_lab_opens_native_widget_in_its_own_gui | frame | Local binding for frame in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of frame_locator; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_lab_opens_native_widget_in_its_own_gui | text | Loop item for text in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 68, 122 |
| test_lab_opens_native_widget_in_its_own_gui | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 68 |
| test_lab_opens_native_widget_in_its_own_gui | other | Local binding for other in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of frame_locator; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| test_lab_opens_native_widget_in_its_own_gui | reopened | Local binding for reopened in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of frame_locator; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| test_lab_opens_native_widget_in_its_own_gui | rows | Local binding for rows in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_lab_opens_native_widget_in_its_own_gui.comprehension_119 | row | Comprehension item for row in test_lab_opens_native_widget_in_its_own_gui.comprehension_119; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 119 |
| test_lab_opens_native_widget_in_its_own_gui.comprehension_120 | row | Comprehension item for row in test_lab_opens_native_widget_in_its_own_gui.comprehension_120; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| test_lab_opens_native_widget_in_its_own_gui | receipts | Local binding for receipts in test_lab_opens_native_widget_in_its_own_gui; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 121 |
| test_lab_opens_native_widget_in_its_own_gui.comprehension_121 | row | Comprehension item for row in test_lab_opens_native_widget_in_its_own_gui.comprehension_121; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 121 |
| test_lab_opens_native_widget_in_its_own_gui.comprehension_121 | item | Comprehension item for item in test_lab_opens_native_widget_in_its_own_gui.comprehension_121; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 121 |
| test_lab_opens_native_widget_in_its_own_gui | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 122 |
| test_lab_opens_native_widget_in_its_own_gui.comprehension_123 | item | Comprehension item for item in test_lab_opens_native_widget_in_its_own_gui.comprehension_123; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 127 |
