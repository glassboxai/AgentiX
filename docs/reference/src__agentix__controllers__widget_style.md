# Reference for src/agentix/controllers/widget_style.py

Owner-scoped widget style window backend; persistence stays in the review service.

The backend only resolves the caller's own proposal, reads the scoped stylesheet and
merges the six edited declarations. Writing goes through
:meth:`ApplicationsBackend.save_file`, so the revocation rule and the ownership lock
keep exactly one implementation.

Source fingerprint: 172bfdde4c0e70c85709d530ab629b6f5476f862c1589975ecf1c625fb837a0c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### WidgetStyleBackend

Load and save the editable declarations of one widget stylesheet.

Kind: class. Declared return: Not declared / class. Source line: 19.

### WidgetStyleBackend.__init__

Bind the applications backend that owns proposals and their lock.

Kind: callable. Declared return: None. Source line: 22.

### WidgetStyleBackend.load

Return the window's initial values for the widget the owner right-clicked.

Kind: callable. Declared return: tuple. Source line: 26.

### WidgetStyleBackend.save

Merge the edited values into the scoped stylesheet and persist them.

Raises ``ValueError`` for an unknown widget, an out-of-range value or a busy
session. Returns the persistence message, the refreshed session token and the
merged stylesheet as a JSON payload the parent bridge applies to the live
preview, so the widget changes without reopening it.

Kind: callable. Declared return: tuple[str, str]. Source line: 47.

### WidgetStyleBackend._instance_ids

Map one tool to the widget instance ids the preview scopes its CSS to.

Kind: callable. Declared return: list[str]. Source line: 97.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | style_member_name | Imported dependency for style member name in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | StyleValues | Imported dependency for StyleValues in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | merge_style | Imported dependency for merge style in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | read_style | Imported dependency for read style in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 16 |
| WidgetStyleBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| WidgetStyleBackend.__init__ | applications | Parameter for applications in WidgetStyleBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| WidgetStyleBackend.__init__ | self.applications | Attribute for applications in WidgetStyleBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| WidgetStyleBackend.load | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| WidgetStyleBackend.load | tool | Parameter for tool in WidgetStyleBackend.load; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 26 |
| WidgetStyleBackend.load | token | Parameter for token in WidgetStyleBackend.load; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 26 |
| WidgetStyleBackend.load | request | Parameter for request in WidgetStyleBackend.load; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 26 |
| WidgetStyleBackend.load | session | Local binding for session in WidgetStyleBackend.load; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| WidgetStyleBackend.load | _ | Local binding for  in WidgetStyleBackend.load; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| WidgetStyleBackend.load | candidate | Local binding for candidate in WidgetStyleBackend.load; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 28 |
| WidgetStyleBackend.load | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of style_member_name; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| WidgetStyleBackend.load | css | Local binding for css in WidgetStyleBackend.load; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| WidgetStyleBackend.load | values | Local binding for values in WidgetStyleBackend.load; use the enclosing contract and type below. | Return type of read_style; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| WidgetStyleBackend.save | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 48 |
| WidgetStyleBackend.save | tool | Parameter for tool in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 49 |
| WidgetStyleBackend.save | radius | Parameter for radius in WidgetStyleBackend.save; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 50 |
| WidgetStyleBackend.save | width | Parameter for width in WidgetStyleBackend.save; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 51 |
| WidgetStyleBackend.save | border_color | Parameter for border color in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 52 |
| WidgetStyleBackend.save | background | Parameter for background in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 53 |
| WidgetStyleBackend.save | font_family | Parameter for font family in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 54 |
| WidgetStyleBackend.save | font_size | Parameter for font size in WidgetStyleBackend.save; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 55 |
| WidgetStyleBackend.save | field_background | Parameter for field background in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 56 |
| WidgetStyleBackend.save | label_font_family | Parameter for label font family in WidgetStyleBackend.save; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 57 |
| WidgetStyleBackend.save | label_font_size | Parameter for label font size in WidgetStyleBackend.save; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 58 |
| WidgetStyleBackend.save | token | Parameter for token in WidgetStyleBackend.save; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 59 |
| WidgetStyleBackend.save | request | Parameter for request in WidgetStyleBackend.save; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 60 |
| WidgetStyleBackend.save | session | Local binding for session in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| WidgetStyleBackend.save | _ | Local binding for  in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 69, 84 |
| WidgetStyleBackend.save | candidate | Local binding for candidate in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of owned_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| WidgetStyleBackend.save | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of style_member_name; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| WidgetStyleBackend.save | css | Local binding for css in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| WidgetStyleBackend.save | values | Local binding for values in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of StyleValues; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| WidgetStyleBackend.save | merged | Local binding for merged in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| WidgetStyleBackend.save | message | Local binding for message in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of save_file; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| WidgetStyleBackend.save | token_out | Local binding for token out in WidgetStyleBackend.save; use the enclosing contract and type below. | Return type of save_file; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| WidgetStyleBackend._instance_ids | package | Parameter for package in WidgetStyleBackend._instance_ids; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 97 |
| WidgetStyleBackend._instance_ids | tool | Parameter for tool in WidgetStyleBackend._instance_ids; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 97 |
| WidgetStyleBackend._instance_ids | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| WidgetStyleBackend._instance_ids | ids | Local binding for ids in WidgetStyleBackend._instance_ids; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 101, 107 |
| WidgetStyleBackend._instance_ids.comprehension_101 | node | Comprehension item for node in WidgetStyleBackend._instance_ids.comprehension_101; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 103 |
