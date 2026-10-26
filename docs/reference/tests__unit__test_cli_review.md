# Reference for tests/unit/test_cli_review.py

CLI-001: terminal decisions must reach the real owner-bound coordinator.

Source fingerprint: 3ee9416fee2cc595298772f9c4b5792ebd2f013337e60e4281b75fe53a6b4d4f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_terminal_resolves_manual_review

Verify terminal resolves manual review.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_terminal_resolves_manual_review.workflow

Provide workflow for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 35.

### test_interrupted_review_denies_and_closes_owner

Verify interrupted review denies and closes owner.

Kind: callable. Declared return: Not declared / class. Source line: 63.

### test_interrupted_review_denies_and_closes_owner.read

Provide read for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 70.

### test_interrupted_review_denies_and_closes_owner.workflow

Provide workflow for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 80.

### test_eof_at_query_exits_cleanly

Verify eof at query exits cleanly.

Kind: callable. Declared return: Not declared / class. Source line: 93.

### test_cli_shows_independent_host_verdicts

Verify cli shows independent host verdicts.

Kind: callable. Declared return: Not declared / class. Source line: 101.

### test_cli_shows_independent_host_verdicts.workflow

Provide workflow for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 122.

### test_review_control_characters_cannot_hide_terminal_content

Verify review control characters cannot hide terminal content.

Kind: callable. Declared return: Not declared / class. Source line: 140.

### test_review_control_characters_cannot_hide_terminal_content.workflow

Provide workflow for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 148.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | ApprovalCoordinator | Imported dependency for ApprovalCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | run_cli | Imported dependency for run cli in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| test_terminal_resolves_manual_review | monkeypatch | Parameter for monkeypatch in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_terminal_resolves_manual_review | capsys | Parameter for capsys in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_terminal_resolves_manual_review | answers | Parameter for answers in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_terminal_resolves_manual_review | expected | Reviewed expected observation kept outside untrusted child execution. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_terminal_resolves_manual_review | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_terminal_resolves_manual_review | security.auto_approve | Attribute for security.auto approve in test_terminal_resolves_manual_review; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 30 |
| test_terminal_resolves_manual_review | results | Local binding for results in test_terminal_resolves_manual_review; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 31 |
| test_terminal_resolves_manual_review | inputs | Local binding for inputs in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_terminal_resolves_manual_review.lambda_33 | prompt | Callback parameter for prompt in test_terminal_resolves_manual_review.lambda_33; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 33 |
| test_terminal_resolves_manual_review.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 35 |
| test_terminal_resolves_manual_review | stopped | Managed resource for stopped in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 52 |
| test_terminal_resolves_manual_review | output | Local binding for output in test_terminal_resolves_manual_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| test_interrupted_review_denies_and_closes_owner | monkeypatch | Parameter for monkeypatch in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_interrupted_review_denies_and_closes_owner | interruption | Parameter for interruption in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_interrupted_review_denies_and_closes_owner | during_edit | Parameter for during edit in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| test_interrupted_review_denies_and_closes_owner | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| test_interrupted_review_denies_and_closes_owner | results | Local binding for results in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 66 |
| test_interrupted_review_denies_and_closes_owner | finished | Local binding for finished in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_interrupted_review_denies_and_closes_owner | decisions | Local binding for decisions in test_interrupted_review_denies_and_closes_owner; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| test_interrupted_review_denies_and_closes_owner.read | prompt | Parameter for prompt in test_interrupted_review_denies_and_closes_owner.read; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_interrupted_review_denies_and_closes_owner.read | answer | Expression binding for answer in test_interrupted_review_denies_and_closes_owner.read; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 74 |
| test_interrupted_review_denies_and_closes_owner.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 80 |
| test_eof_at_query_exits_cleanly | monkeypatch | Parameter for monkeypatch in test_eof_at_query_exits_cleanly; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 93 |
| test_eof_at_query_exits_cleanly.lambda_95 | prompt | Callback parameter for prompt in test_eof_at_query_exits_cleanly.lambda_95; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 95 |
| test_eof_at_query_exits_cleanly.lambda_95.comprehension_95 | _ | Comprehension item for  in test_eof_at_query_exits_cleanly.lambda_95.comprehension_95; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 95 |
| test_eof_at_query_exits_cleanly | stopped | Managed resource for stopped in test_eof_at_query_exits_cleanly; use the enclosing contract and type below. | Return type of raises; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 96 |
| test_eof_at_query_exits_cleanly.lambda_97 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 97 |
| test_cli_shows_independent_host_verdicts | system | Parameter for system in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_cli_shows_independent_host_verdicts | monkeypatch | Parameter for monkeypatch in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_cli_shows_independent_host_verdicts | capsys | Parameter for capsys in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 101 |
| test_cli_shows_independent_host_verdicts | service | Local binding for service in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_cli_shows_independent_host_verdicts | system.security.auto_approve | Attribute for system.security.auto approve in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 104 |
| test_cli_shows_independent_host_verdicts | edited | Local binding for edited in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| test_cli_shows_independent_host_verdicts | inputs | Local binding for inputs in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 119 |
| test_cli_shows_independent_host_verdicts.lambda_120 | prompt | Callback parameter for prompt in test_cli_shows_independent_host_verdicts.lambda_120; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 120 |
| test_cli_shows_independent_host_verdicts.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 122 |
| test_cli_shows_independent_host_verdicts.workflow | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 125 |
| test_cli_shows_independent_host_verdicts.workflow | original | Local binding for original in test_cli_shows_independent_host_verdicts.workflow; use the enclosing contract and type below. | Return type of replace; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| test_cli_shows_independent_host_verdicts | output | Local binding for output in test_cli_shows_independent_host_verdicts; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_review_control_characters_cannot_hide_terminal_content | monkeypatch | Parameter for monkeypatch in test_review_control_characters_cannot_hide_terminal_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_review_control_characters_cannot_hide_terminal_content | capsys | Parameter for capsys in test_review_control_characters_cannot_hide_terminal_content; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 140 |
| test_review_control_characters_cannot_hide_terminal_content | security | Owner-scoped approval and path boundary injected into this service. | Return type of for_owner; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| test_review_control_characters_cannot_hide_terminal_content | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 143 |
| test_review_control_characters_cannot_hide_terminal_content | inputs | Local binding for inputs in test_review_control_characters_cannot_hide_terminal_content; use the enclosing contract and type below. | Return type of iter; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| test_review_control_characters_cannot_hide_terminal_content.lambda_145 | prompt | Callback parameter for prompt in test_review_control_characters_cannot_hide_terminal_content.lambda_145; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 145 |
| test_review_control_characters_cannot_hide_terminal_content | decisions | Local binding for decisions in test_review_control_characters_cannot_hide_terminal_content; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 146 |
| test_review_control_characters_cannot_hide_terminal_content.workflow | query | Original user request or a trusted test query; avoid payload logging by default. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 148 |
| test_review_control_characters_cannot_hide_terminal_content | output | Local binding for output in test_review_control_characters_cannot_hide_terminal_content; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 155 |
