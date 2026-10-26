# AgentiX Four Week Project Proposal

Prepared 23 October 2026 | Planning proposal | 

## Project objective

Deliver a supervised local pilot that turns an English user request into validated software tools, reusable Gradio widgets and a connected application. A software engineer will approve the requirements, implementation, tests and acceptance evidence before release. The pilot will use local Ollama with qwen3-coder:30b for application agents and Playwright for widget and application verification.

The four-week commitment will be a bounded pilot, not a general-purpose autonomous software factory or a production security certification. The inital rpository is the starting point, and then will be necessary to revalidate the supporting services and concentrate implementation effort on the Widget Designer, Assembler and Supervisor extensions. All activities in this proposal will be treated as work to be performed and accepted during the project; no milestone will be assumed complete at kickoff.

## Milestone overview

| Milestone | Target | Planned effort | Reserve | Acceptance outcome | Status |
| --- | --- | --- | --- | --- | --- |
| M1 Foundation and execution decision | End of Week 1 | 4 days | 1 day | Approve contracts, threat boundary, fixtures and pilot scope | Pending |
| M2 Widget Designer | End of Week 2 | 4 days | 1 day | Generate and review three supported widget patterns with stable IDs | Pending |
| M3 Assembler and Supervisor | End of Week 3 | 4 days | 1 day | Assemble and verify a connected application with controlled repair | Pending |
| M4 Pilot acceptance and handover | End of Week 4 | 4 days | 1 day | Accept two supervised scenarios and deliver reproducible evidence | Pending |

## Delivery assumptions

- Allocate one senior Python and AI engineer for 20 working days at eight hours per day: 160 hours in total. Allocate 16 days to planned work and four days to contingency, defect correction and integration: a 20 percent reserve.
- Require the product owner or reviewing software engineer to provide approximately 30 minutes of review per working day, with milestone decisions within one working day. This review capacity will be additional to the engineering estimate.
- Use a Windows development workstation, an operational Ollama service, qwen3-coder:30b and an installed Playwright browser. Confirm hardware capacity and model availability at kickoff; do not assume model response times from deterministic tests.
- Plan four consecutive working weeks. An indicative calendar will run from 26 October to 20 November 2026, subject to kickoff confirmation and reviewer availability. No weekend work will be assumed.
- Limit the pilot to one active assembly operation, workflows with two or three widgets and bounded JSON-compatible data. Preserve session separation for review and results.

## Scope and exclusions

Include tool requirements and implementation review; strict tool, widget and workflow contracts; native isolated tool execution; a local review GUI and CLI; the three agent extensions; controlled application startup and shutdown; independent acceptance checks; structured logs; regression tests; and English documentation.

Support text, numeric, boolean and bounded selection controls, with readable text or tabular outputs. Implement three widget patterns across these controls and two representative end-to-end workflows. Require deterministic operations for acceptance evidence; treat open-ended natural-language quality as a separate human review decision.

Exclude Docker, installer development, cloud hosting, public sharing, authentication redesign, arbitrary dependency installation, external integrations, unrestricted filesystem access, file uploads, cyclic graphs, arbitrary JavaScript, a visual drag-and-drop editor and unattended self-repair. Defer distributed agents, broad performance optimization and production deployment certification. Do not inspect or modify the project's existing generated_tools contents during engineering work; use independently authored temporary fixtures and separate temporary storage for approved live trials.

## Proposed architecture

### Tool contracts and validated handoffs

Define versioned Pydantic models for ToolDefinition, WidgetDefinition, WorkflowDefinition and ValidationReport. Use Annotated metadata on every supported tool parameter and return type to express descriptions, units, constraints and UI hints. Enforce runtime validation for both inputs and outputs; annotations alone will not enforce a contract. Configure strict validation, forbid unexpected fields, reject nonfinite numbers and bound text, collection sizes and nesting. Use a documented subset of JSON-compatible types and explicit adapters for structured model results.

