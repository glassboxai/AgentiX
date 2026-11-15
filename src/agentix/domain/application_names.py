"""Human application names and safe deterministic Windows directory names."""

import re
import unicodedata

# Display-name bound and the Windows device names that cannot be folder names.
MAX_APPLICATION_NAME_LENGTH = 100
RESERVED_DEVICE_NAMES = frozenset(
    {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        *[f"COM{i}" for i in range(1, 10)],
        *[f"LPT{i}" for i in range(1, 10)],
    }
)


def application_folder(name: str) -> str:
    """Validate a display name and derive a non-device ASCII folder name.

    Paths, trailing punctuation, empty names and Windows devices are rejected.
    The catalog reserves the derived folder without overwriting prior packages.
    """
    if (
        not isinstance(name, str)
        or not 1 <= len(name) <= MAX_APPLICATION_NAME_LENGTH
        or name != name.strip()
    ):
        raise ValueError("Application name must contain 1 to 100 characters")
    if not all(c.isalnum() or c in " _-" for c in name):
        raise ValueError("Application name contains unsupported characters")
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    folder = re.sub(r"[ _-]+", "-", ascii_name.lower()).strip("-")
    if not folder or folder.upper() in RESERVED_DEVICE_NAMES:
        raise ValueError("Choose a different application name")
    return folder
