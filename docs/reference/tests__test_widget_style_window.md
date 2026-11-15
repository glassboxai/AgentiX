# Reference for tests/test_widget_style_window.py

The right-click style window is driven by the framed widget and the parent bridge.

Source fingerprint: 5ae15619921649b695cbe3de1de9533b5636de497f473a0e04c98e51bd060e73

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_v7_076_editor_posts_the_right_clicked_widget_tool

Only a widget control of one tool reports its tool name for styling.

Kind: callable. Declared return: None. Source line: 11.

### test_v7_076_editor_posts_the_right_clicked_widget_tool.route

Serve inert HTML and the authorized layout payload.

Kind: callable. Declared return: None. Source line: 41.

### test_v7_076_saved_stylesheet_is_applied_to_the_live_widget

The parent bridge pushes the merged CSS and the framed widget restyles.

Kind: callable. Declared return: None. Source line: 91.

### test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.route

Serve the parent shell, the framed preview and its layout payload.

Kind: callable. Declared return: None. Source line: 129.

### test_v7_076_window_can_be_dragged_by_its_title

The overlay follows the pointer from its title bar and stays on screen.

The real ``style.css`` is loaded on purpose: its ``!important`` position rules
are what made an inline left/top drag jump and freeze.

Kind: callable. Declared return: None. Source line: 203.

### test_v7_076_window_can_be_dragged_by_its_title.route

Serve one inert overlay page with the maintained stylesheet.

Kind: callable. Declared return: None. Source line: 220.

### test_v7_076_served_stylesheet_applies_without_the_parent_bridge

The standalone page behind "View as web" renders the saved style on its own.

Kind: callable. Declared return: None. Source line: 260.

### test_v7_076_served_stylesheet_applies_without_the_parent_bridge.route

Serve one inert standalone page with the served stylesheet only.

Kind: callable. Declared return: None. Source line: 280.

### test_v7_077_field_and_caption_are_styled_in_the_served_page

The field box and the caption get their own colour, family and size.

Kind: callable. Declared return: None. Source line: 307.

### test_v7_077_field_and_caption_are_styled_in_the_served_page.route

Serve one inert standalone page with the served stylesheet only.

Kind: callable. Declared return: None. Source line: 330.

### test_v7_076_saved_web_style_overrides_gradio_startup_snapshot

A web reload must beat Gradio's earlier, more specific startup copy.

Kind: callable. Declared return: None. Source line: 356.

### test_v7_077_window_is_compact_and_scrolls_inside_itself

The window stays narrow and scrolls with the shared thin scrollbar.

Kind: callable. Declared return: None. Source line: 416.

### test_v7_077_window_is_compact_and_scrolls_inside_itself.route

Serve one inert overlay page with the maintained stylesheet.

Kind: callable. Declared return: None. Source line: 433.

### test_v7_077_caption_font_reaches_the_span_and_spares_the_grip

The served sheet styles the caption text, not the layout grip glyph.

Kind: callable. Declared return: None. Source line: 460.

### test_v7_077_caption_font_reaches_the_span_and_spares_the_grip.route

Serve one inert standalone page with the served stylesheet only.

Kind: callable. Declared return: None. Source line: 481.

### test_v7_076_parent_opens_the_window_from_a_frame_message

Only the framed application's valid tool name reaches the hidden opener.

Kind: callable. Declared return: None. Source line: 505.

### test_v7_076_parent_opens_the_window_from_a_frame_message.route

Serve the parent page and one inert framed child.

