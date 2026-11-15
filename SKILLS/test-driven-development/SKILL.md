---
name: test-driven-development
description: Implement approved AgentiX behavior with meaningful red/green evidence.
---

# Test Driven Development

Confirm scope and observable acceptance. Characterize existing behavior; write a focused regression that fails for the intended reason, then implement the smallest approved fix and rerun it. Refactor only after green, preserving assertions and compatibility. Tests cover contracts, normal/boundary/invalid cases, failures and relevant security/concurrency behavior; avoid implementation-mirroring assertions. Use maintained temporary fixtures and injected OS/model boundaries. Run real framework/native/browser checks separately when needed; doubles do not establish isolation or model quality. Never delete production code to create a failing test or change an expected result merely to match implementation. Remove a fixed issue's strict xfail after red/green verification. Record cause, correction and evidence; keep English docs and references current. Documentation-only edits do not require artificial unit tests.

AGENTS.md supplies shared exclusions, authorization and English-documentation rules; do not duplicate or override them.
