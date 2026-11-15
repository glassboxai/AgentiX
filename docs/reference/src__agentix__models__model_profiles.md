# Reference for src/agentix/models/model_profiles.py

Validated session model profiles and explicit provider-client construction.

Profiles contain credential references, never API keys. Network resolution is an
injected boundary; HTTPS and public resolution checks reduce SSRF but do not
replace an outbound proxy against DNS rebinding. No import performs network IO.

Source fingerprint: f08251ff9e3c9fd4a910086220b3bb404b674cc349783765bf9c3cd8645e9eaa

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### resolve_addresses

Resolve a host through the OS; propagate lookup failure to the caller.

Kind: callable. Declared return: list[str]. Source line: 31.

### ModelProfile

Nonsecret provider choices; consent authorizes remote task transmission.

Attributes:
    provider: Closed provider choice, not an arbitrary SDK routing prefix.
    model: Bounded provider model name without a routing prefix.
    endpoint: Loopback Ollama root or HTTPS public API base URL.
    credential_ref: Opaque Windows Credential Manager target; hidden in repr.
    remote_consent: Explicit acknowledgement that task data leaves this PC.

Kind: class. Declared return: Not declared / class. Source line: 37.

### ModelProfile.validate

Reject malformed choices and unsafe URLs before any credential lookup.

DNS inspection is needed only for remote configuration. Raises ValueError
with fixed, secret-free messages. The caller controls explicit activation.

Kind: callable. Declared return: None. Source line: 54.

### ensure_configurable

Deny runtime replacement while an operation or human review is active.

Kind: callable. Declared return: None. Source line: 125.

### create_profile_llm

Build an explicitly configured bounded client; never set process env vars.

Vault and factory injection enable offline verification. Provider construction
errors are replaced with fixed messages because vendor exceptions can expose
request headers. Keys are used only by the owning in-memory SDK client.

Kind: callable. Declared return: Any. Source line: 136.

### SessionModelConfiguration

Own transactional provider changes and credentials for one UI controller.

The controller lock must cover configure/close. External factories are injected
at bootstrap; construction itself performs no credential or network operation.

Kind: class. Declared return: Not declared / class. Source line: 176.

### SessionModelConfiguration.__init__

Retain explicit boundaries and an initially local nonsecret profile.

Kind: callable. Declared return: None. Source line: 183.

### SessionModelConfiguration.configure

Validate, construct and atomically commit fresh services, or retain old ones.

Saved remote activation needs fresh consent, matching metadata and revision.
Unsaved compatibility callers may use an ephemeral session credential.
There is no API for revealing keys or changing process environment.

Kind: callable. Declared return: str. Source line: 212.

### SessionModelConfiguration.close

Forget session state; persisted user credentials require explicit deletion.

Kind: callable. Declared return: None. Source line: 282.

### SessionModelConfiguration._repository

Lazily open the injected user-local store; construction performs no IO.

Kind: callable. Declared return: Any. Source line: 288.

### SessionModelConfiguration.saved_choices

Expose only names and opaque IDs, never credential values or references.

Kind: callable. Declared return: list[tuple[str, str]]. Source line: 299.

### SessionModelConfiguration.select_saved

Select a validated record for this session without activating its model.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 305.

### SessionModelConfiguration.ensure_generation_identity

Capture a first-use local baseline or reject a changed trusted identity.

Only a selected saved local profile may own a baseline. This metadata read
performs no inference, model pull, or service start.

Kind: callable. Declared return: str. Source line: 313.

### SessionModelConfiguration.reset_generation_identity

Explicitly replace a changed local baseline after the user requests reset.

Kind: callable. Declared return: str. Source line: 337.

### SessionModelConfiguration.save_profile

Save selected metadata/key without giving remote data-transfer consent.

Kind: callable. Declared return: str. Source line: 355.

### SessionModelConfiguration.delete_profile

Delete the selected inactive profile; never silently stop active work.

