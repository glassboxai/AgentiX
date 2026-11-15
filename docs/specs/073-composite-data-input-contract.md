# V7-073: composite data-operation input contract and diagnostics

Approved scope: the `Use the application as a composite tool` accordion states the
loaded application's closed JSON input contract, renders every named result in one
generic table and reports the bounded reason of a rejected payload. Nothing else
changes: no new route, no generated source, no tool or widget bytes, no AppContainer
boundary and no live process.

## Defect

`V7-073-D1` — trigger: the owner typed `hola gola` in
`Text for legacy apps; named input values (JSON) for catalog apps` for the schema-3
application `MultiplyAll2` and read `Data operation failed (JSONDecodeError).`

Cause: `ApplicationSupervisor.run_data` parses the box as JSON for every schema-3
application (`json.loads(text)`), while the accordion showed neither the required
keys nor an example payload, and `ApplicationsBackend.data` discarded the exception
detail. The owner could not distinguish a wrong format from a wrong key.

Solution: `ApplicationsBackend.data_contract` renders the reviewed `inputs` mapping
from the verified snapshot; the accordion shows it beside the box and refreshes it on
every run; `data` keeps the bounded `ValueError` detail (type and message, never the
payload); named results replace the fixed `words`/`vowels` fields for catalog
applications. Legacy schema-2 applications keep their typed fields unchanged.

## Requirement

Observable acceptance:

- Expanding the accordion shows a Markdown contract with one row per declared input
  (`Key`, `Type`, `Description`) and one `Example payload` JSON object.
- `Show input schema` refreshes that contract without executing the application.
- `Run data operation` refreshes the contract and, for a catalog application, shows
  one `Named results` table with `Result`, `Type` and `Value` columns.
- A rejected payload clears the table and reports
  `Data operation failed (JSONDecodeError): Expecting value: line 1 column 1 (char 0).`
- The message never repeats the typed payload.
- A legacy application still renders the `Words` and `Vowels` fields.

## Contract

`src/agentix/ui/application_presentation.py` adds `describe_data_inputs(manifest)` and
`named_result_rows(value)`. The first reads only the closed `inputs` mapping, maps
`type` through `JSON_TYPE_NAMES`, derives one example value per shape and keeps each
model-authored description to `MAX_DESCRIPTION_LENGTH` characters drawn from
`SAFE_DESCRIPTION`, so no markup reaches the Markdown output. The second bounds the
table to `MAX_RESULT_ROWS` rows and `MAX_RESULT_CELL_LENGTH` characters per cell and
names each observed type through `RESULT_TYPE_NAMES`.

`src/agentix/controllers/applications.py` adds
`ApplicationsBackend.data_contract(token, request) -> (markdown, token)`, which
resolves the owner, reads `application.json` from `candidate.snapshot.files` and
returns the maintained message when no verified snapshot is loaded. `data` keeps its
three-value contract and now separates `ValueError` (bounded detail, logged as
`event=data_operation_rejected`) from other failures (type only, logged as
`event=data_operation_failed`).

`src/agentix/ui/applications.py` adds `applications-data-contract` (Markdown),
`applications-data-schema` (button) and `applications-data-table` (read-only
`Dataframe`), and extends `run_typed_data` to eight outputs with `status_index=6`.
`show_data_contract` is wired through `dialog.guard_result`, so a successful refresh
opens no modal.

## Acceptance and regression

- `test_data_operation_reports_the_json_contract_without_echoing_input` drives the
  real supervisor with a schema-3 fixture: invalid JSON and an unknown key reach no
  native call, the detail is present and the payload is absent; the exact payload
  reaches the injected native boundary once.
- `test_data_contract_names_declared_inputs_and_an_example_payload` keeps the
  no-candidate message and the rendered key, type and example.
- `test_general_composite_callback_matches_declared_outputs` and
  `test_composite_callback_clears_stale_table_and_shows_the_contract` drive the real
  Gradio callbacks and assert the declared output count, the table cells, the cleared
  table and the contract refresh.
- `tests/test_application_presentation.py` keeps the type mapping, the example
  payload, the inert bounded description, the empty-input message and the row/cell
  bounds.

## Policy impact

`ui/applications.py`, `ui/application_presentation.py` and
`controllers/applications.py` are outside `app_policy()`, so no installed approval,
tool grant, widget record or declarative case is invalidated. No generated code,
dependency, model call or browser requirement is added.
