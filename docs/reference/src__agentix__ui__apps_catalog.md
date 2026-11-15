# Reference for src/agentix/ui/apps_catalog.py

Installed Apps Catalog controls; discovery/execution remain owner-bound backend work.

Source fingerprint: 4cdea8e80bcf426c4149ad383f489ab8e6350ef7e5b3ce1bafd2f8d8a20cc63b

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### require_selected_app

Reject catalog actions before any backend call when nothing is selected.

Kind: callable. Declared return: None. Source line: 11.

### catalog_view

Rebuild dropdown choices and description from one protected listing.

Both outputs come from the same read so a successful re-approval or
re-verification drops the stale label and its guidance in one refresh.

Kind: callable. Declared return: tuple. Source line: 17.

### build_apps_catalog

Render one right-side durable catalog with explicit load/play actions.

Kind: callable. Declared return: None. Source line: 30.

### build_apps_catalog.reveal_apps_folder

Open this owner's installed applications folder; no browser path is accepted.

Kind: callable. Declared return: Not declared / class. Source line: 76.

### build_apps_catalog.refresh_apps

Preserve selection while refreshing protected metadata and its description.

Kind: callable. Declared return: Not declared / class. Source line: 92.

### build_apps_catalog.describe_app

Show escaped metadata only for an exact catalog selection.

Kind: callable. Declared return: Not declared / class. Source line: 96.

### build_apps_catalog.load_selected

Require an explicit catalog selection before streaming the load.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### build_apps_catalog.play_selected

Require an explicit catalog selection before streaming the launch.

Kind: callable. Declared return: Not declared / class. Source line: 127.

### build_apps_catalog.reverify_selected

Require an explicit catalog selection before repeating independent gates.

Kind: callable. Declared return: Not declared / class. Source line: 132.

### build_apps_catalog.initial_catalog

Populate once on page load, without continuous artifact polling.

