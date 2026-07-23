import pytest
from docs.check_readme_changes import check_readme_changes

def test_check_readme_changes_only_readme():
    """Test that when only 'docs/README.md' is changed, the function returns True."""
    changed_files = ["docs/README.md"]
    assert check_readme_changes(changed_files) == True

def test_check_readme_changes_extra_files():
    """Test that when additional files outside 'docs/README.md' are changed, the function returns False."""
    changed_files = ["docs/README.md", "script.py"]
    assert check_readme_changes(changed_files) == False

def test_check_readme_changes_no_files():
    """Test that when no files are provided, the function returns False."""
    changed_files = []
    assert check_readme_changes(changed_files) == False

def test_check_readme_changes_different_files():
    """Test that when files other than 'docs/README.md' are changed, the function returns False."""
    changed_files = ["docs/other_document.md"]
    assert check_readme_changes(changed_files) == False