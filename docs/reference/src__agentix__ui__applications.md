# Reference for src/agentix/ui/applications.py

Applications controls; owner-bound review and execution live in the backend.

Source fingerprint: 01b92860a86f45e8b410d1080ef0e2c5711fbc1a09e14a40f7f967ca5513ac52

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### widget_source_name

Resolve a double-clicked widget tool to its reviewed widget source filename.

Only a canonical tool identifier is accepted, so browser text never becomes a path.

Kind: callable. Declared return: str. Source line: 23.

### _build_application_workspace

Present approved catalog dependencies, readable review and the framed preview.

Kind: callable. Declared return: None. Source line: 33.

### _build_application_workspace.run_typed_data

Present approved structured data as typed results, without generating a tool.

Kind: callable. Declared return: Not declared / class. Source line: 224.

### _build_application_workspace.show_data_contract

Show the loaded application's declared inputs without executing it.

Kind: callable. Declared return: Not declared / class. Source line: 266.

### _build_application_workspace.refresh_review

Reset to a readable composition file after generating/saving a revision.

Kind: callable. Declared return: Not declared / class. Source line: 301.

### _build_application_workspace.select_file

Show a coherent triplet for any implementation/widget/tests selection.

Kind: callable. Declared return: Not declared / class. Source line: 328.

### _build_application_workspace.select_widget_file

Open <tool>_widget.py and its three panes for a double-clicked widget.

Kind: callable. Declared return: Not declared / class. Source line: 379.

### _build_application_workspace.edited_file

Require explicit save rather than approving an older displayed snapshot.

Kind: callable. Declared return: Not declared / class. Source line: 388.

### _build_application_workspace.edited_group

A change in any pane clears the old review checkbox.

Kind: callable. Declared return: Not declared / class. Source line: 401.

### _build_application_workspace.poll_application

Update owned lifecycle and repair visibility without progress flicker.

Kind: callable. Declared return: Not declared / class. Source line: 490.

### build_applications_frontend

Compose a full-width workspace and one collapsible right sidebar for the catalog.

