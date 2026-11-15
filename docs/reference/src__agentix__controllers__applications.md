# Reference for src/agentix/controllers/applications.py

Owner-checked Applications controller; no Gradio imports or generated execution.

Source fingerprint: 8d58fb3e41d0bd6bfa1f54391e02da86d6d252c8d782b24b1c605f0c6ab2d673

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _StreamRejected

Carry a precondition result out of a lock before yielding to Gradio.

Kind: class. Declared return: Not declared / class. Source line: 52.

### _StreamRejected.__init__

Retain only the maintained response tuple, without private source data.

Kind: callable. Declared return: None. Source line: 55.

### _safe_stream

Release lexical locks before suspending a rejected streaming callback.

Kind: callable. Declared return: Not declared / class. Source line: 61.

### _safe_stream.stream

Preserve callback metadata and return a safe precondition result.

Kind: callable. Declared return: Not declared / class. Source line: 65.

### ApplicationState

One browser's proposal and preview, bound to a verified Tools session.

Kind: class. Declared return: Not declared / class. Source line: 76.

### ApplicationsBackend

Coordinate owner, model, review and preview lifecycle independently of UI.

Kind: class. Declared return: Not declared / class. Source line: 92.

### ApplicationsBackend.__init__

Inject storage/execution factories; construction starts no model or server.

Kind: callable. Declared return: None. Source line: 95.

### ApplicationsBackend._resolve

Verify token/owner before touching a candidate or model boundary.

Kind: callable. Declared return: tuple[Any, ApplicationState]. Source line: 124.

### ApplicationsBackend._close

Cancel publication and close only this browser's owned preview.

Kind: callable. Declared return: None. Source line: 139.

### ApplicationsBackend._candidate_idle

Reject candidate actions during Tools work, generation or pending review.

Kind: callable. Declared return: None. Source line: 152.

### ApplicationsBackend.owned_candidate

Resolve the caller's own proposal for a presentation-only service.

Reuses the single ownership check instead of duplicating token/owner logic;
the caller still decides whether the proposal is idle enough to mutate.

Kind: callable. Declared return: tuple[Any, ApplicationState, Any]. Source line: 161.

### ApplicationsBackend.invalidate_candidates

Invalidate edited description/limit revisions without cancelling model work.

Kind: callable. Declared return: str. Source line: 172.

### ApplicationsBackend.candidate_controls

Read owner-local control availability plus a short reason for a blocked button.

Kind: callable. Declared return: tuple[bool, bool, str, str]. Source line: 194.

### ApplicationsBackend.request_candidates

Search before generation; publish only the latest owner-bound description/limit.

When the frontend supplies the application name, it is validated here so a
missing or invalid name is reported before any retrieval inference starts.

Kind: callable. Declared return: tuple[CandidateSelection | None, str]. Source line: 222.

### ApplicationsBackend.accept_candidates

Consume exactly the displayed server snapshot before starting application agents.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 339.

### ApplicationsBackend.generate_named

Require a user name before generation and bind it to the pending review.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 421.

### ApplicationsBackend.generate

Start a fresh user operation, never an automatic repair after rejection.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 447.

### ApplicationsBackend.repair

Request at most two new proposals from structured independent failure data.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 465.

### ApplicationsBackend._generate

Stream stage visibility; never approve or execute generated artifacts.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 501.

### ApplicationsBackend._generate.recheck_dependencies

Recheck both installed tool grants and reused widget identities.

Kind: callable. Declared return: None. Source line: 649.

### ApplicationsBackend.approve

Run independent gates only after owner-bound explicit human approval.

Kind: callable. Declared return: Iterator[tuple[Any, ...]]. Source line: 703.

### ApplicationsBackend.install_host_requirement

Install a previously disclosed host dependency after an explicit UI action.

Only the owner of an unchanged pending application review can reach the
injected registry. No browser value, generated source or model response
selects the requirement or its command.

Kind: callable. Declared return: tuple[str, str]. Source line: 818.

### ApplicationsBackend.stop

Stop/reject this owner's application without touching other sessions.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 880.

### ApplicationsBackend.data

Reuse the independently verified data operation without launching its GUI.

Kind: callable. Declared return: tuple[Any, str, str]. Source line: 898.

### ApplicationsBackend.data_contract

Describe the loaded application's declared data inputs without executing it.

The manifest comes from the verified snapshot, so the owner sees the exact
closed keys and types before typing a payload. No child module is imported
and no model or native execution occurs.

Kind: callable. Declared return: tuple[str, str]. Source line: 945.

### ApplicationsBackend.poll

Serialize stop/failure observation with this owner's open/close transitions.

Kind: callable. Declared return: tuple[Any, Any, str]. Source line: 962.

### ApplicationsBackend._poll_owned

Observe and optionally close one preview while holding its owner lock.

The busy-state check and teardown must be one lifecycle transition. A
stale observation must never close a newly started worker or its lease.
Model/native execution remains outside this polling path; teardown affects
only the owning session and retains the existing public status contract.

Kind: callable. Declared return: tuple[Any, Any, str]. Source line: 968.

### ApplicationsBackend.catalog_entries

List protected installed apps; stale records stay visible for re-approval.

Kind: callable. Declared return: tuple[list, str]. Source line: 1011.

### ApplicationsBackend.describe_app

Display bounded escaped metadata; the browser never supplies a package path.

Kind: callable. Declared return: str. Source line: 1024.

### ApplicationsBackend.load_app

Restore a verified app to an owner-local working copy; loading executes nothing.

Kind: callable. Declared return: Iterator[tuple]. Source line: 1063.

### ApplicationsBackend.load_app.recheck

Observe protected library and current installed-tool approval drift.

Kind: callable. Declared return: None. Source line: 1152.

### ApplicationsBackend.open_app

Open an unchanged installed app without another model or acceptance suite.

Kind: callable. Declared return: Iterator[tuple]. Source line: 1237.

### ApplicationsBackend.reverify_app

Repeat independent gates on installed bytes and reseal only after they pass.

Kind: callable. Declared return: Iterator[tuple]. Source line: 1331.

### ApplicationsBackend.reverify_app.recheck

Observe installed bytes and current tool approvals during the gates.

Kind: callable. Declared return: None. Source line: 1411.

### ApplicationsBackend.review_files

Read the current owner-only file inventory and concise review sections.

Kind: callable. Declared return: tuple. Source line: 1483.

### ApplicationsBackend.review_panes

Resolve a tool group without discarding dirty buffers on a same-tool selection.

Kind: callable. Declared return: dict. Source line: 1508.

### ApplicationsBackend.mark_group_edited

Mark any pane dirty; no old application approval may authorize unsaved code.

Kind: callable. Declared return: str. Source line: 1520.

### ApplicationsBackend.save_review

Validate and save the selected single file or all four grouped buffers.

Kind: callable. Declared return: tuple. Source line: 1530.

### ApplicationsBackend.mark_edited

Invalidate the checkbox path as soon as an editable file changes on screen.

Kind: callable. Declared return: str. Source line: 1601.

### ApplicationsBackend.read_file

Resolve selected filenames on the server; reject arbitrary filesystem paths.

Kind: callable. Declared return: tuple. Source line: 1613.

### ApplicationsBackend.save_file

Save only idle owner edits and require an entirely fresh application review.

Kind: callable. Declared return: tuple. Source line: 1624.

### ApplicationsBackend.review_tools

Use normal manual file/test/acceptance services for modified shared tools.

Kind: callable. Declared return: Iterator[tuple]. Source line: 1673.

### ApplicationsBackend.review_tools.review_worker

The existing tool services own publication; no direct approval/ledger mutation.

Kind: callable. Declared return: None. Source line: 1726.

### ApplicationsBackend.review_tools.recheck

Bind the new app review to the newly published installed tools.

Kind: callable. Declared return: None. Source line: 1851.

