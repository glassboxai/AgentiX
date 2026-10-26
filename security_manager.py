"""Compatibility exports for the extracted approval/path/storage facade."""

import _agentix_path
from agentix.security import SecurityManager, SecurityViolationError

__all__ = ["SecurityManager", "SecurityViolationError"]
