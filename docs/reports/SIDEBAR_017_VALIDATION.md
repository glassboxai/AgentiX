# UI-MODEL-002 sidebar validation

Date: 2026-10-25. Approved scope: match NexisNodes/aXiom Glass Box secondary-button colors, hide local-unused credentials/consent, and verify all five action controls. Implementation is in AgentiX v3, not v2.

## Changes and reproduced failure

Secondary sidebar buttons now use translucent dark rgba(255,255,255,.035), light #f1f3f5 text and a subtle rgba(255,255,255,.10) border, with hover/focus states. Styling is scoped to the sidebar; primary/destructive semantics remain. Ollama hides API key and remote-transfer consent on initial render, provider selection and profile outputs. Switching providers clears key and consent. External providers show a password input and unchecked consent. Backend remote consent and owner validation are unchanged.

Two browser tests failed against the prior implementation because local-mode secret controls were visible: sidebar-017-red.txt. The approved corrections now pass. Existing characterization before changes also passed two old model/profile scenarios; that did not establish complete coverage of every button. In particular, Refresh saved profiles previously relied on automatic page loading rather than an explicit button click.

## Observable button verification

| Button | Browser action and verified consequence |
| --- | --- |
| Refresh models | Click reads a new deterministic catalog response; qwen3:14b becomes selectable only after that click. |
| Apply model | Select a model, apply it, then submit a query through the GUI. The resulting configured injected-client identity changes to ollama/qwen3:14b or openai/test-model. This is an observable runtime handoff, not LLM inference. |
| Save profile | Create a synthetic external profile, clear the key field, load it from another session, update its name with an empty key and save again. Independent service tests check persistence, stale revisions and failure preservation. |
| Refresh saved profiles | Open the second session before profile creation; after the first session saves, explicitly click refresh and select the newly discovered profile. |
| Delete selected profile | Click delete in the inactive second session, refresh choices, confirm the entry is absent and its temporary JSON metadata is removed. |

Additional assertions cover computed button colors, local hidden fields, external password masking, unchecked fresh consent, provider-switch clearing, hide/open controls, shared-session protection, actual approval editing/host comparison and desktop/mobile layout. Password masking was verified again after the final visibility updates.

## Results and evidence

- Complete offline regression suite: **412 passed**, 24 deselected, 15 existing CrewAI deprecation warnings. Raw: sidebar-017-offline.txt.
- Complete real Edge/Playwright browser suite: **8 passed**, 428 deselected, 46.76 seconds. Raw: sidebar-017-browser.txt; screenshots: sidebar-017-browser/.
- Real CrewAI/Gradio and Windows Credential Manager checks: **7 passed**, 429 deselected. The native credential test uses a unique synthetic target, verifies cross-process reading via a digest, and deletes that target. Raw: sidebar-017-framework-vault.txt.
- Additional password/conditional-control check: **1 passed**, seven deselected. Raw: sidebar-017-password-check.txt.
- Ruff and format verification passed; **89 files already formatted**. Source reference regeneration/freshness passed. Raw: sidebar-017-ruff.txt, sidebar-017-format.txt, sidebar-017-reference.txt.
- Separate real local Ollama discovery called /api/tags without inference: **13 installed models**, required qwen3-coder:30b present. Raw: sidebar-017-local-ollama.txt. No model was pulled or substituted.

Browser model/network/vault factories are deliberately doubled; Gradio, Edge, request routing, metadata persistence, review and callback behavior are real. The separate tags check verifies the actual local discovery service, and native credential checks verify the Windows vault. This does not authenticate a real paid provider, validate arbitrary model quality, or establish generated-code correctness. No native-isolation code changed; its existing evidence belongs to the prior security release rather than being claimed as newly rerun here.

## Report provenance and preservation

Local qwen3:14b drafted report prose using only the compact evidence JSON, never code or tests. SIDEBAR_017_DRAFT.md and its provenance are retained as an unverified draft. Review found one inaccurate wording: it said no actual inference/paid APIs were implemented, whereas the evidence only says they were not exercised by these engineering tests. This reviewed final report corrects that wording and adds the separately observed real Ollama tags result. The report-generation inference itself is prose drafting, distinct from application functional inference.

The live 7873 application was not restarted, and no existing generated tool or real API key was inspected, modified or executed. Tests own and stop only their disposable servers. The open application must be explicitly restarted by the operator to load modified Python/UI source; refreshing the browser alone does not load it.

English specification, architecture, operating manual, technical guide, authorization rules, change/incident records and source references were synchronized. Source hashes for this change are in sidebar-017-source-hashes.json; older evidence and hash manifests remain unchanged.
