# Reference for src/agentix/ui/widget_style_dialog.py

Overlay window that edits one widget's scoped stylesheet from a right-click.

Presentation only: the window collects six values, the backend merges them into
``<tool>_widget.css`` and the review service persists the file. Gradio 6 has no
modal component, so the window is a hidden column positioned by ``style.css``.

Source fingerprint: edd0aab519aeca307eb7747f6040a3591f76a4bee3877ec9feb90b926b2f2a3b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### WidgetStyleDialog

Hidden overlay bound to one widget stylesheet, opened by the parent bridge.

Kind: class. Declared return: Not declared / class. Source line: 13.

### WidgetStyleDialog.__init__

Build the window and wire open, save and cancel; no IO happens here.

Kind: callable. Declared return: None. Source line: 16.

### WidgetStyleDialog._opened

Reveal the window with the stored values of the right-clicked widget.

The container output must be an update, not a value: Gradio renders a
hidden column only when an update makes it visible.

Kind: callable. Declared return: tuple. Source line: 145.

### WidgetStyleDialog.outputs

Expose the window outputs the open handler fills in one row.

Kind: callable. Declared return: list. Source line: 179.

### WidgetStyleDialog._saved

Persist the style, close the window and hand the merged CSS to the bridge.

A rejected value raises before the update is produced, so the window stays
open with the user's input instead of closing on a failed save.

Kind: callable. Declared return: tuple. Source line: 196.

### WidgetStyleDialog.hide

Close the window; the collected values stay until the next open.

Kind: callable. Declared return: Any. Source line: 232.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | FONTS | Imported dependency for FONTS in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| WidgetStyleDialog.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| WidgetStyleDialog.__init__ | gr | Parameter for gr in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| WidgetStyleDialog.__init__ | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 16 |
| WidgetStyleDialog.__init__ | bind | Parameter for bind in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| WidgetStyleDialog.__init__ | session_state | Parameter for session state in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 16 |
| WidgetStyleDialog.__init__ | self._gr | Attribute for gr in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 18 |
| WidgetStyleDialog.__init__ | self.session_state | Attribute for session state in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 19 |
| WidgetStyleDialog.__init__ | self.backend | Injected framework/execution provider; callers determine the required protocol. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 20 |
| WidgetStyleDialog.__init__ | self.tool | Attribute for tool in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| WidgetStyleDialog.__init__ | self.open | Attribute for open in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| WidgetStyleDialog.__init__ | self.apply | Attribute for apply in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| WidgetStyleDialog.__init__ | container | Managed resource for container in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Column; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 36 |
| WidgetStyleDialog.__init__ | self.container | Attribute for container in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| WidgetStyleDialog.__init__ | self.status | Attribute for status in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| WidgetStyleDialog.__init__ | self.radius | Attribute for radius in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| WidgetStyleDialog.__init__ | self.width | Attribute for width in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| WidgetStyleDialog.__init__ | self.border_color | Attribute for border color in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of ColorPicker; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| WidgetStyleDialog.__init__ | self.background | Attribute for background in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of ColorPicker; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| WidgetStyleDialog.__init__ | self.font_family | Attribute for font family in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| WidgetStyleDialog.__init__ | self.font_size | Attribute for font size in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| WidgetStyleDialog.__init__ | self.field_background | Attribute for field background in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of ColorPicker; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| WidgetStyleDialog.__init__ | self.label_font_family | Attribute for label font family in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| WidgetStyleDialog.__init__ | self.label_font_size | Attribute for label font size in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| WidgetStyleDialog.__init__ | self.save | Attribute for save in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 109 |
| WidgetStyleDialog.__init__ | self.cancel | Attribute for cancel in WidgetStyleDialog.__init__; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| WidgetStyleDialog._opened | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| WidgetStyleDialog._opened | tool | Parameter for tool in WidgetStyleDialog._opened; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 145 |
| WidgetStyleDialog._opened | token | Parameter for token in WidgetStyleDialog._opened; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 145 |
| WidgetStyleDialog._opened | request | Parameter for request in WidgetStyleDialog._opened; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 145 |
| WidgetStyleDialog._opened | status | Local binding for status in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | radius | Local binding for radius in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | width | Local binding for width in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | border | Local binding for border in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | background | Local binding for background in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | font | Local binding for font in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | size | Local binding for size in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | field | Local binding for field in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | label_font | Local binding for label font in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | label_size | Local binding for label size in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog._opened | token_out | Local binding for token out in WidgetStyleDialog._opened; use the enclosing contract and type below. | Return type of load; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| WidgetStyleDialog.outputs | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 179 |
| WidgetStyleDialog._saved | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 197 |
| WidgetStyleDialog._saved | tool | Parameter for tool in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 198 |
| WidgetStyleDialog._saved | radius | Parameter for radius in WidgetStyleDialog._saved; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 199 |
| WidgetStyleDialog._saved | width | Parameter for width in WidgetStyleDialog._saved; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 200 |
| WidgetStyleDialog._saved | border_color | Parameter for border color in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 201 |
| WidgetStyleDialog._saved | background | Parameter for background in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 202 |
| WidgetStyleDialog._saved | font_family | Parameter for font family in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 203 |
| WidgetStyleDialog._saved | font_size | Parameter for font size in WidgetStyleDialog._saved; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 204 |
| WidgetStyleDialog._saved | field_background | Parameter for field background in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 205 |
| WidgetStyleDialog._saved | label_font_family | Parameter for label font family in WidgetStyleDialog._saved; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 206 |
| WidgetStyleDialog._saved | label_font_size | Parameter for label font size in WidgetStyleDialog._saved; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 207 |
| WidgetStyleDialog._saved | token | Parameter for token in WidgetStyleDialog._saved; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 208 |
| WidgetStyleDialog._saved | request | Parameter for request in WidgetStyleDialog._saved; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 209 |
| WidgetStyleDialog._saved | message | Local binding for message in WidgetStyleDialog._saved; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| WidgetStyleDialog._saved | token_out | Local binding for token out in WidgetStyleDialog._saved; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| WidgetStyleDialog._saved | payload | Local binding for payload in WidgetStyleDialog._saved; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 216 |
| WidgetStyleDialog.hide | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 232 |
