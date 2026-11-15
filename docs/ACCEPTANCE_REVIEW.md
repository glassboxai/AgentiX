# Reviewing generated tests and acceptance cases

Agentix first generates Python unittest tests and runs them in isolation. A successful initial result is **provisional**, because generated Python can manipulate its own testing framework. It does not authorize the tool.

## Review in the Gradio application

1. Submit your requirement. Review ordinary file writes as before, or use file auto-approval for those writes only.
2. The agent runs provisional tests and proposes acceptance cases. The authorization panel shows the Python tests read-only, the provisional output and editable acceptance JSON.
3. Check that every case's purpose, function, inputs and expected result match your requirement. Add boundaries and invalid inputs. Edit expectations or tolerances if necessary. Changing Python tests requires rejecting and requesting regeneration; the editable acceptance document contains data only.
4. Select **Approve Reviewed Content** or **Reject Operation**. File auto-approval never accepts this review. A request expires after five minutes by default. Rejection/expiry prevents automatic reprompting in that query; submit a new query to start another review.
5. After approval, Agentix executes each case in a fresh isolated process. The separate **Tool validation** panel shows host-computed verdicts, expected/observed data and the approved contract digest. Any failed case prevents authorization. Large displayed details are explicitly truncated; transport and schema limits still apply.

The panel distinguishes provisional checks, pending human review, approved/evaluating, rejected/failed, verified-against-approved-cases and invalidated states. A model's conversational answer cannot replace that panel's authorization status. Only covered functions become executable.

## Editable case format

```json
{
  "version": 1,
  "cases": [
    {
      "id": "positive_sum",
      "purpose": "Add two positive integers",
      "function": "add",
      "kwargs": {"a": 2, "b": 3},
      "expect": {"kind": "value", "value": 5}
    },
    {
      "id": "invalid_input",
      "purpose": "Reject a text argument",
      "function": "add",
      "kwargs": {"a": "invalid", "b": 3},
      "expect": {"kind": "raises", "type": "TypeError"}
    }
  ]
}
```

- `value`: exact, recursive JSON comparison. Numbers, strings and booleans are distinct; integer `5` and floating-point `5.0` also differ. Dictionary key order does not matter; list order does.
- `approx`: numeric comparison, for example `{"kind":"approx","value":0.3,"abs_tol":1e-9,"rel_tol":1e-9}`. Both tolerances must be explicit, finite and nonnegative. Choose them to match the requirement.
- `raises`: compare the function's reported exception type. Child/process/serialization failures cannot satisfy it. Fatal process exits are failures, not expected exceptions.

Use one to sixteen cases and unique identifiers beginning with a letter, followed by letters, digits or underscores. Functions must be public names. The complete document is limited to 64 KiB; values must be finite JSON data, with bounded nesting/collections/strings. Do not insert Python assertions or scripts. Standard-library tools returning JSON-compatible values are supported; custom Python objects require the generated function to provide an appropriate JSON representation.

## Authorization lifetime and scope

Approval binds the owner, implementation, Python tests, edited acceptance contract, covered functions and evaluator version. After a successful isolated call, a bounded session-only grant may authorize unchanged functions in later queries without repeating tests or acceptance. Each answer still requires a fresh isolated call and current-query receipt. Re-running provisional checks, observed file drift, explicit revocation or session closure removes the grant. With the approved REUSE-002 protected store, intact successful approvals survive restart, model runtime replacement and other sessions on the same deployment/user/machine. Without a protected record, renewed review is required. Sensitive or unclassified calls require explicit per-call approval without expanding sandbox permissions. No acceptance document is silently written as a project artifact.

Expected values stay in the parent evaluator and are never supplied to the isolated implementation. The evaluator executes no generated assertions and loads no Python objects from child data. However, finite cases prove agreement only for the observed inputs. They do not prove every possible input, internal execution provenance or that the approved requirement itself is correct. A second AI reviewer is not an independent source of truth.

Interactive acceptance is implemented in both Gradio and the CLI. The terminal uses the same owner-bound coordinator and host evaluator. No Docker or installer is required or added by this feature. Existing native Windows isolation requirements still apply.

## Terminal review

Start `.\.autotool\Scripts\python.exe main.py` from the checkout. Submit a query as before. When approval is required, the terminal displays the action, destination and content. Acceptance reviews additionally display provisional results and Python tests. Type `approve` to authorize exactly that displayed request, `reject` (or an empty answer) to deny it, or `edit` to enter replacement content across multiple lines. Finish editing with `.end` on its own line, then explicitly choose `approve` or `reject`. A literal `.end` line cannot be entered through this editor. Directory creation and file writing require separate decisions unless file auto-approval is already configured; acceptance always requires manual review.

After the workflow completes, `HOST VALIDATION STATUS` displays the maintained evaluator's state and case verdicts separately from the model's final response. Review text escapes terminal control characters while retaining original approval bytes. EOF or Ctrl+C exits and denies pending/future permissions; `q`, `quit` and `exit` remain query-level exit aliases. Request expiry still denies authorization, even if the terminal is waiting for input; a late decision is reported as stale. Interrupting a terminal session does not forcibly cancel an in-flight model call. CLI review tests use trusted temporary fixtures, without a live model. Browser regression instructions are in `BROWSER_TESTING.md`.
