from __future__ import annotations

from docs.check_readme_changes import check_readme_changes

def test_check_readme_single_file() -> None:
    """Test if only modifying 'docs/README.md' returns True."""
    assert check_readme_changes(["docs/README.md"]) is True

def test_check_readme_multiple_files() -> None:
    """Test if modifying additional files returns False."""
    assert check_readme_changes(["docs/README.md", "src/main.py"]) is False

def test_check_readme_with_empty_list() -> None:
    """Test if providing an empty list returns False."""
    assert check_readme_changes([]) is False
