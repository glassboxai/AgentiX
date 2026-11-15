---
name: verification-before-completion
description: Make completion claims from fresh, relevant evidence.
---

# Verification Before Completion

Identify the check supporting each claim; run it, inspect exit status and actual output, and report failures/skips/xfails honestly. For code changes use the exact v5 interpreter, appropriate regressions, Ruff lint/format and source-reference freshness; add explicit framework/native/browser/model checks only as warranted. Never claim a simulated boundary is real isolation, a unittest report proves semantics, or a prior screenshot establishes current behavior. For documentation-only work verify scope, links and reference consistency without needless model/server runs. Compare against acceptance criteria and report unresolved limits, evidence provenance and whether a source fix is loaded in the live process. No live restart without explicit authorization.

AGENTS.md supplies shared exclusions, authorization and English-documentation rules; do not duplicate or override them.
