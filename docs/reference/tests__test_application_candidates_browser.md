# Reference for tests/test_application_candidates_browser.py

Real disposable GUI validation of retrieval preview, spinner and explicit acceptance.

Source fingerprint: e1377f2150c540ec76f28683cbeee3ef2540e4a900dd7743685279ec8b542df0

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_candidate_preview_spinner_and_acceptance

Use actual Gradio callbacks and two browsers with explicit model/approval doubles.

Kind: callable. Declared return: None. Source line: 16.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 12 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 13 |
| test_candidate_preview_spinner_and_acceptance | tmp_path | Parameter for tmp path in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 16 |
| test_candidate_preview_spinner_and_acceptance | expect | Imported dependency for expect in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_candidate_preview_spinner_and_acceptance | sync_playwright | Imported dependency for sync playwright in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 18 |
| test_candidate_preview_spinner_and_acceptance | port | Local binding for port in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 20 |
| test_candidate_preview_spinner_and_acceptance | logpath | Local binding for logpath in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 21 |
| test_candidate_preview_spinner_and_acceptance | log | Managed resource for log in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 22 |
| test_candidate_preview_spinner_and_acceptance | process | Local binding for process in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_candidate_preview_spinner_and_acceptance | url | Local binding for url in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_candidate_preview_spinner_and_acceptance | driver | Managed resource for driver in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 39 |
| test_candidate_preview_spinner_and_acceptance | browser | Local binding for browser in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| test_candidate_preview_spinner_and_acceptance | first | Local binding for first in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 43 |
| test_candidate_preview_spinner_and_acceptance | second | Local binding for second in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 43 |
| test_candidate_preview_spinner_and_acceptance | panel | Local binding for panel in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_candidate_preview_spinner_and_acceptance | accept | Local binding for accept in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| test_candidate_preview_spinner_and_acceptance | checks | Local binding for checks in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_candidate_preview_spinner_and_acceptance | colors | Local binding for colors in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of evaluate; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_candidate_preview_spinner_and_acceptance | audit | Local binding for audit in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 69, 120 |
| test_candidate_preview_spinner_and_acceptance | spinner | Local binding for spinner in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Return type of locator; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| test_candidate_preview_spinner_and_acceptance | stop_process_tree | Imported dependency for stop process tree in test_candidate_preview_spinner_and_acceptance; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 128 |
