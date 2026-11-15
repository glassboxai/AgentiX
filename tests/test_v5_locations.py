"""Storage location regressions must not adopt packaged-host v4 or legacy v5 data."""

import pytest

from agentix.settings import Settings


def test_missing_home_never_falls_back_to_the_v5_profile(tmp_path):
    """A missing AGENTIX_HOME must fail instead of resolving the retired v5 root."""
    values = {"USERPROFILE": str(tmp_path), "LOCALAPPDATA": str(tmp_path / "virtualized")}
    with pytest.raises(ValueError, match="AGENTIX_HOME"):
        Settings.from_environment(values, base_dir=tmp_path / "checkout")


def test_explicit_home_and_tools_root_control_storage(tmp_path):
    """Both configured roots govern storage without creating files."""
    tools = tmp_path / "checkout" / "generated_tools"
    settings = Settings.from_environment(
        {"AGENTIX_HOME": str(tmp_path / "My data"), "AGENTIX_TOOLS_ROOT": str(tools)},
        base_dir=tmp_path,
    )
    assert settings.tools_root == tools
    assert settings.data_root == tmp_path / "My data/data"
    assert not settings.tools_root.exists()


def test_missing_tools_root_is_rejected(tmp_path):
    """The published Tools root is never derived from a default home."""
    with pytest.raises(ValueError, match="AGENTIX_TOOLS_ROOT"):
        Settings.from_environment({"AGENTIX_HOME": str(tmp_path / "My data")}, base_dir=tmp_path)


@pytest.mark.parametrize("bad", ["relative", "../other", ""])
def test_relative_or_empty_home_rejected(bad, tmp_path):
    """Never resolve a user data root relative to the current checkout."""
    with pytest.raises(ValueError):
        Settings.from_environment({"AGENTIX_HOME": bad}, base_dir=tmp_path)
