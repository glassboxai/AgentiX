# IAC-010: explicit V7 runtime and artifact roots

Status: implemented, pending the reviewed operator `Plan`/`Apply` installation.

## Current behavior

The schema-1 infrastructure profile derived its managed runtime root and tool
catalog from the legacy `AgentiX/v5` user-local namespace. The launcher then
overrode `AGENTIX_HOME` and `AGENTIX_TOOLS_ROOT` with those derived paths.

## Approved behavior

The schema-2 reviewed profile declares two absolute local paths:

- `home`: `D:\\AI\\Agentix-data\\v7`, the exclusive managed runtime and
  application-state root.
- `toolsRoot`: `D:\\AI\\AgentiX_v7\\generated_tools`, the separate catalog
  root for generated tool and application artifacts.

The application keeps drafts, approvals, application packages, profiles and logs
below `home\\data`; only public generated tool artifacts use `toolsRoot`. The IaC
plan fingerprints both values. It rejects missing or unknown fields,
relative paths, parent traversal, volume roots, UNC paths, existing reparse
points, a runtime root overlapping the checkout, and a runtime root overlapping
the artifact root. No V5 data is read, moved, deleted or adopted. A stale
location receipt cannot redirect a schema-2 launch: it must match the current
configured home exactly.

## Acceptance criteria

| ID | Observable criterion | Evidence |
| --- | --- | --- |
| IAC-010-01 | The checked-in profile declares schema 2 and the two approved absolute roots. | `test_checked_in_schema_two_configuration_declares_approved_roots` |
| IAC-010-02 | `Get-IacPaths` derives runtime/launcher/environment paths below `home` and artifacts from `toolsRoot`. | `test_schema_two_configuration_selects_separate_home_and_artifact_roots` |
| IAC-010-03 | Relative and overlapping roots fail before planning, provisioning or launch. | `test_schema_two_configuration_rejects_relative_roots`; `test_schema_two_configuration_rejects_overlapping_runtime_and_artifact_roots` |
| IAC-010-04 | The owner receipt records only the reviewed schema-2 runtime root. | `test_location_receipt_binds_the_configured_deployment_root` |
| IAC-010-05 | Drafts remain below `home/data` when public artifacts use an external root. | `test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout` |
| IAC-010-06 | Launch continues to set both environment variables only for its owned process and restores them afterward. | Existing `test_launcher_preserves_absent_environment_variables` plus offline IaC tests |

## Compatibility and residual risk

Schema 1 is intentionally rejected: V7 starts clean rather than silently
adopting the V5 namespace. The former V5 directory remains untouched and can
be retained for rollback or removed only through a separate user-authorized
data-retention action. Native AppContainer profiles remain Windows-managed
temporary execution state; their cleanup receipts now reside below the V7
runtime home after installation. Offline tests exercise planning and path
validation only; they do not provision dependencies, launch the GUI or prove a
clean-Windows installation.
