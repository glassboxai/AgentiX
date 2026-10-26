# Reference for tools/collect_evidence.py

Inspect historical baseline XML and compare current entrypoint hashes.

This helper is retained for the original baseline workflow. Current refactoring
evidence is recorded separately and includes package files, not just entrypoints.

Source fingerprint: 59d237cb34fe77725d749295127a14403b669547c5659e132f1d9c9b27daa14d

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### distribution_versions

Return available versions and explicit missing metadata without aborting.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### collect

Read test XML and compare production hashes with the pre-test baseline.

Kind: callable. Declared return: Not declared / class. Source line: 29.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | importlib | Imported dependency for importlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | platform | Imported dependency for platform in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | ET | Imported dependency for ET in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | ROOT | Module binding for ROOT in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 14 |
| module | PRODUCTION | Module binding for PRODUCTION in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 15 |
| distribution_versions | names | Parameter for names in distribution_versions; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| distribution_versions | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 20 |
| distribution_versions | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 21 |
| collect | baseline | Local binding for baseline in collect; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| collect | current | Local binding for current in collect; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 34 |
| collect.comprehension_34 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 35 |
| collect | suites | Local binding for suites in collect; use the enclosing contract and type below. | Return type of getroot; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| collect | cases | Local binding for cases in collect; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| collect | expected | Reviewed expected observation kept outside untrusted child execution. | list | Enclosing invocation or class/instance lifetime | 39 |
| collect.comprehension_39 | case | Comprehension item for case in collect.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 39 |
| collect.comprehension_46.comprehension_47 | tag | Comprehension item for tag in collect.comprehension_46.comprehension_47; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 47 |
| collect.comprehension_46 | case | Comprehension item for case in collect.comprehension_46; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 48 |
| collect.comprehension_50 | case | Comprehension item for case in collect.comprehension_50; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 50 |
| collect.comprehension_51 | case | Comprehension item for case in collect.comprehension_51; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 51 |
