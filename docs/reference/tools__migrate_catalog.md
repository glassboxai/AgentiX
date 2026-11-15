# Reference for tools/migrate_catalog.py

Plan or apply explicitly reviewed catalog relocation, without model inference.

The review digest authorizes only the exact plan. Applications reuse protected
human-reviewed cases and require fresh native/browser gates; no auto-approval
switch, changed-policy tool grant transfer or host-execution fallback exists.

Source fingerprint: 13381bf6ff0ad43f15beb9f35fca813564a36e863cd625e7cbf302e00ac493fb

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### verify_application

Run protected reviewed cases through native and browser production gates.

No expected value is inferred, altered or sent to a model. The child receives
inputs only. Always close the verifier's own preview; leave live apps alone.

Kind: callable. Declared return: bool. Source line: 32.

### verify_exception_cases

Compare all reviewed exception types on the host, sending child inputs only.

The injected evaluator is a test seam. Production always uses WindowsSandbox
without fallback. Retain bounded case IDs and verdicts, not code or arguments.
Raise ValueError on any child/process mismatch and never silently drop a case.

Kind: callable. Declared return: None. Source line: 50.

### verify_widget

Check unchanged widget bytes against every current approved value case.

Trusted connection code forwards literal reviewed arguments; expected results
stay in the host review. No model is constructed, no installed code is changed
and generated child tests are provisional. Exact exception types are checked
separately through native observations; browser checks use typed value cases.

Kind: callable. Declared return: bool. Source line: 88.

### main

Print a safe plan or apply its reviewed digest; return 2 for blocked entries.

Kind: callable. Declared return: int. Source line: 156.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ApplicationPipeline | Imported dependency for ApplicationPipeline in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | matches_expectation | Imported dependency for matches expectation in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | WindowsDataProtection | Imported dependency for WindowsDataProtection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | CatalogMigration | Imported dependency for CatalogMigration in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| module | fingerprint | Imported dependency for fingerprint in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| verify_application | package | Parameter for package in verify_application; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 32 |
| verify_application | review | Parameter for review in verify_application; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 32 |
| verify_application | evidence | Parameter for evidence in verify_application; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 32 |
| verify_application | candidate | Local binding for candidate in verify_application; use the enclosing contract and type below. | Return type of Candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| verify_application | supervisor | Local binding for supervisor in verify_application; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| verify_exception_cases | tool | Parameter for tool in verify_exception_cases; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 51 |
| verify_exception_cases | evidence | Parameter for evidence in verify_exception_cases; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 51 |
| verify_exception_cases | evaluate | Parameter for evaluate in verify_exception_cases; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 51 |
| verify_exception_cases | observe | Local binding for observe in verify_exception_cases; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| verify_exception_cases | verdicts | Local binding for verdicts in verify_exception_cases; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 60 |
| verify_exception_cases | case | Loop item for case in verify_exception_cases; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 61 |
| verify_exception_cases | observed | Returned observation checked against the reviewed host-side expectation. | Return type of observe; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| verify_exception_cases | passed | Local binding for passed in verify_exception_cases; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65 |
| verify_widget | tool | Parameter for tool in verify_widget; use the enclosing contract and type below. | ApprovedTool | Enclosing invocation or class/instance lifetime | 88 |
| verify_widget | proposal | Parameter for proposal in verify_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 88 |
| verify_widget | css | Parameter for css in verify_widget; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 88 |
| verify_widget | evidence | Parameter for evidence in verify_widget; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 88 |
| verify_widget | reviewed | Local binding for reviewed in verify_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 96 |
| verify_widget.comprehension_97 | case | Comprehension item for case in verify_widget.comprehension_97; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 97 |
| verify_widget | cases | Local binding for cases in verify_widget; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 100 |
| verify_widget.comprehension_100 | case | Comprehension item for case in verify_widget.comprehension_100; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 100 |
| verify_widget | widgets | Local binding for widgets in verify_widget; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 103 |
| verify_widget.comprehension_103 | i | Comprehension item for i in verify_widget.comprehension_103; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 103 |
| verify_widget | lines | Local binding for lines in verify_widget; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 104 |
| verify_widget | widget | Loop item for widget in verify_widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 109 |
| verify_widget | case | Loop item for case in verify_widget; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 109 |
| verify_widget | arguments | Local binding for arguments in verify_widget; use the enclosing contract and type below. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 110 |
| verify_widget.comprehension_110 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 110 |
| verify_widget.comprehension_110 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 110 |
| verify_widget | plan | Local binding for plan in verify_widget; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 114 |
| verify_widget | coordinator | Local binding for coordinator in verify_widget; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| verify_widget | candidate | Local binding for candidate in verify_widget; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| verify_widget.lambda_123 | _ | Callback parameter for  in verify_widget.lambda_123; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 123 |
| verify_widget | css_path | Local binding for css path in verify_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 127 |
| verify_widget | manifest_path | Local binding for manifest path in verify_widget; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 129 |
| verify_widget | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| verify_widget | review | Local binding for review in verify_widget; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 133 |
| verify_widget.comprehension_138 | widget | Comprehension item for widget in verify_widget.comprehension_138; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 140 |
| verify_widget.comprehension_138 | case | Comprehension item for case in verify_widget.comprehension_138; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 140 |
| verify_widget.comprehension_142 | widget | Comprehension item for widget in verify_widget.comprehension_142; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 142 |
| verify_widget.comprehension_142 | case | Comprehension item for case in verify_widget.comprehension_142; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 142 |
| verify_widget | candidate.digest | Attribute for candidate.digest in verify_widget; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| verify_widget | candidate.review_text | Attribute for candidate.review text in verify_widget; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 145 |
| verify_widget | supervisor | Local binding for supervisor in verify_widget; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| main | migration | Local binding for migration in main; use the enclosing contract and type below. | Return type of CatalogMigration; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| main | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 175 |
| main.comprehension_177 | item | Comprehension item for item in main.comprehension_177; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 177 |
