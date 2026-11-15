# AgentiX Four Week Project Proposal

Prepared 23 October 2026 | Plain-English revision: 25 October 2026 | All milestones pending

## What this project will achieve

AgentiX will help turn an everyday request, written in English, into a small working application. It will create the tools that do the work, give them simple screens, and connect those screens into a useful sequence.

A software engineer will stay in control. The engineer will review the requirements, generated code, tests and results before accepting the work. The goal is a **supervised pilot that demonstrates this process**, rather than a system that can build any application without help.

The existing repository will provide the starting point. Its supporting features will be checked again during the project. Everything in this proposal will remain work to be completed and approved; no milestone will be considered finished at kickoff.

## A simple example

A user might ask:

> “Create an application that counts the words in a document, labels it as short or long using a limit I choose, and presents the result clearly.”

AgentiX will aim to build three connected screens:

1. **Count words:** enter text and calculate its word count.
2. **Check the limit:** use that count to classify the document.
3. **Present the result:** produce a clear summary of the outcome.

Each small screen is a **widget**. The calculation behind it is a **tool**. The project will demonstrate how AgentiX creates these parts, checks them and joins them together. The actual two pilot examples will be agreed in Week 1.

## What will be delivered

The pilot will include three new agent roles:

| Role | What it will do |
| --- | --- |
| Widget Designer | Turn an approved tool into a small, usable screen with suitable fields, buttons and results. |
| Assembler | Connect approved widgets so that the result of one step becomes the input to the next. |
| Supervisor / Executor | Arrange checks, start the application in a controlled way, report problems and coordinate reviewed corrections. |

The delivery will cover **three supported widget patterns** and **two complete example applications**. Each application will contain two or three widgets. Supported controls will include text fields, numbers, checkboxes and lists of choices, with readable text or tables as results.

The pilot will handle one application-building operation at a time for just one user.

## Schedule and effort

The project will take **four working weeks: 20 working days**.

An indicative calendar is **27 October to 23 November 2026**; dates and reviewer availability will be confirmed at kickoff.

| Milestone | Target | Main result | Status |
| --- | --- | --- | --- |
| M1 — Agree the foundations | End of Week 1 | Approve the pilot examples, working rules and safe way to run the application. | Pending |
| M2 — Create individual widgets | End of Week 2 | Demonstrate three reviewed and tested widget patterns. | Pending |
| M3 — Connect and supervise | End of Week 3 | Demonstrate a connected application and a controlled correction process. | Pending |
| M4 — Accept and hand over | End of Week 4 | Complete the two pilot examples and deliver the evidence and operating guide. | Pending |

### Week 1 Agree the foundations

The work will focus on checking the starting point and deciding exactly what the pilot will support.

- Check normal startup, the existing agent workflow, browser and command-line operation, human approvals, user separation and safe tool execution. Investigate the known startup/tracking problem and agree a tested startup policy.
- Agree the information each tool and widget needs, the results it must produce, and which combinations are allowed.
- Choose the two pilot examples and write down their expected results before development.
- Make the safe-execution decision, as explained below, then finish the detailed design around that decision.

### Week 2 Create individual widgets

The Widget Designer will be developed and connected to the existing tool services.

- Generate three supported widget patterns for engineer review.
- Make every control clearly labelled and easy for automated browser tests to find.
- Check that buttons actually call the intended tool, produce the expected result and explain invalid inputs. Prevent accidental duplicate submissions while work is running.
- Run one supervised generation trial with the real local AI model and record any manual corrections.

### Week 3 Connect and supervise

The Assembler and Supervisor will be developed to turn individual widgets into an application.

- Connect two or three approved widgets and check that their inputs and outputs fit together.
- Start a temporary application, confirm it is ready, and run browser checks.
- Report failures clearly and support reviewed corrections, cancellation and cleanup.

### Week 4 Accept and hand over

The final week will focus on reliability, complete examples and practical handover.

- Fix release-blocking problems and repeat the checks for user separation, approvals, input/output validation and recovery after failures.
- Complete two supervised trials from ordinary English requests using the real local AI model, including one three-widget application.
- Deliver the source, repeatable test instructions, results, troubleshooting guide, known limitations and next-step priorities.
- Demonstrate the pilot and review the evidence.