Kind: callable. Declared return: str. Source line: 386.

### RemoteRequestPolicy

Recheck approved origins and DNS before each credential-bearing request.

Resolution and connection are distinct OS operations; a hostile DNS service
can still race them. An outbound enforcing proxy is needed to remove that gap.

Kind: class. Declared return: Not declared / class. Source line: 400.

### RemoteRequestPolicy.__init__

Retain nonsecret approved endpoint data and the resolver boundary.

Kind: callable. Declared return: None. Source line: 407.

### RemoteRequestPolicy.validate_url

Deny changed origins, paths, credentials or private resolution.

Kind: callable. Declared return: None. Source line: 411.

### RemoteRequestPolicy.validate_response

Never follow provider redirects or forward credentials to a new origin.

Kind: callable. Declared return: None. Source line: 428.

### remote_interceptor

Construct the installed CrewAI sync/async transport hook lazily.

CrewAI builds explicit HTTP transports for interceptors; HTTPX disables
environment proxy discovery when an explicit transport is supplied. This
integration is covered separately from offline policy checks.

Kind: callable. Declared return: Any. Source line: 434.

### remote_interceptor.Guard

Guard both synchronous and asynchronous provider network operations.

Kind: class. Declared return: Not declared / class. Source line: 445.

### remote_interceptor.Guard.on_outbound

Validate the final URL before transport sends headers and body.

Kind: callable. Declared return: Any. Source line: 448.

### remote_interceptor.Guard.on_inbound

Reject redirects before the client can process them.

Kind: callable. Declared return: Any. Source line: 453.

### remote_interceptor.Guard.aon_outbound

Apply the identical outbound policy to asynchronous calls.

Kind: callable. Declared return: Any. Source line: 458.

### remote_interceptor.Guard.aon_inbound

Apply the identical response policy to asynchronous calls.

Kind: callable. Declared return: Any. Source line: 462.

### installed_models

Read installed names from loopback /api/tags; never pull or run a model.

Ignore environment proxies, reject redirects, bound response bytes and timeout.
Reader injection supports deterministic offline tests without local services.

Kind: callable. Declared return: list[str]. Source line: 469.

### installed_models.NoRedirects

Deny all redirects away from the selected local Ollama origin.

Kind: class. Declared return: Not declared / class. Source line: 480.

### installed_models.NoRedirects.redirect_request

Return no replacement request, causing urllib to deny redirection.

Kind: callable. Declared return: None. Source line: 483.

### installed_models.read

Read one bounded JSON document from the fixed local endpoint.

