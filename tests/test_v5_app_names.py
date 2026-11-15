"""Named application folders retain opaque authorization identities."""

import pytest
from test_installed_apps import library, verified


def test_named_folder_and_display_name_survive_reload(tmp_path):
    """Catch catalog entries being stored under an unreadable UUID or losing names."""
    service = library(tmp_path)
    item = verified(tmp_path)
    item.display_name = "My Text Analysis"
    app = service.publish(item)
    assert app.name == "My Text Analysis"
    assert app.package.name == "my-text-analysis"
    assert app.id != app.package.name
    assert library(tmp_path).get(app.id).name == "My Text Analysis"
    assert [x.id for x in library(tmp_path).list()] == [app.id]


@pytest.mark.parametrize("name", ["", "../escape", "CON", "Text/analysis", "name.", "a" * 101])
def test_invalid_name_never_publishes(tmp_path, name):
    """Reject traversal, Windows devices and ambiguous names before copying files."""
    service = library(tmp_path)
    item = verified(tmp_path)
    item.display_name = name
    with pytest.raises(ValueError):
        service.publish(item)
    assert service.list() == []


def test_duplicate_name_preserves_original(tmp_path):
    """Never overwrite a reviewed application when a second name collides."""
    service = library(tmp_path)
    first = verified(tmp_path / "first")
    first.display_name = "Text Analysis"
    original = service.publish(first)
    second = verified(tmp_path / "second")
    second.display_name = "text analysis"
    with pytest.raises(ValueError, match="name"):
        service.publish(second)
    assert service.get(original.id).digest == original.digest