Kind: callable. Declared return: Not declared / class. Source line: 160.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | STARTUP_TIMER_SECONDS | Module binding for STARTUP TIMER SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 5 |
| module | CATALOG_OUTPUT_COUNT | Module binding for CATALOG OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 6 |
| module | STARTUP_OUTPUT_COUNT | Module binding for STARTUP OUTPUT COUNT in module; use the enclosing contract and type below. | int | Module/process lifetime | 7 |
| module | NO_SELECTION | Module binding for NO SELECTION in module; use the enclosing contract and type below. | str | Module/process lifetime | 8 |
| require_selected_app | selected | Parameter for selected in require_selected_app; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 11 |
| catalog_view | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 17 |
| catalog_view | gr | Parameter for gr in catalog_view; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 17 |
| catalog_view | selected | Parameter for selected in catalog_view; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 17 |
| catalog_view | token | Parameter for token in catalog_view; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 17 |
| catalog_view | request | Parameter for request in catalog_view; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 17 |
| catalog_view | choices | Local binding for choices in catalog_view; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| catalog_view | owned | Local binding for owned in catalog_view; use the enclosing contract and type below. | Return type of catalog_entries; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| catalog_view | ids | Local binding for ids in catalog_view; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 24 |
| catalog_view.comprehension_24 | _ | Comprehension item for  in catalog_view.comprehension_24; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| catalog_view.comprehension_24 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 24 |
| catalog_view | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| catalog_view | description | Local binding for description in catalog_view; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| build_apps_catalog | gr | Parameter for gr in build_apps_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 31 |
| build_apps_catalog | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 32 |
| build_apps_catalog | bind | Parameter for bind in build_apps_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| build_apps_catalog | session_state | Parameter for session state in build_apps_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 34 |
| build_apps_catalog | workspace | Parameter for workspace in build_apps_catalog; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 35 |
| build_apps_catalog | progress | Parameter for progress in build_apps_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 36 |
| build_apps_catalog | maintenance | Parameter for maintenance in build_apps_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 37 |
| build_apps_catalog | operation | Local binding for operation in build_apps_catalog; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| build_apps_catalog | dialog | Local binding for dialog in build_apps_catalog; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 43, 47 |
| build_apps_catalog | MessageDialog | Imported dependency for MessageDialog in build_apps_catalog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| build_apps_catalog | reveal_apps | Local binding for reveal apps in build_apps_catalog; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| build_apps_catalog | choice | Local binding for choice in build_apps_catalog; use the enclosing contract and type below. | Return type of Dropdown; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| build_apps_catalog | description | Local binding for description in build_apps_catalog; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| build_apps_catalog | refresh | Local binding for refresh in build_apps_catalog; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| build_apps_catalog | load | Local binding for load in build_apps_catalog; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| build_apps_catalog | play | Local binding for play in build_apps_catalog; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| build_apps_catalog | reverify | Local binding for reverify in build_apps_catalog; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| build_apps_catalog | build_delete_controls | Imported dependency for build delete controls in build_apps_catalog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 63 |
| build_apps_catalog.reveal_apps_folder | token | Parameter for token in build_apps_catalog.reveal_apps_folder; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 76 |
| build_apps_catalog.reveal_apps_folder | request | Parameter for request in build_apps_catalog.reveal_apps_folder; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 76 |
| build_apps_catalog | build_candidate_panel | Imported dependency for build candidate panel in build_apps_catalog; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 88 |
| build_apps_catalog.refresh_apps | selected | Parameter for selected in build_apps_catalog.refresh_apps; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 92 |
| build_apps_catalog.refresh_apps | token | Parameter for token in build_apps_catalog.refresh_apps; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 92 |
| build_apps_catalog.refresh_apps | request | Parameter for request in build_apps_catalog.refresh_apps; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 92 |
| build_apps_catalog.describe_app | selected | Parameter for selected in build_apps_catalog.describe_app; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 96 |
| build_apps_catalog.describe_app | token | Parameter for token in build_apps_catalog.describe_app; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 96 |
| build_apps_catalog.describe_app | request | Parameter for request in build_apps_catalog.describe_app; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 96 |
| build_apps_catalog.load_selected | selected | Parameter for selected in build_apps_catalog.load_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 122 |
| build_apps_catalog.load_selected | token | Parameter for token in build_apps_catalog.load_selected; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 122 |
| build_apps_catalog.load_selected | request | Parameter for request in build_apps_catalog.load_selected; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 122 |
| build_apps_catalog.play_selected | selected | Parameter for selected in build_apps_catalog.play_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 127 |
| build_apps_catalog.play_selected | token | Parameter for token in build_apps_catalog.play_selected; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 127 |
| build_apps_catalog.play_selected | request | Parameter for request in build_apps_catalog.play_selected; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 127 |
| build_apps_catalog.reverify_selected | selected | Parameter for selected in build_apps_catalog.reverify_selected; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 132 |
| build_apps_catalog.reverify_selected | token | Parameter for token in build_apps_catalog.reverify_selected; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 132 |
| build_apps_catalog.reverify_selected | request | Parameter for request in build_apps_catalog.reverify_selected; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 132 |
| build_apps_catalog | startup | Local binding for startup in build_apps_catalog; use the enclosing contract and type below. | Return type of Timer; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| build_apps_catalog.initial_catalog | selected | Parameter for selected in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 160 |
| build_apps_catalog.initial_catalog | token | Parameter for token in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 160 |
| build_apps_catalog.initial_catalog | request | Parameter for request in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 160 |
| build_apps_catalog.initial_catalog | update | Local binding for update in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | Return type of refresh_apps; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| build_apps_catalog.initial_catalog | description_text | Local binding for description text in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | Return type of refresh_apps; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
| build_apps_catalog.initial_catalog | owned | Local binding for owned in build_apps_catalog.initial_catalog; use the enclosing contract and type below. | Return type of refresh_apps; see its callable contract | Enclosing invocation or class/instance lifetime | 162 |
