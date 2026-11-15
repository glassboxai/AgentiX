# Reference for src/agentix/application/general_acceptance.py

Independent host comparisons for generic model widgets inside native previews.

Source fingerprint: a554a170e4c4ab731fea62aa62885a589beee5c8a4e5021c09fa7badf9c6d556

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### launch_acceptance_browser

Launch the acceptance Chromium, retaining bounded evidence on launch failure.

A configured but missing AGENTIX_PLAYWRIGHT_EXECUTABLE fails with clear guidance
instead of a raw driver error. Launch errors never carry page or payload data.

Kind: callable. Declared return: Not declared / class. Source line: 14.

### fill_input

Drive the actual browser control, never call the generated callback on host.

Kind: callable. Declared return: Not declared / class. Source line: 53.

### click_and_wait

Wait for a fresh Gradio queue acknowledgement and completed loading state.

Equal previous values cannot establish callback completion. Gradio marks
outputs pending before submitting /queue/join and hides status trackers only
after completion. No predicted output or arbitrary sleep replaces these signals.

Kind: callable. Declared return: str. Source line: 66.

### display_expectation

Compare numeric presentation exactly while allowing omitted integer decimals.

Gradio tables can render 3.0 as 3. Anchors reject numeric prefixes and suffixes;
padding is presentation whitespace, never a numeric tolerance or rounding rule.

Kind: callable. Declared return: str | re.Pattern[str]. Source line: 91.

### assert_output

Compare rendered scalar/table values with reviewed expectations outside the child.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### browser_verify

Verify individual widget callbacks, repeated combined execution and unique IDs.

Kind: callable. Declared return: None. Source line: 136.

### browser_verify.restrict

Only the owned native bridge origin is reachable by this test browser.

Kind: callable. Declared return: Not declared / class. Source line: 145.

### verify

Hold expected results outside native execution; publish only after GUI comparison.

