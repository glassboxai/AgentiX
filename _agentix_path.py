"""Allow legacy checkout entrypoints to locate the src-layout package.

Installed applications resolve agentix normally; a checkout needs only its local
src directory added to Python's module path, without runtime initialization.
"""

import sys
from pathlib import Path

source_directory = str(Path(__file__).resolve().parent / "src")
if source_directory not in sys.path:
    sys.path.insert(0, source_directory)