Kind: callable. Declared return: None. Source line: 524.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ASSETS | Module binding for ASSETS in module; use the enclosing contract and type below. | Return type of Path; see its callable contract | Module/process lifetime | 7 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | os | Imported dependency for os in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | sync_playwright | Imported dependency for sync playwright in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 15 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | application_layout_groups | Imported dependency for application layout groups in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 17 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | application_layout_ids | Imported dependency for application layout ids in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 17 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 19 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | allowed | Local binding for allowed in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | groups | Local binding for groups in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | positions | Local binding for positions in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 27 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool.comprehension_27 | index | Comprehension item for index in test_v7_076_editor_posts_the_right_clicked_widget_tool.comprehension_27; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 29 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool.comprehension_27 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 29 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | html | Local binding for html in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool.comprehension_34 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 36 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool.route | request_route | Parameter for request route in test_v7_076_editor_posts_the_right_clicked_widget_tool.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 41 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | driver | Managed resource for driver in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 56 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | browser | Local binding for browser in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_v7_076_editor_posts_the_right_clicked_widget_tool | page | Local binding for page in test_v7_076_editor_posts_the_right_clicked_widget_tool; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | json | Imported dependency for json in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 93 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | os | Imported dependency for os in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 94 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | sync_playwright | Imported dependency for sync playwright in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 96 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | application_layout_groups | Imported dependency for application layout groups in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | application_layout_ids | Imported dependency for application layout ids in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 100 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | allowed | Local binding for allowed in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 106 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | groups | Local binding for groups in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 107 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | positions | Local binding for positions in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 108 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.comprehension_108 | index | Comprehension item for index in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.comprehension_108; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 110 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.comprehension_108 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 110 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | child | Local binding for child in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.comprehension_116 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | parent | Local binding for parent in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 124 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.route | request_route | Parameter for request route in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.route | url | Local binding for url in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 131 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | css | Local binding for css in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 147 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | driver | Managed resource for driver in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 152 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | browser | Local binding for browser in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | page | Local binding for page in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | frame | Local binding for frame in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of frame_locator; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | applied | Local binding for applied in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 175 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | value_and_caption | Local binding for value and caption in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| test_v7_076_saved_stylesheet_is_applied_to_the_live_widget | changed | Local binding for changed in test_v7_076_saved_stylesheet_is_applied_to_the_live_widget; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 185 |
| test_v7_076_window_can_be_dragged_by_its_title | os | Imported dependency for os in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 209 |
| test_v7_076_window_can_be_dragged_by_its_title | sync_playwright | Imported dependency for sync playwright in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| test_v7_076_window_can_be_dragged_by_its_title | stylesheet | Local binding for stylesheet in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 213 |
| test_v7_076_window_can_be_dragged_by_its_title | html | Local binding for html in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 214 |
| test_v7_076_window_can_be_dragged_by_its_title.route | request_route | Parameter for request route in test_v7_076_window_can_be_dragged_by_its_title.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 220 |
| test_v7_076_window_can_be_dragged_by_its_title | driver | Managed resource for driver in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 224 |
| test_v7_076_window_can_be_dragged_by_its_title | browser | Local binding for browser in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 225 |
| test_v7_076_window_can_be_dragged_by_its_title | page | Local binding for page in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 229 |
| test_v7_076_window_can_be_dragged_by_its_title | dialog | Local binding for dialog in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 233 |
| test_v7_076_window_can_be_dragged_by_its_title | title | Local binding for title in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 234 |
| test_v7_076_window_can_be_dragged_by_its_title | start | Local binding for start in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 235 |
| test_v7_076_window_can_be_dragged_by_its_title | box | Local binding for box in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 236, 248 |
| test_v7_076_window_can_be_dragged_by_its_title | nudged | Local binding for nudged in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 240 |
| test_v7_076_window_can_be_dragged_by_its_title | moved | Local binding for moved in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 245 |
| test_v7_076_window_can_be_dragged_by_its_title | clamped | Local binding for clamped in test_v7_076_window_can_be_dragged_by_its_title; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 253 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | os | Imported dependency for os in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 262 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | sync_playwright | Imported dependency for sync playwright in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 264 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | served_style | Imported dependency for served style in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 266 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | css | Local binding for css in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 268 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | served | Local binding for served in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 272 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | html | Local binding for html in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge.route | request_route | Parameter for request route in test_v7_076_served_stylesheet_applies_without_the_parent_bridge.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 280 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | driver | Managed resource for driver in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 284 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | browser | Local binding for browser in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 285 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | page | Local binding for page in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 289 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | node | Local binding for node in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 293 |
| test_v7_076_served_stylesheet_applies_without_the_parent_bridge | control | Local binding for control in test_v7_076_served_stylesheet_applies_without_the_parent_bridge; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | os | Imported dependency for os in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 309 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | sync_playwright | Imported dependency for sync playwright in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 311 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | served_style | Imported dependency for served style in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 313 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | StyleValues | Imported dependency for StyleValues in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 314 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | merge_style | Imported dependency for merge style in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 314 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | default_widget_css | Imported dependency for default widget css in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | merged | Local binding for merged in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 317 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | served | Local binding for served in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 322 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | html | Local binding for html in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 323 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page.route | request_route | Parameter for request route in test_v7_077_field_and_caption_are_styled_in_the_served_page.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 330 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | driver | Managed resource for driver in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 334 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | browser | Local binding for browser in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | page | Local binding for page in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | field | Local binding for field in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 343 |
| test_v7_077_field_and_caption_are_styled_in_the_served_page | caption | Local binding for caption in test_v7_077_field_and_caption_are_styled_in_the_served_page; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 347 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | tmp_path | Parameter for tmp path in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 356 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | os | Imported dependency for os in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 358 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | SimpleNamespace | Imported dependency for SimpleNamespace in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 359 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | sync_playwright | Imported dependency for sync playwright in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 361 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | STYLE_MARKER | Imported dependency for STYLE MARKER in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 363 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | ApplicationSession | Imported dependency for ApplicationSession in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 363 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | served_style | Imported dependency for served style in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 363 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | StyleValues | Imported dependency for StyleValues in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 364 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | merge_style | Imported dependency for merge style in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 364 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | default_widget_css | Imported dependency for default widget css in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 365 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | original | Local binding for original in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 367 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | updated | Local binding for updated in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of merge_style; see its callable contract | Enclosing invocation or class/instance lifetime | 372 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | startup | Local binding for startup in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 377 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | session | Local binding for session in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of __new__; see its callable contract | Enclosing invocation or class/instance lifetime | 378 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | session.root | Attribute for session.root in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 379 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | session.application | Attribute for session.application in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 380 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | session.manifest | Attribute for session.manifest in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 381 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | latest | Local binding for latest in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 384 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | prefixed | Local binding for prefixed in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 385 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | html | Local binding for html in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 389 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | driver | Managed resource for driver in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 395 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | browser | Local binding for browser in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 396 |
| test_v7_076_saved_web_style_overrides_gradio_startup_snapshot | page | Local binding for page in test_v7_076_saved_web_style_overrides_gradio_startup_snapshot; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 400 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | os | Imported dependency for os in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 418 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | sync_playwright | Imported dependency for sync playwright in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 420 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | stylesheet | Local binding for stylesheet in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 422 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | rows | Local binding for rows in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 423 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself.comprehension_423 | index | Comprehension item for index in test_v7_077_window_is_compact_and_scrolls_inside_itself.comprehension_423; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 425 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | html | Local binding for html in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 427 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself.route | request_route | Parameter for request route in test_v7_077_window_is_compact_and_scrolls_inside_itself.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 433 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | driver | Managed resource for driver in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 437 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | browser | Local binding for browser in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 438 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | page | Local binding for page in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 442 |
| test_v7_077_window_is_compact_and_scrolls_inside_itself | measured | Local binding for measured in test_v7_077_window_is_compact_and_scrolls_inside_itself; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 445 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | os | Imported dependency for os in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 462 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | sync_playwright | Imported dependency for sync playwright in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 464 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | served_style | Imported dependency for served style in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 466 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | css | Local binding for css in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 468 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | served | Local binding for served in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 472 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | html | Local binding for html in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 473 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip.route | request_route | Parameter for request route in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 481 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | driver | Managed resource for driver in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 485 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | browser | Local binding for browser in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 486 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | page | Local binding for page in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 490 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | caption | Local binding for caption in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 494 |
| test_v7_077_caption_font_reaches_the_span_and_spares_the_grip | grip | Local binding for grip in test_v7_077_caption_font_reaches_the_span_and_spares_the_grip; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 498 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | os | Imported dependency for os in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 507 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | expect | Imported dependency for expect in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 509 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | sync_playwright | Imported dependency for sync playwright in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 509 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | html | Local binding for html in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 511 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | child | Local binding for child in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 519 |
| test_v7_076_parent_opens_the_window_from_a_frame_message.route | request_route | Parameter for request route in test_v7_076_parent_opens_the_window_from_a_frame_message.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 524 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | driver | Managed resource for driver in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 531 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | browser | Local binding for browser in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 532 |
| test_v7_076_parent_opens_the_window_from_a_frame_message | page | Local binding for page in test_v7_076_parent_opens_the_window_from_a_frame_message; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 536 |