Assign tool version, widget instance, schema version, artifact digest, owner and operation identity to every handoff. Reject incompatible schema versions, unknown component types, missing outputs, duplicate IDs and unapproved source changes. Validate metadata as data without evaluating generated annotations or importing untrusted modules on the host. Require fresh approval and verification when approved artifacts change.

### Widget Designer agent

Have the designer consume an approved ToolDefinition and emit two synchronized artifacts: a Python Gradio fragment for review/export and a validated WidgetDefinition for assembly. Require a Group or equivalent bounded container, explicit input/output mappings and deterministic elem_id values. Use a namespace such as ax_widget_instance_control so two instances of the same tool cannot collide. Provide accessible labels as well as IDs. Bind callbacks through the maintained tool-execution gateway, rather than through an unrestricted function reference embedded in generated code.

### Assembler agent

Have the assembler translate the original user request into an acyclic workflow of two or three approved widget instances. Require a WorkflowDefinition containing nodes, typed ports, explicit connections and a component-ID map, plus the corresponding Python Blocks source. Check port compatibility before rendering and reject ambiguous mappings, silent coercion, cycles and missing dependencies.

Sequence downstream work only after successful upstream completion. A second independent click handler on the same button will not provide that guarantee. Use a success-dependent event chain supported by the pinned Gradio version, or a maintained orchestration callback that awaits and validates the upstream result before invoking the next stage. Keep each user's intermediate values separate and prevent stale results from an earlier operation from advancing a new workflow.

### Supervisor and Executor agent

Have the supervisor review artifact structure, request schema checks, prepare proposed Playwright tests and manage a disposable application server through maintained lifecycle services. Let host-owned checks decide whether validation passes; do not allow the supervisor or generated tests to declare their own success authoritative. Return structured diagnostics to the assembler, identify the affected node and preserve the failing artifact and trace.

Allow at most two proposed repair attempts per operation within a fixed time budget. Require engineer review of each changed artifact and test expectation before rerunning it. A human rejection will stop the operation without automatic reprompting. On timeout, cancellation, failed verification or exhausted attempts, stop the owned process tree, report the failure and retain bounded evidence. Never weaken an expected result just to obtain a pass.

## Execution boundary decision

Resolve the highest-risk dependency by Day 3. A short-lived, standard-library tool sandbox and a long-lived Gradio server with dependencies and a listening socket will require different capabilities. Syntax checking, allowlisted imports, Pydantic and ordinary subprocesses will not by themselves provide operating-system isolation.

The recommended four-week delivery path will run a maintained Gradio renderer from validated WidgetDefinition and WorkflowDefinition data. It will invoke generated business logic only through the native isolated tool gateway. The designer and assembler will still produce Python source for engineer inspection and export; the host will not dynamically import or exec that generated source. The supervisor will launch the maintained renderer and verify the resulting interface with Playwright.

If executing the generated Gradio Python itself is mandatory, first prove a separate native execution boundary for approved dependencies, loopback communication, filesystem restrictions, resource limits, process cleanup and session isolation. Do not silently run that code on the host if the proof fails. By Day 3, the owner will either approve the schema-driven pilot path, accept a demonstrated isolated generated-server path, or rebaseline scope and time. Direct execution of arbitrary generated Gradio code will not be an unconditional four-week commitment.

Launch only owned loopback servers with public sharing disabled and readiness checks before testing. Keep reviewed expectations outside untrusted processes and revoke authorization when code or contracts change. Preserve bounded diagnostics and verbose activity.

## Week 1 Foundation and execution decision

**Planned effort 4 days plus 1 reserve day.**

Prioritize the feasibility spike before completing detailed contracts so the architecture decision can be made by Day 3; finish the contract details against the selected runner afterward.

