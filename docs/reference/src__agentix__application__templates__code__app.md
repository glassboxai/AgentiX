# Reference for src/agentix/application/templates/code/app.py

Native compositor for persisted connection code and approved reusable widgets.

Source fingerprint: 8bac166f8cd3e2091bbcc57a1968297f8e92645ae41a1e70e29bcd27487d9b65

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### application_title

Read the host-staged display name; never accept markup or a missing snapshot.

The supervisor writes application_display.json beside this module only when the
owner named the application. Markdown-active characters are dropped so a name
cannot restyle the heading, and any read or shape failure keeps the default.

Kind: callable. Declared return: str. Source line: 12.

### input_component

Build a typed public application control with a stable non-widget identity.

Kind: callable. Declared return: gr.components.Component. Source line: 39.

### create_application

Render inputs/widgets and connect Run directly to generated Python in isolation.

Kind: callable. Declared return: gr.Blocks. Source line: 53.

### create_application.run_all

Clear stale displays, run complete code and populate observed widget arguments.

Kind: callable. Declared return: Iterator[list[object]]. Source line: 90.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | gr | Imported dependency for gr in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Context | Imported dependency for Context in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ElementIds | Imported dependency for ElementIds in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | MANIFEST | Imported dependency for MANIFEST in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | execute | Imported dependency for execute in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| application_title | json | Imported dependency for json in application_title; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| application_title | Path | Imported dependency for Path in application_title; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| application_title | record | Local binding for record in application_title; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| application_title | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| application_title | cleaned | Local binding for cleaned in application_title; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| application_title.comprehension_31 | character | Comprehension item for character in application_title.comprehension_31; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 33 |
| input_component | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 39 |
| input_component | shape | Parameter for shape in input_component; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 39 |
| input_component | options | Local binding for options in input_component; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 41 |
| create_application | json | Imported dependency for json in create_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 55 |
| create_application | ids | Local binding for ids in create_application; use the enclosing contract and type below. | Return type of ElementIds; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| create_application | widgets | Local binding for widgets in create_application; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 58 |
| create_application | managed | Local binding for managed in create_application; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 58 |
| create_application | demo | Managed resource for demo in create_application; use the enclosing contract and type below. | Return type of Blocks; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 59 |
| create_application | button | Local binding for button in create_application; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| create_application | inputs | Local binding for inputs in create_application; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 67 |
| create_application.comprehension_67 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| create_application.comprehension_67 | shape | Comprehension item for shape in create_application.comprehension_67; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 68 |
| create_application | widget | Loop item for widget in create_application; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 70 |
| create_application | identity | Explicit owner identity used by a session factory or fixture. | tuple | Enclosing invocation or class/instance lifetime | 71 |
| create_application | name | Current identifier selected by parsing, lookup or dependency registration. | tuple | Enclosing invocation or class/instance lifetime | 71, 85 |
| create_application | contract | Validated declarative acceptance data bound to current artifact identities. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| create_application | refs | Local binding for refs in create_application; use the enclosing contract and type below. | Return type of create_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| create_application | refs['button'].visible | Attribute for refs['button'].visible in create_application; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 84 |
| create_application | component | Loop item for component in create_application; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 85 |
| create_application | component.interactive | Attribute for component.interactive in create_application; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 86 |
| create_application | status | Local binding for status in create_application; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| create_application.run_all | values | Parameter for values in create_application.run_all; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 90 |
| create_application.run_all | payload | Local binding for payload in create_application.run_all; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| create_application.run_all | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 95 |
| create_application.run_all | shape | Loop item for shape in create_application.run_all; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 95 |
| create_application.run_all | results | Local binding for results in create_application.run_all; use the enclosing contract and type below. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| create_application.run_all | arguments | Local binding for arguments in create_application.run_all; use the enclosing contract and type below. | Return type of execute; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| create_application.run_all.comprehension_100 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 100 |
| create_application.run_all.comprehension_100 | refs | Comprehension item for refs in create_application.run_all.comprehension_100; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 100 |
| create_application.run_all.comprehension_101 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 101 |
| create_application.run_all.comprehension_101 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 101 |
| create_application.run_all.comprehension_101 | _ | Comprehension item for  in create_application.run_all.comprehension_101; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 101 |
| create_application.comprehension_112 | refs | Comprehension item for refs in create_application.comprehension_112; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 112 |
| create_application.comprehension_113 | _ | Comprehension item for  in create_application.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| create_application.comprehension_113 | component | Comprehension item for component in create_application.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
