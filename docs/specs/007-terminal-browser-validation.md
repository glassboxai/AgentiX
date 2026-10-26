# CLI-001 and E2E-001: terminal review and browser regression tests

Status: implemented and verified. Approved by the user's request to implement the proposed terminal and browser work. Current evidence: `../reports/CLI_BROWSER.md`.

CLI-001 preserves `main.py`, exit aliases, blank-input handling and workflow error recovery. The main terminal thread owns all input; a daemon worker runs the shared workflow. Pending requests display their action, content and review context. Only an explicit approve decision authorizes the displayed owner/request pair. Reject is the default. Edit accepts multiline content terminated by `.end`, followed by a separate approval decision. EOF and Ctrl+C close the approval coordinator and exit without granting pending or future permissions. A terminal interrupt cannot forcibly terminate an in-flight model call.

Manual acceptance is mandatory even with file auto-approval. The terminal uses the existing coordinator and acceptance evaluator; it does not implement another verifier. Logs contain event and operation identifiers, never reviewed bodies. Terminal output intentionally displays review content to the local user.

E2E-001 uses real Gradio and Playwright with a separate loopback server, temporary storage and independently authored trusted fixtures. It verifies human review, edited acceptance cases, rejection, and browser session separation. It makes no Ollama requests and does not establish OS isolation or model quality. Native isolation remains covered by its separate opt-in suite. Browser tests must never restart the live application or access project generated artifacts.

Validation: characterize existing CLI tests first; capture new failing CLI regressions before implementation; run offline, framework and opt-in browser checks; retain raw evidence and document dependencies and limitations.
