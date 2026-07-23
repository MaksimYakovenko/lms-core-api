from __future__ import annotations

import os
from typing import Sequence

# Utility function
def files_modified(file_paths: Sequence[str]) -> bool:
    """Check whether the given file list contains only the README.md file."""
    return all(os.path.normpath(file_path) == os.path.normpath('docs/README.md') for file_path in file_paths)

# Example invocation for testing purposes
if __name__ == "__main__":
    # Simulated list of changed files
    changed_files = ["docs/README.md", "src/main.py"]
    if not files_modified(changed_files):
        print("Error: Files outside 'docs/README.md' have been modified.")
    else:
        print("All modifications restricted to 'docs/README.md'.")
