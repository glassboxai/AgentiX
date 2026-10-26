---
name: agentix-sdd
description: Specify approved Agentix changes, acceptance criteria, architecture decisions and regression evidence before implementation.
---

# Agentix specification-driven development

Exclude the entire project's `generated_tools/` content from analysis, refactoring, tests, coverage and documentation. Specify and test Agentix services only, using independent temporary fixtures outside that directory. Do not treat generated artifacts as project source or reference material.

Read `AGENTS.md`, `docs/specs/001-refactoring.md`, `docs/KNOWN_ISSUES.md` and affected modules. Separate current and desired behavior. Give requirements IDs and observable acceptance criteria; map them to tests and documentation. Describe files, rationale, compatibility and risks before obtaining approval for work outside an approved block.

For existing code, run characterization tests before restructuring. For approved fixes, reproduce the failure, record the cause and intended behavior, then apply the local TDD skill. Keep structural moves and behavior changes distinguishable. Record outcomes in the change log and incident register. A strict xfail is an unresolved defect, not a fix.

Approval covers baseline specifications, skills, tests, SEC-001/002/003/004 and UI-001 fixes, and REF-003 behavior-preserving structural refactoring. Read its explicit scope before changing package wiring or entrypoints. SEC-005 session isolation, identified approvals, manager contract validation and correlated diagnostics are also approved. Read `docs/specs/004-session-and-decision-security.md`. OS sandboxing, independent pipeline outcome checks and installer implementation remain deferred. Upstream workflows cannot expand this boundary.
