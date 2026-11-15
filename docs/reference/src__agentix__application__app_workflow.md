# Reference for src/agentix/application/app_workflow.py

Supervised v5 application lifecycle with explicit legacy pilot compatibility.

All model artifacts remain data on the host. Complete-package review and native
execution are required. Proposed child tests never determine the acceptance verdict.

Source fingerprint: 4c0a5dd9465d1e73576c1e19c028c6609b06a3a0a6acd84763fa7ff60060ab38

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Candidate

Owner-bound pending review and verified preview; never serialized to a browser.

Kind: class. Declared return: Not declared / class. Source line: 30.

### Candidate.close

Stop only this candidate's owned application preview.

Kind: callable. Declared return: None. Source line: 49.

### ApplicationPipeline

Persist catalog-driven proposals; retain fixed composition only for legacy fixtures.

Kind: class. Declared return: Not declared / class. Source line: 59.

### ApplicationPipeline.__init__

Inject independent storage/model boundary; construction performs no IO.

Kind: callable. Declared return: None. Source line: 62.

### ApplicationPipeline.set_model_client

Use the active session client for the default CrewAI coordinator.

Explicit legacy client and coordinator factories remain subsystem overrides.
The method is called before generation and performs no model I/O.

Kind: callable. Declared return: None. Source line: 82.

### ApplicationPipeline.generate

Propose a workflow and per-tool widgets without approval or host execution.

Failures preserve the operation directory and any model evidence. No retry
or repair is automatic. The full source closure is included in review text.

Kind: callable. Declared return: Candidate. Source line: 91.

### ApplicationPipeline.bind_widget_publication

Bind widget publication to exact current tool grants, including approved revisions.

Kind: callable. Declared return: None. Source line: 111.

### ApplicationPipeline.bind_widget_publication.check_widgets

Observe co-located widget drift/revocation before reuse or publication.

Kind: callable. Declared return: None. Source line: 118.

### ApplicationPipeline.bind_widget_publication.publish_widgets

Publish reviewed current bytes only after independent acceptance passes.

Kind: callable. Declared return: None. Source line: 126.

### browser_origin_allowed

Permit verification requests only to the maintained local preview origin.

Kind: callable. Declared return: bool. Source line: 156.

### ApplicationSupervisor

Maintain approval, native/data/browser gates and owned preview lifecycle.

Kind: class. Declared return: Not declared / class. Source line: 172.

### ApplicationSupervisor.__init__

Inject expensive boundaries for offline tests; production remains native-only.

Kind: callable. Declared return: None. Source line: 175.

### ApplicationSupervisor.approve

Bind explicit human review to the displayed candidate and unchanged bytes.

Kind: callable. Declared return: None. Source line: 185.

### ApplicationSupervisor.verify

Publish only after independent native and real browser checks pass.

Kind: callable. Declared return: object. Source line: 211.

### ApplicationSupervisor._snapshot

Recheck the complete dependency closure before each permitted operation.

Kind: callable. Declared return: None. Source line: 274.

### ApplicationSupervisor.open_verified

Open a protected installed snapshot without repeating prior test suites.

Kind: callable. Declared return: object. Source line: 286.

### ApplicationSupervisor.run_data

Reuse the verified application's strict data entrypoint without its GUI.

