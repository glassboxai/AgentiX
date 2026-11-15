# V7-046: public application input layout

Approved scope: schema-3 public inputs must participate in the existing canvas
editor. Preserve component identities, values, callback bindings, strict geometry
validation and persisted positions. Do not alter approval hashes, existing apps,
other versions, generated_tools or live processes.

## Incident and correction

The compositor created application_input_<name> controls outside application-canvas.
The editor searches only canvas descendants. Independently, application_layout_ids
omitted public input IDs, so moving the controls alone would not enable editing or
storage. V6-044 regressions covered widget controls but omitted public inputs.

Create public inputs inside the canvas and include their declared schema-3 IDs in
the shared allowlist. Reuse the existing editor and numeric storage validation;
keep the Run toolbar outside the canvas and preserve legacy schema behavior.

## Acceptance and regression

All declared public inputs can move and resize. Edits preserve entered text and
callback bindings/results. Save/reload restores geometry. Unknown input IDs,
toolbar IDs and invalid numeric geometry remain rejected. Tests use independently
authored temporary packages and inert HTML, never existing generated artifacts.

Before correction the allowlist assertion and real Gradio ancestry assertion
failed. After correction, three focused checks passed: the contract, real Gradio
composition/callback and Playwright editor movement/resize/save/reload. Gradio
inserts Form containers, so ancestry checks include structural descendants.
Playwright used installed Microsoft Edge with an intercepted loopback endpoint;
its default bundled Chromium executable was absent. No download was performed.
This browser fixture does not establish physical disk persistence or live GUI
behavior. Existing callback expectations remain unchanged. No inference, native
isolation claim, deployment or live restart is part of this block. Maintained
runtime byte changes continue to invalidate previous policy-bound approvals.

## Final verification (2026-10-30)

- Offline suite: 834 passed, 87 deselected; 18 CrewAI deprecation warnings.
- Focused red/green: contract and Gradio ancestry failed before the correction;
  contract, Gradio and inert browser regression passed after it (3 passed).
- Additional explicit frameworks/browser run: 5 passed, 10 deselected, including
  the existing native code-package browser test with authored temporary fixtures.
  This is fixture evidence, not real-model or existing installed-app acceptance.
- Ruff lint passed; format verification passed for all 323 maintained Python files.
- Reference generation and exact freshness check passed; changed reference entries
  were reviewed for canvas ancestry, public IDs and preserved callback contracts.

No change was deployed to the running GUI. The installed Microsoft Edge executable
was used only by disposable browser tests. No existing instance was restarted.
This record is manually authored from raw test evidence; no model drafted prose.

### New maintained source hashes

These SHA-256 values identify this correction; historical baseline hashes remain
unchanged. They do not represent installed package or approval hashes.


- src/agentix/application/templates/code/app.py: 899d634da2a8c6a1b2062b5e0119c310cfab2aa6e788d308563abebc9e65b41d
- src/agentix/layout_contracts.py: 33cab2aff07b7ca5e9f76de51f81ddec7d957d25bbeb1b6091cecec300c86219
- tests/test_code_application.py: e2042d58e23154c9b10416e51eeb47ef89632437bfe545fe797a3ae14c9219a6
