"""Intentional legacy combined callback facade; new shell uses separate backends."""

from agentix.controllers.sidebar import SidebarBackend
from agentix.controllers.tools import ToolsBackend


class SessionCallbacks(ToolsBackend):
    """Preserve prior imports while keeping sidebar implementations in their own module."""

    configure_model = SidebarBackend.configure_model
    model_menu = SidebarBackend.model_menu
    refresh_models = SidebarBackend.refresh_models
