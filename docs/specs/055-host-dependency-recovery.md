# V7-055: approved host dependency recovery

Status: implemented.

## Problem

Application acceptance can require a host component which is absent even though
the managed Python environment is otherwise usable. Before this change, browser
acceptance failed after review and closed the candidate when Playwright Chromium
was missing. The generic failure did not offer an explicit, bounded recovery.

## Requirements

**V7-055-01.** The host owns an immutable registry of recoverable requirements.
Generated Tools, generated applications, model output, browser input and error
text cannot name a requirement, alter an installation command or add a source.

**V7-055-02.** Before an application is approved or independently verified,
AgentiX checks the registered browser-acceptance requirement. If it is missing,
the reviewed candidate remains pending and is neither approved nor executed.

**V7-055-03.** The Applications UI states the requirement, purpose and action,
then exposes an installation button only for the owning pending review. Clicking
that button is the user's explicit consent for this one host change. Declining
or ignoring it makes no host change. Dismissing an informational dialog with
**Ok** is not consent and does not start an installation.

**V7-055-04.** The initial registry entry is `playwright-chromium`. It invokes
only the active AgentiX Python with `-I -m playwright install chromium`, retains
no package-manager configuration from the parent environment, and verifies that
the Playwright-selected executable exists after completion. It never installs
Firefox, WebKit, Python packages, Ollama, models or arbitrary third-party
dependencies.

**V7-055-05.** Success and failure are logged with requirement ID, outcome and
exception type only. No generated content, command output, prompt, credentials
or browser payload is logged or shown. The user must press **Approve and
verify** again after a successful installation; the previous approval click is
not replayed.

## Acceptance cases

| ID | Observable result |
| --- | --- |
| AC-055-01 | A missing registered browser requirement blocks approval before candidate approval, native execution or browser launch. |
| AC-055-02 | The install control is unavailable to other sessions, without a pending review, or for an unknown requirement. |
| AC-055-03 | A confirmed install executes only the registry command and succeeds only after the registered probe reports the expected executable. |
| AC-055-04 | Failed installation leaves the reviewed candidate pending and emits no raw installer output. |
| AC-055-05 | Existing browser launch evidence and fail-closed behavior remain for unregistered failures or post-probe races. |
| AC-055-06 | Selecting **Ok** on the informational dialog changes no host state; only **Install required host dependency** may invoke the registered installer. |

## Security and compatibility

This is an extension point for future host-owned, reviewed requirements; it is
not arbitrary dependency provisioning. Existing IaC provisioning remains the
preferred normal setup path and still uses its pinned dependency policy. No
generated artifact format, approval grant, Tool, installed application or
Ollama behavior changes.
