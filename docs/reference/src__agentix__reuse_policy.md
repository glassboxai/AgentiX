# Reference for src/agentix/reuse_policy.py

Conservative unattended-call eligibility; native isolation remains mandatory.

This module never imports generated code. Unknown syntax/capabilities require
manual call approval. Classification does not establish semantic correctness or
purity and cannot grant filesystem, network or process permissions.

Source fingerprint: c6ef587ee26d3b5e6038e573c11dc83a993f5c223cc7098606f0d6ab2e7aab68

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### computation_only

Return whether exact source uses only the explicit computation vocabulary.

Parameters: UTF-8 Python source bytes. Returns False for invalid/unknown
constructs, private introspection, dynamic calls or unapproved imports.
No source is executed; callers must still use OS isolation and reviewed grants.

Kind: callable. Declared return: bool. Source line: 94.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | _CALLS | Module binding for CALLS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 11 |
| module | _MODULES | Module binding for MODULES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 14 |
| module | _METHODS | Module binding for METHODS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 15 |
| module | _NODES | Module binding for NODES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 18 |
| computation_only | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 94 |
| computation_only | tree | Local binding for tree in computation_only; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| computation_only | functions | Local binding for functions in computation_only; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 103 |
| computation_only.comprehension_103 | node | Comprehension item for node in computation_only.comprehension_103; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 103 |
| computation_only | modules | Local binding for modules in computation_only; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 104 |
| computation_only | calls | Local binding for calls in computation_only; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 105 |
| computation_only | node | Loop item for node in computation_only; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 106 |
| computation_only | alias | Loop item for alias in computation_only; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 115, 122 |
| computation_only | module_attribute | Local binding for module attribute in computation_only; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