## How safety and human review will work

Generated software will be treated as untrusted. An engineer will review its requirements, code, tests and expected results. If an approved part changes, the relevant approval and checks will need to be repeated.

The recommended pilot will build screens through a trusted application using checked descriptions of the widgets and their connections. Generated tool calculations will run through the existing isolated execution service. Generated screen code will still be available for inspection and export, but it will not automatically be run inside the main application.

If directly running newly generated screen code is essential, a separate safe way to host it must first be demonstrated. Direct execution of arbitrary generated screen code is not an unconditional four-week promise.

Applications will be available only on the local computer, without public sharing. Test launches will stop only the processes they own. Error records and activity logs will be kept for troubleshooting, with sensible limits.

A failing operation may receive **at most two proposed repair attempts**, within an agreed time limit. Each changed item and changed test expectation will need engineer approval before another run. Rejection will stop the operation; the system must not keep trying automatically or change an expected answer merely to make a test pass.

## How we will decide the pilot is ready

| Area | Evidence required |
| --- | --- |
| Correct inputs and outputs | Reject the wrong kind of value, values outside the agreed limits, missing information and unsuitable connections. Check returned results as well as submitted inputs. |
| Working widgets | Test all three patterns with ordinary values, exact limits and invalid inputs; observe the actual tool result. |
| Working connections | Test two-step and three-step applications, repeated widgets, failed earlier steps and old results that must not be reused. |
| Human control | Demonstrate editing, approval and rejection, renewed checks after changes, and a stopped operation after rejection. |
| Safe startup and shutdown | Demonstrate readiness checks, failed startup, cancellation, timeout and cleanup without stopping unrelated applications. |
| Browser usability | Run at least **10 repeatable desktop browser scenarios**, with **two representative scenarios also tested at a narrow screen width**. Include clear labels and accessibility checks. |
| Repeatability | Run the same browser test set **three consecutive times** without unexplained intermittent failures. |
| Independent checking | Compare actual results with expectations approved outside the generated program. A generated test report cannot declare itself authoritative. |
| Real AI trials | Complete two engineer-supervised examples with **qwen3-coder:30b**, recording attempts, time taken, failures and manual corrections. First-attempt success is not guaranteed. |
| Handover | Deliver source, test evidence, screenshots, logs, operating instructions, known limitations and the acceptance decision. |

The examples will use calculations or rules with clearly checkable answers. If summarization or translation is included, the connections can be tested automatically, but language quality will need separate human review.

## What the project needs and what could affect delivery

The project will need a Windows workstation with enough capacity for the local Ollama service and **qwen3-coder:30b**, plus a browser supported by **Playwright**, the automated browser-testing tool. Availability and actual model response times will be checked at kickoff.

| Risk | Planned response |
| --- | --- |
| The proposed application cannot be run safely | Use the demonstrated trusted-screen approach or replan. |
| AI responses are slow or inconsistent | Keep examples small, measure real response times early and limit repair attempts. |
| Screen connections or supporting libraries do not work as expected | Use fixed compatible versions and test the connections before expanding the pilot. |
| Reviews delay progress | Schedule regular decisions and agree an alternate reviewer if needed. Review delays beyond one working day will be raised with the owner. |


Distributed operation, broad performance optimization and production certification will remain outside the pilot.

## Working approach and final handover

Requirements and expected results will be agreed before implementation. Tests will be written to demonstrate the required behavior, and fixes will retain a test that detects the original problem. Each defect will have a recorded cause, correction and verification result.

Progress, remaining work and contingency will be reviewed weekly.

The handover will contain the three agent integrations, supported widgets, connected-application builder, supervision and startup/shutdown services, tests, two supervised example records, English documentation and a prioritized follow-on backlog. Approving this proposal will agree the planning direction; implementation changes will still follow the project's approved-change process.

### Brief implementation note

The engineering design will use Gradio for screens, Pydantic and Annotated descriptions to define and check exchanged information, and Playwright for browser verification. Each screen control will have a stable `elem_id` so tests can find it reliably. Connections will be checked before use; later steps will run only after earlier steps succeed. Versions and reviewed files will be traceable, and changed or incompatible information will be rejected. These are implementation details supporting the outcomes above, not extra deliverables for the owner to specify.
