# RAG-008: Named retrieval policies — 2026-11-03

Review identified duplicated limits and unnamed ranking/generation parameters in
the initial RAG implementation. The correction centralizes them in typed Final
constants with documented meanings and units in agentix.retrieval.policy.

Keyword validation, JSON schema and prompt share the same bounds. BM25 derives
its saturation multiplier and normalization complement from k1 and b. Byte limits,
character limits, candidate budgets, schema identity and diagnostic display bounds
remain separate policies. Existing numeric values, ranking and stored schema are
preserved. The keyword count error now renders the limit numerically.

## Verification

| Check | Observed result |
| --- | --- |
| Pre-refactor characterization and retrieval tests | 40 passed; exit 0 |
| Post-refactor characterization and retrieval tests | 40 passed; exit 0 |
| Focused tests including reference freshness | 43 passed; exit 0 |
| Final full offline suite | 939 passed, 89 deselected, 41 warnings; exit 0; 78.46 seconds |
| Ruff check | All checks passed; exit 0 |
| Ruff format --check | 346 files already formatted; exit 0 |
| Reference freshness | No issues; exit 0 |

Five added characterization tests independently pin keyword/prompt/JSON bounds,
BM25 golden scores, UTF-8 query and default result limits, descriptor character
limits, and exact HTTP request/response byte boundaries. Expected values remain
literal in tests so changing a production constant cannot silently alter the
expected contract. This refactor was green before and after; no runtime defect
or artificial failing regression is claimed.

Manual review and an AST inventory found policy numbers centralized, with only
intrinsic zeros/ones, positions and rank origins remaining in business code.
References, architecture, specification, incident record and change log are
synchronized. Source fingerprints are in RAG_008_SOURCE_HASHES.json; the earlier
RAG_001_SOURCE_HASHES.json remains intact as historical evidence.

No real-model, framework, native-isolation or browser run was repeated for this
constant extraction. The previous model evaluation remains historical evidence.
No original tool data, live processes or agent wiring changed. Existing Chroma,
CrewAI and Gradio warnings remain visible. The report was authored directly from
reviewed local command outputs, without model-generated engineering code/tests.
