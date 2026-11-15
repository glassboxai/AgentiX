# V7-072: refresh control for the generated application

Approved scope: the Generated Application toolbar gains one `refresh` control to the
left of `play`, which reloads the same already validated loopback page so a layout
saved from another browser tab is read again. Nothing else changes: no new route, no
new callback, no generated source, no live process.

## Requirement

Observable acceptance:

- The isolated toolbar shows four compact controls in one row, ordered left to right
  as `refresh`, `play`, `edit`, `close`, each 32 px wide at the same top offset.
- The refresh control renders the `⟳` glyph and exposes the accessible name
  `Reload application`.
- Activating it reloads the document at the same supervisor origin, so the editor
  re-reads `/_agentix/layout` and repaints the persisted geometry and visibility.
- The control adds no Gradio callback, no queue entry, no API name and no host route;
  it is not a movable or hideable canvas control.

## Contract

`src/agentix/lab/widget_worker.py` registers
`gr.Button("Reload application", elem_id="application_refresh",
elem_classes=["application-refresh-button"], scale=0, min_width=32)` before the Edit
button and attaches no `.click` handler, so the child gains no callback surface.

`src/agentix/ui/assets/application_editor.js` binds a capture-phase click listener on
`#application_refresh` that calls `preventDefault`, `stopImmediatePropagation` and
`location.reload()`. The reload targets the page the owner already has open; the
editor therefore re-runs its existing `/_agentix/layout` probe with `cache:
'no-store'`. The listener is registered before the paused-page branch, so the
maintained stopped page keeps working unchanged and simply has no such control.

`src/agentix/ui/assets/style.css` adds `#application_refresh` to the shared absolute
toolbar rule, anchors it at `right: 126px` (12 px + three 38 px steps) and draws the
glyph through `::after`, matching the existing `play`, `edit` and `close` rules.

`src/agentix/layout_contracts.py` is unchanged: `application_refresh` is not part of
`application_layout_ids`, so a layout or hidden record that names it is still
rejected as an unknown movable control.

## Acceptance and regression

- `test_v7_072_worker_registers_a_refresh_toolbar_control` keeps the identifier, the
  class and the absence of a callback in the maintained worker.
- `test_v7_072_refresh_stays_outside_the_movable_layout_allowlist` keeps the toolbar
  identity out of persisted geometry and visibility.
- `test_v7_072_stylesheet_places_refresh_left_of_play` keeps the shared rule, the
  `right: 126px` anchor and the `⟳` glyph in the maintained sheet.
- `test_v7_072_refresh_reloads_the_page_and_sits_left_of_play` drives the real editor
  script and stylesheet in Chromium: the control is visible with its accessible name,
  its box starts left of `play`, the computed `::after` content is `⟳`, one document
  load precedes the click, and the click produces a second document load that clears
  a page-global marker and re-initializes the editor.

## Policy impact

`lab/widget_worker.py` and `ui/assets/application_editor.js` participate in
`app_policy()`, so the digest moves and an application installed before this change
requires re-approval; until then it keeps the previous three-control toolbar. No
approved tool, widget, declarative case or AppContainer boundary changes.
