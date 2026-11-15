# Reference for tests/test_retrieval_ollama.py

Opt-in real local retrieval evaluation; never import or execute tool snapshots.

Run explicitly with -m ollama_retrieval. This separate model choice is authorized
for RAG metadata retrieval, not application-generation acceptance.

Source fingerprint: 4a55a223d3d303d06f7762bbaf9ca4c1d20a99d101d1b807ea99add6ff8922f5

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_local_ollama_retrieval

Evaluate four reviewed expected top hits with installed local models only.

Missing/unavailable models fail this explicit evaluation, rather than silently
skipping or pulling a model. Storage is temporary and fixture code is inert.

Kind: callable. Declared return: None. Source line: 26.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | OllamaClient | Imported dependency for OllamaClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | OllamaEmbeddings | Imported dependency for OllamaEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | OllamaKeywords | Imported dependency for OllamaKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | descriptor_from_source | Imported dependency for descriptor from source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 22 |
| module | pytestmark | Module binding for pytestmark in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 23 |
| test_local_ollama_retrieval | tmp_path | Parameter for tmp path in test_local_ollama_retrieval; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 26 |
| test_local_ollama_retrieval | client | Local binding for client in test_local_ollama_retrieval; use the enclosing contract and type below. | Return type of OllamaClient; see its callable contract | Enclosing invocation or class/instance lifetime | 32 |
| test_local_ollama_retrieval | service | Local binding for service in test_local_ollama_retrieval; use the enclosing contract and type below. | Return type of ToolRetriever; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_local_ollama_retrieval | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_local_ollama_retrieval | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 35 |
| test_local_ollama_retrieval | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 36 |
| test_local_ollama_retrieval | source | Explicit source document or source-code text; never imported for reference generation. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_local_ollama_retrieval | case_id | Loop item for case id in test_local_ollama_retrieval; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| test_local_ollama_retrieval | query | Original user request or a trusted test query; avoid payload logging by default. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| test_local_ollama_retrieval | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| test_local_ollama_retrieval | started | Local binding for started in test_local_ollama_retrieval; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_local_ollama_retrieval | results | Local binding for results in test_local_ollama_retrieval; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
