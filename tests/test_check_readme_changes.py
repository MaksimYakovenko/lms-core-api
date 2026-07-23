from __future__ import annotations

def test_files_modified() -> None:
    from check_readme_changes import files_modified

    # Test cases
    assert files_modified(["docs/README.md"])
    assert not files_modified(["docs/README.md", "src/main.py"])
    assert not files_modified(["src/app.py"])
    assert not files_modified([]) # No files modified
    assert files_modified(["docs\\README.md","docs/README.md"])
    # Simulate situation with normalized paths, particularly in cross-platform scenarios.
