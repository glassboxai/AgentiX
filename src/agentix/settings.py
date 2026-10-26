"""Immutable settings loaded without initializing external services or storage."""

import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Runtime inputs; constructing settings never creates their target paths.

    Attributes:
        base_dir: Application checkout root, independent of the working directory.
        tools_root: Artifact storage root used only when services are invoked.
        model: CrewAI model identifier, including the existing Ollama prefix.
        ollama_url: Existing configurable provider endpoint.
        temperature: Existing low-temperature generation setting.
        server_port: Explicit loopback TCP port; occupied ports fail without fallback.
        open_browser: Whether manual GUI launch opens the local browser.
    """

    base_dir: Path
    tools_root: Path
    model: str = "ollama/qwen3-coder:30b"
    ollama_url: str = "http://localhost:11434"
    temperature: float = 0.2
    server_port: int = 7860
    open_browser: bool = True

    @classmethod
    def from_environment(
        cls, environment: Mapping[str, str] | None = None, base_dir: Path | None = None
    ) -> "Settings":
        """Read configuration values without changing the process environment.

        An explicit base directory supports isolated tests. Defaults preserve the
        original checkout-relative storage location rather than the package path.
        """
        values = os.environ if environment is None else environment
        base = Path(base_dir) if base_dir is not None else Path(__file__).resolve().parents[2]
        port_text = values.get("AGENTIX_SERVER_PORT", "7860")
        if not port_text.isascii() or not port_text.isdigit() or not 1 <= int(port_text) <= 65535:
            raise ValueError("AGENTIX_SERVER_PORT must be an integer between 1 and 65535")
        browser_text = values.get("AGENTIX_OPEN_BROWSER", "true").lower()
        if browser_text not in ("true", "false"):
            raise ValueError("AGENTIX_OPEN_BROWSER must be true or false")
        tools = Path(values.get("AGENTIX_TOOLS_ROOT", str(base / "generated_tools")))
        if not tools.is_absolute():
            raise ValueError("AGENTIX_TOOLS_ROOT must be an absolute path")
        return cls(
            base,
            tools,
            values.get("OLLAMA_MODEL", "ollama/qwen3-coder:30b"),
            values.get("OLLAMA_BASE_URL", "http://localhost:11434"),
            server_port=int(port_text),
            open_browser=browser_text == "true",
        )
