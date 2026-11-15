# V7-068: collapsible, resizable right-hand sidebars for Tools and Applications

Approved scope: the Tools and Applications tabs each gain one right-hand
`gr.Sidebar` with the same style and behavior as the shared model sidebar on the
left. Both start collapsed, expand and collapse with the native toggle, and can be
resized by dragging their inner edge. The catalog, validation and human-review
controls that used to occupy a second column move inside them, so the conversation
and the application workspace use the full width. Nothing else changes: no new
callback, no controller or backend behavior, no dependency, no generated source and
no live process.

## Requirement

Observable acceptance:

- The Tools tab shows `#tools-sidebar` on the right, closed on first render, with
  `Installed Tools Catalog`, `View in explorer`, `Installed tool`,
  `Delete selected tool`, `Tool validation` and `Authorization & Test Review`
  inside it.
- The Applications tab shows `#applications-sidebar` on the right, closed on first
  render, with the whole installed-application catalog inside it: `View in
  explorer`, `Refresh apps`, the application selector and description,
  `Load`/`Play`/`Re-verify`, `Delete selected application` and the candidate panel.
- Both sidebars use the model sidebar's palette, secondary-button treatment,
  independent scrolling, accessible hiding of collapsed content and the same
  toggle affordance.
- Dragging the inner edge resizes the panel between 280 px and the smaller of
  720 px and 60 % of the viewport; the chosen width survives collapse/expand and a
  tab switch, and each tab keeps its own width.
- The work area is no longer split into two columns: `#agentix-workspace` and
  `#applications-workspace` hold one full-width column.

## Design

`src/agentix/ui/tools.py` keeps the conversation row and renders the catalog,
validation and review controls inside
`gr.Sidebar(position="right", open=False, width=420, elem_id="tools-sidebar")`.
`src/agentix/ui/applications.py` keeps the workspace row and renders
`build_apps_catalog` inside
`gr.Sidebar(position="right", open=False, width=380, elem_id="applications-sidebar")`.
Both sidebars are siblings of their tab's work row, so Gradio hides them with the
inactive tab and only one is ever visible.

Gradio 6.30 has no native resize and publishes one global `--overlap-amount` on
`documentElement`, which two mounted sidebars would overwrite. The maintained
`src/agentix/ui/assets/sidebar_resize.js` therefore owns the geometry per panel:
it appends a `role="separator"` handle on the inner edge, writes
`--agentix-sidebar-width` on the sidebar and, for the shared left panel only,
`--overlap-amount` on the single `.sidebar-parent`, and reasserts both after a
toggle. `style.css` declares the
width and the closed offset with `!important`, so Gradio's inline width cannot win
on re-render. Keyboard support uses the arrow keys (16 px steps) and `Home` to
restore the approved default; double-click does the same.

## Defect V7-068-D1

The Applications sidebar could not be resized from its upper edge. Cause: the drag
handle was a 10 px strip at `left: -5px`, so it overlapped the native toggle button
by 5 px; a pointerdown near the top hit the toggle and collapsed the panel instead
of resizing it. A second cause made a resize disappear after a callback: the handle
was injected once at load, so a Gradio re-render that replaced the sidebar subtree
left the panel without a handle at the stylesheet default width. Solution: move the
handle fully outside the toggle (`left`/`right: -12px`, 12 px wide) and re-scan on
DOM mutations, re-appending a missing handle and restoring the owner's stored width.
Regression:
`tests/e2e/test_browser_review.py::test_tab_sidebars_collapse_resize_and_keep_independent_widths`
asserts zero handle/toggle overlap, a real Applications drag, and handle plus width
restored after the injected node is removed.

## Defect V7-068-D2

