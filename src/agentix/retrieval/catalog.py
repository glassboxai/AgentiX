"""Read the GUI catalog's explicit root into bounded AST-only search descriptors.

No directory is guessed and no generated Python is imported or executed. This
adapter accepts the same ToolCatalog instance/root as the GUI. Scans are read-only;
filesystem changes after a scan become visible on the next synchronization.
"""

import hashlib
import os
import stat
from dataclasses import replace
from itertools import islice
from pathlib import Path

from agentix.storage.catalog import ToolCatalog
from agentix.storage.catalog_lock import reject_alias

from . import policy
from .contracts import CatalogRejection, CatalogSnapshot, descriptor_from_source


def _stamp(value: os.stat_result) -> tuple[int, ...]:
    """Identify an opened file version to detect ordinary replacement/write races."""
    return value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns


class CatalogToolSource:
    """Adapt canonical installed functions from an explicitly injected GUI catalog.

    Invalid tools are reported, while directory/read failures abort the snapshot.
    Alias and size checks bound metadata reads; they are not execution isolation
    or a guarantee against a hostile process racing filesystem checks.
    """

    def __init__(self, catalog: ToolCatalog) -> None:
        """Remember an absolute catalog root without enumerating or executing tools."""
        self.catalog = catalog
        self.root = Path(catalog.root)
        if not self.root.is_absolute():
            raise ValueError("Catalog source requires an absolute root")
        reject_alias(self.root)
        normalized = os.path.normcase(str(self.root.resolve()))
        self.identity = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    @staticmethod
    def _read(source: Path) -> bytes:
        """Read bounded regular unaliased bytes, rejecting changed versions and hard links.

        Raise ValueError for unsafe paths, OverflowError for oversized source and
        OSError when a complete stable read cannot be established. No source runs.
        """
        reject_alias(source)
        before = source.stat(follow_symlinks=False)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError("Unsafe catalog source")
        if before.st_size > policy.MAX_CATALOG_SOURCE_BYTES:
            raise OverflowError("Catalog source exceeds read bound")
        with source.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            if _stamp(before) != _stamp(opened):
                raise OSError("Catalog source changed during scan")
            raw = stream.read(policy.MAX_CATALOG_SOURCE_BYTES + 1)
            after = os.fstat(stream.fileno())
        reject_alias(source)
        current = source.stat(follow_symlinks=False)
        if _stamp(before) != _stamp(after) or _stamp(after) != _stamp(current):
            raise OSError("Catalog source changed during scan")
        if len(raw) > policy.MAX_CATALOG_SOURCE_BYTES:
            raise OverflowError("Catalog source exceeds read bound")
        return raw

    def snapshot(self) -> CatalogSnapshot:
        """Return a full source snapshot or propagate directory/read errors.

        Missing roots fail explicitly; existing empty roots represent deletion of
        all tools. Canonical parse errors, aliases and oversized files are reported
        as rejected entries, so stale descriptors are removed during synchronization.
        """
        if Path(self.catalog.root) != self.root:
            raise ValueError("Catalog source root changed; bind a new source")
        reject_alias(self.root)
        entries = list(islice(self.root.iterdir(), policy.MAX_CATALOG_ENTRIES + 1))
        if len(entries) > policy.MAX_CATALOG_ENTRIES:
            raise ValueError("Catalog source exceeds entry bound")
        descriptors, rejected = [], []
        for folder in sorted(entries):
            source = folder / f"{folder.name}_code.py"
            try:
                reject_alias(folder)
                if not folder.is_dir():
                    continue
                reject_alias(source)
            except ValueError:
                rejected.append(CatalogRejection(folder.name, "unsafe_path"))
                continue
            if not self.catalog.contains(folder.name):
                rejected.append(CatalogRejection(folder.name, "missing_or_invalid_entry"))
                continue
            try:
                raw = self._read(source)
            except ValueError:
                rejected.append(CatalogRejection(folder.name, "unsafe_path"))
                continue
            except OverflowError:
                rejected.append(CatalogRejection(folder.name, "source_limit"))
                continue
            try:
                descriptor = descriptor_from_source(
                    folder.name, raw.decode("utf-8-sig"), artifact_ref=folder.name
                )
            except (SyntaxError, UnicodeError):
                rejected.append(CatalogRejection(folder.name, "invalid_source"))
                continue
            except ValueError:
                rejected.append(CatalogRejection(folder.name, "unsupported_contract"))
                continue
            descriptors.append(replace(descriptor, contract_digest=hashlib.sha256(raw).hexdigest()))
        reject_alias(self.root)
        return CatalogSnapshot(tuple(descriptors), tuple(rejected))
