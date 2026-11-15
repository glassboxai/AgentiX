# Independent tool retrieval

Install the optional pinned dependency from requirements-retrieval.txt in the
managed environment only when absent. No agent/controller integration is enabled.

```python
from agentix.retrieval import (
    OllamaClient, OllamaEmbeddings, OllamaKeywords, ToolRetriever,
)

client = OllamaClient()
retriever = ToolRetriever(
    "./data/tool_registry",
    embeddings=OllamaEmbeddings(client),
    keyword_generator=OllamaKeywords(client),
)
# Register explicit ToolDescriptor instances using retriever.upsert(descriptor).
results = retriever.search("Count the words in a text", limit=5)
for result in results:
    print(result.descriptor.name, result.rank, result.score, result.mode)
```

Unbound instances require explicitly registered descriptors. For automatic catalog
synchronization, bind the source shown below. Treat returned
artifact references as opaque data. A later adapter must resolve them through
the current approved catalog; never import a candidate's entrypoint on the host.

Architecture: service coordinates storage/providers, contracts owns typed data and
AST extraction, lexical owns tokenization/BM25, ollama owns local HTTP boundaries.
All external providers are injected. See [RAG-001 specification](specs/051-tool-retrieval.md)
for limits, concurrency, privacy, ranking and evaluation commands.

Numeric policies and units are named typed constants in src/agentix/retrieval/policy.py. Shared keyword bounds drive both validation and the model request. BM25 derives its normalization factors from its named parameters. See RAG-008 in the specification; this is an internal maintenance boundary, not a runtime configuration API.

## Load the same installed catalog as the GUI

```python
from agentix.retrieval import CatalogToolSource

# runtime.catalog is the current GUI runtime's ToolCatalog.
retriever = ToolRetriever(
    index_path,
    embeddings=OllamaEmbeddings(client),
    keyword_generator=OllamaKeywords(client),
    descriptor_source=CatalogToolSource(runtime.catalog),
)
print(retriever.last_sync_report)
results = retriever.search("Count the words in a text")
```

Binding loads immediately. Each search rescans the source and reconciles additions,
changes and removals before ranking. Unchanged tools keep their embeddings. Use
retriever.synchronize() to refresh explicitly. An unavailable source fails the search;
old results are not served. Changes after the scan appear on the next search. There
is no background watcher or automatic connection to the existing GUI process.

For a standalone initial load/refresh, use the managed interpreter:

```text
python tools/sync_tool_registry.py --tools-root <actual-GUI-tools-root> --index <dedicated-index>
```

Omit --tools-root only when the shell has the same AGENTIX_HOME/AGENTIX_TOOLS_ROOT
configuration as the GUI launcher. Source-bound indexes require the same source
when reopened. Do not reuse a manually populated collection for authoritative sync.
The JSON summary reports additions, updates, removals, unchanged tools and rejections.

## Applications GUI integration
On the next normal application launch, the GUI initializes the catalog-backed index. Generate application searches the entered description first. Review the list below Delete selected application, adjust Candidate limit with its arrows and click Accept candidates and generate. Editing the description leaves the preview unchanged; acceptance requires the searched description. Current tool approval and source checks still apply; this candidate button does not approve application execution. The existing live process is not reloaded by this source change. See specs/052-application-tool-candidates.md.

### Candidate selection (RAG-011)

Typing leaves the preview unchanged; Generate application or a limit change runs search. Uncheck tools to exclude them. Each new search checks all results. Acceptance displays the selected count and requires a nonempty eligible subset matching the searched description. See specs/053-candidate-checkboxes.md.
