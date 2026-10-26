"""Verify preserved configuration values through explicit, inert settings."""

import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock

import pytest

from agentix.bootstrap import create_llm
from agentix.settings import Settings


@pytest.mark.parametrize("model,url", [(None, None), ("ollama/custom", "http://127.0.0.1:11435")])
def test_configuration_defaults_and_overrides(monkeypatch, model, url):
    """Retain model/provider values while deferring construction until requested."""
    root = Path(__file__).resolve().parents[2]
    values = {}
    if model is not None:
        values["OLLAMA_MODEL"] = model
    if url is not None:
        values["OLLAMA_BASE_URL"] = url
    settings = Settings.from_environment(values, base_dir=root)
    crew = ModuleType("crewai")
    crew.LLM = Mock()
    monkeypatch.setitem(sys.modules, "crewai", crew)
    crew.LLM.assert_not_called()
    create_llm(settings)
    crew.LLM.assert_called_once_with(
        model=model or "ollama/qwen3-coder:30b",
        base_url=url or "http://localhost:11434",
        temperature=0.2,
        timeout=120,
        max_tokens=8192,
        max_retries=0,
    )
    assert settings.tools_root == root / "generated_tools"
