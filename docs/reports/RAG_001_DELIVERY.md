# RAG-001 delivery verification — 2026-11-03

Implemented the independent agentix.retrieval package in AgentiX_v7. Agent,
controller and execution wiring is unchanged. No live application was restarted.
No original tool data or generated_tools content was modified or executed.

## Evidence

Interpreter: managed v5 environment 7d6df7e204a38b63, Python 3.11.9.
Installed dependencies: ChromaDB 1.5.9, pytest 9.1.1, Ruff 0.14.1.

| Check | Observed result |
| --- | --- |
| Final python -m pytest -q | 934 passed, 89 deselected, 39 warnings; exit 0; 84.16 seconds |
| Focused retrieval plus reference tests | 38 passed; exit 0 |
| Explicit -m ollama_retrieval evaluation | 1 test passed, four expected first-position matches; exit 0; 35.18 seconds |
| Ruff lint, maintained roots and active entrypoints | All checks passed; exit 0 |
| Ruff format verification | 344 files already formatted; exit 0 |
| tools/build_reference.py --check | No issues; exit 0 |

The default suite includes 35 retrieval-specific tests. Real Chroma persistence
is exercised with deterministic embedding/keyword providers. The separate local
model evaluation used qwen3:14b and nomic-embed-text:latest; all four searches
completed in hybrid mode. Search latencies were 17.026 seconds for calculation
(first model load), 2.665 seconds for vowels, 2.646 seconds for words and 3.276
seconds for random numbers. This small fixture set is not a general quality benchmark.

Copied implementations/specifications are static AST-only fixtures. Their original
bytes and provenance are verified against tests/fixtures/tool_retrieval/provenance.json.
The evidence establishes retrieval, not functional correctness or approval of those tools.

## Development regressions and limits

Initial collection failed because agentix.retrieval did not exist (feature red).
RAG-ERR-001 reproduced Chroma's rejection of legacy distance metadata during
modify; collection configuration resolves it. RAG-ERR-002 reproduced placeholder
stage durations; measured stage timers now pass the captured-log regression.
Two intermediate full runs detected stale references while development was in
progress. The final frozen-source run passes, including the freshness gate.

Chroma emits a legacy embedding-configuration deprecation warning. Remaining
warnings originate in CrewAI compatibility and Gradio callback tests. None is
suppressed or treated as proof of model, browser or isolation correctness.
Framework/native/browser markers were not run for this independent retrieval change.

Real-model evidence preceded the final logging timers, return annotations and
field comments; retrieval policy did not change afterwards. Evaluated and final
source fingerprints are recorded separately in RAG_001_SOURCE_HASHES.json;
historical package evidence is not replaced. The final offline suite validates
current sources. Manual reference review covered public contracts, model failure
behavior, AST extraction, privacy, ranking and concurrency restrictions.

This report was authored directly from reviewed command outputs. No remote
endpoint was used for report inputs and no model generated engineering code/tests.
Ollama inference was confined to retrieval keywords and embeddings.

See [specification](../specs/051-tool-retrieval.md) and [usage](../TOOL_RETRIEVAL.md).
