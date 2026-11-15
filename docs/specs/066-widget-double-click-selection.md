# V7-066: double-click a widget to open its reviewed source

Approved scope: in a Generated Application, a double-click on a widget control
selects `<tool_name>_widget.py` in `Application files and proposed tests` and
shows the three existing columns (`Tool Implementation`, `Tool Widget`,
`Tool tests + Widget tests`) with that widget's code. Nothing else changes:
no new route, no new approval, no generated source, no live process.

## Requirement

While reviewing a composed application the owner recognizes a widget on screen
but must find its file by hand in the dropdown. The double-click must resolve
that widget to its tool's reviewed widget source and reuse the grouped review
that already exists.

Observable acceptance:

- Double-clicking a widget control selects `<tool>_widget.py` in the file
  dropdown and fills the three columns with that tool's implementation, widget,
  tool tests and widget tests.
- The review accordion opens so the columns are visible.
- Status and public input controls report nothing; only widget controls of a
  tool do.
- A name that is not a canonical tool identifier is rejected before any file
  lookup, and a message from any window other than the framed application is
  ignored.

## Contract

`src/agentix/ui/assets/application_editor.js` adds one `dblclick` listener on
the canvas. It resolves the owning control through the already loaded `nodes`
allowlist and the existing `groups` mapping from `GET /_agentix/layout`, skips
`application_status` and `application_input_*`, and posts
`{type: 'agentix-widget-selection', tool}` to the parent page. Geometry,
visibility, colors and callbacks are untouched.

`src/agentix/ui/assets/widget_selection.js` is a new maintained parent-page
script. It keeps the current `#applications-frame iframe`, ignores any message
whose `source` is not that frame's `contentWindow`, accepts only
`^[a-z][a-z0-9_]{0,63}$`, writes the name into the CSS-hidden
`#applications-widget-selection` textbox and clicks the CSS-hidden
`#applications-widget-select` button, the same value-at-click pattern already
used by `chathelper.js`.

`src/agentix/ui/branding.py` registers the new script in `launch_options()`.

`src/agentix/ui/applications.py` adds `widget_source_name(tool)`, which accepts
only a canonical tool identifier and returns `<tool>_widget.py`, plus the hidden
textbox/button pair and `select_widget_file`, which sets the dropdown, opens the
review accordion and reuses `select_file` for the three columns. No backend,
storage or contract change was needed.

## Acceptance and regression

- `tests/test_code_application.py::test_v7_066_widget_source_name_accepts_only_a_tool_identifier`
  covers the accepted name and rejected empty, spaced, traversal, uppercase,
  hyphenated, oversized and non-string values.
- `tests/test_code_application.py::test_v7_066_editor_posts_the_double_clicked_widget_tool`
  drives the real editor script with inert DOM controls: the widget posts its
  tool, Status and a public input post nothing.
- `tests/test_code_application.py::test_v7_066_parent_selects_the_widget_file_from_a_frame_message`
  drives the real parent script with a real iframe: the framed tool name reaches
  the hidden selector, an invalid name and a top-window message do not.
- `tests/test_v5_review_browser.py` now also clicks the hidden selector in the
  real Gradio page and asserts the dropdown shows `count_words_in_text_widget.py`
  and the widget column shows `create_widget`.
- `tests/unit/test_presentation.py` asserts the new script is part of
  `launch_options()`.

## Verification

Executed on 2026-11-12 with the managed v5 interpreter
(`D:/AI/Agentix-data/v7/environments/7d6df7e204a38b63/Scripts/python.exe`):

- Red first: the new offline test and the `launch_options()` assertion failed
  before the implementation.
- Focused offline set (`test_code_application`, `test_presentation`,
  `test_reference_freshness`, `test_application_review`,
  `test_applications_backend`, `test_ui_stylesheet`): 63 passed, 12 deselected.
- Browser with the installed Microsoft Edge executable: the two new script
  regressions passed (4 passed together with the offline pair), and
  `tests/test_v5_review_browser.py` passed against a disposable real Gradio
  server, including the new dropdown and widget-column assertions.
- Ruff lint and format: clean on the five changed Python files.
- `tools/build_reference.py` then `--check`: no issues.

`ui/assets/application_editor.js` participates in `app_policy()`, so the policy
digest moved to
`b6729019a6bd53dc713bfebda243c6d2ab059c34e5ccfc50b9ca9b1a1cd21f6f` and installed
applications require re-approval under the new boundary. `widget_selection.js`
is a parent-page asset and is not part of that digest. No live process was
restarted and nothing was deployed to the running GUI.