Kind: callable. Declared return: dict[str, Any]. Source line: 489.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ipaddress | Imported dependency for ipaddress in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | socket | Imported dependency for socket in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | dataclass | Imported dependency for dataclass in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | field | Imported dependency for field in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | urlsplit | Imported dependency for urlsplit in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | MAX_MODEL_NAME_LENGTH | Module binding for MAX MODEL NAME LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 16 |
| module | MODEL_NAME_PATTERN | Module binding for MODEL NAME PATTERN in module; use the enclosing contract and type below. | Return type of compile; see its callable contract | Module/process lifetime | 17 |
| module | MAX_ENDPOINT_LENGTH | Module binding for MAX ENDPOINT LENGTH in module; use the enclosing contract and type below. | int | Module/process lifetime | 18 |
| module | MIN_PRINTABLE_CODE_POINT | Module binding for MIN PRINTABLE CODE POINT in module; use the enclosing contract and type below. | int | Module/process lifetime | 19 |
| module | DEFAULT_TEMPERATURE | Module binding for DEFAULT TEMPERATURE in module; use the enclosing contract and type below. | float | Module/process lifetime | 20 |
| module | REQUEST_TIMEOUT_SECONDS | Module binding for REQUEST TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 21 |
| module | MAX_OUTPUT_TOKENS | Module binding for MAX OUTPUT TOKENS in module; use the enclosing contract and type below. | int | Module/process lifetime | 22 |
| module | REDIRECT_STATUS_MIN | Module binding for REDIRECT STATUS MIN in module; use the enclosing contract and type below. | int | Module/process lifetime | 23 |
| module | REDIRECT_STATUS_MAX | Module binding for REDIRECT STATUS MAX in module; use the enclosing contract and type below. | int | Module/process lifetime | 24 |
| module | CATALOG_TIMEOUT_SECONDS | Module binding for CATALOG TIMEOUT SECONDS in module; use the enclosing contract and type below. | int | Module/process lifetime | 25 |
| module | CATALOG_MAX_BYTES | Module binding for CATALOG MAX BYTES in module; use the enclosing contract and type below. | int | Module/process lifetime | 26 |
| module | CATALOG_READ_BYTES | Module binding for CATALOG READ BYTES in module; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Module/process lifetime | 27 |
| module | MAX_CATALOG_MODELS | Module binding for MAX CATALOG MODELS in module; use the enclosing contract and type below. | int | Module/process lifetime | 28 |
| resolve_addresses | host | Parameter for host in resolve_addresses; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 31 |
| resolve_addresses.comprehension_33 | entry | Comprehension item for entry in resolve_addresses.comprehension_33; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 33 |
| ModelProfile | provider | Typed binding for provider in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 48 |
| ModelProfile | model | Typed binding for model in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 49 |
| ModelProfile | endpoint | Typed binding for endpoint in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 50 |
| ModelProfile | credential_ref | Typed binding for credential ref in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 51 |
| ModelProfile | remote_consent | Typed binding for remote consent in ModelProfile; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 52 |
| ModelProfile.validate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 54 |
| ModelProfile.validate | resolver | Parameter for resolver in ModelProfile.validate; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 54 |
| ModelProfile.validate.comprehension_73 | c | Comprehension item for c in ModelProfile.validate.comprehension_73; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 73 |
| ModelProfile.validate | url | Local binding for url in ModelProfile.validate; use the enclosing contract and type below. | Return type of urlsplit; see its callable contract | Enclosing invocation or class/instance lifetime | 77 |
| ModelProfile.validate | port | Local binding for port in ModelProfile.validate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| ModelProfile.validate | addresses | Local binding for addresses in ModelProfile.validate; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 108, 111 |
| ModelProfile.validate.comprehension_114 | address | Comprehension item for address in ModelProfile.validate.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 120 |
| ensure_configurable | controller | Parameter for controller in ensure_configurable; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 125 |
| create_profile_llm | profile | Parameter for profile in create_profile_llm; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 137 |
| create_profile_llm | vault | Parameter for vault in create_profile_llm; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 138 |
| create_profile_llm | factory | Parameter for factory in create_profile_llm; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 139, 154 |
| create_profile_llm | resolver | Parameter for resolver in create_profile_llm; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 141 |
| create_profile_llm | native_factory | Local binding for native factory in create_profile_llm; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 150 |
| create_profile_llm | LLM | Imported dependency for LLM in create_profile_llm; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 152 |
| create_profile_llm | options | Local binding for options in create_profile_llm; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 155 |
| create_profile_llm | key | Local binding for key in create_profile_llm; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 164 |
| SessionModelConfiguration.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 184 |
| SessionModelConfiguration.__init__ | controller | Parameter for controller in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 185 |
| SessionModelConfiguration.__init__ | runtime_factory | Parameter for runtime factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 186 |
| SessionModelConfiguration.__init__ | vault_factory | Parameter for vault factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 188 |
| SessionModelConfiguration.__init__ | llm_factory | Parameter for llm factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 189 |
| SessionModelConfiguration.__init__ | client | Parameter for client in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 190 |
| SessionModelConfiguration.__init__ | resolver | Parameter for resolver in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 191 |
| SessionModelConfiguration.__init__ | store_factory | Parameter for store factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.__init__ | catalog_reader | Parameter for catalog reader in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 193 |
| SessionModelConfiguration.__init__ | WindowsCredentialVault | Imported dependency for WindowsCredentialVault in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 196 |
| SessionModelConfiguration.__init__ | self.controller | Attribute for controller in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 198 |
| SessionModelConfiguration.__init__ | self.runtime_factory | Attribute for runtime factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 198 |
| SessionModelConfiguration.__init__ | self.vault_factory | Attribute for vault factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 199 |
| SessionModelConfiguration.__init__ | self.llm_factory | Attribute for llm factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 200 |
| SessionModelConfiguration.__init__ | self.resolver | Attribute for resolver in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 200 |
| SessionModelConfiguration.__init__ | self.vault | Attribute for vault in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 201 |
| SessionModelConfiguration.__init__ | self.client | Attribute for client in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 201 |
| SessionModelConfiguration.__init__ | self.profile | Attribute for profile in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 202 |
| SessionModelConfiguration.__init__ | self.catalog_reader | Attribute for catalog reader in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 203 |
| SessionModelConfiguration.__init__ | self.store_factory | Attribute for store factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 204 |
| SessionModelConfiguration.__init__ | self.store | Attribute for store in SessionModelConfiguration.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 205 |
| SessionModelConfiguration.__init__ | self.saved_id | Attribute for saved id in SessionModelConfiguration.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 206 |
| SessionModelConfiguration.__init__ | self.saved_version | Attribute for saved version in SessionModelConfiguration.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 207 |
| SessionModelConfiguration.__init__ | self.persistent_active | Attribute for persistent active in SessionModelConfiguration.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 208 |
| SessionModelConfiguration.__init__ | self.generation_digest | Attribute for generation digest in SessionModelConfiguration.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 209 |
| SessionModelConfiguration.__init__ | self.identity_reader | Attribute for identity reader in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 210 |
| SessionModelConfiguration.configure | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | provider | Parameter for provider in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | model | Parameter for model in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | endpoint | Parameter for endpoint in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | key | Parameter for key in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | consent | Parameter for consent in SessionModelConfiguration.configure; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 212 |
| SessionModelConfiguration.configure | uuid4 | Imported dependency for uuid4 in SessionModelConfiguration.configure; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 219 |
| SessionModelConfiguration.configure | candidate | Local binding for candidate in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 222, 241, 253 |
| SessionModelConfiguration.configure | reference | Local binding for reference in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 224, 251 |
| SessionModelConfiguration.configure | persistent | Local binding for persistent in SessionModelConfiguration.configure; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 225, 237, 244 |
| SessionModelConfiguration.configure | generation_digest | Local binding for generation digest in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 226, 236 |
| SessionModelConfiguration.configure | saved | Local binding for saved in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 228 |
| SessionModelConfiguration.configure | self.vault | Attribute for vault in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 250 |
| SessionModelConfiguration.configure | client | Local binding for client in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of create_profile_llm; see its callable contract | Enclosing invocation or class/instance lifetime | 254 |
| SessionModelConfiguration.configure | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of runtime_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
| SessionModelConfiguration.configure | self.controller.run_system | Attribute for controller.run system in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 272 |
| SessionModelConfiguration.configure | self.controller.validation | Attribute for controller.validation in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 273 |
| SessionModelConfiguration.configure | self.controller.tool_operations | Attribute for controller.tool operations in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 274 |
| SessionModelConfiguration.configure | self.controller.get_installed_tools_catalog | Attribute for controller.get installed tools catalog in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 275 |
| SessionModelConfiguration.configure | self.client | Attribute for client in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 276 |
| SessionModelConfiguration.configure | self.profile | Attribute for profile in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 277 |
| SessionModelConfiguration.configure | self.generation_digest | Attribute for generation digest in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 278 |
| SessionModelConfiguration.configure | self.persistent_active | Attribute for persistent active in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 279 |
| SessionModelConfiguration.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 282 |
| SessionModelConfiguration.close | self.profile | Attribute for profile in SessionModelConfiguration.close; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 286 |
| SessionModelConfiguration._repository | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 288 |
| SessionModelConfiguration._repository | DeferredCredentialVault | Imported dependency for DeferredCredentialVault in SessionModelConfiguration._repository; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 293 |
| SessionModelConfiguration._repository | self.vault | Attribute for vault in SessionModelConfiguration._repository; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 295 |
| SessionModelConfiguration._repository | self.store | Attribute for store in SessionModelConfiguration._repository; use the enclosing contract and type below. | Return type of store_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 296 |
| SessionModelConfiguration.saved_choices | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 299 |
| SessionModelConfiguration.saved_choices.comprehension_301 | record | Comprehension item for record in SessionModelConfiguration.saved_choices.comprehension_301; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 302 |
| SessionModelConfiguration.select_saved | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 305 |
| SessionModelConfiguration.select_saved | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 305 |
| SessionModelConfiguration.select_saved | record | Local binding for record in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 308 |
| SessionModelConfiguration.select_saved | self.saved_id | Attribute for saved id in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 309 |
| SessionModelConfiguration.select_saved | self.saved_version | Attribute for saved version in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 310 |
| SessionModelConfiguration.ensure_generation_identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 313 |
| SessionModelConfiguration.ensure_generation_identity | read_generation_identity | Imported dependency for read generation identity in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 319 |
| SessionModelConfiguration.ensure_generation_identity | ProfileError | Imported dependency for ProfileError in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 320 |
| SessionModelConfiguration.ensure_generation_identity | current | Local binding for current in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 325 |
| SessionModelConfiguration.ensure_generation_identity | record | Local binding for record in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Return type of trust_generation_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| SessionModelConfiguration.ensure_generation_identity | self.saved_version | Attribute for saved version in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 333 |
| SessionModelConfiguration.ensure_generation_identity | self.generation_digest | Attribute for generation digest in SessionModelConfiguration.ensure_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 334 |
| SessionModelConfiguration.reset_generation_identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 337 |
| SessionModelConfiguration.reset_generation_identity | read_generation_identity | Imported dependency for read generation identity in SessionModelConfiguration.reset_generation_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 339 |
| SessionModelConfiguration.reset_generation_identity | current | Local binding for current in SessionModelConfiguration.reset_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 343 |
| SessionModelConfiguration.reset_generation_identity | record | Local binding for record in SessionModelConfiguration.reset_generation_identity; use the enclosing contract and type below. | Return type of trust_generation_digest; see its callable contract | Enclosing invocation or class/instance lifetime | 348 |
| SessionModelConfiguration.reset_generation_identity | self.saved_version | Attribute for saved version in SessionModelConfiguration.reset_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 351 |
| SessionModelConfiguration.reset_generation_identity | self.generation_digest | Attribute for generation digest in SessionModelConfiguration.reset_generation_identity; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 352 |
| SessionModelConfiguration.save_profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 356 |
| SessionModelConfiguration.save_profile | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 357 |
| SessionModelConfiguration.save_profile | provider | Parameter for provider in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 358 |
| SessionModelConfiguration.save_profile | model | Parameter for model in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 359 |
| SessionModelConfiguration.save_profile | endpoint | Parameter for endpoint in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 360 |
| SessionModelConfiguration.save_profile | key | Parameter for key in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 361 |
| SessionModelConfiguration.save_profile | ProfileError | Imported dependency for ProfileError in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 365 |
| SessionModelConfiguration.save_profile | saved | Local binding for saved in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 368 |
| SessionModelConfiguration.save_profile | error | Caught exception for error in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | OSError | Current exception handler; Python clears this binding afterward | 377 |
| SessionModelConfiguration.save_profile | self.saved_id | Attribute for saved id in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 379 |
| SessionModelConfiguration.save_profile | self.saved_version | Attribute for saved version in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 379 |
| SessionModelConfiguration.delete_profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 386 |
| SessionModelConfiguration.delete_profile | self.saved_id | Attribute for saved id in SessionModelConfiguration.delete_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 396 |
| SessionModelConfiguration.delete_profile | self.saved_version | Attribute for saved version in SessionModelConfiguration.delete_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 396 |
| RemoteRequestPolicy.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 407 |
| RemoteRequestPolicy.__init__ | profile | Parameter for profile in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 407 |
| RemoteRequestPolicy.__init__ | resolver | Parameter for resolver in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 407 |
| RemoteRequestPolicy.__init__ | self.profile | Attribute for profile in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 409 |
| RemoteRequestPolicy.__init__ | self.resolver | Attribute for resolver in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 409 |
| RemoteRequestPolicy.validate_url | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 411 |
| RemoteRequestPolicy.validate_url | destination | Parameter for destination in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 411 |
| RemoteRequestPolicy.validate_url | approved | Local binding for approved in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 414 |
| RemoteRequestPolicy.validate_url | target | Local binding for target in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 414 |
| RemoteRequestPolicy.validate_url | prefix | Local binding for prefix in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 424 |
| RemoteRequestPolicy.validate_response | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 428 |
| RemoteRequestPolicy.validate_response | status | Parameter for status in RemoteRequestPolicy.validate_response; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 428 |
| remote_interceptor | profile | Parameter for profile in remote_interceptor; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 434 |
| remote_interceptor | resolver | Parameter for resolver in remote_interceptor; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 434 |
| remote_interceptor | BaseInterceptor | Imported dependency for BaseInterceptor in remote_interceptor; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 441 |
| remote_interceptor | policy | Local binding for policy in remote_interceptor; use the enclosing contract and type below. | Return type of RemoteRequestPolicy; see its callable contract | Enclosing invocation or class/instance lifetime | 443 |
| remote_interceptor.Guard.on_outbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 448 |
| remote_interceptor.Guard.on_outbound | message | Parameter for message in remote_interceptor.Guard.on_outbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 448 |
| remote_interceptor.Guard.on_inbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 453 |
| remote_interceptor.Guard.on_inbound | message | Parameter for message in remote_interceptor.Guard.on_inbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 453 |
| remote_interceptor.Guard.aon_outbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 458 |
| remote_interceptor.Guard.aon_outbound | message | Parameter for message in remote_interceptor.Guard.aon_outbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 458 |
| remote_interceptor.Guard.aon_inbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 462 |
| remote_interceptor.Guard.aon_inbound | message | Parameter for message in remote_interceptor.Guard.aon_inbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 462 |
| installed_models | endpoint | Parameter for endpoint in installed_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 469 |
| installed_models | reader | Parameter for reader in installed_models; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 469 |
| installed_models | json | Imported dependency for json in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 475 |
| installed_models | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 476 |
| installed_models | ProxyHandler | Imported dependency for ProxyHandler in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 476 |
| installed_models | build_opener | Imported dependency for build opener in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 476 |
| installed_models.NoRedirects.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | req | Parameter for req in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | fp | Parameter for fp in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | code | Source snapshot passed through approval, syntax checks and isolated staging. | int | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | msg | Parameter for msg in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | headers | Parameter for headers in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.NoRedirects.redirect_request | newurl | Parameter for newurl in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 484 |
| installed_models.read | url | Parameter for url in installed_models.read; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 489 |
| installed_models.read | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 491 |
| installed_models.read | payload | Local binding for payload in installed_models.read; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 494 |
| installed_models | data | Local binding for data in installed_models; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 500 |
| installed_models | names | Local binding for names in installed_models; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 507 |
| installed_models | item | Loop item for item in installed_models; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 508 |
| installed_models | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 511 |
