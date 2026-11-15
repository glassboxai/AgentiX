"""Stage or apply explicitly reviewed application runtime/dependency updates."""

import argparse
import json
import os
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(PROJECT / "src"))

from agentix.security.data_protection import WindowsDataProtection  # noqa: E402
from agentix.storage.application_update import ApplicationUpdates  # noqa: E402
from agentix.storage.catalog_migration import CatalogMigration  # noqa: E402
from tools.migrate_catalog import verify_application  # noqa: E402


def main() -> int:
    """Plan without installed writes, or apply one exact operator-reviewed plan.

    Source/target paths must be explicit. No model calls, app renaming, generated
    logic edits, case inference or current-grant overwrites are supported.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-home", type=Path, required=True)
    parser.add_argument("--source-tools", type=Path, required=True)
    parser.add_argument("--target-home", type=Path, required=True)
    parser.add_argument("--application", action="append", required=True)
    parser.add_argument("--review-digest", help="Exact digest of the reviewed update plan")
    args = parser.parse_args()
    os.environ["AGENTIX_HOME"] = str(args.target_home)
    os.environ["AGENTIX_TOOLS_ROOT"] = str(args.target_home / "data/tools")
    migration = CatalogMigration(
        args.source_home, args.source_tools, args.target_home, protector=WindowsDataProtection()
    )
    service = ApplicationUpdates(migration)
    result = (
        service.apply(args.application, args.review_digest, verifier=verify_application)
        if args.review_digest
        else service.plan(args.application)
    )
    print(json.dumps(result, indent=2))
    return 2 if any(item["status"] == "blocked" for item in result["items"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
