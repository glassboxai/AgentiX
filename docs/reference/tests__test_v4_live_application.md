# Reference for tests/test_v4_live_application.py

Opt-in real model GUI trial with a separate explicit engineer-review gate.

The test cannot approve generated code on its own. An operator must read the
captured snapshot and provide its exact SHA-256 and explicit decision externally.

Source fingerprint: 98c3dcfdffc957499128eda4257a76720e6da4551b016f6f78b6c772171afce6

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_live_v4_application_with_human_review

Use an English problem-only query and actual local model/native/browser gates.

Kind: callable. Declared return: Not declared / class. Source line: 23.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | await_http | Imported dependency for await http in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | free_port | Imported dependency for free port in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 19 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 20 |
| test_live_v4_application_with_human_review | tmp_path | Parameter for tmp path in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 23 |
| test_live_v4_application_with_human_review | expect | Imported dependency for expect in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_live_v4_application_with_human_review | sync_playwright | Imported dependency for sync playwright in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_live_v4_application_with_human_review | trial | Local binding for trial in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_live_v4_application_with_human_review | recovery_package | Local binding for recovery package in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_live_v4_application_with_human_review | recovery_review | Local binding for recovery review in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_live_v4_application_with_human_review | port | Local binding for port in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of free_port; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_live_v4_application_with_human_review | capture | Local binding for capture in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_live_v4_application_with_human_review | decision | Local binding for decision in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| test_live_v4_application_with_human_review | logpath | Local binding for logpath in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| test_live_v4_application_with_human_review | log | Managed resource for log in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 40 |
| test_live_v4_application_with_human_review | env | Local binding for env in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| test_live_v4_application_with_human_review | process | Local binding for process in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| test_live_v4_application_with_human_review | url | Local binding for url in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 67 |
| test_live_v4_application_with_human_review | driver | Managed resource for driver in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 69 |
| test_live_v4_application_with_human_review | browser | Local binding for browser in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of launch; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| test_live_v4_application_with_human_review | page | Local binding for page in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_live_v4_application_with_human_review | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 76 |
| test_live_v4_application_with_human_review | snapshot | Local binding for snapshot in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of input_value; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_live_v4_application_with_human_review | review_hash | Local binding for review hash in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_live_v4_application_with_human_review | deadline | Local binding for deadline in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 89 |
| test_live_v4_application_with_human_review | reviewed | Local binding for reviewed in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_live_v4_application_with_human_review | frame | Local binding for frame in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Return type of frame_locator; see its callable contract | Enclosing invocation or class/instance lifetime | 103 |
| test_live_v4_application_with_human_review | text | Loop item for text in test_live_v4_application_with_human_review; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| test_live_v4_application_with_human_review | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
