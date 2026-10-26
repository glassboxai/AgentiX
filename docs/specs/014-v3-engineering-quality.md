# V3-001 Engineering quality and curated release

Status: approved by the user request to create AgentiX_v3 on 2026-10-23.

Preserve GUI/CLI behavior, qwen3-coder:30b, manual acceptance, session ownership
and native execution isolation. Preserve the original AgentiX_v2 copy. Omit only
obsolete alternatives, caches, root runtime logs, nonportable environments and
intermediate document authoring/rendering artifacts from the new release. Never
traverse existing generated_tools. Keep historical audit reports and active
compatibility facades. Record omissions in a copy manifest.

V3-01: enforce Ruff and documented SRP/OCP/DRY/LoD/SOLID/IoC/DI decisions.
V3-02: expose an execution-backend protocol and inject it at the composition root;
all owner services receive the same backend, with no host execution fallback.
V3-03: disable Gradio analytics at explicit process startup to prevent the observed
normal-launch theme comparison failure and avoid analytics requests.
V3-04: publish module/class/method/variable reference documents with source-bound
freshness and inventory checks. Never include secret values. Include English
contracts and semantic guidance, and keep all maintained production docstrings.
V3-05: provide reproducible Unit, Integration, Functional and Regression Testing
commands, requirements validation and release evidence without claiming universal
correctness or new model quality from deterministic tests.
V3-06: identify the curated release as 3.0.0 while preserving the agentix import
package and active root compatibility modules.

Write failing regressions first. Re-run offline, framework, native-isolation and
disposable browser checks; update architecture, incidents and change log together.
The four-week proposed Widget Designer/Assembler/Supervisor features remain a
proposal and are not implemented by this maintenance release. No installer or
Docker work is authorized. Use the v2 interpreter for verification without copying
its environment; document clean-environment installation separately.

## Implementation and verification

Implemented in the curated 3.0.0 checkout. The final offline suite passed 322 tests; all 19 explicitly selected integrations passed. Ruff lint/format and source reference freshness passed. See `../reports/V3_ENGINEERING.md` for evidence and limitations. The installed v2 interpreter was used; a fresh-environment installation remains unverified.
