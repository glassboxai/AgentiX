# V7-076: widget style window and style-only persistence

Status: implemented. Identifier: V7-076.

## Problem

A widget's scoped stylesheet could only be edited as raw text in the review
editor, and any saved byte revoked the whole application approval. Changing a
border colour therefore cost the same as changing executable code, because
`_identity` hashed every captured member, including `<tool>_widget.css`, into one
application digest.

## Decision

Two sequential changes, both approved by the owner.

1. A scoped stylesheet no longer participates in the application identity. The
   closed grammar in `agentix.widgets.styles` is the gate for style bytes, so a
   colour, radius or font edit keeps the existing approval valid.
2. A right-click on a widget control opens an overlay window that edits six
   declarations and writes them back to `<tool>_widget.css`.

## Requirements

- Right-clicking a widget control in the framed preview opens the window for that
  widget's tool, and only while the layout editor is active. Status and public-input
  controls are excluded, exactly as for the double-click source selection of V7-066.
- Saving applies the merged stylesheet to the running preview immediately, scoped to
  the widget instance ids declared by the manifest, and reapplies it when the preview
  reloads in the same session. The live copy is applied as inline `!important`
  declarations on the widget nodes, because the preview sheet forces radius and
  background at specificity (0,5,0) with `!important`; the saved file keeps the plain
  reviewed form.
- Saving also rewrites the served `application.css`, so a reload and the separate
  "View as web" tab render the new style without the parent bridge. That served copy
  raises specificity to (0,10,0) at startup and (0,14,0) after a style save,
  marks declarations important and repeats font rules
  on `input, textarea, select, button`, `label span` and `.label-wrap span`, which do
  not inherit font from the container. Layout grips are excluded so their glyph size
  never follows the widget font.
- The window is compact (`min(430px, 94vw)`, `max-height: min(88vh, 760px)`) and
  scrolls inside itself with the shared thin scrollbar. `Value font` / `Value size`
  style the text typed or shown inside the widget; `Caption font` / `Caption size`
  style the label above it.
- The window edits border radius (0-64 px), border width (0-8 px), border color,
  background color, font family from a closed list, and font size (8-72 px).
- Saving rewrites only those declarations in the base scoped block. Unmanaged
  declarations and every `:hover` block are preserved.
- `border-style` is derived: `solid` for a non-zero width, `none` for zero.
- Saving a stylesheet does not revoke the application approval and does not close
  the preview. Saving any executable member keeps the existing revoke-before-write
  rule.
- For a loaded installed application the save also rewrites `<tool>_widget.css`
  inside `data/applications/<app>`, because the loaded candidate is a disposable
  draft copy. The installed package is re-verified first and its sealed digest stays
  valid.
- The member hash in `application.json` is rewritten, so capture still proves the
  stylesheet on disk is the one the package declares.
- A stylesheet edited outside the maintained writer is still rejected by capture.

## Implementation

| Module | Contract |
| --- | --- |
| `agentix.widgets.styles` | `STYLE_SUFFIX`; `border-radius` added with bounds 0-64 and up to four values |
| `agentix.widgets.style_editor` | `StyleValues`, `read_style`, `checked`, `merge_style`; pure text transformation, no IO |
| `agentix.application.style_member` | `style_member_name`, `write_style_member`; validates, writes and rebinds one member hash |
| `agentix.lab.application_artifacts` | `_identity` excludes style members and normalises declared style hashes out of `application.json` |
| `agentix.application.app_review` | `save` returns whether the grant was revoked; the style branch returns `False` |
| `agentix.controllers.applications` | `owned_candidate` accessor; `save_file` reports the style-only outcome |
| `agentix.controllers.widget_style` | `WidgetStyleBackend.load/save`; persistence delegated to `save_file` |
| `agentix.ui.widget_style_dialog` | overlay window, hidden opener and `outputs()` |
| `agentix.ui.assets.widget_style.js` | parent bridge: framed child plus canonical tool only |
| `agentix.ui.assets.application_editor.js` | `contextmenu` publishes `agentix-widget-style` |

## Security

The style surface stays inside the existing grammar: no imports, URLs, custom
properties, positioning, visibility or interaction properties. Bounds on radius,
width, padding, margin and font size keep a stylesheet from covering or displacing
the lifecycle controls. The window accepts only a canonical tool identifier, so
browser text never becomes a path. `write_style_member` rejects reparse ancestors
and hard-linked members before writing.

## Consequences

- `app_policy()` changes because `widgets/styles.py`, `lab/application_artifacts.py`
  and `ui/assets/application_editor.js` are policy members. Installed applications
  require one re-approval after this block; subsequent style edits require none.
- A running preview stages its stylesheet at startup, so the new style appears when
  the preview is reopened.

## Defects corrected after the first delivery

