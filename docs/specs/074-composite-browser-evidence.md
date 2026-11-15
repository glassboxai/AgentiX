# V7-074: browser evidence for the composite accordion and its cancellation fixture

Approved scope: the cancellation browser test slows an application-owned tool instead
of a maintained runtime member, and one new browser regression renders the composite
accordion. Nothing else changes: no production module, no generated source, no tool
or widget bytes, no AppContainer boundary and no live process.

## Defect

`V7-074-D1` — trigger: `tests/test_application_controls_browser.py` failed with
`RuntimeSourceChanged: Maintained compositor source was modified` before Chromium
started.

Cause: the fixture appended a slow `analyze_text` to `operation.py`, which is a
maintained `SHARED` member, and then called `application_digest` and
`approve_application` with strict capture. `_capture` compares every `SHARED` member
with `runtime_template(name)` and rejects the difference
(`src/agentix/application/general_package.py:99`). `allow_runtime_drift=True` is not a
correction: `capture_with_current_runtime` replaces the member with the template and
would delete the delay the test needs.

Solution: the fixture now inserts `time.sleep(5)` inside the application-owned
`count_words_in_text_code.py`, whose `Annotated` signature and extracted schema are
unchanged, and recomputes the manifest hashes as before. Strict capture therefore
still proves the reviewed bytes, and the toolbar cancellation path keeps its slow
operation.

`V7-074-D2` — trigger: after the capture correction the same test timed out waiting
for `#application_input textarea`.

Cause: both `tests/test_application_controls_browser.py` and the shared
`check_analysis` helper in `tests/test_composite_browser.py` still addressed the
legacy schema-2 control `application_input`. Schema-3 applications render one public
input per declared name as `application_input_<name>`
(`src/agentix/application/templates/code/app.py:41`,
`src/agentix/layout_contracts.py:125`), so the locator never resolved.

Solution: both modules address `#application_input_text textarea`, the identifier the
fixture manifest declares. No production selector changes.

`V7-074-D3` — trigger: the new accordion regression read the default placeholder
instead of the contract.

Cause: the contract is refreshed by `Show input schema` or by a run, not on expand, so
the assertion had to drive the maintained control first; the Markdown table also
renders as cells, not as raw pipe text.

Solution: the test clicks `#applications-data-schema` and asserts the rendered cells
(`text`, `string`, `Text to analyze`) plus the `Example payload` line.

`V7-074-D4` — trigger: the accordion regression read
`Session expired or owner does not match` in `#applications-status` instead of the
JSON diagnostic.

Cause: the backend double returned the literal `"owned"` as the session token, so the
callback replaced the real `gr.State` token with a value no session owns; the next
activity tick and poll rejected it. The real backend always returns
`session.token`.

Solution: both doubles echo the incoming token, and the test asserts that
`Session expired` never appears.

`V7-074-D5` — trigger: the run callback failed with
`ComponentProcessingError: Could not postprocess output component at index 5`.

Cause: the test bound the Playwright locator to the name `contract`, shadowing the
Markdown string the backend double returns, so a `Locator` reached the `markdown`
output.

Solution: the locator is named `contract_view`; the double keeps returning text.

## Requirement

Observable acceptance:

- The cancellation test reaches `ApplicationPreview`, stops a running operation,
  resumes it and closes its job without a capture rejection.
- `tests/test_composite_data_browser.py` opens the real Applications tab in Chromium,
  expands `Use the application as a composite tool`, activates `Show input schema`
  and reads the rendered contract cells and the `Example payload` line.
- Running a rejected payload hides the named-result table and the generic result,
  keeps the contract visible and shows `JSONDecodeError` in `#applications-status`
  while the real session token stays valid.

## Contract

`tests/test_application_controls_browser.py` patches only
`count_words_in_text_code.py`; `operation.py`, `app.py`, `application_context.py`,
`application_values.py` and `element_ids.py` stay byte-identical to their templates.
Both browser modules address the schema-3 public input `#application_input_text`,
never the legacy `#application_input` control.

`tests/test_composite_data_browser.py` builds the maintained view through
`build_view(sessions, applications_backend=backend)` with an explicit backend double
for `data` and `data_contract`, launches it on an ephemeral loopback port with
`prevent_thread_lock=True` and closes it in `finally`. The double is stated in the
module docstring: this check proves rendering, not native isolation or supervisor
behaviour, which the offline and Windows-isolation suites cover.

## Acceptance and regression

- `test_native_toolbar_stops_and_restarts_same_reviewed_snapshot` (markers `browser`
  and `windows_isolation`) keeps cancellation, restart and owned-job cleanup.
- `test_composite_accordion_renders_contract_table_and_rejection` (marker `browser`)
  keeps the visible contract, the hidden stale table and the bounded diagnostic.
- `check_analysis` in `tests/test_composite_browser.py` keeps the schema-3 input
  identifier for every caller that drives the framed application.

## Policy impact

Only test modules change, so no installed approval, tool grant, widget record,
declarative case or policy digest moves. No dependency, model call or browser
requirement is added.
