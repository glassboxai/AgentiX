# Reference for src/agentix/security/reuse_policy.py

Conservative unattended-call eligibility; native isolation remains mandatory.

This module never imports generated code. Unknown syntax/capabilities require
manual call approval. Classification does not establish semantic correctness or
purity and cannot grant filesystem, network or process permissions.

The importable-module list is owner-extensible through portable_modules.json in
the deployment data root. Policy allowance never installs packages: third-party
imports still require the managed environment to provide them.

Source fingerprint: 2ee506378e2b7664272b44285c4b1b1697cb0d2780ad97885e43c79438911e10

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### allowed_modules

Return the effective owner-approved importable modules.

Reads portable_modules.json ({"allowed_modules": ["re", ...]}) from the
deployment data root, or from an explicit path in tests. A missing or
invalid file fails closed to the maintained default. A valid list fully
replaces the default; typing is always forced because canonical Annotated
contracts require it. The file is read on every call so owner edits apply
without a restart.

Kind: callable. Declared return: frozenset[str]. Source line: 43.

### unapproved_imports

Return imported module roots outside the allowed set, without executing code.

Kind: callable. Declared return: set[str]. Source line: 69.

### computation_only

Return whether exact source uses only the explicit computation vocabulary.

Parameters: UTF-8 Python source bytes and, optionally, the allowed import
set; None loads the owner-configured allowed_modules(). Returns False for
invalid/unknown constructs, private introspection, dynamic calls or
unapproved imports. No source is executed; callers must still use OS
isolation and reviewed grants.

Kind: callable. Declared return: bool. Source line: 166.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | _CALLS | Module binding for CALLS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 18 |
| module | _MODULES | Module binding for MODULES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 22 |
| module | _MODULE_NAME | Module binding for MODULE NAME in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 40 |
| allowed_modules | path | Path under validation or an explicitly scoped maintained source path. | 'Path &#124; None' | Enclosing invocation or class/instance lifetime | 43, 56 |
| allowed_modules | data_directory | Imported dependency for data directory in allowed_modules; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| allowed_modules | document | Structured reference/Word/AST document owned by the current authoring operation. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| allowed_modules | entries | Local binding for entries in allowed_modules; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| allowed_modules.comprehension_60 | entry | Comprehension item for entry in allowed_modules.comprehension_60; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 61 |
| unapproved_imports | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 69 |
| unapproved_imports | modules | Parameter for modules in unapproved_imports; use the enclosing contract and type below. | frozenset[str] | Enclosing invocation or class/instance lifetime | 69 |
| unapproved_imports | tree | Local binding for tree in unapproved_imports; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| unapproved_imports | rejected | Local binding for rejected in unapproved_imports; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 75 |
| unapproved_imports | node | Loop item for node in unapproved_imports; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 76 |
| unapproved_imports.comprehension_78 | alias | Comprehension item for alias in unapproved_imports.comprehension_78; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 79 |
| module | _METHODS | Module binding for METHODS in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 87 |
| module | _NODES | Module binding for NODES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 90 |
| computation_only | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 166 |
| computation_only | modules | Parameter for modules in computation_only; use the enclosing contract and type below. | frozenset[str] &#124; None | Enclosing invocation or class/instance lifetime | 166, 176 |
| computation_only | tree | Local binding for tree in computation_only; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| computation_only | functions | Local binding for functions in computation_only; use the enclosing contract and type below. | set | Enclosing invocation or class/instance lifetime | 179 |
| computation_only.comprehension_179 | node | Comprehension item for node in computation_only.comprehension_179; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 181 |
| computation_only | imported | Local binding for imported in computation_only; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| computation_only | calls | Local binding for calls in computation_only; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 185 |
| computation_only | node | Loop item for node in computation_only; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 186 |
| computation_only | alias | Loop item for alias in computation_only; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 200, 207 |
| computation_only | module_attribute | Local binding for module attribute in computation_only; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 213 |
