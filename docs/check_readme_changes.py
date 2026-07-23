from __future__ import annotations

from collections.abc import Iterable

def check_readme_changes(changed_files: Iterable[str]) -> bool:
    """Verify if the provided file list contains only 'docs/README.md'.

    Parameters:
    - changed_files: An iterable of file paths that have been modified.

    Returns:
    - A boolean indicating if the only file modified is 'docs/README.md'.
    """
    # Evaluate if the modified files are limited to the specified file
    return set(changed_files) == {"docs/README.md"}

if __name__ == "__main__":
    print(check_readme_changes(["docs/README.md"]))  # Expected: True
    print(check_readme_changes(["docs/README.md", "other_file.py"]))  # Expected: False
