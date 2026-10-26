# Reference for src/agentix/model_profiles.py

Validated session model profiles and explicit provider-client construction.

Profiles contain credential references, never API keys. Network resolution is an
injected boundary; HTTPS and public resolution checks reduce SSRF but do not
replace an outbound proxy against DNS rebinding. No import performs network IO.

Source fingerprint: 91ed13b9a785423ee9d2f5b562a959397cb21c5c1a24a0dbe31a8d9351fe0392

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### resolve_addresses

Resolve a host through the OS; propagate lookup failure to the caller.

Kind: callable. Declared return: list[str]. Source line: 17.

### ModelProfile

Nonsecret provider choices; consent authorizes remote task transmission.

Attributes:
    provider: Closed provider choice, not an arbitrary SDK routing prefix.
    model: Bounded provider model name without a routing prefix.
    endpoint: Loopback Ollama root or HTTPS public API base URL.
    credential_ref: Opaque Windows Credential Manager target; hidden in repr.
    remote_consent: Explicit acknowledgement that task data leaves this PC.

Kind: class. Declared return: Not declared / class. Source line: 23.

### ModelProfile.validate

Reject malformed choices and unsafe URLs before any credential lookup.

DNS inspection is needed only for remote configuration. Raises ValueError
with fixed, secret-free messages. The caller controls explicit activation.

Kind: callable. Declared return: None. Source line: 40.

### ensure_configurable

Deny runtime replacement while an operation or human review is active.

Kind: callable. Declared return: None. Source line: 111.

### create_profile_llm

Build an explicitly configured bounded client; never set process env vars.

Vault and factory injection enable offline verification. Provider construction
errors are replaced with fixed messages because vendor exceptions can expose
request headers. Keys are used only by the owning in-memory SDK client.

Kind: callable. Declared return: Any. Source line: 119.

### SessionModelConfiguration

Own transactional provider changes and credentials for one UI controller.

The controller lock must cover configure/close. External factories are injected
at bootstrap; construction itself performs no credential or network operation.

Kind: class. Declared return: Not declared / class. Source line: 159.

### SessionModelConfiguration.__init__

Retain explicit boundaries and an initially local nonsecret profile.

Kind: callable. Declared return: None. Source line: 166.

### SessionModelConfiguration.configure

Validate, construct and atomically commit fresh services, or retain old ones.

Saved remote activation needs fresh consent, matching metadata and revision.
Unsaved compatibility callers may use an ephemeral session credential.
There is no API for revealing keys or changing process environment.

Kind: callable. Declared return: str. Source line: 192.

### SessionModelConfiguration.close

Forget session state; persisted user credentials require explicit deletion.

Kind: callable. Declared return: None. Source line: 249.

### SessionModelConfiguration._repository

Lazily open the injected user-local store; construction performs no IO.

Kind: callable. Declared return: Any. Source line: 255.

### SessionModelConfiguration.saved_choices

Expose only names and opaque IDs, never credential values or references.

Kind: callable. Declared return: list[tuple[str, str]]. Source line: 266.

### SessionModelConfiguration.select_saved

Select a validated record for this session without activating its model.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 272.

### SessionModelConfiguration.save_profile

Save selected metadata/key without giving remote data-transfer consent.

Kind: callable. Declared return: str. Source line: 280.

### SessionModelConfiguration.delete_profile

Delete the selected inactive profile; never silently stop active work.

Kind: callable. Declared return: str. Source line: 298.

### RemoteRequestPolicy

Recheck approved origins and DNS before each credential-bearing request.

Resolution and connection are distinct OS operations; a hostile DNS service
can still race them. An outbound enforcing proxy is needed to remove that gap.

Kind: class. Declared return: Not declared / class. Source line: 312.

### RemoteRequestPolicy.__init__

Retain nonsecret approved endpoint data and the resolver boundary.

Kind: callable. Declared return: None. Source line: 319.

### RemoteRequestPolicy.validate_url

Deny changed origins, paths, credentials or private resolution.

Kind: callable. Declared return: None. Source line: 323.

### RemoteRequestPolicy.validate_response

Never follow provider redirects or forward credentials to a new origin.

Kind: callable. Declared return: None. Source line: 340.

### remote_interceptor

Construct the installed CrewAI sync/async transport hook lazily.

CrewAI builds explicit HTTP transports for interceptors; HTTPX disables
environment proxy discovery when an explicit transport is supplied. This
integration is covered separately from offline policy checks.

Kind: callable. Declared return: Any. Source line: 346.

### remote_interceptor.Guard

Guard both synchronous and asynchronous provider network operations.

Kind: class. Declared return: Not declared / class. Source line: 357.

### remote_interceptor.Guard.on_outbound

Validate the final URL before transport sends headers and body.

