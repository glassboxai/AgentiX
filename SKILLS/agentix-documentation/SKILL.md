---
name: agentix-documentation
description: Maintain English Agentix architecture, installation instructions, change and incident records, and evidence-grounded local Ollama report drafts.
---

# Agentix documentation maintenance

Do not inspect or document content within the project's `generated_tools/`, and do not create tests for those artifacts. Documentation may explain Agentix's own storage/execution contracts without analyzing generated tool implementations.

Use code and raw verification evidence as the source of truth. Keep current behavior in `docs/DocumentacionTecnica.md`, proposals in `docs/specs/`, decisions in `docs/adr/` and changes in `docs/CHANGELOG.md`. Every incident needs status, trigger, cause, affected code, reproducer, proposed/implemented solution and verification. Never describe a proposed fix as implemented.

During approved code changes, write English module/class/function docstrings describing contracts, side effects, exceptions and relevant security/concurrency decisions. Add explanatory comments where useful. Keep installer and `docs/INSTALLATION.md` synchronized; do not claim an unimplemented installer exists.

For reports, run `tools/draft_report.py` with reviewed evidence JSON and local `qwen3:14b` when available. Request prose only. Review all factual claims against evidence, retain provenance and distinguish unverified draft from verified report. Never request code or tests from the local model. Record local-service failures and prepare a reviewed fallback report if needed.
