# AgentiX v7 documentation map

**Read selectively.** Do not load the whole docs tree, all reports or all source reference pages. Files on disk consume model context only when read/injected. This cleanup reduces duplicate instructions and encourages narrow retrieval; it does not change application inference or erase existing chat history.

| Need | Read |
| --- | --- |
| Working rules | [AGENTS](../AGENTS.md) |
| Current execution flow and architecture | [Architecture](V7_ARCHITECTURE.md) |
| Tool/widget/app folders and approvals | [Storage](V7_STORAGE.md) |
| Launch and operation | [INSTALLATION](INSTALLATION.md) |
| Security controls and residual risks | [LLM_SECURITY_2026](LLM_SECURITY_2026.md), [KNOWN_ISSUES](KNOWN_ISSUES.md) |
| Historical defect causes and regressions | [V7_INCIDENTS](V7_INCIDENTS.md) |
| Requirements | specs 037, 038, 039 [041 workflow bindings](specs/041-general-workflow-bindings.md) or [042 CrewAI coordination](specs/042-crewai-application-coordination.md) or [043 generated connection code](specs/043-generated-application-code.md): open only the affected one |
| Verification commands | [TEST_PLAN](specs/TEST_PLAN.md) |
| Historical V5 four-tool delivery | [V5_039_DELIVERY_REPORT](reports/V5_039_DELIVERY_REPORT.md) |
| Module/class/method/variable detail | [reference index](reference/README.md), then one module page |
| Historical requirements and incident IDs | [HISTORY](HISTORY.md) |
| Historical migration provenance | [migration manifests](history/migration/) |
| Cleanup scope and measurements | [DOC_040_CLEANUP](reports/DOC_040_CLEANUP.md) |

The reference tree is generated for exact freshness checks. DOC-040 preserved it unchanged; subsequent approved source changes regenerate the synchronized references. JSON/XML evidence, Python examples, configuration and fixture data are retained rather than treated as disposable prose. Historical pointers preserve document paths; full originals are in the external backup reported by the user. Such pointers are not requirements to reread the backup. Keep only final meaningful evidence for future changes; avoid accumulating every interim log or transcript in maintained documentation.

Schema-3 acceptance proposals and missing-case guidance: [V6-045](specs/045-proposed-acceptance-cases.md).

Public input canvas membership and layout: [V7-046](specs/046-public-input-layout.md).

Reviewed catalog relocation and blockers: [V7-047](specs/047-catalog-migration.md).

Reviewed installed package updates: [V7-048](specs/048-installed-application-update.md).

Existing Ollama server upgrades and launch readiness: [V7-050](specs/050-ollama-launch-compatibility.md).

Independent hybrid tool retrieval: [RAG-001](specs/051-tool-retrieval.md), [usage](TOOL_RETRIEVAL.md).

GUI startup retrieval and explicit application candidate selection: [RAG-010](specs/052-application-tool-candidates.md).

- [RAG-011 stable previews and candidate checkboxes](specs/053-candidate-checkboxes.md).

- [V7-054 acceptance approval readiness](specs/054-acceptance-approval-readiness.md).

- [V7-055 explicit host dependency recovery](specs/055-host-dependency-recovery.md).

- [V7-058 explicit profile selection and truthful generation diagnostics](specs/058-profile-selection-diagnostics.md).

- [V7-059 closed public input schema diagnostics](specs/059-closed-input-schema-diagnostics.md).

- [V7-060 permanent application removal with a stale policy binding](specs/060-stale-policy-removal.md).

- [V7-061 catalog services outside the installed-application policy](specs/061-catalog-services-outside-policy.md).

- [V7-062 widget visibility outside Edit](specs/062-widget-visibility.md).

- [V7-063 catalog explorer buttons and per-tool handle colors](specs/063-catalog-explorer-and-tool-colors.md).

- [V7-064 actionable catalog dependency diagnostics](specs/064-catalog-dependency-diagnostics.md).

- [V7-065 catalog folder window raised above the browser](specs/065-explorer-window-foreground.md).

- [V7-066 double-click a widget to open its reviewed source](specs/066-widget-double-click-selection.md).

- [V7-076 widget style window and style-only persistence](specs/076-widget-style-window.md).
- [V7-067 separate web tab, Edit affordances and code-help identity](specs/067-generated-application-web-and-edit-affordances.md).
- [V7-068 collapsible, resizable right-hand sidebars for Tools and Applications](specs/068-tab-right-sidebars.md).
- [V7-072 refresh control for the generated application](specs/072-application-refresh-control.md).
- [V7-073 composite data-operation input contract and diagnostics](specs/073-composite-data-input-contract.md).
- [V7-074 browser evidence for the composite accordion](specs/074-composite-browser-evidence.md).

- [V7-075 Mermaid rendering in the read-only Code Help transcript](specs/075-code-help-mermaid-rendering.md).
