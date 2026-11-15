# V7-067: separate web tab, Edit affordances, colour legend and code-help identity

Approved scope: in a Generated Application, a `View as web` link beside the cyan
heading opens the same already validated loopback page in a new browser tab; Edit
mode keeps the widget name clear of its move handle, restores the default surface
of the outer box, shows a bordered visibility checkbox and adds a vertical colour
legend; the isolated page titles itself with the owner's application name; and
Code Help names the file it is answering about. Nothing else changes: no new
route, no new capability, no generated source, no live process.

## Requirement

Observable acceptance:

- The heading row shows `View as web` next to `Generated Application`; activating
  it opens the same supervisor origin in a new tab with `noopener noreferrer`.
- In Edit mode the widget label starts after the move handle, the outer box uses
  the default block surface, and the visibility checkbox shows a visible border and
  a filled, checked state. Outside Edit mode the surface is transparent and the
  checkbox is hidden again.
- In Edit mode a small `Tools` box pinned to the left, below the layout notice,
  lists one swatch per tool/widget colour, matching the colour of that widget's
  move handle, and disappears when Edit ends.
- The isolated page heading shows the application name the owner gave, and the
  maintained default when no name was staged.
- Code Help shows, under its title, the file the question is about, and follows a
  later change of the selected file.

## Defect V7-067-D1

HELP-01 (`specs/037-v5-structure-and-workspace.md`) requires the context chat to
receive the filename, and `V7_ARCHITECTURE.md` states that Code Help receives it.
The controller did receive it, but the floating window never displayed it:
`chathelper.js` stored `component.id` (`applications-tool-code`) in
`popup.dataset.filename`, so the owner could not see which file the answer
concerned. Cause: the pane identity was confused with the file identity. Solution:
derive the file from the selected dropdown value and the pane suffix, and render
it in `#chathelper-file`. Regression:
`tests/test_v7_067_application_web_and_edit.py::test_v7_067_code_help_names_the_selected_file`.

## Defect V7-067-D2

The visibility checkbox toggled its own `checked` property but showed no visible
change, so the owner reported that it could not be activated or deactivated. Cause:
the Edit rule forced `background-color: #050608`, while the maintained checkmark is
a near-black `#061016` stroke drawn for an accent fill; checked and unchecked looked
identical. A second cause kept the fix from applying: Gradio rewrites custom CSS
with a `.gradio-container.gradio-container-6-30-0 .contain` prefix, which raised the
base rule above a plain `:checked` selector. Solution: keep `display` on the
unprefixed rule and give the colour rules container-scoped selectors with enough
specificity, so checked is accent-filled with a visible dark checkmark and unchecked
is dark with an accent border. Regression:
`test_v7_067_editor_legend_surfaces_and_visible_checkbox` asserts both computed
backgrounds and the persisted hidden state after leaving Edit.

## Defect V7-067-D3

The colour legend stretched across the whole viewport and sat vertically centred.
Cause: Gradio's `div.svelte-siq5d6 > * { width: var(--size-full) }` applied to the
`aside`, so the fixed box measured the full 1400 px width. Solution: `width:
max-content`, `align-items: flex-start`, a bounded `max-width`, and the caption
renamed to `Tools`. V7-068-D5 later moved the box to `position: absolute` inside the
canvas at `top: 48px; right: 12px`, directly below the play/edit/close toolbar, so the
regression now asserts the caption, a width below 300 px, a right edge 12 px inside
the canvas and a top below the toolbar buttons.

## Contract

`src/agentix/ui/application_presentation.py` renders the heading row, the link and
the unchanged `iframe_html(url)` frame. The link reuses the URL already validated
by `iframe_html`; the name only labels the section and the link title.

`src/agentix/lab/application_session.py` accepts a bounded `display_name` and, when
present, stages `application_display.json` beside the reviewed snapshot.
`src/agentix/application/templates/code/app.py` reads that file in
`application_title()`, drops Markdown-active characters and falls back to
`Generated Application`. No query parameter, no `js` dependency and no `eval` are
used, because the bridge Content Security Policy forbids `unsafe-eval` and a
`js`-only `load` dependency leaves the page on its loading state.

`src/agentix/lab/application_panel.py` forwards the name to the session, and
`app_workflow.py`/`general_acceptance.py` pass `candidate.display_name` through
`preview_factory`.

`src/agentix/ui/assets/application_editor.js` adds `paintLegend`, built from the
same `colorFor`/`groups` mapping as the move handles, and removes it when Edit
ends. `src/agentix/ui/assets/style.css` carries the label padding, the Edit-only
surface, the container-scoped checkbox colours, the compact `Tools` legend and the
link styles.

## Acceptance and regression

- `test_v7_067_frame_offers_a_separate_tab_and_labels_the_section` covers the link,
  the escaped name and the rejected non-loopback origin.
- `test_v7_067_isolated_page_titles_itself_from_the_staged_name` starts the real
  isolated worker twice and reads `/config`: the named run renders
  `## Vowel counter`, the unnamed run renders `## Generated Application`, and no
  dependency carries `js`.
- `test_v7_067_editor_legend_surfaces_and_visible_checkbox` drives the real editor
  script and stylesheet in Chromium: transparent surface outside Edit,
  `rgb(11, 13, 17)` inside, 28 px label padding, a 2 px checkbox border with an
  accent fill when checked and a dark fill when unchecked, one legend row per tool
  colour matching the handle, a `Tools` caption in a box narrower than 300 px, the
  legend removed on exit, and the unchecked control hidden outside Edit and visible
  again on re-entry.
- `test_v7_067_code_help_names_the_selected_file` drives the real helper script and
  follows a later file selection.
- `test_widget_panel.py::test_iframe_never_accepts_a_display_name_parameter` keeps
  the frame free of a name parameter.
- `test_ui_stylesheet.py` keeps the Edit surface, the checkbox border, the legend
  and the two new identifiers in the maintained stylesheet.

## Policy impact

`templates/code/app.py` participates in `app_policy()`, so its digest moves and an
application installed before this change requires re-approval; until then it keeps
showing the maintained default heading. `application_display.json` is staged
outside the reviewed snapshot and never alters the approved digest.
