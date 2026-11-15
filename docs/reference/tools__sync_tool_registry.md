# Reference for tools/sync_tool_registry.py

Load/synchronize the GUI's installed tool root into a dedicated local RAG index.

Uses Settings and ToolCatalog rather than guessing a tools directory. Reads source
as bounded AST metadata only. Never imports tools, changes approval state, installs
models, starts a GUI or restarts services. Run again to refresh without searching;
bound ToolRetriever instances also synchronize automatically before every search.

Source fingerprint: 249953208e5ea322e83480859d56c562b06542dd46262eb559ffe22fe0879185

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### main

Synchronize configured tools and print counts/rejections as JSON.

Optional explicit roots support the exact deployment launcher configuration.
The index defaults to a sibling tool_registry directory beside the tools root.
Failures propagate; unavailable models never trigger downloads or fallback.

Kind: callable. Declared return: None. Source line: 30.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | argparse | Imported dependency for argparse in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Sequence | Imported dependency for Sequence in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | asdict | Imported dependency for asdict in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | CatalogToolSource | Imported dependency for CatalogToolSource in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | OllamaClient | Imported dependency for OllamaClient in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | OllamaEmbeddings | Imported dependency for OllamaEmbeddings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | OllamaKeywords | Imported dependency for OllamaKeywords in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | ToolRetriever | Imported dependency for ToolRetriever in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | Settings | Imported dependency for Settings in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| main | argv | Parameter for argv in main; use the enclosing contract and type below. | Sequence[str] &#124; None | Enclosing invocation or class/instance lifetime | 30 |
| main | parser | Local binding for parser in main; use the enclosing contract and type below. | Return type of ArgumentParser; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| main | args | Local binding for args in main; use the enclosing contract and type below. | Return type of parse_args; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| main | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| main | catalog | Local binding for catalog in main; use the enclosing contract and type below. | Return type of ToolCatalog; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| main | index | Local binding for index in main; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| main | client | Local binding for client in main; use the enclosing contract and type below. | Return type of OllamaClient; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| main | retriever | Local binding for retriever in main; use the enclosing contract and type below. | Return type of ToolRetriever; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
