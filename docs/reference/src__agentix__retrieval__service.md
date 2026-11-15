# Reference for src/agentix/retrieval/service.py

Independent persistent hybrid retrieval; candidates never authorize execution.

All operations are serialized per instance. Multiple writer processes/instances
must be coordinated by the caller. ChromaDB and provider failures remain explicit.
No generated code is imported, executed or discovered by this module.

Source fingerprint: fd90d70cef960fc421be3f12641938d7693e82837a31dd7e35d70b14580b659f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ToolRetriever

Coordinate storage, local model boundaries and hybrid candidate ranking.

Chroma is initialized only on explicit construction. Providers are injected;
default Ollama adapters are composed by the caller. No global handlers or
agent wiring are changed. Use a dedicated database directory for this index.

Kind: class. Declared return: Not declared / class. Source line: 36.

### ToolRetriever.__init__

Open a cosine collection and reject incompatible model/schema identities.

Unbound construction creates storage without inference. An explicitly bound
descriptor source performs its first sync, including embeddings. The first write
establishes embedding dimensions. Raise ValueError for incompatible indexes;
underlying storage exceptions are propagated.

Kind: callable. Declared return: None. Source line: 44.

### ToolRetriever._bind_source

Persist source identity and refuse unrelated or unbound reuse of an owned index.

Kind: callable. Declared return: None. Source line: 99.

### ToolRetriever.synchronize

Reconcile a complete authoritative snapshot before serving catalog candidates.

Remove deleted/rejected entries, embed only new/changed descriptors and keep
unchanged vectors. Scan/provider/storage failures propagate and prevent search;
partial writes are retried on the next sync. No transaction or watcher is claimed.

Kind: callable. Declared return: SyncReport. Source line: 121.

### ToolRetriever._model_tag

Bound and sanitize configured model identifiers before diagnostics.

Kind: callable. Declared return: str. Source line: 196.

### ToolRetriever._operation

Serialize operations and log safe outcomes, elapsed milliseconds and correlation.

Kind: callable. Declared return: Iterator[str]. Source line: 205.

### ToolRetriever._event

Emit maintained diagnostic fields only; never accept provider payloads.

Kind: callable. Declared return: None. Source line: 227.

### ToolRetriever._vectors

Validate finite nonzero vectors and persist the initial index dimension.

Raise ValueError on malformed output or model/dimension changes. Provider
errors propagate; storing a dimension never constitutes a successful upsert.

Kind: callable. Declared return: list[list[float]]. Source line: 252.

### ToolRetriever._payload

Validate and snapshot JSON metadata, returning storage and searchable text.

Kind: callable. Declared return: tuple[str, str]. Source line: 285.

### ToolRetriever.upsert

Insert or replace a descriptor and vector by ID; never inspect artifact paths.

Kind: callable. Declared return: None. Source line: 328.

### ToolRetriever._store_descriptor

Persist one validated descriptor/vector using the owning operation's diagnostics.

Kind: callable. Declared return: None. Source line: 333.

### ToolRetriever.delete

Idempotently remove an explicit ID; invalid IDs raise ValueError.

Kind: callable. Declared return: None. Source line: 355.

### ToolRetriever.search

Return hybrid candidates, not approvals, with at most limit entries.

A nonempty query is bounded to 32 KiB and limit to 1..100. Empty storage
avoids all model calls. Keyword generation failure degrades explicitly;
embedding/storage errors propagate. Bound sources synchronize before querying.
Changes after that scan are observed on the next search; no watcher is started.
No score threshold is imposed.

