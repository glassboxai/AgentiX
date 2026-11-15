# Reference for tests/test_application_pipeline.py

Pipeline tests substitute only slow model/native/browser boundaries.

Source fingerprint: 3117c5ef1b9cd3c601efbc59740e8330f280a994f5328ef8cf20dc68bd07edcf

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_pipeline_persists_exact_proposals_without_approval

Catch overwriting proposals, auto-approval or importing generated Python.

Kind: callable. Declared return: Not declared / class. Source line: 11.

### test_pipeline_persists_exact_proposals_without_approval.factory

Build a model-boundary fixture for the independently exercised pipeline.

Kind: callable. Declared return: Not declared / class. Source line: 15.

### test_pipeline_persists_exact_proposals_without_approval.factory.client

Return a controlled model-boundary proposal without executing source.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### test_pipeline_canonicalizes_its_owned_data_root

Catch packaging an unresolved operator data alias rejected by source capture.

Kind: callable. Declared return: Not declared / class. Source line: 67.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | widget_source | Imported dependency for widget source in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | ApplicationPipeline | Imported dependency for ApplicationPipeline in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| test_pipeline_persists_exact_proposals_without_approval | tmp_path | Parameter for tmp path in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 11 |
| test_pipeline_persists_exact_proposals_without_approval | requests | Local binding for requests in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 13 |
| test_pipeline_persists_exact_proposals_without_approval.factory | folder | Parameter for folder in test_pipeline_persists_exact_proposals_without_approval.factory; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 15 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client | role | Parameter for role in test_pipeline_persists_exact_proposals_without_approval.factory.client; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client | content | Artifact or review text whose encoding, size and approval state must be checked. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client | module | Local binding for module in test_pipeline_persists_exact_proposals_without_approval.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 22 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client | catalog | Local binding for catalog in test_pipeline_persists_exact_proposals_without_approval.factory.client; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client.comprehension_31 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 31 |
| test_pipeline_persists_exact_proposals_without_approval.factory.client.comprehension_36 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 37 |
| test_pipeline_persists_exact_proposals_without_approval | installed | Imported dependency for installed in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| test_pipeline_persists_exact_proposals_without_approval | registry | Imported dependency for registry in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 45 |
| test_pipeline_persists_exact_proposals_without_approval | fixtures | Local binding for fixtures in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_pipeline_persists_exact_proposals_without_approval | tools | Local binding for tools in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| test_pipeline_persists_exact_proposals_without_approval | candidate | Local binding for candidate in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 50 |
| test_pipeline_persists_exact_proposals_without_approval | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_pipeline_persists_exact_proposals_without_approval | proposals | Local binding for proposals in test_pipeline_persists_exact_proposals_without_approval; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 60 |
| test_pipeline_canonicalizes_its_owned_data_root | tmp_path | Parameter for tmp path in test_pipeline_canonicalizes_its_owned_data_root; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 67 |
| test_pipeline_canonicalizes_its_owned_data_root | pipeline | Local binding for pipeline in test_pipeline_canonicalizes_its_owned_data_root; use the enclosing contract and type below. | Return type of ApplicationPipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 69 |
