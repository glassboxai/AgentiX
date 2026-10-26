# UI-013: reference typography and square controls

Status: approved, implemented and verified on 2026-10-20, including checkbox
styling. See `../reports/UI013_REFERENCE_CONTROLS.md`.

Add The Glass Box AI Project link below the final header description. Match the
observed local reference: Inter, 44px/500 desktop heading, 14px/400 body/fields,
16px/600 action buttons. Keep the compact send glyph. All application controls,
panels and chat bubbles have square corners. Reference checkboxes are 20px,
2px muted borders, dark unchecked fill, cyan checked fill and dark check mark,
with cyan keyboard focus and disabled opacity. Preserve native checkbox semantics
and Windows forced-color support. Do not change approval defaults or behavior.

Change only branding/CSS, related presentation tests and documentation. Verify
the link order, computed typography/radii and checkbox checked/unchecked/focus
states through a disposable browser. Preserve previous verification evidence and
leave running applications untouched; open a separate updated instance.
