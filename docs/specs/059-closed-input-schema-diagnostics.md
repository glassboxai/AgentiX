# V7-059: closed public input schema diagnostics

## Observed defect

Creating `SuperRepeater` with the description "Create an application which takes
a text as input. Then it repeats that text a given number of times. Finally
returns the number of vowels in the text with the repeated input text." and
accepting only `count_vowels` and `repeat_word_tool` produced no application and
the status line `Application generation failed (ValueError). Evidence retained;
no retry or approval occurred.`

The log recorded `candidate_accepted count=2`, both `candidate_selected` events,
`application_tools_resolved tools=['count_vowels', 'repeat_word_tool']`,
`application_model_started`, `stage=application_plan event=crew_started tasks=2`
and `crew_finished` after 84 to 89 seconds, then `application_generation_failed
error_type=ValueError`. The `application_widgets` stage was never reached. Three
attempts on 2026-11-11 failed identically.

## Cause

The plan task returned a public input schema carrying a JSON Schema numeric
bound:

```json
"repeat_count": {"type": "integer", "description": "...", "minimum": 0}
```

`validate_input_shape` accepted only `type`, `description`, `enum` and `items`,
so `validate_catalog` raised `ValueError("Unsupported application input schema")`.
`ApplicationCode.inputs` is typed `dict[str, dict[str, Any]]`, so pydantic let the
extra key through and the rejection happened only in the host contract check.

The model did not hallucinate: `repeat_word_tool` declares "Must be a non-negative
integer" and "ValueError: If count is negative", so the planner translated the
approved tool contract into canonical JSON Schema. The plan prompt only said
"scalar or array JSON schemas" and never listed the closed keys, and the
integrator task returned the planner's `inputs` unchanged in all three drafts.

The controller reduced every non-`CatalogDependencyError` exception to its type
name, so the owner saw `(ValueError)` without the rejected key.

## Solution

- `src/agentix/adapters/application_crewai.py`: the plan prompt now lists the
  closed keys `type`, `description`, `enum` and `items` and forbids `minimum`,
  `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `pattern`, `format`,
  `multipleOf`, `minLength`, `maxLength` and any other JSON Schema keyword,
  stating that numeric bounds belong to the approved tool contract. The
  integrator task inherits the text because it extends the same request.
- `src/agentix/domain/application_code.py`: `ApplicationContractError(ValueError)`
  and `unsupported_input_keys()` build a closed message naming the input identity
  and the sorted rejected keys plus the allowed list. The contract is not
  relaxed: `minimum` is still rejected.
- `src/agentix/controllers/applications.py`: the generation failure line
  propagates the text only for `CatalogDependencyError` and
  `ApplicationContractError`; every other `ValueError` keeps its type name. A
  dedicated type is required because `pydantic.ValidationError` subclasses
  `ValueError` and its message embeds the offending value, which would leak model
  or user payload into the owner-facing status line and the event log.

Accepting numeric bounds in the public input schema is deliberately out of scope;
it would touch the shared value validator, the native template, the acceptance
case generator and the browser comparison, and would duplicate the validation the
approved tool already performs.

## Evidence

- `tests/test_code_application.py`: a bound is rejected with a message naming the
  input and the key, every unsupported key is listed in sorted order, the rejected
  value never appears in the message, and the four documented keys plus arrays
  still validate.
- `tests/test_application_crews.py`: the persisted `plan-request.json` carries the
  closed key list and the forbidden keywords, and `connect-request.json` extends
  the same system text.
- `tests/test_applications_backend.py`: an `ApplicationContractError` reaches the
  owner with its bounded reason, without the type name and with the retained
  evidence sentence.

Offline suite, Ruff lint/format and `tools/build_reference.py --check` pass. No
live model run, browser check or process restart was performed; the live
`SuperRepeater` confirmation with the original description remains pending an
authorized launch.