### ApplicationsBackend.review_state

Expose only this owner's current review/repair eligibility to the frontend.

Kind: callable. Declared return: dict[str, Any]. Source line: 1870.

### ApplicationsBackend.close_owner

Close resources when either shared session expiry or browser unload occurs.

Kind: callable. Declared return: None. Source line: 1898.

### ApplicationsBackend.unload

Close the framework owner's resources without resolving an expired token.

Kind: callable. Declared return: None. Source line: 1905.

### ApplicationsBackend.close_all

Stop only registered application resources when the supervisor exits.

Kind: callable. Declared return: None. Source line: 1909.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | atexit | Imported dependency for atexit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | functools | Imported dependency for functools in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | time | Imported dependency for time in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Iterator | Imported dependency for Iterator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | check_dependencies | Imported dependency for check dependencies in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | rebind_dependencies | Imported dependency for rebind dependencies in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ApplicationReview | Imported dependency for ApplicationReview in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | ApplicationPipeline | Imported dependency for ApplicationPipeline in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ApplicationSupervisor | Imported dependency for ApplicationSupervisor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | Candidate | Imported dependency for Candidate in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | AcceptedCandidates | Imported dependency for AcceptedCandidates in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | CandidateSelection | Imported dependency for CandidateSelection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | CandidateState | Imported dependency for CandidateState in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | SelectedToolRegistry | Imported dependency for SelectedToolRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | present_candidates | Imported dependency for present candidates in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | SessionRegistry | Imported dependency for SessionRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 25 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 26 |
| module | ApplicationContractError | Imported dependency for ApplicationContractError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 27 |
| module | approve_application | Imported dependency for approve application in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 28 |
| module | retrieval_policy | Imported dependency for retrieval policy in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 29 |
| module | GuiToolRetrieval | Imported dependency for GuiToolRetrieval in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 30 |
| module | ApprovedToolRegistry | Imported dependency for ApprovedToolRegistry in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 31 |
| module | CatalogDependencyError | Imported dependency for CatalogDependencyError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 31 |
| module | ToolCatalog | Imported dependency for ToolCatalog in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 32 |
| module | InstalledApps | Imported dependency for InstalledApps in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 33 |
| module | data_directory | Imported dependency for data directory in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 34 |
| module | WidgetStore | Imported dependency for WidgetStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 35 |
| module | describe_data_inputs | Imported dependency for describe data inputs in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 36 |
| module | generated_application_frame | Imported dependency for generated application frame in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 36 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 38 |
| module | MAX_CONCURRENT_PREVIEWS | Module binding for MAX CONCURRENT PREVIEWS in module; use the enclosing contract and type below. | int | Module/process lifetime | 40 |
| module | MAX_REPAIR_ATTEMPTS | Module binding for MAX REPAIR ATTEMPTS in module; use the enclosing contract and type below. | int | Module/process lifetime | 41 |
| module | TOOL_REVIEW_POLL_SECONDS | Module binding for TOOL REVIEW POLL SECONDS in module; use the enclosing contract and type below. | float | Module/process lifetime | 42 |
| module | GROUP_SELECTION_PREFIX | Module binding for GROUP SELECTION PREFIX in module; use the enclosing contract and type below. | str | Module/process lifetime | 43 |
| module | IDENTITY_REJECTION_CODES | Module binding for IDENTITY REJECTION CODES in module; use the enclosing contract and type below. | Return type of frozenset; see its callable contract | Module/process lifetime | 45 |
| module | IDENTITY_UNAVAILABLE | Module binding for IDENTITY UNAVAILABLE in module; use the enclosing contract and type below. | str | Module/process lifetime | 46 |
| _StreamRejected.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 55 |
| _StreamRejected.__init__ | row | Parameter for row in _StreamRejected.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 55 |
| _StreamRejected.__init__ | self.row | Attribute for row in _StreamRejected.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| _safe_stream | method | Parameter for method in _safe_stream; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 61 |
| _safe_stream.stream | args | Parameter for args in _safe_stream.stream; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| _safe_stream.stream | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 65 |
| _safe_stream.stream | error | Caught exception for error in _safe_stream.stream; use the enclosing contract and type below. | _StreamRejected | Current exception handler; Python clears this binding afterward | 69 |
| ApplicationState | token | Typed binding for token in ApplicationState; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 79 |
| ApplicationState | controller | Typed binding for controller in ApplicationState; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 80 |
| ApplicationState | candidate | Typed binding for candidate in ApplicationState; use the enclosing contract and type below. | Candidate &#124; None | Enclosing invocation or class/instance lifetime | 81 |
| ApplicationState | cancelled | Typed binding for cancelled in ApplicationState; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 82 |
| ApplicationState | held_slot | Typed binding for held slot in ApplicationState; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 83 |
| ApplicationState | repairs | Typed binding for repairs in ApplicationState; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 84 |
| ApplicationState | repair_allowed | Typed binding for repair allowed in ApplicationState; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 85 |
| ApplicationState | unsaved_file | Typed binding for unsaved file in ApplicationState; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 86 |
| ApplicationState | pending_host_requirement | Typed binding for pending host requirement in ApplicationState; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 87 |
| ApplicationState | retrieval_state | Typed binding for retrieval state in ApplicationState; use the enclosing contract and type below. | CandidateState | Enclosing invocation or class/instance lifetime | 88 |
| ApplicationState | accepted_dependencies | Typed binding for accepted dependencies in ApplicationState; use the enclosing contract and type below. | AcceptedCandidates &#124; None | Enclosing invocation or class/instance lifetime | 89 |
| ApplicationsBackend.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 96 |
| ApplicationsBackend.__init__ | sessions | Parameter for sessions in ApplicationsBackend.__init__; use the enclosing contract and type below. | SessionRegistry | Enclosing invocation or class/instance lifetime | 97 |
| ApplicationsBackend.__init__ | pipeline_factory | Parameter for pipeline factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 99 |
| ApplicationsBackend.__init__ | supervisor | Parameter for supervisor in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 100 |
| ApplicationsBackend.__init__ | parent_port | Parameter for parent port in ApplicationsBackend.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 101 |
| ApplicationsBackend.__init__ | registry_factory | Parameter for registry factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 102 |
| ApplicationsBackend.__init__ | library_factory | Parameter for library factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 103 |
| ApplicationsBackend.__init__ | retrieval | Parameter for retrieval in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 104 |
| ApplicationsBackend.__init__ | host_requirements | Parameter for host requirements in ApplicationsBackend.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 105 |
| ApplicationsBackend.__init__ | self.sessions | Attribute for sessions in ApplicationsBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 108 |
| ApplicationsBackend.__init__ | self.pipeline_factory | Attribute for pipeline factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 108 |
| ApplicationsBackend.__init__ | self.registry_factory | Attribute for registry factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 109 |
| ApplicationsBackend.__init__ | self.library_factory | Attribute for library factory in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 110 |
| ApplicationsBackend.__init__ | self.retrieval | Attribute for retrieval in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 111 |
| ApplicationsBackend.__init__ | self.host_requirements | Attribute for host requirements in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 114 |
| ApplicationsBackend.__init__ | self.supervisor | Attribute for supervisor in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 115 |
| ApplicationsBackend.__init__ | self.origin | Attribute for origin in ApplicationsBackend.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 116 |
| ApplicationsBackend.__init__ | self.states | Attribute for states in ApplicationsBackend.__init__; use the enclosing contract and type below. | dict[str, ApplicationState] | Enclosing invocation or class/instance lifetime | 119 |
| ApplicationsBackend.__init__ | self.lock | Attribute for lock in ApplicationsBackend.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| ApplicationsBackend.__init__ | self.preview_slots | Attribute for preview slots in ApplicationsBackend.__init__; use the enclosing contract and type below. | Return type of BoundedSemaphore; see its callable contract | Enclosing invocation or class/instance lifetime | 121 |
| ApplicationsBackend._resolve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 124 |
| ApplicationsBackend._resolve | token | Parameter for token in ApplicationsBackend._resolve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 124 |
| ApplicationsBackend._resolve | request | Parameter for request in ApplicationsBackend._resolve; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 124 |
| ApplicationsBackend._resolve | owner | Local binding for owner in ApplicationsBackend._resolve; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| ApplicationsBackend._resolve | session | Local binding for session in ApplicationsBackend._resolve; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| ApplicationsBackend._resolve | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 129, 132, 134 |
| ApplicationsBackend._resolve | session.controller.application_cleanup | Attribute for session.controller.application cleanup in ApplicationsBackend._resolve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 136 |
| ApplicationsBackend._close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 139 |
| ApplicationsBackend._close | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | ApplicationState | Enclosing invocation or class/instance lifetime | 139 |
| ApplicationsBackend._close | state.cancelled | Attribute for state.cancelled in ApplicationsBackend._close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 141 |
| ApplicationsBackend._close | state.unsaved_file | Attribute for state.unsaved file in ApplicationsBackend._close; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 143 |
| ApplicationsBackend._close | state.held_slot | Attribute for state.held slot in ApplicationsBackend._close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 148 |
| ApplicationsBackend._close | state.controller.state.application_review_pending | Attribute for state.controller.state.application review pending in ApplicationsBackend._close; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 149 |
| ApplicationsBackend._candidate_idle | controller | Parameter for controller in ApplicationsBackend._candidate_idle; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 152 |
| ApplicationsBackend.owned_candidate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 161 |
| ApplicationsBackend.owned_candidate | token | Parameter for token in ApplicationsBackend.owned_candidate; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 161 |
| ApplicationsBackend.owned_candidate | request | Parameter for request in ApplicationsBackend.owned_candidate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 161 |
| ApplicationsBackend.owned_candidate | session | Local binding for session in ApplicationsBackend.owned_candidate; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| ApplicationsBackend.owned_candidate | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| ApplicationsBackend.invalidate_candidates | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| ApplicationsBackend.invalidate_candidates | token | Parameter for token in ApplicationsBackend.invalidate_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 172 |
| ApplicationsBackend.invalidate_candidates | request | Parameter for request in ApplicationsBackend.invalidate_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 172 |
| ApplicationsBackend.invalidate_candidates | session | Local binding for session in ApplicationsBackend.invalidate_candidates; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| ApplicationsBackend.invalidate_candidates | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| ApplicationsBackend.invalidate_candidates | invalidated | Local binding for invalidated in ApplicationsBackend.invalidate_candidates; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 175, 182, 186 |
| ApplicationsBackend.invalidate_candidates | state.accepted_dependencies | Attribute for state.accepted dependencies in ApplicationsBackend.invalidate_candidates; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 183 |
| ApplicationsBackend.candidate_controls | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 195 |
| ApplicationsBackend.candidate_controls | token | Parameter for token in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 195 |
| ApplicationsBackend.candidate_controls | request | Parameter for request in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 195 |
| ApplicationsBackend.candidate_controls | selected_ids | Parameter for selected ids in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 195 |
| ApplicationsBackend.candidate_controls | session | Local binding for session in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| ApplicationsBackend.candidate_controls | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 198 |
| ApplicationsBackend.candidate_controls | idle | Local binding for idle in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 199 |
| ApplicationsBackend.candidate_controls | selection | Local binding for selection in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 204 |
| ApplicationsBackend.candidate_controls | ready | Local binding for ready in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205, 208, 219 |
| ApplicationsBackend.candidate_controls | reason | Local binding for reason in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 205, 209, 213, 219 |
| ApplicationsBackend.candidate_controls | chosen | Local binding for chosen in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211 |
| ApplicationsBackend.candidate_controls | ineligible | Local binding for ineligible in ApplicationsBackend.candidate_controls; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 212 |
| ApplicationsBackend.request_candidates | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationsBackend.request_candidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationsBackend.request_candidates | limit | Parameter for limit in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 223, 247 |
| ApplicationsBackend.request_candidates | token | Parameter for token in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationsBackend.request_candidates | request | Parameter for request in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationsBackend.request_candidates | name | Current identifier selected by parsing, lookup or dependency registration. | str &#124; None | Enclosing invocation or class/instance lifetime | 223 |
| ApplicationsBackend.request_candidates | session | Local binding for session in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| ApplicationsBackend.request_candidates | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 230 |
| ApplicationsBackend.request_candidates | controller | Local binding for controller in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 231 |
| ApplicationsBackend.request_candidates | application_folder | Imported dependency for application folder in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 233 |
| ApplicationsBackend.request_candidates | revision | Local binding for revision in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of invalidate; see its callable contract | Enclosing invocation or class/instance lifetime | 266 |
| ApplicationsBackend.request_candidates | state.accepted_dependencies | Attribute for state.accepted dependencies in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 267 |
| ApplicationsBackend.request_candidates | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 268, 336 |
| ApplicationsBackend.request_candidates | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 269, 337 |
| ApplicationsBackend.request_candidates | started | Local binding for started in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of perf_counter; see its callable contract | Enclosing invocation or class/instance lifetime | 270 |
| ApplicationsBackend.request_candidates | catalog | Local binding for catalog in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 278 |
| ApplicationsBackend.request_candidates | results | Local binding for results in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of search; see its callable contract | Enclosing invocation or class/instance lifetime | 282 |
| ApplicationsBackend.request_candidates | view | Local binding for view in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Return type of present_candidates; see its callable contract | Enclosing invocation or class/instance lifetime | 284 |
| ApplicationsBackend.request_candidates | state.retrieval_state.selection | Attribute for state.retrieval state.selection in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 295 |
| ApplicationsBackend.request_candidates | item | Loop item for item in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 305 |
| ApplicationsBackend.request_candidates | error | Caught exception for error in ApplicationsBackend.request_candidates; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 315 |
| ApplicationsBackend.accept_candidates | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 340 |
| ApplicationsBackend.accept_candidates | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 341 |
| ApplicationsBackend.accept_candidates | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 342 |
| ApplicationsBackend.accept_candidates | limit | Parameter for limit in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 343, 353 |
| ApplicationsBackend.accept_candidates | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 344 |
| ApplicationsBackend.accept_candidates | token | Parameter for token in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 345 |
| ApplicationsBackend.accept_candidates | request | Parameter for request in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 346 |
| ApplicationsBackend.accept_candidates | selected_ids | Parameter for selected ids in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | list[str] &#124; None | Enclosing invocation or class/instance lifetime | 348 |
| ApplicationsBackend.accept_candidates | session | Local binding for session in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 351 |
| ApplicationsBackend.accept_candidates | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 351 |
| ApplicationsBackend.accept_candidates | selection | Local binding for selection in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 362 |
| ApplicationsBackend.accept_candidates | expected | Reviewed expected observation kept outside untrusted child execution. | Return type of selected_expected; see its callable contract | Enclosing invocation or class/instance lifetime | 378 |
| ApplicationsBackend.accept_candidates | selected | Local binding for selected in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Return type of AcceptedCandidates; see its callable contract | Enclosing invocation or class/instance lifetime | 386 |
| ApplicationsBackend.accept_candidates | error | Caught exception for error in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 392 |
| ApplicationsBackend.accept_candidates | message | Local binding for message in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 399 |
| ApplicationsBackend.accept_candidates | tool_id | Loop item for tool id in ApplicationsBackend.accept_candidates; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 412 |
| ApplicationsBackend.generate_named | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 422 |
| ApplicationsBackend.generate_named | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 423 |
| ApplicationsBackend.generate_named | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 424 |
| ApplicationsBackend.generate_named | token | Parameter for token in ApplicationsBackend.generate_named; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 425 |
| ApplicationsBackend.generate_named | request | Parameter for request in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 426 |
| ApplicationsBackend.generate_named | selected | Parameter for selected in ApplicationsBackend.generate_named; use the enclosing contract and type below. | AcceptedCandidates &#124; None | Enclosing invocation or class/instance lifetime | 428 |
| ApplicationsBackend.generate_named | application_folder | Imported dependency for application folder in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 431 |
| ApplicationsBackend.generate_named | row | Loop item for row in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 438 |
| ApplicationsBackend.generate_named | session | Local binding for session in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 439 |
| ApplicationsBackend.generate_named | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 439 |
| ApplicationsBackend.generate_named | state.candidate.display_name | Attribute for state.candidate.display name in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 441 |
| ApplicationsBackend.generate_named | review | Local binding for review in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 442 |
| ApplicationsBackend.generate_named | state.candidate.review_text | Attribute for state.candidate.review text in ApplicationsBackend.generate_named; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 444 |
| ApplicationsBackend.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 448 |
| ApplicationsBackend.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 449 |
| ApplicationsBackend.generate | token | Parameter for token in ApplicationsBackend.generate; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 450 |
| ApplicationsBackend.generate | request | Parameter for request in ApplicationsBackend.generate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 451 |
| ApplicationsBackend.generate | selected | Parameter for selected in ApplicationsBackend.generate; use the enclosing contract and type below. | AcceptedCandidates &#124; None | Enclosing invocation or class/instance lifetime | 453 |
| ApplicationsBackend.generate | session | Local binding for session in ApplicationsBackend.generate; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 456 |
| ApplicationsBackend.generate | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 456 |
| ApplicationsBackend.generate | state.repairs | Attribute for state.repairs in ApplicationsBackend.generate; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 461 |
| ApplicationsBackend.generate | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.generate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 462 |
| ApplicationsBackend.repair | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 465 |
| ApplicationsBackend.repair | token | Parameter for token in ApplicationsBackend.repair; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 465 |
| ApplicationsBackend.repair | request | Parameter for request in ApplicationsBackend.repair; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 465 |
| ApplicationsBackend.repair | session | Local binding for session in ApplicationsBackend.repair; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 467 |
| ApplicationsBackend.repair | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 467 |
| ApplicationsBackend.repair | report | Local binding for report in ApplicationsBackend.repair; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 488 |
| ApplicationsBackend.repair | query | Original user request or a trusted test query; avoid payload logging by default. | Return type of read_text; see its callable contract | Enclosing invocation or class/instance lifetime | 489 |
| ApplicationsBackend.repair | state.repairs | Attribute for state.repairs in ApplicationsBackend.repair; use the enclosing contract and type below. | Preserved or operator-dependent type | Enclosing invocation or class/instance lifetime | 490 |
| ApplicationsBackend.repair | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.repair; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 491 |
| ApplicationsBackend.repair | display_name | Local binding for display name in ApplicationsBackend.repair; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 492 |
| ApplicationsBackend.repair | row | Loop item for row in ApplicationsBackend.repair; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 493 |
| ApplicationsBackend.repair | state.candidate.display_name | Attribute for state.candidate.display name in ApplicationsBackend.repair; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 497 |
| ApplicationsBackend._generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 502 |
| ApplicationsBackend._generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 503 |
| ApplicationsBackend._generate | token | Parameter for token in ApplicationsBackend._generate; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 504 |
| ApplicationsBackend._generate | request | Parameter for request in ApplicationsBackend._generate; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 505 |
| ApplicationsBackend._generate | feedback | Parameter for feedback in ApplicationsBackend._generate; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 507 |
| ApplicationsBackend._generate | selected | Parameter for selected in ApplicationsBackend._generate; use the enclosing contract and type below. | AcceptedCandidates &#124; None | Enclosing invocation or class/instance lifetime | 508 |
| ApplicationsBackend._generate | session | Local binding for session in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 511 |
| ApplicationsBackend._generate | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 511 |
| ApplicationsBackend._generate | controller | Local binding for controller in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 512 |
| ApplicationsBackend._generate | profile | Local binding for profile in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 535 |
| ApplicationsBackend._generate | ProfileError | Imported dependency for ProfileError in ApplicationsBackend._generate; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 548 |
| ApplicationsBackend._generate | had_trusted_digest | Local binding for had trusted digest in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of bool; see its callable contract | Enclosing invocation or class/instance lifetime | 551 |
| ApplicationsBackend._generate | captured_tofu_baseline | Local binding for captured tofu baseline in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 555 |
| ApplicationsBackend._generate | error | Caught exception for error in ApplicationsBackend._generate; use the enclosing contract and type below. | ProfileError | Current exception handler; Python clears this binding afterward | 558, 680 |
| ApplicationsBackend._generate | state.accepted_dependencies | Attribute for state.accepted dependencies in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 591 |
| ApplicationsBackend._generate | state.cancelled | Attribute for state.cancelled in ApplicationsBackend._generate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 592 |
| ApplicationsBackend._generate | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend._generate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 593, 700 |
| ApplicationsBackend._generate | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend._generate; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 594, 701 |
| ApplicationsBackend._generate | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 609 |
| ApplicationsBackend._generate | registry | Local binding for registry in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of registry_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 610, 616 |
| ApplicationsBackend._generate | tools | Local binding for tools in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 617 |
| ApplicationsBackend._generate | pipeline | Local binding for pipeline in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of pipeline_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 624 |
| ApplicationsBackend._generate | configured | Local binding for configured in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 625 |
| ApplicationsBackend._generate | set_model_client | Local binding for set model client in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 626 |
| ApplicationsBackend._generate | pipeline.widget_store | Attribute for pipeline.widget store in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of for_controller; see its callable contract | Enclosing invocation or class/instance lifetime | 630 |
| ApplicationsBackend._generate | candidate | Local binding for candidate in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 637 |
| ApplicationsBackend._generate | widget_check | Local binding for widget check in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 647 |
| ApplicationsBackend._generate | candidate.dependency_check | Attribute for candidate.dependency check in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 655 |
| ApplicationsBackend._generate | state.candidate | Attribute for state.candidate in ApplicationsBackend._generate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 669 |
| ApplicationsBackend._generate | controller.state.application_review_pending | Attribute for controller.state.application review pending in ApplicationsBackend._generate; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 670 |
| ApplicationsBackend._generate | detail | Local binding for detail in ApplicationsBackend._generate; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 683, 686, 688 |
| ApplicationsBackend.approve | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 704 |
| ApplicationsBackend.approve | reviewed | Parameter for reviewed in ApplicationsBackend.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 704 |
| ApplicationsBackend.approve | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 704 |
| ApplicationsBackend.approve | token | Parameter for token in ApplicationsBackend.approve; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 704 |
| ApplicationsBackend.approve | request | Parameter for request in ApplicationsBackend.approve; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 704 |
| ApplicationsBackend.approve | session | Local binding for session in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 707 |
| ApplicationsBackend.approve | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 707 |
| ApplicationsBackend.approve | controller | Local binding for controller in ApplicationsBackend.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 708 |
| ApplicationsBackend.approve | failure | Local binding for failure in ApplicationsBackend.approve; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 710, 716, 720, 727, 734, 741, 749, 752 |
| ApplicationsBackend.approve | candidate | Local binding for candidate in ApplicationsBackend.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 712 |
| ApplicationsBackend.approve | acceptance_status | Imported dependency for acceptance status in ApplicationsBackend.approve; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 729 |
| ApplicationsBackend.approve | valid | Local binding for valid in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of acceptance_status; see its callable contract | Enclosing invocation or class/instance lifetime | 731 |
| ApplicationsBackend.approve | guidance | Local binding for guidance in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of acceptance_status; see its callable contract | Enclosing invocation or class/instance lifetime | 731 |
| ApplicationsBackend.approve | requirement | Expression binding for requirement in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of missing; see its callable contract | Enclosing invocation or class/instance lifetime | 737 |
| ApplicationsBackend.approve | state.pending_host_requirement | Attribute for state.pending host requirement in ApplicationsBackend.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 740 |
| ApplicationsBackend.approve | state.held_slot | Attribute for state.held slot in ApplicationsBackend.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 754 |
| ApplicationsBackend.approve | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 755, 815 |
| ApplicationsBackend.approve | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.approve; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 756, 816 |
| ApplicationsBackend.approve | state.cancelled | Attribute for state.cancelled in ApplicationsBackend.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 757 |
| ApplicationsBackend.approve | preview | Local binding for preview in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of verify; see its callable contract | Enclosing invocation or class/instance lifetime | 775 |
| ApplicationsBackend.approve | installed | Local binding for installed in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of publish; see its callable contract | Enclosing invocation or class/instance lifetime | 776 |
| ApplicationsBackend.approve | candidate.catalog_id | Attribute for candidate.catalog id in ApplicationsBackend.approve; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 782 |
| ApplicationsBackend.approve | controller.state.application_review_pending | Attribute for controller.state.application review pending in ApplicationsBackend.approve; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 791 |
| ApplicationsBackend.approve | error | Caught exception for error in ApplicationsBackend.approve; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 797 |
| ApplicationsBackend.approve | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.approve; use the enclosing contract and type below. | Return type of is_file; see its callable contract | Enclosing invocation or class/instance lifetime | 799 |
| ApplicationsBackend.install_host_requirement | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 818 |
| ApplicationsBackend.install_host_requirement | token | Parameter for token in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 818 |
| ApplicationsBackend.install_host_requirement | request | Parameter for request in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 818 |
| ApplicationsBackend.install_host_requirement | session | Local binding for session in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 825 |
| ApplicationsBackend.install_host_requirement | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 825 |
| ApplicationsBackend.install_host_requirement | controller | Local binding for controller in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 826 |
| ApplicationsBackend.install_host_requirement | identifier | Local binding for identifier in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 828 |
| ApplicationsBackend.install_host_requirement | candidate | Local binding for candidate in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 829 |
| ApplicationsBackend.install_host_requirement | candidate_identity | Local binding for candidate identity in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 838 |
| ApplicationsBackend.install_host_requirement | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 839, 856 |
| ApplicationsBackend.install_host_requirement | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 840, 857 |
| ApplicationsBackend.install_host_requirement | error | Caught exception for error in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 843 |
| ApplicationsBackend.install_host_requirement | state.pending_host_requirement | Attribute for state.pending host requirement in ApplicationsBackend.install_host_requirement; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 869 |
| ApplicationsBackend.stop | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 880 |
| ApplicationsBackend.stop | token | Parameter for token in ApplicationsBackend.stop; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 880 |
| ApplicationsBackend.stop | request | Parameter for request in ApplicationsBackend.stop; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 880 |
| ApplicationsBackend.stop | session | Local binding for session in ApplicationsBackend.stop; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 882 |
| ApplicationsBackend.stop | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 882 |
| ApplicationsBackend.stop | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.stop; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 885 |
| ApplicationsBackend.stop | state.accepted_dependencies | Attribute for state.accepted dependencies in ApplicationsBackend.stop; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 886 |
| ApplicationsBackend.stop | state.candidate.approved | Attribute for state.candidate.approved in ApplicationsBackend.stop; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 889 |
| ApplicationsBackend.stop | state.candidate.verified | Attribute for state.candidate.verified in ApplicationsBackend.stop; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 890 |
| ApplicationsBackend.stop | state.candidate.snapshot | Attribute for state.candidate.snapshot in ApplicationsBackend.stop; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 891 |
| ApplicationsBackend.data | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 898 |
| ApplicationsBackend.data | text | Parameter for text in ApplicationsBackend.data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 898 |
| ApplicationsBackend.data | token | Parameter for token in ApplicationsBackend.data; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 898 |
| ApplicationsBackend.data | request | Parameter for request in ApplicationsBackend.data; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 898 |
| ApplicationsBackend.data | session | Local binding for session in ApplicationsBackend.data; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 900 |
| ApplicationsBackend.data | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 900 |
| ApplicationsBackend.data | session.controller.state.application_busy | Attribute for session.controller.state.application busy in ApplicationsBackend.data; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 912, 942 |
| ApplicationsBackend.data | session.controller.state.application_phase | Attribute for session.controller.state.application phase in ApplicationsBackend.data; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 913, 943 |
| ApplicationsBackend.data | error | Caught exception for error in ApplicationsBackend.data; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 920, 934 |
| ApplicationsBackend.data | detail | Local binding for detail in ApplicationsBackend.data; use the enclosing contract and type below. | Return type of rstrip; see its callable contract | Enclosing invocation or class/instance lifetime | 922 |
| ApplicationsBackend.data | message | Local binding for message in ApplicationsBackend.data; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 928 |
| ApplicationsBackend.data_contract | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 945 |
| ApplicationsBackend.data_contract | token | Parameter for token in ApplicationsBackend.data_contract; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 945 |
| ApplicationsBackend.data_contract | request | Parameter for request in ApplicationsBackend.data_contract; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 945 |
| ApplicationsBackend.data_contract | session | Local binding for session in ApplicationsBackend.data_contract; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 952 |
| ApplicationsBackend.data_contract | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 952 |
| ApplicationsBackend.data_contract | candidate | Local binding for candidate in ApplicationsBackend.data_contract; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 953 |
| ApplicationsBackend.data_contract | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 959 |
| ApplicationsBackend.poll | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 962 |
| ApplicationsBackend.poll | token | Parameter for token in ApplicationsBackend.poll; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 962 |
| ApplicationsBackend.poll | request | Parameter for request in ApplicationsBackend.poll; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 962 |
| ApplicationsBackend.poll | session | Local binding for session in ApplicationsBackend.poll; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 964 |
| ApplicationsBackend.poll | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 964 |
| ApplicationsBackend._poll_owned | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 968 |
| ApplicationsBackend._poll_owned | session | Parameter for session in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 968 |
| ApplicationsBackend._poll_owned | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | ApplicationState | Enclosing invocation or class/instance lifetime | 968 |
| ApplicationsBackend._poll_owned | candidate | Local binding for candidate in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 976 |
| ApplicationsBackend._poll_owned | candidate.approved | Attribute for candidate.approved in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 987 |
| ApplicationsBackend._poll_owned | candidate.verified | Attribute for candidate.verified in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 987 |
| ApplicationsBackend._poll_owned | candidate.snapshot | Attribute for candidate.snapshot in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 988 |
| ApplicationsBackend._poll_owned | diagnostics | Local binding for diagnostics in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1000 |
| ApplicationsBackend._poll_owned | timed_out | Local binding for timed out in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1001 |
| ApplicationsBackend._poll_owned | message | Local binding for message in ApplicationsBackend._poll_owned; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1003 |
| ApplicationsBackend.catalog_entries | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1011 |
| ApplicationsBackend.catalog_entries | token | Parameter for token in ApplicationsBackend.catalog_entries; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1011 |
| ApplicationsBackend.catalog_entries | request | Parameter for request in ApplicationsBackend.catalog_entries; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1011 |
| ApplicationsBackend.catalog_entries | session | Local binding for session in ApplicationsBackend.catalog_entries; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1013 |
| ApplicationsBackend.catalog_entries | _ | Local binding for  in ApplicationsBackend.catalog_entries; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1013 |
| ApplicationsBackend.catalog_entries | choices | Local binding for choices in ApplicationsBackend.catalog_entries; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 1014 |
| ApplicationsBackend.catalog_entries.comprehension_1014 | entry | Comprehension item for entry in ApplicationsBackend.catalog_entries.comprehension_1014; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1019 |
| ApplicationsBackend.describe_app | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1024 |
| ApplicationsBackend.describe_app | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1024 |
| ApplicationsBackend.describe_app | token | Parameter for token in ApplicationsBackend.describe_app; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1024 |
| ApplicationsBackend.describe_app | request | Parameter for request in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1024 |
| ApplicationsBackend.describe_app | html | Imported dependency for html in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1026 |
| ApplicationsBackend.describe_app | session | Local binding for session in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1028 |
| ApplicationsBackend.describe_app | _ | Local binding for  in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1028 |
| ApplicationsBackend.describe_app | library | Local binding for library in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Return type of library_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1029 |
| ApplicationsBackend.describe_app | app | Local binding for app in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 1031 |
| ApplicationsBackend.describe_app | entry | Local binding for entry in ApplicationsBackend.describe_app; use the enclosing contract and type below. | Return type of entry; see its callable contract | Enclosing invocation or class/instance lifetime | 1033 |
| ApplicationsBackend.describe_app | error | Caught exception for error in ApplicationsBackend.describe_app; use the enclosing contract and type below. | ValueError | Current exception handler; Python clears this binding afterward | 1044 |
| ApplicationsBackend.load_app | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1063 |
| ApplicationsBackend.load_app | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1063 |
| ApplicationsBackend.load_app | token | Parameter for token in ApplicationsBackend.load_app; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1063 |
| ApplicationsBackend.load_app | request | Parameter for request in ApplicationsBackend.load_app; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1063 |
| ApplicationsBackend.load_app | uuid4 | Imported dependency for uuid4 in ApplicationsBackend.load_app; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1065 |
| ApplicationsBackend.load_app | session | Local binding for session in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1067 |
| ApplicationsBackend.load_app | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1067 |
| ApplicationsBackend.load_app | controller | Local binding for controller in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1068 |
| ApplicationsBackend.load_app | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.load_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1088, 1233 |
| ApplicationsBackend.load_app | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.load_app; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1089, 1234 |
| ApplicationsBackend.load_app | library | Local binding for library in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of library_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1099 |
| ApplicationsBackend.load_app | app | Local binding for app in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 1101, 1107, 1109 |
| ApplicationsBackend.load_app | stale | Local binding for stale in ApplicationsBackend.load_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1102, 1110, 1117 |
| ApplicationsBackend.load_app | registry | Local binding for registry in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of registry_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1111 |
| ApplicationsBackend.load_app | rebound | Local binding for rebound in ApplicationsBackend.load_app; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 1112, 1116 |
| ApplicationsBackend.load_app | snapshot | Local binding for snapshot in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 1118 |
| ApplicationsBackend.load_app | nonce | Local binding for nonce in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1119 |
| ApplicationsBackend.load_app | folder | Local binding for folder in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1120 |
| ApplicationsBackend.load_app | package | Local binding for package in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1121 |
| ApplicationsBackend.load_app | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1123 |
| ApplicationsBackend.load_app | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1123 |
| ApplicationsBackend.load_app | review | Local binding for review in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 1129 |
| ApplicationsBackend.load_app.comprehension_1130 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1132 |
| ApplicationsBackend.load_app.comprehension_1130 | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1132 |
| ApplicationsBackend.load_app | candidate | Local binding for candidate in ApplicationsBackend.load_app; use the enclosing contract and type below. | Return type of Candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 1138 |
| ApplicationsBackend.load_app.recheck | current | Local binding for current in ApplicationsBackend.load_app.recheck; use the enclosing contract and type below. | Return type of load_for_runtime_refresh; see its callable contract | Enclosing invocation or class/instance lifetime | 1156, 1158, 1160 |
| ApplicationsBackend.load_app.recheck | binding | Local binding for binding in ApplicationsBackend.load_app.recheck; use the enclosing contract and type below. | Return type of rebind_dependencies; see its callable contract | Enclosing invocation or class/instance lifetime | 1166 |
| ApplicationsBackend.load_app.recheck | candidate.review_text | Attribute for candidate.review text in ApplicationsBackend.load_app.recheck; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 1169 |
| ApplicationsBackend.load_app | candidate.dependency_check | Attribute for candidate.dependency check in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1177 |
| ApplicationsBackend.load_app | state.candidate | Attribute for state.candidate in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1178 |
| ApplicationsBackend.load_app | state.cancelled | Attribute for state.cancelled in ApplicationsBackend.load_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1179 |
| ApplicationsBackend.load_app | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.load_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1180 |
| ApplicationsBackend.load_app | controller.state.application_review_pending | Attribute for controller.state.application review pending in ApplicationsBackend.load_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1182 |
| ApplicationsBackend.load_app | reason | Local binding for reason in ApplicationsBackend.load_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1183 |
| ApplicationsBackend.load_app | error | Caught exception for error in ApplicationsBackend.load_app; use the enclosing contract and type below. | CatalogDependencyError | Current exception handler; Python clears this binding afterward | 1214, 1223 |
| ApplicationsBackend.open_app | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1237 |
| ApplicationsBackend.open_app | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1237 |
| ApplicationsBackend.open_app | token | Parameter for token in ApplicationsBackend.open_app; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1237 |
| ApplicationsBackend.open_app | request | Parameter for request in ApplicationsBackend.open_app; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1237 |
| ApplicationsBackend.open_app | session | Local binding for session in ApplicationsBackend.open_app; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1239 |
| ApplicationsBackend.open_app | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1239 |
| ApplicationsBackend.open_app | candidate | Local binding for candidate in ApplicationsBackend.open_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1242 |
| ApplicationsBackend.open_app | state.held_slot | Attribute for state.held slot in ApplicationsBackend.open_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1290 |
| ApplicationsBackend.open_app | session.controller.state.application_busy | Attribute for session.controller.state.application busy in ApplicationsBackend.open_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1291, 1327 |
| ApplicationsBackend.open_app | session.controller.state.application_phase | Attribute for session.controller.state.application phase in ApplicationsBackend.open_app; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1292, 1328 |
| ApplicationsBackend.open_app | candidate.library_lease | Attribute for candidate.library lease in ApplicationsBackend.open_app; use the enclosing contract and type below. | Return type of open_lease; see its callable contract | Enclosing invocation or class/instance lifetime | 1294 |
| ApplicationsBackend.open_app | preview | Local binding for preview in ApplicationsBackend.open_app; use the enclosing contract and type below. | Return type of open_verified; see its callable contract | Enclosing invocation or class/instance lifetime | 1303 |
| ApplicationsBackend.open_app | error | Caught exception for error in ApplicationsBackend.open_app; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 1316 |
| ApplicationsBackend.reverify_app | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1331 |
| ApplicationsBackend.reverify_app | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1331 |
| ApplicationsBackend.reverify_app | token | Parameter for token in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1331 |
| ApplicationsBackend.reverify_app | request | Parameter for request in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1331 |
| ApplicationsBackend.reverify_app | uuid4 | Imported dependency for uuid4 in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1333 |
| ApplicationsBackend.reverify_app | session | Local binding for session in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1335 |
| ApplicationsBackend.reverify_app | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1335 |
| ApplicationsBackend.reverify_app | controller | Local binding for controller in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1336 |
| ApplicationsBackend.reverify_app | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1353, 1480 |
| ApplicationsBackend.reverify_app | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1354, 1481 |
| ApplicationsBackend.reverify_app | library | Local binding for library in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of library_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1356 |
| ApplicationsBackend.reverify_app | app | Local binding for app in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of load_stale; see its callable contract | Enclosing invocation or class/instance lifetime | 1369 |
| ApplicationsBackend.reverify_app | registry | Local binding for registry in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of registry_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1370 |
| ApplicationsBackend.reverify_app | snapshot | Local binding for snapshot in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of approve_application; see its callable contract | Enclosing invocation or class/instance lifetime | 1386 |
| ApplicationsBackend.reverify_app | folder | Local binding for folder in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1387 |
| ApplicationsBackend.reverify_app | package | Local binding for package in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1388 |
| ApplicationsBackend.reverify_app | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1390 |
| ApplicationsBackend.reverify_app | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1390 |
| ApplicationsBackend.reverify_app | review | Local binding for review in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 1392 |
| ApplicationsBackend.reverify_app.comprehension_1393 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1395 |
| ApplicationsBackend.reverify_app.comprehension_1393 | content | Artifact or review text whose encoding, size and approval state must be checked. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1395 |
| ApplicationsBackend.reverify_app | candidate | Local binding for candidate in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of Candidate; see its callable contract | Enclosing invocation or class/instance lifetime | 1398 |
| ApplicationsBackend.reverify_app | candidate.dependency_check | Attribute for candidate.dependency check in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1415 |
| ApplicationsBackend.reverify_app | preview | Local binding for preview in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of verify; see its callable contract | Enclosing invocation or class/instance lifetime | 1424 |
| ApplicationsBackend.reverify_app | resealed | Local binding for resealed in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | Return type of reseal; see its callable contract | Enclosing invocation or class/instance lifetime | 1425 |
| ApplicationsBackend.reverify_app | error | Caught exception for error in ApplicationsBackend.reverify_app; use the enclosing contract and type below. | CatalogDependencyError | Current exception handler; Python clears this binding afterward | 1441, 1460 |
| ApplicationsBackend.review_files | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1483 |
| ApplicationsBackend.review_files | token | Parameter for token in ApplicationsBackend.review_files; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1483 |
| ApplicationsBackend.review_files | request | Parameter for request in ApplicationsBackend.review_files; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1483 |
| ApplicationsBackend.review_files | session | Local binding for session in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1485 |
| ApplicationsBackend.review_files | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1485 |
| ApplicationsBackend.review_files | service | Local binding for service in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of ApplicationReview; see its callable contract | Enclosing invocation or class/instance lifetime | 1488 |
| ApplicationsBackend.review_files | entries | Local binding for entries in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of entries; see its callable contract | Enclosing invocation or class/instance lifetime | 1489 |
| ApplicationsBackend.review_files | snapshot | Local binding for snapshot in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 1490 |
| ApplicationsBackend.review_files | first | Local binding for first in ApplicationsBackend.review_files; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1491 |
| ApplicationsBackend.review_files | text | Local binding for text in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1496 |
| ApplicationsBackend.review_files | editable | Local binding for editable in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1496 |
| ApplicationsBackend.review_files | hint | Local binding for hint in ApplicationsBackend.review_files; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1496 |
| ApplicationsBackend.review_panes | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1508 |
| ApplicationsBackend.review_panes | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1508 |
| ApplicationsBackend.review_panes | token | Parameter for token in ApplicationsBackend.review_panes; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1508 |
| ApplicationsBackend.review_panes | request | Parameter for request in ApplicationsBackend.review_panes; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1508 |
| ApplicationsBackend.review_panes | session | Local binding for session in ApplicationsBackend.review_panes; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1510 |
| ApplicationsBackend.review_panes | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1510 |
| ApplicationsBackend.review_panes | panes | Local binding for panes in ApplicationsBackend.review_panes; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 1513 |
| ApplicationsBackend.review_panes | expected | Reviewed expected observation kept outside untrusted child execution. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1514 |
| ApplicationsBackend.mark_group_edited | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1520 |
| ApplicationsBackend.mark_group_edited | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1520 |
| ApplicationsBackend.mark_group_edited | token | Parameter for token in ApplicationsBackend.mark_group_edited; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1520 |
| ApplicationsBackend.mark_group_edited | request | Parameter for request in ApplicationsBackend.mark_group_edited; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1520 |
| ApplicationsBackend.mark_group_edited | session | Local binding for session in ApplicationsBackend.mark_group_edited; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1522 |
| ApplicationsBackend.mark_group_edited | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1522 |
| ApplicationsBackend.mark_group_edited | panes | Local binding for panes in ApplicationsBackend.mark_group_edited; use the enclosing contract and type below. | Return type of panes; see its callable contract | Enclosing invocation or class/instance lifetime | 1526 |
| ApplicationsBackend.mark_group_edited | state.unsaved_file | Attribute for state.unsaved file in ApplicationsBackend.mark_group_edited; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1527 |
| ApplicationsBackend.save_review | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1531 |
| ApplicationsBackend.save_review | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1532 |
| ApplicationsBackend.save_review | text | Parameter for text in ApplicationsBackend.save_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1533 |
| ApplicationsBackend.save_review | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 1534 |
| ApplicationsBackend.save_review | widget | Parameter for widget in ApplicationsBackend.save_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1535 |
| ApplicationsBackend.save_review | tool_tests | Parameter for tool tests in ApplicationsBackend.save_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1536 |
| ApplicationsBackend.save_review | widget_tests | Parameter for widget tests in ApplicationsBackend.save_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1537 |
| ApplicationsBackend.save_review | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1538 |
| ApplicationsBackend.save_review | token | Parameter for token in ApplicationsBackend.save_review; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1539 |
| ApplicationsBackend.save_review | request | Parameter for request in ApplicationsBackend.save_review; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1540 |
| ApplicationsBackend.save_review | session | Local binding for session in ApplicationsBackend.save_review; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1543 |
| ApplicationsBackend.save_review | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1543 |
| ApplicationsBackend.save_review | role | Local binding for role in ApplicationsBackend.save_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1547 |
| ApplicationsBackend.save_review | changed | Local binding for changed in ApplicationsBackend.save_review; use the enclosing contract and type below. | Return type of save_group; see its callable contract | Enclosing invocation or class/instance lifetime | 1555 |
| ApplicationsBackend.save_review | state.unsaved_file | Attribute for state.unsaved file in ApplicationsBackend.save_review; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1572 |
| ApplicationsBackend.save_review | frame | Local binding for frame in ApplicationsBackend.save_review; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1574 |
| ApplicationsBackend.save_review | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.save_review; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1590 |
| ApplicationsBackend.save_review | session.controller.state.application_review_pending | Attribute for session.controller.state.application review pending in ApplicationsBackend.save_review; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1591 |
| ApplicationsBackend.mark_edited | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1601 |
| ApplicationsBackend.mark_edited | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1601 |
| ApplicationsBackend.mark_edited | token | Parameter for token in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1601 |
| ApplicationsBackend.mark_edited | request | Parameter for request in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1601 |
| ApplicationsBackend.mark_edited | session | Local binding for session in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1603 |
| ApplicationsBackend.mark_edited | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1603 |
| ApplicationsBackend.mark_edited | _ | Local binding for  in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1607 |
| ApplicationsBackend.mark_edited | editable | Local binding for editable in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1607 |
| ApplicationsBackend.mark_edited | state.unsaved_file | Attribute for state.unsaved file in ApplicationsBackend.mark_edited; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1610 |
| ApplicationsBackend.read_file | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1613 |
| ApplicationsBackend.read_file | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1613 |
| ApplicationsBackend.read_file | token | Parameter for token in ApplicationsBackend.read_file; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1613 |
| ApplicationsBackend.read_file | request | Parameter for request in ApplicationsBackend.read_file; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1613 |
| ApplicationsBackend.read_file | session | Local binding for session in ApplicationsBackend.read_file; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1615 |
| ApplicationsBackend.read_file | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1615 |
| ApplicationsBackend.read_file | text | Local binding for text in ApplicationsBackend.read_file; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1621 |
| ApplicationsBackend.read_file | editable | Local binding for editable in ApplicationsBackend.read_file; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1621 |
| ApplicationsBackend.read_file | hint | Local binding for hint in ApplicationsBackend.read_file; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 1621 |
| ApplicationsBackend.save_file | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | text | Parameter for text in ApplicationsBackend.save_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | token | Parameter for token in ApplicationsBackend.save_file; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | request | Parameter for request in ApplicationsBackend.save_file; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1625 |
| ApplicationsBackend.save_file | session | Local binding for session in ApplicationsBackend.save_file; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1628 |
| ApplicationsBackend.save_file | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1628 |
| ApplicationsBackend.save_file | preview | Local binding for preview in ApplicationsBackend.save_file; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 1642 |
| ApplicationsBackend.save_file | restage | Local binding for restage in ApplicationsBackend.save_file; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 1646 |
| ApplicationsBackend.save_file | revoked | Local binding for revoked in ApplicationsBackend.save_file; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 1649 |
| ApplicationsBackend.save_file | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.save_file; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1652 |
| ApplicationsBackend.save_file | session.controller.state.application_review_pending | Attribute for session.controller.state.application review pending in ApplicationsBackend.save_file; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1653 |
| ApplicationsBackend.save_file | message | Local binding for message in ApplicationsBackend.save_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1654, 1659 |
| ApplicationsBackend.save_file | state.unsaved_file | Attribute for state.unsaved file in ApplicationsBackend.save_file; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1658 |
| ApplicationsBackend.review_tools | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1673 |
| ApplicationsBackend.review_tools | token | Parameter for token in ApplicationsBackend.review_tools; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1673 |
| ApplicationsBackend.review_tools | request | Parameter for request in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1673 |
| ApplicationsBackend.review_tools | hashlib | Imported dependency for hashlib in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1675 |
| ApplicationsBackend.review_tools | uuid4 | Imported dependency for uuid4 in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1676 |
| ApplicationsBackend.review_tools | application_digest | Imported dependency for application digest in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1678 |
| ApplicationsBackend.review_tools | parse_contract | Imported dependency for parse contract in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 1679 |
| ApplicationsBackend.review_tools | session | Local binding for session in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1681 |
| ApplicationsBackend.review_tools | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1681 |
| ApplicationsBackend.review_tools | controller | Local binding for controller in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1682 |
| ApplicationsBackend.review_tools | item | Local binding for item in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1684 |
| ApplicationsBackend.review_tools | operations | Local binding for operations in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 1685 |
| ApplicationsBackend.review_tools | snapshot | Local binding for snapshot in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 1704 |
| ApplicationsBackend.review_tools | contracts | Local binding for contracts in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 1705 |
| ApplicationsBackend.review_tools | files | Local binding for files in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 1706 |
| ApplicationsBackend.review_tools | pending | Defensive pending-approval snapshot; never a capability to approve another owner. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 1707 |
| ApplicationsBackend.review_tools | controller.state.application_busy | Attribute for controller.state.application busy in ApplicationsBackend.review_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1720, 1867 |
| ApplicationsBackend.review_tools | controller.state.application_phase | Attribute for controller.state.application phase in ApplicationsBackend.review_tools; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1721, 1868 |
| ApplicationsBackend.review_tools | controller.security.operation_id | Attribute for controller.security.operation id in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1722 |
| ApplicationsBackend.review_tools | completed | Local binding for completed in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of Event; see its callable contract | Enclosing invocation or class/instance lifetime | 1723 |
| ApplicationsBackend.review_tools | failures | Local binding for failures in ApplicationsBackend.review_tools; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 1724 |
| ApplicationsBackend.review_tools.review_worker | revision | Loop item for revision in ApplicationsBackend.review_tools.review_worker; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1729 |
| ApplicationsBackend.review_tools.review_worker | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1730 |
| ApplicationsBackend.review_tools.review_worker | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 1731, 1734 |
| ApplicationsBackend.review_tools.review_worker | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of compile_and_save_code_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 1735, 1738, 1741, 1752 |
| ApplicationsBackend.review_tools.review_worker | case | Local binding for case in ApplicationsBackend.review_tools.review_worker; use the enclosing contract and type below. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 1744 |
| ApplicationsBackend.review_tools.review_worker.comprehension_1745 | case | Comprehension item for case in ApplicationsBackend.review_tools.review_worker.comprehension_1745; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1745 |
| ApplicationsBackend.review_tools.review_worker | error | Caught exception for error in ApplicationsBackend.review_tools.review_worker; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 1757 |
| ApplicationsBackend.review_tools | state.candidate | Attribute for state.candidate in ApplicationsBackend.review_tools; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 1788 |
| ApplicationsBackend.review_tools | state.accepted_dependencies | Attribute for state.accepted dependencies in ApplicationsBackend.review_tools; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 1789 |
| ApplicationsBackend.review_tools | state.repair_allowed | Attribute for state.repair allowed in ApplicationsBackend.review_tools; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 1790 |
| ApplicationsBackend.review_tools | registry | Local binding for registry in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of registry_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 1804 |
| ApplicationsBackend.review_tools | tools | Local binding for tools in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1805 |
| ApplicationsBackend.review_tools | role | Loop item for role in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1806 |
| ApplicationsBackend.review_tools | tool | Loop item for tool in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1806 |
| ApplicationsBackend.review_tools | filename | Local binding for filename in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1807 |
| ApplicationsBackend.review_tools | manifest | Versioned inventory or launch record; not an execution-authorization capability. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 1831 |
| ApplicationsBackend.review_tools.comprehension_1832 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1834 |
| ApplicationsBackend.review_tools | item.digest | Attribute for item.digest in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of application_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 1839 |
| ApplicationsBackend.review_tools | item.identity | Attribute for item.identity in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1840 |
| ApplicationsBackend.review_tools.comprehension_1842 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 1843 |
| ApplicationsBackend.review_tools | item.review_text | Attribute for item.review text in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 1845 |
| ApplicationsBackend.review_tools | widget_check | Local binding for widget check in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1849 |
| ApplicationsBackend.review_tools | item.dependency_check | Attribute for item.dependency check in ApplicationsBackend.review_tools; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1857 |
| ApplicationsBackend.review_state | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1870 |
| ApplicationsBackend.review_state | token | Parameter for token in ApplicationsBackend.review_state; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 1870 |
| ApplicationsBackend.review_state | request | Parameter for request in ApplicationsBackend.review_state; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1870 |
| ApplicationsBackend.review_state | session | Local binding for session in ApplicationsBackend.review_state; use the enclosing contract and type below. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1872 |
| ApplicationsBackend.review_state | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of _resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 1872 |
| ApplicationsBackend.review_state | busy | Local binding for busy in ApplicationsBackend.review_state; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1873 |
| ApplicationsBackend.review_state | requirement | Local binding for requirement in ApplicationsBackend.review_state; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 1874 |
| ApplicationsBackend.review_state | requirement_message | Local binding for requirement message in ApplicationsBackend.review_state; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1875, 1878, 1880 |
| ApplicationsBackend.close_owner | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1898 |
| ApplicationsBackend.close_owner | owner | Parameter for owner in ApplicationsBackend.close_owner; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 1898 |
| ApplicationsBackend.close_owner | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Return type of pop; see its callable contract | Enclosing invocation or class/instance lifetime | 1901 |
| ApplicationsBackend.unload | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1905 |
| ApplicationsBackend.unload | request | Parameter for request in ApplicationsBackend.unload; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 1905 |
| ApplicationsBackend.close_all | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 1909 |
| ApplicationsBackend.close_all | states | Local binding for states in ApplicationsBackend.close_all; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 1912 |
| ApplicationsBackend.close_all | state | Owner-local mutable workflow/UI state guarded by its documented synchronization. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 1914 |
| ApplicationsBackend.close_all | error | Caught exception for error in ApplicationsBackend.close_all; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 1917 |
