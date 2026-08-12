from __future__ import annotations

import sys
import subprocess
import json

def verify_changes() -> None:
    """Check that only the README.md file is being modified."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--cached'],
            text=True, check=True, capture_output=True
        )
        changed_files = result.stdout.strip().splitlines()
        if not all(file == "README.md" for file in changed_files):
            print("Error: Only changes to README.md are permitted.", file=sys.stderr)
            sys.exit(1)
        print("Change verification finished successfully.")
    except subprocess.CalledProcessError as error:
        print(f"Error during subprocess execution: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    verify_changes()
