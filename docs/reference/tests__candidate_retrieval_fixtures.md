# Reference for tests/candidate_retrieval_fixtures.py

Explicit retrieval double for legacy browser fixtures; never contacts a model.

Legacy role aliases are test data. This adapter deliberately represents them in
search metadata without claiming production canonical-catalog discovery support.

Source fingerprint: 26b3a43db4c09eba22ac30b666b9e9c70848bfc5e670d206ab505a630a44f963

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### RegistryRetrievalDouble

Return authored fixture descriptors through the same candidate acceptance gate.

Kind: class. Declared return: Not declared / class. Source line: 17.

### RegistryRetrievalDouble.__init__

Inject the browser fixture's catalog-to-owner registry factory and audit hook.

Kind: callable. Declared return: None. Source line: 22.

### RegistryRetrievalDouble._descriptor

Represent an explicit legacy function alias using the generic descriptor contract.

Kind: callable. Declared return: ToolDescriptor. Source line: 28.

### RegistryRetrievalDouble.search

Extract trusted temporary fixture metadata; never approve or execute source.

Kind: callable. Declared return: list[SearchResult]. Source line: 33.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | replace | Imported dependency for replace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | ToolDescriptor | Imported dependency for ToolDescriptor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | CatalogDependencyError | Imported dependency for CatalogDependencyError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| RegistryRetrievalDouble | startup_message | Local binding for startup message in RegistryRetrievalDouble; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 20 |
| RegistryRetrievalDouble.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| RegistryRetrievalDouble.__init__ | registry_factory | Parameter for registry factory in RegistryRetrievalDouble.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 22 |
| RegistryRetrievalDouble.__init__ | audit | Parameter for audit in RegistryRetrievalDouble.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 22 |
| RegistryRetrievalDouble.__init__ | self.registry_factory | Attribute for registry factory in RegistryRetrievalDouble.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 24 |
| RegistryRetrievalDouble.__init__ | self.audit | Attribute for audit in RegistryRetrievalDouble.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 25 |
| RegistryRetrievalDouble._descriptor | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 28 |
| RegistryRetrievalDouble._descriptor | function | Parameter for function in RegistryRetrievalDouble._descriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 28 |
| RegistryRetrievalDouble._descriptor | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 28 |
| RegistryRetrievalDouble._descriptor | item | Local binding for item in RegistryRetrievalDouble._descriptor; use the enclosing contract and type below. | Return type of descriptor_from_source; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| RegistryRetrievalDouble.search | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| RegistryRetrievalDouble.search | catalog | Parameter for catalog in RegistryRetrievalDouble.search; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| RegistryRetrievalDouble.search | handle | Parameter for handle in RegistryRetrievalDouble.search; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| RegistryRetrievalDouble.search | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 33 |
| RegistryRetrievalDouble.search | limit | Parameter for limit in RegistryRetrievalDouble.search; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 33 |
| RegistryRetrievalDouble.search | tools | Local binding for tools in RegistryRetrievalDouble.search; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| RegistryRetrievalDouble.search | descriptors | Local binding for descriptors in RegistryRetrievalDouble.search; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 39, 44 |
| RegistryRetrievalDouble.search.comprehension_39 | tool | Comprehension item for tool in RegistryRetrievalDouble.search.comprehension_39; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 41 |
| RegistryRetrievalDouble.search | folder | Loop item for folder in RegistryRetrievalDouble.search; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 45 |
| RegistryRetrievalDouble.search | source | Explicit source document or source-code text; never imported for reference generation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 46 |
| RegistryRetrievalDouble.search | text | Local binding for text in RegistryRetrievalDouble.search; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| RegistryRetrievalDouble.search | functions | Local binding for functions in RegistryRetrievalDouble.search; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 50 |
| RegistryRetrievalDouble.search.comprehension_50 | node | Comprehension item for node in RegistryRetrievalDouble.search.comprehension_50; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
| RegistryRetrievalDouble.search.comprehension_58 | rank | Comprehension item for rank in RegistryRetrievalDouble.search.comprehension_58; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 60 |
| RegistryRetrievalDouble.search.comprehension_58 | item | Comprehension item for item in RegistryRetrievalDouble.search.comprehension_58; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 60 |