1. Establish and revalidate modular Python architecture, the Manager to Architect to Coder to Tester workflow, GUI/CLI compatibility, session ownership, approval lifecycle, stage handoffs, isolated execution and regression commands. Reproduce the telemetry-related normal-startup failure and specify a tested startup policy. Allocate 0.75 day.
2. Specify strict input/output schemas, Annotated metadata, widget IDs, typed connections and rejection rules. Pin compatible Gradio, Pydantic and Playwright versions. Allocate 1 day.
3. Time-box the native generated-server feasibility spike and demonstrate the maintained renderer alternative. Record the boundary decision by Day 3. Allocate 1.5 days.
4. Approve observable acceptance cases, two pilot scenarios, component limits and a traceability matrix linking requirements to tests and milestones. Allocate 0.75 day.

**M1 acceptance:** obtain owner approval of the execution architecture; pass the supporting regression baseline or explicitly resolve blocking failures; demonstrate rejection of malformed schemas and incompatible ports; and freeze the pilot scope. Stop or replan if no safe execution path can be demonstrated. Do not spend later weeks compensating for an unresolved boundary decision.

## Week 2 Widget Designer

**Planned effort 4 days plus 1 reserve day. Dependency M1.**

1. Implement the designer's prompt, structured response parsing, reviewed Python fragment and matching WidgetDefinition. Cover three component patterns and deterministic unique IDs. Allocate 2 days.
2. Integrate the maintained renderer, approved tool bindings and strict input/output gateway. Show validation failures as actionable UI messages and prevent duplicate submission while a callback is running. Allocate 1 day.
3. Write and execute unit, adapter and Playwright tests for each pattern; conduct one real qwen3-coder:30b supervised widget-generation trial and record every manual correction. Allocate 1 day.

**M2 acceptance:** generate and review three widget patterns; locate every interactive control through its documented elem_id; verify normal, boundary and invalid-input behavior; instantiate the same widget twice without ID collision or shared state; and show that rejected/unapproved artifacts cannot execute. Retain proposed and approved tests separately. Do not count a rendered form as proof that its tool callback works.

## Week 3 Assembler and Supervisor

**Planned effort 4 days plus 1 reserve day. Dependencies M1 and M2.**

1. Implement the assembler's typed acyclic graph, original-query preservation, port checks, widget-instance namespaces and generated Blocks source. Allocate 1.5 days.
2. Implement supervisor validation, readiness/health checks, disposable server launch, controlled browser execution, cancellation and process cleanup. Allocate 1.5 days.
3. Integrate structured diagnostics, the bounded repair loop, mandatory rereview and host-owned acceptance verdicts. Allocate 1 day.

**M3 acceptance:** assemble a two-widget workflow; verify that widget B receives the new successful output of widget A, not an earlier or empty value; prevent B from running after an upstream failure; reject an incompatible connection; and demonstrate a failing GUI test being reported, reviewed and rerun against a corrected artifact. Show that rejection, cancellation and startup failure leave no owned application server running.

## Week 4 Acceptance and handover

**Planned effort 4 days plus 1 reserve day. Dependency M3.**

1. Harden session separation, output validation, invalid-schema handling, stale approvals, loopback launch and failure recovery. Run repeated deterministic GUI scenarios and fix release blockers. Allocate 1.5 days.
2. Execute the regression gates and two supervised qwen3-coder:30b end-to-end trials from ordinary English requests, including one three-widget workflow. Allocate 1.5 days.
3. Update English architecture, agent contracts, runbook, operator review guide, incident register and known limitations. Package reproducible test commands, pinned dependencies and traces. Allocate 0.75 day.
4. Demonstrate the pilot, review evidence with the owner and agree the post-pilot backlog. Allocate 0.25 day.

**M4 acceptance:** obtain engineer signoff against the final criteria below; deliver the source snapshot and evidence; and leave no unresolved blocker that permits unauthorized execution, cross-session leakage or unsupported success claims. Defer cosmetic or nonessential enhancements rather than consuming the safety and acceptance gates.

## Final acceptance criteria

