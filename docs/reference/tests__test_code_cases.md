# Reference for tests/test_code_cases.py

V6-045: propose reviewed data without executing generated connection code.

Source fingerprint: 5e109cd36c8086f387b6e9c73953e02534694a35b85cc79a15d9bccb67b12e99

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_reviewed_cases_fill_a_compatible_dependent_application

Only approved expected values may flow through connection assignments.

Kind: callable. Declared return: None. Source line: 9.

### test_partial_cases_report_missing_expectations_without_predicting

A missing downstream approved case must remain a visible human decision.

Kind: callable. Declared return: None. Source line: 31.

### test_unsupported_python_is_never_evaluated

Calls outside the reviewed declarative subset leave pending data, never run.

Kind: callable. Declared return: None. Source line: 42.

### test_missing_cases_produce_persistent_actionable_status

V6-045: approval rejection must identify cases, without crossing execution gates.

Kind: callable. Declared return: None. Source line: 53.

### test_missing_cases_produce_persistent_actionable_status.reject

Simulate the existing supervisor acceptance rejection without native work.

Kind: callable. Declared return: Not declared / class. Source line: 65.

### test_pipeline_prefills_editor_but_still_requires_human_review

Generated suggestions stay editable and never replace explicit owner approval.

Kind: callable. Declared return: None. Source line: 96.

### test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator

Return independently authored inert source and presentation fixtures.

Kind: class. Declared return: Not declared / class. Source line: 106.

### test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.plan

Return one direct reviewed call with a public input.

Kind: callable. Declared return: Not declared / class. Source line: 109.

### test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets

Supply trusted widget fixtures without model work.

Kind: callable. Declared return: Not declared / class. Source line: 118.

### test_incompatible_literals_and_branching_leave_expectations_pending

Neither a different constant nor unsupported control flow invents a result.

Kind: callable. Declared return: None. Source line: 142.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | approved_tool | Imported dependency for approved tool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | proposal | Imported dependency for proposal in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| test_reviewed_cases_fill_a_compatible_dependent_application | propose_cases | Imported dependency for propose cases in test_reviewed_cases_fill_a_compatible_dependent_application; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 11 |
| test_reviewed_cases_fill_a_compatible_dependent_application | tool | Local binding for tool in test_reviewed_cases_fill_a_compatible_dependent_application; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 13 |
| test_reviewed_cases_fill_a_compatible_dependent_application | contract | Validated declarative acceptance data bound to current artifact identities. | dict | Enclosing invocation or class/instance lifetime | 14 |
| test_reviewed_cases_fill_a_compatible_dependent_application | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_partial_cases_report_missing_expectations_without_predicting | propose_cases | Imported dependency for propose cases in test_partial_cases_report_missing_expectations_without_predicting; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| test_partial_cases_report_missing_expectations_without_predicting | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_unsupported_python_is_never_evaluated | propose_cases | Imported dependency for propose cases in test_unsupported_python_is_never_evaluated; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 44 |
| test_unsupported_python_is_never_evaluated | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_unsupported_python_is_never_evaluated | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_missing_cases_produce_persistent_actionable_status | tmp_path | Parameter for tmp path in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 53 |
| test_missing_cases_produce_persistent_actionable_status | json | Imported dependency for json in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 55 |
| test_missing_cases_produce_persistent_actionable_status | SimpleNamespace | Imported dependency for SimpleNamespace in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 56 |
| test_missing_cases_produce_persistent_actionable_status | registry | Imported dependency for registry in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 58 |
| test_missing_cases_produce_persistent_actionable_status | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| test_missing_cases_produce_persistent_actionable_status | sessions | Local binding for sessions in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of registry; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_missing_cases_produce_persistent_actionable_status | owner | Local binding for owner in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| test_missing_cases_produce_persistent_actionable_status.reject | args | Parameter for args in test_missing_cases_produce_persistent_actionable_status.reject; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| test_missing_cases_produce_persistent_actionable_status | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_missing_cases_produce_persistent_actionable_status | request | Local binding for request in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_missing_cases_produce_persistent_actionable_status | _ | Local binding for  in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_missing_cases_produce_persistent_actionable_status | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 71 |
| test_missing_cases_produce_persistent_actionable_status | state.candidate | Attribute for state.candidate in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| test_missing_cases_produce_persistent_actionable_status | owner.controller.state.application_review_pending | Attribute for owner.controller.state.application review pending in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 87 |
| test_missing_cases_produce_persistent_actionable_status | rows | Local binding for rows in test_missing_cases_produce_persistent_actionable_status; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_pipeline_prefills_editor_but_still_requires_human_review | tmp_path | Parameter for tmp path in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| test_pipeline_prefills_editor_but_still_requires_human_review | json | Imported dependency for json in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| test_pipeline_prefills_editor_but_still_requires_human_review | pytest | Imported dependency for pytest in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 100 |
| test_pipeline_prefills_editor_but_still_requires_human_review | WIDGET | Imported dependency for WIDGET in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 101 |
| test_pipeline_prefills_editor_but_still_requires_human_review | ApplicationReview | Imported dependency for ApplicationReview in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 103 |
| test_pipeline_prefills_editor_but_still_requires_human_review | ApplicationPipeline | Imported dependency for ApplicationPipeline in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 104 |
| test_pipeline_prefills_editor_but_still_requires_human_review | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 104 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.plan | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 109 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.plan | args | Parameter for args in test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.plan; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 109 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.plan | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of proposal; see its callable contract | Enclosing invocation or class/instance lifetime | 111 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets | tools | Parameter for tools in test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets | feedback | Parameter for feedback in test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 118 |
| test_pipeline_prefills_editor_but_still_requires_human_review.Coordinator.widgets.comprehension_120 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 122 |
| test_pipeline_prefills_editor_but_still_requires_human_review | item | Local binding for item in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_pipeline_prefills_editor_but_still_requires_human_review.lambda_125 | _ | Callback parameter for  in test_pipeline_prefills_editor_but_still_requires_human_review.lambda_125; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 125 |
| test_pipeline_prefills_editor_but_still_requires_human_review | text | Local binding for text in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_pipeline_prefills_editor_but_still_requires_human_review | editable | Local binding for editable in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_pipeline_prefills_editor_but_still_requires_human_review | hint | Local binding for hint in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_pipeline_prefills_editor_but_still_requires_human_review | supervisor | Local binding for supervisor in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Return type of ApplicationSupervisor; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| test_pipeline_prefills_editor_but_still_requires_human_review | old_identity | Local binding for old identity in test_pipeline_prefills_editor_but_still_requires_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_incompatible_literals_and_branching_leave_expectations_pending | propose_cases | Imported dependency for propose cases in test_incompatible_literals_and_branching_leave_expectations_pending; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 144 |
| test_incompatible_literals_and_branching_leave_expectations_pending | source | Explicit source document or source-code text; never imported for reference generation. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 146 |
| test_incompatible_literals_and_branching_leave_expectations_pending | assembly | Local binding for assembly in test_incompatible_literals_and_branching_leave_expectations_pending; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 150 |
| test_incompatible_literals_and_branching_leave_expectations_pending | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of propose_cases; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
