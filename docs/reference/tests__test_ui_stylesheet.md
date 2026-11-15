# Reference for tests/test_ui_stylesheet.py

Readable inline code inside Gradio markdown for the maintained dark palette.

Source fingerprint: 8ddfbb23ba26f517348f124186f470298c83240e5b217441dc0c2c441e6f2336

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_stylesheet_defines_dark_inline_code_colors

Catch white-on-white inline code such as File, Action and Stored package values.

Kind: callable. Declared return: None. Source line: 6.

### test_stylesheet_hides_collapsed_group_wrappers_while_editing

Catch Gradio 6 gr-group borders and fill left visible once children are absolute.

Kind: callable. Declared return: None. Source line: 17.

### test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable

Catch a transparent Edit surface, a hidden checkbox or an unstyled legend.

Kind: callable. Declared return: None. Source line: 30.

### test_stylesheet_keeps_right_tab_sidebars_resizable

Catch a right sidebar without its own width, inner border or drag handle.

Kind: callable. Declared return: None. Source line: 63.

### test_stylesheet_is_the_only_served_asset

Keep the maintained stylesheet inside the packaged UI assets directory.

Kind: callable. Declared return: None. Source line: 79.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| test_stylesheet_defines_dark_inline_code_colors | stylesheet | Imported dependency for stylesheet in test_stylesheet_defines_dark_inline_code_colors; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 8 |
| test_stylesheet_defines_dark_inline_code_colors | css | Local binding for css in test_stylesheet_defines_dark_inline_code_colors; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 10 |
| test_stylesheet_hides_collapsed_group_wrappers_while_editing | stylesheet | Imported dependency for stylesheet in test_stylesheet_hides_collapsed_group_wrappers_while_editing; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 19 |
| test_stylesheet_hides_collapsed_group_wrappers_while_editing | css | Local binding for css in test_stylesheet_hides_collapsed_group_wrappers_while_editing; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_stylesheet_hides_collapsed_group_wrappers_while_editing | rule | Local binding for rule in test_stylesheet_hides_collapsed_group_wrappers_while_editing; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22 |
| test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable | stylesheet | Imported dependency for stylesheet in test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 32 |
| test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable | css | Local binding for css in test_stylesheet_keeps_edit_surfaces_and_the_color_legend_readable; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_stylesheet_keeps_right_tab_sidebars_resizable | stylesheet | Imported dependency for stylesheet in test_stylesheet_keeps_right_tab_sidebars_resizable; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 65 |
| test_stylesheet_keeps_right_tab_sidebars_resizable | css | Local binding for css in test_stylesheet_keeps_right_tab_sidebars_resizable; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_stylesheet_is_the_only_served_asset | branding | Imported dependency for branding in test_stylesheet_is_the_only_served_asset; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 81 |
