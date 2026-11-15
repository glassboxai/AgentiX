# Reference for tools/probe_group_ids.py

Observe structural IDs with a trusted fixture, not model code or native evidence.

Source fingerprint: a0576ac0c630250d8187394950f0fd0e03e4aa64b7d53994cc66ae29def5e1f3

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | subprocess | Imported dependency for subprocess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Counter | Imported dependency for Counter in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ProxyHandler | Imported dependency for ProxyHandler in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | build_opener | Imported dependency for build opener in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | sync_playwright | Imported dependency for sync playwright in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 15 |
| module | listener | Managed resource for listener in module; use the enclosing contract and type below. | Return type of socket; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 16 |
| module | port | Module binding for port in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 18 |
| module | log | Managed resource for log in module; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 19 |
| module | process | Module binding for process in module; use the enclosing contract and type below. | Return type of Popen; see its callable contract | Module/process lifetime | 20 |
| module | url | Module binding for url in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 24 |
| module | opener | Module binding for opener in module; use the enclosing contract and type below. | Return type of build_opener; see its callable contract | Module/process lifetime | 25 |
| module | _ | Loop item for  in module; use the enclosing contract and type below. | Element of the declared iterable | Module/process lifetime | 26 |
| module | driver | Managed resource for driver in module; use the enclosing contract and type below. | Return type of sync_playwright; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 32 |
| module | browser | Module binding for browser in module; use the enclosing contract and type below. | Return type of launch; see its callable contract | Module/process lifetime | 33 |
| module | page | Module binding for page in module; use the enclosing contract and type below. | Return type of new_page; see its callable contract | Module/process lifetime | 36 |
| module | expect | Imported dependency for expect in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 38 |
| module | text | Loop item for text in module; use the enclosing contract and type below. | Element of the declared iterable | Module/process lifetime | 40 |
| module | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Module/process lifetime | 41 |
| module | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 44 |
| module | elements | Module binding for elements in module; use the enclosing contract and type below. | Return type of evaluate_all; see its callable contract | Module/process lifetime | 48 |
| module | counts | Module binding for counts in module; use the enclosing contract and type below. | Return type of Counter; see its callable contract | Module/process lifetime | 51 |
| comprehension_51 | item | Comprehension item for item in comprehension_51; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 51 |
| module | duplicates | Module binding for duplicates in module; use the enclosing contract and type below. | dict | Module/process lifetime | 52 |
| comprehension_52 | key | Comprehension item for key in comprehension_52; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
| comprehension_52 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
| module | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Module/process lifetime | 53 |
| comprehension_55 | item | Comprehension item for item in comprehension_55; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 55 |
