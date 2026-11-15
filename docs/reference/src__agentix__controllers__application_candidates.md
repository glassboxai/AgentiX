# Reference for src/agentix/controllers/application_candidates.py

Server-owned application candidate snapshots and exact dependency selection.

Selection is a generation constraint, not an approval grant. Existing catalog
eligibility and current approved source bytes are rechecked at acceptance and use.

Source fingerprint: 5203c5f26eaf69d539d628a0f170fe526a11231a08ba0f6679c231a5f4cc74f7

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### AcceptedCandidates

Bind accepted dependencies to the exact application description on the server.

Kind: class. Declared return: Not declared / class. Source line: 21.

### CandidateSelection

Present one immutable search revision; its identity is checked with owner/token.

Kind: class. Declared return: Not declared / class. Source line: 30.

### CandidateSelection.expected

Return a fresh mapping of candidate identities to their source fingerprints.

Kind: callable. Declared return: dict[str, str]. Source line: 50.

### CandidateSelection.selected_expected

Validate a nonempty browser subset against this snapshot and its eligibility.

Kind: callable. Declared return: dict[str, str]. Source line: 54.

### CandidateState

Retain retrieval state only within the owning application session.

Kind: class. Declared return: Not declared / class. Source line: 73.

### CandidateState.invalidate

Clear a displayed selection and advance its revision before asynchronous work.

Kind: callable. Declared return: str. Source line: 82.

### SelectedToolRegistry

Constrain an existing approval registry to exactly the accepted tool names.

Kind: class. Declared return: Not declared / class. Source line: 89.

### SelectedToolRegistry.__init__

Copy server-owned expected source identities; never accept browser descriptors.

Kind: callable. Declared return: None. Source line: 92.

### SelectedToolRegistry.resolve

Revalidate eligibility and exact source hashes, returning only selected tools.

Kind: callable. Declared return: dict[str, ApprovedTool]. Source line: 96.

### SelectedToolRegistry.recheck

Reject source/grant changes without introducing unrelated catalog dependencies.

Kind: callable. Declared return: None. Source line: 114.

### _candidate_status

Map one bounded ineligibility reason to an owner-actionable row label.

Kind: callable. Declared return: str. Source line: 120.

### present_candidates

Mark every returned candidate's current eligibility without silently filtering it.

