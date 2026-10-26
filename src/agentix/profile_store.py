"""User-owned nonsecret model profiles with Windows credential references.

Writes use an interprocess lock and atomic metadata replacement. Credential and
file services are not a transactional database: cleanup references are retained
for retry, while a failed metadata commit keeps the old profile authoritative.
Same-user malware is outside the Windows credential/user filesystem boundary.
"""

import json
import logging
import os
import re
import tempfile
import threading
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from uuid import uuid4

from .diagnostics import log_event
from .model_profiles import ModelProfile, resolve_addresses
from .profile_errors import ProfileError

logger = logging.getLogger(__name__)


class SavedProfiles:
    """Persist a bounded catalog; keys live exclusively in an injected vault."""

    def __init__(
        self, directory: Path, vault: Any, *, resolver: Callable = resolve_addresses
    ) -> None:
        """Retain user-local location and external boundaries without creating files."""
        self.directory, self.vault, self.resolver = Path(directory), vault, resolver
        self._lock = threading.RLock()

    def _path(self, identity: str) -> Path:
        """Reject path input and reparse ancestors before accessing owned metadata."""
        if not isinstance(identity, str) or not re.fullmatch(r"[a-f0-9]{32}", identity):
            raise ValueError("Invalid saved profile identifier")
        target = self.directory / (identity + ".json")
        self._check_path(target)
        return target

    @staticmethod
    def _check_path(target: Path) -> None:
        """Deny existing reparse components; never follow metadata links."""
        for path in (target, *target.parents):
            try:
                state = path.lstat()
            except FileNotFoundError:
                continue
            if path.is_symlink() or getattr(state, "st_file_attributes", 0) & 0x400:
                raise ProfileError("profile_link")

    def get(self, identity: str) -> dict[str, Any]:
        """Read validated bounded metadata; never read a credential value."""
        try:
            with self._path(identity).open("rb") as stream:
                raw = stream.read(65537)
            if len(raw) > 65536:
                raise ValueError("Saved profile is oversized")
            record = json.loads(raw)
            fields = {
                "id",
                "version",
                "name",
                "provider",
                "model",
                "endpoint",
                "credential_ref",
                "retired_refs",
            }
            if (
                not isinstance(record, dict)
                or set(record) != fields
                or record["id"] != identity
                or type(record["version"]) is not int
                or record["version"] < 1
            ):
                raise ValueError("Invalid saved profile metadata")
            self._validate_name(record["name"])
            if record["provider"] not in ("Ollama", "OpenAI", "OpenAI-compatible"):
                raise ProfileError("metadata_invalid")
            # Consent is intentionally not persisted. Do not resolve DNS on reads.
            ModelProfile(
                record["provider"], record["model"], record["endpoint"], remote_consent=True
            ).validate(lambda host: ["93.184.216.34"])
            reference = record["credential_ref"]
            if (
                not isinstance(reference, str)
                or (record["provider"] == "Ollama" and reference)
                or (record["provider"] != "Ollama" and not reference)
            ):
                raise ProfileError("metadata_invalid")
            references = ([reference] if reference else []) + record["retired_refs"]
            if (
                not isinstance(record["retired_refs"], list)
                or len(references) > 65
                or any(
                    not isinstance(ref, str)
                    or not re.fullmatch(r"AgentiX/v3/" + identity + r"/[a-f0-9]{32}", ref)
                    for ref in references
                )
            ):
                raise ValueError("Saved credential ownership does not match profile")
            return record
        except (OSError, TypeError, KeyError, json.JSONDecodeError, UnicodeError):
            raise ProfileError("metadata_invalid") from None

    @staticmethod
    def _validate_name(name: str) -> None:
        """Limit display names to readable nonmarkup characters."""
        if (
            not isinstance(name, str)
            or not 1 <= len(name.strip()) <= 64
            or any(not character.isprintable() or character in "<>&`" for character in name)
        ):
            raise ProfileError("profile_name")

    def list(self) -> list[dict[str, Any]]:
        """List bounded validated metadata; corruption is reported rather than hidden."""
        self._check_path(self.directory)
        paths = []
        for path in self.directory.glob("*.json"):
            paths.append(path)
            if len(paths) > 64:
                raise ValueError("Saved profile capacity exceeded")
        return sorted(
            [self.get(path.stem) for path in paths],
            key=lambda item: (item["name"].casefold(), item["id"]),
        )

    @contextmanager
    def _exclusive(self) -> Iterator[None]:
        """Serialize writes across processes; fail after five seconds of contention."""
        with self._lock:
            self._check_path(self.directory / "profiles.lock")
            self.directory.mkdir(parents=True, exist_ok=True)
            with (self.directory / "profiles.lock").open("a+b") as stream:
                stream.seek(0, 2)
                if stream.tell() == 0:
                    stream.write(b"0")
                    stream.flush()
                deadline = time.monotonic() + 5
                while True:
                    try:
                        stream.seek(0)
                        if os.name == "nt":
                            import msvcrt

                            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                        else:
                            import fcntl

                            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        break
                    except OSError:
                        if time.monotonic() >= deadline:
                            raise ProfileError("profile_busy") from None
                        time.sleep(0.05)
                try:
                    yield
                finally:
                    stream.seek(0)
                    if os.name == "nt":
                        msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                    else:
                        fcntl.flock(stream, fcntl.LOCK_UN)

    def _commit(self, record: dict[str, Any]) -> None:
        """Replace one metadata file atomically; never include API key values."""
        target = self._path(record["id"])
        descriptor, temporary = tempfile.mkstemp(
            prefix=".profile-", suffix=".tmp", dir=self.directory
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(record, stream)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, target)
        finally:
            Path(temporary).unlink(missing_ok=True)

    def save(
        self,
        name: str,
        provider: str,
        model: str,
        endpoint: str,
        key: str,
        identity: str = "",
        version: int | None = None,
    ) -> dict[str, Any]:
        """Create/update metadata and credentials, rejecting stale edits before IO.

        Empty keys retain an existing credential. New keys get new opaque targets;
        a failed commit removes the candidate and leaves the original untouched.
        Cleanup failures retain old references for retry on update or deletion.
        """
        self._validate_name(name)
        name = name.strip()
        remote = provider != "Ollama"
        try:
            ModelProfile(provider, model, endpoint, remote_consent=True).validate(self.resolver)
        except ValueError:
            raise ProfileError("model_settings") from None
        with self._exclusive():
            old = self.get(identity) if identity else None
            if old and (type(version) is not int or old["version"] != version):
                raise ProfileError("profile_changed")
            if not old and len(self.list()) >= 64:
                raise ProfileError("profile_capacity")
            if remote and not key and (not old or not old["credential_ref"]):
                raise ProfileError("key_required")
            identity = identity or uuid4().hex
            write_key = remote and bool(key)
            reference = (
                (f"AgentiX/v3/{identity}/{uuid4().hex}" if write_key else old["credential_ref"])
                if remote
                else ""
            )
            retired = list(old["retired_refs"]) if old else []
            if old and old["credential_ref"] and old["credential_ref"] != reference:
                retired.append(old["credential_ref"])
            if len(retired) > 64:
                raise ValueError("Credential cleanup is required before another update")
            record = dict(
                id=identity,
                version=(old["version"] + 1 if old else 1),
                name=name,
                provider=provider,
                model=model,
                endpoint=endpoint,
                credential_ref=reference,
                retired_refs=retired,
            )
            phase = "credential_write" if write_key else "metadata_write"
            try:
                if write_key:
                    self.vault.write(reference, key)
                phase = "metadata_write"
                self._commit(record)
            except Exception as error:
                log_event(
                    logger,
                    "profile_save_failed",
                    error=error,
                    request_id=phase,
                    level=logging.ERROR,
                )
                if write_key:
                    try:
                        self.vault.delete(reference)
                    except Exception as cleanup_error:
                        log_event(
                            logger,
                            "credential_candidate_cleanup_failed",
                            error=cleanup_error,
                            level=logging.ERROR,
                        )
                if isinstance(error, ProfileError):
                    raise error from None
                raise ProfileError(phase, getattr(error, "winerror", None)) from None
            remaining = []
            for obsolete in retired:
                try:
                    self.vault.delete(obsolete)
                except Exception as error:
                    remaining.append(obsolete)
                    log_event(
                        logger, "credential_cleanup_deferred", error=error, level=logging.ERROR
                    )
            if remaining != retired:
                record["retired_refs"] = remaining
                try:
                    self._commit(record)
                except OSError as error:
                    log_event(
                        logger,
                        "credential_cleanup_metadata_failed",
                        error=error,
                        level=logging.ERROR,
                    )
            log_event(logger, "model_profile_saved")
            return record

    def delete(self, identity: str, version: int) -> None:
        """Remove exactly the selected profile and its owned credential targets.

        A partial vault failure leaves metadata for an explicit retry. Existing
        active SDK clients can retain their already loaded credential in memory.
        """
        with self._exclusive():
            record = self.get(identity)
            if type(version) is not int or record["version"] != version:
                raise ProfileError("profile_changed")
            try:
                for reference in (
                    [record["credential_ref"]] if record["credential_ref"] else []
                ) + record["retired_refs"]:
                    self.vault.delete(reference)
                self._path(identity).unlink()
            except Exception:
                raise ValueError(
                    "Profile deletion incomplete; retry the explicit deletion"
                ) from None
            log_event(logger, "model_profile_deleted")
