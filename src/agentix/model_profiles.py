"""Validated session model profiles and explicit provider-client construction.

Profiles contain credential references, never API keys. Network resolution is an
injected boundary; HTTPS and public resolution checks reduce SSRF but do not
replace an outbound proxy against DNS rebinding. No import performs network IO.
"""

import ipaddress
import re
import socket
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlsplit


def resolve_addresses(host: str) -> list[str]:
    """Resolve a host through the OS; propagate lookup failure to the caller."""
    return list({entry[4][0] for entry in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)})


@dataclass(frozen=True)
class ModelProfile:
    """Nonsecret provider choices; consent authorizes remote task transmission.

    Attributes:
        provider: Closed provider choice, not an arbitrary SDK routing prefix.
        model: Bounded provider model name without a routing prefix.
        endpoint: Loopback Ollama root or HTTPS public API base URL.
        credential_ref: Opaque Windows Credential Manager target; hidden in repr.
        remote_consent: Explicit acknowledgement that task data leaves this PC.
    """

    provider: str = "Ollama"
    model: str = "qwen3-coder:30b"
    endpoint: str = "http://127.0.0.1:11434"
    credential_ref: str = field(default="", repr=False)
    remote_consent: bool = False

    def validate(self, resolver: Callable = resolve_addresses) -> None:
        """Reject malformed choices and unsafe URLs before any credential lookup.

        DNS inspection is needed only for remote configuration. Raises ValueError
        with fixed, secret-free messages. The caller controls explicit activation.
        """
        if self.provider not in ("Ollama", "OpenAI", "OpenAI-compatible"):
            raise ValueError("Unsupported model provider")
        if (
            not isinstance(self.model, str)
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_./:-]{0,199}", self.model)
            or ".." in self.model
            or "//" in self.model
            or self.model.endswith("/")
        ):
            raise ValueError("Invalid model name")
        if (
            not isinstance(self.endpoint, str)
            or len(self.endpoint) > 2048
            or any(ord(c) < 33 for c in self.endpoint)
        ):
            raise ValueError("Invalid provider endpoint")
        try:
            url = urlsplit(self.endpoint)
            port = url.port
        except ValueError:
            raise ValueError("Invalid provider endpoint") from None
        if (
            not url.hostname
            or url.username
            or url.password
            or url.query
            or url.fragment
            or "%" in url.netloc
            or "\\" in self.endpoint
        ):
            raise ValueError("Provider endpoint must not contain credentials or URL payloads")
        if self.provider == "Ollama":
            if (
                url.scheme != "http"
                or url.hostname not in ("localhost", "127.0.0.1", "::1")
                or url.path not in ("", "/")
            ):
                raise ValueError("Ollama requires a plain HTTP loopback endpoint")
            return
        if self.remote_consent is not True:
            raise ValueError("Explicit remote data consent is required")
        if url.scheme != "https" or port not in (None, 443):
            raise ValueError("Remote providers require HTTPS on port 443")
        if self.provider == "OpenAI" and (
            url.hostname != "api.openai.com" or url.path.rstrip("/") != "/v1"
        ):
            raise ValueError("OpenAI requires its official API endpoint")
        try:
            addresses = [str(ipaddress.ip_address(url.hostname))]
        except ValueError:
            try:
                addresses = resolver(url.hostname)
            except Exception:
                raise ValueError("Provider address could not be validated") from None
        if not addresses or any(
            (
                not ipaddress.ip_address(address).is_global
                or ipaddress.ip_address(address).is_multicast
                or ipaddress.ip_address(address).is_reserved
            )
            for address in addresses
        ):
            raise ValueError("Remote provider must resolve only to public addresses")


def ensure_configurable(controller: Any) -> None:
    """Deny runtime replacement while an operation or human review is active."""
    if controller.state.is_running:
        raise ValueError("Finish the current operation before changing models")
    if controller.security.get_pending_request():
        raise ValueError("Complete the pending review before changing models")


def create_profile_llm(
    profile: ModelProfile,
    vault: Any,
    factory: Callable | None = None,
    *,
    resolver: Callable = resolve_addresses,
) -> Any:
    """Build an explicitly configured bounded client; never set process env vars.

    Vault and factory injection enable offline verification. Provider construction
    errors are replaced with fixed messages because vendor exceptions can expose
    request headers. Keys are used only by the owning in-memory SDK client.
    """
    profile.validate(resolver)
    native_factory = factory is None
    if factory is None:
        from crewai import LLM

        factory = LLM
    options = dict(
        model=("ollama/" if profile.provider == "Ollama" else "openai/") + profile.model,
        base_url=profile.endpoint,
        temperature=0.2,
        timeout=120,
        max_tokens=8192,
        max_retries=0,
    )
    if profile.provider != "Ollama":
        key = vault.read(profile.credential_ref)
        if not key:
            raise ValueError("An API credential is required")
        options["api_key"] = key
        if native_factory:
            options["interceptor"] = remote_interceptor(profile, resolver)
    try:
        return factory(**options)
    except Exception:
        raise ValueError("Model client could not be initialized; check provider settings") from None


