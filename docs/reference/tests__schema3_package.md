# Reference for tests/schema3_package.py

Build a real schema-3 application package from approved catalog fixtures.

The helper replaces the retired fixed text-analysis package. It performs no model
inference: the coordinator boundary returns authored artifacts, and the pipeline
still validates manifests, connection code and widget contracts.

Source fingerprint: 58e32f9518fb463332f99d1c1a6fc61b4c7d08f8964c0ab3f3137e3b74dc26dd

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### build

Return a generated candidate whose package is a valid schema-3 application.

Kind: callable. Declared return: Not declared / class. Source line: 29.

### build.factory

Return authored artifacts across the production coordinator boundary.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### build.factory.client

Never infer with a real model in package fixtures.

Kind: callable. Declared return: Not declared / class. Source line: 42.

### widget_source

Render a minimal approved widget importing the exact tool module.

Kind: callable. Declared return: str. Source line: 64.

### package

Return only the generated package directory for capture-level tests.

Kind: callable. Declared return: Path. Source line: 92.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | CONNECTION_CODE | Module binding for CONNECTION CODE in module; use the enclosing contract and type below. | Return type of join; see its callable contract | Module/process lifetime | 10 |
| module | WIDGET_TESTS | Module binding for WIDGET TESTS in module; use the enclosing contract and type below. | str | Module/process lifetime | 21 |
| build | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 29 |
| build | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 29 |
| build | installed | Imported dependency for installed in build; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| build | registry | Imported dependency for registry in build; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| build | ApplicationPipeline | Imported dependency for ApplicationPipeline in build; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 33 |
| build | tools_root | Local binding for tools root in build; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| build | tools | Local binding for tools in build; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| build.factory | folder | Parameter for folder in build.factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| build.factory.client | role | Parameter for role in build.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| build.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 42 |
| build.factory.client | module | Local binding for module in build.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| build.factory.client | catalog | Local binding for catalog in build.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 51 |
| build.factory.client.comprehension_54 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 54 |
| widget_source | module | Parameter for module in widget_source; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 64 |
| widget_source | function | Local binding for function in widget_source; use the enclosing contract and type below. | Return type of removesuffix; see its callable contract | Enclosing invocation or class/instance lifetime | 66 |
| package | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 92 |