Both tab sidebars rendered as Gradio's default `position: fixed` overlay spanning the
whole viewport (`y=0`, height 1100 px), so they covered the header and the tab bar and
sat outside the tab they belong to. Cause: the maintained CSS only overrode width and
the closed offset, leaving Gradio's fixed positioning in place. Solution: position each
panel absolutely against its own tab column (`top/bottom/right: 0`, `height: auto`),
keep the native slide with `transform: translateX(100%)` closed and `translateX(0)`
open, clip the closed panel with `overflow-x: clip` on `#tools-tab` and
`#applications-tab`, cancel the outer `.sidebar-parent` overlap padding for these two
panels, and move the width padding onto the tab's own workspace row. The resizer now
also writes `--agentix-sidebar-width` on the containing column, because custom
properties do not propagate upwards and the workspace padding must follow a resize.
Regression: `tests/unit/test_right_sidebars.py::test_tab_sidebars_are_contained_by_their_tab_not_the_viewport`
and the containment assertions in the browser test.

The browser tab title was `AgentiX v5`, inherited from the V5 shell. It is now
`AgentiX` (`src/agentix/ui/shell.py`), covered by
`tests/unit/test_right_sidebars.py::test_browser_title_has_no_version_suffix` and the
`to_have_title` assertion in the browser test.

## Defect V7-068-D3

Both tab dropdowns opened far from their input: measured 475 px below the
`Installed applications` field (input `y=416`, list `y=908`) and above the
`Installed tool` field. Cause: the panel slid with `transform: translateX(...)`, and a
transformed element becomes the containing block for `position: fixed` descendants.
Gradio's `.options` list is `position: fixed` with viewport coordinates, so it was
offset by the panel origin. Solution: slide with `right`
(`calc(var(--agentix-sidebar-width) * -1)` closed, `0` open) and force
`transform: none`, keeping the panel absolute inside its tab without creating a
containing block. Verified in Chromium: a fixed probe inside the panel now reports
the same viewport coordinates as one in `body`, open and closed.

## Defect V7-068-D4

A generated widget could be covered by the tools color legend. Cause: the legend was
`position: fixed; z-index: 900` while widget nodes had no `z-index`. Solution: the
legend drops to `z-index: 1` and `.application-layout-active [id^="application_"]`
paints at `z-index: 2`. Verified with an independently authored fixture that loads
the delivered stylesheet: at the overlap point `elementFromPoint` returns the widget,
not the legend.

## Defect V7-068-D5

The tools legend sat at the canvas top-left as a `position: fixed` overlay, so it
could cover application controls. It now renders as `position: absolute` inside the
canvas at `top: 48px; right: 12px`, directly below the play/edit/close toolbar
(buttons occupy `top: 8px` with 32 px height). Verified with an independently
authored fixture loading the delivered stylesheet: legend top 56 px against a lowest
button bottom of 48 px, and its right edge stays inside the canvas.

## Defect V7-068-D6

The resizer clamped every panel to `min(720px, 60% of the viewport)`, so a user could
not widen a tab sidebar further. The clamp now enforces only the 280 px minimum, the
`aria-valuemax` attribute is gone, and the small-viewport `max-width` cap applies to
the shared model sidebar only. Verified in Chromium: dragging Tools to the left edge
produced 1380 px, well beyond the former 720 px limit.

## Defect V7-069

Expanding the shared left model sidebar left an 80 px empty strip between the panel
and the work area. Cause: all three panels share one `.sidebar-parent`, and
`sidebar_resize.js` wrote `--overlap-amount` on it for every panel. The last mounted
panel (Tools, 420 px) therefore won, so Gradio's padding used 420 px instead of the
left panel's own 390 px. Solution: only `#agentix-sidebar` writes that variable, and
it computes `width - parent.left + 30`, the same formula and 30 px gutter Gradio uses
natively. Regression: `tests/unit/test_right_sidebars.py::test_left_sidebar_overlap_belongs_to_its_own_width`
and `tests/e2e/test_browser_review.py::test_left_sidebar_keeps_one_native_gutter_beside_the_work_area`,
which measured 80 px before the fix and 30 px after it, also with the Tools panel open.

## Defect V7-070

