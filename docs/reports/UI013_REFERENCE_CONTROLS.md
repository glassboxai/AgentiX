# UI-013: reference controls and typography

Date: 2026-10-20. Implemented within the approved presentation block.

The fixed The Glass Box AI Project link follows the final header description and
targets https://glassboxai.dev/. The reference at localhost:8769/gradio was
inspected through the browser. Its computed typography, square controls and
rendered stylesheet supplied the visual contract; its settings were not saved or
modified. The reference's checked and unchecked checkboxes were inspected without
toggling application configuration.

The header now uses a responsive maximum 44px/500 Inter title; body/fields use
14px/400 and buttons 16px/600. The compact send glyph is preserved. A scoped
square-corner rule covers controls, panels, messages and pseudo-elements.
Checkboxes match the observed 20px square, 2px muted border, dark unchecked fill,
cyan checked fill and dark SVG check. Keyboard focus remains visible, disabled
opacity is specified and forced-color mode restores native appearance. Native
checkbox semantics, initial unchecked approval state and server callbacks are
unchanged. No script or remote font/resource request was introduced.

The header regression failed before adding the link (`ui013-link-red.txt`).
Final evidence: 316 offline tests passed with 19 deselected (`ui013-offline.txt`);
five browser checks passed (`ui013-browser.txt`); Ruff lint/format passed for 78
active Python files. Browser checks cover desktop/mobile, href, title weight,
computed square corners, checkbox width/border/fill, Space-key toggling, checked
state, focus outline and the existing approval/session behavior. Earlier UI-012
framework evidence remains historical; no new framework or isolation claim is
made for this CSS/header adjustment.

`ui013-live.png` records the new actual GUI at localhost:7872. That separate
instance has an empty temporary catalog, retains qwen3-coder:30b/native isolation,
and has not executed a new query. Older live instances were not restarted.
Browser fixtures do not prove new live model or native isolation behavior.
New hashes are separate in `ui013-hashes.json`; older snapshots are preserved.

Local qwen3:14b is used only to draft report prose. The draft/provenance is
retained and reviewed against these raw checks; no code/tests are model-generated.
