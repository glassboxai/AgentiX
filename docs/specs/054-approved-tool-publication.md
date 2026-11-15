# PUB-001: approved tool publication

Status: implemented pending full offline verification.

## Requirement

`data/tools` contains only tools that completed the current human acceptance
gate. Specifications, code and tests proposed during creation or repair remain
under `data/drafts/<owner>/<operation>/<tool_name>`.

## Acceptance criteria

- A proposal never creates a public tool directory before acceptance succeeds.
- Publication copies exact bounded reviewed specification, code and test bytes
  into a new public directory and never overwrites an existing one.
- Failed, rejected or incomplete work restores public-catalog access and retains
  its draft for evidence/repair.
- Creation and repair execute only public bytes after publication.
- The approval policy fingerprints the storage facade and publication service,
  invalidating prior durable tool grants.

## Limits

Directory publication is not claimed crash-atomic. Existing applications and
widgets are not migrated by this change; their dependency checks continue to
require current tool grants.
