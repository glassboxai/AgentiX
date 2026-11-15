# Reference for tests/unit/test_right_sidebars.py

V7-068: each tab owns a right-hand sidebar for its catalog, validation and review controls.

Source fingerprint: 816bedeaaa14d464b3b2cb3cfbeb40ea4a56fc53263f237486655cbb7b22a3f1

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Registry

Record component creation, nesting and event wiring without a browser.

Kind: class. Declared return: Not declared / class. Source line: 13.

### Registry.__init__

Start an empty creation log and an empty container stack.

Kind: callable. Declared return: None. Source line: 16.

### Registry.next_identity

Return a stable component identity for nesting assertions.

Kind: callable. Declared return: int. Source line: 23.

### Registry.factory

Return a Gradio-like constructor that records its parent container.

Kind: callable. Declared return: Not declared / class. Source line: 28.

### Registry.factory.build

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 31.

### Registry.by_elem_id

Return the single component carrying an exact maintained element id.

Kind: callable. Declared return: Not declared / class. Source line: 36.

### Registry.is_inside

Walk recorded parents to prove real container nesting.

Kind: callable. Declared return: bool. Source line: 42.

### Component

Minimal Gradio component double supporting context managers and event wiring.

Kind: class. Declared return: Not declared / class. Source line: 52.

### Component.__init__

Record the component and the container that currently owns it.

Kind: callable. Declared return: None. Source line: 55.

### Component.__enter__

Push this component as the active container.

Kind: callable. Declared return: Not declared / class. Source line: 64.

### Component.__exit__

Pop the active container without suppressing exceptions.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### Component.__getattr__

Absorb any Gradio event registration and return this component.

Kind: callable. Declared return: Not declared / class. Source line: 74.

### Component.__getattr__.event

Missing docstring: completion is blocked.

Kind: callable. Declared return: Not declared / class. Source line: 77.

### _gradio

Build the component surface used by the two tab frontends.

Kind: callable. Declared return: SimpleNamespace. Source line: 83.

### _bind

Keep the handler identity so event names remain assertable.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### _dialog

Use the real modal so its own components participate in nesting checks.

Kind: callable. Declared return: Not declared / class. Source line: 123.

### _build_tools

Render the Tools tab with catalog maintenance enabled.

Kind: callable. Declared return: None. Source line: 130.

### _build_applications

Render the Applications tab with catalog maintenance enabled.

Kind: callable. Declared return: None. Source line: 148.

### test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review

The Tools catalog, validation and review live in one collapsible right sidebar.

Kind: callable. Declared return: Not declared / class. Source line: 168.

### test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog

The installed-app catalog, its refresh and explorer actions live in the right sidebar.

Kind: callable. Declared return: Not declared / class. Source line: 190.

### test_both_tabs_keep_one_sidebar_each_and_no_second_column

Each tab owns exactly one right sidebar; the work area is no longer split in two.

Kind: callable. Declared return: Not declared / class. Source line: 212.

### test_approved_sidebar_widths_stay_above_the_resize_minimum

Approved defaults must be reachable by the maintained resize minimum.

Kind: callable. Declared return: Not declared / class. Source line: 228.

### test_sidebar_resizer_has_no_maximum_width

The user may widen a tab sidebar without an upper bound.

Kind: callable. Declared return: Not declared / class. Source line: 233.

### test_left_sidebar_is_not_resizable_and_owns_its_overlap

V7-070: the shared model sidebar keeps its fixed width and native padding.

Kind: callable. Declared return: Not declared / class. Source line: 244.

### test_right_sidebars_keep_a_small_inset_from_the_workspace

V7-070/V7-071: both tab panels pad their content and keep a real gap.

Kind: callable. Declared return: Not declared / class. Source line: 257.

### test_tools_legend_sits_below_the_application_toolbar

The legend must render under play/edit/close, not over the canvas top-left.

Kind: callable. Declared return: Not declared / class. Source line: 271.