Kind: callable. Declared return: Not declared / class. Source line: 229.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | TYPE_CHECKING | Imported dependency for TYPE CHECKING in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | urlsplit | Imported dependency for urlsplit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 11 |
| launch_acceptance_browser | driver | Parameter for driver in launch_acceptance_browser; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 14 |
| launch_acceptance_browser | evidence | Parameter for evidence in launch_acceptance_browser; use the enclosing contract and type below. | Path &#124; None | Enclosing invocation or class/instance lifetime | 14 |
| launch_acceptance_browser | executable | Local binding for executable in launch_acceptance_browser; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| launch_acceptance_browser | error | Caught exception for error in launch_acceptance_browser; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 27 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 49 |
| module | Preview | Imported dependency for Preview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 50 |
| fill_input | page | Parameter for page in fill_input; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| fill_input | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 53 |
| fill_input | parameter | Parameter for parameter in fill_input; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 53 |
| fill_input | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| fill_input | control | Local binding for control in fill_input; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| click_and_wait | page | Parameter for page in click_and_wait; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 66 |
| click_and_wait | button_id | Parameter for button id in click_and_wait; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 66 |
| click_and_wait | output_ids | Parameter for output ids in click_and_wait; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 66 |
| click_and_wait | expect | Imported dependency for expect in click_and_wait; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| click_and_wait | acknowledgement | Managed resource for acknowledgement in click_and_wait; use the enclosing contract and type below. | Return type of expect_response; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 75 |
| click_and_wait.lambda_76 | response | Bounded response text to render or validate; it is not executable code. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 76 |
| click_and_wait | response | Bounded response text to render or validate; it is not executable code. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 80 |
| click_and_wait | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| click_and_wait | output | Loop item for output in click_and_wait; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 84 |
| display_expectation | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 91 |
| display_expectation | text | Local binding for text in display_expectation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 98 |
| display_expectation | suffix | Local binding for suffix in display_expectation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 99 |
| assert_output | page | Parameter for page in assert_output; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| assert_output | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 104 |
| assert_output | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| assert_output | expect | Imported dependency for expect in assert_output; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 106 |
| assert_output | control | Local binding for control in assert_output; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| assert_output | grid | Local binding for grid in assert_output; use the enclosing contract and type below. | Return type of get_by_role; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| assert_output | viewport | Local binding for viewport in assert_output; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| assert_output | index | Loop item for index in assert_output; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 116 |
| assert_output | item | Loop item for item in assert_output; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 116 |
| assert_output | fraction | Local binding for fraction in assert_output; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| assert_output | inputs | Local binding for inputs in assert_output; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| assert_output | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of display_expectation; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| browser_verify | preview | Parameter for preview in browser_verify; use the enclosing contract and type below. | 'Preview' | Enclosing invocation or class/instance lifetime | 136 |
| browser_verify | candidate | Parameter for candidate in browser_verify; use the enclosing contract and type below. | 'Candidate' | Enclosing invocation or class/instance lifetime | 136 |
| browser_verify | review | Parameter for review in browser_verify; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 136 |
| browser_verify | expect | Imported dependency for expect in browser_verify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 138 |
| browser_verify | sync_playwright | Imported dependency for sync playwright in browser_verify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 138 |
| browser_verify | origin | Local binding for origin in browser_verify; use the enclosing contract and type below. | Return type of urlsplit; see its callable contract | Enclosing invocation or class/instance lifetime | 140 |
| browser_verify | driver | Managed resource for driver in browser_verify; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 141 |
| browser_verify | browser | Local binding for browser in browser_verify; use the enclosing contract and type below. | Return type of launch_acceptance_browser; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| browser_verify | context | Local binding for context in browser_verify; use the enclosing contract and type below. | Return type of new_context; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| browser_verify.restrict | route | Parameter for route in browser_verify.restrict; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 145 |
| browser_verify.restrict | url | Local binding for url in browser_verify.restrict; use the enclosing contract and type below. | Return type of urlsplit; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| browser_verify | page | Local binding for page in browser_verify; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| browser_verify | completed_events | Local binding for completed events in browser_verify; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 160 |
| browser_verify | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 161 |
| browser_verify | connected | Local binding for connected in browser_verify; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 162 |
| browser_verify.comprehension_162 | widget | Comprehension item for widget in browser_verify.comprehension_162; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 162 |
| browser_verify | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 163, 196 |
| browser_verify | cases | Loop item for cases in browser_verify; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 163 |
| browser_verify | case | Loop item for case in browser_verify; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 168 |
| browser_verify | parameter | Loop item for parameter in browser_verify; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 169 |
| browser_verify | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 169, 181, 196 |
| browser_verify | acceptance | Local binding for acceptance in browser_verify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 179 |
| browser_verify | _ | Loop item for  in browser_verify; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 180 |
| browser_verify | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 181 |
| browser_verify.comprehension_190 | identity | Explicit owner identity used by a session factory or fixture. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 190 |
| browser_verify | ids | Local binding for ids in browser_verify; use the enclosing contract and type below. | Return type of evaluate_all; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| browser_verify | error | Caught exception for error in browser_verify; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 218 |
| verify | supervisor | Parameter for supervisor in verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 229 |
| verify | candidate | Parameter for candidate in verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 229 |
| verify | parent_origin | Parameter for parent origin in verify; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 229 |
| verify | review | Local binding for review in verify; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 231 |
| verify | acceptance | Local binding for acceptance in verify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 232 |
| verify | preview | Local binding for preview in verify; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 233, 263 |
| verify | WidgetTestsFailed | Imported dependency for WidgetTestsFailed in verify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 235 |
| verify | run_application_widget_tests | Imported dependency for run application widget tests in verify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 235 |
| verify | new_widgets | Local binding for new widgets in verify; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 237 |
| verify.comprehension_237 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 239 |
| verify.comprehension_237 | status | Comprehension item for status in verify.comprehension_237; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 239 |
| verify | test_report | Local binding for test report in verify; use the enclosing contract and type below. | Return type of run_application_widget_tests; see its callable contract | Enclosing invocation or class/instance lifetime | 245 |
| verify | error | Caught exception for error in verify; use the enclosing contract and type below. | WidgetTestsFailed | Current exception handler; Python clears this binding afterward | 246, 279 |
| verify | candidate.preview | Attribute for candidate.preview in verify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 266, 287 |
| verify | candidate.verified | Attribute for candidate.verified in verify; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 273, 288 |
