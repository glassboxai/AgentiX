# Reference for src/agentix/storage/locations.py

Stable explicit per-user v7 paths; resolving a path never creates directories.

Source fingerprint: 824c69848d29ba18bc52d5360862e6f719027dd9f33b930dcd79f63ea67a931a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### require_v7_namespace

Reject a resolved path inside the retired AgentiX v5 persistent namespace.

Comparison uses whole path segments of the resolved path, so an unrelated
directory whose name merely contains ``v5`` is accepted. Nothing is created.

Kind: callable. Declared return: Path. Source line: 11.

### user_home

Return the explicitly configured deployment home; no legacy default applies.

AGENTIX_HOME is mandatory because the retired v5 profile must never receive
v7 state. Relative roots, traversal and existing aliases are rejected, and no
files are read recursively.

Kind: callable. Declared return: Path. Source line: 28.

### data_directory

Return the common data root for tools, apps, grants and model metadata.

Kind: callable. Declared return: Path. Source line: 55.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | stat | Imported dependency for stat in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Mapping | Imported dependency for Mapping in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | _LEGACY_NAMESPACES | Module binding for LEGACY NAMESPACES in module; use the enclosing contract and type below. | tuple | Module/process lifetime | 8 |
| require_v7_namespace | path | Path under validation or an explicitly scoped maintained source path. | Path | Enclosing invocation or class/instance lifetime | 11 |
| require_v7_namespace | label | Parameter for label in require_v7_namespace; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 11 |
| require_v7_namespace | resolved | Local binding for resolved in require_v7_namespace; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| require_v7_namespace | parts | Local binding for parts in require_v7_namespace; use the enclosing contract and type below. | Return type of tuple; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| require_v7_namespace.comprehension_18 | part | Comprehension item for part in require_v7_namespace.comprehension_18; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 18 |
| require_v7_namespace | index | Loop item for index in require_v7_namespace; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 19 |
| user_home | environment | Parameter for environment in user_home; use the enclosing contract and type below. | Mapping[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 28 |
| user_home | values | Local binding for values in user_home; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| user_home | configured | Local binding for configured in user_home; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 36 |
| user_home | root | Explicit root directory against which named paths are resolved. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| user_home | part | Loop item for part in user_home; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 45 |
| data_directory | environment | Parameter for environment in data_directory; use the enclosing contract and type below. | Mapping[str, str] &#124; None | Enclosing invocation or class/instance lifetime | 55 |
