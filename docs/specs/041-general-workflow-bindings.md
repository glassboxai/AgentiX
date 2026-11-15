# V5-041: general declarative workflow bindings

Status: approved and implemented on 2026-10-30; verified with independent fixtures.
Live 7880 reload and actual-model creation remain deferred.
Incident: V5-ERR-041-01. No live application restart is authorized.

WF-01: preserve legacy external widget ports and complete-result edges. Add named
shared external inputs, JSON constants and bounded nonnegative array-item selection.
Sources are mutually exclusive. Reject malformed bindings, incompatible types,
unknown dependencies, cycles and inconsistent shared-input contracts before execution.
WF-02: render one editable control per named shared input. Resolve constants and
edges in dependency order, reuse a node result for every consumer, and fail without
publishing partial results when selection or a call fails. Keep native isolation.
WF-03: show the declarative plan in exact-byte review. The model uses catalog
contracts and original requirements; there are no tool-name or algorithm exceptions.
The plan states shared input names, constants, selected items and dependencies.
Human review and independent host-held acceptance remain mandatory: type checks
and model statements do not prove natural-language semantic correctness.
WF-04: choose compatible approved independent cases across the entire graph with
bounded search, including shared values, constants and projected results. Reject
when no coherent case exists; never compute expected values by calling tool code.
WF-05: cover unrelated chains, forks, repeated tools, invalid connections and legacy
compatibility using trusted temporary fixtures. No existing generated artifacts,
model inference, downloads or live-server restart are part of offline verification.

Payload compatibility: named shared inputs use the first consuming node/parameter
in manifest order as their canonical external port. Other consumers resolve that
same value. Duplicate submissions and nonexternal ports are rejected. This keeps
the existing named-node payload shape and exact-call review boundary.


## Binding syntax and verification mapping

Every binding retains an explicit `node` field. Legacy `{node: null}` is a local
external input; `{node: prior_id}` consumes a complete prior result. Extended
sources are `{node: null, input: shared_name}`, `{node: null, value: JSON_literal}`
and `{node: prior_id, index: nonnegative_integer}`. Extra keys and source mixtures
fail validation. Shared contract/default differences are rejected conservatively.

WF-01/WF-04/WF-05 map to tests/test_workflow_bindings.py and the legacy graph and
pipeline regressions. WF-02 is additionally checked with real in-memory Gradio,
headless AppContainer execution and a disposable native browser. WF-03 is checked
by exact graph/acceptance retention in the review; actual model semantic quality
is not inferred from injected proposals. See
[verification results](../reports/V5_041_WORKFLOW_BINDINGS.md).


## Approved live transport follow-up

WF-06 / V5-ERR-041-03: preserve explicit binding-field presence through Pydantic
serialization and the actual LocalModelClient boundary, not only injected model
proposals. The provider JSON schema must express disjoint source shapes; mixed
sources and null selectors are rejected before and after inference.
WF-07: inject a strict integer HTTP timeout in the range 1–600 seconds. Keep the
normal default at 120 seconds. Only the separately owned validation GUI uses an
explicit 600-second client factory at the composition root. No automatic retry,
model substitution, remote endpoint or relaxation of review/isolation is allowed.
The user approved this follow-up and continuation until A complex task is working;
the live 7880 process must remain intact.


WF-08: derive the General Assembler provider grammar from approved catalog ports.
Fresh node IDs carry short deterministic catalog prefixes, allowing complete-result
and array-item references only to tools with compatible return types. Unknown tools,
unknown/missing ports and incorrectly typed constants are excluded in the grammar;
host graph checks remain authoritative for identity, cycles and shared-input rules.
Legacy arbitrary IDs remain accepted by host validation. No tool-family names or
request-specific graph is encoded. Numerical forks and unrelated string pipelines
are covered by independent grammar tests.


## Supersession by V5-042

The user subsequently approved CrewAI coordination and removal of provider-specific
prefix grammar. WF-08 describes historical intermediate behavior and is superseded
by [V5-042](042-crewai-application-coordination.md). Source-preserving bindings,
host type checks, persisted compatibility and native isolation remain required.
The direct HTTP model boundary is retained only for legacy fixtures/pilot use.
