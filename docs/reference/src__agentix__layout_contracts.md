# Reference for src/agentix/layout_contracts.py

Strict presentation-only geometry; no executable strings, selectors or host paths.

Source fingerprint: 15600b80d1a04077cba706fdb98357f31a90d85f4e207c1ff2e2292446fbf660

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _legacy_control

Return whether a legacy schema-2 identifier is a movable canvas control.

Kind: callable. Declared return: bool. Source line: 19.

### Rectangle

Pixel geometry bounded to the generated application's editable canvas.

Kind: class. Declared return: Not declared / class. Source line: 24.

### Layout

Versioned data-only layout with immutable toolbar/authorization boundaries.

Kind: class. Declared return: Not declared / class. Source line: 34.

### Layout.known_controls

Never let layout records target the toolbar, parent UI or arbitrary selectors.

Kind: callable. Declared return: dict[str, Rectangle]. Source line: 44.

### Layout.known_hidden_controls

Keep persisted visibility on the same reviewed controls as geometry.

Kind: callable. Declared return: list[str] | None. Source line: 60.

### validate_layout

Return normalized safe JSON data; raise ValueError without applying invalid edits.

Kind: callable. Declared return: dict. Source line: 79.

### application_layout_groups

Map every movable control to the tool whose widgets it belongs to.

Public inputs and Status are their own groups so unrelated controls never
share a color. Legacy schema-2 manifests return an empty mapping because
their widget-to-tool relation is not recorded. The result is presentation
data only and never widens the movable allowlist.

Kind: callable. Declared return: dict[str, str]. Source line: 86.

### application_layout_ids

Derive reviewed canvas IDs for connection-code widgets and public inputs.

Return None for legacy formats using the fixed compatibility allowlist.
Schema-3 public inputs use their stable application_input_<name> IDs.
Toolbar IDs are never included; callers share this set for editing and storage.

Kind: callable. Declared return: set[str] | None. Source line: 112.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | BaseModel | Imported dependency for BaseModel in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ConfigDict | Imported dependency for ConfigDict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Field | Imported dependency for Field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ValidationInfo | Imported dependency for ValidationInfo in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | field_validator | Imported dependency for field validator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | _LEGACY_CONTROLS | Module binding for LEGACY CONTROLS in module; use the enclosing contract and type below. | set | Module/process lifetime | 7 |
| module | _LEGACY_WIDGET_CONTROL | Module binding for LEGACY WIDGET CONTROL in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 14 |
| _legacy_control | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 19 |
| Rectangle | model_config | Local binding for model config in Rectangle; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 27 |
| Rectangle | x | Typed binding for x in Rectangle; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 28 |
| Rectangle | y | Typed binding for y in Rectangle; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 29 |
| Rectangle | width | Typed binding for width in Rectangle; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 30 |
| Rectangle | height | Typed binding for height in Rectangle; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 31 |
| Layout | model_config | Local binding for model config in Layout; use the enclosing contract and type below. | Return type of ConfigDict; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| Layout | version | Typed binding for version in Layout; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 38 |
| Layout | positions | Typed binding for positions in Layout; use the enclosing contract and type below. | dict[str, Rectangle] | Enclosing invocation or class/instance lifetime | 39 |
| Layout | hidden | Typed binding for hidden in Layout; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 40 |
| Layout.known_controls | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| Layout.known_controls | positions | Parameter for positions in Layout.known_controls; use the enclosing contract and type below. | dict[str, Rectangle] | Enclosing invocation or class/instance lifetime | 45 |
| Layout.known_controls | info | Parameter for info in Layout.known_controls; use the enclosing contract and type below. | ValidationInfo | Enclosing invocation or class/instance lifetime | 45 |
| Layout.known_controls | allowed | Local binding for allowed in Layout.known_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| Layout.known_controls | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 53 |
| Layout.known_hidden_controls | cls | Class receiving this class-level operation. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| Layout.known_hidden_controls | hidden | Parameter for hidden in Layout.known_hidden_controls; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 61 |
| Layout.known_hidden_controls | info | Parameter for info in Layout.known_hidden_controls; use the enclosing contract and type below. | ValidationInfo | Enclosing invocation or class/instance lifetime | 61 |
| Layout.known_hidden_controls | allowed | Local binding for allowed in Layout.known_hidden_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 68 |
| Layout.known_hidden_controls | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 73 |
| validate_layout | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 79 |
| validate_layout | allowed | Parameter for allowed in validate_layout; use the enclosing contract and type below. | set[str] &#124; None | Enclosing invocation or class/instance lifetime | 79 |
| application_layout_groups | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 86 |
| application_layout_groups | ElementIds | Imported dependency for ElementIds in application_layout_groups; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 96 |
| application_layout_groups | registry | Local binding for registry in application_layout_groups; use the enclosing contract and type below. | Return type of ElementIds; see its callable contract | Enclosing invocation or class/instance lifetime | 98 |
| application_layout_groups | groups | Local binding for groups in application_layout_groups; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 99 |
| application_layout_groups.comprehension_100 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 102 |
| application_layout_groups | node | Loop item for node in application_layout_groups; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| application_layout_groups | parameters | Local binding for parameters in application_layout_groups; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| application_layout_groups | scope | Local binding for scope in application_layout_groups; use the enclosing contract and type below. | Return type of new_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| application_layout_groups | role | Loop item for role in application_layout_groups; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 107 |
| application_layout_ids | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 112 |
| application_layout_ids | ElementIds | Imported dependency for ElementIds in application_layout_ids; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 121 |
| application_layout_ids | registry | Local binding for registry in application_layout_ids; use the enclosing contract and type below. | Return type of ElementIds; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| application_layout_ids | allowed | Local binding for allowed in application_layout_ids; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 124 |
| application_layout_ids.comprehension_125 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 125 |
| application_layout_ids | node | Loop item for node in application_layout_ids; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 126 |
| application_layout_ids | parameters | Local binding for parameters in application_layout_ids; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| application_layout_ids | scope | Local binding for scope in application_layout_ids; use the enclosing contract and type below. | Return type of new_widget; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| application_layout_ids | roles | Local binding for roles in application_layout_ids; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 129 |
| application_layout_ids.comprehension_130 | role | Comprehension item for role in application_layout_ids.comprehension_130; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 130 |