class SessionModelConfiguration:
    """Own transactional provider changes and credentials for one UI controller.

    The controller lock must cover configure/close. External factories are injected
    at bootstrap; construction itself performs no credential or network operation.
    """

    def __init__(
        self,
        controller: Any,
        runtime_factory: Callable,
        *,
        vault_factory: Callable | None = None,
        llm_factory: Callable | None = None,
        resolver: Callable = resolve_addresses,
        store_factory: Callable | None = None,
        catalog_reader: Callable | None = None,
    ) -> None:
        """Retain explicit boundaries and an initially local nonsecret profile."""
        from .credentials import WindowsCredentialVault

        self.controller, self.runtime_factory = controller, runtime_factory
        self.vault_factory = vault_factory or WindowsCredentialVault
        self.llm_factory, self.resolver = llm_factory, resolver
        self.vault = None
        self.profile = ModelProfile()
        self.catalog_reader = catalog_reader
        self.store_factory = store_factory
        self.store = None
        self.saved_id = ""
        self.saved_version = None
        self.persistent_active = False

    def configure(self, provider: str, model: str, endpoint: str, key: str, consent: bool) -> str:
        """Validate, construct and atomically commit fresh services, or retain old ones.

        Saved remote activation needs fresh consent, matching metadata and revision.
        Unsaved compatibility callers may use an ephemeral session credential.
        There is no API for revealing keys or changing process environment.
        """
        from uuid import uuid4

        ensure_configurable(self.controller)
        candidate = ModelProfile(provider, model, endpoint, remote_consent=consent)
        candidate.validate(self.resolver)
        reference = ""
        persistent = False
        if provider != "Ollama" and self.store_factory is not None:
            if key or not self.saved_id:
                raise ValueError("Save the external profile before activating it")
            saved = self._repository().get(self.saved_id)
            if saved["version"] != self.saved_version or (
                saved["provider"],
                saved["model"],
                saved["endpoint"],
            ) != (provider, model, endpoint):
                raise ValueError("Save or reload the changed profile before activation")
            candidate = ModelProfile(provider, model, endpoint, saved["credential_ref"], consent)
            persistent = True
        try:
            if provider != "Ollama" and not persistent:
                self.vault = self.vault or self.vault_factory()
                reference = f"AgentiX/v3/{self.controller.state.session_id}/{uuid4().hex}"
                self.vault.write(reference, key)
                candidate = ModelProfile(provider, model, endpoint, reference, consent)
            client = create_profile_llm(
                candidate, self.vault, self.llm_factory, resolver=self.resolver
            )
            runtime = self.runtime_factory(client)
        except Exception:
            if reference and self.vault:
                self.vault.delete(reference)
            raise ValueError("Model configuration failed; previous settings are retained") from None
        # Do not publish the new runtime until the old credential can be removed.
        if self.profile.credential_ref and self.vault and not self.persistent_active:
            try:
                self.vault.delete(self.profile.credential_ref)
            except Exception:
                if reference:
                    self.vault.delete(reference)
                raise ValueError(
                    "Credential cleanup failed; previous settings are retained"
                ) from None
        self.controller.run_system = runtime.orchestrator.run_system
        self.controller.validation = runtime.operations.acceptance
        self.controller.get_installed_tools_catalog = runtime.catalog.render
        self.profile = candidate
        self.persistent_active = persistent
        return f"Active provider: {provider}. Model: {model}. Previous validation must be repeated."

    def close(self) -> None:
        """Forget session state; persisted user credentials require explicit deletion."""
        if self.vault and self.profile.credential_ref and not self.persistent_active:
            self.vault.delete(self.profile.credential_ref)
            self.profile = ModelProfile()

    def _repository(self) -> Any:
        """Lazily open the injected user-local store; construction performs no IO."""
        if self.store_factory is None:
            raise ValueError("Saved profiles are unavailable")
        if self.store is None:
            from .credentials import DeferredCredentialVault

            self.vault = self.vault or DeferredCredentialVault(self.vault_factory)
            self.store = self.store_factory(self.vault)
        return self.store

    def saved_choices(self) -> list[tuple[str, str]]:
        """Expose only names and opaque IDs, never credential values or references."""
        return [("New profile", "")] + [
            (record["name"], record["id"]) for record in self._repository().list()
        ]

    def select_saved(self, identity: str) -> dict[str, Any] | None:
        """Select a validated record for this session without activating its model."""
        ensure_configurable(self.controller)
        record = self._repository().get(identity) if identity else None
        self.saved_id = identity
        self.saved_version = record["version"] if record else None
        return record

    def save_profile(self, name: str, provider: str, model: str, endpoint: str, key: str) -> str:
        """Save selected metadata/key without giving remote data-transfer consent."""
        ensure_configurable(self.controller)
        from .profile_errors import ProfileError

        try:
            saved = self._repository().save(
                name, provider, model, endpoint, key, self.saved_id, self.saved_version
            )
        except OSError as error:
            raise ProfileError("metadata_write", getattr(error, "winerror", None)) from None
        self.saved_id, self.saved_version = saved["id"], saved["version"]
        return (
            "Profile saved. Apply model to use these local settings."
            if provider == "Ollama"
            else "Profile saved. Activate it only after reviewing remote data consent."
        )

    def delete_profile(self) -> str:
        """Delete the selected inactive profile; never silently stop active work."""
        ensure_configurable(self.controller)
        if not self.saved_id:
            raise ValueError("Select a saved profile to delete")
        if self.persistent_active and self.profile.credential_ref.startswith(
            "AgentiX/v3/" + self.saved_id + "/"
        ):
            raise ValueError("Switch to Ollama before deleting the active profile")
        self._repository().delete(self.saved_id, self.saved_version)
        self.saved_id, self.saved_version = "", None
        return "Profile and owned credentials deleted. Active clients in other sessions require a model change; provider revocation is separate."


