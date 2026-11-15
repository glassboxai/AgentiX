# V7-058: explicit profile selection and truthful generation diagnostics

## Observed defect

Creating `VowelsExceptA` with the description "Create an application which takes
a text and returns the total amount of vowels minus the amount of 'a'" and
accepting the three approved tools `count_vowels`, `count_letter_a` and
`calculator` produced no application and no message. The status line showed
`The saved local model identity is unavailable or changed. Inspect it and use
Reset trusted generation identity only if you accept the change.`

The log recorded `candidate_accepted count=3`, the three `candidate_selected`
events and `application_generate_started`, then stopped. `application_tools_resolved`
was never reached.

## Cause

`SessionModelConfiguration.ensure_generation_identity()` requires a selected
saved profile because the TOFU baseline is stored inside the profile record.
Every browser session starts with `saved_id=""`, and only `select_saved()` fills
it, so a fresh session failed the precondition even though the trusted digest
was unchanged. `ApplicationsBackend._generate()` caught `(ProfileError, ValueError)`
together and replaced every failure with the changed-digest text, which names a
destructive reset that cannot fix a missing selection. `_safe_stream()` yielded
that row without logging, so the rejection left no trace.

Tools never checks the generation identity, so the same session could create
tools and not applications.

## Solution

1. `profile_errors.MESSAGES` gains the closed code `profile_not_selected`:
   `Select a saved local profile in Model settings before generating an application.`
2. `ensure_generation_identity()` raises `ProfileError("profile_not_selected")`
   instead of an untyped `ValueError` when no saved profile is selected. The
   precondition itself is unchanged.
3. `_generate()` handles `ProfileError` separately: `profile_not_selected` and
   `generation_identity_changed` show their own closed message, any other
   `ProfileError` and a bare `ValueError` keep the unavailable-or-changed text.
   Each rejection logs `event=application_generate_rejected reason=<code>`.
4. `UiController.profile_action()` accepts the `load` action. It refreshes the
   saved catalog and, when the session has no selection and exactly one profile
   is saved, selects that profile for editing. `demo.load` uses `load`; the
   Refresh saved profiles button keeps `refresh` and never selects for the owner.

## Requirements

1. With one saved local profile and no manual selection, a new session can accept
   candidates and start application generation without touching Model settings.
2. With zero or several saved profiles the selection stays explicit, and the
   rejection names the missing selection instead of a changed digest.
3. A genuinely changed digest still reports `generation_identity_changed` and is
   only replaceable by the explicit reset action.
4. Every identity rejection is logged with a bounded reason code and no payload.
5. No profile record, credential or trusted digest is rewritten by this change.

## Security constraints

- Auto-selection loads a record for editing; it never activates a provider,
  never grants remote consent and never writes the trusted digest.
- The rejection log carries only the session id and the closed reason code.
- The changed-digest path keeps its existing refusal; nothing is reset
  automatically.

## Evidence

`tests/test_applications_backend.py` covers the missing-selection message, its
log event and the unchanged changed-digest refusal.
`tests/unit/test_saved_model_profiles.py` covers auto-selection with one profile,
explicit selection with two, and the Refresh button keeping the selection.
Offline suite, Ruff and reference freshness were run after the change.

The reported failure was reproduced on the live 7878 instance: with `New profile`
selected the accept stream stopped silently, and after selecting `Default profile`
the same accept reached `application_tools_resolved` and `application_model_started`.
The live process was not restarted.
