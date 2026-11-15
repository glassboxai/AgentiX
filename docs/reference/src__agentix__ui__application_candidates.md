# Reference for src/agentix/ui/application_candidates.py

Candidate preview controls below application deletion, with explicit generation consent.

Source fingerprint: 0854b2ef1e93d199dcf10b1ca30cc637a78e77126eb64b6e5dbb830c385aa919

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### candidate_choices

Return plain-text checkbox labels and snapshot IDs; Gradio renders labels as text.

Kind: callable. Declared return: list[tuple[str, str]]. Source line: 13.

### build_candidate_panel

Wire search, integer spinner and owner-checked acceptance without starting agents early.

Kind: callable. Declared return: None. Source line: 21.

### build_candidate_panel.clear_candidates

Invalidate explicitly queued candidate snapshots before slow inference starts.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 59.

### build_candidate_panel.search_candidates

Stream a visible search stage and publish only the latest backend revision.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 70.

### build_candidate_panel.accept_candidates

Disable repeat consent immediately and show the submitted selection's status.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 113.

### build_candidate_panel.refresh_controls

Keep busy/review controls disabled and name the reason inside the button label.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 151.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Final | Imported dependency for Final in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | CANDIDATE_CONTROL_POLL_SECONDS | Typed binding for CANDIDATE CONTROL POLL SECONDS in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 8 |
| candidate_choices | view | Parameter for view in candidate_choices; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 13 |
| candidate_choices.comprehension_15 | item | Comprehension item for item in candidate_choices.comprehension_15; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 17 |
| candidate_choices.comprehension_15 | row | Comprehension item for row in candidate_choices.comprehension_15; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 17 |
| build_candidate_panel | gr | Parameter for gr in build_candidate_panel; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | bind | Parameter for bind in build_candidate_panel; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | session_state | Parameter for session state in build_candidate_panel; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | workspace | Parameter for workspace in build_candidate_panel; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | progress | Parameter for progress in build_candidate_panel; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 22 |
| build_candidate_panel | dialog | Local binding for dialog in build_candidate_panel; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| build_candidate_panel | operation | Local binding for operation in build_candidate_panel; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 26 |
| build_candidate_panel | status | Local binding for status in build_candidate_panel; use the enclosing contract and type below. | Return type of Markdown; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| build_candidate_panel | limit | Local binding for limit in build_candidate_panel; use the enclosing contract and type below. | Return type of Number; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| build_candidate_panel | candidates | Local binding for candidates in build_candidate_panel; use the enclosing contract and type below. | Return type of CheckboxGroup; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| build_candidate_panel | identity | Explicit owner identity used by a session factory or fixture. | Return type of Textbox; see its callable contract | Enclosing invocation or class/instance lifetime | 51 |
| build_candidate_panel | accept | Local binding for accept in build_candidate_panel; use the enclosing contract and type below. | Return type of Button; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| build_candidate_panel | candidate_outputs | Local binding for candidate outputs in build_candidate_panel; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 57 |
| build_candidate_panel.clear_candidates | token | Parameter for token in build_candidate_panel.clear_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 59 |
| build_candidate_panel.clear_candidates | request | Parameter for request in build_candidate_panel.clear_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 59 |
| build_candidate_panel.clear_candidates | owned | Local binding for owned in build_candidate_panel.clear_candidates; use the enclosing contract and type below. | Return type of invalidate_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| build_candidate_panel.search_candidates | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 71 |
| build_candidate_panel.search_candidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 71 |
| build_candidate_panel.search_candidates | count | Parameter for count in build_candidate_panel.search_candidates; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 71 |
| build_candidate_panel.search_candidates | token | Parameter for token in build_candidate_panel.search_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 71 |
| build_candidate_panel.search_candidates | request | Parameter for request in build_candidate_panel.search_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 71 |
| build_candidate_panel.search_candidates | view | Local binding for view in build_candidate_panel.search_candidates; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| build_candidate_panel.search_candidates | owned | Local binding for owned in build_candidate_panel.search_candidates; use the enclosing contract and type below. | Return type of request_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| build_candidate_panel | search_inputs | Local binding for search inputs in build_candidate_panel; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 94 |
| build_candidate_panel | event | Loop item for event in build_candidate_panel; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 95 |
| build_candidate_panel.accept_candidates | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 114 |
| build_candidate_panel.accept_candidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 115 |
| build_candidate_panel.accept_candidates | count | Parameter for count in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 116 |
| build_candidate_panel.accept_candidates | selection_id | Parameter for selection id in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 117 |
| build_candidate_panel.accept_candidates | chosen | Parameter for chosen in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 118 |
| build_candidate_panel.accept_candidates | token | Parameter for token in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 119 |
| build_candidate_panel.accept_candidates | request | Parameter for request in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 120 |
| build_candidate_panel.accept_candidates | untouched | Local binding for untouched in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | Return type of tuple; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| build_candidate_panel.accept_candidates.comprehension_123 | _ | Comprehension item for  in build_candidate_panel.accept_candidates.comprehension_123; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 123 |
| build_candidate_panel.accept_candidates | row | Loop item for row in build_candidate_panel.accept_candidates; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 126 |
| build_candidate_panel | acceptance_outputs | Local binding for acceptance outputs in build_candidate_panel; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 142 |
| build_candidate_panel.refresh_controls | chosen | Parameter for chosen in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 151 |
| build_candidate_panel.refresh_controls | token | Parameter for token in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 151 |
| build_candidate_panel.refresh_controls | request | Parameter for request in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 151 |
| build_candidate_panel.refresh_controls | idle | Local binding for idle in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| build_candidate_panel.refresh_controls | ready | Local binding for ready in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| build_candidate_panel.refresh_controls | owned | Local binding for owned in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| build_candidate_panel.refresh_controls | reason | Local binding for reason in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Return type of candidate_controls; see its callable contract | Enclosing invocation or class/instance lifetime | 153 |
| build_candidate_panel.refresh_controls | label | Local binding for label in build_candidate_panel.refresh_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 154, 156 |
| build_candidate_panel | control_outputs | Local binding for control outputs in build_candidate_panel; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 164 |
