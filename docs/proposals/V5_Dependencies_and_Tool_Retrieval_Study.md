# Dependencies and tool retrieval: proposed next increments

Status: research and recommendations, not implemented. Reviewed 29 October 2026.
No packages, embedding models, database credentials or network capabilities were
added by this study.

## 1. What happens today

The managed host environment already contains NumPy and pandas through its pinned
runtime lock. This does not mean every generated tool may import them. The normal
tool runner stages a restricted standard-library runtime. The experimental widget
worker stages the pinned UI runtime, but its approved imports/contracts remain
restricted. An unavailable import must fail rather than execute on the host.

The current Applications pilot supports reviewed word/vowel tools. It does not
yet assemble arbitrary pandas, database, plotting or LLM-backed applications.

## 2. Recommended dependency workflow

1. The designer declares required packages and their purpose as proposal data.
2. A maintained dependency service checks package names, compatible Windows
   wheels, Python 3.11.9 compatibility and the allowed package/source policy.
3. The user reviews a concrete provisioning plan. Resolve direct and transitive
   dependencies to exact versions and hashes before installation.
4. The host provisioner builds a separate immutable runtime identified by its
   dependency lock. Generated code cannot run pip, alter PATH or choose an index.
5. Run import checks and independent native tests against that exact runtime.
6. Bind the tool/widget/application approval to the dependency lock as well as
   its code/contracts. Reusing the same lock should reuse the prepared runtime.

pip documents hash checking together with binary-only distributions as controls
for repeatable package installation. These checks do not establish that a package
is harmless: package approval and independent execution checks remain necessary.
[Source: pip secure installs](https://pip.pypa.io/en/stable/topics/secure-installs/)

Do not install each requested library into AgentiX's own running environment.
That could break existing applications and expand every worker's import surface.
If two tools need conflicting package versions, resolve a compatible application
lock or execute them in separate native boundaries exchanging typed data. Do not
silently upgrade another tool's runtime.

## 3. Suggested order for new capabilities

| Capability | First supported form | Important boundary |
| --- | --- | --- |
| pandas | Bounded tables returned as typed columns/rows | Row/column/size limits; no Python objects over IPC |
| Matplotlib / seaborn | Worker-created plot delivered through a Gradio plot/image component | Headless rendering; bounded images; no arbitrary host file paths |
| scikit-learn | Small bounded inference/training task in an approved runtime | CPU/RAM/time limits; reject untrusted pickle models |
| SQLite | A database inside an explicitly approved workspace | Parameterized queries, transaction rules and declared write permission |
| Remote database | Narrow maintained database gateway | Least-privilege credentials stay on the host; explicit destination/operation scope |
| Tool using an LLM | Injected maintained model gateway | No keys in generated code; limits and consent for external content transmission |
| Streamlit | A separately reviewed application renderer, if needed | A separate server/lifecycle/transport integration, not a Gradio widget import |

Gradio already provides data and plot-oriented components. My recommendation is
to prove one table and one chart using Gradio before adding another UI framework.
[Source: Gradio components](https://www.gradio.app/docs)

Streamlit starts its own server through streamlit run. Therefore, adding its
package would not by itself connect it to create_widget(context) or to the existing
Gradio IPC bridge. Supporting it needs a separate feasibility/security increment.
[Source: Streamlit execution model](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

Local Ollama calls from generated tools also need a narrow host gateway: the
AppContainer's network restrictions should remain in force. Remote model calls
add explicit data-transfer consent and potentially billable-operation approval.
No tool should receive a general HTTP proxy or a credential value.

## 4. Why tool retrieval is useful

Currently, the tool manager receives a rendered catalog. The installed-application
selector also limits its metadata list to 32 entries. Neither approach scales
reliably to a large catalog: a useful entry can be absent or buried in irrelevant
context. These are findings from the maintained implementation, not a claim that
CrewAI itself guarantees a particular tool-selection limit.

A retrieval stage would search the complete approved catalog, then give the local
LLM a small relevant shortlist. The LLM still interprets the task and selects an
operation. The host still checks current approvals and executes in native isolation.

```text
User request
  -> search approved tool/application metadata
  -> bounded relevant shortlist
  -> qwen3-coder:30b selects an explicit operation
  -> host checks identity, contract, permissions and current bytes
  -> native execution
  -> observed result
```

CrewAI documents custom BaseTool adapters with typed argument schemas. A maintained
catalog-search adapter can use that interface without importing generated Python
on the host. I would first inject retrieval before the existing strict selectors;
a dynamically callable search tool can follow if the pilot demonstrates a need.
[Source: CrewAI custom tools](https://docs.crewai.com/en/learn/create-custom-tools)

The documentation currently redirects to CrewAI 1.15.33; this checkout pins
1.15.28. No claim of drop-in compatibility follows from reading newer documentation.
The integration must be tested against the pinned installed release.

## 5. langchain_core and an in-memory index

InMemoryVectorStore is a plausible small-catalog starting point. Its documented
implementation stores vectors in a dictionary and uses NumPy cosine similarity.
It offers search/filter/delete operations without requiring a separate database
server. It still needs a real embedding provider.
[Source: LangChain InMemoryVectorStore](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore)

Index names, reviewed descriptions, input/output contracts, capability labels
and a few reviewed usage examples. Do not embed API keys, user data or full source
files. Include tools and reusable applications, but separate draft/rejected matches
from executable candidates so a pending tool is not needlessly recreated.

The index is a search aid, never the authority for approval or deletion dependency
checks. Re-check every shortlisted item against the authoritative catalog before
execution. Add/update/remove entries when approvals, source or catalog membership
change. Treat retrieved descriptions as untrusted data, not agent instructions.

An embedding model is distinct from the model that writes code and makes decisions.
qwen3-coder:30b remains the generation/selection model. A new embedding model needs
your explicit approval; no assumption is made that the coder model supports the
embedding endpoint. A small CPU-capable local provider would reduce GPU contention.
Ollama documents a dedicated embeddings API and recommends using the same model
for catalog indexing and queries.
[Source: Ollama embeddings](https://docs.ollama.com/capabilities/embeddings)

Do not load embedding weights or recompute the whole index whenever the website
opens. Build incrementally, cache bounded vectors with a model/catalog identity
and keep the searchable store in memory. Rebuild safely on stale cache; never
load an untrusted pickle. A lexical fallback should work while the index prepares.

## 6. Pilot and acceptance before broad rollout

- Compare lexical search, semantic search and a simple combined ranking.
- Use independently labeled requests over catalogs of 10, 100, 500 and 1,000 tools.
- Measure whether the correct tool appears in the shortlist, wrong-tool selection,
  unnecessary tool creation, latency, RAM and embedding/model startup cost.
- Include similar names, different capabilities, deleted/revoked tools, stale
  indexes, no-match requests and multi-step requests.
- Use synthetic vectors only for wiring tests; they do not prove semantic quality.
- Run the end-to-end pilot with the approved real local embedding provider and
  qwen3-coder:30b, with human-reviewed expected selections and observed executions.

My suggested sequence is: finish deletion/repair, prove one dependency-locked table
and plot family, then evaluate retrieval with a growing fixture catalog. Retrieval
is useful but does not itself implement general workflow planning or prove that
a selected tool is functionally correct.
