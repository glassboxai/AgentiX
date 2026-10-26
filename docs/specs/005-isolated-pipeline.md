# EXEC-002 / FLOW-002: native execution and observed pipeline outcomes

Status: execution-isolation implementation verified, 2026-10-19. Its initial outcome gate is superseded by ACCEPT-001 (`006-human-acceptance.md`): unittest success is provisional and final authorization requires human-reviewed host comparisons. Docker is rejected; installer deferred. Historical evidence: `../reports/ISOLATED_PIPELINE.md`; current evidence: `../reports/HUMAN_ACCEPTANCE.md`.

## Scope and acceptance criteria

- EXEC-02: use Windows AppContainer with no network capabilities and a Job Object. Never fall back to host execution. Launch suspended, validate the child token and assign resource limits before resuming. Terminate the job on timeout, excessive output or host handle closure.
- EXEC-03: copy only an application-owned Python runtime and the two explicitly requested artifacts to a disposable workspace. Grant the unique AppContainer SID read access to the runtime and workspace; do not grant access to the project. Do not inherit host environment secrets or handles other than output pipes. Existing Windows resources explicitly accessible to AppContainers remain subject to Windows policy; this is not a virtual machine.
- FLOW-02: only the application test service can publish an in-memory result. Require a successful isolated process, a valid structured report, at least one executed test, and no failures/errors/skips/expected failures. Independently compile exact source/test snapshots without execution. Bind evidence to the owner, operation, and exact code/test bytes. Clear evidence before every attempt. The manager's prose never grants verification.
- FLOW-03: gate both the final manager stage and tool execution against current evidence; reject missing, stale, changed or foreign evidence. Never import generated code in the host process.
- EXEC-04: use independently authored temporary fixtures only. Default tests remain offline; native Windows tests are explicit opt-in and must verify real access restrictions. Never access the project's excluded artifact directory or restart the live app.

## Limits and compatibility

The initial sandbox supports standard-library Python functions and unittest. Third-party dependencies and filesystem/network side effects are unavailable. Resource defaults: 30 seconds, 512 MiB job memory, eight processes, 256 KiB combined output. A copied runtime is disposed after every invocation; cold startup has additional overhead. Unsupported platforms and provisioning failures deny execution.

Structured unittest reports describe observed execution, not semantic correctness. Generated Python shares the interpreter with unittest and can deliberately forge its own report or alter the framework. This implementation does not attest malicious test honesty. Host-observed isolation/exit/limits and content hashes are separate from these untrusted test claims. Independent human-authored acceptance tests remain necessary for stronger assurance.

## Changes

Add native process/workspace and sandbox protocol modules, a per-runtime verification ledger, and tests. Replace host import/subprocess execution in execution/testing services, connect the shared ledger in composition, and gate orchestration. Update architecture, incidents, changes and verification evidence in English. No installer implementation or changes to generated artifact contents are authorized.