Kind: callable. Declared return: list[SearchResult]. Source line: 368.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | uuid | Imported dependency for uuid in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | contextmanager | Imported dependency for contextmanager in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | asdict | Imported dependency for asdict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | DescriptorSource | Imported dependency for DescriptorSource in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | EmbeddingProvider | Imported dependency for EmbeddingProvider in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | KeywordProvider | Imported dependency for KeywordProvider in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | SyncReport | Imported dependency for SyncReport in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | ToolDescriptor | Imported dependency for ToolDescriptor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | validate_keywords | Imported dependency for validate keywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | bm25 | Imported dependency for bm25 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 31 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 33 |
| ToolRetriever.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 45 |
| ToolRetriever.__init__ | path | Path under validation or an explicitly scoped maintained source path. | str &#124; Path | Enclosing invocation or class/instance lifetime | 46 |
| ToolRetriever.__init__ | embeddings | Parameter for embeddings in ToolRetriever.__init__; use the enclosing contract and type below. | EmbeddingProvider | Enclosing invocation or class/instance lifetime | 47 |
| ToolRetriever.__init__ | keyword_generator | Parameter for keyword generator in ToolRetriever.__init__; use the enclosing contract and type below. | KeywordProvider | Enclosing invocation or class/instance lifetime | 48 |
| ToolRetriever.__init__ | collection_name | Parameter for collection name in ToolRetriever.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 50 |
| ToolRetriever.__init__ | descriptor_source | Parameter for descriptor source in ToolRetriever.__init__; use the enclosing contract and type below. | DescriptorSource &#124; None | Enclosing invocation or class/instance lifetime | 51 |
| ToolRetriever.__init__ | chromadb | Imported dependency for chromadb in ToolRetriever.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 60 |
| ToolRetriever.__init__ | Settings | Imported dependency for Settings in ToolRetriever.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 61 |
| ToolRetriever.__init__ | self.embeddings | Attribute for embeddings in ToolRetriever.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63 |
| ToolRetriever.__init__ | self.keyword_generator | Attribute for keyword generator in ToolRetriever.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| ToolRetriever.__init__ | self._lock | Attribute for lock in ToolRetriever.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| ToolRetriever.__init__ | self._source | Attribute for source in ToolRetriever.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| ToolRetriever.__init__ | self.last_sync_report | Attribute for last sync report in ToolRetriever.__init__; use the enclosing contract and type below. | SyncReport &#124; None | Enclosing invocation or class/instance lifetime | 67 |
| ToolRetriever.__init__ | self._client | Attribute for client in ToolRetriever.__init__; use the enclosing contract and type below. | Return type of PersistentClient; see its callable contract | Enclosing invocation or class/instance lifetime | 70 |
| ToolRetriever.__init__ | self._collection | Attribute for collection in ToolRetriever.__init__; use the enclosing contract and type below. | Return type of get_or_create_collection; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| ToolRetriever.__init__ | metadata | Local binding for metadata in ToolRetriever.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 82 |
| ToolRetriever._bind_source | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 99 |
| ToolRetriever._bind_source | metadata | Local binding for metadata in ToolRetriever._bind_source; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 101 |
| ToolRetriever._bind_source | bound | Local binding for bound in ToolRetriever._bind_source; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 102 |
| ToolRetriever._bind_source | identity | Explicit owner identity used by a session factory or fixture. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 107 |
| ToolRetriever.synchronize | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| ToolRetriever.synchronize | operation | Managed resource for operation in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of _operation; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 128 |
| ToolRetriever.synchronize | started | Local binding for started in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 131, 165 |
| ToolRetriever.synchronize | snapshot | Local binding for snapshot in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| ToolRetriever.synchronize | desired | Local binding for desired in ToolRetriever.synchronize; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 133 |
| ToolRetriever.synchronize.comprehension_133 | item | Comprehension item for item in ToolRetriever.synchronize.comprehension_133; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 133 |
| ToolRetriever.synchronize | item | Loop item for item in ToolRetriever.synchronize; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 136, 171 |
| ToolRetriever.synchronize | entry | Loop item for entry in ToolRetriever.synchronize; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 146 |
| ToolRetriever.synchronize | reconcile_started | Local binding for reconcile started in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 157 |
| ToolRetriever.synchronize | stored | Local binding for stored in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 158 |
| ToolRetriever.synchronize | existing | Local binding for existing in ToolRetriever.synchronize; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 159 |
| ToolRetriever.synchronize.comprehension_159 | key | Comprehension item for key in ToolRetriever.synchronize.comprehension_159; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 161 |
| ToolRetriever.synchronize.comprehension_159 | metadata | Comprehension item for metadata in ToolRetriever.synchronize.comprehension_159; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 161 |
| ToolRetriever.synchronize | removed | Local binding for removed in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 163 |
| ToolRetriever.synchronize | added | Local binding for added in ToolRetriever.synchronize; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 170, 179 |
| ToolRetriever.synchronize | updated | Local binding for updated in ToolRetriever.synchronize; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 170, 177 |
| ToolRetriever.synchronize | unchanged | Local binding for unchanged in ToolRetriever.synchronize; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 170, 173 |
| ToolRetriever.synchronize | key | Loop item for key in ToolRetriever.synchronize; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 171 |
| ToolRetriever.synchronize | report | Local binding for report in ToolRetriever.synchronize; use the enclosing contract and type below. | Return type of SyncReport; see its callable contract | Enclosing invocation or class/instance lifetime | 180 |
| ToolRetriever.synchronize | self.last_sync_report | Attribute for last sync report in ToolRetriever.synchronize; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 181 |
| ToolRetriever._model_tag | provider | Parameter for provider in ToolRetriever._model_tag; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 196 |
| ToolRetriever._operation | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 205 |
| ToolRetriever._operation | stage | Parameter for stage in ToolRetriever._operation; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 205 |
| ToolRetriever._operation | operation | Local binding for operation in ToolRetriever._operation; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 207 |
| ToolRetriever._operation | started | Local binding for started in ToolRetriever._operation; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 208 |
| ToolRetriever._operation | exc | Caught exception for exc in ToolRetriever._operation; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 213 |
| ToolRetriever._event | operation | Parameter for operation in ToolRetriever._event; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 228 |
| ToolRetriever._event | stage | Parameter for stage in ToolRetriever._event; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 229 |
| ToolRetriever._event | outcome | Parameter for outcome in ToolRetriever._event; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 230 |
| ToolRetriever._event | started | Parameter for started in ToolRetriever._event; use the enclosing contract and type below. | float &#124; None | Enclosing invocation or class/instance lifetime | 232 |
| ToolRetriever._event | level | Parameter for level in ToolRetriever._event; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 233 |
| ToolRetriever._event | details | Parameter for details in ToolRetriever._event; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 234 |
| ToolRetriever._event | duration | Local binding for duration in ToolRetriever._event; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 237 |
| ToolRetriever._vectors | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 252 |
| ToolRetriever._vectors | texts | Parameter for texts in ToolRetriever._vectors; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 252 |
| ToolRetriever._vectors | vectors | Local binding for vectors in ToolRetriever._vectors; use the enclosing contract and type below. | Return type of embed; see its callable contract | Enclosing invocation or class/instance lifetime | 258 |
| ToolRetriever._vectors | dimension | Local binding for dimension in ToolRetriever._vectors; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 261, 274 |
| ToolRetriever._vectors | vector | Loop item for vector in ToolRetriever._vectors; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 262 |
| ToolRetriever._vectors.comprehension_265 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 269 |
| ToolRetriever._vectors.comprehension_270 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 270 |
| ToolRetriever._vectors | metadata | Local binding for metadata in ToolRetriever._vectors; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 275 |
| ToolRetriever._payload | descriptor | Parameter for descriptor in ToolRetriever._payload; use the enclosing contract and type below. | ToolDescriptor | Enclosing invocation or class/instance lifetime | 285 |
| ToolRetriever._payload | data | Local binding for data in ToolRetriever._payload; use the enclosing contract and type below. | Return type of asdict; see its callable contract | Enclosing invocation or class/instance lifetime | 289 |
| ToolRetriever._payload | key | Loop item for key in ToolRetriever._payload; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 290 |
| ToolRetriever._payload | payload | Local binding for payload in ToolRetriever._payload; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 311 |
| ToolRetriever._payload | document | Structured reference/Word/AST document owned by the current authoring operation. | Return type of join; see its callable contract | Enclosing invocation or class/instance lifetime | 316 |
| ToolRetriever.upsert | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 328 |
| ToolRetriever.upsert | descriptor | Parameter for descriptor in ToolRetriever.upsert; use the enclosing contract and type below. | ToolDescriptor | Enclosing invocation or class/instance lifetime | 328 |
| ToolRetriever.upsert | operation | Managed resource for operation in ToolRetriever.upsert; use the enclosing contract and type below. | Return type of _operation; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 330 |
| ToolRetriever._store_descriptor | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 333 |
| ToolRetriever._store_descriptor | descriptor | Parameter for descriptor in ToolRetriever._store_descriptor; use the enclosing contract and type below. | ToolDescriptor | Enclosing invocation or class/instance lifetime | 333 |
| ToolRetriever._store_descriptor | operation | Parameter for operation in ToolRetriever._store_descriptor; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 333 |
| ToolRetriever._store_descriptor | payload | Local binding for payload in ToolRetriever._store_descriptor; use the enclosing contract and type below. | Return type of _payload; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| ToolRetriever._store_descriptor | document | Structured reference/Word/AST document owned by the current authoring operation. | Return type of _payload; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| ToolRetriever._store_descriptor | started | Local binding for started in ToolRetriever._store_descriptor; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 336, 346 |
| ToolRetriever._store_descriptor | vectors | Local binding for vectors in ToolRetriever._store_descriptor; use the enclosing contract and type below. | Return type of _vectors; see its callable contract | Enclosing invocation or class/instance lifetime | 337 |
| ToolRetriever.delete | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 355 |
| ToolRetriever.delete | tool_id | Parameter for tool id in ToolRetriever.delete; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 355 |
| ToolRetriever.delete | operation | Managed resource for operation in ToolRetriever.delete; use the enclosing contract and type below. | Return type of _operation; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 357 |
| ToolRetriever.delete | started | Local binding for started in ToolRetriever.delete; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 364 |
| ToolRetriever.search | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 369 |
| ToolRetriever.search | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 370 |
| ToolRetriever.search | keywords | Parameter for keywords in ToolRetriever.search; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 371 |
| ToolRetriever.search | limit | Parameter for limit in ToolRetriever.search; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 372 |
| ToolRetriever.search | operation | Managed resource for operation in ToolRetriever.search; use the enclosing contract and type below. | Return type of _operation; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 382 |
| ToolRetriever.search | supplied | Local binding for supplied in ToolRetriever.search; use the enclosing contract and type below. | Return type of validate_keywords; see its callable contract | Enclosing invocation or class/instance lifetime | 399 |
| ToolRetriever.search | started | Local binding for started in ToolRetriever.search; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 402, 408, 439, 443, 453, 463 |
| ToolRetriever.search | snapshot | Local binding for snapshot in ToolRetriever.search; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 403 |
| ToolRetriever.search | count | Local binding for count in ToolRetriever.search; use the enclosing contract and type below. | Return type of len; see its callable contract | Enclosing invocation or class/instance lifetime | 404 |
| ToolRetriever.search | mode | Local binding for mode in ToolRetriever.search; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 409, 421 |
| ToolRetriever.search | generated | Local binding for generated in ToolRetriever.search; use the enclosing contract and type below. | Return type of validate_keywords; see its callable contract | Enclosing invocation or class/instance lifetime | 411, 421 |
| ToolRetriever.search | exc | Caught exception for exc in ToolRetriever.search; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 420 |
| ToolRetriever.search | documents | Local binding for documents in ToolRetriever.search; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 431 |
| ToolRetriever.search | descriptors | Local binding for descriptors in ToolRetriever.search; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 432 |
| ToolRetriever.search.comprehension_432 | key | Comprehension item for key in ToolRetriever.search.comprehension_432; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 434 |
| ToolRetriever.search.comprehension_432 | meta | Comprehension item for meta in ToolRetriever.search.comprehension_432; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 434 |
| ToolRetriever.search | candidate_limit | Local binding for candidate limit in ToolRetriever.search; use the enclosing contract and type below. | Return type of min; see its callable contract | Enclosing invocation or class/instance lifetime | 436 |
| ToolRetriever.search | lexical | Local binding for lexical in ToolRetriever.search; use the enclosing contract and type below. | Return type of bm25; see its callable contract | Enclosing invocation or class/instance lifetime | 440 |
| ToolRetriever.search | lexical_ids | Local binding for lexical ids in ToolRetriever.search; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 441 |
| ToolRetriever.search.lambda_441 | key | Callback parameter for key in ToolRetriever.search.lambda_441; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 441 |
| ToolRetriever.search | vector | Local binding for vector in ToolRetriever.search; use the enclosing contract and type below. | Return type of _vectors; see its callable contract | Enclosing invocation or class/instance lifetime | 444 |
| ToolRetriever.search | response | Bounded response text to render or validate; it is not executable code. | Return type of query; see its callable contract | Enclosing invocation or class/instance lifetime | 454 |
| ToolRetriever.search | semantic | Local binding for semantic in ToolRetriever.search; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 457 |
| ToolRetriever.search.comprehension_457 | key | Comprehension item for key in ToolRetriever.search.comprehension_457; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 459 |
| ToolRetriever.search.comprehension_457 | distance | Comprehension item for distance in ToolRetriever.search.comprehension_457; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 459 |
| ToolRetriever.search | semantic_ids | Local binding for semantic ids in ToolRetriever.search; use the enclosing contract and type below. | Return type of sorted; see its callable contract | Enclosing invocation or class/instance lifetime | 461 |
| ToolRetriever.search.lambda_461 | key | Callback parameter for key in ToolRetriever.search.lambda_461; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 461 |
| ToolRetriever.search | scores | Typed binding for scores in ToolRetriever.search; use the enclosing contract and type below. | dict[str, float] | Enclosing invocation or class/instance lifetime | 464 |
| ToolRetriever.search | branch | Loop item for branch in ToolRetriever.search; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 465 |
| ToolRetriever.search | rank | Loop item for rank in ToolRetriever.search; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 466, 469 |
| ToolRetriever.search | key | Loop item for key in ToolRetriever.search; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 466, 469 |
| ToolRetriever.search | ranked | Local binding for ranked in ToolRetriever.search; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 468 |
| ToolRetriever.search.lambda_468 | key | Callback parameter for key in ToolRetriever.search.lambda_468; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 468 |
| ToolRetriever.search | selected | Local binding for selected in ToolRetriever.search; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 484 |
| ToolRetriever.search.comprehension_499 | rank | Comprehension item for rank in ToolRetriever.search.comprehension_499; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 509 |
| ToolRetriever.search.comprehension_499 | key | Comprehension item for key in ToolRetriever.search.comprehension_499; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 509 |
