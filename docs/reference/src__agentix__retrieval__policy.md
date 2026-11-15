# Reference for src/agentix/retrieval/policy.py

Named retrieval policies, algorithm parameters and measurement units.

Values preserve the approved RAG-001 behavior. Limits with equal numeric values
remain separate when their meaning or units differ. These internal constants are
not a runtime configuration API. Changing INDEX_SCHEMA_VERSION requires an
explicit storage compatibility decision; ranking tuning does not change schema.

Source fingerprint: 49a61d164e796a6a1ad14b8d64dfc616465e25109855eecc593c565f326665f7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Final | Imported dependency for Final in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | BYTES_PER_KIB | Typed binding for BYTES PER KIB in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 12 |
| module | BYTES_PER_MIB | Typed binding for BYTES PER MIB in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 13 |
| module | MILLISECONDS_PER_SECOND | Typed binding for MILLISECONDS PER SECOND in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 14 |
| module | DEFAULT_SEARCH_LIMIT | Typed binding for DEFAULT SEARCH LIMIT in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 17 |
| module | MIN_SEARCH_LIMIT | Typed binding for MIN SEARCH LIMIT in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 18 |
| module | MAX_SEARCH_LIMIT | Typed binding for MAX SEARCH LIMIT in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 19 |
| module | MIN_BRANCH_CANDIDATES | Typed binding for MIN BRANCH CANDIDATES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 20 |
| module | BRANCH_CANDIDATE_MULTIPLIER | Typed binding for BRANCH CANDIDATE MULTIPLIER in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 21 |
| module | RRF_RANK_CONSTANT | Typed binding for RRF RANK CONSTANT in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 22 |
| module | BM25_K1 | Typed binding for BM25 K1 in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 25 |
| module | BM25_B | Typed binding for BM25 B in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 26 |
| module | BM25_IDF_SMOOTHING | Typed binding for BM25 IDF SMOOTHING in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 27 |
| module | MAX_KEYWORD_COUNT | Typed binding for MAX KEYWORD COUNT in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 30 |
| module | MAX_KEYWORD_CHARACTERS | Typed binding for MAX KEYWORD CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 31 |
| module | MAX_KEYWORD_RESPONSE_CHARACTERS | Typed binding for MAX KEYWORD RESPONSE CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 32 |
| module | KEYWORD_GENERATION_MAX_TOKENS | Typed binding for KEYWORD GENERATION MAX TOKENS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 33 |
| module | KEYWORD_GENERATION_TEMPERATURE | Typed binding for KEYWORD GENERATION TEMPERATURE in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 34 |
| module | INDEX_SCHEMA_VERSION | Typed binding for INDEX SCHEMA VERSION in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 39 |
| module | MAX_TOOL_ID_CHARACTERS | Typed binding for MAX TOOL ID CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 40 |
| module | MAX_DESCRIPTOR_FIELD_CHARACTERS | Typed binding for MAX DESCRIPTOR FIELD CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 41 |
| module | MAX_DESCRIPTOR_BYTES | Typed binding for MAX DESCRIPTOR BYTES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 42 |
| module | MAX_QUERY_BYTES | Typed binding for MAX QUERY BYTES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 43 |
| module | DEFAULT_OLLAMA_TIMEOUT_SECONDS | Typed binding for DEFAULT OLLAMA TIMEOUT SECONDS in module; use the enclosing contract and type below. | Final[float] | Module/process lifetime | 46 |
| module | MAX_HTTP_REQUEST_BYTES | Typed binding for MAX HTTP REQUEST BYTES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 47 |
| module | MAX_HTTP_RESPONSE_BYTES | Typed binding for MAX HTTP RESPONSE BYTES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 48 |
| module | MAX_LOG_MODEL_ID_CHARACTERS | Typed binding for MAX LOG MODEL ID CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 51 |
| module | LOG_TOOL_HASH_CHARACTERS | Typed binding for LOG TOOL HASH CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 52 |
| module | MAX_CATALOG_ENTRIES | Typed binding for MAX CATALOG ENTRIES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 55 |
| module | MAX_CATALOG_SOURCE_BYTES | Typed binding for MAX CATALOG SOURCE BYTES in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 56 |
