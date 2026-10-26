# UI-012: AgentiX identity and readable workflow presentation

Status: approved, implemented and verified on 2026-10-20. See
`../reports/UI012_PRESENTATION.md` for evidence and limits.

## Scope and acceptance

- UI-012-01: replace the old heading with a left-aligned supplied logo, AgentiX
  to its right, and three adjacent stacked lines: Agentic Software Engineering.;
  Developer-in-the-Loop.; AI-generated code. Software engineer-supervised. Built
  for secure, maintainable, production-quality software. All interface typography
  uses Inter. Adapt the supplied CSS's near-black, cyan and subtle-border palette.
- UI-012-02: replace decorative interface emoji with text. The compact submit
  button uses a neutral send glyph and an accessible English action name.
  Preserve original third-party verbose messages and technical events.
- UI-012-03: format host-observed results deterministically, displaying structured
  data as readable fields/tables rather than a Python dictionary. Never invent
  values, units, currency or execution success. Keep the exact execution record
  available in a collapsed disclosure. Currency formatting requires explicit
  currency information in the original query, not a guessed tool category.
- UI-012-04: validation shows stage and pass/fail counts above a bounded scrolling
  case list. Each case reveals its expected/observed data only when expanded.
  Review context keeps provisional output and full Python tests accessible in
  disclosures. Mandatory editable human approval remains unchanged.
- UI-012-05: show tool names in a bounded catalog with native disclosure arrows;
  signatures/descriptions appear only on expansion. Keep the original AST catalog
  text unchanged for application agents and CLI compatibility.
- UI-012-06: responsive layout, visible keyboard focus, contrast, keyboard-operable
  disclosures and local branding assets. No external font request is required.

## Implementation and verification

Affected: UI view/controller, new presentation helpers and local visual assets,
launch-time styling in the normal and disposable launchers, UI tests and docs.
Do not change execution, authorization, acceptance comparisons or agent prompts.
Do not read existing project-generated tools. Author temporary fixtures for tests.

Capture failing regressions before implementation. Run offline tests, real
framework checks, Ruff and disposable browser checks. Verify desktop/narrow
layouts and retain screenshots. Keep the user's existing live server untouched.
This is presentation verification, not a new real-model quality/isolation claim.
