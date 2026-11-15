# V5-043 — Generated application connection code

Status: implemented and verified with authored fixtures and the real Simply app.

## Result

The default CrewAI route generates Python connection code and presentation/input
metadata. New version-3 packages have no workflow, execution order or binding
interpreter. Opening or executing them does not call agents. Tools and their
contracts remain unchanged. Exact dependency checks, widget reuse, human review,
strict values and native AppContainer execution remain in place. Legacy packages
keep their original runtime compatibility.

The existing file editor exposes generated connection code and independent
application acceptance inputs/expected values. Cases start empty and block approval
until reviewed; they stay outside the child. Source/case edits revoke approval.

## Verification

- Initial focused regression: five expected failures before implementation.
- Offline suite: 827 passed, 85 deselected.
- Real CrewAI/Gradio framework checks: 13 passed, 899 deselected; no inference.
- Native positive fixture: one test, two different dependent-call inputs passed.
- Native rejection fixtures: missing and duplicate calls each rejected with specific
  child errors, observed nonzero process exit and no published application result.
- Native browser fixture: one test; both repeated combined runs matched host-held
  expected results and displayed the observed tool arguments.
- Ruff lint passed; format check passed for 321 maintained files.
- Source reference freshness passed. No project generated_tools inspection.

The first native positive attempt and one rejection attempt timed out preparing
Windows ACLs before child execution; isolated repeats passed. An initial test
assertion incorrectly expected a Boolean instead of the native API's empty failure
string; it was corrected while retaining all error/result checks. Historical
verification hashes were not replaced. Current source hashes are recorded separately
in [the machine-readable receipt](V5_043_VERIFICATION.json).

## Live Simply app

The owned GUI at http://127.0.0.1:7882/ was reloaded after validating its launcher
and child ownership. Port 7880 and other user processes were preserved.

The original English requirement-only request was submitted to qwen3-coder:30b.
The generated code calls both counters with the original text, then passes their
scalar results directly to two calculator calls with multiplier 3. It has no array
indexing. Three approved tool widgets were reused; no tool revisions or old tool
test reruns occurred. The human reviewer supplied independent Hello world values:
three vowels, two words, products nine and six. Native data comparison and both repeated browser runs passed. The app was installed
as `simply-app` and left open. A final visible run returned 3, 2, 9 and 6 with
status Completed. The current direct preview is http://127.0.0.1:53317/; use the
installed application catalog in 7882 after closing it. No agents run on Run.

The new manifest has schema_version 3 and no graph fields. Exact original legacy
app/operation template baseline hashes remain unchanged and are recorded in the
receipt. No tools, tool contracts or grants were edited. The original random-number
A complex task has not been regenerated with the new route in this block.

Provenance: engineer-authored and manually reviewed report; no report inference or
remote endpoint. Authored framework/native fixtures establish architecture/runtime
behavior; model quality is claimed only for the separately described observed run.
See [requirements](../specs/043-generated-application-code.md).
