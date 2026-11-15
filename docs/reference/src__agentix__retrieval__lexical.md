# Reference for src/agentix/retrieval/lexical.py

Offline lexical scoring for arbitrary domain terms and Python identifiers.

Source fingerprint: bacb3e539fecad13da50d31f1157111735adc86d31b765571e7c049bea090ee4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### tokens

Keep complete Unicode identifiers and add underscore/camel-case segments.

Kind: callable. Declared return: list[str]. Source line: 10.

### bm25

Return positive BM25 scores using k1=1.5 and b=0.75; no persistent side index.

Rebuild from the same stored snapshot used for semantic retrieval. This favors
correctness after updates/reopen over large-corpus performance in the first release.

Kind: callable. Declared return: dict[str, float]. Source line: 23.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | math | Imported dependency for math in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Counter | Imported dependency for Counter in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | BM25_B | Imported dependency for BM25 B in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | BM25_IDF_SMOOTHING | Imported dependency for BM25 IDF SMOOTHING in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | BM25_K1 | Imported dependency for BM25 K1 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| tokens | text | Parameter for text in tokens; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 10 |
| tokens | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | list | Enclosing invocation or class/instance lifetime | 12 |
| tokens | word | Loop item for word in tokens; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 13 |
| tokens | segmented | Local binding for segmented in tokens; use the enclosing contract and type below. | Return type of sub; see its callable contract | Enclosing invocation or class/instance lifetime | 15, 16 |
| tokens | parts | Local binding for parts in tokens; use the enclosing contract and type below. | Return type of split; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| bm25 | documents | Parameter for documents in bm25; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 23 |
| bm25 | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 23 |
| bm25 | counts | Local binding for counts in bm25; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 29 |
| bm25.comprehension_29 | key | Comprehension item for key in bm25.comprehension_29; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 29 |
| bm25.comprehension_29 | text | Comprehension item for text in bm25.comprehension_29; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 29 |
| bm25 | lengths | Local binding for lengths in bm25; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 30 |
| bm25.comprehension_30 | key | Comprehension item for key in bm25.comprehension_30; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 30 |
| bm25.comprehension_30 | count | Comprehension item for count in bm25.comprehension_30; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 30 |
| bm25 | average | Local binding for average in bm25; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 31 |
| bm25 | scores | Local binding for scores in bm25; use the enclosing contract and type below. | Return type of fromkeys; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| bm25 | term | Loop item for term in bm25; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 33 |
| bm25 | frequency | Local binding for frequency in bm25; use the enclosing contract and type below. | Return type of sum; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| bm25.comprehension_34 | count | Comprehension item for count in bm25.comprehension_34; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 34 |
| bm25 | idf | Local binding for idf in bm25; use the enclosing contract and type below. | Return type of log; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| bm25 | key | Loop item for key in bm25; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 38 |
| bm25 | count | Loop item for count in bm25; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 38 |
| bm25 | tf | Local binding for tf in bm25; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| bm25 | length_normalization | Local binding for length normalization in bm25; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| bm25.comprehension_42 | key | Comprehension item for key in bm25.comprehension_42; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
| bm25.comprehension_42 | score | Comprehension item for score in bm25.comprehension_42; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 42 |
