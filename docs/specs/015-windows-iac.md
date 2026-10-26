# IAC-001: native per-user Windows desired state

Status: approved plan, 2026-10-24; implementation evidence tracked separately.

The approved block adds WinGet, DSC and PowerShell Plan/Apply/Test operations,
without Docker, elevation, automatic startup, or restarting existing applications.
Retain Python 3.11.9 and ollama/qwen3-coder:30b. The old Python release is an explicit
user choice, not a claim that its security limitations are resolved.

IAC-01: Plan is non-mutating except an explicitly requested plan output document.
Bind configuration, maintained infrastructure source and observed preconditions;
Apply rejects stale or altered actions. Unknown configuration fields fail closed.
IAC-02: exact official package versions, verified downloads and fully hashed Python
dependencies; reuse compatible prerequisites without adopting or upgrading them.
IAC-03: DSC command resource owns convergence, with get/test/set operations. Fail
dependent work on prerequisite failure. Retrying repairs owned incomplete state;
unchanged reapplication makes no resource changes.
IAC-04: managed environment and launchers under LOCALAPPDATA/AgentiX/v3; no global
PATH changes, services, scheduled tasks, firewall changes or generated-artifact scans.
IAC-05: model download requires a reviewed explicit flag. A missing/unreachable
Ollama server is diagnosed without starting or restarting it. Never substitute models.
IAC-06: optional environment settings select managed tools, port 7873 and browser
behavior. Legacy port 7860 and manual GUI/CLI entrypoints remain compatible. Bind
only loopback and fail on occupied ports; no listener termination or random fallback.
IAC-07: retain bounded resource/outcome/duration diagnostics, no secrets/artifacts;
report partial failures without pretending package installations are transactional.
IAC-08: run offline tests with fake providers, PowerShell parser/static checks,
real DSC integration, parallel provisioning, fresh-environment regression/framework/
native/browser checks, CLI exit and disposable GUI startup. Distinguish fresh venv
verification from a clean Windows-machine installation.

No graphical installer, Python upgrade, widget agents, executor-contract fix or
currency presentation change is included. Existing project generated_tools is never
traversed. Native sandboxing and manual human acceptance remain mandatory.
