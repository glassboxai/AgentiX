"""Closed, payload-free profile errors suitable for user-facing diagnostics."""

MESSAGES = {
    "key_format": "API credential format is invalid. Paste only the key: 8 to 2048 printable ASCII characters, without whitespace.",
    "key_capacity": "Credential redaction capacity is reached. Start a new application process before adding another distinct key.",
    "key_storage_limit": "API credential exceeds the Windows vault storage limit for this encoding.",
    "credential_unavailable": "Windows Credential Manager is unavailable. Local profiles remain usable.",
    "credential_write": "Windows Credential Manager could not save the credential. The previous profile is retained.",
    "credential_read": "Saved credential is unavailable. Re-enter and save its key before activation.",
    "credential_delete": "Windows Credential Manager could not remove an owned credential. Retry deletion.",
    "metadata_write": "Profile metadata could not be written. Check free space and permissions; the previous profile is retained.",
    "metadata_invalid": "Saved profile metadata is unavailable or invalid. Existing files were not overwritten.",
    "profile_name": "Profile name must contain 1 to 64 printable characters, without markup or control characters.",
    "model_settings": "Provider, model or endpoint settings are invalid or could not be verified. Check the selected provider and endpoint.",
    "key_required": "A new external profile requires an API key. Local Ollama profiles do not.",
    "profile_changed": "Saved profile changed; reload it before updating or deleting.",
    "profile_capacity": "Saved profile capacity is reached. Delete an unused profile first.",
    "profile_link": "Profile storage must not contain filesystem links.",
    "profile_busy": "Profile storage is busy. Retry after the other operation finishes.",
}


class ProfileError(ValueError):
    """Carry only a closed reason code and optional numeric Windows status.

    No caller-supplied message, key, URL, path or vendor exception body is stored.
    The UI may display this exception's text; other exceptions remain private.
    """

    def __init__(self, code: str, system_code: int | None = None) -> None:
        """Validate fixed diagnostic fields and construct a safe public message."""
        if code not in MESSAGES:
            raise ValueError("Unknown profile diagnostic code")
        self.code = code
        self.system_code = (
            system_code if type(system_code) is int and 0 <= system_code <= 4294967295 else None
        )
        message = f"[{code}] {MESSAGES[code]}"
        if self.system_code is not None:
            message += f" Windows error code: {self.system_code}."
        super().__init__(message)