Kind: callable. Declared return: Any. Source line: 360.

### remote_interceptor.Guard.on_inbound

Reject redirects before the client can process them.

Kind: callable. Declared return: Any. Source line: 365.

### remote_interceptor.Guard.aon_outbound

Apply the identical outbound policy to asynchronous calls.

Kind: callable. Declared return: Any. Source line: 370.

### remote_interceptor.Guard.aon_inbound

Apply the identical response policy to asynchronous calls.

Kind: callable. Declared return: Any. Source line: 374.

### installed_models

Read installed names from loopback /api/tags; never pull or run a model.

Ignore environment proxies, reject redirects, bound response bytes and timeout.
Reader injection supports deterministic offline tests without local services.

Kind: callable. Declared return: list[str]. Source line: 381.

### installed_models.NoRedirects

Deny all redirects away from the selected local Ollama origin.

Kind: class. Declared return: Not declared / class. Source line: 392.

### installed_models.NoRedirects.redirect_request

Return no replacement request, causing urllib to deny redirection.

Kind: callable. Declared return: None. Source line: 395.

### installed_models.read

Read one bounded JSON document from the fixed local endpoint.

Kind: callable. Declared return: dict[str, Any]. Source line: 401.

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
| resolve_addresses | host | Parameter for host in resolve_addresses; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 17 |
| resolve_addresses.comprehension_19 | entry | Comprehension item for entry in resolve_addresses.comprehension_19; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 19 |
| ModelProfile | provider | Typed binding for provider in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| ModelProfile | model | Typed binding for model in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 35 |
| ModelProfile | endpoint | Typed binding for endpoint in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 36 |
| ModelProfile | credential_ref | Typed binding for credential ref in ModelProfile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 37 |
| ModelProfile | remote_consent | Typed binding for remote consent in ModelProfile; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 38 |
| ModelProfile.validate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 40 |
| ModelProfile.validate | resolver | Parameter for resolver in ModelProfile.validate; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 40 |
| ModelProfile.validate.comprehension_59 | c | Comprehension item for c in ModelProfile.validate.comprehension_59; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 59 |
| ModelProfile.validate | url | Local binding for url in ModelProfile.validate; use the enclosing contract and type below. | Return type of urlsplit; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| ModelProfile.validate | port | Local binding for port in ModelProfile.validate; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 64 |
| ModelProfile.validate | addresses | Local binding for addresses in ModelProfile.validate; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 94, 97 |
| ModelProfile.validate.comprehension_100 | address | Comprehension item for address in ModelProfile.validate.comprehension_100; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 106 |
| ensure_configurable | controller | Parameter for controller in ensure_configurable; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 111 |
| create_profile_llm | profile | Parameter for profile in create_profile_llm; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 120 |
| create_profile_llm | vault | Parameter for vault in create_profile_llm; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 121 |
| create_profile_llm | factory | Parameter for factory in create_profile_llm; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 122, 137 |
| create_profile_llm | resolver | Parameter for resolver in create_profile_llm; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 124 |
| create_profile_llm | native_factory | Local binding for native factory in create_profile_llm; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 133 |
| create_profile_llm | LLM | Imported dependency for LLM in create_profile_llm; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 135 |
| create_profile_llm | options | Local binding for options in create_profile_llm; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| create_profile_llm | key | Local binding for key in create_profile_llm; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 147 |
| SessionModelConfiguration.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 167 |
| SessionModelConfiguration.__init__ | controller | Parameter for controller in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 168 |
| SessionModelConfiguration.__init__ | runtime_factory | Parameter for runtime factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 169 |
| SessionModelConfiguration.__init__ | vault_factory | Parameter for vault factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 171 |
| SessionModelConfiguration.__init__ | llm_factory | Parameter for llm factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 172 |
| SessionModelConfiguration.__init__ | resolver | Parameter for resolver in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 173 |
| SessionModelConfiguration.__init__ | store_factory | Parameter for store factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 174 |
| SessionModelConfiguration.__init__ | catalog_reader | Parameter for catalog reader in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 175 |
| SessionModelConfiguration.__init__ | WindowsCredentialVault | Imported dependency for WindowsCredentialVault in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 178 |
| SessionModelConfiguration.__init__ | self.controller | Attribute for controller in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 180 |
| SessionModelConfiguration.__init__ | self.runtime_factory | Attribute for runtime factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 180 |
| SessionModelConfiguration.__init__ | self.vault_factory | Attribute for vault factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 181 |
| SessionModelConfiguration.__init__ | self.llm_factory | Attribute for llm factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 182 |
| SessionModelConfiguration.__init__ | self.resolver | Attribute for resolver in SessionModelConfiguration.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 182 |
| SessionModelConfiguration.__init__ | self.vault | Attribute for vault in SessionModelConfiguration.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 183 |
| SessionModelConfiguration.__init__ | self.profile | Attribute for profile in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 184 |
| SessionModelConfiguration.__init__ | self.catalog_reader | Attribute for catalog reader in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 185 |
| SessionModelConfiguration.__init__ | self.store_factory | Attribute for store factory in SessionModelConfiguration.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 186 |
| SessionModelConfiguration.__init__ | self.store | Attribute for store in SessionModelConfiguration.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 187 |
| SessionModelConfiguration.__init__ | self.saved_id | Attribute for saved id in SessionModelConfiguration.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 188 |
| SessionModelConfiguration.__init__ | self.saved_version | Attribute for saved version in SessionModelConfiguration.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 189 |
| SessionModelConfiguration.__init__ | self.persistent_active | Attribute for persistent active in SessionModelConfiguration.__init__; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 190 |
| SessionModelConfiguration.configure | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | provider | Parameter for provider in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | model | Parameter for model in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | endpoint | Parameter for endpoint in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | key | Parameter for key in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | consent | Parameter for consent in SessionModelConfiguration.configure; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 192 |
| SessionModelConfiguration.configure | uuid4 | Imported dependency for uuid4 in SessionModelConfiguration.configure; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 199 |
| SessionModelConfiguration.configure | candidate | Local binding for candidate in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 202, 216, 223 |
| SessionModelConfiguration.configure | reference | Local binding for reference in SessionModelConfiguration.configure; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 204, 221 |
| SessionModelConfiguration.configure | persistent | Local binding for persistent in SessionModelConfiguration.configure; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 205, 217 |
| SessionModelConfiguration.configure | saved | Local binding for saved in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of get; see its callable contract | Enclosing invocation or class/instance lifetime | 209 |
| SessionModelConfiguration.configure | self.vault | Attribute for vault in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 220 |
| SessionModelConfiguration.configure | client | Local binding for client in SessionModelConfiguration.configure; use the enclosing contract and type below. | Return type of create_profile_llm; see its callable contract | Enclosing invocation or class/instance lifetime | 224 |
| SessionModelConfiguration.configure | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of runtime_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 227 |
| SessionModelConfiguration.configure | self.controller.run_system | Attribute for controller.run system in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 242 |
| SessionModelConfiguration.configure | self.controller.validation | Attribute for controller.validation in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 243 |
| SessionModelConfiguration.configure | self.controller.get_installed_tools_catalog | Attribute for controller.get installed tools catalog in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 244 |
| SessionModelConfiguration.configure | self.profile | Attribute for profile in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 245 |
| SessionModelConfiguration.configure | self.persistent_active | Attribute for persistent active in SessionModelConfiguration.configure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 246 |
| SessionModelConfiguration.close | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 249 |
| SessionModelConfiguration.close | self.profile | Attribute for profile in SessionModelConfiguration.close; use the enclosing contract and type below. | Return type of ModelProfile; see its callable contract | Enclosing invocation or class/instance lifetime | 253 |
| SessionModelConfiguration._repository | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 255 |
| SessionModelConfiguration._repository | DeferredCredentialVault | Imported dependency for DeferredCredentialVault in SessionModelConfiguration._repository; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 260 |
| SessionModelConfiguration._repository | self.vault | Attribute for vault in SessionModelConfiguration._repository; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 262 |
| SessionModelConfiguration._repository | self.store | Attribute for store in SessionModelConfiguration._repository; use the enclosing contract and type below. | Return type of store_factory; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| SessionModelConfiguration.saved_choices | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 266 |
| SessionModelConfiguration.saved_choices.comprehension_268 | record | Comprehension item for record in SessionModelConfiguration.saved_choices.comprehension_268; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 269 |
| SessionModelConfiguration.select_saved | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 272 |
| SessionModelConfiguration.select_saved | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 272 |
| SessionModelConfiguration.select_saved | record | Local binding for record in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 275 |
| SessionModelConfiguration.select_saved | self.saved_id | Attribute for saved id in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 276 |
| SessionModelConfiguration.select_saved | self.saved_version | Attribute for saved version in SessionModelConfiguration.select_saved; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 277 |
| SessionModelConfiguration.save_profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | provider | Parameter for provider in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | model | Parameter for model in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | endpoint | Parameter for endpoint in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | key | Parameter for key in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 280 |
| SessionModelConfiguration.save_profile | ProfileError | Imported dependency for ProfileError in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 283 |
| SessionModelConfiguration.save_profile | saved | Local binding for saved in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | Return type of save; see its callable contract | Enclosing invocation or class/instance lifetime | 286 |
| SessionModelConfiguration.save_profile | error | Caught exception for error in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | OSError | Current exception handler; Python clears this binding afterward | 289 |
| SessionModelConfiguration.save_profile | self.saved_id | Attribute for saved id in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 291 |
| SessionModelConfiguration.save_profile | self.saved_version | Attribute for saved version in SessionModelConfiguration.save_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 291 |
| SessionModelConfiguration.delete_profile | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 298 |
| SessionModelConfiguration.delete_profile | self.saved_id | Attribute for saved id in SessionModelConfiguration.delete_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 308 |
| SessionModelConfiguration.delete_profile | self.saved_version | Attribute for saved version in SessionModelConfiguration.delete_profile; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 308 |
| RemoteRequestPolicy.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 319 |
| RemoteRequestPolicy.__init__ | profile | Parameter for profile in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 319 |
| RemoteRequestPolicy.__init__ | resolver | Parameter for resolver in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 319 |
| RemoteRequestPolicy.__init__ | self.profile | Attribute for profile in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 321 |
| RemoteRequestPolicy.__init__ | self.resolver | Attribute for resolver in RemoteRequestPolicy.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 321 |
| RemoteRequestPolicy.validate_url | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 323 |
| RemoteRequestPolicy.validate_url | destination | Parameter for destination in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 323 |
| RemoteRequestPolicy.validate_url | approved | Local binding for approved in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 326 |
| RemoteRequestPolicy.validate_url | target | Local binding for target in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 326 |
| RemoteRequestPolicy.validate_url | prefix | Local binding for prefix in RemoteRequestPolicy.validate_url; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 336 |
| RemoteRequestPolicy.validate_response | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 340 |
| RemoteRequestPolicy.validate_response | status | Parameter for status in RemoteRequestPolicy.validate_response; use the enclosing contract and type below. | int | Enclosing invocation or class/instance lifetime | 340 |
| remote_interceptor | profile | Parameter for profile in remote_interceptor; use the enclosing contract and type below. | ModelProfile | Enclosing invocation or class/instance lifetime | 346 |
| remote_interceptor | resolver | Parameter for resolver in remote_interceptor; use the enclosing contract and type below. | Callable | Enclosing invocation or class/instance lifetime | 346 |
| remote_interceptor | BaseInterceptor | Imported dependency for BaseInterceptor in remote_interceptor; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 353 |
| remote_interceptor | policy | Local binding for policy in remote_interceptor; use the enclosing contract and type below. | Return type of RemoteRequestPolicy; see its callable contract | Enclosing invocation or class/instance lifetime | 355 |
| remote_interceptor.Guard.on_outbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 360 |
| remote_interceptor.Guard.on_outbound | message | Parameter for message in remote_interceptor.Guard.on_outbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 360 |
| remote_interceptor.Guard.on_inbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 365 |
| remote_interceptor.Guard.on_inbound | message | Parameter for message in remote_interceptor.Guard.on_inbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 365 |
| remote_interceptor.Guard.aon_outbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 370 |
| remote_interceptor.Guard.aon_outbound | message | Parameter for message in remote_interceptor.Guard.aon_outbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 370 |
| remote_interceptor.Guard.aon_inbound | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 374 |
| remote_interceptor.Guard.aon_inbound | message | Parameter for message in remote_interceptor.Guard.aon_inbound; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 374 |
| installed_models | endpoint | Parameter for endpoint in installed_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 381 |
| installed_models | reader | Parameter for reader in installed_models; use the enclosing contract and type below. | Callable &#124; None | Enclosing invocation or class/instance lifetime | 381 |
| installed_models | json | Imported dependency for json in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 387 |
| installed_models | HTTPRedirectHandler | Imported dependency for HTTPRedirectHandler in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 388 |
| installed_models | ProxyHandler | Imported dependency for ProxyHandler in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 388 |
| installed_models | build_opener | Imported dependency for build opener in installed_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 388 |
| installed_models.NoRedirects.redirect_request | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | req | Parameter for req in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | fp | Parameter for fp in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | code | Source snapshot passed through approval, syntax checks and isolated staging. | int | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | msg | Parameter for msg in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | headers | Parameter for headers in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.NoRedirects.redirect_request | newurl | Parameter for newurl in installed_models.NoRedirects.redirect_request; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 396 |
| installed_models.read | url | Parameter for url in installed_models.read; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 401 |
| installed_models.read | response | Bounded response text to render or validate; it is not executable code. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 403 |
| installed_models.read | payload | Local binding for payload in installed_models.read; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 404 |
| installed_models | data | Local binding for data in installed_models; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 410 |
| installed_models | names | Local binding for names in installed_models; use the enclosing contract and type below. | Return type of set; see its callable contract | Enclosing invocation or class/instance lifetime | 417 |
| installed_models | item | Loop item for item in installed_models; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 418 |
| installed_models | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 421 |