Kind: callable. Declared return: None. Source line: 540.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | named_result_rows | Imported dependency for named result rows in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | build_apps_catalog | Imported dependency for build apps catalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | ResultField | Imported dependency for ResultField in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | build_results | Imported dependency for build results in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | result_values | Imported dependency for result values in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | APPLICATION_POLL_SECONDS | Module binding for APPLICATION POLL SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 10 |
| module | QUERY_INPUT_LINES | Module binding for QUERY INPUT LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 11 |
| module | REQUIREMENTS_INPUT_LINES | Module binding for REQUIREMENTS INPUT LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 12 |
| module | SOURCE_EDITOR_LINES | Module binding for SOURCE EDITOR LINES in module; use the enclosing contract and type below. | int | Module/process lifetime | 13 |
| module | WORKSPACE_COLUMN_SCALE | Module binding for WORKSPACE COLUMN SCALE in module; use the enclosing contract and type below. | int | Module/process lifetime | 14 |
| module | WORKSPACE_COLUMN_MIN_WIDTH | Module binding for WORKSPACE COLUMN MIN WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 15 |
| module | APPLICATIONS_SIDEBAR_WIDTH_PIXELS | Module binding for APPLICATIONS SIDEBAR WIDTH PIXELS in module; use the enclosing contract and type below. | int | Module/process lifetime | 16 |
| module | REVIEW_OUTPUT_COUNT | Module binding for REVIEW OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 17 |
| module | SELECTION_OUTPUT_COUNT | Module binding for SELECTION OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 18 |
| module | POLL_OUTPUT_COUNT | Module binding for POLL OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 19 |
| module | WIDGET_TOOL_NAME | Module binding for WIDGET TOOL NAME in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 20 |
| widget_source_name | tool | Parameter for tool in widget_source_name; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 23 |
| _build_application_workspace | gr | Parameter for gr in _build_application_workspace; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| _build_application_workspace | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 34 |
| _build_application_workspace | bind | Parameter for bind in _build_application_workspace; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| _build_application_workspace | session_state | Parameter for session state in _build_application_workspace; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| _build_application_workspace | progress | Parameter for progress in _build_application_workspace; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| _build_application_workspace | dialog | Parameter for dialog in _build_application_workspace; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34, 60 |
| _build_application_workspace | operation | Local binding for operation in _build_application_workspace; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| _build_application_workspace | application_name | Local binding for application name in _build_application_workspace; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| _build_application_workspace | query | Original user request or a trusted test query; avoid payload logging by default. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| _build_application_workspace | generate | Local binding for generate in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| _build_application_workspace | status | Local binding for status in _build_application_workspace; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| _build_application_workspace | WidgetStyleBackend | Imported dependency for WidgetStyleBackend in _build_application_workspace; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| _build_application_workspace | WidgetStyleDialog | Imported dependency for WidgetStyleDialog in _build_application_workspace; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 53 |
| _build_application_workspace | MessageDialog | Imported dependency for MessageDialog in _build_application_workspace; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 57 |
| _build_application_workspace | identity | Explicit owner identity used by a session factory or fixture. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| _build_application_workspace | review | Local binding for review in _build_application_workspace; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| _build_application_workspace | review_panel | Managed resource for review panel in _build_application_workspace; use the enclosing contract and type below. | Return type of Accordion; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 64 |
| _build_application_workspace | requirements | Local binding for requirements in _build_application_workspace; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| _build_application_workspace | files | Local binding for files in _build_application_workspace; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| _build_application_workspace | widget_selection | Local binding for widget selection in _build_application_workspace; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| _build_application_workspace | widget_select | Local binding for widget select in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| _build_application_workspace | file_hint | Local binding for file hint in _build_application_workspace; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
| _build_application_workspace | editor | Local binding for editor in _build_application_workspace; use the enclosing contract and type below. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| _build_application_workspace | tool_panes | Managed resource for tool panes in _build_application_workspace; use the enclosing contract and type below. | Return type of Row; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 95 |
| _build_application_workspace | code_pane | Local binding for code pane in _build_application_workspace; use the enclosing contract and type below. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 97 |
| _build_application_workspace | widget_pane | Local binding for widget pane in _build_application_workspace; use the enclosing contract and type below. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| _build_application_workspace | tool_tests_pane | Local binding for tool tests pane in _build_application_workspace; use the enclosing contract and type below. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| _build_application_workspace | widget_tests_pane | Local binding for widget tests pane in _build_application_workspace; use the enclosing contract and type below. | Return type of Code; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| _build_application_workspace | save | Local binding for save in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| _build_application_workspace | cases | Local binding for cases in _build_application_workspace; use the enclosing contract and type below. | Return type of JSON; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| _build_application_workspace | build_chathelper | Imported dependency for build chathelper in _build_application_workspace; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 139 |
| _build_application_workspace | reviewed | Local binding for reviewed in _build_application_workspace; use the enclosing contract and type below. | Return type of Checkbox; see its callable contract | Enclosing invocation or class/instance lifetime | 149 |
| _build_application_workspace | acceptance_notice | Local binding for acceptance notice in _build_application_workspace; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 154 |
| _build_application_workspace | approve | Local binding for approve in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 159 |
| _build_application_workspace | reject | Local binding for reject in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| _build_application_workspace | host_requirement | Local binding for host requirement in _build_application_workspace; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| _build_application_workspace | install_host_requirement | Local binding for install host requirement in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| _build_application_workspace | frame | Local binding for frame in _build_application_workspace; use the enclosing contract and type below. | Return type of HTML; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| _build_application_workspace | data_input | Local binding for data input in _build_application_workspace; use the enclosing contract and type below. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 173 |
| _build_application_workspace | data_contract | Local binding for data contract in _build_application_workspace; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| _build_application_workspace | run_data | Local binding for run data in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| _build_application_workspace | show_contract | Local binding for show contract in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 183 |
| _build_application_workspace | fields | Local binding for fields in _build_application_workspace; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 184 |
| _build_application_workspace | legacy_data_result | Managed resource for legacy data result in _build_application_workspace; use the enclosing contract and type below. | Return type of Row; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 188 |
| _build_application_workspace | data_outputs | Local binding for data outputs in _build_application_workspace; use the enclosing contract and type below. | Return type of build_results; see its callable contract | Enclosing invocation or class/instance lifetime | 189 |
| _build_application_workspace | general_data_result | Local binding for general data result in _build_application_workspace; use the enclosing contract and type below. | Return type of HTML; see its callable contract | Enclosing invocation or class/instance lifetime | 190 |
| _build_application_workspace | general_data_table | Local binding for general data table in _build_application_workspace; use the enclosing contract and type below. | Return type of Dataframe; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| _build_application_workspace | outputs | Local binding for outputs in _build_application_workspace; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 201 |
| _build_application_workspace.run_typed_data | text | Parameter for text in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 224 |
| _build_application_workspace.run_typed_data | token | Parameter for token in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 224 |
| _build_application_workspace.run_typed_data | request | Parameter for request in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 224 |
| _build_application_workspace.run_typed_data | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of data_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 226 |
| _build_application_workspace.run_typed_data | _ | Local binding for  in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Return type of data_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 226 |
| _build_application_workspace.run_typed_data | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| _build_application_workspace.run_typed_data | message | Local binding for message in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| _build_application_workspace.run_typed_data | owned | Local binding for owned in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Return type of data; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| _build_application_workspace.run_typed_data | format_result | Imported dependency for format result in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 228 |
| _build_application_workspace.run_typed_data | generic | Local binding for generic in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 230 |
| _build_application_workspace.run_typed_data | rendered | Local binding for rendered in _build_application_workspace.run_typed_data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 231 |
| _build_application_workspace.show_data_contract | token | Parameter for token in _build_application_workspace.show_data_contract; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 266 |
| _build_application_workspace.show_data_contract | request | Parameter for request in _build_application_workspace.show_data_contract; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 266 |
| _build_application_workspace | repair | Local binding for repair in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 277 |
| _build_application_workspace | review_tools | Local binding for review tools in _build_application_workspace; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| _build_application_workspace.refresh_review | token | Parameter for token in _build_application_workspace.refresh_review; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 301 |
| _build_application_workspace.refresh_review | request | Parameter for request in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 301 |
| _build_application_workspace.refresh_review | entries | Local binding for entries in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | first | Local binding for first in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | text | Local binding for text in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | editable | Local binding for editable in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | hint | Local binding for hint in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | original | Local binding for original in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | acceptance | Local binding for acceptance in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.refresh_review | owned | Local binding for owned in _build_application_workspace.refresh_review; use the enclosing contract and type below. | Return type of review_files; see its callable contract | Enclosing invocation or class/instance lifetime | 303 |
| _build_application_workspace.select_file | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 328 |
| _build_application_workspace.select_file | token | Parameter for token in _build_application_workspace.select_file; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 328 |
| _build_application_workspace.select_file | request | Parameter for request in _build_application_workspace.select_file; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 328 |
| _build_application_workspace.select_file | panes | Local binding for panes in _build_application_workspace.select_file; use the enclosing contract and type below. | Return type of review_panes; see its callable contract | Enclosing invocation or class/instance lifetime | 333 |
| _build_application_workspace.select_file | error | Caught exception for error in _build_application_workspace.select_file; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 334 |
| _build_application_workspace.select_file | text | Local binding for text in _build_application_workspace.select_file; use the enclosing contract and type below. | Return type of read_file; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| _build_application_workspace.select_file | editable | Local binding for editable in _build_application_workspace.select_file; use the enclosing contract and type below. | Return type of read_file; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| _build_application_workspace.select_file | hint | Local binding for hint in _build_application_workspace.select_file; use the enclosing contract and type below. | Return type of read_file; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| _build_application_workspace.select_file | owned | Local binding for owned in _build_application_workspace.select_file; use the enclosing contract and type below. | Return type of read_file; see its callable contract | Enclosing invocation or class/instance lifetime | 339 |
| _build_application_workspace.select_file | updates | Local binding for updates in _build_application_workspace.select_file; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 361 |
| _build_application_workspace.select_file.comprehension_364 | key | Comprehension item for key in _build_application_workspace.select_file.comprehension_364; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 366 |
| _build_application_workspace.select_widget_file | tool | Parameter for tool in _build_application_workspace.select_widget_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 379 |
| _build_application_workspace.select_widget_file | token | Parameter for token in _build_application_workspace.select_widget_file; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 379 |
| _build_application_workspace.select_widget_file | request | Parameter for request in _build_application_workspace.select_widget_file; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 379 |
| _build_application_workspace.select_widget_file | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of widget_source_name; see its callable contract | Enclosing invocation or class/instance lifetime | 381 |
| _build_application_workspace.edited_file | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 388 |
| _build_application_workspace.edited_file | token | Parameter for token in _build_application_workspace.edited_file; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 388 |
| _build_application_workspace.edited_file | request | Parameter for request in _build_application_workspace.edited_file; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 388 |
| _build_application_workspace.edited_file | hint | Local binding for hint in _build_application_workspace.edited_file; use the enclosing contract and type below. | Return type of mark_edited; see its callable contract | Enclosing invocation or class/instance lifetime | 390 |
| _build_application_workspace.edited_group | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 401 |
| _build_application_workspace.edited_group | token | Parameter for token in _build_application_workspace.edited_group; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 401 |
| _build_application_workspace.edited_group | request | Parameter for request in _build_application_workspace.edited_group; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 401 |
| _build_application_workspace | pane | Loop item for pane in _build_application_workspace; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 405 |
| _build_application_workspace.poll_application | token | Parameter for token in _build_application_workspace.poll_application; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 490 |
| _build_application_workspace.poll_application | request | Parameter for request in _build_application_workspace.poll_application; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 490 |
| _build_application_workspace.poll_application | message | Local binding for message in _build_application_workspace.poll_application; use the enclosing contract and type below. | Return type of poll; see its callable contract | Enclosing invocation or class/instance lifetime | 492 |
| _build_application_workspace.poll_application | content | Artifact or review text whose encoding, size and approval state must be checked. | Return type of poll; see its callable contract | Enclosing invocation or class/instance lifetime | 492 |
| _build_application_workspace.poll_application | owned | Local binding for owned in _build_application_workspace.poll_application; use the enclosing contract and type below. | Return type of poll; see its callable contract | Enclosing invocation or class/instance lifetime | 492 |
| _build_application_workspace.poll_application | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of review_state; see its callable contract | Enclosing invocation or class/instance lifetime | 493 |
| _build_application_workspace.poll_application | available | Local binding for available in _build_application_workspace.poll_application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 494 |
| _build_application_workspace.poll_application | host_dependency_available | Local binding for host dependency available in _build_application_workspace.poll_application; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 495 |
| build_applications_frontend | gr | Parameter for gr in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 541 |
| build_applications_frontend | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 542 |
| build_applications_frontend | bind | Parameter for bind in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 543 |
| build_applications_frontend | session_state | Parameter for session state in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 544 |
| build_applications_frontend | progress | Parameter for progress in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 545 |
| build_applications_frontend | maintenance | Parameter for maintenance in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 546 |
| build_applications_frontend | dialog | Parameter for dialog in build_applications_frontend; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 547 |
| build_applications_frontend | workspace | Local binding for workspace in build_applications_frontend; use the enclosing contract and type below. | Return type of _build_application_workspace; see its callable contract | Enclosing invocation or class/instance lifetime | 552 |
