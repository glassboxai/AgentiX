# Reference for src/agentix/retrieval/contracts.py

Typed retrieval contracts and static Python descriptor extraction.

Descriptors are search metadata, never execution capabilities. Source is parsed
with AST only; no imports, annotation evaluation or fixture execution occurs.

Source fingerprint: 5287d0bf51b4e580fdffd57930336715077ccff352bec9eb548e278e4a0c824e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### EmbeddingProvider

Inject a stable model identity and batch embedding boundary.

Kind: class. Declared return: Not declared / class. Source line: 16.

### EmbeddingProvider.embed

Return one finite, fixed-dimension vector per text or raise an error.

Kind: callable. Declared return: list[list[float]]. Source line: 21.

### KeywordProvider

Inject local generation independently from embedding and storage.

Kind: class. Declared return: Not declared / class. Source line: 26.

### KeywordProvider.generate

Return at most twenty bounded keyword strings, or raise an error.

Kind: callable. Declared return: list[str]. Source line: 31.

### ToolDescriptor

Describe one canonical public function without approval or test claims.

Schemas are JSON data. Artifact references are opaque catalog identifiers,
not filesystem access grants. The digest identifies the indexed contract.

Kind: class. Declared return: Not declared / class. Source line: 37.

### SearchResult

Return a candidate with one-based rank and non-probabilistic RRF score.

Semantic score is cosine similarity; lexical score is BM25. A missing branch
has a None score. Mode is hybrid or keyword_fallback, never authorization.

Kind: class. Declared return: Not declared / class. Source line: 56.

### validate_keywords

Validate bounded JSON-style terms and deduplicate case-insensitively.

Raise ValueError on malformed output; callers distinguish generated failure
from invalid caller input. No coercion of arbitrary objects is performed.

Kind: callable. Declared return: list[str]. Source line: 72.

### _annotation

Extract Python type spelling and literal Annotated description without eval.

Kind: callable. Declared return: dict[str, str]. Source line: 97.

### descriptor_from_source

Parse a canonical synchronous function into search metadata, never executing it.

Parameters are the canonical function name, explicit Python source and opaque
catalog reference. Return a source-bound descriptor; reject ambiguous, missing
or private entrypoints with ValueError and propagate SyntaxError for bad source.

Kind: callable. Declared return: ToolDescriptor. Source line: 116.

### CatalogRejection

Identify an omitted tool and a maintained safe reason code, without source text.

Kind: class. Declared return: Not declared / class. Source line: 154.

### CatalogSnapshot

Represent one complete bounded source scan; unreadable roots must raise.

Kind: class. Declared return: Not declared / class. Source line: 162.

### DescriptorSource

Inject an authoritative descriptor snapshot independently of storage and UI.

Kind: class. Declared return: Not declared / class. Source line: 169.

### DescriptorSource.snapshot

Read a complete snapshot or raise; never convert a failed scan to an empty catalog.

Kind: callable. Declared return: CatalogSnapshot. Source line: 174.

### SyncReport

Describe a completed incremental sync; rejected tools cannot remain searchable.

