"""Only recorded owned empty AppContainer residues may be removed."""

import pytest


def service(tmp_path):
    """Resolve the cleanup implementation without loading Windows native APIs."""
    try:
        from agentix.sandbox.profile_cleanup import ProfileCleanup
    except ImportError:
        pytest.fail("Owned AppContainer residual cleanup is not implemented")
    return ProfileCleanup(tmp_path / "Packages", tmp_path / "pending")


def test_empty_owned_residue_is_removed_after_release(tmp_path):
    """Catch successful native profile deletion still leaving empty AC/Temp trees."""
    cleanup = service(tmp_path)
    name = "Agentix.v5." + "a" * 32
    folder = tmp_path / "Packages" / name
    (folder / "AC/Temp").mkdir(parents=True)
    cleanup.track(name)
    assert cleanup.release(name)
    assert not folder.exists()
    assert not list((tmp_path / "pending").glob("*.json"))


def test_nonempty_and_unowned_profiles_are_preserved(tmp_path):
    """Never delete user files or another AgentiX version's sandbox."""
    cleanup = service(tmp_path)
    name = "Agentix.v5." + "b" * 32
    folder = tmp_path / "Packages" / name
    folder.mkdir(parents=True)
    (folder / "diagnostic.txt").write_text("keep")
    cleanup.track(name)
    assert not cleanup.release(name)
    assert (folder / "diagnostic.txt").read_text() == "keep"
    with pytest.raises(ValueError):
        cleanup.track("Agentix." + "c" * 32)


def test_active_owner_is_never_recovered(tmp_path):
    """Recovery must preserve another live process's recorded profile."""
    cleanup = service(tmp_path)
    name = "Agentix.v5." + "d" * 32
    folder = tmp_path / "Packages" / name
    folder.mkdir(parents=True)
    cleanup.track(name)
    cleanup.recover(lambda pid: True, lambda name: True)
    assert folder.exists()
    cleanup.recover(lambda pid: False, lambda name: False)
    assert folder.exists()
    cleanup.recover(lambda pid: False, lambda name: True)
    assert not folder.exists()