| Area | Evidence to obtain before acceptance |
| --- | --- |
| Strict contracts | Reject string-to-number coercion, boolean-as-number confusion, nonfinite values, unexpected fields, duplicate IDs and incompatible typed ports; validate outputs too |
| Widget behavior | Cover all three patterns with normal, exact-boundary and invalid inputs; prove callback execution through observed results |
| Workflow sequencing | Test two-node and three-node chains, duplicate widget instances, upstream failure and stale intermediate values |
| Human oversight | Demonstrate review/edit/approve/reject, artifact-change invalidation and a stopped repair operation after rejection |
| Supervisor lifecycle | Observe startup readiness, cancellation, timeout, failed launch, bounded output and cleanup of only the owned server |
| Browser testing | Run at least 10 deterministic GUI scenarios at desktop width, with two representative scenarios repeated at a narrow width; use stable IDs and accessibility assertions |
| Repeatability | Run the deterministic GUI pack three consecutive times with no unexplained intermittent failure; use bounded auto-retrying assertions rather than fixed sleeps |
| Independent correctness | Compare reviewed deterministic expected results in maintained host code; keep generated unittest and Playwright reports provisional until reviewed |
| Live generation | Complete two engineer-supervised qwen3-coder:30b scenarios; record attempts, latency, failures and manual corrections without promising first-attempt model success |
| Release evidence | Run offline, real-framework, native-isolation and disposable-browser gates appropriate to the change; retain logs, traces, screenshots, artifact identities and a signed decision |

Use a deterministic fixture such as a text statistics widget feeding a threshold classification widget, optionally followed by a result-formatting widget. The owner will approve the actual scenarios in Week 1. If a workflow uses summarization or translation, verify connections and execution deterministically, then assess content quality separately through reviewed examples; do not pretend that an exact string comparison proves language quality.

## Risks and scope controls

| Risk | Planned response | Decision trigger |
| --- | --- | --- |
| Generated server cannot be safely hosted | Prove the boundary early; prefer the maintained schema-driven renderer | Day 3 architecture decision |
| Local model latency or inconsistent artifacts | Keep schemas small, bound retries, measure real latency and schedule supervised trials early | More than one reserve day consumed in a week |
| GUI events or dependencies diverge | Pin versions; test success sequencing and adapter construction before expansion | A core handoff fails its regression gate |
| Reviewer unavailability | Schedule daily decisions and nominate an alternate reviewer | Approval waits exceed one working day |
| Reserve is consumed | Defer extra widget patterns, cosmetic changes and additional scenarios | Forecast exceeds 20 working days |

Do not cut authorization, native tool isolation, output validation, mandatory review, error reporting or independent acceptance to recover schedule. If those gates cannot be met, report an incomplete pilot rather than declare a production-ready release. Additional staffing may improve parallel delivery, but this estimate will not assume it. No monetary budget will be committed without an agreed engineering rate.

## Governance and handover

Use specification-driven development and test-driven development: approve observable requirements, capture a failing reproducer, implement the change and retain passing regression evidence. Record each defect's cause, correction and test. Review progress and remaining reserve at the end of each week. Treat changed agent contracts or execution boundaries as scope decisions requiring explicit owner approval.

Deliver a reviewed proposal and requirements matrix, architecture decision, strict schemas, three agent integrations, supported widget patterns, typed assembler, supervisor lifecycle services, regression and Playwright suites, two supervised scenario records, English documentation and a prioritized follow-on backlog. Keep every work item and milestone pending until its evidence is accepted. Acceptance of this planning document will authorize planning direction only; production changes will remain subject to the project's approved-block process.

## Technical references

Consult the pinned installed versions as the implementation authority. Use these official references to validate the design during Week 1:

- Gradio Blocks and event sequencing: https://github.com/gradio-app/gradio/blob/main/guides/03_building-with-blocks/01_blocks-and-event-listeners.md
- Gradio component elem_id: https://www.gradio.app/docs/gradio/button
- Pydantic strict mode: https://pydantic.dev/docs/validation/2.12/concepts/strict_mode/
- Playwright locators: https://playwright.dev/python/docs/locators
- Playwright auto-waiting and assertions: https://playwright.dev/python/docs/actionability
