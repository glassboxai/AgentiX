"""Shared parent/native application theme factory; all custom rules live in CSS."""

from typing import Any


def create_theme(gr: Any) -> Any:
    """Create the same local-only theme for host and isolated Gradio composition."""
    return gr.themes.Base(
        primary_hue="cyan",
        secondary_hue="slate",
        font=["Inter", "Arial", "sans-serif"],
        font_mono=["Inter", "Arial", "sans-serif"],
    )