### test_browser_title_has_no_version_suffix

The browser tab must read AgentiX, not the inherited v5 label.

Kind: callable. Declared return: Not declared / class. Source line: 283.

### test_tab_sidebars_are_contained_by_their_tab_not_the_viewport

Catch a fixed full-height overlay that covers the header and the tab bar.

Kind: callable. Declared return: Not declared / class. Source line: 292.

### test_widgets_paint_above_the_tools_legend

A generated widget must never be covered by the tools color legend.

Kind: callable. Declared return: Not declared / class. Source line: 314.

### test_right_sidebar_assets_are_registered_for_the_browser

Styling and the resize behavior ship with the maintained launch options.

Kind: callable. Declared return: Not declared / class. Source line: 323.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | TOOLS_SIDEBAR_WIDTH | Module binding for TOOLS SIDEBAR WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 8 |
| module | APPLICATIONS_SIDEBAR_WIDTH | Module binding for APPLICATIONS SIDEBAR WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 9 |
| module | MINIMUM_SIDEBAR_WIDTH | Module binding for MINIMUM SIDEBAR WIDTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 10 |
| Registry.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| Registry.__init__ | self.created | Attribute for created in Registry.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 18 |
| Registry.__init__ | self.parents | Attribute for parents in Registry.__init__; use the enclosing contract and type below. | dict[int, int &#124; None] | Enclosing invocation or class/instance lifetime | 19 |
| Registry.__init__ | self.stack | Attribute for stack in Registry.__init__; use the enclosing contract and type below. | list[int] | Enclosing invocation or class/instance lifetime | 20 |
| Registry.__init__ | self._identities | Attribute for identities in Registry.__init__; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 21 |
| Registry.next_identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| Registry.next_identity | self._identities | Attribute for identities in Registry.next_identity; use the enclosing contract and type below. | Preserved or operator-dependent type | Enclosing invocation or class/instance lifetime | 25 |
| Registry.factory | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 28 |
| Registry.factory | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 28 |
| Registry.factory.build | args | Parameter for args in Registry.factory.build; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| Registry.factory.build | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| Registry.by_elem_id | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 36 |
| Registry.by_elem_id | elem_id | Parameter for elem id in Registry.by_elem_id; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 36 |
| Registry.by_elem_id | matches | Local binding for matches in Registry.by_elem_id; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 38 |
| Registry.by_elem_id.comprehension_38 | item | Comprehension item for item in Registry.by_elem_id.comprehension_38; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 38 |
| Registry.is_inside | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| Registry.is_inside | child | Parameter for child in Registry.is_inside; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| Registry.is_inside | ancestor | Parameter for ancestor in Registry.is_inside; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| Registry.is_inside | current | Local binding for current in Registry.is_inside; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44, 48 |
| Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| Component.__init__ | registry | Parameter for registry in Component.__init__; use the enclosing contract and type below. | Registry | Enclosing invocation or class/instance lifetime | 55 |
| Component.__init__ | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 55 |
| Component.__init__ | args | Parameter for args in Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| Component.__init__ | self.registry | Attribute for registry in Component.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 57 |
| Component.__init__ | self.name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| Component.__init__ | self.identity | Explicit owner identity used by a session factory or fixture. | Return type of next_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 64 |
| Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| Component.__exit__ | args | Parameter for args in Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| Component.__getattr__.event | args | Parameter for args in Component.__getattr__.event; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 77 |
| _gradio | registry | Parameter for registry in _gradio; use the enclosing contract and type below. | Registry | Enclosing invocation or class/instance lifetime | 83 |
| _gradio | names | Local binding for names in _gradio; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 85 |
| _gradio.comprehension_111 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 111 |
| _bind | handler | Parameter for handler in _bind; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| _bind | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| _dialog | gr | Parameter for gr in _dialog; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 123 |
| _dialog | MessageDialog | Imported dependency for MessageDialog in _dialog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 125 |
| _build_tools | registry | Parameter for registry in _build_tools; use the enclosing contract and type below. | Registry | Enclosing invocation or class/instance lifetime | 130 |
| _build_tools | gr | Parameter for gr in _build_tools; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 130 |
| _build_tools | build_tools_frontend | Imported dependency for build tools frontend in _build_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 132 |
| _build_tools | maintenance | Local binding for maintenance in _build_tools; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| _build_applications | registry | Parameter for registry in _build_applications; use the enclosing contract and type below. | Registry | Enclosing invocation or class/instance lifetime | 148 |
| _build_applications | gr | Parameter for gr in _build_applications; use the enclosing contract and type below. | SimpleNamespace | Enclosing invocation or class/instance lifetime | 148 |
| _build_applications | build_applications_frontend | Imported dependency for build applications frontend in _build_applications; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 150 |
| _build_applications | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 152 |
| _build_applications | backend.sessions | Attribute for backend.sessions in _build_applications; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| _build_applications | backend.retrieval.startup_message | Attribute for backend.retrieval.startup message in _build_applications; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 154 |
| _build_applications | maintenance | Local binding for maintenance in _build_applications; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review | registry | Local binding for registry in test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review; use the enclosing contract and type below. | Return type of Registry; see its callable contract | Enclosing invocation or class/instance lifetime | 170 |
| test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review | gr | Local binding for gr in test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review; use the enclosing contract and type below. | Return type of _gradio; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review | sidebar | Local binding for sidebar in test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review; use the enclosing contract and type below. | Return type of by_elem_id; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review | elem_id | Loop item for elem id in test_tools_sidebar_is_a_collapsed_right_sidebar_owning_catalog_and_review; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 179 |
| test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog | registry | Local binding for registry in test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog; use the enclosing contract and type below. | Return type of Registry; see its callable contract | Enclosing invocation or class/instance lifetime | 192 |
| test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog | gr | Local binding for gr in test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog; use the enclosing contract and type below. | Return type of _gradio; see its callable contract | Enclosing invocation or class/instance lifetime | 193 |
| test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog | sidebar | Local binding for sidebar in test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog; use the enclosing contract and type below. | Return type of by_elem_id; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog | elem_id | Loop item for elem id in test_applications_sidebar_is_a_collapsed_right_sidebar_owning_the_catalog; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 201 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column | registry | Local binding for registry in test_both_tabs_keep_one_sidebar_each_and_no_second_column; use the enclosing contract and type below. | Return type of Registry; see its callable contract | Enclosing invocation or class/instance lifetime | 214 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column | gr | Local binding for gr in test_both_tabs_keep_one_sidebar_each_and_no_second_column; use the enclosing contract and type below. | Return type of _gradio; see its callable contract | Enclosing invocation or class/instance lifetime | 215 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column | sidebars | Local binding for sidebars in test_both_tabs_keep_one_sidebar_each_and_no_second_column; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 219 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_219 | item | Comprehension item for item in test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_219; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 219 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_220 | item | Comprehension item for item in test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_220; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 220 |
| test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_224 | item | Comprehension item for item in test_both_tabs_keep_one_sidebar_each_and_no_second_column.comprehension_224; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 224 |
| test_approved_sidebar_widths_stay_above_the_resize_minimum | width | Parameter for width in test_approved_sidebar_widths_stay_above_the_resize_minimum; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 228 |
| test_sidebar_resizer_has_no_maximum_width | launch_options | Imported dependency for launch options in test_sidebar_resizer_has_no_maximum_width; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 235 |
| test_sidebar_resizer_has_no_maximum_width | script | Local binding for script in test_sidebar_resizer_has_no_maximum_width; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 237 |
| test_left_sidebar_is_not_resizable_and_owns_its_overlap | launch_options | Imported dependency for launch options in test_left_sidebar_is_not_resizable_and_owns_its_overlap; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 246 |
| test_left_sidebar_is_not_resizable_and_owns_its_overlap | stylesheet | Imported dependency for stylesheet in test_left_sidebar_is_not_resizable_and_owns_its_overlap; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 246 |
| test_left_sidebar_is_not_resizable_and_owns_its_overlap | script | Local binding for script in test_left_sidebar_is_not_resizable_and_owns_its_overlap; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_left_sidebar_is_not_resizable_and_owns_its_overlap | css | Local binding for css in test_left_sidebar_is_not_resizable_and_owns_its_overlap; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 249 |
| test_right_sidebars_keep_a_small_inset_from_the_workspace | stylesheet | Imported dependency for stylesheet in test_right_sidebars_keep_a_small_inset_from_the_workspace; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 259 |
| test_right_sidebars_keep_a_small_inset_from_the_workspace | css | Local binding for css in test_right_sidebars_keep_a_small_inset_from_the_workspace; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 261 |
| test_right_sidebars_keep_a_small_inset_from_the_workspace | rule | Local binding for rule in test_right_sidebars_keep_a_small_inset_from_the_workspace; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 262 |
| test_tools_legend_sits_below_the_application_toolbar | stylesheet | Imported dependency for stylesheet in test_tools_legend_sits_below_the_application_toolbar; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 273 |
| test_tools_legend_sits_below_the_application_toolbar | css | Local binding for css in test_tools_legend_sits_below_the_application_toolbar; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 275 |
| test_tools_legend_sits_below_the_application_toolbar | legend | Local binding for legend in test_tools_legend_sits_below_the_application_toolbar; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 276 |
| test_browser_title_has_no_version_suffix | SessionRegistry | Imported dependency for SessionRegistry in test_browser_title_has_no_version_suffix; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 285 |
| test_browser_title_has_no_version_suffix | build_view | Imported dependency for build view in test_browser_title_has_no_version_suffix; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 286 |
| test_browser_title_has_no_version_suffix | view | Local binding for view in test_browser_title_has_no_version_suffix; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 288 |
| test_browser_title_has_no_version_suffix.lambda_288 | identity | Explicit owner identity used by a session factory or fixture. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 288 |
| test_tab_sidebars_are_contained_by_their_tab_not_the_viewport | stylesheet | Imported dependency for stylesheet in test_tab_sidebars_are_contained_by_their_tab_not_the_viewport; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 294 |
| test_tab_sidebars_are_contained_by_their_tab_not_the_viewport | css | Local binding for css in test_tab_sidebars_are_contained_by_their_tab_not_the_viewport; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 296 |
| test_widgets_paint_above_the_tools_legend | stylesheet | Imported dependency for stylesheet in test_widgets_paint_above_the_tools_legend; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 316 |
| test_widgets_paint_above_the_tools_legend | css | Local binding for css in test_widgets_paint_above_the_tools_legend; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 318 |
| test_right_sidebar_assets_are_registered_for_the_browser | launch_options | Imported dependency for launch options in test_right_sidebar_assets_are_registered_for_the_browser; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 325 |
| test_right_sidebar_assets_are_registered_for_the_browser | stylesheet | Imported dependency for stylesheet in test_right_sidebar_assets_are_registered_for_the_browser; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 325 |
| test_right_sidebar_assets_are_registered_for_the_browser | css | Local binding for css in test_right_sidebar_assets_are_registered_for_the_browser; use the enclosing contract and type below. | Return type of stylesheet; see its callable contract | Enclosing invocation or class/instance lifetime | 327 |
| test_right_sidebar_assets_are_registered_for_the_browser | elem_id | Loop item for elem id in test_right_sidebar_assets_are_registered_for_the_browser; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 328 |
| test_right_sidebar_assets_are_registered_for_the_browser | options | Local binding for options in test_right_sidebar_assets_are_registered_for_the_browser; use the enclosing contract and type below. | Return type of launch_options; see its callable contract | Enclosing invocation or class/instance lifetime | 331 |
