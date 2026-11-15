# Reference for tests/test_v7_067_application_web_and_edit.py

V7-067: separate web tab, Edit affordances, legend and code-help file identity.

Source fingerprint: 6b391a90a5ffa3826b6cd40c572c215b0cd0ae2491c81686413c6cc7f38c0c6b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_v7_067_frame_offers_a_separate_tab_and_labels_the_section

The heading link reuses the validated origin and the name only labels the section.

Kind: callable. Declared return: None. Source line: 8.

### test_v7_067_isolated_page_titles_itself_from_the_staged_name

The child renders the owner's name server-side; no query string or eval is involved.

Kind: callable. Declared return: None. Source line: 27.

### test_v7_067_editor_legend_surfaces_and_visible_checkbox

Edit shows the legend, the default surface, the shifted label and a visible checkbox.

Kind: callable. Declared return: None. Source line: 58.

### test_v7_067_editor_legend_surfaces_and_visible_checkbox.route

Serve inert HTML and one fixed authorized layout payload.

Kind: callable. Declared return: None. Source line: 96.

### test_v7_067_editor_legend_surfaces_and_visible_checkbox.style

Read one computed style value from the real maintained stylesheet.

Kind: callable. Declared return: str. Source line: 112.

### test_v7_067_code_help_names_the_selected_file

The helper names the pane's real file and follows a later file selection.

Kind: callable. Declared return: None. Source line: 208.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_v7_067_frame_offers_a_separate_tab_and_labels_the_section | generated_application_frame | Imported dependency for generated application frame in test_v7_067_frame_offers_a_separate_tab_and_labels_the_section; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_v7_067_frame_offers_a_separate_tab_and_labels_the_section | frame | Local binding for frame in test_v7_067_frame_offers_a_separate_tab_and_labels_the_section; use the enclosing contract and type below. | Return type of generated_application_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_v7_067_frame_offers_a_separate_tab_and_labels_the_section | injected | Local binding for injected in test_v7_067_frame_offers_a_separate_tab_and_labels_the_section; use the enclosing contract and type below. | Return type of generated_application_frame; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | tmp_path | Parameter for tmp path in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | json | Imported dependency for json in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 29 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | make_code_candidate | Imported dependency for make code candidate in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | approve_application | Imported dependency for approve application in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | ApplicationSession | Imported dependency for ApplicationSession in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 34 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | item | Local binding for item in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of make_code_candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | approved | Local binding for approved in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | named | Local binding for named in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | config | Local binding for config in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 41, 50 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | heading | Local binding for heading in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 42, 51 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_42 | component | Comprehension item for component in test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_42; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_44 | dependency | Comprehension item for dependency in test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_44; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 44 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name | unnamed | Local binding for unnamed in test_v7_067_isolated_page_titles_itself_from_the_staged_name; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_51 | component | Comprehension item for component in test_v7_067_isolated_page_titles_itself_from_the_staged_name.comprehension_51; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 51 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | os | Imported dependency for os in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | expect | Imported dependency for expect in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 62 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | sync_playwright | Imported dependency for sync playwright in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 62 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | application_layout_groups | Imported dependency for application layout groups in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 64 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | application_layout_ids | Imported dependency for application layout ids in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 64 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | manifest | Versioned inventory or launch record; not an execution-authorization capability. | dict | Enclosing invocation or class/instance lifetime | 66 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | allowed | Local binding for allowed in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of application_layout_ids; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | groups | Local binding for groups in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of application_layout_groups; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | positions | Local binding for positions in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 81 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.comprehension_81 | index | Comprehension item for index in test_v7_067_editor_legend_surfaces_and_visible_checkbox.comprehension_81; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.comprehension_81 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 83 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | html | Local binding for html in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.comprehension_88 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 91 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.route | request_route | Parameter for request route in test_v7_067_editor_legend_surfaces_and_visible_checkbox.route; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.route | request | Local binding for request in test_v7_067_editor_legend_surfaces_and_visible_checkbox.route; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.style | page | Parameter for page in test_v7_067_editor_legend_surfaces_and_visible_checkbox.style; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.style | selector | Parameter for selector in test_v7_067_editor_legend_surfaces_and_visible_checkbox.style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 112 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox.style | prop | Parameter for prop in test_v7_067_editor_legend_surfaces_and_visible_checkbox.style; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 112 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | driver | Managed resource for driver in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 120 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | browser | Local binding for browser in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | page | Local binding for page in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | legend | Local binding for legend in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 141 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | canvas | Local binding for canvas in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | edit | Local binding for edit in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of bounding_box; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | rows | Local binding for rows in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | toggle | Local binding for toggle in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of get_by_label; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | handle | Local binding for handle in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of style; see its callable contract | Enclosing invocation or class/instance lifetime | 181 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | swatches | Local binding for swatches in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| test_v7_067_editor_legend_surfaces_and_visible_checkbox | colors | Local binding for colors in test_v7_067_editor_legend_surfaces_and_visible_checkbox; use the enclosing contract and type below. | Return type of evaluate_all; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_v7_067_code_help_names_the_selected_file | os | Imported dependency for os in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 210 |
| test_v7_067_code_help_names_the_selected_file | expect | Imported dependency for expect in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 212 |
| test_v7_067_code_help_names_the_selected_file | sync_playwright | Imported dependency for sync playwright in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 212 |
| test_v7_067_code_help_names_the_selected_file | html | Local binding for html in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 214 |
| test_v7_067_code_help_names_the_selected_file | driver | Managed resource for driver in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 223 |
| test_v7_067_code_help_names_the_selected_file | browser | Local binding for browser in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| test_v7_067_code_help_names_the_selected_file | page | Local binding for page in test_v7_067_code_help_names_the_selected_file; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