| ID | Cause | Solution | Regression |
| --- | --- | --- | --- |
| V7-076-D1 | `_identity` changed the digest formula, so every record sealed before this block reported `source_changed` and `Load selected app` failed with `ValueError` | `_legacy_digest` reproduces the previous formula and `_validated` accepts a record whose legacy digest matches; `load_app` also falls back to `load_stale` for a stale policy | `test_record_sealed_with_the_legacy_digest_still_loads`, `test_legacy_digest_does_not_accept_a_changed_member` |
| V7-076-D2 | `save.click` declared only status and token as outputs, so no update could hide the overlay | `_saved` returns the container update and the save handler declares it; a rejected value raises before the update | `test_save_closes_the_window_on_success`, `test_save_keeps_the_window_open_when_a_value_is_rejected` |
| V7-076-D3 | The overlay was fixed and centred with no pointer handling | `widget_style.js` drags by the title bar and clamps to the viewport | `test_v7_076_window_can_be_dragged_by_its_title` |
| V7-076-D4 | `contextmenu` published the tool in view mode, so the window opened without the layout editor | The handler returns unless `editing` is true | `test_v7_076_editor_posts_the_right_clicked_widget_tool` (view mode posts nothing, edit mode posts once) |
| V7-076-D5 | The preview stages `application.css` once at startup, so a saved stylesheet never reached the running widget | `save` returns the merged CSS with the tool's widget instance ids; the bridge pushes it to the frame and the editor injects a scoped live style, reapplied on reload | `test_v7_076_saved_stylesheet_is_applied_to_the_live_widget` (computed `border-radius` becomes 12px) |
| V7-076-D6 | The drag wrote inline `left`/`top`, which lose to the `!important` position rules in `style.css`; clearing the inline `transform` then dropped the centring translate, so the box jumped by half its size and froze | The stylesheet resolves `left`/`top` from `--agentix-widget-style-left/top` and the shift from `--agentix-widget-style-shift`; the drag sets those custom properties, which `!important` does not override | `test_v7_076_window_can_be_dragged_by_its_title` now loads the real `style.css` and asserts a 20/30 px nudge and a 100/60 px drag with no jump |
| V7-076-D7 | `load_app` copies the installed package into a disposable draft, so the style save only rewrote the draft and `<tool>_widget.css` under `data/applications/<app>` never changed | `InstalledApps.write_style_member` re-verifies the installed package, rewrites the member and its manifest hash, and keeps the sealed digest valid; `save_file` calls it for a style member of a candidate with a `catalog_id` | `test_installed_style_write_changes_the_installed_package`, `test_installed_style_write_rejects_an_unsafe_declaration`, `test_save_file_writes_the_installed_package_for_a_style_member` |
| V7-076-D8 | The live copy injected the stored CSS unchanged, so `:where()` (specificity 0) lost to the preview's own `.application-layout-editing .application-editable-element { background: … !important }`; radius, background and border never showed while font did | The live copy raises specificity to `[id^="…"][id]` and marks every declaration `!important`; the saved file keeps its reviewed plain form | `test_v7_076_saved_stylesheet_is_applied_to_the_live_widget` now loads the real `style.css` and asserts radius, background, family and size together |
| V7-076-D9 | Even at `[id][id]` the injected rule lost: the preview sheet declares `border-radius: 0 !important` and `background: … !important` at specificity (0,4,0) in a later sheet, so source order and specificity both favoured it | The live copy applies each declaration as an inline `!important` style on the widget nodes, which outranks every author stylesheet; the saved file is unchanged | GUI end-to-end on `MultiplyAll2`: computed `['18px', 'rgb(38, 23, 125)', 'Tahoma', '26px']` after saving radius 18 and size 26 |
| V7-076-D10 | `application.css` was staged once at startup, so the separate "View as web" tab and any reload kept the old stylesheet; and font declarations on the widget container never reached the inner `<input>`, which does not inherit font | `ApplicationSession.restage_styles` rewrites the served stylesheet on save; `served_style` raises specificity to (0,6,0), marks declarations important and repeats font rules on `input, textarea, select, button`; the live inline copy does the same for controls | GUI end-to-end: inline and web tab both `['22px', 'rgb(38, 23, 125)', 'Georgia', '28px']`, inner input `['Georgia', '28px']`; `test_served_style_wins_the_preview_cascade_and_reaches_form_controls`, `test_restage_styles_rewrites_the_served_stylesheet`, `test_v7_076_served_stylesheet_applies_without_the_parent_bridge` |
| V7-077-D1 | The window was 460 px wide and 727 px tall with one field per row, so it covered the preview | Fields are paired in rows and the window is `min(360px, 92vw)` wide with `max-height: min(68vh, 560px)`, `overflow-y: auto` and the shared thin scrollbar | GUI: `DIALOG_SIZE [360, 490, 'auto', True]`; `test_v7_077_window_is_compact_and_scrolls_inside_itself` |
| V7-077-D2 | The inline copy applied `font-size` to every `button` inside the widget, which includes `.application-layout-handle`, so the six grip dots grew instead of the caption | The control loop excludes `.application-layout-handle` and `.application-visibility-toggle`, and the grip pins `font-size: 12px !important` | GUI: `INLINE_HANDLE 12px` while `INLINE_LABEL ['Tahoma', '27px']`; `test_v7_077_caption_font_reaches_the_span_and_spares_the_grip` |
| V7-077-D3 | The caption text lives in `label > span`, which Gradio styles directly, so the `label` rule never reached it; and `served_style` appended `label span` to a selector already ending in `label`, building an impossible `label label span` | Caption blocks emit `span` as their descendant target and container blocks emit `label span` / `.label-wrap span`; the inline copy sets the font on `label span` and `.label-wrap span` | GUI web tab: `label ['Tahoma', '27px']`, `span ['Tahoma', '27px']`, `input` field `rgb(31, 42, 68)`; `test_served_style_reaches_the_caption_span_and_spares_layout_grips` |
| V7-077-D4 | `restage_styles` rebuilt the served sheet from `members.get("application.css", b"")`, which is never a package member, so every save replaced the 30 KB base stylesheet with the widget block alone (30694 → 1467 bytes) and the web tab rendered an unstyled page | `_stage_payload` appends the widget block after `STYLE_MARKER`; `restage_styles` truncates at the marker and rebuilds only that block, keeping the base sheet | GUI: served CSS stays 30980 bytes after saving and the web tab computes `44px`; `test_restage_styles_keeps_the_base_stylesheet` |
| V7-077-D5 | The window was 360×560 with no room for the status line, and `gr.Markdown` captions rendered twice because Gradio applies `elem_classes` to two nested nodes | Window is `min(430px, 94vw)` with `max-height: min(88vh, 760px)`; the status block is allowed to overflow; captions use `gr.HTML` and only where the component label is not self-explanatory | GUI: `GEOMETRY [430, 731, 729, 729]`, status `50` px tall with the full sentence, three captions, Save visible; screenshot reviewed |
| V7-076-D11 | Gradio's embedded startup stylesheet prefixes the old widget rules with three container classes. The first regression fixture modelled the older (0,6,0) startup selector, so raising the served selector to (0,10,0) passed that fixture but still lost to a current (0,10,0) startup selector plus the three classes | The current regression uses the startup sheet produced by the same `served_style` version as the restaged sheet; D13 supplies the causal correction | Live 7878/58075: served CSS carried Value size 20 px while the web input computed 8 px; CSSOM showed the prefixed startup rule and the later, weaker linked rule |
| V7-076-D12 | The live inline renderer propagated each caption rule to every descendant form control of a Gradio `label`; the label can wrap the value input, so the final caption pass overwrote its value font | Caption selectors propagate only to descendant spans; the base widget selector still propagates to form controls and caption spans, with the later caption span rule winning for caption text | Live 7878: saves of Value/Caption 24/19, 13/30 and 29/17 produced input sizes 19, 30 and 17 px before correction; `test_v7_076_saved_stylesheet_is_applied_to_the_live_widget` failed at 27/27 instead of 20/27 and now verifies a second 13/30 save |
| V7-076-D13 | After a save, the linked `application.css` had the same (0,10,0) widget selector as Gradio's embedded startup copy; Gradio's three container classes made the stale copy win even though the HTTP response used `no-store` and contained new rules | `restage_styles` emits a (0,14,0) served copy while startup remains (0,10,0); the extra four attribute selectors outrank Gradio's three class selectors without changing the reviewed stylesheet | `test_v7_076_saved_web_style_overrides_gradio_startup_snapshot` fails with `system-ui`/20 px against the current startup copy before correction and passes with Georgia/31 px and `rgb(34, 68, 102)` after; live post-fix measurement awaits a later authorized launch |
| V7-076-D14 | Each `restage_styles` call rebuilt the served sheet from the original immutable approved files, so saving a second widget restored the first widget's old CSS in `application.css`; the framed preview retained the first save as inline style and diverged from "View as web" | Keep a session-owned copy of the latest per-widget CSS bytes and rebuild the served sheet from it after every save; `ApplicationReview.save` continues writing each individual `<tool>_widget.css` and its manifest hash | `test_restage_styles_preserves_successive_widget_saves` failed on the lost first radius and passes after correction; `test_review_style_save_keeps_the_candidate_approved` verifies both individual CSS files; browser snapshot test passes; live 7878/60126 processes were not restarted |

## Verification

`tests/test_widget_style_member.py` (identity, manifest rebinding, rejection,
hard link, review revocation split), `tests/test_widget_style_editor.py` (defaults,
merge preservation, derived border style, bounds, backend load/save) and
`tests/test_widget_style_window.py` (browser: right-click message and parent
bridge). Offline suites `test_v5_widget_css`, `test_code_application`,
`test_general_application_pipeline`, `test_composite_application`,
`test_application_catalog`, `test_widget_reuse`, `test_installed_apps`,
`test_applications_backend` and `test_v4_shell` remain green, with Ruff and
reference freshness.