Kind: callable. Declared return: CandidateSelection. Source line: 130.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | Mapping | Imported dependency for Mapping in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Final | Imported dependency for Final in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | SearchResult | Imported dependency for SearchResult in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | RetrieverHandle | Imported dependency for RetrieverHandle in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | CatalogDependencyError | Imported dependency for CatalogDependencyError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | CANDIDATE_SUMMARY_CHARACTERS | Typed binding for CANDIDATE SUMMARY CHARACTERS in module; use the enclosing contract and type below. | Final[int] | Module/process lifetime | 17 |
| AcceptedCandidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 24 |
| AcceptedCandidates | expected | Reviewed expected observation kept outside untrusted child execution. | dict[str, str] | Enclosing invocation or class/instance lifetime | 25 |
| AcceptedCandidates | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 26 |
| CandidateSelection | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 33 |
| CandidateSelection | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 34 |
| CandidateSelection | limit | Typed binding for limit in CandidateSelection; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 35 |
| CandidateSelection | results | Typed binding for results in CandidateSelection; use the enclosing contract and type below. | tuple[SearchResult, ...] | Enclosing invocation or class/instance lifetime | 36 |
| CandidateSelection | rows | Typed binding for rows in CandidateSelection; use the enclosing contract and type below. | tuple[tuple[str, str, float, str], ...] | Enclosing invocation or class/instance lifetime | 39 |
| CandidateSelection | ready | Typed binding for ready in CandidateSelection; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 42 |
| CandidateSelection | message | Typed binding for message in CandidateSelection; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 43 |
| CandidateSelection | eligible_ids | Typed binding for eligible ids in CandidateSelection; use the enclosing contract and type below. | frozenset[str] | Enclosing invocation or class/instance lifetime | 45 |
| CandidateSelection.expected | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| CandidateSelection.expected.comprehension_52 | item | Comprehension item for item in CandidateSelection.expected.comprehension_52; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 52 |
| CandidateSelection.selected_expected | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| CandidateSelection.selected_expected | selected_ids | Parameter for selected ids in CandidateSelection.selected_expected; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 54 |
| CandidateSelection.selected_expected | chosen | Local binding for chosen in CandidateSelection.selected_expected; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| CandidateSelection.selected_expected.comprehension_60 | item | Comprehension item for item in CandidateSelection.selected_expected.comprehension_60; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 60 |
| CandidateSelection.selected_expected.comprehension_69 | key | Comprehension item for key in CandidateSelection.selected_expected.comprehension_69; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| CandidateSelection.selected_expected.comprehension_69 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 69 |
| CandidateState | handle | Typed binding for handle in CandidateState; use the enclosing contract and type below. | RetrieverHandle | Enclosing invocation or class/instance lifetime | 76 |
| CandidateState | revision | Typed binding for revision in CandidateState; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 77 |
| CandidateState | selection | Typed binding for selection in CandidateState; use the enclosing contract and type below. | CandidateSelection &#124; None | Enclosing invocation or class/instance lifetime | 78 |
| CandidateState.invalidate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| CandidateState.invalidate | self.revision | Attribute for revision in CandidateState.invalidate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 84 |
| CandidateState.invalidate | self.selection | Attribute for selection in CandidateState.invalidate; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 85 |
| SelectedToolRegistry.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 92 |
| SelectedToolRegistry.__init__ | registry | Parameter for registry in SelectedToolRegistry.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 92 |
| SelectedToolRegistry.__init__ | expected | Reviewed expected observation kept outside untrusted child execution. | Mapping[str, str] | Enclosing invocation or class/instance lifetime | 92 |
| SelectedToolRegistry.__init__ | self.registry | Attribute for registry in SelectedToolRegistry.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 94 |
| SelectedToolRegistry.__init__ | self.expected | Reviewed expected observation kept outside untrusted child execution. | tuple | Enclosing invocation or class/instance lifetime | 94 |
| SelectedToolRegistry.resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| SelectedToolRegistry.resolve | available | Local binding for available in SelectedToolRegistry.resolve; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 102 |
| SelectedToolRegistry.resolve.comprehension_102 | role | Comprehension item for role in SelectedToolRegistry.resolve.comprehension_102; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 102 |
| SelectedToolRegistry.resolve.comprehension_102 | tool | Comprehension item for tool in SelectedToolRegistry.resolve.comprehension_102; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 102 |
| SelectedToolRegistry.resolve | selected | Local binding for selected in SelectedToolRegistry.resolve; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 103 |
| SelectedToolRegistry.resolve | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| SelectedToolRegistry.resolve | digest | Content fingerprint for change detection; not a substitute for human approval. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 104 |
| SelectedToolRegistry.resolve | entry | Local binding for entry in SelectedToolRegistry.resolve; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| SelectedToolRegistry.resolve | role | Local binding for role in SelectedToolRegistry.resolve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| SelectedToolRegistry.resolve | tool | Local binding for tool in SelectedToolRegistry.resolve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| SelectedToolRegistry.recheck | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 114 |
| SelectedToolRegistry.recheck | expected | Reviewed expected observation kept outside untrusted child execution. | Mapping[str, ApprovedTool] | Enclosing invocation or class/instance lifetime | 114 |
| _candidate_status | reason | Parameter for reason in _candidate_status; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 120 |
| _candidate_status | lowered | Local binding for lowered in _candidate_status; use the enclosing contract and type below. | Return type of lower; see its callable contract | Enclosing invocation or class/instance lifetime | 124 |
| present_candidates | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 131 |
| present_candidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 131 |
| present_candidates | limit | Parameter for limit in present_candidates; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 131 |
| present_candidates | results | Parameter for results in present_candidates; use the enclosing contract and type below. | list[SearchResult] | Enclosing invocation or class/instance lifetime | 131 |
| present_candidates | registry | Parameter for registry in present_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 131 |
| present_candidates | available | Local binding for available in present_candidates; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 135, 137 |
| present_candidates.comprehension_135 | tool | Comprehension item for tool in present_candidates.comprehension_135; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 135 |
| present_candidates | reasons | Typed binding for reasons in present_candidates; use the enclosing contract and type below. | dict[str, str] | Enclosing invocation or class/instance lifetime | 138, 142, 144 |
| present_candidates | skip_reasons | Local binding for skip reasons in present_candidates; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| present_candidates | rows | Local binding for rows in present_candidates; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 145 |
| present_candidates | ready | Local binding for ready in present_candidates; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 145, 154 |
| present_candidates | eligible_ids | Typed binding for eligible ids in present_candidates; use the enclosing contract and type below. | set[str] | Enclosing invocation or class/instance lifetime | 146 |
| present_candidates | blocked | Typed binding for blocked in present_candidates; use the enclosing contract and type below. | list[str] | Enclosing invocation or class/instance lifetime | 147 |
| present_candidates | item | Loop item for item in present_candidates; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 148 |
| present_candidates | descriptor | Local binding for descriptor in present_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 149 |
| present_candidates | tool | Local binding for tool in present_candidates; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 150 |
| present_candidates | valid | Local binding for valid in present_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 151 |
| present_candidates | summary | Local binding for summary in present_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 159 |
| present_candidates | approval_blocked | Local binding for approval blocked in present_candidates; use the enclosing contract and type below. | Return type of any; see its callable contract | Enclosing invocation or class/instance lifetime | 168 |
| present_candidates.comprehension_168 | reason | Comprehension item for reason in present_candidates.comprehension_168; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 169 |
| present_candidates | message | Local binding for message in present_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 171, 181, 183 |
| present_candidates.comprehension_182 | item | Comprehension item for item in present_candidates.comprehension_182; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 182 |