Two follow-up corrections to the same geometry. First, the shared left model sidebar
must not be resizable: it keeps Gradio's fixed 390 px width, so `panels()` no longer
lists it, `style.css` drops its handle rules, and no handle is injected. The overlap
is still owned by that panel through `syncOverlap()`, reasserted on class/style
mutations and on window resize, because Gradio's native value is `width + 10` and
would leave a 60 px strip. Second, both right panels sat flush against the workspace
edge they border, so their content now keeps a small inset
(`padding: 22px 22px 22px 40px`) inside `.sidebar-content`. Regression:
`tests/unit/test_right_sidebars.py::test_left_sidebar_is_not_resizable_and_owns_its_overlap`
and `::test_right_sidebars_keep_a_small_inset_from_the_workspace`, plus the browser
assertions that `#agentix-sidebar` has no `.agentix-sidebar-resizer`, that the gap
stays 30 px, and that the Tools content keeps its computed inset.

## Defect V7-071

Both right panels still sat flush against the workspace: the V7-070 inset padded the
content inside `.sidebar-content`, but the panel itself stayed anchored at
`right: 0`, so its border touched the workspace edge. Solution: the open panel is now
anchored at `right: var(--agentix-sidebar-gap)` (12 px, declared on
`#tools-tab`/`#applications-tab`), and the workspace reserves
`width + gap * 2`, so content stops one gap short of the border and the 12 px resizer
handle fills the gap exactly. Measured in Chromium at 1600 px: panel right edge 12 px
inside the tab, content 12 px left of the panel border, previously 0 px. Regression:
`tests/unit/test_right_sidebars.py::test_right_sidebars_keep_a_small_inset_from_the_workspace`
and the gap assertions in
`tests/e2e/test_browser_review.py::test_tab_sidebars_collapse_resize_and_keep_independent_widths`.

## Contract

- `build_tools_frontend` and `build_applications_frontend` keep their signatures;
  only the container of the right-hand controls changes.
- `TOOLS_SIDEBAR_WIDTH_PIXELS` (420) and `APPLICATIONS_SIDEBAR_WIDTH_PIXELS` (380)
  are the approved defaults; `CHAT_COLUMN_SCALE` and `WORKSPACE_COLUMN_SCALE` are 1
  because each row now has a single child.
- `sidebar_resize.js` performs no storage, network or generated-code access; it
  only reads and writes DOM geometry for the two maintained right sidebar ids and
  the fixed left panel's overlap.
- Collapsed content stays out of keyboard and accessibility navigation through the
  existing `visibility: hidden` rule, now shared by all three sidebars.

## Acceptance and regression

- `tests/unit/test_right_sidebars.py` builds both frontends with a recording
  Gradio double and asserts position, collapsed state, approved width and real
  container nesting for every relocated control, plus the registered stylesheet
  and script.
- `tests/test_ui_stylesheet.py::test_stylesheet_keeps_right_tab_sidebars_resizable`
  keeps the width properties, the inner border and the handle rules.
- `tests/e2e/test_browser_review.py::test_left_sidebar_keeps_one_native_gutter_beside_the_work_area`
  measures the strip between the open left panel and `#agentix-tabs` (30 px) and
  re-measures it with the Tools panel open.
- `tests/e2e/test_browser_review.py::test_tab_sidebars_collapse_resize_and_keep_independent_widths`
  drives Chromium: closed by default, native toggle, drag resize, width retained
  across collapse/expand and across a tab switch, and an independent Applications
  width.
- `tests/e2e/test_browser_review.py::test_model_sidebar_is_hideable_and_key_input_clears`
  now opens the Tools sidebar before asserting the single review panel, and
  `tests/test_application_review_browser.py` scopes its toggle to
  `#agentix-sidebar`; both keep their original assertions.
- `tests/test_v4_shell.py::test_sidebar_is_shared_outside_both_tabs` and
  `tests/unit/test_model_profiles.py::test_review_container_is_single_below_validation_and_outside_sidebar`
  previously required exactly one sidebar in the whole view. They now require one
  shared model sidebar outside both tabs plus exactly one right sidebar per tab,
  and keep the original single-editor, ordering and uniqueness assertions.

## Policy impact

None. No reviewed tool, widget, application snapshot, dependency or approval
binding changes; the relocated controls keep their element ids and callbacks.