class RemoteRequestPolicy:
    """Recheck approved origins and DNS before each credential-bearing request.

    Resolution and connection are distinct OS operations; a hostile DNS service
    can still race them. An outbound enforcing proxy is needed to remove that gap.
    """

    def __init__(self, profile: ModelProfile, resolver: Callable = resolve_addresses) -> None:
        """Retain nonsecret approved endpoint data and the resolver boundary."""
        self.profile, self.resolver = profile, resolver

    def validate_url(self, destination: str) -> None:
        """Deny changed origins, paths, credentials or private resolution."""
        self.profile.validate(self.resolver)
        approved, target = urlsplit(self.profile.endpoint), urlsplit(destination)
        if (
            (target.scheme, target.hostname, target.port)
            != (approved.scheme, approved.hostname, approved.port)
            or target.username
            or target.password
            or target.query
            or target.fragment
        ):
            raise ValueError("Provider request destination was not approved")
        prefix = approved.path.rstrip("/") + "/"
        if not target.path.startswith(prefix) or ".." in target.path or "%" in target.path:
            raise ValueError("Provider request path was not approved")

    def validate_response(self, status: int) -> None:
        """Never follow provider redirects or forward credentials to a new origin."""
        if 300 <= status < 400:
            raise ValueError("Provider redirects are not allowed")


def remote_interceptor(profile: ModelProfile, resolver: Callable) -> Any:
    """Construct the installed CrewAI sync/async transport hook lazily.

    CrewAI builds explicit HTTP transports for interceptors; HTTPX disables
    environment proxy discovery when an explicit transport is supplied. This
    integration is covered separately from offline policy checks.
    """
    from crewai.llms.hooks.base import BaseInterceptor

    policy = RemoteRequestPolicy(profile, resolver)

    class Guard(BaseInterceptor):
        """Guard both synchronous and asynchronous provider network operations."""

        def on_outbound(self, message: Any) -> Any:
            """Validate the final URL before transport sends headers and body."""
            policy.validate_url(str(message.url))
            return message

        def on_inbound(self, message: Any) -> Any:
            """Reject redirects before the client can process them."""
            policy.validate_response(message.status_code)
            return message

        async def aon_outbound(self, message: Any) -> Any:
            """Apply the identical outbound policy to asynchronous calls."""
            return self.on_outbound(message)

        async def aon_inbound(self, message: Any) -> Any:
            """Apply the identical response policy to asynchronous calls."""
            return self.on_inbound(message)

    return Guard()


def installed_models(endpoint: str, reader: Callable | None = None) -> list[str]:
    """Read installed names from loopback /api/tags; never pull or run a model.

    Ignore environment proxies, reject redirects, bound response bytes and timeout.
    Reader injection supports deterministic offline tests without local services.
    """
    import json
    from urllib.request import HTTPRedirectHandler, ProxyHandler, build_opener

    ModelProfile(endpoint=endpoint).validate()

    class NoRedirects(HTTPRedirectHandler):
        """Deny all redirects away from the selected local Ollama origin."""

        def redirect_request(
            self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str
        ) -> None:
            """Return no replacement request, causing urllib to deny redirection."""
            return None

    def read(url: str) -> dict[str, Any]:
        """Read one bounded JSON document from the fixed local endpoint."""
        with build_opener(ProxyHandler({}), NoRedirects()).open(url, timeout=5) as response:
            payload = response.read(1048577)
        if len(payload) > 1048576:
            raise ValueError("Ollama response exceeded the size limit")
        return json.loads(payload)

    try:
        data = (reader or read)(endpoint.rstrip("/") + "/api/tags")
        if (
            not isinstance(data, dict)
            or not isinstance(data.get("models"), list)
            or len(data["models"]) > 1024
        ):
            raise ValueError("Invalid model catalog")
        names = set()
        for item in data["models"]:
            if not isinstance(item, dict) or not isinstance(item.get("name"), str):
                continue
            name = item["name"]
            try:
                ModelProfile(model=name).validate()
            except ValueError:
                continue
            names.add(name)
        return sorted(names)
    except Exception:
        raise ValueError(
            "Installed models could not be read. Check that local Ollama is running."
        ) from None
