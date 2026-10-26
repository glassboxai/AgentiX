# LIVE-UX-001: verbose agent messages alongside technical events

Date: 2026-10-19. Status: approved display correction implemented and verified.

The user explicitly requested retaining technical events in the GUI while restoring
the original `verbose=True` messages. All four application agents and all Crew
construction paths now enable verbosity, including the manager, separately gated
creation stages and final execution Crew. The expandable activity preserves the
installed CrewAI renderer's role, task, tool result and final-answer information
instead of replacing that information with diagnostic summaries.

Both the main GUI and supervised temporary launcher use a shared startup stdout
routing context. Workers retain context-local ownership; no worker installs its
own process-wide stream. The original stream is restored on exit or launch failure.
Technical events continue to appear in the same session-owned activity. No global
active-session pointer or shared user-visible buffer is introduced.

## Reproduced failures and corrections

`verbose-activity-red.txt` records eight initially failing cases covering agent
and Crew verbosity, output routing and startup restoration. Those cases now pass.

VERBOSE-ERR-001: the real SDK renderer uses Unicode panel icons that a redirected
Windows cp1252 console can reject. The original capture mirrored to that console
before retaining GUI text, so the failure erased useful activity. The capture now
retains Unicode and escapes only the host-console copy if encoding fails. Other
I/O failures still propagate. `verbose-unicode-red.txt` records the failing unit
reproducer; `verbose-framework-first.txt` records the actual renderer failure.

VERBOSE-ERR-002: Rich prints a panel through many styled write fragments. Treating
each fragment as a stripped message broke formatting and displaced useful content
from the activity tail. Capture now reconstructs logical lines, strips complete
ANSI sequences even when split between writes, and includes a bounded partial line
for streaming. `verbose-fragments-red.txt` records the failing reproducer;
`verbose-framework-second.txt` records lost earlier activity before reconstruction.
Existing tail and retention fixtures now terminate logical lines explicitly.

Retention remains bounded: 256 completed lines, a partial line limited to 4096
characters, and a visible tail capped at 256 lines. Individual retained lines are
limited to 4096 characters. The normal UI continues to show its configured tail;
this is not an unlimited execution archive. SDK renderer limits also still apply.

## Fresh verification

| Check | Result | Evidence |
| --- | --- | --- |
| Offline suite | 284 passed | `verbose-offline.txt` |
| Real framework adapters | 5 passed | `verbose-frameworks.txt` |
| Deterministic browser scenarios | 3 passed | `verbose-browser.txt` |
| Ruff check and formatting | Passed; 71 active Python files already formatted | `verbose-ruff.txt` |

The new real-framework test emits actual CrewAI start/action/finish events through
its normal event bus and console renderer. Two concurrent real UiController
workers receive their own role, task, tool result, final answer and technical
event text in the rendered conversation, without the other controller's content.
It starts no model or HTTP server. The browser suite uses its established trusted
temporary fixtures; it does not establish model quality or tool correctness.
Source hashes and precise scope are in `verbose-evidence.json`.

## Scope and remaining work

The application model remains `ollama/qwen3-coder:30b`. The supervised functional
run is still paused; this display change does not resume it or certify a live
tool-creation outcome. Shared workflow instructions and additional handoff work
remain proposed in specification 010. No existing generated project artifacts
were read or executed, and the user's original live process was not restarted.
An already running process must load the updated source at its next launch.

Verbose console text can intentionally include workflow information requested by
the user. Structured diagnostic events retain their fixed-field, payload-free
policy. No comprehensive sanitization of arbitrary provider verbose output is
claimed. This change does not alter approval, acceptance or native isolation rules.

## Local report provenance

A prose-only draft was requested from local `qwen3:14b`, separately from the
application model, using the evidence JSON. Code and tests were not requested
from Ollama. The draft and provenance are retained under `verbose-ollama-draft`;
this reviewed report, source and raw verification evidence are authoritative.

Review corrections: the draft incorrectly inferred unresolved defects from the
recorded pre-fix failures. Those verbosity, Unicode and fragment failures now
have passing regressions; they are not outstanding defects. Its suggestion that
excluding generated artifacts or avoiding a live restart reduces the validity of
the reported adapter/routing checks is unsupported. Those are explicit scope
constraints; the paused real-model workflow is separately and clearly unverified.
