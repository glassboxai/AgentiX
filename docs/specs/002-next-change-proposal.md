# REF-002: Approved defect corrections

Status: explicitly approved and implemented on 2026-10-19 for SEC-001, SEC-002, SEC-003, SEC-004 and UI-001. See `../reports/FIXES.md` for verification.

## First production block: paths and final-content validation

Affected files: `security_manager.py`, `custom_tools.py`, `app.py`, their tests, technical architecture, change log and incident register. Root entrypoints and UI workflow remain compatible.

1. Fix SEC-001/SEC-002 by validating tool identifiers and constraining resolved filesystem paths by components rather than prefixes. Reject absolute paths, parent traversal, drive/UNC escapes and Windows alternate stream/device ambiguities. Add Windows-specific and nested-path compatibility tests; define link/reparse-point policy explicitly. Do not claim string validation alone removes filesystem race attacks.
2. Fix SEC-003 by returning defensive pending-request snapshots. Preserve editor content and current approval timing; do not redesign all concurrency in this block.
3. Fix SEC-004 by validating final approved Python content before persistence, including edited generated tests. Add a content-validation contract at the storage boundary, preserve ordinary Markdown writes and make validation failures visible. Test that existing valid files remain intact after rejection or invalid edits.
4. Add useful module/class/function contracts, rationale comments and diagnostic logs to changed paths. Keep content/prompt bodies out of routine logs.
5. For each fix, run the reproducer failing first, implement minimally, remove its strict xfail and run the entire suite. Update issue status only after verification. Preserve unrelated behavior.

6. Fix UI-001 with a dataclass history default factory: every ExecutionState owns its own list. This is not per-browser session isolation.

Implemented path policy: accept a single tool-name component and relative nested artifact paths; reject traversal components, drive/UNC/rooted syntax, Windows device names, alternate streams, invalid characters and trailing dots/spaces. Resolve existing filesystem links, reject tool-directory aliases and require the resolved artifact to remain within its tool. Revalidate the destination after file approval. These checks do not eliminate adversarial filesystem races or provide OS isolation.

Final-content policy: compile approved `.py` text without executing it before opening a destination for writing. For append operations, compile the existing text plus the approved addition. Invalid edits return an error and preserve an existing destination. Markdown persistence and ordinary approval/rejection behavior remain unchanged. Atomic replacement for valid writes is deferred; this fix guarantees pre-write syntax validation, not crash-atomic storage.

## Subsequent separately reviewed blocks

Instance history sharing (UI-001) is fixed. Per-browser state and correlated approvals (AUTH-001) remain separate work, followed by package restructuring. Review generated-code execution isolation before changing semantics; an ordinary subprocess is not a secure sandbox.

The installer, dependency locking and clean-install validation remain a later deliverable. Present exact affected files and acceptance criteria before each block. Approval of this first security block would not authorize arbitrary architecture or packaging changes.
