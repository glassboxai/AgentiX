# UI-MODEL-002: sidebar controls and functional verification

Approved by the user on 2026-10-25 after explanation of the files and rationale.

Use NexisNodes v0.4.0 Glass Box sidebar secondary-button tokens: translucent dark background rgba(255,255,255,.035), text #f1f3f5 and border rgba(255,255,255,.10), with visible hover/focus and unchanged primary/destructive semantic styles. Keep square geometry. Apply only to the AgentiX sidebar.

For Ollama, hide API key and external-transfer consent on first render, provider changes and saved-profile resets/loads. Clear both values on provider changes. External profiles expose the password and unchecked consent; local execution never requires either. Preserve backend validation, ownership and remote consent enforcement.

Playwright must click all five controls and assert their effects: Refresh models reveals a newly discovered choice; Apply model changes the selected runtime's observable behavior; Save profile persists metadata to another session and supports updates; Refresh saved profiles discovers a profile created after that browser loaded; Delete removes the selected profile from storage and refreshed choices. Test hidden local secrets, external visibility, clearing on provider changes and computed sidebar colors. Use synthetic keys, injected network/model/vault boundaries and independent temporary storage. No paid inference or existing generated artifacts. Distinguish simulated services from real Gradio/Edge/Windows vault checks.

Use SDD/TDD, preserve red evidence, update English docs/incidents/reference, run relevant unit/framework/native credential/browser tests, offline suite and Ruff. Existing live instances must not be restarted by automated tests.

Implementation: completed; verification and limitations are recorded in ../reports/SIDEBAR_017_VALIDATION.md.
