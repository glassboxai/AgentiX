"""Verify source reference completeness and synchronization without importing source."""

from pathlib import Path

from tools.build_reference import build_documents, scan_source


def test_inventory_documents_parameters_attributes_locals_and_types(tmp_path):
    """Preserve lexical ownership and declared types without publishing values."""
    source = tmp_path / "sample.py"
    source.write_text(
        '''"""Trusted source fixture."""
class Example:
    """Own an explicit resource."""
    def update(self, count: int) -> int:
        """Return the next count."""
        self.count = count
        next_count = count + 1
        return next_count
''',
        encoding="utf-8",
    )
    inventory = scan_source(source, "sample.py")
    names = {(item["scope"], item["name"]) for item in inventory["variables"]}
    assert ("Example.update", "count") in names
    assert ("Example.update", "self.count") in names
    assert ("Example.update", "next_count") in names
    assert inventory["symbols"][1]["returns"] == "int"


def test_reference_check_detects_source_changes_and_never_reads_excluded_storage(tmp_path):
    """Keep authored temporary generated storage outside reference discovery."""
    folder = tmp_path / "src"
    folder.mkdir()
    source = folder / "sample.py"
    source.write_text('"""Documented fixture."""\ncount = 1\n', encoding="utf-8")
    excluded = tmp_path / "generated_tools"
    excluded.mkdir()
    (excluded / "unreadable.py").write_text("invalid python !", encoding="utf-8")
    assert build_documents(tmp_path) == []
    assert build_documents(tmp_path, check=True) == []
    source.write_text('"""Changed contract."""\ncount = 2\n', encoding="utf-8")
    assert build_documents(tmp_path, check=True)


def test_release_reference_is_current():
    """Fail the offline suite whenever source and maintained reference diverge."""
    root = Path(__file__).resolve().parents[2]
    assert build_documents(root, check=True) == []
