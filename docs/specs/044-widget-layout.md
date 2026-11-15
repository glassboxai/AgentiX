# V6-044 widget layout correction


## V6-044: connection-code widget layout

Approved scope: repair schema-3 layout discovery without changing generated widget
source, executable approvals, live processes or generated_tools. In Edit, visible
widget inputs/outputs must receive the same move/resize handles as Status; saving
and reading geometry must retain numeric bounds and reject toolbar/foreign IDs.

Cause: application_layout_ids returned None for schema 3. The browser therefore
used its legacy words/vowels allowlist, which includes Status but omits arbitrary
widget identities. Storage used the same legacy fallback and rejected their IDs.
The shared contract now derives schema-3 IDs from widgets and the maintained
ElementIds registry, including the supported input alias. Schema-2 selection is
preserved. Existing editor pointer/keyboard events need no changes.

Regression: test_v6_044_code_widgets_have_editable_persistable_geometry failed
because the allowed set was None; after correction, the focused code-application
and controls suite passed (14 passed, 7 deselected). The regression independently
expects both widget instances, numeric geometry and forbidden toolbar/foreign IDs.
No model, generated artifact or live application was executed for this correction.
The current live process has not been restarted; deployment to it is unverified.


Final validation (2026-10-30): offline run completed with 827 passed and one
reference-freshness failure caused by adding the browser test during that run.
The reference is regenerated and the freshness regression rerun separately.
Chromium editor check: 1 passed, 14 deselected. This uses inert HTML, the real
maintained editor script and a Playwright-intercepted layout endpoint; it verifies
keyboard movement/resizing and persistence reload, not real Gradio rendering,
physical disk persistence or the live Simply app. The initial browser fixture
omitted the relative canvas positioning and blocked the toolbar; correcting that
fixture to match the canvas positioning resolved the harness failure. Production
JavaScript was unchanged. Ruff lint/format and reference freshness are checked.
This record is manually authored from raw test output; routine fix documentation
requires no Ollama inference. No live restart or model acceptance is claimed.
