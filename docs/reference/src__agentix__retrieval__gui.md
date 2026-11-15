# Reference for src/agentix/retrieval/gui.py

GUI composition boundary for catalog retrieval with private provider clients.

One service serializes index operations within the GUI process. Each owner retains
its own retriever/providers in a handle; startup clients are not shared with owners.
Do not run the standalone index writer concurrently from another process.

Source fingerprint: c23ae7d9f4d59a8c2a129de2cd14947122d3c4d7bd6d98de26f0b9dd8cfc412c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### RetrieverHandle

Own one session's retriever and the physical catalog identity it serves.

Kind: class. Declared return: Not declared / class. Source line: 30.

### catalog_retriever

Compose local providers and the same dedicated index used by the sync CLI.

Kind: callable. Declared return: ToolRetriever. Source line: 37.

### GuiToolRetrieval

Serialize one GUI's catalog access without retaining a shared model client.

Kind: class. Declared return: Not declared / class. Source line: 48.

### GuiToolRetrieval.__init__

Inject explicit composition; construction performs no inference or filesystem IO.

Kind: callable. Declared return: None. Source line: 51.

### GuiToolRetrieval.initialize

Load at GUI startup; record safe failure and allow later search to retry.

Kind: callable. Declared return: str. Source line: 57.

### GuiToolRetrieval.search

Synchronize/search through an owner-private client under the common index lock.

Failures propagate to the controller for safe UI reporting. A changed catalog
root creates a new bound client rather than reusing another source's index.

Kind: callable. Declared return: list[SearchResult]. Source line: 78.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | policy | Imported dependency for policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | CatalogToolSource | Imported dependency for CatalogToolSource in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | OllamaClient | Imported dependency for OllamaClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | OllamaEmbeddings | Imported dependency for OllamaEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | OllamaKeywords | Imported dependency for OllamaKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 26 |
| RetrieverHandle | retriever | Typed binding for retriever in RetrieverHandle; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 33 |
| RetrieverHandle | root | Explicit root directory against which named paths are resolved. | str | Enclosing invocation or class/instance lifetime | 34 |
| catalog_retriever | catalog | Parameter for catalog in catalog_retriever; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 37 |
| catalog_retriever | client | Local binding for client in catalog_retriever; use the enclosing contract and type below. | Return type of OllamaClient; see its callable contract | Enclosing invocation or class/instance lifetime | 39 |
| GuiToolRetrieval.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| GuiToolRetrieval.__init__ | factory | Parameter for factory in GuiToolRetrieval.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 51 |
| GuiToolRetrieval.__init__ | self.factory | Attribute for factory in GuiToolRetrieval.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| GuiToolRetrieval.__init__ | self.lock | Attribute for lock in GuiToolRetrieval.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| GuiToolRetrieval.__init__ | self.startup_message | Attribute for startup message in GuiToolRetrieval.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 55 |
| GuiToolRetrieval.initialize | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| GuiToolRetrieval.initialize | catalog | Parameter for catalog in GuiToolRetrieval.initialize; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 57 |
| GuiToolRetrieval.initialize | started | Local binding for started in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| GuiToolRetrieval.initialize | temporary | Local binding for temporary in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Return type of factory; see its callable contract | Enclosing invocation or class/instance lifetime | 62 |
| GuiToolRetrieval.initialize | report | Local binding for report in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 63 |
| GuiToolRetrieval.initialize | count | Local binding for count in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| GuiToolRetrieval.initialize | self.startup_message | Attribute for startup message in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 65, 68 |
| GuiToolRetrieval.initialize | outcome | Local binding for outcome in GuiToolRetrieval.initialize; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 66, 69 |
| GuiToolRetrieval.initialize | error_type | Local binding for error type in GuiToolRetrieval.initialize; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 66, 69 |
| GuiToolRetrieval.initialize | error | Caught exception for error in GuiToolRetrieval.initialize; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 67 |
| GuiToolRetrieval.search | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| GuiToolRetrieval.search | catalog | Parameter for catalog in GuiToolRetrieval.search; use the enclosing contract and type below. | ToolCatalog | Enclosing invocation or class/instance lifetime | 79 |
| GuiToolRetrieval.search | handle | Parameter for handle in GuiToolRetrieval.search; use the enclosing contract and type below. | RetrieverHandle | Enclosing invocation or class/instance lifetime | 79 |
| GuiToolRetrieval.search | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 79 |
| GuiToolRetrieval.search | limit | Parameter for limit in GuiToolRetrieval.search; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 79 |
| GuiToolRetrieval.search | root | Explicit root directory against which named paths are resolved. | Return type of normcase; see its callable contract | Enclosing invocation or class/instance lifetime | 86 |
| GuiToolRetrieval.search | handle.retriever | Attribute for handle.retriever in GuiToolRetrieval.search; use the enclosing contract and type below. | Return type of factory; see its callable contract | Enclosing invocation or class/instance lifetime | 90 |
| GuiToolRetrieval.search | handle.root | Attribute for handle.root in GuiToolRetrieval.search; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 91 |