Kind: callable. Declared return: dict. Source line: 296.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | partial | Imported dependency for partial in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | urlsplit | Imported dependency for urlsplit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | make_application_coordinator | Imported dependency for make application coordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApplicationCoordinator | Imported dependency for ApplicationCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | CallableCoordinator | Imported dependency for CallableCoordinator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ApprovedApplication | Imported dependency for ApprovedApplication in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | application_digest | Imported dependency for application digest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | ApplicationPreview | Imported dependency for ApplicationPreview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 23 |
| module | execute_application | Imported dependency for execute application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 24 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 26 |
| Candidate | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 33 |
| Candidate | folder | Typed binding for folder in Candidate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 34 |
| Candidate | package | Typed binding for package in Candidate; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 35 |
| Candidate | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 36 |
| Candidate | review_text | Typed binding for review text in Candidate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 37 |
| Candidate | approved | Typed binding for approved in Candidate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 38 |
| Candidate | verified | Typed binding for verified in Candidate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 39 |
| Candidate | snapshot | Typed binding for snapshot in Candidate; use the enclosing contract and type below. | ApprovedApplication &#124; None | Enclosing invocation or class/instance lifetime | 40 |
| Candidate | preview | Typed binding for preview in Candidate; use the enclosing contract and type below. | object &#124; None | Enclosing invocation or class/instance lifetime | 41 |
| Candidate | dependency_check | Typed binding for dependency check in Candidate; use the enclosing contract and type below. | Callable[[], None] &#124; None | Enclosing invocation or class/instance lifetime | 42 |
| Candidate | widget_commit | Typed binding for widget commit in Candidate; use the enclosing contract and type below. | Callable[['Candidate'], None] &#124; None | Enclosing invocation or class/instance lifetime | 43 |
| Candidate | catalog_id | Typed binding for catalog id in Candidate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 44 |
| Candidate | display_name | Typed binding for display name in Candidate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 45 |
| Candidate | library_lease | Typed binding for library lease in Candidate; use the enclosing contract and type below. | object &#124; None | Enclosing invocation or class/instance lifetime | 46 |
| Candidate | runtime_refresh | Typed binding for runtime refresh in Candidate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 47 |
| Candidate.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 49 |
| Candidate.close | self.preview | Attribute for preview in Candidate.close; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 53 |
| Candidate.close | self.library_lease | Attribute for library lease in Candidate.close; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 56 |
| ApplicationPipeline.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| ApplicationPipeline.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 64 |
| ApplicationPipeline.__init__ | client_factory | Parameter for client factory in ApplicationPipeline.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 65 |
| ApplicationPipeline.__init__ | widget_store | Parameter for widget store in ApplicationPipeline.__init__; use the enclosing contract and type below. | object &#124; None | Enclosing invocation or class/instance lifetime | 67 |
| ApplicationPipeline.__init__ | coordinator_factory | Parameter for coordinator factory in ApplicationPipeline.__init__; use the enclosing contract and type below. | Callable[[Path], ApplicationCoordinator] &#124; None | Enclosing invocation or class/instance lifetime | 68 |
| ApplicationPipeline.__init__ | self.root | Explicit root directory against which named paths are resolved. | tuple | Enclosing invocation or class/instance lifetime | 71 |
| ApplicationPipeline.__init__ | self.client_factory | Attribute for client factory in ApplicationPipeline.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 71 |
| ApplicationPipeline.__init__ | self.widget_store | Attribute for widget store in ApplicationPipeline.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 72 |
| ApplicationPipeline.__init__ | self._uses_default_coordinator | Attribute for uses default coordinator in ApplicationPipeline.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 75 |
| ApplicationPipeline.__init__ | self.coordinator_factory | Attribute for coordinator factory in ApplicationPipeline.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| ApplicationPipeline.set_model_client | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 82 |
| ApplicationPipeline.set_model_client | llm | Parameter for llm in ApplicationPipeline.set_model_client; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 82 |
| ApplicationPipeline.set_model_client | self.coordinator_factory | Attribute for coordinator factory in ApplicationPipeline.set_model_client; use the enclosing contract and type below. | Return type of partial; see its callable contract | Enclosing invocation or class/instance lifetime | 89 |
| ApplicationPipeline.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationPipeline.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationPipeline.generate | feedback | Parameter for feedback in ApplicationPipeline.generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationPipeline.generate | tools | Parameter for tools in ApplicationPipeline.generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 92 |
| ApplicationPipeline.generate.comprehension_105 | tool | Comprehension item for tool in ApplicationPipeline.generate.comprehension_105; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 105 |
| ApplicationPipeline.generate | generate | Imported dependency for generate in ApplicationPipeline.generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 107 |
| ApplicationPipeline.bind_widget_publication | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationPipeline.bind_widget_publication | candidate | Parameter for candidate in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationPipeline.bind_widget_publication | tools | Parameter for tools in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationPipeline.bind_widget_publication | store | Parameter for store in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 112 |
| ApplicationPipeline.bind_widget_publication | expected_widgets | Parameter for expected widgets in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 112, 116 |
| ApplicationPipeline.bind_widget_publication.comprehension_116 | role | Comprehension item for role in ApplicationPipeline.bind_widget_publication.comprehension_116; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 116 |
| ApplicationPipeline.bind_widget_publication.comprehension_116 | tool | Comprehension item for tool in ApplicationPipeline.bind_widget_publication.comprehension_116; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 116 |
| ApplicationPipeline.bind_widget_publication.check_widgets | role | Loop item for role in ApplicationPipeline.bind_widget_publication.check_widgets; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationPipeline.bind_widget_publication.check_widgets | expected | Reviewed expected observation kept outside untrusted child execution. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | item | Parameter for item in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 126 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | snapshot | Local binding for snapshot in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 129 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | proposals_now | Local binding for proposals now in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 130 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | role | Loop item for role in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 131 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | tool | Loop item for tool in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 131 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | proposal | Local binding for proposal in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | filename | Local binding for filename in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 133 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | previous | Local binding for previous in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 135 |
| ApplicationPipeline.bind_widget_publication.publish_widgets | css | Local binding for css in ApplicationPipeline.bind_widget_publication.publish_widgets; use the enclosing contract and type below. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| ApplicationPipeline.bind_widget_publication | candidate.dependency_check | Attribute for candidate.dependency check in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 152 |
| ApplicationPipeline.bind_widget_publication | candidate.widget_commit | Attribute for candidate.widget commit in ApplicationPipeline.bind_widget_publication; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 153 |
| browser_origin_allowed | url | Parameter for url in browser_origin_allowed; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 156 |
| browser_origin_allowed | origin | Parameter for origin in browser_origin_allowed; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 156 |
| browser_origin_allowed | target | Local binding for target in browser_origin_allowed; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 159 |
| browser_origin_allowed | expected | Reviewed expected observation kept outside untrusted child execution. | tuple | Enclosing invocation or class/instance lifetime | 159 |
| ApplicationSupervisor.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| ApplicationSupervisor.__init__ | native | Parameter for native in ApplicationSupervisor.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 178 |
| ApplicationSupervisor.__init__ | browser | Parameter for browser in ApplicationSupervisor.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 179 |
| ApplicationSupervisor.__init__ | preview_factory | Parameter for preview factory in ApplicationSupervisor.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 180 |
| ApplicationSupervisor.__init__ | self.native | Attribute for native in ApplicationSupervisor.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 183 |
| ApplicationSupervisor.__init__ | self.browser | Attribute for browser in ApplicationSupervisor.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 183 |
| ApplicationSupervisor.__init__ | self.preview_factory | Attribute for preview factory in ApplicationSupervisor.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 183 |
| ApplicationSupervisor.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 185 |
| ApplicationSupervisor.approve | candidate | Parameter for candidate in ApplicationSupervisor.approve; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 185 |
| ApplicationSupervisor.approve | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 185 |
| ApplicationSupervisor.approve | reviewed | Parameter for reviewed in ApplicationSupervisor.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 185 |
| ApplicationSupervisor.approve | snapshot | Local binding for snapshot in ApplicationSupervisor.approve; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 194 |
| ApplicationSupervisor.approve | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| ApplicationSupervisor.approve | review | Local binding for review in ApplicationSupervisor.approve; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 201 |
| ApplicationSupervisor.approve | validate_acceptance | Imported dependency for validate acceptance in ApplicationSupervisor.approve; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 202 |
| ApplicationSupervisor.approve | acceptance | Local binding for acceptance in ApplicationSupervisor.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 204 |
| ApplicationSupervisor.approve.comprehension_205 | key | Comprehension item for key in ApplicationSupervisor.approve.comprehension_205; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 205 |
| ApplicationSupervisor.approve | candidate.snapshot | Attribute for candidate.snapshot in ApplicationSupervisor.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 207 |
| ApplicationSupervisor.approve | candidate.approved | Attribute for candidate.approved in ApplicationSupervisor.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 208 |
| ApplicationSupervisor.verify | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 211 |
| ApplicationSupervisor.verify | candidate | Parameter for candidate in ApplicationSupervisor.verify; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 211 |
| ApplicationSupervisor.verify | parent_origin | Parameter for parent origin in ApplicationSupervisor.verify; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 211 |
| ApplicationSupervisor.verify | stage | Local binding for stage in ApplicationSupervisor.verify; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 214, 221, 229, 234, 237 |
| ApplicationSupervisor.verify | preview | Local binding for preview in ApplicationSupervisor.verify; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 215, 230 |
| ApplicationSupervisor.verify | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| ApplicationSupervisor.verify | verify | Imported dependency for verify in ApplicationSupervisor.verify; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 219 |
| ApplicationSupervisor.verify | candidate.preview | Attribute for candidate.preview in ApplicationSupervisor.verify; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 233, 270 |
| ApplicationSupervisor.verify | candidate.verified | Attribute for candidate.verified in ApplicationSupervisor.verify; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 240, 271 |
| ApplicationSupervisor.verify | error | Caught exception for error in ApplicationSupervisor.verify; use the enclosing contract and type below. | BaseException | Current exception handler; Python clears this binding afterward | 246 |
| ApplicationSupervisor._snapshot | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 274 |
| ApplicationSupervisor._snapshot | candidate | Parameter for candidate in ApplicationSupervisor._snapshot; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 274 |
| ApplicationSupervisor.open_verified | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 286 |
| ApplicationSupervisor.open_verified | candidate | Parameter for candidate in ApplicationSupervisor.open_verified; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 286 |
| ApplicationSupervisor.open_verified | parent_origin | Parameter for parent origin in ApplicationSupervisor.open_verified; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 286 |
| ApplicationSupervisor.open_verified | candidate.preview | Attribute for candidate.preview in ApplicationSupervisor.open_verified; use the enclosing contract and type below. | Return type of preview_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 291 |
| ApplicationSupervisor.run_data | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 296 |
| ApplicationSupervisor.run_data | candidate | Parameter for candidate in ApplicationSupervisor.run_data; use the enclosing contract and type below. | Candidate | Enclosing invocation or class/instance lifetime | 296 |
| ApplicationSupervisor.run_data | text | Parameter for text in ApplicationSupervisor.run_data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 296 |
| ApplicationSupervisor.run_data | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 301 |
| ApplicationSupervisor.run_data | validate_payload | Imported dependency for validate payload in ApplicationSupervisor.run_data; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 303 |
| ApplicationSupervisor.run_data | payload | Local binding for payload in ApplicationSupervisor.run_data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 305 |