Kind: class. Declared return: Not declared / class. Source line: 180.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ast | Imported dependency for ast in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Sequence | Imported dependency for Sequence in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| EmbeddingProvider | model_id | Typed binding for model id in EmbeddingProvider; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 19 |
| EmbeddingProvider.embed | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 21 |
| EmbeddingProvider.embed | texts | Parameter for texts in EmbeddingProvider.embed; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 21 |
| KeywordProvider | model_id | Typed binding for model id in KeywordProvider; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 29 |
| KeywordProvider.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 31 |
| KeywordProvider.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 31 |
| ToolDescriptor | tool_id | Typed binding for tool id in ToolDescriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| ToolDescriptor | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 45 |
| ToolDescriptor | description | Typed binding for description in ToolDescriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 46 |
| ToolDescriptor | entrypoint | Typed binding for entrypoint in ToolDescriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 47 |
| ToolDescriptor | input_schema | Typed binding for input schema in ToolDescriptor; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 48 |
| ToolDescriptor | output_schema | Typed binding for output schema in ToolDescriptor; use the enclosing contract and type below. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 49 |
| ToolDescriptor | keywords | Typed binding for keywords in ToolDescriptor; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 50 |
| ToolDescriptor | artifact_ref | Typed binding for artifact ref in ToolDescriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 51 |
| ToolDescriptor | contract_digest | Typed binding for contract digest in ToolDescriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 52 |
| SearchResult | descriptor | Typed binding for descriptor in SearchResult; use the enclosing contract and type below. | ToolDescriptor | Enclosing invocation or class/instance lifetime | 63 |
| SearchResult | rank | Typed binding for rank in SearchResult; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 64 |
| SearchResult | score | Typed binding for score in SearchResult; use the enclosing contract and type below. | float | Enclosing invocation or class/instance lifetime | 65 |
| SearchResult | semantic_score | Typed binding for semantic score in SearchResult; use the enclosing contract and type below. | float &#124; None | Enclosing invocation or class/instance lifetime | 66 |
| SearchResult | lexical_score | Typed binding for lexical score in SearchResult; use the enclosing contract and type below. | float &#124; None | Enclosing invocation or class/instance lifetime | 67 |
| SearchResult | mode | Typed binding for mode in SearchResult; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 68 |
| SearchResult | keyword_model | Typed binding for keyword model in SearchResult; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 69 |
| validate_keywords | value | Value at the current validation/rendering boundary; apply the enclosing contract. | object | Enclosing invocation or class/instance lifetime | 72 |
| validate_keywords | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | tuple | Enclosing invocation or class/instance lifetime | 80 |
| validate_keywords | seen | Local binding for seen in validate_keywords; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 80 |
| validate_keywords | term | Loop item for term in validate_keywords; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 81 |
| validate_keywords | clean | Local binding for clean in validate_keywords; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| _annotation | node | Parameter for node in _annotation; use the enclosing contract and type below. | ast.expr &#124; None | Enclosing invocation or class/instance lifetime | 97 |
| _annotation | parts | Typed binding for parts in _annotation; use the enclosing contract and type below. | Sequence[ast.expr] | Enclosing invocation or class/instance lifetime | 102 |
| _annotation | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | dict | Enclosing invocation or class/instance lifetime | 105 |
| descriptor_from_source | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 116 |
| descriptor_from_source | source | Explicit source document or source-code text; never imported for reference generation. | str | Enclosing invocation or class/instance lifetime | 116 |
| descriptor_from_source | artifact_ref | Parameter for artifact ref in descriptor_from_source; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 116 |
| descriptor_from_source | tree | Local binding for tree in descriptor_from_source; use the enclosing contract and type below. | Return type of parse; see its callable contract | Enclosing invocation or class/instance lifetime | 123 |
| descriptor_from_source | functions | Local binding for functions in descriptor_from_source; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 124 |
| descriptor_from_source.comprehension_124 | n | Comprehension item for n in descriptor_from_source.comprehension_124; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 124 |
| descriptor_from_source | function | Local binding for function in descriptor_from_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 127 |
| descriptor_from_source | positional | Local binding for positional in descriptor_from_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
| descriptor_from_source | parameters | Local binding for parameters in descriptor_from_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 129 |
| descriptor_from_source | properties | Local binding for properties in descriptor_from_source; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 130 |
| descriptor_from_source.comprehension_130 | arg | Comprehension item for arg in descriptor_from_source.comprehension_130; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 130 |
| descriptor_from_source | required | Local binding for required in descriptor_from_source; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 131 |
| descriptor_from_source.comprehension_131 | arg | Comprehension item for arg in descriptor_from_source.comprehension_131; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 131 |
| descriptor_from_source.comprehension_132 | arg | Comprehension item for arg in descriptor_from_source.comprehension_132; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 134 |
| descriptor_from_source.comprehension_132 | default | Comprehension item for default in descriptor_from_source.comprehension_132; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 134 |
| descriptor_from_source | arg | Loop item for arg in descriptor_from_source; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 137 |
| CatalogRejection | tool_id | Typed binding for tool id in CatalogRejection; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 157 |
| CatalogRejection | reason | Typed binding for reason in CatalogRejection; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 158 |
| CatalogSnapshot | descriptors | Typed binding for descriptors in CatalogSnapshot; use the enclosing contract and type below. | tuple[ToolDescriptor, ...] | Enclosing invocation or class/instance lifetime | 165 |
| CatalogSnapshot | rejected | Typed binding for rejected in CatalogSnapshot; use the enclosing contract and type below. | tuple[CatalogRejection, ...] | Enclosing invocation or class/instance lifetime | 166 |
| DescriptorSource | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 172 |
| DescriptorSource.snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 174 |
| SyncReport | added | Typed binding for added in SyncReport; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 183 |
| SyncReport | updated | Typed binding for updated in SyncReport; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 184 |
| SyncReport | removed | Typed binding for removed in SyncReport; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 185 |
| SyncReport | unchanged | Typed binding for unchanged in SyncReport; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 186 |
| SyncReport | rejected | Typed binding for rejected in SyncReport; use the enclosing contract and type below. | tuple[CatalogRejection, ...] | Enclosing invocation or class/instance lifetime | 187 |
