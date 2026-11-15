"""Owner-scoped widget style window backend; persistence stays in the review service.

The backend only resolves the caller's own proposal, reads the scoped stylesheet and
merges the six edited declarations. Writing goes through
:meth:`ApplicationsBackend.save_file`, so the revocation rule and the ownership lock
keep exactly one implementation.
"""

import json
import logging
from typing import Any

from agentix.application.style_member import style_member_name
from agentix.widgets.style_editor import StyleValues, merge_style, read_style

logger = logging.getLogger(__name__)


class WidgetStyleBackend:
    """Load and save the editable declarations of one widget stylesheet."""

    def __init__(self, applications: Any) -> None:
        """Bind the applications backend that owns proposals and their lock."""
        self.applications = applications

    def load(self, tool: str, token: str | None, request: Any) -> tuple:
        """Return the window's initial values for the widget the owner right-clicked."""
        session, _, candidate = self.applications.owned_candidate(token, request)
        name = style_member_name(tool)
        css = (candidate.package / name).read_text(encoding="utf-8")
        values = read_style(css, tool)
        logger.info("session=%s event=widget_style_opened tool=%s", session.session_id, tool)
        return (
            f"Editing `{name}`. Saving keeps the current approval valid.",
            values.radius,
            values.width,
            values.border_color,
            values.background,
            values.font_family,
            values.font_size,
            values.field_background,
            values.label_font_family,
            values.label_font_size,
            session.token,
        )

    def save(
        self,
        tool: str,
        radius: float,
        width: float,
        border_color: str,
        background: str,
        font_family: str,
        font_size: float,
        field_background: str,
        label_font_family: str,
        label_font_size: float,
        token: str | None,
        request: Any,
    ) -> tuple[str, str]:
        """Merge the edited values into the scoped stylesheet and persist them.

        Raises ``ValueError`` for an unknown widget, an out-of-range value or a busy
        session. Returns the persistence message, the refreshed session token and the
        merged stylesheet as a JSON payload the parent bridge applies to the live
        preview, so the widget changes without reopening it.
        """
        session, _, candidate = self.applications.owned_candidate(token, request)
        name = style_member_name(tool)
        css = (candidate.package / name).read_text(encoding="utf-8")
        values = StyleValues(
            int(radius),
            int(width),
            border_color,
            background,
            font_family,
            int(font_size),
            field_background,
            label_font_family,
            int(label_font_size),
        )
        merged = merge_style(css, tool, values)
        message, _, _, _, _, token_out = self.applications.save_file(
            name, merged, candidate.identity, token, request
        )
        logger.info("session=%s event=widget_style_saved tool=%s", session.session_id, tool)
        return (
            message,
            token_out,
            json.dumps(
                {"tool": tool, "ids": self._instance_ids(candidate.package, tool), "css": merged}
            ),
        )

    @staticmethod
    def _instance_ids(package: Any, tool: str) -> list[str]:
        """Map one tool to the widget instance ids the preview scopes its CSS to."""
        try:
            manifest = json.loads((package / "application.json").read_text(encoding="utf-8"))
            ids = [
                node["id"]
                for node in manifest.get("widgets", [])
                if isinstance(node, dict) and node.get("tool") == tool
            ]
        except (OSError, ValueError, KeyError, TypeError):
            ids = []
        return ids or [tool]
