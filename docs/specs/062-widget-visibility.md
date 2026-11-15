# V7-062: widget visibility outside Edit

Approved scope: in a generated application's Edit mode, every editable canvas
control exposes a small checkbox. Checked keeps that control visible after
leaving Edit; unchecked hides it. Persisted visibility must reuse the existing
layout record, the shared control allowlist and the existing authorized route.
Toolbar controls, approval hashes, generated widget source, existing applications,
other versions, `generated_tools` and live processes stay unchanged.

## Requirement

Applications composed from several widgets accumulate intermediate inputs and
outputs that are only useful while configuring or debugging. The owner needs to
choose, per control, whether it remains part of the delivered GUI, without
editing generated code and without losing the control's callback bindings.

Observable acceptance:

- Entering Edit shows one checkbox per editable control and no checkbox elsewhere.
- Unchecking a control and leaving Edit hides it; checking it keeps it visible.
- Leaving Edit saves geometry and visibility together; a failed save keeps Edit
  active and reports the failure instead of silently discarding the choice.
- Reloading or reopening the application restores the saved visibility.
- Hidden controls keep their values and callbacks: hiding is presentation only.
- Unknown, duplicated or toolbar identifiers and invalid geometry are rejected.

## Contract

`src/agentix/layout_contracts.py` keeps `version: 1` and adds the optional
`hidden` list (at most 64 entries, no duplicates). It is validated against the
same `allowed` set as `positions`, so `application_edit`, `application_execute`,
`application_stop` and foreign identifiers remain rejected. `hidden` defaults to
`None` and normalization excludes it when absent, so existing `config.json`
records and their comparisons stay byte-compatible. The legacy schema-2 fallback
reuses one shared predicate for both fields instead of duplicating the pattern.

`src/agentix/ui/assets/application_editor.js` keeps the loaded `hidden` set,
renders one `input[type=checkbox].application-visibility-toggle` per control
inside the canvas, and positions it over the control's top-right corner. The
toggle stops click and pointer propagation so it never invokes a Gradio callback.
Entering Edit makes every control visible before geometry is captured, so a
hidden control cannot collapse to the minimum rectangle. Leaving Edit posts
`{version, positions, hidden}` to the existing `/_agentix/layout` route.

`src/agentix/ui/assets/style.css` hides the toggles outside Edit and applies
`display: none` to hidden controls. Positioning stays inline because an
`!important` offset would override the computed rectangle.

`src/agentix/application/app_controls.py` and
`src/agentix/storage/installed_apps.py` needed no route or storage change: the
same authorized request now carries the extra validated field.

## Acceptance and regression

- `tests/test_code_application.py::test_v7_062_layout_hidden_visibility_contract`
  covers accepted visibility, the unchanged legacy payload and rejected toolbar,
  duplicate and unknown identifiers.
- `tests/test_application_controls.py::test_layout_hidden_controls_roundtrip_and_reject_toolbar`
  covers the authorized route, persistence roundtrip and rejection of toolbar
  identifiers without mutating the stored record.
- `tests/test_code_application.py::test_v7_062_editor_hides_unchecked_controls_after_edit`
  drives the real editor script with inert DOM controls and an intercepted
  loopback route: uncheck, leave Edit, hidden, reload, still hidden, and visible
  again inside Edit with the checkbox unchecked.
- `tests/test_v5_native_editor_browser.py` now also asserts that every real
  Gradio control exposes its visibility checkbox in Edit.

The first browser attempt failed for two implementation reasons that the
regression exposed: an `!important` CSS offset overrode the computed position,
and the fixture needed the maintained stylesheet to position absolute toggles.
Both were corrected in the implementation, not by relaxing assertions.

## Verification

- Focused offline: `tests/test_code_application.py`,
  `tests/test_application_controls.py`, `tests/test_installed_apps.py`,
  `tests/test_application_update.py` and `tests/test_application_review_browser.py`
  collected 60 passed, 14 deselected.
- Browser: the new editor regression, the existing V6-044 editor regression and
  the native editor test collected 3 passed with the installed Microsoft Edge
  executable; the native test was rerun with `browser and windows_isolation`
  and passed, exercising real Gradio composition inside AppContainer.
- Ruff lint and format checks passed for the changed Python files.
- Reference generation and the exact freshness check passed after regeneration.
- Full offline suite: 1020 passed, 84 deselected, 1 failed
  (`tests/unit/test_reference_freshness.py`, caused by regenerating references
  before the last test edit). References were regenerated and that test then
  passed 3/3; the freshness check reports no issues.

No change was deployed to the running GUI and no live process was restarted.
`layout_contracts.py` and `ui/assets/application_editor.js` participate in
`app_policy()`, so the policy digest moved to
`fb943707bfc10e53af64041b530d778eeba9d26d7ef22b819b7f9219f25ee447` and
installed applications require re-approval under the new boundary. This record
is manually authored from raw test evidence; no model drafted prose.
