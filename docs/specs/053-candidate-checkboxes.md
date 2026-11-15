# RAG-011: stable previews and explicit tool subsets

Status: implemented; user approved both blocks on 2026-11-03. Supersedes the description-change invalidation and read-only list presentation in specification 052.

| Requirement | Observable acceptance |
| --- | --- |
| RAG-011-01 | Typing or replacing the description does not clear or search the candidate list. Only Generate application and limit changes search. |
| RAG-011-02 | Acceptance rejects a description different from the server snapshot, without generation. |
| RAG-011-03 | Every result has a checkbox, initially checked; every new search resets all checks. |
| RAG-011-04 | Acceptance passes only checked snapshot IDs with server-owned source hashes. Empty, duplicate, foreign and ineligible IDs are rejected. |
| RAG-011-05 | Acceptance shows the selected count and is disabled for an empty or ineligible subset. An unchecked ineligible candidate does not block an eligible subset. |
| RAG-011-06 | Owner, revision, source, approval and replay checks remain mandatory. Acceptance logs count and selected tool IDs without descriptions or code. |

## Contracts and responsibilities

The frontend uses Gradio CheckboxGroup plain-text labels containing bounded name, description, score and eligibility. Values are tool IDs from the search snapshot. Description edits have no callback to this panel. The existing control timer checks availability only and performs no inference. Checkbox changes refresh controls, not search results.

CandidateSelection.selected_expected validates a nonempty unique subset and independent snapshot eligible_ids. The server preserves retrieval order and resolves fingerprints itself. ApplicationsBackend.accept_candidates accepts keyword-only selected_ids; omission preserves trusted legacy callers selecting the entire snapshot. The GUI always supplies explicit IDs. Current source and approval are rechecked immediately before generation. Editing the description back to the exact searched value allows acceptance if the snapshot otherwise remains valid.

No Tools dialog or approval callbacks are changed. No live process is restarted. Browser tests use a separate disposable server with retrieval and generation doubles; they do not establish real model quality.
