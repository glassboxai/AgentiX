# RAG-011 delivery evidence

The user approved stable description editing followed by candidate checkboxes. Requirement and acceptance contracts are in [specification 053](../specs/053-candidate-checkboxes.md).

## Implemented behavior

Description edits leave the preview unchanged and do not call retrieval. Generate application and limit changes search; new results reset all checkboxes to checked. Labels show name, bounded description, score and eligibility in the dark theme. Acceptance displays the selected count and disables an empty or ineligible subset. Only checked server-snapshot IDs and server-owned source hashes reach generation. An eligible subset may exclude an ineligible result. Changed descriptions, owners, revisions, source bytes, approval and replay remain checked at acceptance/use. Selection counts and accepted IDs are logged without descriptions or source bodies.

## Evidence

Final frozen-source offline suite: **980 passed, 91 deselected, 59 warnings in 83.91 seconds**. Raw evidence: RAG_011_OFFLINE_FINAL.txt.

- Four new subset regressions failed before implementation because the API did not accept selected_ids; they pass after implementation.
- Candidate/backend targeted checks: 38 passed, 1 framework test deselected.
- Actual Gradio/CrewAI in-memory checks: 3 passed, 36 deselected. No inference or live server.
- Candidate and related review browser checks: 5 passed, 2 deselected. A final candidate-only rerun after dark-theme styling: 1 passed. These use disposable loopback servers and explicit retrieval/generation doubles.
- Ruff lint and format: all checks passed, 355 files formatted. Generated source references report no issues.
- Initial complete-suite evidence is retained in RAG_011_OFFLINE.txt. Its failures were a Gradio double missing CheckboxGroup and a browser reference changed during verification. The double inventory was updated without weakening existing assertions, references rebuilt, and source frozen before the final rerun in RAG_011_OFFLINE_FINAL.txt.
- RAG_011_BROWSER.json contains only candidate limits and generation dependency IDs. RAG_011_CANDIDATE_PANEL.png records the inspected final panel. RAG_011_SOURCE_HASHES.json records maintained source hashes and unchanged Tools source hashes.

The declined Tools dialog/callback changes were not applied. No live application was restarted and no real-model generation or native-isolation evaluation is claimed. The changes load at the next normal application launch. This routine engineering note was authored and checked against local test evidence without model inference.
