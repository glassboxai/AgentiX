# Reference for tests/test_direct_widget_native.py

Native-only probes of an explicitly reviewed external model candidate.

Source fingerprint: ef85bbb2d051743f3be438078c84689bca60a49379220fde7746dc6eadb53f35

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### reviewed

Require independent operator review; never infer approval from child tests.

Kind: callable. Declared return: Not declared / class. Source line: 12.

### probe

Review a maintained probe shell while preserving exact model widget bytes.

Kind: callable. Declared return: Not declared / class. Source line: 23.

### test_generated_widget_two_instances_native

Catch shared IDs, shared callbacks and invalid stale results in actual Gradio.

Kind: callable. Declared return: Not declared / class. Source line: 33.

### test_proposed_model_tests_really_fail_in_separate_sandbox

Record the model tests' actual failure; never execute them on the host.

Kind: callable. Declared return: Not declared / class. Source line: 65.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 9 |
| reviewed | approve_application | Imported dependency for approve application in reviewed; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 14 |
| reviewed | folder | Local binding for folder in reviewed; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| reviewed | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| probe | capability | Parameter for capability in probe; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| probe | replacements | Parameter for replacements in probe; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| probe | ApprovedApplication | Imported dependency for ApprovedApplication in probe; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 25 |
| probe.comprehension_28 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 28 |
| probe.comprehension_28 | body | Comprehension item for body in probe.comprehension_28; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 28 |
| test_generated_widget_two_instances_native | ApplicationSession | Imported dependency for ApplicationSession in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 35 |
| test_generated_widget_two_instances_native | capability | Local binding for capability in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_generated_widget_two_instances_native | shell | Local binding for shell in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_generated_widget_two_instances_native | session | Managed resource for session in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 43 |
| test_generated_widget_two_instances_native | config | Local binding for config in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_generated_widget_two_instances_native | ids | Local binding for ids in test_generated_widget_two_instances_native; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 45 |
| test_generated_widget_two_instances_native.comprehension_45 | component | Comprehension item for component in test_generated_widget_two_instances_native.comprehension_45; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| test_generated_widget_two_instances_native | endpoint | Loop item for endpoint in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 51 |
| test_generated_widget_two_instances_native | text | Loop item for text in test_generated_widget_two_instances_native; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 51 |
| test_generated_widget_two_instances_native | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 51 |
| test_generated_widget_two_instances_native | response | Bounded response text to render or validate; it is not executable code. | Return type of request; see its callable contract | Enclosing invocation or class/instance lifetime | 57 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | ApplicationSession | Imported dependency for ApplicationSession in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 67 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | capability | Local binding for capability in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Return type of reviewed; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | folder | Local binding for folder in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | shell | Local binding for shell in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 71 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | session | Managed resource for session in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Return type of ApplicationSession; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 85 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | config | Local binding for config in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_proposed_model_tests_really_fail_in_separate_sandbox | report | Local binding for report in test_proposed_model_tests_really_fail_in_separate_sandbox; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_proposed_model_tests_really_fail_in_separate_sandbox.comprehension_92 | c | Comprehension item for c in test_proposed_model_tests_really_fail_in_separate_sandbox.comprehension_92; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 94 |
