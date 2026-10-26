# ADR-0001: Characterize before restructuring

Date: 2026-10-19. Status: accepted for phases 1–3.

Legacy imports initialize services and global state. Import complete modules with explicit external dependency doubles to keep tests deterministic and offline. Use real temporary storage, compilation, AST inspection and trusted component execution. Test real configuration with external initialization intercepted.

This isolates the baseline but cannot prove third-party schema compatibility or host security. Preserve separate component tests and add live-framework tests during approved refactoring. Strict xfails expose defects without treating them as intended contracts. Do not modify production to simplify baseline testing.

Package architecture and OS execution isolation remain proposed. Agentix retains local Ollama code generation; engineering report helpers generate prose only.
